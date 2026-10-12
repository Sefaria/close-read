// Close Read homepage
// Makes the case twice: for learners (what reading one is like) and for
// teachers (what making one takes), then shows the readings on one screen.
// Readings come from data/index.json; entries with "listed": false are retired
// from this page but still load by URL (and are still tested).

// Tile order and default tag for each index.json `category` (an entry's own `tag` overrides it).
const HOME_CATEGORIES = [
  { id: 'branching', tag: 'Branching paths' },
  { id: 'single', tag: 'One sheet' },
  { id: 'range', tag: 'Other texts & teachers' },
];

const HOME_LEARNER_POINTS = [
  {
    title: 'Engaging like video, paced like reading',
    body: 'The verse stays on screen. Each scroll brings the next source or question and lights the words it is about. The reader moves on when they are ready, not when the video does.',
  },
  {
    title: 'Paths to follow, and every branch pays off',
    body: 'The reader chooses a passage, then a year of the teacher’s lessons on it. Each branch is a complete lesson with its own sources and questions, not a teaser for the next one.',
  },
  {
    title: 'Impossible to get lost',
    body: 'A breadcrumb always shows where you are and how you got there. The text never scrolls away, and Back takes you to your last choice.',
  },
];

const HOME_TEACHER_POINTS = [
  {
    title: 'Minutes',
    body: 'Readings like these used to need a designer and a developer for every highlight, transition and branch. Now AI builds them from the teacher’s material. A Nechama reading, dense with layered sources, takes about half an hour. Most teachers’ material is quicker.',
  },
  {
    title: 'The teacher’s Torah, kept intact',
    body: 'The sources and questions are the teacher’s own. In Bereshit every quote is cut word for word from her sheets and cited, and the tests fail if one drifts.',
  },
  {
    title: 'A new way to reach students',
    body: 'A source sheet becomes something students open on a phone and follow on their own. Teachers get a new medium without having to learn one.',
  },
];

function buildHome() {
  document.title = 'Close Read: Torah study that moves at the learner’s pace';
  document.body.classList.add('is-home');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const heroPath = 'read/bereshit/?path=creation/cr-1963';

  const header = document.querySelector('.title-screen');
  header.className = 'home-hero';
  header.innerHTML = `
    <div class="home-hero-text">
      <div class="home-eyebrow">Close Read <span class="home-eyebrow-he">קריאה מקרוב</span></div>
      <h1 class="home-headline">The pull of video, at the learner’s pace.</h1>
      <p class="home-lede">
        Close Read turns a teacher’s Torah into a guided reading. The text stays in view while sources
        and questions arrive one at a time, lighting the words they discuss. Learners choose their path,
        get a full lesson down every branch, and never lose their place.
      </p>
      <div class="home-ctas">
        <a class="home-cta home-cta-primary" href="${heroPath}">Try this path yourself</a>
        <a class="home-cta" href="#readings">See the readings</a>
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

  const points = list => list.map(p => `
    <div class="home-point">
      <h3 class="home-point-title">${p.title}</h3>
      <p>${p.body}</p>
    </div>`).join('');

  const main = document.getElementById('main-content');
  main.className = 'home-main';
  main.innerHTML = `
    <section class="home-pitch" aria-labelledby="home-learners">
      <div class="home-pitch-head">
        <div class="home-section-title">For learners</div>
        <h2 class="home-pitch-title" id="home-learners">A lesson they follow, not a page they scroll past.</h2>
      </div>
      <div class="home-points">${points(HOME_LEARNER_POINTS)}</div>
    </section>
    <section class="home-pitch home-pitch-teachers" aria-labelledby="home-teachers">
      <div class="home-pitch-head">
        <div class="home-section-title">For teachers</div>
        <h2 class="home-pitch-title" id="home-teachers">The teacher brings the Torah. We make it compelling.</h2>
      </div>
      <div class="home-points">${points(HOME_TEACHER_POINTS)}</div>
    </section>
    <section class="home-readings" id="readings" aria-labelledby="home-readings-title">
      <div class="home-readings-head">
        <h2 class="home-pitch-title" id="home-readings-title">The readings</h2>
        <p>Each one is here for something the others don’t show.</p>
      </div>
      <div class="home-card-grid"></div>
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
      document.querySelector('.home-card-grid').innerHTML =
        `<p class="home-error">Could not load the readings. ${err.message}</p>`;
    });
}

function renderReadings(sheets) {
  const grid = document.querySelector('.home-card-grid');
  const rank = id => {
    const i = HOME_CATEGORIES.findIndex(c => c.id === id);
    return i < 0 ? HOME_CATEGORIES.length : i;
  };
  [...sheets]
    .sort((a, b) => rank(a.category) - rank(b.category))
    .forEach(sheet => grid.appendChild(buildReadingCard(sheet)));
}

function buildReadingCard(sheet) {
  const cat = HOME_CATEGORIES.find(c => c.id === sheet.category);
  const card = document.createElement('article');
  card.className = 'home-card';
  card.dataset.category = sheet.category || '';
  // read/<slug>/ is the generated share page (its own link preview); see scripts/build_previews.py.
  const href = `read/${sheet.slug}/`;
  card.innerHTML = `
    <a class="index-card" href="${href}">
      ${sheet.tag || cat ? `<span class="home-card-tag">${sheet.tag || cat.tag}</span>` : ''}
      <span class="home-card-title-en">${sheet.title.en}</span>
      <span class="home-card-author">${sheet.author.en}</span>
      ${sheet.shows ? `<span class="home-card-shows">${sheet.shows}</span>` : ''}
    </a>
    ${sheet.demoPath ? `<a class="home-card-demo" href="${href}?path=${sheet.demoPath}">Try: ${sheet.demoLabel}</a>` : ''}
  `;
  return card;
}
