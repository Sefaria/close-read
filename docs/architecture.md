# Close Read: Technical Architecture

## Overview

Close Read is a static, data-driven scrollytelling engine for bilingual (Hebrew/English) Torah study. It takes a JSON data file and renders an interactive experience where a primary verse stays pinned on the right side of the screen while commentary cards scroll on the left, triggering word-level highlights and verse transitions.

No build step. No framework. HTML + CSS + vanilla JS, with GSAP ScrollTrigger from CDN.

## File Structure

```
close_read/
├── index.html              # Shell: empty containers, loads scripts
├── css/
│   └── close-read.css      # All styles, layout, typography, animations
├── js/
│   ├── engine.js           # Main app: fetches data, builds DOM, orchestrates scroll
│   └── text-effects.js     # Word-level highlighting and verse crossfade
├── data/
│   └── noah-5712.json      # Content data (swappable)
└── docs/
    ├── data-format.md      # JSON schema documentation
    └── architecture.md     # This file
```

## Initialization Flow

```
DOMContentLoaded
  ├── Register GSAP ScrollTrigger
  ├── Parse ?sheet= query param (default: "noah-5712")
  ├── fetch("data/{sheet}.json")
  └── document.fonts.ready
        ├── new CloseReadApp(data)
        ├── app.init()
        │     ├── buildTitleScreen()      ← from data.title
        │     ├── buildSections()         ← from data.sections
        │     ├── buildClosing()          ← from data.title
        │     ├── buildSectionNav()       ← dots + ScrollTrigger per section
        │     ├── setupScrollTriggers()   ← per-card triggers + title animations
        │     ├── setupProgressBar()      ← top progress indicator
        │     └── updatePageTitle()       ← document.title from data
        └── ScrollTrigger.refresh() (200ms delay for layout settle)
```

**Why `document.fonts.ready`**: ScrollTrigger calculates trigger positions based on element dimensions. If fonts haven't loaded yet, Hebrew text may reflow, causing all triggers to be miscalculated. Waiting for fonts prevents this.

## Layout Architecture

### Desktop (>768px)

```
┌──────────────────────────────────────────────────┐
│ Title Screen (full width, 100vh)                 │
├──────────────────────────────────────────────────┤
│ Section Title Card (full width, centered)        │
├───────────────────┬──────────────────────────────┤
│ Step Track (40%)  │ Primary Text Area (60%)      │
│ order: 1          │ order: 2                     │
│ position: static  │ position: sticky; top: 0     │
│ scrolls normally  │ height: 100vh                │
│                   │ border-left, box-shadow       │
│ ┌───────────────┐ │                              │
│ │ Card (intro)  │ │   GENESIS 8:1                │
│ │ min-h: 80vh   │ │                              │
│ │ pad-top: 30vh │ │   וַיִּזְכֹּר אֱלֹהִים       │
│ └───────────────┘ │   ...                        │
│ ┌───────────────┐ │                              │
│ │ Card (Rashi)  │ │   God remembered Noah...     │
│ │ min-h: 60vh   │ │                              │
│ └───────────────┘ │                              │
│ ┌───────────────┐ │                              │
│ │ Card (Ramban) │ │                              │
│ └───────────────┘ │                              │
├───────────────────┴──────────────────────────────┤
│ Next Section Title Card                          │
├──────────────────────────────────────────────────┤
│ ...                                              │
├──────────────────────────────────────────────────┤
│ Closing Screen (full width)                      │
└──────────────────────────────────────────────────┘
```

The `scroll-container` is a flexbox row. The step track (left, 40%) scrolls normally. The primary text area (right, 60%) is `position: sticky; top: 0; height: 100vh` so it stays pinned while cards scroll past.

### Mobile (<768px)

Stacks vertically: primary text on top (sticky, auto-height), cards below.

## Key Mechanisms

### 1. ScrollTrigger Activation

Each step card gets a GSAP ScrollTrigger:

```
trigger: card element
start: 'top 55%'    ← card's top reaches 55% down the viewport
end: 'bottom 40%'   ← card's bottom reaches 40% down the viewport
```

When a card enters this zone, `activateStep()` fires. When it leaves, `deactivateStep()` fires.

**Exclusive activation**: When a card activates, all other active cards in the same section are deactivated first. This prevents highlight conflicts when trigger zones briefly overlap.

### 2. Word Highlighting (text-effects.js)

**Wrapping phase** (`wrapWords`): When a verse is first rendered, each word group defined in the data's `words` map is found in the rendered HTML using regex, and wrapped in `<span class="word-group" data-word="groupId">`. The regex uses flexible whitespace matching to handle maqaf, zero-width spaces, and normal spaces in Hebrew text.

**Highlight phase** (`highlight`): When a step with a `highlight` array activates:
1. All `.word-group` spans get class `dimmed` (muted color)
2. Spans matching the highlight IDs get class `highlighted` (accent color + background)
3. The verse container gets class `has-highlights` (dims un-wrapped text)

**Reset phase** (`reset`): When a step with no highlights activates, all dimming and highlighting is removed, showing the verse at full opacity.

**Effects**: Steps can specify `"effect": "glow"` or `"effect": "pulse"` for stronger visual emphasis.

### 3. Verse Crossfade (text-effects.js)

All verses for a section (primary + any from `verse-change` steps) are pre-built in the DOM at startup, positioned absolutely, with only the active one visible (`opacity: 1`).

When `crossfadeTo()` is called:
1. Current verse gets `active` removed, `fading-out` added (animates opacity to 0)
2. New verse gets `active` added (animates opacity to 1)
3. CSS transitions handle the animation (0.6s)

The engine determines which verse to show by searching backwards from the current step through the section's steps array for the most recent `verse-change`.

### 4. Comparison Mode

When a verse has `"mode": "comparison"`, it renders as two side-by-side panels with a "vs." divider. The right panel's highlights use a second color (blue vs. the default brown) via CSS `:nth-child(3)` targeting.

Word groups in comparison mode can include `"side": "left"` or `"right"` to restrict matching to one panel.

### 5. Source Color System

Commentary cards display a source badge whose color is determined by CSS attribute selectors on `data-source`. The mapping is in CSS, not JS:

```css
.source-label[data-source="Rashi"] { color: var(--color-rashi); }
```

To add a new source, add a CSS rule. No JS changes needed.

## CSS Architecture

### Design Tokens

All colors, fonts, and easing are CSS custom properties on `:root`. Key groups:

- **`--color-bg-*`**: Background colors (cream, warm, card white)
- **`--color-text-*`**: Text hierarchy (primary, secondary, muted, dimmed)
- **`--color-accent`**: Primary accent (warm brown #8b5e3c)
- **`--color-highlight-*`**: First highlight color (brown) and second (blue, for comparisons)
- **`--color-{source}-*`**: Per-commentator colors (rashi, ramban, ibn-ezra, midrash)
- **`--font-*`**: Hebrew (Frank Ruhl Libre), English (Crimson Text), UI (Inter)

### Responsive Breakpoint

Single breakpoint at 768px. Below it:
- Layout stacks vertically (flex-direction: column)
- Primary text area switches from sticky-right to sticky-top
- Font sizes scale down (18px base to 16px)
- Comparison mode stacks, "vs." divider hidden

### Reduced Motion

`prefers-reduced-motion: reduce` kills all animations and transitions.

## Data Loading

The engine loads `data/{name}.json` where `{name}` comes from the `?sheet=` query parameter (default: `noah-5712`). This means:

- `localhost:8080/` loads `data/noah-5712.json`
- `localhost:8080/?sheet=vayera-5715` loads `data/vayera-5715.json`
- If the file doesn't exist, an error message is shown in the main content area

No server-side logic. The static file server just needs to serve the `data/` directory.

## Dependencies

| Library | Version | Source | Purpose |
|---------|---------|--------|---------|
| GSAP | 3.12.5 | CDN (cdnjs) | Animation engine |
| ScrollTrigger | 3.12.5 | CDN (cdnjs) | Scroll-driven triggers (GSAP plugin) |
| Frank Ruhl Libre | - | Google Fonts | Hebrew serif typeface |
| Crimson Text | - | Google Fonts | English serif typeface |
| Inter | - | Google Fonts | UI/label typeface |

No npm, no build step, no bundler. All dependencies loaded from CDN.

## Known Constraints

- **GSAP license**: Free for non-commercial use. Commercial use requires a GSAP license.
- **Static hosting**: Requires a web server (even `python -m http.server`) because of `fetch()`. Won't work from `file://`.
- **Hebrew word matching**: The regex-based phrase matching is fragile with nikkud variations. The Hebrew text in the data file must exactly match what's rendered, including cantillation marks if present.
- **No RTL page direction**: The page is LTR. Hebrew text blocks use `direction: rtl` per-element. This works well for the current layout but may need revisiting for a fully RTL interface.
- **Single-page**: Each JSON file produces one scrollytelling page. There's no index or navigation between different sheets.
