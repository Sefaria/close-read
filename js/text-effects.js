// Text Effects Engine
// Handles word-level highlighting, dimming, focus, and transitions

const TextEffects = {
  // Current state
  activeHighlights: [],

  // Shrink primary-he / primary-en font sizes so the content fits inside the
  // panel's padded area. CSS clamp() with cqi/vh can scale to the container
  // dimensions but can't measure CONTENT height — so for tall passages (e.g.
  // a theme with many highlighted phrases across long verses) the content
  // still overflows. This pass measures and shrinks proportionally.
  //
  // Idempotent: clears its own inline font-size before measuring so re-runs
  // (e.g. on resize) start from CSS-clamp baseline.
  fitToPanel(panel) {
    if (!panel) return;
    // Skip hidden panels (their clientHeight is 0 — fitting them is meaningless
    // and would compute a negative innerH).
    if (panel.clientHeight === 0 || panel.offsetParent === null) return;

    const content = panel.querySelector('.primary-text-content.active');
    if (!content) return;
    const he = content.querySelector('.primary-he');
    const en = content.querySelector('.primary-en');
    if (!he && !en) return;

    // Reset inline sizing so measurement reflects current CSS baseline
    if (he) { he.style.fontSize = ''; he.style.lineHeight = ''; }
    if (en) { en.style.fontSize = ''; en.style.lineHeight = ''; en.style.display = ''; }

    // Force reflow before measuring
    void content.offsetHeight;

    const cs = getComputedStyle(panel);
    const panelInnerH = panel.clientHeight
      - parseFloat(cs.paddingTop)
      - parseFloat(cs.paddingBottom);
    if (panelInnerH <= 0) return;

    const contentH = content.scrollHeight;
    if (contentH <= panelInnerH) return; // already fits

    // Shrink by the ratio, with a 5% safety margin and a minimum floor.
    const ratio = (panelInnerH / contentH) * 0.95;
    if (he) {
      const base = parseFloat(getComputedStyle(he).fontSize);
      const shrunk = Math.max(14, base * ratio);
      he.style.fontSize = shrunk + 'px';
      he.style.lineHeight = '1.65';
    }
    if (en) {
      const base = parseFloat(getComputedStyle(en).fontSize);
      const shrunk = Math.max(12, base * ratio);
      en.style.fontSize = shrunk + 'px';
      en.style.lineHeight = '1.6';
    }

    // Second pass: if still overflowing (floor kicked in), hide the English
    // caption rather than crop the verse.
    void content.offsetHeight;
    if (content.scrollHeight > panelInnerH && en) {
      en.style.display = 'none';
    }
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
    }
  },

  // Reset all highlights. Optionally scope to a section element.
  reset(animate = true, sectionEl = null) {
    this.activeHighlights = [];
    const scope = sectionEl || document;
    scope.querySelectorAll('.word-group').forEach(span => {
      span.classList.remove('dimmed', 'highlighted', 'glow', 'pulse');
    });
    scope.querySelectorAll('.primary-text-content').forEach(el => {
      el.classList.remove('has-highlights');
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
    }
  },

};
