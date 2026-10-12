# Brief: drafting Noach leaves (Stage 4)

You're turning Nechama Leibowitz's study sheets (gilyonot) into Close Read leaves: scrolling
cards on the left, a pinned verse (or image) on the right whose phrases light up as each card
is read. **We're taking her thinking from one form into another.** The reader experiences the
content (her chosen sources, her questions, the verse), not narration about her sheet.

The worked examples are Bereshit's: `leaf_1963` in `research/scripts/bereshit_leaves/creation.py`
and `leaf_1942` in `research/scripts/bereshit_leaves/cain.py`. Read them first, and copy their
shape and voice. Noach leaves go in `research/scripts/noach_leaves/<theme>.py` and start with
`from noach_lib import *  # noqa: F401,F403`.

## Inputs (all checked; don't go around them)

- **Harvest:** `research/parshiyot/noach-harvest/<theme>/<year>.json`. Every item has
  `i`, `kind`, `he`, often `ref`/`en`, `basis`, and scan-check fields. This is the **only**
  source of her Hebrew and of source texts.
- **Scan check:** `research/parshiyot/noach-scancheck/<sheet>-<year>.md`. For each source
  it gives her start/stop points (`EXPANDED (start: …; stop: …)`, `החל מן … עד …`) and her
  scan headers.
- **Triage:** `noach-scancheck/triage.json`. Items with `use: open` must be settled from
  the cited text before you quote them (see your assignment); if you can't settle one, don't
  quote it.
- **Design:** `research/parshiyot/noach.md` §7 (which sections to render) and §2 (fidelity).
- **Library:** `research/scripts/nechama_lib.py (via noach_lib.py)`: `harvest`, `item`, `cut`, `underline`,
  `narration`, `commentary`, `question`, `primary`, `verse_set`, `words`, `vp`.
- **Verses:** `research/parshiyot/noach-verses.json`, read by `primary()`. MAM Hebrew
  plus JPS English ("the Lord" for the divine name).

## Hard rules (a test enforces the first four)

1. **Never type her Hebrew, or a source's.** Every commentary/question card goes through
   `commentary(...)` / `question(...)` with the harvest index; its Hebrew is `cut(item,
   start, stop)`, a verbatim slice. `tests/test_provenance.py` fails otherwise.
2. **Never type verse Hebrew.** Word groups come from `primary(ref, keys, {id: (bare letters,
   English phrase)})`, which finds the pointed phrase in the cached verse. The English phrase
   must occur **exactly once** in the panel's English, and no two phrases may overlap.
3. **The first step of every section has no `highlight`** (the verse breathes first).
4. **Don't quote** items with `exclude`, `publish: false`, or an unsettled `triage.use: open`.
5. **Honor her start/stop points.** Where the scan check records a stop (`עד …`) or start
   (`החל מן …`), slice there. If the phrase isn't in the digitized text, the digitizer
   attached a different passage: quote less, or not at all, and note it.
6. **A source marked NOT-IN-SCAN** (the digitizer supplied text she didn't print) may be
   quoted only if one of her questions in that section names that source. Note it.
7. **Her questions:** hers only, her Hebrew, and our faithful English translation. You may
   **omit** questions (density, or a dependency on a source not on the sheet); never invent,
   merge or paraphrase one. Keep her number prefix ("1.") as in the harvest.
8. **Sources keep her order.** A question may follow the source it asks about.
9. **English:** `en_basis: "ours"`, a faithful plain translation of exactly the slice.
   `"sefaria"` (the item's own `en`) only if you quote the **whole** item **and** it's
   the full canonical text. Her quotes are usually abridged, so default to ours.
   Transliteration style follows 1963: "R.", "Shabbat", "Va-yekhullu".
10. **Narration is content-only and minimal:** point at the verse ("The end of the sixth
    day.") or at what's on an image. Never "her sheet / her next section / she adds…", never a
    gilayon year in a card, never explain a source, and never state her question for her.
    No `annotation` fields.
11. **Labels:** names only (`'Rashi'`, `'Bereshit Rabbah'`). A commentary on a midrash is
    labeled "X, on the midrash". Use her own attribution for unusual names. Don't add eras or
    schools.
12. **No manuscript images** in Noach (Lev, 2026-10-12).

## Shape of a leaf

```python
def leaf_1953(prefix='gd-1953'):
    h = harvest('garden', '1953')
    P = lambda: primary('Genesis 2:18-24', ['2:18', ..., '2:24'], {...})
    return [
        {'id': prefix, 'title': {'en': '1953 · <content title>'}, 'primaryText': P(), 'steps': [...]},
        # optional continuation when the verse focus moves far (a new panel scrolls in):
        {'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '<content title>'},
         'primaryText': primary(...), 'steps': [...]},
    ]
```

- **Ids.** The first section's `id` is exactly `prefix` (it's the branch target); every step
  id starts with `prefix`.
- **Titles.** The leaf title is `'<year> · <content title>'`, e.g. `'1958 · Righteous in His Generations'`. Continuation titles are content titles.
- **primaryText.** Only the verses the leaf's cards point at, trimmed honestly; non-adjacent
  verses are joined with " … " and given a ref like `Genesis 2:18, 20, 24`. Prefer a
  continuation with a new panel to one giant panel.
- **Density.** Render the §7 sections, at least 3 cruxes with her commentators. Aim for
  20–35 steps.
- **Highlights.** Bind most cards to a phrase. Use `effect: 'glow'` sparingly; `question()`
  pulses by default.

## Check and record

- Run `python3 research/scripts/check_leaves.py noach <theme> [year]` until it reports **0 failing
  checks**.
- Write the paper trail to `research/parshiyot/noach-leaves/<theme>.md`, one section per
  leaf:
  - sections rendered;
  - each card's harvest `[i]` and slice (start/stop);
  - questions omitted and why;
  - NOT-IN-SCAN sources quoted (rule 6);
  - open triage items, how you settled them, and the evidence;
  - translation choices worth a second look.
- Touch nothing else: no `data/`, no tests, no lib (if the lib is missing something, say so
  in your report).

## Noach additions (2026-10-12)

- **Editor's box.** Items the scan check marks EDITOR (Perlman's «שאלות בטעמי המקרא») are not
  hers and are never quoted.
- **1970 is Nataf's bilingual edition.** For her questions and framing there, use Nataf's
  published English: `question(..., en=None, en_basis='nataf')` takes the item's `en_nataf`
  (whole item only). Sources she quotes still get our English (or Sefaria's, by rule 9).
- **Divine name** in the English: "the Lord" (the verse cache's convention); in her Hebrew the
  harvest's spelling (ה', אלוקים, א-לוהים) stands.
- **Comparison panels** (two passages side by side, `mode: comparison`) fit her "השווה" tables
  (e.g. God's blessing to Adam, 1:28, beside the blessing to Noah, 9:1–2). Keep each side to a few
  short lines; see `comparison_4_3()` in `bereshit_leaves/cain.py`.

## After the scan checks (2026-10-12): what every drafter must know

- **Mechanics.** Module `research/scripts/noach_leaves/<theme>.py` (themes: generation, flood,
  covenant, blood, babel), one `leaf_<year>(prefix=...)` per gilayon, prefixes `gn-`, `fl-`,
  `cv-`, `bl-`, `bb-` (e.g. `fl-1952`). `harvest('<theme>', '<year>')`. Check with
  `python3 research/scripts/check_leaves.py noach <theme> <year>`; 0 failing checks.
- **Scan-only items have string keys:** `'after 50'` (1945 §ה Q2), `'after 17'` (1951 §ב Q3),
  `'after 32'`, `'after 35'` (1944 §ב Q5, Q7), `'after 30'` (1960's last question),
  `'before 19'`, `'before 24'` (1958: the two Rashi passages she printed). Use them like any index:
  `question(id, h, 'after 50', ...)`.
- **Triage is done.** `triage.json` says, per item, whether the scan or the digitization stands.
  Source texts with known slips were fixed by `overrides.json` `replace`. If you find another
  slip inside a source you want to quote, don't type a fix: slice around it, or report it.
- **Pointers inside source items.** 1944 [27] and 1952 [32] carry her question/pointer typed in
  front of a Rashi; 1947 [14] carries her «החל מן "והטעם אלה תולדות"» start point. Cut the
  question out with `cut()` for a `question()` card; quote the source from its own start.
- **Underlining.** Questions that ask about «המסומן בקו» need the underline:
  `underline(cut(...), span)` with the span recorded in the scan-check file (1957 Ibn Ezra,
  Radak; 1960 Abarbanel §ד; 1968 Rekhasim §ג, Ibn Kaspi §ד; 1953-style). If the span isn't
  recorded, omit that question.
- **Her order.** 1962 §ד prints its midrash blocks 2), 3), 1); render the scan's order.
  1960's digitized §ג is her §ד (her sheet has no ג). 1970: her §ה (Rashi, Bekhor Shor and three
  questions on 9:5, items [21]–[28]) sits inside the digitized §ד; her §ו is digitized as ה.
  Section boundaries for titles and panels come from the scan-check file.
- **Duplicates in the digitization:** 1946 Abarbanel lead-in [23]/[24] and the Akeda label in
  [28] are printed twice; slice so each appears once.
- **Nataf (1970):** `question(..., en=None, en_basis='nataf')` for her own items only, whole item.
- **Her השווה tables** (1947 §א, 1957 §א, 1970 §א, 1948 §ב): a comparison panel, copying
  `comparison_4_3()` from `bereshit_leaves/cain.py`, with each side a few short lines.
- **Report:** at the end, give one BLURB line per leaf (the passage or question it explores, in
  the voice of `BLURBS` in `build_bereshit.py`).
