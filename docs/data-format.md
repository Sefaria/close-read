# Close Read: Data File Format

Each Close Read experience is driven by a single JSON file in `data/`. This document describes the schema.

## Top-Level Structure

```json
{
  "title": { ... },
  "sections": [ ... ]
}
```

### `title`

Metadata for the title screen, closing screen, and page `<title>`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `he` | string | yes | Hebrew title (e.g. "פרשת נח תשי״ב") |
| `en` | string | yes | English title |
| `subtitle.he` | string | yes | Hebrew subtitle |
| `subtitle.en` | string | yes | English subtitle |
| `author.he` | string | yes | Hebrew author name |
| `author.en` | string | yes | English author name |
| `sourceUrl` | string | no | URL to original source (e.g. Sefaria sheet) |
| `sourceLabel` | string | no | Link text for source URL. Defaults to "View the original source" |
| `questionLabel` | `{he, en}` | no | Label for question cards (e.g. `{"he": "נחמה שואלת", "en": "Nechama asks"}`). Can also be overridden per-step |

---

## `sections`

An array of section objects. Each section has a primary text that stays pinned on the right side of the screen, and a sequence of steps (commentary cards) that scroll on the left.

### Section Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique DOM id (e.g. `"section-a"`) |
| `title.he` | string | yes | Hebrew section heading |
| `title.en` | string | yes | English section heading |
| `primaryText` | VerseData | yes | The verse pinned on screen when the section begins |
| `steps` | Step[] | yes | Ordered sequence of cards and verse changes |

---

## VerseData

A verse can be rendered in two modes: **single** (default) or **comparison** (side-by-side).

### Single Verse

```json
{
  "ref": "Genesis 8:1",
  "he": "וַיִּזְכֹּר אֱלֹהִים אֶת־נֹחַ ...",
  "en": "God remembered Noah ...",
  "words": { ... }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | string | yes | Sefaria-style reference. Used for linking and for matching during verse crossfades |
| `he` | string | yes | Full Hebrew text of the verse |
| `en` | string | yes | Full English translation |
| `words` | WordMap | no | Word groups available for highlighting (see below) |

### Comparison Verse

Set `"mode": "comparison"` to show two verses side by side.

```json
{
  "ref": "Genesis 8:7-8",
  "mode": "comparison",
  "left": { "ref": "Genesis 8:7", "he": "...", "en": "..." },
  "right": { "ref": "Genesis 8:8", "he": "...", "en": "..." },
  "words": { ... }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ref` | string | yes | Combined reference for the pair. Must be unique within the section |
| `mode` | `"comparison"` | yes | Triggers side-by-side layout |
| `left` | object | yes | Left verse: `ref`, `he`, `en` |
| `right` | object | yes | Right verse: `ref`, `he`, `en` |
| `words` | WordMap | no | Word groups (use `side` to target left/right) |

---

## WordMap

A dictionary of targetable word groups. Keys are arbitrary IDs that steps reference in their `highlight` arrays.

```json
"words": {
  "kol-hachaya": {
    "he": "כׇּל־הַחַיָּה",
    "en": "all the beasts"
  },
  "me-ito": {
    "he": "מֵאִתּוֹ",
    "en": "from him",
    "side": "right"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `he` | string | yes | Hebrew phrase to match and wrap. Uses flexible whitespace matching (maqaf, spaces, zero-width chars) |
| `en` | string | yes | English phrase to match and wrap |
| `side` | `"left"` or `"right"` | no | Only for comparison mode. Limits matching to one side |

**How matching works**: The engine searches the rendered HTML for the exact phrase, allowing flexible whitespace. Each match is wrapped in a `<span class="word-group" data-word="key">`. When a step highlights that key, the span gets styled.

**Gotchas**:
- Hebrew phrases must match the verse text exactly (including nikkud if present)
- If a phrase appears in both the left and right comparison text, use `side` to disambiguate
- Keep English phrases unique enough to avoid matching substrings of other phrases

---

## Steps

Steps are the core content units. They scroll as cards on the left side. There are four types:

### `narration`

Contextual text with no source attribution. Renders without a card background.

```json
{
  "id": "a-intro",
  "type": "narration",
  "text": { "he": "...", "en": "..." },
  "highlight": ["word-id-1"],
  "effect": "glow"
}
```

### `commentary`

A source text with attribution, optional Sefaria link, and optional annotation.

```json
{
  "id": "a-rashi",
  "type": "commentary",
  "source": "Rashi",
  "ref": "Rashi on Genesis 8:1:2",
  "sourceLabel": { "he": "רש\"י", "en": "Rashi" },
  "text": { "he": "...", "en": "..." },
  "highlight": ["kol-hachaya", "kol-habehema"],
  "annotation": { "he": "...", "en": "..." }
}
```

### `question`

A study question, rendered with a distinctive border and a configurable label (from `title.questionLabel` or per-step `questionLabel`).

```json
{
  "id": "a-question",
  "type": "question",
  "text": { "he": "...", "en": "..." },
  "highlight": ["kol-hachaya"],
  "effect": "pulse"
}
```

### `verse-change`

Not a visible card. Tells the engine to crossfade the pinned verse to a new one. Must appear in the steps array *before* any steps that refer to the new verse.

```json
{
  "id": "b-transition",
  "type": "verse-change",
  "newVerse": {
    "ref": "Genesis 8:15-16",
    "he": "...",
    "en": "...",
    "words": { ... }
  }
}
```

The `newVerse` object follows the same VerseData format (single or comparison).

### Common Step Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique step identifier |
| `type` | string | yes | One of: `narration`, `commentary`, `question`, `verse-change` |
| `text` | `{he, en}` | yes* | Bilingual text content (*not on `verse-change`) |
| `highlight` | string[] | no | Array of word-group IDs to highlight when this step is active. Omit to show the verse at full opacity (no dimming) |
| `effect` | string | no | Highlight style: `"highlight"` (default), `"glow"`, or `"pulse"` |

### Commentary-Only Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `source` | string | yes | Source name, used for CSS color mapping (e.g. `"Rashi"`, `"Ramban"`). Unknown sources get a neutral warm-brown fallback |
| `ref` | string | no | Sefaria reference for linking |
| `sourceLabel` | `{he, en}` | yes | Display name for the source badge |
| `annotation` | `{he, en}` | no | Nechama's framing note, displayed below the source text |
| `questionLabel` | `{he, en}` | no | Override the title-level question label for this specific step |

---

## Source Color Mapping

The `source` field on commentary steps maps to CSS color classes. Currently supported:

| `source` value | Color |
|---------------|-------|
| `Rashi` | Warm brown |
| `Ramban` | Green |
| `Ibn Ezra` | Blue |
| `Bereshit Rabbah` | Purple |
| `Aggadat Bereishit` | Purple |
| `Tanchuma` | Purple |

To add a new source color, add a CSS rule: `.source-label[data-source="NewSource"] { ... }`

---

## Design Patterns

### Intro steps should have no highlights

The first step in each section should typically be a `narration` with no `highlight` array. This lets the verse appear at full opacity before any dimming begins.

### Verse changes precede their steps

Place `verse-change` steps in the array *before* the steps that reference the new verse's word groups. The engine searches backwards from each step to find the most recent verse-change.

### Word group IDs are scoped to their verse

Word group IDs only need to be unique within their verse's `words` map. Different verses can reuse the same IDs without conflict since only the active verse's words are in the DOM at any time.
