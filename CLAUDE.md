# Close Read

A data-driven scrollytelling engine for Torah study in the style of NYT's "Close Read" format. Primary verses stay pinned on screen while commentary cards scroll past, triggering word-level highlights, verse transitions, and side-by-side comparisons.

Built for Nechama Leibowitz's study sheets, starting with Parashat Noah 5712.

## Project Structure

```
close_read/
├── index.html              # Empty shell — all content built from JSON
├── css/close-read.css      # Layout, typography, animations, theme
├── js/
│   ├── engine.js           # CloseReadApp class: data loading, DOM building, scroll orchestration
│   └── text-effects.js     # TextEffects: word wrapping, highlighting, verse crossfade
├── data/
│   ├── index.json           # Sheet manifest (drives the index page)
│   └── *.json               # Sheet data files (one per sheet)
└── docs/
    ├── data-format.md      # JSON schema: how to author a data file
    └── architecture.md     # Technical details: layout, scroll triggers, word matching
```

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

## Stack

Static HTML/CSS/JS. No build step. GSAP + ScrollTrigger from CDN. Google Fonts (Frank Ruhl Libre, Crimson Text, Inter).

## Design Decisions

- **Left/right layout**: Commentary cards scroll on the left (40%), primary text is sticky on the right (60%). Mobile stacks vertically.
- **Light theme**: Warm cream background (#faf8f4), brown accent (#8b5e3c). Dark mode was tried and rejected — hard to read with bilingual text.
- **Verse breathing**: Intro steps (no `highlight` array) show the verse at full opacity before any dimming begins. This is deliberate — don't add highlights to intro steps.
- **Dimming approach**: Uses `color` change (to --color-text-muted) rather than `opacity` reduction. Prevents double-dimming when both word-group and container styles apply.
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
