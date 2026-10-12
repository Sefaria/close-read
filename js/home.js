// Close Read homepage
// Makes the case for the method, then lists the readings grouped by what each
// one shows about the tool. Readings come from data/index.json; entries with
// "listed": false are retired from this page but still load by URL (and are
// still tested).

const HOME_CATEGORIES = [
  {
    id: 'branching',
    title: 'One teacher’s whole body of work, as a single reading',
    intro: 'Nechama Leibowitz wrote on each parsha for thirty years, returning to the same verses with new questions. On Sefaria those lessons sit as dozens of separate sheets. Here the reader chooses a passage, then a year, and walks that lesson. One reading holds many lessons.',
  },
  {
    id: 'single',
    title: 'One source sheet, taught',
    intro: 'The basic unit is one sheet turned into a guided reading. The verse stays in view, and each source and question lights the words it is about.',
  },
  {
    id: 'range',
    title: 'Other teachers, other texts, either language',
    intro: 'The engine knows nothing about Nechama or Torah. These readings test it on Midrash, Mishnah and Talmud, with English-first and Hebrew-first texts, written by living teachers.',
  },
];

const HOME_POINTS = [
  {
    title: 'The text never leaves the screen',
    body: 'A source sheet lists texts one after another, and the verse scrolls away. Here the verse is pinned. Each commentary card lights the exact words it discusses and dims the rest.',
  },
  {
    title: 'The reader chooses the path',
    body: 'Where a teacher returned to a passage many times, the reader picks which lesson to take. Bereshit holds fifteen of Nechama’s gilyonot in one reading.',
  },
  {
    title: 'The primary sources, in place',
    body: 'Manuscript pages zoom to the line under discussion, and conflicting verses sit side by side. All of it comes from Sefaria’s library.',
  },
];

const HOME_PROOF = [
  {
    title: 'New readings are data, not code',
    body: 'Each reading is a single JSON file. The engine builds everything from it, with no build step and no per-reading code.',
  },
  {
    title: 'Every quote is traceable',
    body: 'In Bereshit, Nechama’s Hebrew is cut from her digitized sheets, never retyped. Each card cites its source sheet, and the digitization was checked against scans of the originals. Tests check that every quoted card is a verbatim slice of the sheet it cites.',
  },
  {
    title: 'Tested on every path',
    body: 'On every change, each branch of each reading is opened at desktop and phone sizes. The tests check that the right words light up, that nothing covers the text, and that history and back-navigation work.',
  },
  {
    title: 'A repeatable weekly cycle',
    body: 'Building a parsha is a scripted pipeline: snapshot her gilyonot, survey them, harvest the sources and questions, then build. At Nasso’s depth that is about six hours of work per parsha.',
  },
];

function buildHome() {
  document.title = 'Close Read: guided close readings of Jewish texts';
  document.body.classList.add('is-home');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const heroPath = '?sheet=bereshit&path=creation/cr-1963';

  const header = document.querySelector('.title-screen');
  header.className = 'home-hero';
  header.innerHTML = `
    <div class="home-hero-text">
      <div class="home-eyebrow">Close Read <span class="home-eyebrow-he">קריאה מקרוב</span></div>
      <h1 class="home-headline">A source sheet, taught.</h1>
      <p class="home-lede">
        Close Read turns a teacher’s source sheet into a guided reading. The verse stays on screen while
        her sources and questions scroll past it, each one lighting the words it is about. Where she taught a
        passage many times, the reader chooses which lesson to follow.
      </p>
      <div class="home-ctas">
        <a class="home-cta home-cta-primary" href="${heroPath}">Walk this path yourself</a>
        <a class="home-cta" href="#readings">See all the readings</a>
      </div>
    </div>
    <figure class="home-hero-media">
      <div class="home-video-frame">
        <video class="home-video" muted loop playsinline preload="${reduceMotion ? 'none' : 'auto'}"
          ${reduceMotion ? 'controls' : 'autoplay'}
          poster="assets/hero/bereshit-walkthrough.jpg"
          aria-label="Screen recording of the Bereshit reading: choosing The Days of Creation, then the 1963 lesson, then the Leningrad Codex with the scribe’s breaks between the days of creation highlighted.">
          <source src="assets/hero/bereshit-walkthrough.webm" type="video/webm">
          <source src="assets/hero/bereshit-walkthrough.mp4" type="video/mp4">
        </video>
      </div>
      <figcaption class="home-video-caption">
        Recorded from the live Bereshit reading. Choose a passage, then a year. Then the Leningrad Codex
        (1008&nbsp;CE) shows where the scribe ended each day of creation, and where chapter&nbsp;2 really begins.
      </figcaption>
    </figure>
  `;

  const main = document.getElementById('main-content');
  main.className = 'home-main';
  main.innerHTML = `
    <section class="home-points" aria-label="What Close Read does">
      ${HOME_POINTS.map(p => `
        <div class="home-point">
          <h2 class="home-point-title">${p.title}</h2>
          <p>${p.body}</p>
        </div>`).join('')}
    </section>
    <section class="home-readings" id="readings">
      <h2 class="home-section-title">What each reading shows</h2>
      <div class="home-categories"></div>
    </section>
    <section class="home-proof">
      <h2 class="home-section-title">Why it can scale</h2>
      <div class="home-proof-grid">
        ${HOME_PROOF.map(p => `
          <div class="home-proof-item">
            <h3>${p.title}</h3>
            <p>${p.body}</p>
          </div>`).join('')}
      </div>
    </section>
  `;

  const closing = document.querySelector('.closing-screen');
  closing.className = 'home-footer';
  closing.innerHTML = `
    <p>Close Read is a Sefaria experiment, built on Sefaria’s open library, API and manuscript collection.</p>
    <p><a href="https://github.com/Sefaria/close-read">Source on GitHub</a></p>
  `;

  fetch('data/index.json')
    .then(res => {
      if (!res.ok) throw new Error('Could not load sheet index');
      return res.json();
    })
    .then(sheets => renderReadings(sheets.filter(s => s.listed !== false)))
    .catch(err => {
      document.querySelector('.home-categories').innerHTML =
        `<p class="home-error">Could not load the readings. ${err.message}</p>`;
    });
}

function renderReadings(sheets) {
  const wrap = document.querySelector('.home-categories');
  HOME_CATEGORIES.forEach(cat => {
    const inCat = sheets.filter(s => s.category === cat.id);
    if (!inCat.length) return;
    const section = document.createElement('div');
    section.className = 'home-category';
    section.innerHTML = `
      <div class="home-category-head">
        <h3 class="home-category-title">${cat.title}</h3>
        <p class="home-category-intro">${cat.intro}</p>
      </div>
      <div class="home-card-grid" data-count="${inCat.length}"></div>
    `;
    const grid = section.querySelector('.home-card-grid');
    inCat.forEach(sheet => grid.appendChild(buildReadingCard(sheet)));
    wrap.appendChild(section);
  });
  // Anything listed but uncategorized still gets shown, last.
  const known = new Set(HOME_CATEGORIES.map(c => c.id));
  const rest = sheets.filter(s => !known.has(s.category));
  if (rest.length) {
    const grid = document.createElement('div');
    grid.className = 'home-card-grid';
    rest.forEach(sheet => grid.appendChild(buildReadingCard(sheet)));
    wrap.appendChild(grid);
  }
}

function buildReadingCard(sheet) {
  const card = document.createElement('article');
  card.className = 'home-card';
  const href = `?sheet=${sheet.slug}`;
  card.innerHTML = `
    <a class="index-card" href="${href}">
      ${sheet.title.he ? `<div class="home-card-title-he">${sheet.title.he}</div>` : ''}
      <div class="home-card-title-en">${sheet.title.en}</div>
      <div class="home-card-author">${sheet.author.en}</div>
      ${sheet.description ? `<p class="home-card-desc">${sheet.description}</p>` : ''}
      ${sheet.shows ? `<p class="home-card-shows"><span class="home-card-shows-label">What it shows</span>${sheet.shows}</p>` : ''}
    </a>
    ${sheet.demoPath ? `<a class="home-card-demo" href="${href}&path=${sheet.demoPath}">Try it: ${sheet.demoLabel}</a>` : ''}
  `;
  return card;
}
