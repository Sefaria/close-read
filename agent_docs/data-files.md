# data/*.json
> Source: [data/](../data/)

## Purpose
The content layer. Each `data/<slug>.json` produces one full scrollytelling page when visited at `?sheet=<slug>`. `data/index.json` is a manifest of all sheets, used to render the homepage when no `?sheet=` param is given. No code lives here — the engine reads these files as-is.

## Files

- **`index.json`** — array of `{slug, title.{he,en}, author.{he,en}, description}`. Drives the homepage. New sheets must be added here or they won't appear on the index (though they'll still load via direct `?sheet=` URL).
- **`<slug>.json`** — one per sheet. Top level: `{title: {...}, sections: [...]}`. Fully specified in [../docs/data-format.md](../docs/data-format.md).

Current sheets (as of stamp):
| Slug | Author | Topic |
|---|---|---|
| `cain-abel-birth-records` | Judy Klitsner | Literary analysis of Genesis 4:1–2 |
| `shemini-5731` | Nechama Leibowitz | Leviticus 10:3 |
| `yitro-5730` | Nechama Leibowitz | Exodus 20:5 |
| `kedoshim-5731` | Nechama Leibowitz | Leviticus 19:16 |
| `minhag-overview` | Zvi Hirschfield | Authority of custom in Halakhah |

## Non-obvious patterns

- **No "default sheet".** The engine renders the homepage from `data/index.json` when `?sheet=` is missing; otherwise it loads `data/<slug>.json`. No file is loaded "by default."
- **Hebrew text in `words` entries must match the verse text byte-for-byte, including nikkud.** Cantillation marks (te'amim, U+0591–U+05AF) and meteg/sof pasuk are stripped from verse text per the conversion guide; word groups must match the stripped form, not the raw Masoretic source. See [../docs/conversion-guide.md](../docs/conversion-guide.md) for the regex.
- **Word-group IDs are verse-scoped, not section-scoped.** Different verses (including a `primaryText` and a later `verse-change.newVerse`) can reuse the same IDs without conflict, because only the active verse's spans exist in the visible DOM at any time.
- **`verse-change` steps must precede their commentary.** Engine searches *backwards* from the current step to find the active verse — see [engine-js.md](engine-js.md). A forward-placed `verse-change` would leave earlier steps pointing at an outdated verse.
- **`source` value is a CSS hook, not a free-text label.** It maps to `[data-source="..."]` selectors in [close-read-css.md](close-read-css.md). Unknown values fall back to the default warm-brown badge. Add a CSS rule, don't add JS.

## Authoring workflow
See [../docs/conversion-guide.md](../docs/conversion-guide.md) — the canonical step-by-step for turning a Sefaria sheet into a data file. Covers naming, cantillation stripping, word group design, English-only sheets, multi-section-same-verse layouts, and a testing checklist.

## Relationships
- **Read by**: [engine-js.md](engine-js.md) (`fetch('data/<slug>.json')` and `fetch('data/index.json')`).
- **Documented by**: [../docs/data-format.md](../docs/data-format.md) (schema reference); [../docs/conversion-guide.md](../docs/conversion-guide.md) (authoring).
