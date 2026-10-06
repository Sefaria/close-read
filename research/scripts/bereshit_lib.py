"""Stage 4 — shared library for the Bereshit Close Read build.

The rule this script exists to enforce: **her Hebrew is never typed here.** Every
commentary and question card quotes a harvest item (bereshit-harvest/<theme>/<year>.json),
cut with `cut()`, which slices verbatim between start/stop phrases and fails if a phrase is
absent. Each such card carries `cite` (sheet, item, harvest file) and `en_basis`
("sefaria" = Sefaria's translation of the whole item; "ours" = our translation).
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

Output (for now): data/bereshit-chapter-break.json, the 1963 leaf on its own, for review.
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..'))
PACK = os.path.join(REPO, 'research', 'parshiyot')
VERSES = json.load(open(os.path.join(PACK, 'bereshit-verses.json')))['verses']


# ─── harvest access ─────────────────────────────────────────────────────────

def harvest(theme, year):
    path = os.path.join(PACK, 'bereshit-harvest', theme, f'{year}.json')
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


def question(id, h, i, en, start=None, stop=None, highlight=None, effect='pulse'):
    it, cite = item(h, i)
    s = {'id': id, 'type': 'question', 'text': {'he': cut(it, start, stop), 'en': en},
         'cite': cite, 'en_basis': 'ours'}
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

LENINGRAD_CREDIT = {
    'en': 'Leningrad Codex (1008 CE). Bruce Zuckerman, West Semitic Research, in collaboration '
          'with the Ancient Biblical Manuscript Center; courtesy Russian National Library, Saltykov-Schedrin',
    'url': 'https://dornsife.usc.edu/wsrp/biblical-manuscripts'}

# Regions: measured on the full-resolution JPEGs; derivation in bereshit.md §5b.
FOLIO_1V = {
    'ref': 'Leningrad Codex, folio 1v', 'mode': 'image',
    'src': 'https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F001B.jpg',
    'link': 'https://www.sefaria.org/Genesis.1.1?with=Manuscripts',
    'width': 3683, 'height': 4224,
    'alt': 'Folio 1v of the Leningrad Codex: Genesis 1:1–26 in three columns of Hebrew script, with Masoretic notes in the margins.',
    'caption': {'en': 'Genesis 1:1–26. Columns read right to left.'},
    'credit': LENINGRAD_CREDIT,
    'regions': {
        'day-1': {'x': 0.61, 'y': 0.452, 'w': 0.2, 'h': 0.026},
        'day-2': {'x': 0.61, 'y': 0.672, 'w': 0.2, 'h': 0.026},
        'day-3': {'x': 0.34, 'y': 0.426, 'w': 0.21, 'h': 0.05},
        'day-4': {'x': 0.08, 'y': 0.252, 'w': 0.2, 'h': 0.048},
        'day-5': {'x': 0.08, 'y': 0.56, 'w': 0.2, 'h': 0.028},
    },
}
FOLIO_2R = {
    'ref': 'Leningrad Codex, folio 2r', 'mode': 'image',
    'src': 'https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F002A.jpg',
    'link': 'https://www.sefaria.org/Genesis.2.1?with=Manuscripts',
    'width': 3958, 'height': 4248,
    'alt': 'Folio 2r of the Leningrad Codex: Genesis 1:26–2:19 in three columns of Hebrew script, with Masoretic notes in the margins.',
    'caption': {'en': 'Genesis 1:26–2:19. Columns read right to left.'},
    'credit': LENINGRAD_CREDIT,
    'regions': {
        'day-6': {'x': 0.625, 'y': 0.664, 'w': 0.195, 'h': 0.026},
        'vayechulu-a': {'x': 0.625, 'y': 0.688, 'w': 0.195, 'h': 0.07},
        'vayechulu-b': {'x': 0.37, 'y': 0.158, 'w': 0.2, 'h': 0.142},
    },
}


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


def gen_1_31_2_3():
    he, en = verse_range('1:31', '2:3')
    return {'ref': 'Genesis 1:31-2:3', 'he': he, 'en': en, 'words': words(he, en, {
        'tov-meod': ('והנה טוב מאד', 'found it very good'),
        'yom-hashishi': ('יום הששי', 'the sixth day'),
        'vayechulu': ('ויכלו השמים והארץ וכל צבאם', 'The heaven and the earth were finished, and all their array'),
        'vaychal': ('ויכל אלהים ביום השביעי מלאכתו', 'On the seventh day God finished the work'),
        'vayishbot': ('וישבת ביום השביעי', 'ceasing on the seventh day'),
    })}



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
