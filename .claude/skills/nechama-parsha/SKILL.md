---
name: nechama-parsha
description: Build a weekly Parsha flow — a branching Close Read scrollytelling sheet grown from Nechama Leibowitz's actual gilyonot on Sefaria. Use whenever the user asks to "build the Nechama flow for [parsha]", "do this week's parsha", "Nechama on [parsha]", "make the [parsha] garden", "build the weekly parsha", or similar. Produces a research pack (audit trail) and a data/<parsha>.json that runs on the forking-paths engine. This is the repeatable weekly cycle; the worked example is data/bereshit.json (built with the scan-checked, quote-don't-type pipeline).
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

The canonical worked example is **Bereshit**: `data/bereshit.json`, the pack
`research/parshiyot/bereshit.md`, the scan checks in `bereshit-scancheck/`, and the leaf
trails in `bereshit-leaves/`. Read the pack's §2 (how Sefaria's digitization departs from her
scans) and `bereshit-leaves/BRIEF.md` (the drafting rules) before building a new parsha.
**Don't copy Nasso.** It predates this pipeline, and some of its question cards are English
paraphrases rather than her questions, which is exactly the fabrication this pipeline exists
to prevent.

## The source

Nechama's sheets are on Sefaria as user **54380** (the Gilyonot Nechama collection).

- All her sheets: `https://www.sefaria.org/api/sheets/user/54380/`. **Keep the trailing
  slash.** Without it the server answers with a 301 redirect and an empty body, and any
  client that doesn't follow redirects sees nothing.
- **Send `User-Agent: Sefaria/close-read`**, the in-house `Sefaria/<service>` convention, so
  our traffic is counted as first-party. Never send a bare `Mozilla/5.0`: Cloudflare
  challenges it with a 403 "Just a moment" HTML page. For example:
  `curl -sL -A "Sefaria/close-read" https://www.sefaria.org/api/sheets/user/54380/ -o /tmp/nechama/all-sheets.json`
  (the scripts in `research/scripts/` already set it).
- Filter to one parsha client-side on `topics[].slug == "parashat-<name>"`.
- One sheet's full body: `https://www.sefaria.org/api/sheets/<id>` — returns an ordered
  `sources[]`, each item either an `outsideText` (her prose / section-header / question)
  or a `ref` + `text` (a source she chose: verse, Rashi, midrash, Rambam, …).

Her sheets are internally organized as **Hebrew-letter sections** (`א.`, `ב.`, `ג.` …),
each a crux with the sources she chose, her framing prose, and her numbered questions.
That internal structure is the raw material for a leaf.

## Workflow (five stages)

The rule underneath every stage is that **her Hebrew is never typed**. It's sliced from text
that has been checked against her original scans, and a test proves it.

### Stage 1 — Snapshot and survey

- `research/scripts/snapshot_parsha.py <parsha> <topic-slug>` freezes every sheet into
  `parshiyot/<parsha>-raw/`, with sha256s. Verify the snapshot against the live API and
  record that in `verification.json`.
- `survey_parsha.py <parsha> <Book> <span>` writes `<parsha>-survey.{json,md}`: every item
  with its `[i]`, a summary table, verse coverage, and a year check.
- Write the pack (`parshiyot/<parsha>.md`): provenance, inventory, tentative clusters, and
  absences. Absences are only *candidates* until the scans confirm them.

### Stage 2 — Design, then STOP and confirm

Pick 4–6 themes and 3 gilyonot per theme, with temporal spread and interpretive contrast,
and list the sections each leaf renders. **Present the outline and wait for the user.**
Leningrad images (`mode: image`) only where the page layout is itself the evidence, once
or twice per parsha.

### Stage 3 — Scan check, triage, harvest

- **Scan check.** For every chosen section, check the digitization against her scan
  (`https://www.nechama.org.il/pdf/<n>.pdf`, every page; most are two). Method, format and
  calibration are in `bereshit-scancheck/README.md`. It's verification, not
  transcription. Spot-check one finding per checker yourself.
- **Transcribe** any sheet whose digitization lost her questions, and have a person verify
  the part you'll use.
- **Triage.** Settle every word-level difference with evidence in `triage.json`. The cited
  source usually decides it: a reference she gives, or the commentator's own text.
  Citation detail the digitizers *added* is editorial, not an error (Lev).
- **Harvest.** `harvest_<parsha>.py` (copy `harvest_bereshit.py`), plus `overrides.json` for
  items the digitization lost. `REVIEW.md` must be empty before drafting.
- **Verses.** `fetch_verses.py` caches MAM Hebrew and JPS English, with footnotes and
  variant notes stripped.

### Stage 4 — Draft

- Leaves go in `research/scripts/<parsha>_leaves/<theme>.py`, with helpers in
  `bereshit_lib.py`. Cards quote harvest items by `cite`, slices are verbatim, and verse
  word groups are found by their bare letters.
- Follow `bereshit-leaves/BRIEF.md` and
  [references/voice-and-fidelity.md](references/voice-and-fidelity.md). **The reader
  experiences the content, not her sheet**: no narration about how her sheet is built.
- Check one theme in isolation with `check_leaves.py <theme>`. Each theme's paper trail goes
  in `<parsha>-leaves/<theme>.md`.
- Assemble with `build_<parsha>.py`.

### Stage 5 — Validate & ship

- Run `python3 -m pytest`. It includes `test_provenance.py`, and the render suite walks
  every path at desktop and phone sizes.
- Take Playwright screenshots of the hard cards: images, comparisons, LTR quotes.
- Bump the asset `?v=` strings, then open the PR. See
  [references/quality-and-errors.md](references/quality-and-errors.md).

## Cadence

The scan check and triage are the expensive, essential part. Bereshit's 15 leaves took
five parallel checkers and five parallel drafters. The scripts are templates: a new parsha
needs its slug, chosen sheets and sections, theme intros, and its leaves.
