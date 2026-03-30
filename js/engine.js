// Close Read Engine
// Orchestrates the scrollytelling experience using GSAP ScrollTrigger
// Data-driven: loads a JSON file and builds all UI from it

document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const sheetName = params.get('sheet');

  if (!sheetName) {
    // No sheet specified — show the index
    document.fonts.ready.then(() => buildIndex());
    return;
  }

  // Load and render a specific sheet
  gsap.registerPlugin(ScrollTrigger);
  const dataUrl = `data/${sheetName}.json`;

  fetch(dataUrl)
    .then(res => {
      if (!res.ok) throw new Error(`Could not load ${dataUrl}`);
      return res.json();
    })
    .then(data => {
      document.fonts.ready.then(() => {
        const app = new CloseReadApp(data);
        app.init();
        setTimeout(() => ScrollTrigger.refresh(), 200);
      });
    })
    .catch(err => {
      document.getElementById('main-content').innerHTML =
        `<div style="padding:4rem;text-align:center;color:#8b5e3c;">
          <p>Could not load sheet data.</p>
          <p style="font-size:0.85rem;color:#8a8279;">${err.message}</p>
        </div>`;
    });
});

function buildIndex() {
  document.title = 'Close Read';

  const header = document.querySelector('.title-screen');
  header.innerHTML = `
    <div class="title-he">קריאה מקרוב</div>
    <div class="title-en">Close Read</div>
    <div class="subtitle-en">Interactive Torah study in the scrollytelling format</div>
  `;

  fetch('data/index.json')
    .then(res => {
      if (!res.ok) throw new Error('Could not load sheet index');
      return res.json();
    })
    .then(sheets => {
      const main = document.getElementById('main-content');
      const list = document.createElement('div');
      list.className = 'index-list';

      sheets.forEach(sheet => {
        const card = document.createElement('a');
        card.className = 'index-card';
        card.href = `?sheet=${sheet.slug}`;
        card.innerHTML = `
          <div class="index-card-title-he">${sheet.title.he}</div>
          <div class="index-card-title-en">${sheet.title.en}</div>
          <div class="index-card-author">${sheet.author.he} / ${sheet.author.en}</div>
          ${sheet.description ? `<div class="index-card-desc">${sheet.description}</div>` : ''}
        `;
        list.appendChild(card);
      });

      main.appendChild(list);
    })
    .catch(err => {
      document.getElementById('main-content').innerHTML =
        `<div style="padding:4rem;text-align:center;color:#8b5e3c;">
          <p>Could not load sheet index.</p>
          <p style="font-size:0.85rem;color:#8a8279;">${err.message}</p>
        </div>`;
    });
}

class CloseReadApp {
  constructor(data) {
    this.data = data;
    this.sections = [];
  }

  init() {
    this.buildTitleScreen();
    this.buildSections();
    this.buildClosing();
    this.buildSectionNav();
    this.setupScrollTriggers();
    this.setupProgressBar();
    this.updatePageTitle();
  }

  // ─── Page Title ───
  updatePageTitle() {
    const t = this.data.title;
    document.title = `Close Read: ${t.en} - ${t.author.en}`;
  }

  // ─── Title Screen ───
  buildTitleScreen() {
    const t = this.data.title;
    const header = document.querySelector('.title-screen');
    header.innerHTML = `
      <div class="title-he">${t.he}</div>
      <div class="title-en">${t.en}</div>
      <div class="subtitle-he">${t.subtitle.he}</div>
      <div class="subtitle-en">${t.subtitle.en}</div>
      <div class="author-he">${t.author.he}</div>
      <div class="author-en">${t.author.en}</div>
      <div class="scroll-hint">scroll</div>
    `;
  }

  // ─── Closing Screen ───
  buildClosing() {
    const t = this.data.title;
    const footer = document.querySelector('.closing-screen');
    footer.innerHTML = `
      <div class="closing-line"></div>
      <p class="closing-text">Based on a study sheet by ${t.author.en}</p>
      ${t.sourceUrl ? `<a class="closing-link" href="${t.sourceUrl}" target="_blank" rel="noopener">${t.sourceLabel || 'View the original source'}</a>` : ''}
    `;
  }

  // ─── Section Nav Dots ───
  buildSectionNav() {
    const nav = document.querySelector('.section-nav');
    this.sections.forEach(({ el, data }, i) => {
      const dot = document.createElement('button');
      dot.className = `section-dot${i === 0 ? ' active' : ''}`;
      dot.setAttribute('aria-label', data.title.en);
      nav.appendChild(dot);

      ScrollTrigger.create({
        trigger: el,
        start: 'top center',
        end: 'bottom center',
        onEnter: () => this.setActiveDot(i),
        onEnterBack: () => this.setActiveDot(i),
      });

      dot.addEventListener('click', () => {
        el.scrollIntoView({ behavior: 'smooth' });
      });
    });
  }

  // ─── Build Sections ───
  buildSections() {
    const main = document.getElementById('main-content');

    this.data.sections.forEach((section) => {
      const sectionEl = document.createElement('div');
      sectionEl.className = 'cr-section';
      sectionEl.id = section.id;

      // Section title card
      sectionEl.innerHTML = `
        <div class="section-title-card">
          <div class="section-title-he">${section.title.he}</div>
          <div class="section-title-en">${section.title.en}</div>
        </div>
      `;

      // Scroll container with sticky text + scrolling cards
      const scrollContainer = document.createElement('div');
      scrollContainer.className = 'scroll-container';

      // Primary text area (sticky)
      const primaryArea = document.createElement('div');
      primaryArea.className = 'primary-text-area';

      if (section.primaryText.mode === 'comparison') {
        primaryArea.appendChild(this.buildComparisonVerse(section.primaryText, true));
      } else {
        primaryArea.appendChild(this.buildVerseContent(section.primaryText, true));
      }

      // Build alternate verses from verse-change steps
      section.steps.forEach(step => {
        if (step.type === 'verse-change' && step.newVerse) {
          if (step.newVerse.mode === 'comparison') {
            primaryArea.appendChild(this.buildComparisonVerse(step.newVerse, false));
          } else {
            primaryArea.appendChild(this.buildVerseContent(step.newVerse, false));
          }
        }
      });

      scrollContainer.appendChild(primaryArea);

      // Step track (commentary cards)
      const stepTrack = document.createElement('div');
      stepTrack.className = 'step-track';

      section.steps.forEach(step => {
        if (step.type === 'verse-change') return;
        stepTrack.appendChild(this.buildStepCard(step));
      });

      scrollContainer.appendChild(stepTrack);
      sectionEl.appendChild(scrollContainer);
      main.appendChild(sectionEl);

      this.sections.push({ el: sectionEl, data: section });
    });
  }

  buildVerseContent(verseData, isActive) {
    const div = document.createElement('div');
    div.className = `primary-text-content${isActive ? ' active' : ''}`;
    div.dataset.ref = verseData.ref;

    const refSlug = verseData.ref.replace(/\s+/g, '_');
    const sefariaUrl = `https://www.sefaria.org/${refSlug}`;

    div.innerHTML = `
      <div class="primary-ref">
        <a href="${sefariaUrl}" target="_blank" rel="noopener">${verseData.ref}</a>
      </div>
      <div class="primary-he">${verseData.he}</div>
      <div class="primary-en">${verseData.en}</div>
    `;

    if (verseData.words) {
      requestAnimationFrame(() => TextEffects.wrapWords(div, verseData.words));
    }

    return div;
  }

  buildComparisonVerse(verseData, isActive) {
    const div = document.createElement('div');
    div.className = `primary-text-content comparison-mode${isActive ? ' active' : ''}`;
    div.dataset.ref = verseData.ref;

    const leftRefSlug = verseData.left.ref.replace(/\s+/g, '_');
    const rightRefSlug = verseData.right.ref.replace(/\s+/g, '_');

    div.innerHTML = `
      <div class="comparison-side">
        <div class="primary-ref">
          <a href="https://www.sefaria.org/${leftRefSlug}" target="_blank" rel="noopener">${verseData.left.ref}</a>
        </div>
        <div class="primary-he">${verseData.left.he}</div>
        <div class="primary-en">${verseData.left.en}</div>
      </div>
      <div class="comparison-vs">vs.</div>
      <div class="comparison-side">
        <div class="primary-ref">
          <a href="https://www.sefaria.org/${rightRefSlug}" target="_blank" rel="noopener">${verseData.right.ref}</a>
        </div>
        <div class="primary-he">${verseData.right.he}</div>
        <div class="primary-en">${verseData.right.en}</div>
      </div>
    `;

    if (verseData.words) {
      requestAnimationFrame(() => TextEffects.wrapWords(div, verseData.words));
    }

    return div;
  }

  buildStepCard(step) {
    const card = document.createElement('div');
    card.className = 'step-card';
    card.dataset.stepId = step.id;
    card.dataset.type = step.type;
    if (step.highlight) card.dataset.highlight = JSON.stringify(step.highlight);
    if (step.effect) card.dataset.effect = step.effect;

    const inner = document.createElement('div');
    inner.className = 'card-inner';

    if (step.type === 'commentary') {
      const refSlug = step.ref ? step.ref.replace(/\s+/g, '_') : '';
      inner.innerHTML = `
        <div>
          <span class="source-label" data-source="${step.source}">${step.sourceLabel.he} / ${step.sourceLabel.en}</span>
          ${step.ref ? `<span class="source-ref"><a href="https://www.sefaria.org/${refSlug}" target="_blank" rel="noopener">${step.ref}</a></span>` : ''}
        </div>
        <div class="card-text-he">${step.text.he}</div>
        <div class="card-text-en">${step.text.en}</div>
        ${step.annotation ? `
          <div class="card-annotation">
            <div class="card-annotation-he">${step.annotation.he}</div>
            <div class="card-annotation-en">${step.annotation.en}</div>
          </div>
        ` : ''}
      `;
    } else if (step.type === 'question') {
      const qLabel = step.questionLabel || this.data.title.questionLabel;
      const qText = qLabel ? `${qLabel.he} / ${qLabel.en}` : '';
      inner.innerHTML = `
        ${qText ? `<div class="question-icon">${qText}</div>` : ''}
        <div class="card-question-he">${step.text.he}</div>
        <div class="card-question-en">${step.text.en}</div>
      `;
    } else if (step.type === 'narration') {
      inner.innerHTML = `
        <div class="narration-he">${step.text.he}</div>
        <div class="narration-en">${step.text.en}</div>
      `;
    }

    card.appendChild(inner);
    return card;
  }

  // ─── ScrollTrigger Setup ───
  setupScrollTriggers() {
    this.sections.forEach(({ el, data }) => {
      const stepCards = el.querySelectorAll('.step-card');

      stepCards.forEach((card) => {
        ScrollTrigger.create({
          trigger: card,
          start: 'top 55%',
          end: 'bottom 40%',
          onEnter: () => this.activateStep(card, el, data),
          onEnterBack: () => this.activateStep(card, el, data),
          onLeave: () => this.deactivateStep(card),
          onLeaveBack: () => this.deactivateStep(card),
        });
      });
    });

    // Section title animations
    document.querySelectorAll('.section-title-card').forEach(title => {
      gsap.from(title.children, {
        scrollTrigger: {
          trigger: title,
          start: 'top 80%',
          end: 'top 40%',
          toggleActions: 'play none none reverse',
        },
        y: 30,
        opacity: 0,
        stagger: 0.15,
        duration: 0.8,
        ease: 'power2.out',
      });
    });
  }

  activateStep(card, sectionEl, sectionData) {
    // Deactivate any other active cards so only one drives highlights
    sectionEl.querySelectorAll('.step-card.is-active').forEach(c => {
      if (c !== card) c.classList.remove('is-active');
    });
    card.classList.add('is-active');

    const stepId = card.dataset.stepId;
    const stepIndex = sectionData.steps.findIndex(s => s.id === stepId);

    // Find the most recent verse-change at or before this step
    let targetVerse = null;
    for (let i = stepIndex - 1; i >= 0; i--) {
      const s = sectionData.steps[i];
      if (s.type === 'verse-change' && s.newVerse) {
        targetVerse = s.newVerse;
        break;
      }
    }

    if (targetVerse) {
      const activeContent = sectionEl.querySelector('.primary-text-content.active');
      if (!activeContent || activeContent.dataset.ref !== targetVerse.ref) {
        TextEffects.crossfadeTo(sectionEl, targetVerse);
        setTimeout(() => {
          const newActive = sectionEl.querySelector('.primary-text-content.active');
          if (newActive && targetVerse.words) {
            TextEffects.wrapWords(newActive, targetVerse.words);
          }
        }, 100);
      }
    } else {
      const originalRef = sectionData.primaryText.ref;
      const activeContent = sectionEl.querySelector('.primary-text-content.active');
      if (activeContent && activeContent.dataset.ref !== originalRef) {
        TextEffects.crossfadeTo(sectionEl, sectionData.primaryText);
      }
    }

    // Handle highlights
    const highlightData = card.dataset.highlight;
    const effect = card.dataset.effect || 'highlight';
    if (highlightData) {
      const groups = JSON.parse(highlightData);
      TextEffects.highlight(groups, { effect });
    } else {
      TextEffects.reset();
    }
  }

  deactivateStep(card) {
    card.classList.remove('is-active');
    const anyActive = document.querySelector('.step-card.is-active');
    if (!anyActive) {
      TextEffects.reset();
    }
  }

  // ─── Progress Bar ───
  setupProgressBar() {
    const bar = document.querySelector('.progress-bar');
    if (!bar) return;

    ScrollTrigger.create({
      trigger: document.body,
      start: 'top top',
      end: 'bottom bottom',
      onUpdate: (self) => {
        bar.style.transform = `scaleX(${self.progress})`;
      }
    });
  }

  setActiveDot(index) {
    document.querySelectorAll('.section-dot').forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }
}
