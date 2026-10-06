"""Stage 3 — fetch and clean the verse texts for a parsha span, once, with provenance.

Writes research/parshiyot/<parsha>-verses.json: {"meta": {...}, "verses": {"1:1": {"he", "en"}}}.
Hebrew: "Miqra according to the Masorah" (MAM), cantillation stripped, maqaf → space,
{פ}/{ס} markers kept separately as `break` (the Masoretic paragraph break after the verse).
English: Sefaria's default English version, HTML and footnotes stripped. Any footnote that
leaks as inline text (e.g. "ceasingaceasing Or 'resting.'") is reported for a manual check.

Usage: python3 research/scripts/fetch_verses.py <parsha> <Book> <span>
   e.g. python3 research/scripts/fetch_verses.py bereshit Genesis 1:31,2:25,3:24,4:26,5:32,6:8
"""
import datetime, json, os, re, sys, urllib.parse, urllib.request

parsha, book = sys.argv[1], sys.argv[2]
span = {int(c): int(n) for c, n in (x.split(':') for x in sys.argv[3].split(','))}
UA = {'User-Agent': 'Sefaria/close-read'}
CANT = re.compile(r'[֑-ֽ֯׀׃׆]')


def get(ref, version):
    q = urllib.parse.urlencode({'version': version})
    url = f'https://www.sefaria.org/api/v3/texts/{urllib.parse.quote(ref)}?{q}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        v = json.load(r)['versions'][0]
    return v['versionTitle'], v['text']


def clean_he(s):
    brk = 'פ' if '{פ}' in s else 'ס' if '{ס}' in s else None
    s = strip_footnotes(s)   # MAM carries variant notes as footnotes (4:13, 5:1)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{[פס]\}', '', s).replace('&nbsp;', ' ').replace('&thinsp;', ' ')
    s = CANT.sub('', s).replace('־', ' ')
    return re.sub(r'\s+', ' ', s).strip(), brk


def strip_footnotes(s):
    """Drop <sup class="footnote-marker">…</sup> and <i class="footnote">…</i>, where the
    footnote can itself contain <i>…</i> (so a non-greedy regex stops too early)."""
    s = re.sub(r'<sup[^>]*class="footnote-marker"[^>]*>.*?</sup>', '', s)
    out, i = [], 0
    for m in re.finditer(r'<i[^>]*class="footnote"[^>]*>', s):
        if m.start() < i:
            continue
        out.append(s[i:m.start()])
        depth, j = 1, m.end()
        for t in re.finditer(r'<i\b[^>]*>|</i>', s[j:]):
            depth += 1 if t.group().startswith('<i') else -1
            if depth == 0:
                i = j + t.end()
                break
        else:
            i = len(s)
    out.append(s[i:])
    return ''.join(out)


# The JPS gender-sensitive edition writes the divine name in small caps
# (G<small>OD</small>, E<small>TERNAL</small>). Close Read sheets use "the Lord"
# (the Nasso convention), recorded in meta.substitutions.
NAME_SUBS = [
    (r'\bthe ETERNAL God\b', 'the Lord God'), (r'\bThe ETERNAL God\b', 'The Lord God'),
    (r'\bthe ETERNAL\b', 'the Lord'), (r'\bThe ETERNAL\b', 'The Lord'),
    (r'\bGOD\b', 'the Lord'),
]


def clean_en(s):
    s = strip_footnotes(s)
    s = re.sub(r'([A-Z])<small>([A-Z]+)</small>', lambda m: m[1] + m[2], s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    for pat, rep in NAME_SUBS:
        s = re.sub(pat, rep, s)
    s = re.sub(r'(^|[.“?!]\s*)the Lord', lambda m: m[1] + 'The Lord', s)
    s = re.sub(r'\bto the the Lord\b', 'to the Lord', s)
    return re.sub(r'\s+', ' ', s).strip()


verses, suspects, versions = {}, [], {}
for ch, last in span.items():
    ref = f'{book} {ch}:1-{last}'
    vt_he, he = get(ref, 'hebrew|Miqra according to the Masorah')
    vt_en, en = get(ref, 'english')
    versions = {'he': vt_he, 'en': vt_en}
    for i, (h, e) in enumerate(zip(he, en), 1):
        h_clean, brk = clean_he(h)
        e_clean = clean_en(e)
        verses[f'{ch}:{i}'] = {'he': h_clean, 'en': e_clean, **({'break': brk} if brk else {})}
        if re.search(r'\b(\w{3,})[a-z]\1\b|\bOr “|\bLit\. |\bHeb\. |[a-z]\.[A-Za-z]', e_clean) or '<' in e_clean:
            suspects.append(f'{ch}:{i}')

out = os.path.join(os.path.dirname(__file__), '..', 'parshiyot', f'{parsha}-verses.json')
json.dump({'meta': {'book': book, 'span': span, 'versions': versions,
                    'fetched_at': datetime.datetime.now().isoformat(timespec='seconds'),
                    'footnote_suspects': suspects,
                    'substitutions': [f'{p} → {r}' for p, r in NAME_SUBS]},
           'verses': verses}, open(out, 'w'), ensure_ascii=False, indent=1)
print(f'{len(verses)} verses → {os.path.normpath(out)}; versions {versions}; footnote suspects: {suspects}')
