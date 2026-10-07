// Text Effects Engine
// Handles word-level highlighting, dimming, focus, and transitions

const TextEffects = {
  // Current state
  activeHighlights: [],

  // Shrink primary-he / primary-en font sizes so the content fits inside the
  // panel's padded area. CSS clamp() with cqi/vh can scale to the container
  // dimensions but can't measure CONTENT height — so tall passages (long
  // primaryText, or any passage in the short mobile panel) still overflow.
  //
  // Text rewraps non-linearly as it shrinks, so instead of one proportional
  // pass this binary-searches the largest scale that fits, applied to every
  // side (comparison mode has two of each). Only if the passage still
  // overflows at the floor sizes is one language hidden — the English caption,
  // or the Hebrew on a sheet with "primaryLanguage": "en" — and the other is
  // then fit on its own.
  //
  // Idempotent: clears its own inline styles before measuring so re-runs
  // (e.g. on resize, or once web fonts load) start from the CSS baseline.
  fitToPanel(panel) {
    if (!panel) return;
    // Skip hidden panels (their clientHeight is 0 — fitting them is meaningless).
    if (panel.clientHeight === 0 || panel.offsetParent === null) return;

    const content = panel.querySelector('.primary-text-content.active');
    if (!content) return;
    if (content.classList.contains('image-mode')) {
      this.layoutImage(content);
      return;
    }
    const he = [...content.querySelectorAll('.primary-he')];
    const en = [...content.querySelectorAll('.primary-en')];
    if (!he.length && !en.length) return;

    [...he, ...en].forEach(el => {
      el.style.fontSize = ''; el.style.lineHeight = ''; el.style.display = '';
    });

    const cs = getComputedStyle(panel);
    const innerH = panel.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
    if (innerH <= 0) return;
    const fits = () => content.scrollHeight <= innerH;
    if (fits()) return;

    const sized = [
      ...he.map(el => ({ el, base: parseFloat(getComputedStyle(el).fontSize), floor: 14, lh: '1.65' })),
      ...en.map(el => ({ el, base: parseFloat(getComputedStyle(el).fontSize), floor: 12, lh: '1.6' })),
    ];
    const apply = (items, scale) => items.forEach(({ el, base, floor, lh }) => {
      el.style.fontSize = Math.max(floor, base * scale) + 'px';
      el.style.lineHeight = lh;
    });
    // Largest scale in [0, 1] at which `items` fit; 0 means "at the floors".
    const search = items => {
      let lo = 0, hi = 1;
      for (let i = 0; i < 10; i++) {
        const mid = (lo + hi) / 2;
        apply(items, mid);
        if (fits()) lo = mid; else hi = mid;
      }
      apply(items, lo);
      return fits();
    };

    if (search(sized)) return;

    // Doesn't fit even at the floors: keep the sheet's primary language
    // (Hebrew unless it sets "primaryLanguage": "en") and drop the other.
    const [keep, drop] = document.body.dataset.primaryLang === 'en' ? [en, he] : [he, en];
    drop.forEach(el => { el.style.display = 'none'; });
    search(sized.filter(s => keep.includes(s.el)));
  },

  // Wrap each word in the primary text with targetable spans
  wrapWords(container, words) {
    const heEls = container.querySelectorAll('.primary-he');
    const enEls = container.querySelectorAll('.primary-en');
    if (heEls.length === 0 && enEls.length === 0) return;

    for (const [groupId, group] of Object.entries(words)) {
      if (group.he) {
        heEls.forEach(el => this._wrapPhrase(el, group.he, groupId, 'he'));
      }
      if (group.en) {
        enEls.forEach(el => this._wrapPhrase(el, group.en, groupId, 'en'));
      }
    }
  },

  _wrapPhrase(el, phrase, groupId, lang) {
    // Skip if this group/lang is already wrapped on this element — re-wrapping
    // would nest spans because the regex still matches the phrase text inside
    // the existing word-group span.
    if (el.querySelector(`.word-group[data-word="${groupId}"][data-lang="${lang}"]`)) return;
    const html = el.innerHTML;
    // Escape special regex chars in the phrase
    const escaped = phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    // Allow flexible whitespace/dash matching
    const flexPattern = escaped.replace(/[\s\u200B\u00A0]+/g, '[\\s\\u200B\\u00A0\u05BE-]*');
    const regex = new RegExp(`(${flexPattern})`, 'g');
    const replacement = `<span class="word-group" data-word="${groupId}" data-lang="${lang}">$1</span>`;
    const newHtml = html.replace(regex, replacement);
    if (newHtml !== html) {
      el.innerHTML = newHtml;
    }
  },

  // Highlight specific word groups, dim everything else.
  // When `sectionEl` is provided, scope the dim/highlight + has-highlights toggle
  // to that section's panel only — necessary because the document contains many
  // .primary-text-content.active elements (one per section) and toggling them all
  // would dim sections the reader isn't on.
  highlight(groupIds, options = {}) {
    const { effect = 'highlight', animate = true, sectionEl = null } = options;

    // Reset previous (scoped if a section was given)
    this.reset(false, sectionEl);

    if (!groupIds || groupIds.length === 0) return;

    this.activeHighlights = groupIds;

    const scope = sectionEl || document;

    // Dim all word groups in scope first
    scope.querySelectorAll('.word-group').forEach(span => {
      span.classList.add('dimmed');
      span.classList.remove('highlighted', 'glow', 'pulse');
    });

    // Highlight the targeted groups within scope
    groupIds.forEach(id => {
      scope.querySelectorAll(`[data-word="${id}"]`).forEach(span => {
        span.classList.remove('dimmed');
        span.classList.add('highlighted');
        if (effect === 'glow') span.classList.add('glow');
        if (effect === 'pulse') span.classList.add('pulse');
      });
    });

    // Also dim un-wrapped text by adding class to the active primary text
    // container inside the scope (not the first one in the document).
    const primaryContainer = scope.querySelector('.primary-text-content.active');
    if (primaryContainer) {
      primaryContainer.classList.add('has-highlights');
      if (primaryContainer.classList.contains('image-mode')) {
        primaryContainer.querySelectorAll('.image-region, .image-hole').forEach(r => {
          if (!groupIds.includes(r.dataset.region)) return;
          r.classList.add('highlighted');
          if (r.classList.contains('image-region')) {
            if (effect === 'glow') r.classList.add('glow');
            if (effect === 'pulse') r.classList.add('pulse');
          }
        });
        this.layoutImage(primaryContainer);
      }
    }
  },

  // Size an image-mode panel item and zoom it to its highlighted regions.
  //
  // The stage (image + SVG overlay) is sized to fit the viewport at the
  // image's aspect ratio, then transformed: with no highlights it sits
  // centered at scale 1; with highlights it scales so the regions' bounding
  // box fills the viewport (with a margin, capped at MAX_ZOOM) and pans so the
  // box is centered — clamped so the page edge never pulls into view when the
  // zoomed page is larger than the viewport. Idempotent; safe on resize.
  MAX_ZOOM: 5,
  // Zoom timing. A fixed duration makes a 5× zoom feel like a lunge next to a
  // 1.4× one, but scaling time with the zoom ratio makes big zooms crawl. Our
  // eyes read zoom on a log scale, so the duration grows with |ln(ratio)|:
  // each doubling of magnification adds the same ZOOM_PER_LN·ln2 ≈ 0.28 s.
  //   1× → 1.4×: ~1.5 s    1× → 5× (or 5× → 1×): ~2.0 s    pan only: 1.35 s
  ZOOM_BASE_S: 1.35,
  ZOOM_PER_LN_S: 0.4,
  ZOOM_MAX_S: 2.5,
  layoutImage(content) {
    const viewport = content.querySelector('.image-viewport');
    const stage = content.querySelector('.image-stage');
    if (!viewport || !stage) return;
    const vw = viewport.clientWidth, vh = viewport.clientHeight;
    if (!vw || !vh) return;
    const aspect = Number(content.dataset.width) / Number(content.dataset.height);
    let sw = vw, sh = vw / aspect;
    if (sh > vh) { sh = vh; sw = vh * aspect; }
    stage.style.width = `${sw}px`;
    stage.style.height = `${sh}px`;

    const lit = [...content.querySelectorAll('.image-region.highlighted')];
    let z = 1, cx = 0.5, cy = 0.5;
    if (lit.length) {
      const num = (r, k) => parseFloat(r.getAttribute(k));
      const x0 = Math.min(...lit.map(r => num(r, 'x')));
      const y0 = Math.min(...lit.map(r => num(r, 'y')));
      const x1 = Math.max(...lit.map(r => num(r, 'x') + num(r, 'width')));
      const y1 = Math.max(...lit.map(r => num(r, 'y') + num(r, 'height')));
      const margin = 1.25;
      z = Math.min(vw / ((x1 - x0) * sw * margin), vh / ((y1 - y0) * sh * margin), this.MAX_ZOOM);
      z = Math.max(z, 1);
      cx = (x0 + x1) / 2;
      cy = (y0 + y1) / 2;
    }
    const pan = (view, size, c) => {
      const scaled = size * z;
      if (scaled <= view) return (view - scaled) / 2;
      return Math.min(0, Math.max(view - scaled, view / 2 - c * scaled));
    };
    const tx = pan(vw, sw, cx), ty = pan(vh, sh, cy);
    const prev = Number(stage.dataset.zoom) || 1;
    const secs = Math.min(this.ZOOM_MAX_S, this.ZOOM_BASE_S + this.ZOOM_PER_LN_S * Math.abs(Math.log(z / prev)));
    stage.style.transitionDuration = `${secs.toFixed(2)}s`;
    stage.dataset.zoom = z;
    stage.style.transform = `translate(${tx}px, ${ty}px) scale(${z})`;
    // non-scaling-stroke can't see the CSS transform, so undo the zoom by hand.
    stage.style.setProperty('--zoom', z);
  },

  // Reset all highlights. Optionally scope to a section element.
  reset(animate = true, sectionEl = null) {
    this.activeHighlights = [];
    const scope = sectionEl || document;
    scope.querySelectorAll('.word-group').forEach(span => {
      span.classList.remove('dimmed', 'highlighted', 'glow', 'pulse');
    });
    scope.querySelectorAll('.image-region, .image-hole').forEach(r => {
      r.classList.remove('highlighted', 'glow', 'pulse');
    });
    scope.querySelectorAll('.primary-text-content').forEach(el => {
      el.classList.remove('has-highlights');
      if (el.classList.contains('image-mode') && el.classList.contains('active')) this.layoutImage(el);
    });
  },

  // Crossfade to a new primary verse
  crossfadeTo(sectionEl, newVerseData) {
    const textArea = sectionEl.querySelector('.primary-text-area');
    if (!textArea) return;

    const currentContent = textArea.querySelector('.primary-text-content.active');

    // Skip if already showing this verse
    if (currentContent && currentContent.dataset.ref === newVerseData.ref) return;

    // Find the target content element by matching data-ref
    const allContents = textArea.querySelectorAll('.primary-text-content');
    let newContent = null;
    for (const el of allContents) {
      if (el.dataset.ref === newVerseData.ref) {
        newContent = el;
        break;
      }
    }

    if (newContent) {
      if (currentContent) {
        currentContent.classList.remove('active');
        currentContent.classList.add('fading-out');
        setTimeout(() => currentContent.classList.remove('fading-out'), 600);
      }
      newContent.classList.add('active');
      if (newVerseData.words) {
        this.wrapWords(newContent, newVerseData.words);
      }
      // Alternate verses are pre-rendered at the CSS baseline size; only the
      // initially active one was fit. Fit the incoming one to the panel now.
      this.fitToPanel(textArea);
    }
  },

};
