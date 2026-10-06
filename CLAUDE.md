# Close Read

A data-driven scrollytelling engine for Torah study in the style of NYT's "Close Read" format. Primary verses stay pinned on screen while commentary cards scroll past, triggering word-level highlights, verse transitions, and side-by-side comparisons.

Built for Nechama Leibowitz's study sheets.

Per-module detail (engine, text effects, CSS, data contract, Nechama workflow, gotchas) lives in the Sefaria wiki at `sefaria-wiki/wiki/repos/close-read/` — start at `_index.md`. Update those pages when you change a module; they replaced the old `agent_docs/` tree.

## Key Documentation

- **[Data Format](docs/data-format.md)** — Full schema for JSON data files. Covers title metadata, sections, verse data (single and comparison modes), word groups for highlighting, and all four step types (narration, commentary, question, verse-change).
- **[Architecture](docs/architecture.md)** — How the JS engine works: initialization flow, ScrollTrigger setup, word highlighting pipeline, verse crossfade mechanism, CSS architecture, and known constraints.
- **[Conversion Guide](docs/conversion-guide.md)** — Step-by-step checklist for turning a Sefaria source sheet into a JSON data file. Covers naming conventions, text sourcing, structure mapping, and testing.

## Running Locally

Requires a web server (fetch won't work from file://):

```bash
cd close_read
python3 -m http.server 8080
# Open http://localhost:8080
```

The default page (`/`) shows an index of available sheets. Load a specific sheet: `http://localhost:8080/?sheet=other-sheet-name`

When adding a new sheet, also add an entry to `data/index.json`.

## Tests

```bash
pip install -r requirements-dev.txt && python3 -m playwright install chromium
python3 -m pytest                      # everything (~1 min)
python3 -m pytest tests/test_data.py   # JSON checks only, no browser (<1 s)
python3 -m pytest -k "nasso and mobile"
```

- `tests/test_data.py` checks the JSON alone. It replays the engine's word wrap, so overlapping or nested word groups, unresolvable highlights, broken branch targets and unreachable sections are caught without a browser.
- `tests/test_render.py` serves the site and opens every leaf path of every sheet in `data/index.json` at desktop (1440×900) and mobile (390×844). It scrolls each card into reading position and checks:
  - the active card is the only active one;
  - the panel shows the right verse, the right words are lit with the rest dimmed, and nothing leaks into other sections;
  - highlighted words are on screen, uncovered and not clipped;
  - the verse fits the screen and the ref label sits clear of the breadcrumb;
  - the card is readable and not covered by the sticky panel;
  - fixed nav doesn't overlap text, and there are no `undefined`s or console errors.
  It also clicks through the branches and walks back with history.
- `tests/sheetmodel.py` mirrors the engine's grouping, branching and active-verse rules. Change it when you change `groupSections`, `pathToVisibleSet` or `activateStep`.
- New sheets are picked up from `data/index.json` automatically. CI runs both layers on every PR (`.github/workflows/test.yml`).

## Stack

Static HTML/CSS/JS. No build step. GSAP + ScrollTrigger from CDN. Google Fonts (Frank Ruhl Libre, Crimson Text, Inter).

## Design Decisions

- **Left/right layout**: Commentary cards scroll on the left (40%), primary text is sticky on the right (60%). Mobile stacks vertically.
- **Light theme**: Warm cream background (#faf8f4), brown accent (#8b5e3c). Dark mode was tried and rejected — hard to read with bilingual text.
- **Verse breathing**: Intro steps (no `highlight` array) show the verse at full opacity before any dimming begins. This is deliberate — don't add highlights to intro steps.
- **Dimming approach**: Uses `color` change (to --color-text-muted) rather than `opacity` reduction. Prevents double-dimming when both word-group and container styles apply.
- **Mobile panel**: the sticky verse panel is a fixed 45vh so cards stay readable below it, and `fitToPanel` shrinks long passages into it. A passage that won't fit even at the minimum sizes (14px Hebrew / 12px English) shows Hebrew only; currently that's Nasso's Nazir passage and Yitro's comparison. On phones the breadcrumb shortens earlier crumbs and keeps the current one whole.
- **Font sizes**: Base 18px, Hebrew primary text clamp(1.5rem, 2.8vw, 2.2rem). Erring on the larger side for readability.

## Working With the Data

To create a new sheet:

1. Create `data/your-sheet.json` following the schema in [data-format.md](docs/data-format.md)
2. Visit `?sheet=your-sheet`
3. The engine builds everything from the JSON — no HTML or JS changes needed

Key things to get right:
- Hebrew text in `words` entries must exactly match the verse text (including nikkud)
- First step in each section should be a `narration` with no `highlight` — lets the verse breathe
- `verse-change` steps must appear before any steps that reference the new verse's word groups
- Word group IDs in `highlight` arrays must match keys in the active verse's `words` map

## Extending

- **New source colors**: Unknown sources get a neutral warm-brown fallback. For a custom color, add `.source-label[data-source="Name"] { ... }` to CSS
- **New step types**: Add a case in `buildStepCard()` in engine.js and matching CSS
- **New highlight effects**: Add a case in the `highlight()` method in text-effects.js and matching CSS class
- **Images in the panel**: use `"mode": "image"` VerseData with fractional `regions` (see [Data Format](docs/data-format.md#image)); steps highlight region ids like word groups
