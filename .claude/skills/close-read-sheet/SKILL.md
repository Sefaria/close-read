---
name: close-read-sheet
description: Create a guided-learning Close Read scrollytelling sheet (data/*.json) from a base text reference (e.g. "Pirkei Avot 2:5"), a Sefaria source sheet (URL or numeric ID), or a Sefaria topic. Use whenever the user asks to "build a Close Read on …", "make a guided learning of …", "turn this sheet into a scrolly", "create a close-read for [Mishnah/parsha/sugya/topic]", or similar. Produces a fully populated data/<slug>.json plus an index.json entry, verified in the browser.
---

# Close Read sheet generator

This skill turns a piece of Torah/Mishnah/Talmud — or a Sefaria source sheet or topic — into a scrollytelling **Close Read** sheet (`data/<slug>.json`) that runs on the engine in this repo.

## When to invoke

The user gives one of four inputs:

1. **A base text reference** — e.g. `Pirkei Avot 2:5`, `Genesis 22:1-19`, `Berakhot 7a:14`, `Mishnah Berakhot 1:1`.
2. **A Sefaria source sheet** — a URL like `https://www.sefaria.org/sheets/160545` or a bare numeric ID.
3. **A Sefaria topic** — e.g. `Akedah`, `Prayer`, `Tochacha`.
4. **A parsha name with "Nechama" framing** — e.g. "Nechama on Beha'alotcha", "Nechama Leibowitz for Shelach", "build the Nasso experience". This is the multi-decade-rendering Mode 4 — see `references/pedagogical-arcs.md`.

Output: a complete `data/<slug>.json` and an entry appended to `data/index.json`. Verify in the browser before reporting done.

For Mode 4 (Nechama parsha), there is also a research pack at
`research/parshiyot/<parsha>.md` — produce it as the Stage-1/2 deliverable and **stop for
user confirmation before harvesting** all selected gilyonot.

## Required reading before you start

Open these in this order. They're short:

- [docs/data-format.md](../../../docs/data-format.md) — full schema for the JSON
- [docs/conversion-guide.md](../../../docs/conversion-guide.md) — practical conversion recipe
- [docs/architecture.md](../../../docs/architecture.md) — how the engine renders the JSON, including comparison mode and verse-change semantics
- [references/pedagogical-arcs.md](references/pedagogical-arcs.md) — how to design the 4–5 section arc for each input mode
- [references/hard-rules.md](references/hard-rules.md) — non-negotiable rules: Hebrew cleaning, word-group constraints, source-color mapping, when to use comparison vs inline quote

Canonical examples to imitate (read at least one before drafting):

- [data/pirkei-avot-1-11.json](../../../data/pirkei-avot-1-11.json) — five sub-sections sharing a single pinned Mishnah; commentators old-to-new; Hasidic + modern closing
- [data/yitro-5730.json](../../../data/yitro-5730.json) — three sections including one comparison-mode pair of biblical verses
- [data/shemini-5731.json](../../../data/shemini-5731.json) — two sections drilling into one verse from multiple angles

## Workflow

### Phase 1 — Fetch source material

Use the Sefaria MCP tools (`get_text`, `get_links_between_texts`, `get_topic_details`, `get_english_translations`, `text_search`). For source sheets the MCP may not have a direct tool — fall back to `WebFetch` against `https://www.sefaria.org/api/sheets/<id>`.

What to grab depends on the input mode:

- **Base text ref:** the text in both languages; `get_links_between_texts` to discover available commentary; then fetch each commentary you plan to use.
- **Source sheet:** the sheet JSON (sources, author commentary, structure). The sheet's *order* and *highlighting* are usable directly — the author has already done the pedagogical sequencing.
- **Topic:** `get_topic_details` for the anchor texts; then fetch each anchor text and the most-cited commentaries for it.

### Phase 2 — Design the arc, then **stop and confirm with the user**

Before writing 30+ steps of content, present:

- Title, subtitle (English; Hebrew if the corpus supports it)
- Section titles in order (typically 3–5)
- Per section: primary text, the 2–3 commentators or sources you'll use, and the question that closes the section
- Total step estimate

Use `AskUserQuestion` if there's a meaningful design decision (which commentators to feature, whether to include a Hasidic/modern voice, how dense the sheet should be, whether to address the original Hebrew or stay English-only).

See [references/pedagogical-arcs.md](references/pedagogical-arcs.md) for the arc templates for each input mode.

### Phase 3 — Write the JSON

Build the file in one pass using a template based on the closest canonical example. Hold to these invariants:

- **Hebrew text must be cantillation-stripped, nikkud-preserved.** Python recipe in [references/hard-rules.md](references/hard-rules.md). Texts from `Torat Emet 357` (Mishnah/Avot) already lack cantillation; Tanakh versions from `Miqra according to the Masorah` need stripping.
- **Word groups within one verse cannot overlap.** Section A might split a Mishnah into 8 phrase-keys; sub-sections that re-use the same `primaryText` MUST use compatible (non-overlapping) word maps. The engine wraps once and reuses across the group.
- **Consecutive sections that share `primaryText.ref` + `he` collapse into one sticky panel.** The user reads the same text continuously while the sidebar advances through sub-sections. This is the preferred shape for a deep dive on a single base text.
- **Short prooftexts (e.g. a single biblical verse quoted by a commentary) stay inline within the commentary card or its annotation.** Do not use `verse-change` to take over the main panel for them.
- **`verse-change` is for substantive parallel/contrast texts** the user will study at length. Use sparingly. Always return to the base text before the next section ends.
- **Comparison mode is for short verse pairs only** (biblical pasuk vs pasuk). Do not use it for full mishnayot or long passages — it cramps the laptop layout. For parallel mishnayot, embed the second one as a commentary card.
- **Closing section, when the corpus allows it,** carries the idea forward through one Hasidic voice (Likutei Moharan, Toldot Yaakov Yosef, Ba'al Shem Tov) and one modern voice (Rav Uziel's Hegyonei Uziel, Rav Kook, Nechama Leibowitz, etc.). Two cards plus framing narration.
- **Source-label colors:** existing CSS tokens are `Rashi`, `Ramban`, `Ibn Ezra`, `Bereshit Rabbah` / `Aggadat Bereishit` / `Tanchuma` (midrash purple), `Mekhilta`, `Talmud`. Other sources fall back to neutral warm-brown. Don't add CSS tokens in this skill — keep it data-only.
- **Narration voice:** didactic guide. The narrator names the puzzles; the commentaries do the work. Don't moralize. Don't summarize commentaries before quoting them.
- **English-only is fine for narration/annotation.** If the corpus has a strong Hebrew tradition (Mishnah, Tanakh, Talmud) keep the primary text and direct commentary quotations bilingual; the rest can be English-only. The engine's title/section/subtitle/source-label/annotation/narration fields all gracefully omit the `.he` field if absent.

### Phase 4 — Register and verify

1. Append a new entry to `data/index.json` with `{slug, title, author, description}`. Author is the original Sefaria author/anthologist when there is one (e.g. for a sheet); otherwise the text's tradition (e.g. `"Avtalyon"` for Avot 1:11) or omit if unclear.
2. Validate the JSON parses: `python3 -c "import json; json.load(open('data/<slug>.json'))"`.
3. Validate every word-group Hebrew phrase actually occurs in its verse text — script in [references/hard-rules.md](references/hard-rules.md).
4. Start the preview server (via `preview_start` against the launch config) and load `?sheet=<slug>`. Use `preview_eval` to confirm:
   - The sheet renders (no `undefined` in DOM)
   - All sections appear (check `.cr-section` count and `.section-dot` count)
   - Primary panel stays pinned across same-text sub-sections (sample `panelVisible` at several scroll positions)
   - Highlights fire on a card with a `highlight` array (check `.word-group.highlighted`)
   - No errors in console (`preview_console_logs` filtered to `error`)

### Phase 5 — Report

Tell the user the slug, the section structure, and the URL `?sheet=<slug>`. Note any commentaries you considered but dropped, and why.

## Things to skip

- Adding new CSS color tokens. Use the fallback for un-tokenized sources. Mention it as a follow-up if a sheet leans heavily on a single un-tokenized commentator.
- Modifying the engine. The data format is expressive; if you find yourself wanting a new step type, the answer is almost always to use existing types differently.
- Long Hebrew narration cards. The engine renders them but reading bilingual narration alongside primary text overloads the eye. Hebrew belongs in the primary panel and in direct commentary quotations.
- Adding Hebrew titles when none are natural. Section titles can be English-only (`{ "en": "..." }`).
