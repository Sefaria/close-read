"""Every quoted card traces to the checked harvest: no Hebrew typed by hand.

Applies to cards carrying `cite` (written by research/scripts/build_bereshit.py), and
requires `cite` on every commentary and question card of a sheet that uses it at all.

For each cited card:
- the cited harvest item exists and is publishable (not excluded, not marked
  not-published, not an open triage item);
- the card's Hebrew (tags stripped, whitespace collapsed) is a verbatim slice of the item's;
- `en_basis` is "ours" or "sefaria"; a "sefaria" English must be the item's own English,
  and then the card must quote the whole item (Sefaria translated the whole, not a slice).
"""

import json
import re

import pytest

from sheetmodel import ROOT, load_sheet, sheet_slugs


def flat(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t or '')).strip()


def find_item(harvest, i):
    for sec in harvest['sections']:
        for it in sec['items']:
            if it.get('i') == i:
                return it
    return None


def cited_sheets():
    out = []
    for slug in sheet_slugs():
        steps = [st for s in load_sheet(slug)['sections'] for st in s.get('steps', [])]
        if any('cite' in st for st in steps):
            out.append(slug)
    return out


@pytest.mark.parametrize('slug', cited_sheets())
def test_quoted_cards_trace_to_harvest(slug):
    problems = []
    for sec in load_sheet(slug)['sections']:
        for st in sec.get('steps', []):
            where = f"{sec['id']}/{st['id']}"
            if st['type'] not in ('commentary', 'question'):
                continue
            cite = st.get('cite')
            if not cite:
                problems.append(f'{where}: {st["type"]} card without cite')
                continue
            harvest = json.loads((ROOT / cite['harvest']).read_text())
            if harvest['sheet_id'] != cite['sheet']:
                problems.append(f'{where}: cite sheet {cite["sheet"]} ≠ harvest {harvest["sheet_id"]}')
            it = find_item(harvest, cite['i'])
            if it is None:
                problems.append(f'{where}: no harvest item {cite["i"]} in {cite["harvest"]}')
                continue
            if it.get('exclude') or it.get('publish') is False or it.get('triage', {}).get('use') == 'open':
                problems.append(f'{where}: quotes an unpublishable item [{cite["i"]}]')
            he = flat(st['text'].get('he'))
            for lang in ('he', 'en'):
                leak = re.search(r'\[[,/?.]{1,4}\]|\[\[|\*\*|«|»', st['text'].get(lang) or '')
                if leak:
                    problems.append(f'{where}: checker markup {leak[0]!r} in displayed {lang}')
            if not he:
                problems.append(f'{where}: no Hebrew')
            elif he not in flat(it['he']):
                problems.append(f'{where}: Hebrew is not a verbatim slice of [{cite["i"]}]: «{he[:60]}…»')
            basis = st.get('en_basis')
            if basis not in ('ours', 'sefaria'):
                problems.append(f'{where}: en_basis must be "ours" or "sefaria", got {basis!r}')
            if basis == 'sefaria':
                if flat(st['text'].get('en')) != flat(it.get('en')):
                    problems.append(f'{where}: en_basis sefaria but the English is not the item\'s own')
                if he != flat(it['he']):
                    problems.append(f'{where}: en_basis sefaria must quote the whole item (Sefaria translated the whole)')
    if problems:
        pytest.fail(f'{len(problems)} provenance problems:\n  ' + '\n  '.join(problems), pytrace=False)


def test_a_cited_sheet_exists():
    """Guard: the provenance test above must actually be running on something."""
    assert cited_sheets(), 'no sheet carries cite; the provenance check is vacuous'
