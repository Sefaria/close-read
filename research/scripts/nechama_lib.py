"""Stage 4 — shared library for the Nechama parsha Close Read builds (Bereshit, Noach, …).

A parsha's own lib (bereshit_lib.py, noach_lib.py) does `from nechama_lib import *` and then
`use('<parsha>')`, which points harvest() at research/parshiyot/<parsha>-harvest/ and the verse
helpers at <parsha>-verses.json. Import one parsha's lib per process.

The rule this script exists to enforce: **her Hebrew is never typed here.** Every
commentary and question card quotes a harvest item (<parsha>-harvest/<theme>/<year>.json),
cut with `cut()`, which slices verbatim between start/stop phrases and fails if a phrase is
absent. Each such card carries `cite` (sheet, item, harvest file) and `en_basis`
("sefaria" = Sefaria's translation of the whole item; "nataf" = R. Francis Nataf's published
English of her own words, in the bilingual editions; "ours" = our translation).
tests/test_provenance.py re-checks every cited card against the harvest.

English: en_basis "sefaria" is safe only when her Hebrew *is* the full canonical source text,
because Sefaria's English translates the canonical ref, not her quotation. An abridged quote
(e.g. 1963's Rashi on 2:2, whose Sefaria English opens "R. Simeon says…", a phrase she didn't
quote) gets our own translation.

What *is* authored here: English translations marked en_basis "ours", and narration.
Narration is about the content (the verse, the page), never about her sheet: no "her
sheet…", "her next section…", "she adds…" (Lev, 2026-10-06: "we're taking her thinking
from one form into another"). Where a source or question sits on her sheet, what was
omitted and why, belongs in the research pack, not on screen. Narration also never states
her question for her.
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..'))
PACK = os.path.join(REPO, 'research', 'parshiyot')
VERSES = {}
PARSHA = None


def use(parsha):
    """Point the helpers at one parsha's harvest and verse cache."""
    global PARSHA
    PARSHA = parsha
    VERSES.clear()
    VERSES.update(json.load(open(os.path.join(PACK, f'{parsha}-verses.json')))['verses'])


# ─── harvest access ─────────────────────────────────────────────────────────

def harvest(theme, year):
    assert PARSHA, 'call use(<parsha>) first'
    path = os.path.join(PACK, f'{PARSHA}-harvest', theme, f'{year}.json')
    return json.load(open(path)), os.path.relpath(path, REPO)


def item(h, i):
    """A publishable harvest item by raw index (or 'after N' for a scan-only insertion)."""
    data, path = h
    for sec in data['sections']:
        for k, it in enumerate(sec['items']):
            if it.get('i', None) == i:
                bad = it.get('exclude') or it.get('publish') is False or it.get('triage', {}).get('use') == 'open'
                assert not bad, f'{path} [{i}] is not publishable: {it.get("exclude") or it.get("triage")}'
                assert not re.search(r'\[[^\]\[]{0,4}\]|\[\[', it['he']), \
                    f'{path} [{i}] carries checker markup; slice around it or fix the harvest'
                return it, {'sheet': data['sheet_id'], 'i': i, 'harvest': path}
    raise KeyError(f'{path}: no item {i}')


def flat(t):
    return re.sub(r'\s+', ' ', t).strip()


def cut(it, start=None, stop=None):
    """Verbatim slice of a harvest item's Hebrew, from `start` through `stop` (inclusive)."""
    he = flat(it['he'])
    a = 0 if start is None else he.find(start)
    assert a >= 0, f'start phrase not in item: {start!r}'
    if stop is None:
        b = len(he)
    else:
        b = he.find(stop, a)
        assert b >= 0, f'stop phrase not in item: {stop!r}'
        b += len(stop)
    return he[a:b].strip()


def underline(he, span):
    assert span in he, f'underline span not in text: {span!r}'
    return he.replace(span, f'<u>{span}</u>', 1)


# ─── card builders ──────────────────────────────────────────────────────────

def narration(id, en, highlight=None, effect=None):
    s = {'id': id, 'type': 'narration', 'text': {'en': en}}
    if highlight:
        s['highlight'] = highlight
    if effect:
        s['effect'] = effect
    return s


def commentary(id, h, i, source, label_he, label_en, en, en_basis, he=None, ref=None,
               highlight=None, effect=None, start=None, stop=None, he_dir=None):
    it, cite = item(h, i)
    s = {'id': id, 'type': 'commentary', 'source': source,
         'sourceLabel': {'he': label_he, 'en': label_en},
         'text': {'he': he if he is not None else cut(it, start, stop), 'en': en},
         'cite': cite, 'en_basis': en_basis}
    if ref:
        s['ref'] = ref
    if highlight:
        s['highlight'] = highlight
    if effect:
        s['effect'] = effect
    if he_dir:
        s['heDir'] = he_dir   # 'ltr' for a source quoted in German/English
    return s


def question(id, h, i, en, start=None, stop=None, highlight=None, effect='pulse', en_basis='ours'):
    """en=None with en_basis 'nataf' uses Nataf's published English of the whole item."""
    it, cite = item(h, i)
    if en_basis == 'nataf':
        assert start is None and stop is None, 'Nataf translated the whole item; quote it whole'
        en = it['en_nataf'] if en is None else en
    s = {'id': id, 'type': 'question', 'text': {'he': cut(it, start, stop), 'en': en},
         'cite': cite, 'en_basis': en_basis}
    if highlight:
        s['highlight'] = highlight
        s['effect'] = effect
    return s


def verse_range(a, b):
    """Hebrew/English for chapter:verse a..b inclusive, from the verse cache."""
    keys = list(VERSES)
    seg = keys[keys.index(a):keys.index(b) + 1]
    return ' '.join(VERSES[k]['he'] for k in seg), ' '.join(VERSES[k]['en'] for k in seg)


# ─── shared panels ──────────────────────────────────────────────────────────

POINTS = re.compile(r'[\u0591-\u05C7]')


def vp(he, letters):
    """The pointed phrase in `he` whose bare letters are `letters` (verse Hebrew is never typed)."""
    bare, idx = [], []
    for k, c in enumerate(he):
        if not POINTS.match(c):
            bare.append(c)
            idx.append(k)
    a = ''.join(bare).find(letters)
    assert a >= 0, f'{letters!r} not in verse'
    end = idx[a + len(letters) - 1] + 1
    while end < len(he) and POINTS.match(he[end]):
        end += 1
    return he[idx[a]:end]


def words(he, en, spec):
    """spec: id → (bare Hebrew letters, English phrase); both must be found in the verse."""
    out = {}
    for wid, (letters, en_phrase) in spec.items():
        assert en_phrase in en, f'{en_phrase!r} not in English'
        out[wid] = {'he': vp(he, letters), 'en': en_phrase}
    return out


def verse_set(keys):
    """Hebrew/English for a list of verses ('2:4', '2:6'); non-adjacent ones are joined with ' … '."""
    allk = list(VERSES)
    he, en, prev = [], [], None
    for k in keys:
        if prev is not None and allk.index(k) != allk.index(prev) + 1:
            he.append('…'); en.append('…')
        he.append(VERSES[k]['he']); en.append(VERSES[k]['en'])
        prev = k
    return ' '.join(he), ' '.join(en)


def primary(ref, keys, spec):
    """A primaryText for verses `keys` with word groups `spec` (id → (bare letters, English))."""
    he, en = verse_set(keys)
    return {'ref': ref, 'he': he, 'en': en, 'words': words(he, en, spec)}
