# Quality & error checking

Thoroughness is part of fidelity: a sheet with a silently-broken highlight or an
overflowing panel misrepresents the material. This file is the discipline that catches
those, plus the specific engine traps this format has already fallen into. Treat the
checklist as mandatory, not optional.

The mechanical rules (Hebrew cantillation cleaning, word-group constraints, source-color
tokens, comparison-vs-inline) live in
[../../close-read-sheet/references/hard-rules.md](../../close-read-sheet/references/hard-rules.md).
Read that too. This file adds the Nechama-flow-specific checks and the gotchas.

---

## The validation script (run before every browser check)

Extends the basic word-group check with **overlap detection** — two word-group phrases
where one contains the other cause a silent wrap failure (the inner one never renders).

```python
import json, re

d = json.load(open('data/<parsha>.json'))
problems = 0

def check(verse, label):
    global problems
    he, en = verse.get('he',''), verse.get('en','')
    items = list(verse.get('words', {}).items())
    for key, w in items:
        # existence: HE phrase present (tolerant of spaces/maqaf)
        pat = re.escape(w['he']).replace(r'\ ', r'[\s​]+').replace(r'\-', r'[\s־\-]')
        if not re.search(pat, he):
            print(f'  MISSING HE {label}: {key} = {w["he"]!r}'); problems += 1
        # EN must appear exactly once (else the global wrap hits the wrong spot)
        n = en.count(w['en'])
        if n == 0:   print(f'  MISSING EN {label}: {key} = {w["en"]!r}'); problems += 1
        elif n > 1:  print(f'  AMBIGUOUS EN {label}: {key} ({n}x) = {w["en"]!r}'); problems += 1
    # overlap: no phrase may contain another (same verse)
    for i,(k1,w1) in enumerate(items):
        for k2,w2 in items[i+1:]:
            if w1['he']!=w2['he'] and (w1['he'] in w2['he'] or w2['he'] in w1['he']):
                print(f'  HE OVERLAP {label}: {k1} vs {k2}'); problems += 1
            if w1['en']!=w2['en'] and (w1['en'] in w2['en'] or w2['en'] in w1['en']):
                print(f'  EN OVERLAP {label}: {k1} vs {k2}'); problems += 1

for s in d['sections']:
    if 'primaryText' in s:
        check(s['primaryText'], s['id'])
print(f'problems: {problems}')
```

Must print `problems: 0`. A real example caught this way: `yissa` =
"May the Lord lift up His face upon you and grant you peace" fully contained `shalom` =
"and grant you peace" — so highlighting `shalom` silently did nothing. Fix by trimming
the longer phrase so they don't overlap.

---

## Browser verification checklist

Start the preview, load `?sheet=<parsha>`, and confirm each — these all correspond to
bugs that have actually shipped in this format:

1. **All leaves reachable.** Click each root-fork branch, then each theme-fork branch;
   confirm the leaf's section becomes visible and the URL path updates
   (`?path=<theme>/<year>`). Deep-link a path directly and confirm it lands.
2. **Highlights fire on the RIGHT panel.** Scroll a card with a `highlight` into view.
   Confirm the lit phrase is in *this section's* pinned panel and that the un-highlighted
   text in *this* panel dims. (See the multi-panel gotcha below — this broke once.)
3. **Ref label clears the breadcrumb.** The `NUMBERS x:y` label at the top of the pinned
   panel must not be covered by the fixed breadcrumb pill.
4. **No vertical overflow.** The Hebrew + English caption must fit the panel without
   clipping the last line. (See fit-to-panel below.)
5. **No `undefined` in the DOM**, no errors in `preview_console_logs` filtered to `error`.
6. **Highlight coverage sanity.** Spot-check that question cards `pulse` and that the
   theme-intro "look at the whole structure" cards light up the verses they describe.

---

## Engine gotchas (each one cost real debugging time)

### Many `.primary-text-content.active` elements at once
A sheet with N sections has **N** panels, each with its own `.primary-text-content` that
carries `.active` (it just means "the visible content in this section"). A 13-leaf sheet
has ~18 of them simultaneously. So **never use `document.querySelector('.primary-text-
content.active')`** to find "the" active panel — it returns the first in DOM order (the
overview's), not the one the reader is on. `TextEffects.highlight()`/`reset()` take a
`sectionEl` parameter and scope to it; `activateStep`/`deactivateStep` pass it through. If
highlights "don't show up" in a leaf, this scoping is the first suspect.

### CSS clamp can't measure content height → fit-to-panel
`font-size: clamp(…, cqi, …)` scales the Hebrew to the panel *width*, but a long passage
still overflows the panel *height* — CSS has no "shrink to fit available height." The
engine's `TextEffects.fitToPanel()` measures content vs. the panel's padded area and
shrinks the font until it fits (with floors). It runs after init, on path change (newly
revealed leaves), and on debounced resize. Two sub-traps:
- **It bails on hidden panels** (`clientHeight === 0`) — a leaf hidden behind an
  un-chosen fork has no measurable height; fit it when it becomes visible, via the
  `applyVisibility` hook, not at init.
- **Schedule with `setTimeout`, not `requestAnimationFrame`.** rAF callbacks don't fire
  in background/inactive tabs, so a panel measured via rAF can stay full-size. The
  symptom: "it resizes when I switch to the tab but not on first load."

The *first* defense against height overflow is still trimming `primaryText` to the
verses the leaves use (see voice-and-fidelity.md) — fit-to-panel is the safety net, not
the primary tool.

### `container-type: size` breaks the sticky panel
The panel needs `container-type: inline-size` (for `cqi` width units), **not** `size`.
Full size-containment zeroes out the sticky `height: 100vh` and the panel collapses to
nothing. For height-awareness use a `vh` term inside the font `clamp()`, not `cqb`.

### `align-items: center` + tall content pushes the ref label off-screen
When content exceeds the panel's padded area, plain `center` distributes overflow equally
above and below — sliding the ref label up under the breadcrumb. Use `align-items: safe
center` (falls back to top-align on overflow) and keep `padding-top` ≥ 4.5rem to clear
the breadcrumb.

### Local-dev caching
`python3 -m http.server` sends no `Cache-Control` headers, so the browser holds stale
JS/CSS/HTML. Symptom: "I fixed it but still see the bug." Defenses, all in place:
- No-cache `<meta>` tags in `index.html`.
- Asset `?v=` query strings bumped to an epoch timestamp on **every** CSS/JS edit
  (`sed -i '' -E "s|close-read.css\?v=[0-9]+|close-read.css?v=$(date +%s)|" index.html`).
- When verifying, hard-reload (`Cmd+Shift+R`) or load `/index.html?bust=<ts>&sheet=…` so
  even a cached index.html is bypassed once.

---

## Definition of done

- Validation script prints `problems: 0`.
- All leaves reachable; deep-links work; back/forward works.
- Highlights fire on the correct panel and dim the rest of *that* panel.
- No panel overflows; ref labels clear the breadcrumb; no console errors.
- Every commentary card's text matches the Sefaria source it cites; every attribution is
  era/school-correct.
- The research pack accounts for every leaf and every cited source.
- Committed with a semantic message; assets cache-busted.
