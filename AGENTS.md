# AGENTS.md

> Per-module detail lives in [agent_docs/](agent_docs/). This file is the map.
> For higher-level docs see [CLAUDE.md](CLAUDE.md) and [docs/](docs/).

Close Read is a static, data-driven scrollytelling engine for bilingual (Hebrew/English) Torah study. Pinned primary verse on one side; commentary cards scroll past on the other, triggering word-level highlights and verse transitions. No build step — plain HTML/CSS/JS plus GSAP from CDN.

## Module map

### Source
| Doc | Covers |
|---|---|
| [agent_docs/engine-js.md](agent_docs/engine-js.md) | `js/engine.js` — `CloseReadApp`, the orchestrator: data fetch, DOM build, ScrollTrigger wiring, step activation. |
| [agent_docs/text-effects-js.md](agent_docs/text-effects-js.md) | `js/text-effects.js` — word wrapping, highlight/dim/glow/pulse, verse crossfade. |
| [agent_docs/close-read-css.md](agent_docs/close-read-css.md) | `css/close-read.css` — all visual styling, layout, tokens, source colors, mobile breakpoint. |
| [agent_docs/data-files.md](agent_docs/data-files.md) | `data/*.json` — current sheets and the contract between content and engine. |

[index.html](index.html) is a 42-line shell (Google Fonts link, container divs, GSAP CDN, app scripts). No agent doc page — it's flat enough to read directly.

### Existing reference docs (kept in [docs/](docs/))
| Doc | Covers |
|---|---|
| [docs/data-format.md](docs/data-format.md) | Full JSON schema for sheets — every field, every step type. Authoritative. |
| [docs/architecture.md](docs/architecture.md) | System overview, init flow, layout diagram. **Partially stale** — see `.stamp` note. |
| [docs/conversion-guide.md](docs/conversion-guide.md) | Step-by-step for turning a Sefaria sheet into a `data/*.json` file. |

## Core conventions

1. **No build step.** Edit, refresh, done. Don't introduce bundlers, npm, or transpilation — the whole point is static delivery.
2. **Engine is data-driven.** [index.html](index.html) is intentionally empty; every element comes from `data/<slug>.json` via [engine-js.md](agent_docs/engine-js.md). Don't hand-author HTML for content.
3. **Dim with `color`, not `opacity`.** Mixing opacity at both word and container levels double-dims. See [close-read-css.md](agent_docs/close-read-css.md) and CLAUDE.md.
4. **Verse-change must precede its steps.** `activateStep` searches backwards from the current step; a `verse-change` placed *after* a step that references its words will leave those words unwrapped. See [engine-js.md](agent_docs/engine-js.md).
5. **First step in each section: no highlight.** Lets the verse breathe at full opacity before dimming begins. Recorded in CLAUDE.md and the conversion guide.
6. **Hebrew text in `words` entries must match verse text byte-for-byte** (including nikkud). Cantillation marks are stripped per the conversion guide; word groups must match the stripped form.
7. **Source colors are CSS, not JS.** Add a new source by adding a `.source-label[data-source="X"]` rule to [close-read-css.md](agent_docs/close-read-css.md). The engine just stamps `data-source` from the JSON.
8. **Refs become Sefaria URLs via `replace(/\s+/g, '_')` only.** Currently safe because all refs are ASCII; revisit if you add refs containing Hebrew or punctuation.
9. **Run from a server, never `file://`.** `fetch()` won't work otherwise. `python3 -m http.server 8080` is the convention.
10. **Register new sheets in [data/index.json](data/index.json).** Direct `?sheet=` URLs work without it, but the homepage won't list them.

## Freshness: regenerate [agent_docs/.stamp](agent_docs/.stamp)

The `.stamp` file records the commit these docs were last audited against. When you make substantial changes in a documented module, update the relevant page **and** bump the stamp.

Format:
```
commit=<40-char SHA>
date=<YYYY-MM-DD>
note=<one paragraph: what changed since last audit + any flagged quirks>
```
