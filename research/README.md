# Research

Source-of-truth artifacts for Close Read sheets, especially Mode 4 (Nechama parsha).

## Layout

- `parshiyot/<parsha>.md` — Per-parsha research pack: full Nechama corpus inventory,
  proposed structure, and per-leaf source notes. The pack is the audit trail; every
  claim about Nechama in `data/<parsha>.json` should trace back here.
- `parshiyot/<parsha>-raw/` — Frozen snapshot of every gilayon for the parsha (the bottom
  of the paper trail), with `manifest.json` and `verification.json`.
- `parshiyot/<parsha>-survey.{json,md}` — Generated survey. Don't hand-edit; re-run the script.
- `parshiyot/<parsha>-harvest/` — Structured per-leaf data extracted from Sefaria sheets.
  One JSON file per chosen gilayon, with her section headers + chosen sources + her
  questions, ready to feed into the JSON builder.
- `scripts/` — Reusable builder/harvester scripts. The Nasso build uses these and they
  are templates for the next parsha:
  - `snapshot_parsha.py` — Stage 1a: freeze every gilayon for a parsha into
    `parshiyot/<parsha>-raw/` (one JSON per sheet + `manifest.json` with sha256s). Reads
    the local prod-restore Mongo (the API with `User-Agent: Sefaria/close-read` works too).
    Verify against live and record it in `<parsha>-raw/verification.json` (see
    `bereshit-raw/` for the method).
  - `survey_parsha.py` — Stage 1b: mechanical survey of the raw snapshot. Every header,
    ref, question and prose item is listed with its `sources[]` index, plus a summary
    table, verse coverage and a Hebrew/Gregorian year check →
    `parshiyot/<parsha>-survey.{json,md}`. Supersedes `pull_headers.py`, which kept its
    data in `/tmp` and lost the paper trail.
  - `fetch_verses.py` — Stage 3: cache a parsha's verses (MAM Hebrew with Masoretic breaks +
    Sefaria's default English, footnotes stripped, divine name normalized) →
    `parshiyot/<parsha>-verses.json`.
  - `harvest_bereshit.py` — Stage 3: per-leaf data from the raw snapshot + scan checks +
    `overrides.json` + `triage.json` (+ a verified transcription where the digitization lost her
    questions) → `parshiyot/bereshit-harvest/`, plus the generated `bereshit-scancheck/REVIEW.md`.
  - `build_bereshit.py` — Stage 4: the sheet JSON. Her Hebrew is sliced from the harvest, never
    typed; every quoted card carries `cite`/`en_basis`, checked by `tests/test_provenance.py`.
  - `pull_headers.py` — (Nasso-era) fetch all sheets in a parsha and extract their section labels
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
