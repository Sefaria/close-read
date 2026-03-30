# Converting a Sefaria Sheet to Close Read Data

Step-by-step guide for turning a Sefaria source sheet into a `data/*.json` file.

## File Naming

Use the pattern: `{parasha}-{year}.json`

- Parasha name in transliterated English, lowercase (e.g. `noah`, `vayera`, `lech-lecha`)
- Year in Hebrew calendar digits (e.g. `5712`, `5715`)
- Examples: `noah-5712.json`, `vayera-5715.json`, `bereshit-5730.json`

If the sheet isn't tied to a specific year, use a descriptive slug: `noah-flood-narrative.json`.

## Conversion Checklist

### 1. Identify the Structure

Open the Sefaria sheet and map out:

- [ ] **Title**: Hebrew + English title, subtitle, author
- [ ] **Sections**: How does the sheet break into thematic units? Each unit becomes a section
- [ ] **Primary verses**: Which biblical verse anchors each section?
- [ ] **Commentary flow**: What order do the commentators appear in each section?
- [ ] **Questions**: Where does the author pose study questions?

Not all sheets break neatly into sections. Some have a single flowing argument; others jump between many verses. Use your judgment -- a section should correspond to "one verse (or verse pair) being examined."

### 2. Build the Title Object

```json
{
  "title": {
    "he": "...",
    "en": "...",
    "subtitle": { "he": "...", "en": "..." },
    "author": { "he": "...", "en": "..." },
    "sourceUrl": "https://www.sefaria.org/sheets/XXXXX",
    "sourceLabel": "View the original sheet on Sefaria",
    "questionLabel": { "he": "נחמה שואלת", "en": "Nechama asks" }
  }
}
```

Adjust `questionLabel` to match the sheet's author. For non-Nechama sheets, use the appropriate name or omit for no label.

### 3. Build Each Section

For each section:

**a. Set the primary verse**

- Use the Sefaria API or MCP tool to get the exact Hebrew text with nikkud/cantillation as it appears on Sefaria
- Get the English translation (JPS or the one used on the sheet)
- The `ref` must be a valid Sefaria reference (e.g. `"Genesis 8:1"`)

**b. Define word groups**

Look at which words the commentators focus on. For each target phrase:

- Create an ID (kebab-case, descriptive): `kol-hachaya`, `vayizkor`
- Copy the exact Hebrew from the verse text (must match character-for-character including nikkud)
- Write the corresponding English phrase
- For comparison mode, add `"side": "left"` or `"right"` if the phrase exists in both panels

**c. Create the steps array**

Walk through the sheet's content in order. For each piece:

| Sheet content | Step type |
|---|---|
| Contextual narration, setup text | `narration` |
| A quoted commentary with source | `commentary` |
| A study question from the author | `question` |
| A shift to a different verse | `verse-change` (followed by steps on the new verse) |

For each step:
- Give it a unique `id` within the file (e.g. `a-rashi`, `b-question-1`)
- Set `highlight` to the word group IDs this step draws attention to
- Omit `highlight` for intro/setup steps (verse shows at full opacity)
- Use `"effect": "glow"` or `"effect": "pulse"` sparingly for emphasis

**d. Handle verse transitions**

When the sheet moves to a new verse within a section:
1. Insert a `verse-change` step with the new verse data (including its own `words` map)
2. Place it *before* any commentary steps that reference the new verse
3. Word group IDs in the new verse are independent of the previous verse

### 4. Commentary Steps

```json
{
  "id": "a-rashi",
  "type": "commentary",
  "source": "Rashi",
  "ref": "Rashi on Genesis 8:1:2",
  "sourceLabel": { "he": "רש\"י", "en": "Rashi" },
  "text": { "he": "...", "en": "..." },
  "highlight": ["kol-hachaya"],
  "annotation": { "he": "...", "en": "..." }
}
```

- `source`: Must match a CSS color mapping (see below). Unknown sources get a neutral fallback color
- `ref`: Sefaria reference for linking. Use the specific commentary ref, not just the commentator name
- `annotation`: The sheet author's own note or framing of the commentary. Optional

### 5. Comparison Mode

When the sheet compares two verses side by side:

```json
{
  "ref": "Genesis 8:7-8",
  "mode": "comparison",
  "left": { "ref": "Genesis 8:7", "he": "...", "en": "..." },
  "right": { "ref": "Genesis 8:8", "he": "...", "en": "..." },
  "words": { ... }
}
```

This works for both `primaryText` and `verse-change` new verses.

## Source Color Mapping

These sources have explicit colors in CSS:

| Source | Color family |
|---|---|
| `Rashi` | Warm brown |
| `Ramban` | Green |
| `Ibn Ezra` | Blue |
| `Bereshit Rabbah` | Purple |
| `Aggadat Bereishit` | Purple |
| `Tanchuma` | Purple |

Any other `source` value gets a neutral warm-brown fallback. To add a new color, add a CSS rule in `close-read.css`:

```css
.source-label[data-source="NewSource"] { background: ...; color: ...; }
```

## Getting Text from Sefaria

### Sheet content via API

Fetch the full sheet JSON from `https://www.sefaria.org/api/sheets/{id}`. The `sources` array contains every item in order. Each source has one of these shapes:

| Source type | Key | Contains |
|---|---|---|
| Library text | `ref`, `text.he`, `text.en` | Biblical verse or commentary with exact ref |
| Author's text (English) | `outsideText` | HTML string — the author's own analysis |
| Author's text (bilingual) | `outsideBiText.he`, `outsideBiText.en` | HTML strings for both languages |

Strip HTML from `outsideText` / `outsideBiText` content. Keep `<i>` tags for transliterated terms; remove everything else (`<div>`, `<b>`, `<a>`, `<small>`, `<p>`).

### Verse text via MCP tools or API

- `get_text` with a ref like `"Genesis 8:1"` returns Hebrew + English
- `get_text` with a commentary ref like `"Rashi on Genesis 8:1:2"` returns the commentary text
- `get_links_between_texts` can help find which commentaries exist for a verse

### Hebrew text: strip cantillation marks

Sefaria's Masoretic text includes both nikkud (vowel points, U+05B0–U+05BC) and cantillation marks (te'amim, U+0591–U+05AF). **Strip cantillation marks and keep only nikkud.** Also strip the meteg (U+05BD) and sof pasuk (׃).

Python one-liner: `re.sub(r'[\u0591-\u05AF\u05BD׃]', '', text)`

This matches the Noah data file's convention and keeps the text readable. Word groups in the `words` map must match the stripped verse text exactly.

### English translations

Use the same translation the sheet uses. Check which version appears in the sheet's `ref`-type sources — that's usually JPS, JPS Gender-Sensitive, or Koren. Be consistent across the whole file.

## Variable Sheet Structures

Not all sheets fit the "one pinned verse + scrolling commentary" pattern perfectly. Common variations:

- **Single long argument**: One section with many steps, no verse changes. This works fine
- **Many short verses**: Consider grouping related verses into sections, using verse-changes within each
- **No clear questions**: Omit question steps; use narration for the author's own observations
- **Multiple authors**: Set `questionLabel` per-step to attribute questions correctly
- **Non-biblical primary text**: The engine doesn't require biblical verses -- any bilingual text works as `primaryText`

When in doubt, prioritize the reading experience. The goal is a guided journey through the text, not a 1:1 reproduction of the sheet layout.

## Lessons from Conversions

### English-only analysis sheets (e.g. Klitsner)

Some sheets have bilingual verses but English-only commentary (`outsideText`, not `outsideBiText`). For these:

- Set `"he": ""` on narration cards where there's no Hebrew analysis text. The empty div collapses gracefully in the rendered card.
- Where the sheet has bold Hebrew phrase sub-headers (e.g. **"וְהָאָדָם יָדַע"** introducing an analytical thread), use those as the `he` field — they serve as visual anchors connecting the card to the pinned verse.
- Use `narration` type throughout. Don't force the `commentary` type for paraphrased sources — it's misleading if the text isn't a direct quote. The author's voice is the consistent thread.

### Multiple sections on the same verse

A long analysis of a single verse can span multiple sections. Sections A and B can both have `"ref": "Genesis 4:1"` as their `primaryText` — the engine renders each section's primary text area independently. Use different `words` maps per section to highlight different aspects of the same verse.

### Word group design

- **No overlapping phrases within a section.** If you need to highlight "קָנִיתִי" alone sometimes and "קָנִיתִי אִישׁ" together at other times, define them as separate non-overlapping groups (`kaniti`, `ish`) and combine them in the `highlight` array: `["kaniti", "ish"]`.
- **The regex replaces ALL occurrences** of a phrase (global flag). If "Abel" appears twice in a verse, both instances get wrapped. This is usually fine — you want all instances highlighted.
- **English word groups must be unique substrings** of the English verse text. Watch for common words that appear multiple times.

### Sectioning a flowing essay

For sheets structured as continuous literary analysis rather than commentator-by-commentator:

1. Identify the 2–4 major analytical threads or textual foci
2. Each focus becomes a section, even if the same verse is primary
3. Aim for 4–8 cards per section (fewer feels thin, more feels like a slog)
4. Combine short adjacent paragraphs into single cards; split very long ones at natural paragraph breaks
5. Short transitional sentences ("But first, the text introduces Abel.") work well as intro cards with no highlight — they give the verse breathing room

### Card rhythm

- First card in each section: no highlight (verse breathing pattern)
- Build from narrower to broader highlights across a section (one word → phrase → full clause)
- Use `"effect": "glow"` for the climactic moment in a section (Eve's full speech, the key theological claim)
- Use `"effect": "pulse"` for ominous or foreboding moments (Abel's name meaning "vapor")
- End sections with a no-highlight transitional card when possible — a palate cleanser before the next section title

## Testing

1. Save your file as `data/{name}.json`
2. Add an entry to `data/index.json` with the slug, title, author, and description
3. Open `index.html?sheet={name}` in a browser (needs a local server)
4. Scroll through slowly, checking:
   - [ ] All verse text renders correctly (especially Hebrew with nikkud)
   - [ ] Word highlights match the right phrases
   - [ ] Verse crossfades trigger at the right moments
   - [ ] Commentary cards have correct source labels and colors
   - [ ] Questions display with the right label
   - [ ] No highlight conflicts (two cards highlighting at once)
   - [ ] Comparison mode renders side-by-side on desktop, stacked on mobile
