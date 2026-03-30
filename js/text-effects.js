// Text Effects Engine
// Handles word-level highlighting, dimming, focus, and transitions

const TextEffects = {
  // Current state
  activeHighlights: [],
  currentVerse: null,

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

  // Highlight specific word groups, dim everything else
  highlight(groupIds, options = {}) {
    const { effect = 'highlight', animate = true } = options;

    // Reset previous
    this.reset(false);

    if (!groupIds || groupIds.length === 0) return;

    this.activeHighlights = groupIds;

    // Dim all word groups first
    document.querySelectorAll('.word-group').forEach(span => {
      span.classList.add('dimmed');
      span.classList.remove('highlighted', 'glow', 'pulse');
    });

    // Highlight the targeted groups
    groupIds.forEach(id => {
      document.querySelectorAll(`[data-word="${id}"]`).forEach(span => {
        span.classList.remove('dimmed');
        span.classList.add('highlighted');
        if (effect === 'glow') span.classList.add('glow');
        if (effect === 'pulse') span.classList.add('pulse');
      });
    });

    // Also dim un-wrapped text by adding class to primary text container
    const primaryContainer = document.querySelector('.primary-text-content.active');
    if (primaryContainer) {
      primaryContainer.classList.add('has-highlights');
    }
  },

  // Reset all highlights
  reset(animate = true) {
    this.activeHighlights = [];
    document.querySelectorAll('.word-group').forEach(span => {
      span.classList.remove('dimmed', 'highlighted', 'glow', 'pulse');
    });
    document.querySelectorAll('.primary-text-content').forEach(el => {
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

  // Set up comparison mode (side-by-side verses)
  setupComparison(container, leftData, rightData) {
    container.classList.add('comparison-mode');
  }
};
