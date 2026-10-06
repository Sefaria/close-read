"""Check one theme's leaves in isolation, with the real test functions (no data/ file needed).

    python3 research/scripts/check_leaves.py garden          # all leaves in the theme
    python3 research/scripts/check_leaves.py garden 1953     # one leaf

Builds the leaves into an in-memory linear sheet and runs tests/test_data.py and
tests/test_provenance.py against it: word groups wrap, highlights resolve, English phrases
are unique, first steps don't highlight, steps are well-formed, images are valid, and every
quoted card traces to the harvest. Exit code 0 = clean.
"""
import importlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path[:0] = [HERE, os.path.join(REPO, 'tests')]
import pytest  # noqa: E402
import sheetmodel, test_data, test_provenance  # noqa: E402

theme = sys.argv[1]
only = sys.argv[2] if len(sys.argv) > 2 else None
mod = importlib.import_module(f'bereshit_leaves.{theme}')
sections = []
for name in sorted(n for n in dir(mod) if n.startswith('leaf_')):
    if only and name != f'leaf_{only}':
        continue
    sections += getattr(mod, name)()
sheet = {'title': {'en': 'check', 'questionLabel': {'en': 'Nechama asks'}}, 'sections': sections}

for m in (sheetmodel, test_data, test_provenance):
    m.load_sheet = lambda slug: sheet
failures = 0
for fn in (test_data.test_word_groups_wrap_cleanly, test_data.test_english_phrases_occur_once,
           test_data.test_highlights_resolve_to_active_verse, test_data.test_first_step_lets_verse_breathe,
           test_data.test_steps_are_well_formed, test_data.test_images_are_well_formed,
           test_provenance.test_quoted_cards_trace_to_harvest):
    try:
        fn('check')
        print(f'ok    {fn.__name__}')
    except pytest.fail.Exception as e:
        failures += 1
        print(f'FAIL  {fn.__name__}\n{e}')
n = sum(len(s.get('steps', [])) for s in sections)
print(f'{theme}{" " + only if only else ""}: {len(sections)} sections, {n} steps, {failures} failing checks')
sys.exit(1 if failures else 0)
