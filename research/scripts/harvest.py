"""Harvest the 13 chosen Nasso gilyonot into structured per-leaf data.

For each sheet, walk its `sources[]` and group by Hebrew-letter section header
(outsideText starting with א./ב./ג. etc). Within each section, collect:
  - section label
  - sources (with ref + Hebrew + English text) — the commentaries she chose
  - questions (outsideText blocks after sources — her actual numbered Qs)
  - prose (outsideText blocks not matching a question pattern — her framing)

Output one structured file per leaf into research/parshiyot/nasso-harvest/.
"""
import json, re, os
from pathlib import Path

CHOSEN = {
    'gezel': [
        ('1944', 'תש"ד', 161971),
        ('1953', 'תשי״ג', 161361),
        ('1968', 'תשכ״ח', 160477),
    ],
    'nazir': [
        ('1942', 'תש"ב', 161916),
        ('1946', 'תש"ו', 161571),
        ('1970', 'תש"ל', 160600),
    ],
    'birkat': [
        ('1951', 'תשי״א', 161630),
        ('1955', 'תשט״ו', 161282),
        ('1962', 'תשכ״ב', 160762),
    ],
    'nesi_im': [
        ('1957', 'תשי״ז', 161143),
        ('1960', 'תש״כ',  161925),
        ('1966', 'תשכ״ו', 161619),
        ('1969', 'תשכ״ט', 160757),
    ],
}

HEB_LETTERS = "אבגדהוזחטיכלמנסעפצקרשת"
SEC_RE  = re.compile(r'^([' + HEB_LETTERS + r'])[.׳״\'”]\s+(.+)')
QNUM_RE = re.compile(r'^\s*(\d+)\s*[.)]')

def strip_html(s):
    s = re.sub(r'<br\s*/?>', '\n', s or '')
    s = re.sub(r'<[^>]+>', '', s)
    return s.strip()

def harvest_sheet(sheet_id, year, year_he):
    sheet = json.load(open(f'/tmp/nechama/sheets/{sheet_id}.json'))
    sources = sheet.get('sources', [])

    sections = []   # [{label, prose, sources, questions, raw_count}]
    cur = None

    def push():
        nonlocal cur
        if cur is not None:
            sections.append(cur)
        cur = None

    for src in sources:
        if 'outsideText' in src:
            txt = strip_html(src['outsideText'])
            if not txt:
                continue
            # Is it a top-level section header? "א. דין קרן וחומש בשבועת שקר"
            mo = SEC_RE.match(txt)
            if mo and len(txt) < 100 and '\n' not in txt:
                # New section
                push()
                cur = {
                    'letter': mo.group(1),
                    'label': txt,
                    'prose': [],
                    'sources': [],
                    'questions': [],
                }
                continue
            # Otherwise: question or prose, attach to current section (or "intro")
            if cur is None:
                cur = {'letter': '_intro', 'label': '(opening)', 'prose': [], 'sources': [], 'questions': []}
            # Sub-letter question (א. ב. ג. nested)? or numbered question (1. 2.)?
            looks_like_question = (
                QNUM_RE.match(txt) or
                txt.startswith('הסבר') or txt.startswith('מה') or txt.startswith('למה') or
                txt.startswith('היכן') or txt.startswith('האם') or txt.startswith('מי') or
                '?' in txt or '!' in txt[-3:] or txt.endswith(':')
            )
            # Heuristic: short + question-like → question; otherwise prose
            if looks_like_question and len(txt) < 600:
                cur['questions'].append(txt)
            else:
                cur['prose'].append(txt)
        elif 'ref' in src:
            ref = src.get('ref')
            text = src.get('text') or {}
            he = strip_html((text.get('he') or '')).strip()
            en = strip_html((text.get('en') or '')).strip()
            entry = {'ref': ref, 'he': he, 'en': en}
            if cur is None:
                cur = {'letter': '_intro', 'label': '(opening)', 'prose': [], 'sources': [], 'questions': []}
            cur['sources'].append(entry)

    push()

    return {
        'sheet_id': sheet_id,
        'year_g': year,
        'year_he': year_he,
        'title': sheet.get('title'),
        'sefaria_url': f'https://www.sefaria.org/sheets/{sheet_id}',
        'sections': sections,
    }

ROOT = Path('/Users/levisrael/sefaria/close_read/research/parshiyot/nasso-harvest')
ROOT.mkdir(parents=True, exist_ok=True)

for theme, picks in CHOSEN.items():
    theme_dir = ROOT / theme
    theme_dir.mkdir(exist_ok=True)
    for year, year_he, sid in picks:
        result = harvest_sheet(sid, year, year_he)
        out = theme_dir / f'{year}.json'
        with open(out, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f'{theme}/{year}: {len(result["sections"])} sections, '
              f'{sum(len(s["sources"]) for s in result["sections"])} sources, '
              f'{sum(len(s["questions"]) for s in result["sections"])} questions')

print('\nDone harvesting.')
