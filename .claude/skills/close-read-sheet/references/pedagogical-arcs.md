# Pedagogical arcs

Three input modes, three different arc shapes. All three converge on the same JSON output format, but the *design move* differs.

## Mode 1 — Base text reference

Use when the user gives a single text reference (e.g. `Pirkei Avot 2:5`, `Genesis 22:1-19`).

Default arc — **5 sections, ~30–40 steps, all sub-sections sharing one pinned primary text:**

### Section A — A First Reading

Phrase-by-phrase plain reading.

- Primary panel: the base text (single mode)
- Word groups: one per natural clause (5–8 groups)
- Step pattern:
  - 1 narration: who said this / where it sits in its corpus (no highlight)
  - N narration cards, one per clause, each highlighting the corresponding word group with a careful, **deliberately under-resolved** English rendering
  - 1 transition narration (no highlight) naming the 2–3 puzzles the words create
  - 1 `question` card listing those puzzles

### Sections B, C, D — One crux per section

Each interpretive puzzle becomes its own section. Walk through commentators **oldest to newest** within each section. The primary panel stays pinned — same `primaryText.ref` and `he` as Section A; the engine collapses them.

- Section title in the sidebar names the puzzle
- 1 intro narration (no highlight)
- 3–5 commentary cards in chronological order. Typical genres:
  - **Tannaitic/midrashic layer** (Avot DeRabbi Natan, Mekhilta, Sifrei, Bereshit Rabbah, Tosefta)
  - **Talmudic** (Bavli or Yerushalmi sugya)
  - **Geonim / Early Rishonim** (Rashi, Rashbam, Ibn Ezra)
  - **Later Rishonim** (Rambam, Ramban, Rabbeinu Yonah, Bartenura on Mishnah)
  - **Early Acharonim** (Tosafot Yom Tov, Maharal, Shem Olam, Abarbanel)
- Each commentary card gets an `annotation` framing what shifts in this voice
- Optional short prooftexts (a biblical verse, a parallel mishnah) live **inline** within the commentary's text or annotation, NOT as `verse-change`
- 1 closing `question` card per section

### Section E — The Idea Carried Forward

Two voices: one Hasidic, one modern. Bridges from ancient to present-day.

- 1 intro narration (no highlight)
- 1 Hasidic commentary card — Likutei Moharan, Toldot Yaakov Yosef, Ba'al Shem Tov, Sefat Emet, etc.
- 1 modern commentary card — Rav Uziel (Hegyonei Uziel), Rav Kook, Heschel, Nechama Leibowitz, etc.
- 1 synthesis narration: name what changes in each direction (inward vs outward, mystical vs practical, etc.)
- 1 closing `question` aimed at the present-day reader

Canonical example of this mode: `data/pirkei-avot-1-11.json`.

## Mode 2 — Sefaria source sheet

Use when the user gives a sheet URL or numeric ID.

The sheet's *own* structure becomes the arc backbone. The author has already done the pedagogical sequencing — your job is to render their move through the close_read format.

- Fetch the sheet JSON (`/api/sheets/<id>`). It contains an ordered list of sources, each with `type` (`source` / `comment` / `outsideText` / `outsideBiText`) and `text` content.
- Group consecutive sources into sections by topical break (often signaled by the author's own `comment` blocks or by `outsideText` headers).
- The sheet usually has 1–3 base verses being explored. Each base verse anchors a section's `primaryText`.
- The author's `comment` blocks become `narration` cards.
- The author's questions (often `outsideText` or formatted with `?`) become `question` cards.
- Each cited source becomes a `commentary` card using its `ref` and the appropriate `sourceLabel`.

Canonical examples of this mode: `data/yitro-5730.json`, `data/shemini-5731.json`, `data/kedoshim-5731.json`.

When the sheet is from a known *author tradition* (Nechama Leibowitz, Klitsner, Hirschfield), match the existing per-sheet voice. Nechama sheets are *question-forward*; Klitsner is *literary-analytical*; Hirschfield is *halakhic-overview*.

## Mode 3 — Sefaria topic

Use when the user gives a topic slug or name.

- Use `get_topic_details` to retrieve the anchor texts and the topic description.
- Identify 1–3 *anchor texts* (the most-cited or most-central). These become the `primaryText` of one or more sections.
- Identify thematic angles within the topic. Each angle becomes a section.

Two common shapes:

**Shape A — single anchor, multiple angles:** One verse or mishnah is the topic's anchor (e.g. Prayer → Brachot 26b). The sections are different angles: timing, language, intentionality, communal vs private. All sections share `primaryText`.

**Shape B — multiple anchors, chronological:** The topic has no single anchor (e.g. Akedah → Genesis 22, but also Pirkei Avot 5:3, Brachot 32b, etc.). Each section anchors on a different text. The arc walks chronologically from biblical to rabbinic to medieval.

For Shape B, sections do NOT collapse (different primary texts), so the section-title cards display prominently between them — as they did before the grouping change.

Topic mode has the most design freedom. Use `AskUserQuestion` to confirm shape (single anchor vs multi-anchor) and section count before writing.

## Mode 4 — Nechama parsha (weekly)

Use when the user gives a parsha name and asks for "Nechama on Parshat X" — a
multi-decade rendering of Nechama Leibowitz's actual gilyonot for that parsha.

### Two artifacts per parsha

This mode produces both a **research pack** (markdown) and the **Close Read** (JSON).
The pack is the source of truth; every claim about Nechama in the JSON traces back to it.

- `research/parshiyot/<parsha>.md` — inventory + design proposal + per-leaf source notes
- `data/<parsha>.json` — the rendered close-read

### Source

Nechama's sheets are on Sefaria as user **54380**.

- Full sheet listing: `https://www.sefaria.org/api/sheets/user/54380` (needs `User-Agent` header)
- Filter to one parsha client-side: `topics[].slug == "parashat-<name>"`
- One sheet's full body: `https://www.sefaria.org/api/sheets/<id>` — returns ordered `sources[]`,
  each either an `outsideText` (her prose/section-header/question) or has a `ref` + `text`
  (a source she chose: verse, Rashi, midrash, etc.)

Her sheets are internally organized as **Hebrew-letter sections** (`א.`, `ב.`, `ג.` …),
each containing 1–N sources she chose, prose framing, and numbered questions she asks.

### Workflow (stages)

**Stage 1 — Inventory** (~30 min). Fetch all her sheets for the parsha. For each: year (Hebrew
& Gregorian), sheet ID, sub-topic, and her internal section labels. Cluster by theme. Note
conspicuous absences (parsha-topics she didn't write on). File into `research/parshiyot/<parsha>.md`.

**Stage 2 — Design** (~20 min). Pick **4–6 themes** for Level 0 and **2–4 of her gilyonot per
theme** for Level 1 (selection criterion: temporal spread across her career + interpretive
contrast). Present the outline. **Stop and confirm with the user before harvesting.**

**Stage 3 — Source harvest** (~2 hr). For each chosen sheet, parse the cached `/api/sheets/<id>`
response into structured per-leaf data: section labels, the sources she chose, her questions.
Save under `research/parshiyot/<parsha>-harvest/<theme>/<year>.json`. Verse texts for each
theme's `primaryText` come from Sefaria MCP `get_text` against the `Miqra according to the
Masorah` version — cleaned with the standard cantillation strip *and* maqaf→space (the repo's
convention; see existing data files).

**Stage 4 — Draft the JSON** (~3 hr). Build the file as overview → root-fork → per-theme (intro
→ theme-fork → leaves). Each leaf renders one gilayon: 1–2 opening narration cards (year + her
framing), **3 of her cruxes** (not all — pick the pedagogically rich ones), each crux =
narration setting up the question → her chosen commentary card(s) → a `question` card using
the `questionLabel: "Nechama asks"` feature in the title block. Closing question.

**Stage 5 — Validate + ship** (~30 min). JSON parse check, word-group validation script from
hard-rules.md, browser verify all leaves reachable via path forks. Add to `data/index.json`.

### Structural rules

- **Trim `primaryText` to verses the leaves actually anchor on.** A theme's verse
  range might be Num 6:1–21 in principle, but if the leaves only reference verses
  2, 5, 7, 11, only those should be in the panel. Join skipped verses with `…` in
  both `he` and `en`. Set `ref` to the actual range you ship (e.g. `Numbers 6:1-3, 5, 7, 11`)
  so the citation chip tells the truth. Long passages overflow the sticky panel
  even with cqi font scaling — trimming is the cure, not bigger fonts.
- **Each leaf has its own section ID** like `<theme>-<year>` (e.g. `gezel-1944`). The Level-1
  fork's branches set `target: <theme>-<year>` and `id: <theme>-<year-prefix>` (e.g. `g-1944`).
- **Leaves within a theme share `primaryText`** (same `ref` and `he`) so the engine collapses
  them into one sticky panel. Define the theme's `words` map once, in a Python dict reused
  across all leaves in that theme (the build script in `/tmp/nechama/build_nasso.py` from
  the Nasso build shows the pattern).
- **Narrator's role narrows.** The narrator names the gilayon (year), names her question,
  names the commentator about to speak — and gets out of the way. No moralizing. No paraphrase
  of what the commentary is about to say.
- **Source label is bilingual when the commentator has a Hebrew name** (`{he: "רש\"י", en: "Rashi"}`).
  English-only is fine for modern voices (`{en: "R. Samson Raphael Hirsch"}`).
- **`Nechama Leibowitz` is a registered source token** with its own CSS color (teal, `--color-nechama`).
  Use her as `source` only when the card actually quotes her own writing (Iyunim, an essay
  passage). Her *questions* go in `question` cards using the title-block's `questionLabel`,
  not as commentary cards.

### Selection heuristic for which gilyonot become leaves

Not every sheet becomes a leaf. Aim for **3 leaves per theme** (4 for a topic she returned
to particularly heavily, like Korban HaNesi'im on Nasso). Criteria:

1. **Temporal spread.** Early (her first decade) + middle (her mature period) + late (her
   final years). The reader feels her returning across decades.
2. **Interpretive contrast.** Two sheets that ask the same question are redundant. Pick sheets
   that *shift the angle* — the early dispute, the mature framing, the late synthesis.
3. **Density.** At least one sheet per theme should have ≥4 cruxes (so the leaf renders rich).
   Single-section "essay" sheets work as the late-period leaf.

### Selection heuristic for which cruxes (within a sheet) become cards

Each sheet has 3–11 cruxes. Render **3 of them per leaf** (not all).

- Prefer cruxes where she pits two commentators against each other.
- Prefer cruxes where her question is sharp and the verse-fragment is highlightable.
- Skip technical-grammar cruxes (e.g. "why hifil and not piel") unless the grammar is the
  pedagogical point.
- Pick cruxes that *cohere* — three different angles on a single thread, not three random shots.

### Canonical example

`data/nasso.json` is the worked example: 4 themes, 13 leaves, 158 step cards.
Research pack: [research/parshiyot/nasso.md](../../../research/parshiyot/nasso.md).
Build script template: `/tmp/nechama/build_nasso.py` from that build session.

---

## Crux selection (all modes)

A "crux" — what becomes a section after the plain reading — is a place where the text's words demand interpretation. Signs you've found a crux:

- Commentators disagree visibly about it (multiple distinct readings exist)
- A literal reading is troubling, embarrassing, or contradicts a known principle
- The text shifts register (genre / tone / speaker / addressee) mid-sentence
- A word is unexpected, a phrase repeats, or a clause seems missing
- The corpus tradition keeps returning to this spot

Don't manufacture cruxes. If a base text only has one real interpretive question, use 3 sections (A: plain reading; B: the question; C: forward), not 5.

## Length calibration

- Quick read: 3 sections, ~15–20 steps. Single crux. Skip the Carried Forward section.
- Standard: 4 sections, ~25–30 steps. Two cruxes. Carried Forward optional.
- Deep dive: 5 sections, ~35–45 steps. 2–3 cruxes plus Carried Forward.

Steps that look pedagogically required but bloat the count without value: phrase-by-phrase cards for phrases that aren't doing interpretive work, "tying-the-bow" narration cards, restating the question after a commentator already named it. Cut these.
