"""Stage 1b — mechanical survey of a parsha's raw gilyonot.

Reads research/parshiyot/<parsha>-raw/*.json (written by snapshot_parsha.py) and
writes research/parshiyot/<parsha>-survey.json plus a generated markdown inventory
research/parshiyot/<parsha>-survey.md.

Everything in the output is *extracted*, never summarized: each section header, ref,
embedded quotation label and question carries `i`, its index into the sheet's
`sources[]`, so any line can be checked against the raw file (and from there against
the original PDF linked in the sheet's summary).

What counts as what (heuristics, kept deliberately literal):
- section header: an outsideText whose HTML has <big>…</big> and whose stripped text
  starts with a Hebrew letter + "."  (her own א./ב./ג. numbering)
- ref source: a sources[] item with `ref` — Sefaria's link layer. The ref label can
  be wrong; `text.he` is her (often abridged) quotation.
- embedded quotation: an outsideText containing a grey (#999 / rgb 153) label — the
  digitizers' convention for a source she quoted that Sefaria couldn't link
  (Cassuto, Hirsch, Benno Jacob, Biur, …). Label text recorded verbatim. This is a
  LOWER BOUND: many typed-in quotations carry no grey label (see quote-like prose).
- question/task: an outsideText whose text has "?" or "!", starts with a number
  ("1." / "א)") or with one of her task verbs (הסבר, השווה, באר, ענה, נסה, הוכח, …).
  Her tasks are often imperatives with no "?" at all ("ענה לשאלתם!").
- quote-like prose: an outsideText that opens with a short "Name:" label (e.g.
  "ר' נפתלי הרץ ויזל, (רנה\"ו):") — usually a source she typed in herself.
- everything else is "prose". EVERY outsideText item is listed in the .md with a
  verbatim snippet, whatever its kind, so nothing on the sheet is hidden by a heuristic.
- cross-link: any `sheet.<id>` data-ref in an outsideText (e.g. "this sheet continues…").

Also emitted, so that every survey claim is reproducible:
- a summary table (one row per sheet) at the top of the .md;
- a coverage block: verses of the parsha's span touched by NO linked ref in any sheet,
  counting both `ref` items and `data-ref` links inside her prose. Linked refs only — a
  verse discussed in unlinked prose still shows as uncovered, so this is an upper
  bound on absence;
- a hard check that each title's Hebrew year (gematria + 5000) == summary's Gregorian
  year + 3760. Exits non-zero on any mismatch.

Usage: python3 research/scripts/survey_parsha.py <parsha> <Book> <span>
   <span> = comma-separated chapter:last-verse pairs covering the parsha
   e.g. python3 research/scripts/survey_parsha.py bereshit Genesis 1:31,2:25,3:24,4:26,5:32,6:8
"""
import glob, html, json, os, re, sys

parsha, book = sys.argv[1], sys.argv[2]
span = {int(c): int(n) for c, n in (x.split(':') for x in sys.argv[3].split(','))}
base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'parshiyot'))
raw_dir = os.path.join(base, f'{parsha}-raw')

HEB = 'אבגדהוזחטיכלמנסעפצקרשת'
HEADER_RE = re.compile(r'^([' + HEB + r'])\.\s*(.*)')
GREY_RE = re.compile(r'color:\s*(?:rgb\(\s*153,\s*153,\s*153\s*\)|#999999?)[^>]*>((?:\s|<[^>]+>)*)([^<]{2,120})')
SHEETLINK_RE = re.compile(r'data-ref="sheet\.(\d+)"')
TASK_RE = re.compile(r'^(?:\(?\d+[.)]|[' + HEB + r']\)|הסבר|השוו?ה|באר|ענה|נסה|הוכח|מצא|עיין|העתק|פרש|תן|הבא|הראה|מה |מדוע|למה|האם|כיצד|היכן|במה|כמי)')
LABEL_RE = re.compile(r'^[^:\n?!]{2,60}:')
VERSE_RE = re.compile(rf'(?:^| on ){book} (\d+):(\d+)(?:-(\d+))?')


def strip(s):
    s = re.sub(r'<br\s*/?>', '\n', s or '')
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'[ \t‎‏]+', ' ', s).strip()


def outside_html(src):
    """Return (html, is_bilingual) for prose items; None for ref items."""
    if 'outsideText' in src:
        return src['outsideText'], False
    if 'outsideBiText' in src:
        return src['outsideBiText'].get('he', ''), True
    return None, False


def verses_of(ref):
    """Base-text verses a ref touches, e.g. 'Rashi on Genesis 3:7:3' -> ['3:7']."""
    m = VERSE_RE.search(ref)
    if not m:
        return []
    ch, v1, v2 = int(m[1]), int(m[2]), m[3]
    # For a commentary ref ("X on Genesis 3:7:3-8:1") the range is in comment
    # numbers, not verses — only take the anchor verse.
    if ' on ' in ref or v2 is None:
        return [f'{ch}:{v1}']
    return [f'{ch}:{v}' for v in range(v1, int(v2) + 1)]


GEMATRIA = dict(zip('אבגדהוזחטיכלמנסעפצקרשת',
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]))


def hebrew_year(s):
    """'תש"ב' -> 5702 (thousands implied)."""
    return 5000 + sum(GEMATRIA.get(ch, 0) for ch in s)


def parse_sheet(d):
    title = d['title']
    summary = strip(d.get('summary', ''))
    m_he = re.search(r'תש["״]?[א-ת]?["״]?[א-ת]', title)
    m_g = re.search(r'\b(19\d\d)\b', summary)
    pdf = re.search(r'nechama\.org\.il/pdf/(\d+)\.pdf', d.get('summary', ''))
    sub = title.split(' - ', 1)[1].strip() if ' - ' in title else None

    preface = {'refs': [], 'embedded': [], 'questions': [], 'prose': []}
    sections, cur = [], preface
    cross, verses, prose_verses = set(), set(), set()
    for i, src in enumerate(d.get('sources', [])):
        h, bi = outside_html(src)
        if h is None:
            ref = src.get('ref', '')
            cur['refs'].append({'i': i, 'ref': ref})
            verses.update(verses_of(ref))
            continue
        txt = strip(h)
        cross.update(int(x) for x in SHEETLINK_RE.findall(h))
        for r in re.findall(r'data-ref="([^"]+)"', h):
            prose_verses.update(verses_of(r))
        hm = HEADER_RE.match(txt)
        if '<big>' in h and hm:
            cur = {'i': i, 'letter': hm[1], 'label': txt,
                   'refs': [], 'embedded': [], 'questions': [], 'prose': []}
            sections.append(cur)
            continue
        for g in GREY_RE.finditer(h):
            label = strip(g[2]).rstrip(':').strip()
            if label:
                cur['embedded'].append({'i': i, 'label': label})
        if not txt:
            continue
        if '?' in txt or '!' in txt or TASK_RE.match(txt):
            cur['questions'].append({'i': i, 'he': txt})
        else:
            kind = 'quote-like' if LABEL_RE.match(txt) else 'prose'
            cur['prose'].append({'i': i, 'kind': kind, 'chars': len(txt), 'he': txt})

    flags = []
    if not sections:
        flags.append('NO_SECTION_HEADERS')
    if not any(s['questions'] for s in sections) and not preface['questions']:
        flags.append('NO_QUESTIONS_IN_DIGITIZATION')
    if any(k in src for src in d.get('sources', []) for k in ('outsideBiText',)):
        flags.append('BILINGUAL_EDITION')
    if not pdf:
        flags.append('NO_PDF_LINK')
    if not m_g:
        flags.append('NO_GREGORIAN_YEAR')

    return {
        'id': d['id'],
        'title': title,
        'sub_topic': sub,
        'year_he': m_he[0] if m_he else None,
        'year_g': int(m_g[1]) if m_g else None,
        'summary': summary,
        'sefaria_url': f"https://www.sefaria.org/sheets/{d['id']}",
        'pdf_url': f'http://www.nechama.org.il/pdf/{pdf[1]}.pdf' if pdf else None,
        'raw_file': f"{parsha}-raw/{d['id']}.json",
        'n_sources': len(d.get('sources', [])),
        'cross_links': sorted(cross),
        'verses': sorted(verses, key=lambda v: tuple(map(int, v.split(':')))),
        'prose_verses': sorted(prose_verses, key=lambda v: tuple(map(int, v.split(':')))),
        'flags': flags,
        'preface': preface,
        'sections': sections,
    }


sheets = [parse_sheet(json.load(open(f)))
          for f in glob.glob(os.path.join(raw_dir, '[0-9]*.json'))]
sheets.sort(key=lambda s: (s['year_g'] or 9999, s['id']))
# Year check: Hebrew year in title vs Gregorian year in summary
year_errors = [s for s in sheets if s['year_he'] is None or s['year_g'] is None
               or hebrew_year(s['year_he']) != s['year_g'] + 3760]
for s in sheets:
    s['year_check'] = 'ok' if s not in year_errors else 'MISMATCH'

# Coverage over the parsha span (linked refs only)
touched = {}
for s in sheets:
    for v in s['verses'] + s['prose_verses']:
        touched.setdefault(v, set()).add(s['id'])
uncovered = {c: [v for v in range(1, n + 1) if f'{c}:{v}' not in touched] for c, n in span.items()}
coverage = {'span': span, 'uncovered': uncovered,
            'touched_outside_span_or_in_span': {v: sorted(ids) for v, ids in sorted(touched.items())}}

json.dump({'sheets': sheets, 'coverage': coverage,
           'year_check': {'rule': 'gematria(title year)+5000 == summary Gregorian + 3760',
                          'mismatches': [s['id'] for s in year_errors]}},
          open(os.path.join(base, f'{parsha}-survey.json'), 'w'), ensure_ascii=False, indent=1)


# ---- generated markdown inventory -------------------------------------------
def snip(t, n):
    t = re.sub(r'\s+', ' ', t)
    return t[:n] + ('…' if len(t) > n else '')


def vrange(vs):
    """Compress ['1:1','1:2','1:3','2:4'] -> '1:1–3, 2:4'."""
    out, run = [], []
    for v in vs:
        c, n = map(int, v.split(':'))
        if run and run[-1][0] == c and run[-1][1] == n - 1:
            run.append((c, n))
        else:
            if run:
                out.append(run)
            run = [(c, n)]
    if run:
        out.append(run)
    return ', '.join(f'{r[0][0]}:{r[0][1]}' + (f'–{r[-1][1]}' if len(r) > 1 else '') for r in out)


L = [f'# {parsha} — generated survey inventory',
     '',
     f'> GENERATED by `research/scripts/survey_parsha.py` from `{parsha}-raw/`. Do not hand-edit;',
     '> re-run the script. `[i]` = index into that sheet\'s `sources[]` in the raw file.',
     '',
     '## Summary table',
     '',
     f'| Year | Sheet | PDF | Sub-topic (her title) | {book} verses (ref items) | Her sections (verbatim, digitized) | refs / Qs | Flags |',
     '|---|---|---|---|---|---|---|---|']
for s in sheets:
    nr = sum(len(x['refs']) for x in s['sections']) + len(s['preface']['refs'])
    nq = sum(len(x['questions']) for x in s['sections']) + len(s['preface']['questions'])
    secs = ' · '.join(x['label'].replace('|', '/') for x in s['sections']) or '*(none digitized)*'
    pdf = s['pdf_url'].replace('http://', 'https://') if s['pdf_url'] else None
    pdf_cell = f"[{pdf.rsplit('/', 1)[1]}]({pdf})" if pdf else '—'
    L.append(f"| **{s['year_he']} / {s['year_g']}** | [{s['id']}]({s['sefaria_url']}) | {pdf_cell} | {s['sub_topic']} "
             f"| {vrange(s['verses'])} | {secs} | {nr} / {nq} | {', '.join(s['flags'])} |")
L += ['',
      f"Year check (gematria(title year)+5000 == Gregorian+3760): "
      f"{'all ' + str(len(sheets)) + ' ok' if not year_errors else 'MISMATCH ' + str([s['id'] for s in year_errors])}",
      '',
      '## Coverage (linked refs only — upper bound on absence)',
      '']
for c, vs in uncovered.items():
    L.append(f"- {book} {c} (1–{span[c]}): uncovered {', '.join(map(str, vs)) if vs else '— none'}")
L.append('')
L.append('## Sheets')
L.append('')
for s in sheets:
    L.append(f"### {s['year_g']} ({s['year_he']}) — {s['sub_topic']}  ·  sheet {s['id']}")
    L.append('')
    L.append(f"- Title (verbatim): {s['title']}")
    L.append(f"- Sefaria: {s['sefaria_url']}  ·  Original PDF: {s['pdf_url'] or '—'}  ·  Raw: `{s['raw_file']}`")
    L.append(f"- {s['n_sources']} source items  ·  {book} verses touched by ref items: {vrange(s['verses']) or '—'}")
    if s['cross_links']:
        L.append(f"- Links to sheet(s): {', '.join(map(str, s['cross_links']))}")
    if s['flags']:
        L.append(f"- **Flags:** {', '.join(s['flags'])}")
    L.append('')
    blocks = ([('(before first header)', s['preface'])] if any(s['preface'][k] for k in ('refs', 'questions', 'prose')) else []) \
        + [(f"[{x['i']}] {x['label']}", x) for x in s['sections']]
    for label, b in blocks:
        L.append(f'- **{label}**')
        items = [(r['i'], f"ref: {r['ref']}") for r in b['refs']] \
            + [(q['i'], f"Q: {snip(q['he'], 220)}") for q in b['questions']] \
            + [(p['i'], f"{p['kind']} ({p['chars']} ch): {snip(p['he'], 110)}") for p in b['prose']]
        grey = {e['i']: e['label'] for e in b['embedded']}
        for i, line in sorted(items):
            tag = f"  ⟨grey label: {grey[i]}⟩" if i in grey else ''
            L.append(f"  - [{i}] {line}{tag}")
    L.append('')
open(os.path.join(base, f'{parsha}-survey.md'), 'w').write('\n'.join(L) + '\n')
print(f'{len(sheets)} sheets → {parsha}-survey.json, {parsha}-survey.md')
if year_errors:
    sys.exit(f'YEAR MISMATCH: {[s["id"] for s in year_errors]}')
