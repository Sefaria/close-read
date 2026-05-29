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

A multi-decade rendering of Nechama Leibowitz's actual gilyonot for one parsha, as a
branching garden. This has graduated into its **own dedicated skill** — see
[`nechama-parsha`](../../nechama-parsha/SKILL.md). Invoke that skill when the user asks
to "build the Nechama flow for [parsha]", "do this week's parsha", "Nechama on [parsha]",
or similar.

In brief: inventory her sheets (Sefaria user 54380) → cluster into themes (Level 0) →
pick dated gilyonot per theme (Level 1) → render each sheet faithfully as a leaf. Two
artifacts: a research pack (`research/parshiyot/<parsha>.md`) and `data/<parsha>.json`.
The worked example is `data/nasso.json`. The editorial guidance (voice, source density,
faithfulness) and the quality/error discipline live in that skill's `references/`.

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
