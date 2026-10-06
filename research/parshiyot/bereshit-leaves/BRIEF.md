# Brief: drafting Bereshit leaves (Stage 4)

You're turning Nechama Leibowitz's study sheets (gilyonot) into Close Read leaves: scrolling
cards on the left, a pinned verse (or image) on the right whose phrases light up as each card
is read. **We're taking her thinking from one form into another.** The reader experiences the
content (her chosen sources, her questions, the verse), not narration about her sheet.

The worked example is `leaf_1963` in `research/scripts/bereshit_leaves/creation.py`. Read
it first, and copy its shape and voice.

## Inputs (all checked; don't go around them)

- **Harvest:** `research/parshiyot/bereshit-harvest/<theme>/<year>.json`. Every item has
  `i`, `kind`, `he`, often `ref`/`en`, `basis`, and scan-check fields. This is the **only**
  source of her Hebrew and of source texts.
- **Scan check:** `research/parshiyot/bereshit-scancheck/<sheet>-<year>.md`. For each source
  it gives her start/stop points (`EXPANDED (start: …; stop: …)`, `החל מן … עד …`) and her
  scan headers.
- **Triage:** `bereshit-scancheck/triage.json`. Items with `use: open` must be settled from
  the cited text before you quote them (see your assignment); if you can't settle one, don't
  quote it.
- **Design:** `research/parshiyot/bereshit.md` §7 (which sections to render) and §2 (fidelity).
- **Library:** `research/scripts/bereshit_lib.py`: `harvest`, `item`, `cut`, `underline`,
  `narration`, `commentary`, `question`, `primary`, `verse_set`, `words`, `vp`, `FOLIO_*`.
- **Verses:** `research/parshiyot/bereshit-verses.json`, read by `primary()`. MAM Hebrew
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
12. **No Leningrad images** except where your assignment says so.

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
- **Titles.** The leaf title is `'<year> · <content title>'`, e.g. `'1953 · A Helper Against
  Him'`. Continuation titles are content titles.
- **primaryText.** Only the verses the leaf's cards point at, trimmed honestly; non-adjacent
  verses are joined with " … " and given a ref like `Genesis 2:18, 20, 24`. Prefer a
  continuation with a new panel to one giant panel.
- **Density.** Render the §7 sections, at least 3 cruxes with her commentators. Aim for
  20–35 steps.
- **Highlights.** Bind most cards to a phrase. Use `effect: 'glow'` sparingly; `question()`
  pulses by default.

## Check and record

- Run `python3 research/scripts/check_leaves.py <theme> [year]` until it reports **0 failing
  checks**.
- Write the paper trail to `research/parshiyot/bereshit-leaves/<theme>.md`, one section per
  leaf:
  - sections rendered;
  - each card's harvest `[i]` and slice (start/stop);
  - questions omitted and why;
  - NOT-IN-SCAN sources quoted (rule 6);
  - open triage items, how you settled them, and the evidence;
  - translation choices worth a second look.
- Touch nothing else: no `data/`, no tests, no lib (if the lib is missing something, say so
  in your report).
