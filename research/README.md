# Research

Source-of-truth artifacts for Close Read sheets, especially Mode 4 (Nechama parsha).

## Layout

- `parshiyot/<parsha>.md` — Per-parsha research pack: full Nechama corpus inventory,
  proposed structure, and per-leaf source notes. The pack is the audit trail; every
  claim about Nechama in `data/<parsha>.json` should trace back here.
- `parshiyot/<parsha>-harvest/` — Structured per-leaf data extracted from Sefaria sheets.
  One JSON file per chosen gilayon, with her section headers + chosen sources + her
  questions, ready to feed into the JSON builder.
- `scripts/` — Reusable builder/harvester scripts. The Nasso build uses these and they
  are templates for the next parsha:
  - `pull_headers.py` — fetch all sheets in a parsha and extract their section labels
    (good for the Stage-1 inventory)
  - `harvest.py` — for chosen gilyonot, produce structured per-leaf JSON
  - `clean_verses.py` — strip cantillation + maqaf from Sefaria text into Close-Read form
  - `build_nasso.py` — assembles `data/nasso.json` from harvest + verses + handcrafted narration
  - `verses.json` — cached cleaned verse texts for Nasso (regenerate per parsha)

## Adding a new parsha

See `.claude/skills/close-read-sheet/references/pedagogical-arcs.md` Mode 4 for the full
workflow. In short:

1. Copy `pull_headers.py`, change the parsha slug, run → produces inventory
2. Write `parshiyot/<parsha>.md` with the inventory + proposed structure
3. **Stop and get user sign-off on structure.**
4. Copy `harvest.py`, change the chosen-sheet IDs, run → produces harvest files
5. Pull verse texts via Sefaria MCP `get_text`, clean with `clean_verses.py` pattern
6. Copy `build_nasso.py`, swap content per leaf, run → produces `data/<parsha>.json`
7. Validate (word-group script in `.claude/skills/close-read-sheet/references/hard-rules.md`)
   and browser-verify

Total: ~6 hours per parsha at this depth.
