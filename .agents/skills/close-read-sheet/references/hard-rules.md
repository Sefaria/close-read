# Hard rules — what the engine does and does not tolerate

Read this once before writing your first card.

## Hebrew text cleaning

The engine renders `he` fields as-is into RTL HTML. Cantillation marks distract; nikkud is essential.

**Strip cantillation, keep nikkud.** Unicode ranges to strip:

- U+0591 – U+05AF (most cantillation)
- U+05BD (meteg, when it's a cantillation marker)
- U+05C0 (paseq)
- U+05C3 (sof pasuq, ׃)
- U+05C6 (nun hafukha)

Keep U+05B0 – U+05BC (sheva, nikkud, dagesh).

Python recipe:

```python
import re
def strip_cantillation(text):
    return re.sub(r'[֑-ֽ֯׀׃׆]', '', text)
```

Which Sefaria versions need stripping:

| Version | Cantillation present? |
|---|---|
| `Torat Emet 357` (Mishnah, Avot) | No — use as-is |
| `Tanach with Nikkud` | No |
| `Miqra according to the Masorah` | **Yes — strip** |
| `Tanach with Ta'amei Hamikra` | **Yes — strip** |
| `Tanach with Text Only` | No (also has no nikkud, less ideal) |

Commentary texts (Rashi, Rambam, Bartenura, etc.) usually have no cantillation. The Vilna edition Rashi may include some markers in the verse-headers (the bold-formatted lemma fragments) — strip those.

## Word groups within a verse

The engine wraps each phrase in `<span class="word-group" data-word="<key>">`. Two rules:

1. **No overlapping phrases within the same verse's `words` map.** If `chachamim` is `חֲכָמִים` (one word) and `chachamim-hizaharu` is `חֲכָמִים, הִזָּהֲרוּ` (two words), the second wrap will collide with the existing span around the first. Result: one of them silently fails to wrap, and its highlight will not render. Pick *one* granularity per phrase.

2. **English phrases must be unique substrings within the verse's English.** The wrap uses a global regex; if the phrase occurs twice, both get wrapped — and the highlight will hit both, which is almost always wrong. Test before relying on a generic phrase like `"the children"` or `"and die"`.

For comparison-mode word maps, add `"side": "left"` or `"side": "right"` to disambiguate phrases that appear on both sides.

## Sections sharing a primary text

The engine collapses consecutive sections whose `primaryText.ref` and `he` are identical into one sticky panel. This is the default smooth-continuity behavior — usually what you want.

When sections share `primaryText`, their `words` maps are **merged into a union** for the single rendered panel. Therefore:

- Same key across sections must have the same `he` value. If section A defines `mayim-raim: וְתִגְלוּ לִמְקוֹם מַיִם הָרָעִים` and section B redefines `mayim-raim: לִמְקוֹם מַיִם הָרָעִים`, the union takes whichever wins the object-merge — which is hard to predict. Just keep them consistent.
- Don't introduce a wider key in a later section that overlaps an existing narrower key (the overlap rule above). If section A has `chachamim: חֲכָמִים` and section E wants to highlight `חֲכָמִים, הִזָּהֲרוּ בְדִבְרֵיכֶם` together, the right move is to give section E a *highlight array* of `["chachamim", "hizaharu-bedivreikhem"]`, not a new wider key.

## Source labels and colors

The engine routes `source` → CSS color via `data-source` attribute. Existing tokens:

| `source` value | Visual family |
|---|---|
| `Rashi` | warm brown (the default Rashi token) |
| `Ramban` | green |
| `Ibn Ezra` | blue |
| `Bereshit Rabbah`, `Aggadat Bereishit`, `Tanchuma` | midrash purple |
| `Mekhilta` | (neutral) |
| `Talmud` | (neutral) |
| `Abarbanel`, `Shem Olam` | (neutral) |
| *anything else* | neutral warm-brown fallback |

Don't add new tokens in this skill. If a sheet leans hard on a single un-tokenized commentator (e.g. Bartenura is the workhorse), mention it as a follow-up — the user can add a CSS rule later.

For `sourceLabel`:
- Use the commentator's Hebrew name when the corpus is bilingual: `{ "he": "רש״י", "en": "Rashi" }`
- English-only label is fine when the corpus is mostly English (modern voices, source-sheet derivations)
- Use the label to disambiguate when the same `source` field carries multiple voices: `"Mekhilta DeRabbi Yishmael"` vs `"Mekhilta DeRashbi"` both with `source: "Mekhilta"`

## When to use comparison mode vs inline quotation

| Situation | Format |
|---|---|
| Two short biblical verses in direct tension (e.g. Ex 20:5 vs Deut 24:16) | Comparison mode in `primaryText` |
| One short biblical verse cited by a commentary as a prooftext | Inline within the commentary's `text` or `annotation` |
| A full parallel mishnah or sugya being discussed | Inline as a `commentary` card with its own `sourceLabel` |
| A substantial parallel passage the user will dwell on | `verse-change` to a new single-mode primary, then return |

Comparison mode crowds the laptop layout when either side runs longer than ~3 short lines. For full mishnayot or paragraphs of Tanakh, always use inline or `verse-change`.

## When to use verse-change

- The new text is **substantive** and the user will study it (not just glance at a prooftext)
- The new text is **short enough** to fit comfortably in the sticky panel (one verse, one short paragraph)
- You can return to the base text within the same section

Counter-cases (use inline instead):
- A one-line prooftext quoted to support a commentary's reading
- A long passage you only want to gesture at
- A text the user will *compare* rather than study (in which case: comparison mode, if both are short enough)

## Validation script

Before declaring the sheet done, run this against the JSON:

```python
import json, re

d = json.load(open('data/<slug>.json'))

def check_words(verse, label):
    text = verse.get('he', '')
    sides = {'left': verse.get('left', {}).get('he', ''),
             'right': verse.get('right', {}).get('he', '')}
    for key, w in verse.get('words', {}).items():
        phrase = w['he']
        side = w.get('side')
        target = sides[side] if side else text
        pattern = re.escape(phrase).replace(r'\ ', r'[\s​]+').replace(r'\-', r'[\s־\-]')
        if not re.search(pattern, target):
            print(f"  MISSING in {label}: key={key!r} phrase={phrase!r}")

def check_en(verse, label):
    text = verse.get('en', '')
    sides = {'left': verse.get('left', {}).get('en', ''),
             'right': verse.get('right', {}).get('en', '')}
    for key, w in verse.get('words', {}).items():
        phrase = w['en']
        side = w.get('side')
        target = sides[side] if side else text
        n = target.count(phrase)
        if n == 0:
            print(f"  EN MISSING in {label}: key={key!r} phrase={phrase!r}")
        elif n > 1:
            print(f"  EN AMBIGUOUS in {label}: key={key!r} ({n} matches) phrase={phrase!r}")

for s in d['sections']:
    check_words(s['primaryText'], s['id'] + ' primary')
    check_en(s['primaryText'], s['id'] + ' primary')
    for step in s['steps']:
        if step.get('type') == 'verse-change':
            check_words(step['newVerse'], s['id'] + ' verse-change ' + step['id'])
            check_en(step['newVerse'], s['id'] + ' verse-change ' + step['id'])
print("done")
```

If anything prints, fix it before browser verification — most often the issue is a typo in the phrase or an English phrase that occurs twice.

## Browser verification checklist

Use `preview_start` then `preview_eval`. Confirm:

1. `document.querySelectorAll('.cr-section').length` — equals number of section *groups* (consecutive same-primary sections merge into one)
2. `document.querySelectorAll('.section-dot').length` — equals the total number of sections in JSON
3. `document.querySelectorAll('.section-divider').length` — equals total sections minus number of groups (the dividers shown for sub-sections beyond the first in each group)
4. `document.body.innerHTML.includes('undefined')` — must be `false`
5. Scroll to a card with a `highlight` array; verify `document.querySelectorAll('.word-group.highlighted, .word-group.glow, .word-group.pulse')` returns matching word keys
6. `preview_console_logs` filtered to `error` — must return nothing
