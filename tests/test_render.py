"""Scroll every card of every branch at desktop and mobile sizes and check what
actually renders.

One test per (sheet, leaf path, viewport). Each path test scrolls the sections
that path is the first to reveal, so shared sections (overview, theme intros)
are scrolled once per viewport rather than once per leaf. Problems are
collected and reported together at the end of each test.

What a test checks:
- page: no console/page/network errors; fonts loaded; no "undefined" text;
  no horizontal scroll; the right sections shown/hidden for the path; nav
  (breadcrumb crumbs or section dots); closing screen visible at a leaf.
- each section panel: every pre-rendered verse has text and every word group
  actually wrapped.
- each card, while active: it is the only active card; the panel shows the
  verse the data says it should; highlighted ids lit (with effect class),
  everything else dimmed, no highlight state leaking to other sections, no
  dimmed words inside a highlighted phrase; highlighted words on screen,
  inside the panel and not covered; the whole verse on screen; the ref label
  not under the breadcrumb; the card itself readable (not covered by the
  sticky panel, not overlapping it on desktop).
"""

import json

import pytest

from sheetmodel import (
    build_tree, card_expectations, group_sections, leaf_paths, load_sheet,
    sheet_slugs, verses_of_group, visible_set,
)

MAX_REPORT = 60


def cases():
    out = []
    for slug in sheet_slugs():
        sheet = load_sheet(slug)
        tree = build_tree(sheet)
        groups = group_sections(sheet, tree)
        owned = set()
        for path in leaf_paths(sheet, tree):
            vis = set(visible_set(sheet, tree, path))
            mine = [g.dom_id for g in groups if not g.is_decision and g.dom_id in vis and g.dom_id not in owned]
            owned.update(mine)
            label = f"{slug}/{'/'.join(path)}" if path else slug
            out.append(pytest.param(slug, path, mine, id=label))
    return out


def sheet_url(base_url, slug, path):
    url = f"{base_url}/index.html?sheet={slug}"
    return url + (f"&path={'/'.join(path)}" if path else "")


def open_sheet(page, base_url, slug, path):
    page.goto(sheet_url(base_url, slug, path))
    page.wait_for_function(
        "() => window.ScrollTrigger && ScrollTrigger.getAll().length > 0"
        " && document.fonts.status === 'loaded'"
    )
    # engine refreshes ScrollTrigger at +200 ms and fits panels at +100 ms
    page.wait_for_timeout(400)


def collapse(problems):
    """Fold 'where: message' lines that share a message into one line."""
    by_msg = {}
    for p in problems:
        where, sep, msg = p.partition(": ")
        if not sep or "/" not in where:
            where, msg = "", p
        by_msg.setdefault(msg, []).append(where)
    out = []
    for msg, wheres in by_msg.items():
        wheres = [w for w in wheres if w]
        if len(wheres) > 3:
            out.append(f"{msg}  [{len(wheres)} cards: {', '.join(wheres[:3])}, …]")
        else:
            out += [f"{w}: {msg}" if w else msg for w in wheres] or [msg]
    return out


def report(problems, header):
    problems = collapse(problems)
    if problems:
        shown = "\n  ".join(problems[:MAX_REPORT])
        more = f"\n  … and {len(problems) - MAX_REPORT} more" if len(problems) > MAX_REPORT else ""
        pytest.fail(f"{header}: {len(problems)} problems\n  {shown}{more}", pytrace=False)


PAGE_PROBE = """(exp) => {
  const out = [];
  for (const f of ['Frank Ruhl Libre', 'Crimson Text', 'Inter']) {
    if (!document.fonts.check(`16px "${f}"`)) out.push(`font not loaded: ${f}`);
  }
  const text = document.body.innerText;
  for (const bad of ['undefined', '[object Object]', 'NaN']) {
    const i = text.indexOf(bad);
    if (i >= 0) out.push(`page text contains "${bad}": …${text.slice(Math.max(0, i - 40), i + 20).replace(/\\s+/g, ' ')}…`);
  }
  if (document.documentElement.scrollWidth > innerWidth + 1)
    out.push(`horizontal scroll: page is ${document.documentElement.scrollWidth}px wide in a ${innerWidth}px viewport`);
  for (const id of exp.groups) {
    const el = document.getElementById(id);
    if (!el) { out.push(`section ${id} not in DOM`); continue; }
    const shown = !el.classList.contains('is-hidden') && el.getBoundingClientRect().height > 0;
    if (exp.visible.includes(id) && !shown) out.push(`section ${id} should be visible on this path`);
    if (!exp.visible.includes(id) && shown) out.push(`section ${id} should be hidden on this path`);
  }
  const pill = document.querySelector('.section-nav.is-breadcrumb');
  if (pill) {
    const r = pill.getBoundingClientRect();
    if (pill.scrollWidth > pill.clientWidth + 1) out.push(`breadcrumb is cut off (${pill.scrollWidth}px of crumbs in a ${pill.clientWidth}px pill)`);
    if (r.left < 0 || r.right > innerWidth) out.push('breadcrumb runs off the screen');
    const here = [...pill.querySelectorAll('.breadcrumb-link')].pop();
    if (here && here.scrollWidth > here.clientWidth + 1) out.push(`current crumb truncated: "${here.textContent}"`);
  }
  const closing = document.querySelector('.closing-screen');
  if (closing && closing.classList.contains('is-hidden')) out.push('closing screen hidden at a leaf');
  const nav = document.querySelector('.section-nav');
  if (exp.branching) {
    const crumbs = [...nav.querySelectorAll('.breadcrumb-link')].map(b => b.textContent);
    if (JSON.stringify(crumbs) !== JSON.stringify(exp.crumbs))
      out.push(`breadcrumb ${JSON.stringify(crumbs)}, expected ${JSON.stringify(exp.crumbs)}`);
  } else {
    const dots = nav.querySelectorAll('.section-dot').length;
    if (dots !== exp.dots) out.push(`${dots} section dots, expected ${exp.dots}`);
  }
  return out;
}"""

PANEL_PROBE = """(exp) => {
  const out = [];
  const sec = document.getElementById(exp.group);
  const contents = [...sec.querySelectorAll('.primary-text-area .primary-text-content')];
  for (const v of exp.verses) {
    const c = contents.find(el => el.dataset.ref === v.ref);
    if (!c) { out.push(`${exp.group}: verse [${v.ref}] not rendered`); continue; }
    if (v.he && !c.querySelector('.primary-he')?.textContent.trim()) out.push(`${exp.group} [${v.ref}]: Hebrew empty`);
    if (!c.querySelector('.primary-en')?.textContent.trim()) out.push(`${exp.group} [${v.ref}]: English empty`);
    for (const [id, langs] of Object.entries(v.words)) {
      for (const lang of langs) {
        if (!c.querySelector(`.word-group[data-word="${CSS.escape(id)}"][data-lang="${lang}"]`))
          out.push(`${exp.group} [${v.ref}]: '${id}' (${lang}) never wrapped — cannot highlight`);
      }
    }
  }
  return out;
}"""

CARD_PROBE = """(exp) => {
  const out = [];
  const vh = innerHeight;
  const card = document.querySelector(`.step-card[data-step-id="${CSS.escape(exp.step)}"]`);
  const sec = document.getElementById(exp.group);
  const panel = sec.querySelector('.primary-text-area');
  const content = panel.querySelector('.primary-text-content.active');
  const desktop = innerWidth > 768;

  const active = [...document.querySelectorAll('.step-card.is-active')].map(c => c.dataset.stepId);
  if (active.length !== 1 || active[0] !== exp.step) out.push(`active cards: ${JSON.stringify(active)}`);
  if (panel.querySelectorAll('.primary-text-content.active').length !== 1) out.push('more than one active verse in panel');
  if (!content) return out.concat('no active verse in panel');
  if (content.dataset.ref !== exp.verse_ref) out.push(`panel shows [${content.dataset.ref}], expected [${exp.verse_ref}]`);

  // ── highlight state ──
  const hl = new Set(exp.highlight);
  const groups = [...content.querySelectorAll('.word-group')];
  document.querySelectorAll('.primary-text-content.has-highlights').forEach(el => {
    if (!sec.contains(el)) out.push(`has-highlights leaked to section ${el.closest('.cr-section')?.id}`);
  });
  if (hl.size) {
    if (!content.classList.contains('has-highlights')) out.push('panel missing has-highlights (rest of verse not dimmed)');
    for (const id of hl) {
      const sp = content.querySelectorAll(`.word-group[data-word="${CSS.escape(id)}"]`);
      if (!sp.length) out.push(`'${id}' has no span in the panel`);
      sp.forEach(s => {
        if (!s.classList.contains('highlighted')) out.push(`'${id}' (${s.dataset.lang}) not highlighted`);
        if (exp.effect === 'glow' || exp.effect === 'pulse') {
          if (!s.classList.contains(exp.effect)) out.push(`'${id}' (${s.dataset.lang}) missing ${exp.effect}`);
        }
        s.querySelectorAll('.word-group.dimmed').forEach(inner =>
          out.push(`'${inner.dataset.word}' renders dimmed inside highlighted '${id}' (${s.dataset.lang})`));
      });
    }
    groups.filter(s => !hl.has(s.dataset.word) && !s.closest('.word-group.highlighted'))
      .forEach(s => { if (!s.classList.contains('dimmed')) out.push(`'${s.dataset.word}' (${s.dataset.lang}) not dimmed`); });
  } else {
    if (content.classList.contains('has-highlights')) out.push('has-highlights on a step with no highlight');
    if (content.querySelector('.word-group.highlighted, .word-group.dimmed')) out.push('leftover highlight/dim state on a step with no highlight');
  }

  // ── visibility ──
  const pr = panel.getBoundingClientRect();
  const crumb = document.querySelector('.section-nav.is-breadcrumb');
  const cr = crumb && crumb.offsetParent !== null ? crumb.getBoundingClientRect() : null;
  const overlaps = (a, b) => a.left < b.right && b.left < a.right && a.top < b.bottom && b.top < a.bottom;
  const hits = (x, y, el) => { const h = document.elementFromPoint(x, y); return h && (h === el || el.contains(h)); };
  // What the eye sees at (x, y): the topmost element that actually paints
  // something. Transparent boxes don't hide anything (but may still eat taps).
  const paints = e => {
    const cs = getComputedStyle(e);
    return !/^(transparent|rgba\\(0, 0, 0, 0\\))$/.test(cs.backgroundColor) || cs.backgroundImage !== 'none'
      || parseFloat(cs.borderTopWidth) > 0 || [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
  };
  const seenBy = (x, y, el) => {
    for (const h of document.elementsFromPoint(x, y)) {
      if (h === el || el.contains(h)) return null;
      if (h.contains(el)) continue;
      if (paints(h)) return h;
    }
    return null;
  };
  const describe = h => h.closest('.primary-text-area') ? 'the sticky verse panel'
    : h.closest('.is-breadcrumb') ? 'the breadcrumb'
    : h.closest('.section-nav') ? 'the section-dots nav' : (h.className || h.tagName);

  const cc = content.getBoundingClientRect();
  if (cc.top < -1 || cc.bottom > vh + 1)
    out.push(`verse not fully on screen (spans ${Math.round(cc.top)}–${Math.round(cc.bottom)}px of ${vh}px)`);
  if (desktop && cc.bottom > pr.bottom + 1) out.push(`verse overflows its panel by ${Math.round(cc.bottom - pr.bottom)}px`);
  const en = content.querySelectorAll('.primary-en');
  if ([...en].some(e => getComputedStyle(e).display === 'none')) {
    // Hiding the caption is fitToPanel's last resort, for a passage that can't
    // fit even at the floor sizes (14px Hebrew / 12px English). Anything else
    // is a sizing bug.
    const els = [...content.querySelectorAll('.primary-he, .primary-en')];
    const saved = els.map(e => e.style.cssText);
    els.forEach(e => { e.style.display = ''; e.style.fontSize = e.classList.contains('primary-he') ? '14px' : '12px'; });
    const pcs = getComputedStyle(panel);
    const fitsAtFloor = content.scrollHeight <= panel.clientHeight - parseFloat(pcs.paddingTop) - parseFloat(pcs.paddingBottom);
    els.forEach((e, i) => { e.style.cssText = saved[i]; });
    if (fitsAtFloor) out.push('English caption hidden although the verse fits at the minimum font sizes');
  }
  const ref = content.querySelector('.primary-ref');
  if (ref && cr && overlaps(ref.getBoundingClientRect(), cr)) out.push('verse ref label is under the breadcrumb');

  const seen = new Set();
  for (const id of hl) {
    content.querySelectorAll(`.word-group[data-word="${CSS.escape(id)}"]`).forEach(s => {
      if (getComputedStyle(s).display === 'none' || s.closest('[style*="display: none"]')) return;
      const key = `${id}/${s.dataset.lang}`;
      for (const r of s.getClientRects()) {
        if (r.width === 0 || seen.has(key)) continue;
        let why = null;
        if (r.top < 0 || r.bottom > vh) why = 'off screen';
        else if (r.top < pr.top - 1 || r.bottom > pr.bottom + 1) why = 'clipped by the panel';
        else { const cover = seenBy(r.left + r.width / 2, r.top + r.height / 2, s); if (cover) why = `covered by ${describe(cover)}`; }
        if (why) { seen.add(key); out.push(`highlighted '${id}' (${s.dataset.lang}) ${why}`); }
      }
    });
  }

  // ── the card itself ──
  const inner = card.querySelector('.card-inner');
  const text = inner.innerText.trim();
  if (!text) out.push('card has no text');
  const ir = inner.getBoundingClientRect();
  if (desktop && overlaps(ir, pr)) out.push('card overlaps the verse panel');
  const top = Math.max(ir.top, 0), bottom = Math.min(ir.bottom, vh);
  if (bottom - top < Math.min(ir.height, 80)) {
    out.push(`card barely on screen (${Math.round(Math.max(0, bottom - top))}px visible)`);
  } else {
    let n = 0, covered = 0, cover = null;
    const blockers = new Set();
    for (let i = 1; i <= 5; i++) for (let j = 1; j <= 5; j++) {
      const x = ir.left + ir.width * j / 6, y = top + (bottom - top) * i / 6;
      n++;
      const c = seenBy(x, y, inner);
      if (c) { covered++; cover = cover || c; }
      else if (!hits(x, y, inner)) blockers.add(describe(document.elementFromPoint(x, y)));
    }
    if (covered / n > 0.4) out.push(`card ${Math.round(100 * covered / n)}% covered by ${describe(cover)}`);
    for (const b of blockers) out.push(`taps on the card are caught by invisible ${b}`);
  }

  // ── fixed nav painted over text ──
  const navBits = [...document.querySelectorAll('.section-dot, .section-nav.is-breadcrumb')]
    .map(e => [e, e.getBoundingClientRect()]).filter(([, r]) => r.width > 0 && r.height > 0);
  const lines = el => { const rg = document.createRange(); rg.selectNodeContents(el); return [...rg.getClientRects()]; };
  for (const [name, el] of [['verse', content], ['card', inner]]) {
    const hit = navBits.find(([, r]) => lines(el).some(t => overlaps(t, r)));
    if (hit) out.push(`${describe(hit[0])} is drawn over the ${name} text`);
  }
  return out;
}"""


def crumbs_for(sheet, tree, path):
    first = next(s for s in sheet["sections"] if s.get("type") != "decision" and s["id"] not in tree.targets)
    out = [first["title"]["en"]]
    from sheetmodel import open_decision
    for i, seg in enumerate(path):
        dec = open_decision(sheet, tree, path[:i])
        out.append(next(b for b in dec["branches"] if b["id"] == seg)["label"]["en"])
    return out


@pytest.mark.parametrize("slug,path,owned", cases())
def test_scroll_path(page, base_url, slug, path, owned):
    sheet = load_sheet(slug)
    tree = build_tree(sheet)
    groups = group_sections(sheet, tree)
    vis = visible_set(sheet, tree, path)
    problems = []

    open_sheet(page, base_url, slug, path)
    problems += page.evaluate(PAGE_PROBE, {
        "groups": [g.dom_id for g in groups],
        "visible": [g.dom_id for g in groups if g.dom_id in vis],
        "branching": tree.branching,
        "crumbs": crumbs_for(sheet, tree, path) if tree.branching else [],
        "dots": sum(len(g.sections) for g in groups if not g.is_decision),
    })

    for g in groups:
        if g.dom_id not in owned:
            continue
        problems += page.evaluate(PANEL_PROBE, {
            "group": g.dom_id,
            "verses": [{
                "ref": v["ref"],
                "he": bool(v.get("he") or v.get("left", {}).get("he")),
                "words": {k: [l for l in ("he", "en") if w.get(l)] for k, w in (v.get("words") or {}).items()},
            } for v in verses_of_group(g)],
        })

    for c in card_expectations(sheet, groups):
        if c["group"] not in owned:
            continue
        where = f"{c['section']}/{c['step']}"
        page.evaluate(
            """(id) => {
              // Scroll like a reader: the card's text centered on screen, or
              // its top near the top of the screen if it is taller than that.
              // Either way the card sits inside its trigger zone (top 55% /
              // bottom 40%) and its neighbours sit outside theirs.
              const c = document.querySelector(`.step-card[data-step-id="${CSS.escape(id)}"] .card-inner`);
              const r = c.getBoundingClientRect();
              const y = r.height > 0.8 * innerHeight
                ? r.top + scrollY - 0.1 * innerHeight
                : r.top + scrollY + r.height / 2 - 0.5 * innerHeight;
              window.scrollTo({ top: y, behavior: 'instant' });
            }""", c["step"])
        try:
            page.wait_for_function(
                """([id, group, ref]) => {
                  const c = document.querySelector(`.step-card[data-step-id="${CSS.escape(id)}"]`);
                  const a = document.getElementById(group).querySelector('.primary-text-area .primary-text-content.active');
                  return c.classList.contains('is-active') && a && a.dataset.ref === ref
                    && !a.classList.contains('fading-out') && getComputedStyle(a).opacity === '1';
                }""", arg=[c["step"], c["group"], c["verse_ref"]], timeout=3000)
        except Exception:
            pass  # the probe below says exactly what is wrong
        problems += [f"{where}: {p}" for p in page.evaluate(CARD_PROBE, c)]

    problems += page.problems
    report(problems, f"{slug} {'/'.join(path) or '(linear)'}")


BRANCHING = [s for s in sheet_slugs() if build_tree(load_sheet(s)).branching]


@pytest.mark.parametrize("slug", BRANCHING)
def test_branch_clicks_and_history(page, base_url, slug):
    """Click down one route through every level, then walk back with history."""
    sheet = load_sheet(slug)
    tree = build_tree(sheet)
    from sheetmodel import open_decision
    problems = []
    open_sheet(page, base_url, slug, [])

    if not page.locator(".closing-screen").evaluate("e => e.classList.contains('is-hidden')"):
        problems.append("closing screen visible before any choice (should block at the first decision)")

    path = []
    while (dec := open_decision(sheet, tree, path)) is not None:
        branch = dec["branches"][-1]
        btn = page.locator(f'[id="{dec["id"]}"] .decision-branch-button').nth(len(dec["branches"]) - 1)
        btn.scroll_into_view_if_needed()
        btn.click()
        path.append(branch["id"])
        try:
            page.wait_for_function("(p) => new URLSearchParams(location.search).get('path') === p", arg="/".join(path), timeout=2000)
        except Exception:
            problems.append(f"after clicking {dec['id']}/{branch['id']}: URL is {page.url}")
        if not btn.evaluate("e => e.classList.contains('is-chosen')"):
            problems.append(f"{dec['id']}/{branch['id']}: button not marked chosen")
        target = page.locator(f'[id="{branch["target"]}"]')
        if target.evaluate("e => e.classList.contains('is-hidden')"):
            problems.append(f"{branch['target']}: still hidden after choosing it")
        crumbs = page.locator(".breadcrumb-link").all_text_contents()
        if crumbs != crumbs_for(sheet, tree, path):
            problems.append(f"breadcrumb {crumbs} after choosing {'/'.join(path)}")

    if page.locator(".closing-screen").evaluate("e => e.classList.contains('is-hidden')"):
        problems.append("closing screen still hidden at a leaf")

    while path:
        page.go_back()
        path.pop()
        expect = "/".join(path) or None
        try:
            page.wait_for_function("(p) => new URLSearchParams(location.search).get('path') === p", arg=expect, timeout=2000)
        except Exception:
            problems.append(f"back button: URL {page.url}, expected path {expect}")
        vis = set(visible_set(sheet, tree, path))
        hidden_wrong = page.evaluate(
            "(vis) => [...document.querySelectorAll('.cr-section')].filter(e => vis.includes(e.id) === e.classList.contains('is-hidden')).map(e => e.id)",
            list(vis))
        if hidden_wrong:
            problems.append(f"after back to '{expect}': wrong visibility for {hidden_wrong}")

    report(problems + page.problems, f"{slug} branch clicks")


@pytest.mark.parametrize("slug", BRANCHING)
def test_invalid_path_falls_back_to_root(page, base_url, slug):
    sheet = load_sheet(slug)
    tree = build_tree(sheet)
    open_sheet(page, base_url, slug, ["no-such-branch", "nor-this"])
    vis = set(visible_set(sheet, tree, []))
    wrong = page.evaluate(
        "(vis) => [...document.querySelectorAll('.cr-section')].filter(e => vis.includes(e.id) === e.classList.contains('is-hidden')).map(e => e.id)",
        list(vis))
    report(([f"wrong visibility for {wrong}"] if wrong else []) + page.problems, f"{slug} invalid path")


def test_index_page_lists_every_sheet(page, base_url):
    page.goto(base_url + "/index.html")
    page.wait_for_selector(".index-card")
    hrefs = page.locator(".index-card").evaluate_all("els => els.map(e => new URL(e.href).searchParams.get('sheet'))")
    missing = [s for s in sheet_slugs() if s not in hrefs]
    report(([f"index page missing {missing}"] if missing else []) + page.problems, "index page")
