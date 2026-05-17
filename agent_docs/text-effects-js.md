# js/text-effects.js
> Source: [js/text-effects.js](../js/text-effects.js)

## Purpose
Implements the word-level interaction layer: wraps phrases in the rendered verse HTML so they're targetable, applies highlight/dim/glow/pulse classes when steps activate, and crossfades between pre-rendered verses. Exposes a single `TextEffects` global; all callers live in [engine-js.md](engine-js.md).

## Key functions

- `wrapWords(container, words)` — for each `(groupId, group)` pair in the data file's `words` map, find `group.he` inside every `.primary-he` descendant and `group.en` inside every `.primary-en`, wrapping matches in `<span class="word-group" data-word="<groupId>" data-lang="he|en">`. Idempotent: a per-phrase guard in `_wrapPhrase` short-circuits repeat calls.
- `_wrapPhrase(el, phrase, groupId, lang)` — the regex-based wrapper. Early-returns if `el` already contains a `.word-group` with matching `data-word`/`data-lang`. Otherwise escapes special regex chars, then collapses internal whitespace to a character class accepting regular spaces, zero-width space, non-breaking space, Hebrew maqaf (U+05BE), and ASCII hyphen.
- `highlight(groupIds, options)` — adds `.dimmed` to every `.word-group` first, then removes `.dimmed` and adds `.highlighted` (plus optional `.glow` or `.pulse`) to spans matching `groupIds`. Also adds `.has-highlights` to the active `.primary-text-content` so un-wrapped text dims via CSS.
- `reset(animate)` — clears all four state classes (`dimmed`, `highlighted`, `glow`, `pulse`) from every `.word-group` and removes `.has-highlights` from every primary-text-content. The `animate` argument is accepted but unused.
- `crossfadeTo(sectionEl, newVerseData)` — finds the pre-rendered `.primary-text-content` whose `data-ref` matches `newVerseData.ref`, swaps `.active` from the current element to it, and adds a transient `.fading-out` class (cleared after 600 ms). If `newVerseData.words` is set, re-wraps words on the new element (no-op if already wrapped).

## Non-obvious patterns

- **`wrapWords` is idempotent by design.** `_wrapPhrase` checks for an existing `.word-group[data-word="..."][data-lang="..."]` on the element and returns early if found. This matters because the engine triggers up to 3 wrap calls on the same verse (initial `requestAnimationFrame` in `buildVerseContent`, `crossfadeTo`'s internal call, and a 100 ms-delayed re-wrap in `activateStep`). Without the guard, the regex still matches the phrase text inside an existing `.word-group` and produces nested spans.
- **`reset` runs inside `highlight`.** Every call to `highlight` calls `reset(false)` first so previous state cleanly clears. Don't add side effects to `reset` that you don't want fired on every highlight.
- **`.dimmed` works via `color`, not `opacity`.** The CSS sets `color: var(--color-text-muted); opacity: 1`. This is deliberate — see CLAUDE.md: opacity-based dimming compounded with container dimming caused double-dimming. Keep it as `color`.
- **`.has-highlights` dims un-wrapped text.** When `highlight` is active, *any* `.primary-he` / `.primary-en` text not inside a `.word-group` is dimmed by this container-scoped class in CSS. This is how partial highlighting works without wrapping every word.
- **Crossfade matches by `data-ref`, not identity.** All alternate verses are pre-rendered (see engine.js). Crossfade picks the right one by string-matching `dataset.ref` against `newVerseData.ref`. Refs must be unique within a section.
- **Empty-string `he` is fine.** Conversion guide notes that English-only sheets use `"he": ""` on cards; that's a card-text quirk, but `wrapWords` is also tolerant — empty `he`/`en` in a group just means no wrap on that side.

## Relationships
- **Depends on**: only the DOM. No external libraries.
- **Depended on by**: [engine-js.md](engine-js.md) — `wrapWords`, `highlight`, `reset`, `crossfadeTo`.

## See also
- [engine-js.md](engine-js.md) — call sites and the activation flow.
- [close-read-css.md](close-read-css.md) — the styles for `.word-group.highlighted`, `.dimmed`, `.glow`, `.pulse`, and `.has-highlights`.
- [../docs/data-format.md](../docs/data-format.md) — `words` map schema.
