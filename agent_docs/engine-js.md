# js/engine.js
> Source: [js/engine.js](../js/engine.js)

## Purpose
The app's entry point and orchestrator. On `DOMContentLoaded` it either renders the sheet index (when no `?sheet=` param) or fetches a sheet's JSON and constructs the entire scrollytelling experience from it via the `CloseReadApp` class. Nothing else writes to the DOM — every section, card, and ScrollTrigger originates here. Word-level effects are delegated to `TextEffects`.

## Key functions

### Top-level (module-scoped)
- `DOMContentLoaded` handler — reads `?sheet=`, branches to `buildIndex()` (no param) or fetches `data/<slug>.json`, instantiates `CloseReadApp`, and calls `ScrollTrigger.refresh()` 200 ms after init.
- `buildIndex()` — fetches `data/index.json` and renders a list of sheet cards on the title screen. Runs only when no `?sheet=` is provided.

### `CloseReadApp`
- `init()` — orchestrates the full build: title, **branch tree**, sections, closing, **path-from-URL + initial visibility**, section nav (dots OR breadcrumb), scroll triggers, progress bar, page title, **popstate listener**.
- `buildBranchTree()` — scans `data.sections` once and builds `this.tree = { decisions, targets, decisionsByLevel }`. Used by every later branching method. For sheets with no decision sections the tree is empty and the engine behaves linearly.
- `readPathFromUrl()` / `writePathToUrl(path)` / `normalizePath(segments)` — URL ↔ path-array round-trip. Normalization walks segments left-to-right and drops the first invalid one (and everything after).
- `pathToVisibleSet(path)` — pure function from a path array to the set of section IDs visible at that path. Used by `applyVisibility`, `updateChosenButtons`, `renderBreadcrumb`, and `normalizePath`.
- `applyVisibility()` — toggles `.is-hidden` on every `.cr-section` based on `pathToVisibleSet(currentPath)` and updates `.is-chosen` on branch buttons. No-op on sheets without branching.
- `onBranchClick(decisionSectionId, branchId)` — the click handler for branch buttons. Mutates `currentPath` at the decision's `level` (dropping anything deeper), re-applies visibility, writes the URL, re-renders breadcrumb, then refreshes ScrollTrigger and smooth-scrolls to the new target inside a `requestAnimationFrame`.
- `wirePopstate()` — listens for browser back/forward and re-applies path + breadcrumb + refresh.
- `buildSections()` — for each `section` in the data: creates a `.cr-section` wrapper, a section-title card, and a `.scroll-container` flexbox containing a sticky `.primary-text-area` and a scrolling `.step-track`. Pre-renders **all** verses for the section (the `primaryText` plus every `verse-change.newVerse`) inside the primary-text-area, with only the first marked `.active`. Decision sections (`type: "decision"`) dispatch to `buildDecisionSection()` instead — a full-width fork with no sticky pane.
- `buildDecisionSection(section)` — full-width `.cr-section[data-type="decision"]` containing a `.decision-prompt` and a `.decision-branches` grid of `.decision-branch-button` elements, each wired to `onBranchClick`.
- `buildVerseContent(verseData, isActive)` / `buildComparisonVerse(...)` — build a single or comparison `.primary-text-content` element. Queues `TextEffects.wrapWords` via `requestAnimationFrame` so wrapping happens after the verse is in the DOM.
- `buildStepCard(step)` — renders one card per step type (`commentary`, `question`, `narration`). `verse-change` steps are skipped here (they're consumed by `buildSections` to build the alternate verses).
- `setupScrollTriggers()` — creates one ScrollTrigger per `.step-card` with `start: 'top 55%'` / `end: 'bottom 40%'`, wiring `onEnter`/`onEnterBack` to `activateStep` and the leave handlers to `deactivateStep`. Also adds entrance animations to section-title children.
- `activateStep(card, sectionEl, sectionData)` — the core scroll-driven logic. Deactivates other active cards in the same section, finds the target verse by scanning backwards through `sectionData.steps` for the most recent `verse-change`, calls `TextEffects.crossfadeTo` if the verse must change, and then either highlights the step's word groups or calls `TextEffects.reset()`.
- `deactivateStep(card)` — removes `.is-active`; if no card is active anywhere, calls `TextEffects.reset()`.
- `buildSectionNav()` / `setActiveDot(i)` — fixed-position dots on the left for linear sheets. On branching sheets (`tree.decisions.size > 0`) the dots are skipped and a `renderBreadcrumb()` call replaces them with a path breadcrumb at the top of the viewport.
- `renderBreadcrumb()` — populates `.section-nav.is-breadcrumb` with one clickable crumb per visible level of the current path (Overview › theme › leaf). Re-renders on every path change.
- `setupProgressBar()` — single body-scoped ScrollTrigger that updates `.progress-bar` `scaleX` to match scroll progress.

## Non-obvious patterns

- **No "default sheet".** With no `?sheet=` param, the index page renders from `data/index.json`.
- **`gsap.registerPlugin(ScrollTrigger)` is gated.** It runs only when a sheet is requested (line 16). The index page never registers it. Don't call `ScrollTrigger.*` from the index path.
- **`document.fonts.ready` matters.** App init waits on font loading because GSAP's ScrollTrigger captures element positions at registration time; Hebrew reflow on font swap would invalidate every trigger.
- **All alternate verses are pre-rendered.** `buildSections` walks every `verse-change` step and renders each `newVerse` into `.primary-text-area` up front. `activateStep` toggles `.active` on the right one; nothing is built lazily. This is what makes crossfade possible: both elements already exist.
- **Verse search is backwards from the step.** `activateStep` finds the active verse by iterating `sectionData.steps` from `stepIndex - 1` down to 0 looking for a `verse-change`. If none is found, it falls back to `sectionData.primaryText`. The "verse-change must precede its steps" rule from the data format is enforced here — there is no forward search.
- **Exclusive activation per section.** Before adding `.is-active`, the function clears `.is-active` from every other card in the *same* section. Cross-section overlap is possible but never observed because trigger zones (55%–40%) don't span sections in practice.
- **Hard-coded 200 ms / 100 ms timeouts.** `ScrollTrigger.refresh()` is delayed 200 ms after init for layout settle; `wrapWords` is re-run 100 ms after `crossfadeTo` to catch the newly-active content. Repeat wrap calls are safe — `_wrapPhrase` short-circuits if the group is already wrapped (see [text-effects-js.md](text-effects-js.md)).
- **Step-card data attributes carry state.** `data-highlight` is a JSON-encoded array stringified at build time and parsed in `activateStep`. `data-effect` carries the effect name. This means highlight data round-trips through the DOM — convenient, but be careful about quoting if you ever add nested structures.
- **Refs become Sefaria URLs via `replace(/\s+/g, '_')`.** This is the only ref-to-URL transform — no encoding of Hebrew or punctuation. Works because all current refs are ASCII.
- **No error retries.** A failed `fetch` writes an inline error div and stops; nothing retries or falls back.

## Relationships
- **Depends on**: `gsap`, `gsap/ScrollTrigger` (CDN globals); [text-effects-js.md](text-effects-js.md) (`TextEffects` global); HTML shell selectors (`.title-screen`, `#main-content`, `.section-nav`, `.closing-screen`, `.progress-bar`); data files in `data/`.
- **Depended on by**: [index.html](../index.html) loads it as the last script tag.

## See also
- [text-effects-js.md](text-effects-js.md) — word wrapping, highlighting, crossfade.
- [close-read-css.md](close-read-css.md) — the class names this file emits (`.scroll-container`, `.primary-text-content.active`, `.step-card.is-active`, etc.).
- [../docs/data-format.md](../docs/data-format.md) — the JSON schema the engine consumes.
- [../docs/architecture.md](../docs/architecture.md) — broader system overview.
