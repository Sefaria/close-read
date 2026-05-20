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
          ${sheet.title.he ? `<div class="index-card-title-he">${sheet.title.he}</div>` : ''}
          <div class="index-card-title-en">${sheet.title.en}</div>
          <div class="index-card-author">${sheet.author.he ? `${sheet.author.he} / ` : ''}${sheet.author.en}</div>
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
    this.tree = null;
    this.currentPath = [];
  }

  init() {
    this.buildTitleScreen();
    this.buildBranchTree();
    this.buildSections();
    this.buildClosing();
    this.currentPath = this.readPathFromUrl();
    this.applyVisibility();
    this.buildSectionNav();
    this.setupScrollTriggers();
    this.setupProgressBar();
    this.updatePageTitle();
    this.wirePopstate();
  }

  // ─── Branching: build tree, path state, visibility ───
  buildBranchTree() {
    const decisions = new Map();        // sectionId → { level, branches, orderIndex }
    const targets = new Map();          // sectionId → { decisionSectionId, branchId, level }
    const decisionsByLevel = new Map(); // level → [decisionSectionId]
    this.data.sections.forEach((section, i) => {
      if (section.type !== 'decision') return;
      decisions.set(section.id, {
        level: section.level,
        branches: section.branches,
        orderIndex: i,
      });
      section.branches.forEach(branch => {
        targets.set(branch.target, {
          decisionSectionId: section.id,
          branchId: branch.id,
          level: section.level,
        });
      });
      if (!decisionsByLevel.has(section.level)) decisionsByLevel.set(section.level, []);
      decisionsByLevel.get(section.level).push(section.id);
    });
    this.tree = { decisions, targets, decisionsByLevel };
  }

  hasBranching() {
    return this.tree && this.tree.decisions.size > 0;
  }

  readPathFromUrl() {
    const raw = new URLSearchParams(window.location.search).get('path');
    if (!raw) return [];
    return this.normalizePath(raw.split('/').filter(Boolean));
  }

  writePathToUrl(path) {
    const params = new URLSearchParams(window.location.search);
    if (path.length === 0) params.delete('path');
    else params.set('path', path.join('/'));
    const search = params.toString();
    const newUrl = `${window.location.pathname}${search ? '?' + search : ''}`;
    history.pushState({ path }, '', newUrl);
  }

  // Drop any segment that doesn't match a reachable branch at its level.
  normalizePath(segments) {
    const valid = [];
    for (let i = 0; i < segments.length; i++) {
      const visible = this.pathToVisibleSet(valid);
      const decisionId = (this.tree.decisionsByLevel.get(i) || []).find(id => visible.has(id));
      if (!decisionId) break;
      const decision = this.tree.decisions.get(decisionId);
      const match = decision.branches.find(b => b.id === segments[i]);
      if (!match) break;
      valid.push(segments[i]);
    }
    return valid;
  }

  // Compute which section IDs are visible for a given path.
  // Rule: non-target reading sections are always visible. Targets are visible
  // iff path[level] === branchId AND their parent decision is visible.
  // Decision sections are visible iff the immediately preceding section is visible.
  pathToVisibleSet(path) {
    const visible = new Set();
    let prevVisible = true;
    this.data.sections.forEach(section => {
      let show;
      if (section.type === 'decision') {
        show = prevVisible;
      } else {
        const target = this.tree.targets.get(section.id);
        if (!target) {
          show = true;
        } else {
          const seg = path[target.level];
          const parentVisible = visible.has(target.decisionSectionId);
          show = parentVisible && seg === target.branchId;
        }
      }
      if (show) visible.add(section.id);
      prevVisible = show;
    });
    return visible;
  }

  applyVisibility() {
    if (!this.hasBranching()) return;
    const visible = this.pathToVisibleSet(this.currentPath);
    document.querySelectorAll('.cr-section').forEach(el => {
      el.classList.toggle('is-hidden', !visible.has(el.id));
    });
    // Block scroll past an unanswered decision: hide the closing screen
    // (and end-of-document hint) when the path doesn't end on a reading section.
    const lastVisibleId = Array.from(visible).pop();
    const lastSection = this.data.sections.find(s => s.id === lastVisibleId);
    const pathIsBlocked = lastSection?.type === 'decision';
    const closing = document.querySelector('.closing-screen');
    if (closing) closing.classList.toggle('is-hidden', pathIsBlocked);
    this.updateChosenButtons();
  }

  updateChosenButtons() {
    document.querySelectorAll('.decision-branch-button.is-chosen')
      .forEach(b => b.classList.remove('is-chosen'));
    this.currentPath.forEach((branchId, level) => {
      const visible = this.pathToVisibleSet(this.currentPath.slice(0, level));
      const decisionId = (this.tree.decisionsByLevel.get(level) || []).find(id => visible.has(id));
      if (!decisionId) return;
      const sel = `[id="${decisionId}"] .decision-branch-button[data-branch="${branchId}"]`;
      const btn = document.querySelector(sel);
      if (btn) btn.classList.add('is-chosen');
    });
  }

  onBranchClick(decisionSectionId, branchId) {
    const decision = this.tree.decisions.get(decisionSectionId);
    if (!decision) return;
    const newPath = this.currentPath.slice(0, decision.level);
    newPath.push(branchId);
    this.currentPath = newPath;
    this.applyVisibility();
    this.writePathToUrl(newPath);
    this.renderBreadcrumb();
    const target = decision.branches.find(b => b.id === branchId).target;
    // Defer ScrollTrigger refresh + smooth-scroll to the next microtask via
    // setTimeout (rAF can be paused in headless / background-tab environments,
    // which would leave triggers stale after a visibility flip).
    setTimeout(() => {
      ScrollTrigger.refresh();
      const el = document.getElementById(target);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 0);
  }

  wirePopstate() {
    window.addEventListener('popstate', () => {
      this.currentPath = this.readPathFromUrl();
      this.applyVisibility();
      if (this.hasBranching()) {
        this.renderBreadcrumb();
        setTimeout(() => ScrollTrigger.refresh(), 0);
      }
    });
  }

  // ─── Page Title ───
  updatePageTitle() {
    const t = this.data.title;
    document.title = t.author?.en
      ? `Close Read: ${t.en} - ${t.author.en}`
      : `Close Read: ${t.en}`;
  }

  // ─── Title Screen ───
  buildTitleScreen() {
    const t = this.data.title;
    const header = document.querySelector('.title-screen');
    header.innerHTML = `
      ${t.he ? `<div class="title-he">${t.he}</div>` : ''}
      <div class="title-en">${t.en}</div>
      ${t.subtitle?.he ? `<div class="subtitle-he">${t.subtitle.he}</div>` : ''}
      ${t.subtitle?.en ? `<div class="subtitle-en">${t.subtitle.en}</div>` : ''}
      ${t.author?.he ? `<div class="author-he">${t.author.he}</div>` : ''}
      ${t.author?.en ? `<div class="author-en">${t.author.en}</div>` : ''}
      <div class="scroll-hint">scroll</div>
    `;
  }

  // ─── Closing Screen ───
  buildClosing() {
    const t = this.data.title;
    const footer = document.querySelector('.closing-screen');
    footer.innerHTML = `
      <div class="closing-line"></div>
      <p class="closing-text">Based on the sources available on Sefaria</p>
      ${t.sourceUrl ? `<a class="closing-link" href="${t.sourceUrl}" target="_blank" rel="noopener">${t.sourceLabel || 'View the original source'}</a>` : ''}
    `;
  }

  // ─── Section Nav: dots for linear sheets, breadcrumb for branching sheets ───
  buildSectionNav() {
    const nav = document.querySelector('.section-nav');
    if (this.hasBranching()) {
      nav.classList.add('is-breadcrumb');
      this.renderBreadcrumb();
      return;
    }
    this.sections.forEach(({ navTarget, data }, i) => {
      const dot = document.createElement('button');
      dot.className = `section-dot${i === 0 ? ' active' : ''}`;
      dot.setAttribute('aria-label', data.title.en);
      nav.appendChild(dot);

      ScrollTrigger.create({
        trigger: navTarget,
        start: 'top 50%',
        onEnter: () => this.setActiveDot(i),
        onEnterBack: () => this.setActiveDot(i),
      });

      dot.addEventListener('click', () => {
        navTarget.scrollIntoView({ behavior: 'smooth' });
      });
    });
  }

  renderBreadcrumb() {
    const nav = document.querySelector('.section-nav');
    nav.innerHTML = '';

    const crumbs = [];
    const firstReading = this.data.sections.find(
      s => s.type !== 'decision' && !this.tree.targets.has(s.id)
    );
    if (firstReading) {
      crumbs.push({ id: firstReading.id, label: firstReading.title.en });
    }

    this.currentPath.forEach((branchId, level) => {
      const visible = this.pathToVisibleSet(this.currentPath.slice(0, level));
      const decisionId = (this.tree.decisionsByLevel.get(level) || []).find(id => visible.has(id));
      if (!decisionId) return;
      const decision = this.tree.decisions.get(decisionId);
      const branch = decision.branches.find(b => b.id === branchId);
      if (!branch) return;
      crumbs.push({ id: branch.target, label: branch.label.en });
    });

    crumbs.forEach((crumb, i) => {
      const link = document.createElement('button');
      link.className = 'breadcrumb-link';
      link.textContent = crumb.label;
      link.addEventListener('click', () => {
        const el = document.getElementById(crumb.id);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      nav.appendChild(link);
      if (i < crumbs.length - 1) {
        const sep = document.createElement('span');
        sep.className = 'breadcrumb-sep';
        sep.textContent = '›';
        nav.appendChild(sep);
      }
    });
  }

  // ─── Group consecutive sections sharing primary text ───
  // Decision sections form their own one-section group; sections that are
  // branch targets never merge backward (they're alternatives, not adjacent
  // continuations of the previous primaryText).
  groupSections() {
    const groups = [];
    let current = null;
    this.data.sections.forEach(section => {
      if (section.type === 'decision') {
        groups.push({ key: `decision:${section.id}`, sections: [section], isDecision: true });
        current = null;
        return;
      }
      const isTarget = this.tree && this.tree.targets.has(section.id);
      const key = this.primaryKey(section.primaryText);
      if (!isTarget && current && current.key === key) {
        current.sections.push(section);
      } else {
        current = { key, sections: [section], isDecision: false };
        groups.push(current);
      }
    });
    return groups;
  }

  primaryKey(pt) {
    if (pt.mode === 'comparison') {
      return `cmp:${pt.left.ref}|${pt.right.ref}|${pt.left.he}|${pt.right.he}`;
    }
    return `single:${pt.ref}|${pt.he}`;
  }

  // Merge word maps across sub-sections that share a primary text. The shared
  // sticky panel is built once; each sub-section's words are unioned so that
  // any sub-section's highlights can target spans on the same DOM.
  mergedPrimaryText(sections) {
    const base = sections[0].primaryText;
    if (base.mode === 'comparison') {
      const words = {};
      sections.forEach(s => Object.assign(words, s.primaryText.words || {}));
      return { ...base, words };
    }
    const words = {};
    sections.forEach(s => Object.assign(words, s.primaryText.words || {}));
    return { ...base, words };
  }

  // ─── Build Sections ───
  buildSections() {
    const main = document.getElementById('main-content');
    const groups = this.groupSections();

    groups.forEach(group => {
      if (group.isDecision) {
        const decisionSection = group.sections[0];
        const sectionEl = this.buildDecisionSection(decisionSection);
        main.appendChild(sectionEl);
        return;
      }
      const firstSection = group.sections[0];
      const sectionEl = document.createElement('div');
      sectionEl.className = 'cr-section';
      sectionEl.id = firstSection.id;

      // Prominent title card for the first sub-section of the group only.
      // Sub-sections that share this group's primary text get inline dividers
      // in the step track instead, so the sticky primary panel stays pinned
      // across the whole group.
      sectionEl.innerHTML = `
        <div class="section-title-card">
          ${firstSection.title.he ? `<div class="section-title-he">${firstSection.title.he}</div>` : ''}
          <div class="section-title-en">${firstSection.title.en}</div>
        </div>
      `;

      // Scroll container with sticky text + scrolling cards
      const scrollContainer = document.createElement('div');
      scrollContainer.className = 'scroll-container';

      // Primary text area (sticky) — one panel for the whole group
      const primaryArea = document.createElement('div');
      primaryArea.className = 'primary-text-area';

      const mergedPrimary = this.mergedPrimaryText(group.sections);
      if (mergedPrimary.mode === 'comparison') {
        primaryArea.appendChild(this.buildComparisonVerse(mergedPrimary, true));
      } else {
        primaryArea.appendChild(this.buildVerseContent(mergedPrimary, true));
      }

      // Build alternate verses from verse-change steps across all sub-sections
      group.sections.forEach(section => {
        section.steps.forEach(step => {
          if (step.type === 'verse-change' && step.newVerse) {
            if (step.newVerse.mode === 'comparison') {
              primaryArea.appendChild(this.buildComparisonVerse(step.newVerse, false));
            } else {
              primaryArea.appendChild(this.buildVerseContent(step.newVerse, false));
            }
          }
        });
      });

      scrollContainer.appendChild(primaryArea);

      // Step track (commentary cards) — concatenated across the group
      const stepTrack = document.createElement('div');
      stepTrack.className = 'step-track';

      group.sections.forEach((section, i) => {
        // Sub-sections beyond the first get an inline divider in the sidebar.
        if (i > 0) {
          stepTrack.appendChild(this.buildSectionDivider(section));
        }
        section.steps.forEach(step => {
          if (step.type === 'verse-change') return;
          const card = this.buildStepCard(step);
          card.dataset.sectionId = section.id;
          stepTrack.appendChild(card);
        });
      });

      scrollContainer.appendChild(stepTrack);
      sectionEl.appendChild(scrollContainer);
      main.appendChild(sectionEl);

      // Register one entry per sub-section for nav dots and scroll triggers.
      group.sections.forEach((section, i) => {
        const navTarget = i === 0
          ? sectionEl.querySelector('.section-title-card')
          : stepTrack.querySelector(`.section-divider[data-section-id="${section.id}"]`);
        this.sections.push({ el: sectionEl, data: section, navTarget });
      });
    });
  }

  buildSectionDivider(section) {
    const divider = document.createElement('div');
    divider.className = 'section-divider';
    divider.dataset.sectionId = section.id;
    divider.innerHTML = `
      ${section.title.he ? `<div class="section-divider-he">${section.title.he}</div>` : ''}
      <div class="section-divider-en">${section.title.en}</div>
    `;
    return divider;
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
      // Wrap synchronously: the div's innerHTML is already populated above, and
      // headless / background-tab environments don't always fire requestAnimationFrame,
      // which would leave word-groups unwrapped and break highlighting entirely.
      TextEffects.wrapWords(div, verseData.words);
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
      <div class="comparison-side left">
        <div class="primary-ref">
          <a href="https://www.sefaria.org/${leftRefSlug}" target="_blank" rel="noopener">${verseData.left.ref}</a>
        </div>
        <div class="primary-he">${verseData.left.he}</div>
        <div class="primary-en">${verseData.left.en}</div>
      </div>
      <div class="comparison-vs">vs.</div>
      <div class="comparison-side right">
        <div class="primary-ref">
          <a href="https://www.sefaria.org/${rightRefSlug}" target="_blank" rel="noopener">${verseData.right.ref}</a>
        </div>
        <div class="primary-he">${verseData.right.he}</div>
        <div class="primary-en">${verseData.right.en}</div>
      </div>
    `;

    if (verseData.words) {
      // Wrap synchronously: the div's innerHTML is already populated above, and
      // headless / background-tab environments don't always fire requestAnimationFrame,
      // which would leave word-groups unwrapped and break highlighting entirely.
      TextEffects.wrapWords(div, verseData.words);
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
      const labelText = step.sourceLabel.he
        ? `${step.sourceLabel.he} / ${step.sourceLabel.en}`
        : step.sourceLabel.en;
      inner.innerHTML = `
        <div>
          <span class="source-label" data-source="${step.source}">${labelText}</span>
          ${step.ref ? `<span class="source-ref"><a href="https://www.sefaria.org/${refSlug}" target="_blank" rel="noopener">${step.ref}</a></span>` : ''}
        </div>
        ${step.text.he ? `<div class="card-text-he">${step.text.he}</div>` : ''}
        <div class="card-text-en">${step.text.en}</div>
        ${step.annotation ? `
          <div class="card-annotation">
            ${step.annotation.he ? `<div class="card-annotation-he">${step.annotation.he}</div>` : ''}
            <div class="card-annotation-en">${step.annotation.en}</div>
          </div>
        ` : ''}
      `;
    } else if (step.type === 'question') {
      const qLabel = step.questionLabel || this.data.title.questionLabel;
      const qText = qLabel
        ? (qLabel.he ? `${qLabel.he} / ${qLabel.en}` : qLabel.en)
        : '';
      inner.innerHTML = `
        ${qText ? `<div class="question-icon">${qText}</div>` : ''}
        ${step.text.he ? `<div class="card-question-he">${step.text.he}</div>` : ''}
        <div class="card-question-en">${step.text.en}</div>
      `;
    } else if (step.type === 'narration') {
      inner.innerHTML = `
        ${step.text.he ? `<div class="narration-he">${step.text.he}</div>` : ''}
        <div class="narration-en">${step.text.en}</div>
      `;
    }

    card.appendChild(inner);
    return card;
  }

  // ─── Decision Section: full-width fork with branch buttons ───
  buildDecisionSection(section) {
    const el = document.createElement('section');
    el.className = 'cr-section';
    el.id = section.id;
    el.dataset.type = 'decision';

    const inner = document.createElement('div');
    inner.className = 'decision-inner';

    const promptEl = document.createElement('div');
    promptEl.className = 'decision-prompt';
    promptEl.innerHTML = `
      ${section.prompt.he ? `<div class="decision-prompt-he">${section.prompt.he}</div>` : ''}
      <div class="decision-prompt-en">${section.prompt.en}</div>
    `;
    inner.appendChild(promptEl);

    const branchesEl = document.createElement('div');
    branchesEl.className = 'decision-branches';
    branchesEl.dataset.count = section.branches.length;
    section.branches.forEach(branch => {
      const btn = document.createElement('button');
      btn.className = 'decision-branch-button';
      btn.dataset.branch = branch.id;
      btn.innerHTML = `
        ${branch.label.he ? `<div class="branch-label-he">${branch.label.he}</div>` : ''}
        <div class="branch-label-en">${branch.label.en}</div>
        ${branch.blurb ? `<div class="branch-blurb">${branch.blurb.en}</div>` : ''}
      `;
      btn.addEventListener('click', () => this.onBranchClick(section.id, branch.id));
      branchesEl.appendChild(btn);
    });
    inner.appendChild(branchesEl);

    el.appendChild(inner);
    return el;
  }

  // ─── ScrollTrigger Setup ───
  setupScrollTriggers() {
    this.sections.forEach(({ el, data }) => {
      // Scope to step cards belonging to this sub-section so that grouped
      // sub-sections each set up triggers only for their own cards.
      const stepCards = el.querySelectorAll(`.step-card[data-section-id="${data.id}"]`);

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
