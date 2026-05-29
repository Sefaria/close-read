---
name: nechama-parsha
description: Build a weekly Parsha flow — a branching Close Read scrollytelling sheet grown from Nechama Leibowitz's actual gilyonot on Sefaria. Use whenever the user asks to "build the Nechama flow for [parsha]", "do this week's parsha", "Nechama on [parsha]", "make the [parsha] garden", "build the weekly parsha", or similar. Produces a research pack (audit trail) and a data/<parsha>.json that runs on the forking-paths engine. This is the repeatable weekly cycle; the worked example is data/nasso.json.
---

# nechama-parsha: build a weekly Parsha flow

This skill turns **Nechama Leibowitz's gilyonot for one parsha** into a branching
Close Read — a "garden of forking paths" where the reader chooses a theme, then
chooses one of her angles across the decades, then walks that actual sheet with the
verse pinned and her commentators lighting up phrases as her question unfolds.

The structure grows out of **her** oeuvre: she returned to each parsha many times
over thirty years, clustering around a handful of passages. Those clusters become the
themes; her individual dated sheets become the leaves.

## The one-sentence philosophy

> Render *her* work faithfully and densely. The narrator names the puzzle and the
> voice about to speak, then gets out of the way. Everything interpretive comes from
> the sources Nechama herself chose.

If you remember nothing else: **the default failure mode is a sheet that's too thin —
one commentary per leaf, narrator paraphrase doing the work.** Lean the other way.
See [references/voice-and-fidelity.md](references/voice-and-fidelity.md).

## What it produces

Two artifacts per parsha, and the JSON cites the pack:

1. `research/parshiyot/<parsha>.md` — the **research pack**: full inventory of her
   sheets, the design (themes + chosen gilyonot + chosen cruxes), per-leaf source
   notes. This is the audit trail. Every claim about Nechama in the JSON traces here.
2. `data/<parsha>.json` — the **Close Read** that runs on the engine, plus an entry in
   `data/index.json`.

## Required reading before you start

- [references/voice-and-fidelity.md](references/voice-and-fidelity.md) — **the heart of
  this skill.** Voice, source density, and faithfulness to her material.
- [references/quality-and-errors.md](references/quality-and-errors.md) — thoroughness
  and error checking: validation script, browser verification, the engine gotchas.
- [../close-read-sheet/references/hard-rules.md](../close-read-sheet/references/hard-rules.md)
  — the engine mechanics (Hebrew cleaning, word-group constraints, source colors). Don't
  re-derive these; they're shared with the general close-read-sheet skill.

The canonical worked example is `data/nasso.json` + `research/parshiyot/nasso.md`. Read
the Nasso pack before building a new parsha — it shows the target shape.

## The source

Nechama's sheets are on Sefaria as user **54380** (the Gilyonot Nechama collection).

- All her sheets: `https://www.sefaria.org/api/sheets/user/54380` (send a `User-Agent`
  header or the request returns empty).
- Filter to one parsha client-side on `topics[].slug == "parashat-<name>"`.
- One sheet's full body: `https://www.sefaria.org/api/sheets/<id>` — returns an ordered
  `sources[]`, each item either an `outsideText` (her prose / section-header / question)
  or a `ref` + `text` (a source she chose: verse, Rashi, midrash, Rambam, …).

Her sheets are internally organized as **Hebrew-letter sections** (`א.`, `ב.`, `ג.` …),
each a crux with the sources she chose, her framing prose, and her numbered questions.
That internal structure is the raw material for a leaf.

## Workflow (five stages)

### Stage 1 — Inventory (~30 min)

Fetch every sheet for the parsha. For each: year (Hebrew + Gregorian), sheet ID,
sub-topic, and her internal section labels (`pull_headers.py` in `research/scripts/`
does this). Cluster by theme. Note conspicuous **absences** — topics in the parsha she
*didn't* write on are themselves a finding worth a card. File all of it into
`research/parshiyot/<parsha>.md`.

### Stage 2 — Design, then STOP and confirm (~20 min)

Pick **4–6 themes** for Level 0 and **2–4 of her gilyonot per theme** for Level 1.
Selection criteria: temporal spread (early / mid / late, so the reader feels her
returning across decades) + interpretive contrast (don't pick two sheets that ask the
same question). At least one sheet per theme should be multi-crux dense.

**Present the outline and wait for the user before harvesting.** This is the cheap
checkpoint — re-scoping after 5 hours of drafting is not.

### Stage 3 — Source harvest (~2 hr)

For each chosen sheet, parse `/api/sheets/<id>` into structured per-leaf data
(`harvest.py`): section labels, the sources she chose, her questions. Save under
`research/parshiyot/<parsha>-harvest/<theme>/<year>.json`. Pull verse texts for each
theme's `primaryText` via Sefaria MCP `get_text` against `Miqra according to the
Masorah`, clean with `clean_verses.py` (cantillation strip + maqaf→space).

### Stage 4 — Draft the JSON (~3 hr)

Build `data/<parsha>.json` as: overview → root-fork → per-theme (intro → theme-fork →
leaves). Each leaf renders one gilayon. Use the `build_<parsha>.py` script pattern
(copy `build_nasso.py`) so the file is reproducible and easy to iterate. The *how* —
card sequence, narration voice, how many cruxes — is all in
[references/voice-and-fidelity.md](references/voice-and-fidelity.md).

### Stage 5 — Validate & ship (~30 min)

Run the extended validation script, browser-verify every leaf, then commit. The full
checklist (and the bugs that taught us each item) is in
[references/quality-and-errors.md](references/quality-and-errors.md). Do not skip it —
this is where silent failures (un-highlighted phrases, overflowing panels, wrong-panel
dimming) get caught.

## Cadence

One parsha per week, ~6 hours of focused work at this depth. The `research/scripts/`
are templates: a new parsha needs its slug, its chosen sheet IDs, and handcrafted
narration swapped in. Same endpoints, same cleaning, same JSON shape.
