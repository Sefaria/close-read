"""Static checks on data/*.json — no browser, runs in well under a second.

Each test collects every problem in a sheet before failing, so one run shows
the whole list rather than the first error.
"""

import re

import pytest

# Open editorial questions: tests stay visible as xfail until decided.
PENDING = {
    ("first-step", "nasso"): "nasso's theme intros light the whole passage on purpose (2026-05 highlight audit); CLAUDE.md says intros don't highlight",
    ("en-repeat", "minhag-overview"): "Talmud text repeats the phrase; decide whether both copies should light up",
}


def pending(kind, slugs):
    return [pytest.param(s, marks=pytest.mark.xfail(reason=PENDING[(kind, s)], strict=True)) if (kind, s) in PENDING else s
            for s in slugs]


from sheetmodel import (
    DATA, build_tree, card_expectations, group_sections, is_image, leaf_paths, load_index,
    load_sheet, sheet_slugs, verse_sides, verses_of_group, visible_set,
)

SLUGS = sheet_slugs()
EFFECTS = {None, "highlight", "glow", "pulse"}


def fail_if(problems, what):
    if problems:
        shown = "\n  ".join(problems[:80])
        more = f"\n  … and {len(problems) - 80} more" if len(problems) > 80 else ""
        pytest.fail(f"{len(problems)} {what}:\n  {shown}{more}", pytrace=False)


# ─── Mirror of TextEffects._wrapPhrase's matcher ───

def js_regex_escape(s):
    return re.sub(r"[.*+?^${}()|\[\]\\]", lambda m: "\\" + m.group(0), s)


def wrap_pattern(phrase):
    escaped = js_regex_escape(phrase)
    return re.compile(re.sub(r"[\s​ ]+", lambda _: "[\\s​ ־-]*", escaped))


def spans(text, phrase):
    return [m.span() for m in wrap_pattern(phrase).finditer(text) if m.end() > m.start()]


# ─── Tests ───

def test_index_is_complete():
    """Every sheet file is in index.json and every index entry has a file."""
    problems = []
    listed = set()
    for entry in load_index():
        slug = entry["slug"]
        listed.add(slug)
        if not (DATA / f"{slug}.json").exists():
            problems.append(f"{slug}: listed in index.json but data/{slug}.json is missing")
        if not entry.get("title", {}).get("en"):
            problems.append(f"{slug}: index entry has no title.en")
        if not entry.get("author", {}).get("en"):
            problems.append(f"{slug}: index entry has no author.en")
    for f in DATA.rglob("*.json"):
        slug = str(f.relative_to(DATA).with_suffix(""))
        if slug != "index" and slug not in listed:
            problems.append(f"{slug}: data file not registered in index.json")
    fail_if(problems, "index problems")


def simulate_wrap(text, words, lang):
    """Replay TextEffects.wrapWords on one text element, in words-map order.

    Returns {id: [ids of word-group spans this id's span sits inside]} for every
    id that got wrapped; ids missing from the result never wrapped.
    """
    html = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for wid, w in words.items():
        phrase = w.get(lang)
        if not phrase or f'data-word="{wid}" data-lang="{lang}"' in html:
            continue
        pat = wrap_pattern(phrase)
        html = pat.sub(lambda m: f'<span class="word-group" data-word="{wid}" data-lang="{lang}">{m.group(0)}</span>', html)
    wrapped, stack = {}, []
    for m in re.finditer(r'<span class="word-group" data-word="([^"]+)" data-lang="[^"]+">|</span>', html):
        if m.group(1):
            wrapped.setdefault(m.group(1), set()).update(stack)
            stack.append(m.group(1))
        else:
            stack.pop()
    return wrapped


@pytest.mark.parametrize("slug", SLUGS)
def test_word_groups_wrap_cleanly(slug):
    """Replays the engine's wrap on every verse and checks the outcome.

    - Every phrase must be found in the verse text.
    - A phrase that overlaps an already-wrapped one cannot match across the
      span tag and silently never wraps.
    - A phrase wrapped *inside* another is fine on its own, but a step that
      highlights the outer phrase without the inner one renders the inner words
      dimmed in the middle of the highlight.
    - An id shared by sub-sections on one panel must mean the same phrase
      (later sub-sections overwrite earlier ones in the merged map).
    """
    sheet = load_sheet(slug)
    problems = []
    groups = group_sections(sheet)
    nested = {}   # (group, verse ref) -> {inner: outers}
    for g in groups:
        if g.is_decision:
            continue
        seen = {}
        for s in g.sections:
            for wid, w in (s["primaryText"].get("words") or {}).items():
                if wid in seen and seen[wid] != (w.get("he"), w.get("en")):
                    problems.append(f"{g.dom_id}: word id '{wid}' defined differently in two sub-sections sharing the panel")
                seen[wid] = (w.get("he"), w.get("en"))

        for verse in verses_of_group(g):
            where = f"{g.dom_id} [{verse['ref']}]"
            words = verse.get("words") or {}
            sides = verse_sides(verse)
            for lang in ("he", "en"):
                got = {}
                for label, he, en, _ in sides:
                    for wid, outers in simulate_wrap(he if lang == "he" else en, words, lang).items():
                        got.setdefault(wid, set()).update(outers)
                for wid, w in words.items():
                    phrase = w.get(lang)
                    if not phrase:
                        continue
                    occurrences = sum(len(spans(he if lang == "he" else en, phrase)) for _, he, en, _ in sides)
                    if occurrences == 0:
                        problems.append(f"{where}: {lang.upper()} '{wid}' not found in verse text: {phrase!r}")
                    elif wid not in got:
                        problems.append(f"{where}: {lang.upper()} '{wid}' overlaps another phrase and never wraps: {phrase!r}")
                    if wid in got and got[wid]:
                        nested.setdefault((g.dom_id, verse["ref"]), {}).setdefault(wid, set()).update(got[wid])

    for c in card_expectations(sheet, groups):
        inner_map = nested.get((c["group"], c["verse_ref"]), {})
        hl = set(c["highlight"])
        for inner, outers in inner_map.items():
            if inner not in hl and outers & hl:
                problems.append(f"{c['section']}/{c['step']}: highlights {sorted(outers & hl)} but nested '{inner}' inside it renders dimmed")
    fail_if(problems, "word-group problems")


@pytest.mark.parametrize("slug", pending("en-repeat", SLUGS))
def test_english_phrases_occur_once(slug):
    """The wrap regex is global, so an EN phrase that occurs twice lights up twice."""
    sheet = load_sheet(slug)
    problems = []
    for g in group_sections(sheet):
        if g.is_decision:
            continue
        for verse in verses_of_group(g):
            sides = verse_sides(verse)
            for wid, w in (verse.get("words") or {}).items():
                if w.get("en"):
                    n = sum(len(spans(en, w["en"])) for _, _, en, _ in sides)
                    if n > 1:
                        problems.append(f"{g.dom_id} [{verse['ref']}]: EN '{wid}' occurs {n}x: {w['en']!r}")
    fail_if(problems, "repeated English phrases")


@pytest.mark.parametrize("slug", SLUGS)
def test_highlights_resolve_to_active_verse(slug):
    """Every highlight id exists in the verse the panel shows for that step."""
    sheet = load_sheet(slug)
    problems = []
    for c in card_expectations(sheet):
        missing = [h for h in c["highlight"] if h not in c["verse_words"]]
        if missing:
            problems.append(f"{c['section']}/{c['step']}: highlight {missing} not in words of [{c['verse_ref']}]")
        if c["effect"] not in EFFECTS:
            problems.append(f"{c['section']}/{c['step']}: unknown effect {c['effect']!r}")
    fail_if(problems, "unresolvable highlights")


@pytest.mark.parametrize("slug", pending("first-step", SLUGS))
def test_first_step_lets_verse_breathe(slug):
    """The first step of each section has no highlight (design decision in CLAUDE.md)."""
    sheet = load_sheet(slug)
    problems = []
    for s in sheet["sections"]:
        steps = [st for st in s.get("steps", []) if st["type"] != "verse-change"]
        if steps and steps[0].get("highlight"):
            problems.append(f"{s['id']}/{steps[0]['id']}: first step highlights {steps[0]['highlight']}")
    fail_if(problems, "sections whose first step highlights")


@pytest.mark.parametrize("slug", SLUGS)
def test_steps_are_well_formed(slug):
    sheet = load_sheet(slug)
    problems = []
    step_ids = {}
    section_ids = set()
    for s in sheet["sections"]:
        if s["id"] in section_ids:
            problems.append(f"duplicate section id {s['id']}")
        section_ids.add(s["id"])
        if s.get("type") == "decision":
            continue
        if not s.get("title", {}).get("en"):
            problems.append(f"{s['id']}: section has no title.en")
        for st in s.get("steps", []):
            where = f"{s['id']}/{st.get('id')}"
            if st.get("id") in step_ids:
                problems.append(f"{where}: step id also used in {step_ids[st['id']]}")
            step_ids[st.get("id")] = s["id"]
            t = st.get("type")
            if t == "verse-change":
                nv = st.get("newVerse") or {}
                if not nv.get("ref"):
                    problems.append(f"{where}: verse-change without newVerse.ref")
                continue
            if t not in {"narration", "commentary", "question"}:
                problems.append(f"{where}: unknown step type {t!r}")
                continue
            if not (st.get("text") or {}).get("en", "").strip():
                problems.append(f"{where}: empty text.en")
            if t == "commentary":
                if not st.get("source"):
                    problems.append(f"{where}: commentary without source")
                if not (st.get("sourceLabel") or {}).get("en"):
                    problems.append(f"{where}: commentary without sourceLabel.en (renders 'undefined')")
    # crossfade matches pre-rendered verses by data-ref, so refs must be unique per panel
    for g in group_sections(sheet):
        if g.is_decision:
            continue
        refs = {}
        for v in verses_of_group(g):
            key = v["src"] if is_image(v) else (v.get("he") if v.get("mode") != "comparison" else v["left"]["he"])
            if v["ref"] in refs and refs[v["ref"]] != key:
                problems.append(f"{g.dom_id}: two different verses share ref {v['ref']!r} — crossfade can't tell them apart")
            refs[v["ref"]] = key
    fail_if(problems, "malformed steps")


@pytest.mark.parametrize("slug", [s for s in SLUGS if build_tree(load_sheet(s)).branching])
def test_branching_structure(slug):
    """Every branch target exists, every reading section is reachable by some
    path, and every leaf path ends on a reading section."""
    sheet = load_sheet(slug)
    tree = build_tree(sheet)
    by_id = {s["id"]: s for s in sheet["sections"]}
    problems = []
    for dec in tree.decisions.values():
        ids = [b["id"] for b in dec["branches"]]
        if len(ids) != len(set(ids)):
            problems.append(f"{dec['id']}: duplicate branch ids")
        for b in dec["branches"]:
            t = by_id.get(b["target"])
            if t is None:
                problems.append(f"{dec['id']}/{b['id']}: target {b['target']!r} does not exist")
            elif t.get("type") == "decision":
                problems.append(f"{dec['id']}/{b['id']}: target {b['target']!r} is a decision")
            if not b.get("label", {}).get("en"):
                problems.append(f"{dec['id']}/{b['id']}: branch without label.en")
        if not dec.get("prompt", {}).get("en"):
            problems.append(f"{dec['id']}: decision without prompt.en")

    for s in sheet["sections"]:
        if s.get("titleCard") is False and s["id"] in tree.targets:
            problems.append(f"{s['id']}: a branch target can't be a continuation (titleCard: false)")
    if sheet["sections"] and sheet["sections"][0].get("titleCard") is False:
        problems.append(f"{sheet['sections'][0]['id']}: the first section can't be a continuation")

    reachable = set()
    for path in leaf_paths(sheet, tree):
        vis = visible_set(sheet, tree, path)
        reachable.update(vis)
        if by_id[vis[-1]].get("type") == "decision":
            problems.append(f"path {'/'.join(path)}: ends on an unanswered decision {vis[-1]}")
    for s in sheet["sections"]:
        if s["id"] not in reachable:
            problems.append(f"{s['id']}: not reachable by any path")
    fail_if(problems, "branching problems")


IMAGE_SLUGS = [s for s in SLUGS if any(is_image(v) for g in group_sections(load_sheet(s)) if not g.is_decision for v in verses_of_group(g))]


@pytest.mark.parametrize("slug", IMAGE_SLUGS)
def test_images_are_well_formed(slug):
    """Image panels: the fields the engine needs, every region inside the image,
    and every region used by some step (an unused region is usually a typo'd id)."""
    sheet = load_sheet(slug)
    problems = []
    used = {}
    for c in card_expectations(sheet):
        if c["verse_mode"] == "image":
            used.setdefault(c["verse_ref"], set()).update(c["highlight"])
    for g in group_sections(sheet):
        if g.is_decision:
            continue
        for v in verses_of_group(g):
            if not is_image(v):
                continue
            where = f"{g.dom_id} [{v['ref']}]"
            for k in ("src", "alt"):
                if not str(v.get(k) or "").strip():
                    problems.append(f"{where}: image without {k}")
            for k in ("width", "height"):
                if not isinstance(v.get(k), (int, float)) or v[k] <= 0:
                    problems.append(f"{where}: image needs a positive numeric {k} (layout is computed from it)")
            if not (v.get("credit") or {}).get("en"):
                problems.append(f"{where}: image without credit.en")
            for rid, r in (v.get("regions") or {}).items():
                try:
                    x, y, w, h = (float(r[k]) for k in ("x", "y", "w", "h"))
                except (KeyError, TypeError, ValueError):
                    problems.append(f"{where}: region '{rid}' needs numeric x, y, w, h")
                    continue
                if w <= 0 or h <= 0 or x < 0 or y < 0 or x + w > 1 or y + h > 1:
                    problems.append(f"{where}: region '{rid}' is not inside the image (fractions 0–1)")
                if rid not in used.get(v["ref"], set()):
                    problems.append(f"{where}: region '{rid}' is never highlighted")
    fail_if(problems, "image problems")


def test_continuation_follows_its_branch():
    """A `titleCard: false` section after a branch target is shown only on that branch's path."""
    pt = {"ref": "x", "he": "א", "en": "a"}
    sheet = {"title": {"en": "t"}, "sections": [
        {"id": "ov", "title": {"en": "o"}, "primaryText": pt, "steps": []},
        {"id": "fork", "type": "decision", "level": 0, "prompt": {"en": "?"}, "branches": [
            {"id": "a", "label": {"en": "A"}, "target": "leaf-a"},
            {"id": "b", "label": {"en": "B"}, "target": "leaf-b"}]},
        {"id": "leaf-a", "title": {"en": "A"}, "primaryText": pt, "steps": []},
        {"id": "leaf-a-page", "titleCard": False, "title": {"en": "A page"}, "primaryText": {**pt, "ref": "y"}, "steps": []},
        {"id": "leaf-b", "title": {"en": "B"}, "primaryText": pt, "steps": []},
    ]}
    tree = build_tree(sheet)
    assert "leaf-a-page" in visible_set(sheet, tree, ["a"])
    assert "leaf-a-page" not in visible_set(sheet, tree, ["b"])
    assert "leaf-a-page" not in visible_set(sheet, tree, [])
