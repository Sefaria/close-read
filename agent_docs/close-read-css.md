# css/close-read.css
> Source: [css/close-read.css](../css/close-read.css)

## Purpose
The entire visual layer in a single ~750-line stylesheet: design tokens, the sticky-text + scrolling-cards layout, source-specific colors, word-highlight states, and the mobile breakpoint. The engine emits class names; this file maps them to appearance. There is no JS styling beyond a couple of inline `style="..."` strings on the error fallback.

## Structure (in source order)
1. Reset + base (`*`, `html`, `body`)
2. `:root` design tokens (colors, fonts, easing)
3. Title screen + `scroll-hint` keyframes
4. Section structure (`.cr-section`, `.section-title-card`)
5. Scrollytelling layout (`.scroll-container`, `.primary-text-area`, `.primary-text-content`)
6. Comparison mode (`.primary-text-content.comparison-mode`, `.comparison-side`, `.comparison-vs`)
7. Word highlighting (`.word-group` + state classes)
8. Commentary, question, and narration card variants
9. Progress bar + section dots
10. Closing screen
11. `@media (max-width: 768px)` responsive overrides
12. Index page (`.index-list`, `.index-card`)
13. `@media (prefers-reduced-motion: reduce)`

## Key tokens

- **Backgrounds**: `--color-bg` (#faf8f4 cream), `--color-bg-warm` (#f5f0e8), `--color-bg-card` (white).
- **Text hierarchy**: `--color-text` → `--color-text-secondary` → `--color-text-muted` → `--color-text-dimmed`. Used for emphasis stepping.
- **Accent**: `--color-accent` (#8b5e3c warm brown) is the global highlight color.
- **Two highlight colors**: `--color-highlight` (brown, default) and `--color-highlight-2` (#2e6b8a blue, applied to the right side of comparison mode).
- **Source palette**: `--color-rashi` (brown), `--color-ramban` (green), `--color-ibn-ezra` (blue), `--color-midrash` (purple). Applied via `[data-source="..."]` attribute selectors on `.source-label`.
- **Fonts**: `--font-hebrew` (Frank Ruhl Libre), `--font-english` (Crimson Text), `--font-ui` (Inter).
- **Easing**: `--ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1)` is reused across every transition.

## Non-obvious patterns

- **Sticky layout uses flex `order`, not float.** `.scroll-container` is `display: flex` with `.step-track { order: 1; width: 40%; }` and `.primary-text-area { order: 2; width: 60%; margin-left: auto; position: sticky; top: 0; height: 100vh; }`. Source order is left-to-right by DOM, but `order` puts the sticky column on the visual right. Mobile flips `flex-direction: column` and uses `order: 1` / `order: 2` to put primary text on top.
- **Right comparison panel coloring uses a `.right` class.** `buildComparisonVerse` (engine.js) stamps `comparison-side left` / `comparison-side right` on the two panels; the blue (`--color-highlight-2`) is applied via `.comparison-side.right .word-group.highlighted`. Word groups with `"side": "right"` in the data still don't drive coloring — DOM class does.
- **Dimming uses `color`, not `opacity`.** `.word-group.dimmed { color: var(--color-text-muted); opacity: 1; }`. The redundant `opacity: 1` is a defensive override — a prior approach used opacity and double-dimmed when both the word and container dimmed. Keep `color` here.
- **`.has-highlights` cascades to un-wrapped text.** When the engine adds this class to the active `.primary-text-content`, *all* `.primary-he` / `.primary-en` inside become muted, *except* word-groups marked `.highlighted` (which override). This is how partial highlight works without wrapping every word.
- **Narration cards strip card chrome.** `.step-card[data-type="narration"] .card-inner` zeroes the background, border, and shadow — narration looks like flowing prose, not a card.
- **Question cards use a gradient + circled "?".** Both visual cues are CSS-only: a `linear-gradient(135deg, accent-soft, card)` on the inner, and a `::before` pseudo-element drawing the circle with `border-radius: 50%`.
- **First and last step cards have padding adjustments.** `.step-card:first-child { padding-top: 30vh; min-height: 80vh; }` so the first card has breathing room above; `:last-child { padding-bottom: 20vh; }` to give the section a soft ending before the next section title.
- **`@media (prefers-reduced-motion: reduce)` is the universal off-switch.** Sets every animation and transition to 0.01 ms via `*` selector. No per-feature opt-in.
- **18 px base on desktop, 16 px on mobile.** `html { font-size: 18px; }` plus a `@media (max-width: 768px) { html { font-size: 16px; } }` override. All `rem`-based sizes scale with this.

## Where to look first
- **Adding a source color**: `~lines 408–413`. Add a `.source-label[data-source="NewSource"] { background: …; color: …; }` rule.
- **Tuning highlight intensity**: `.word-group.highlighted` (~line 304) and `.has-highlights .primary-he` (~line 331).
- **Mobile layout tweaks**: the single `@media (max-width: 768px)` block at the bottom (~lines 635–690).
- **New step type styling**: add `.step-card[data-type="newtype"] .card-inner { … }` alongside the existing narration/question variants.

## Relationships
- **Consumed by**: every DOM element produced by [engine-js.md](engine-js.md). The class names and `data-*` attributes that JS emits are this file's selectors.
- **Triggered by**: [text-effects-js.md](text-effects-js.md) for `.dimmed`, `.highlighted`, `.glow`, `.pulse`, `.has-highlights`, `.fading-out`, `.active`.

## See also
- [engine-js.md](engine-js.md) — where each class name originates.
- [text-effects-js.md](text-effects-js.md) — runtime class toggling for word effects.
