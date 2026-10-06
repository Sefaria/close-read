"""Stage 3b — harvest the 15 chosen Bereshit gilyonot into per-leaf data.

Inputs (all in the repo, all cited in the output):
- research/parshiyot/bereshit-raw/<id>.json      Sefaria digitization (frozen, hash-verified)
- research/parshiyot/bereshit-scancheck/<id>-<year>.md
                                                  scan check: where the scan differs, its
                                                  wording wins; sources the digitization lost;
                                                  the scan's section headers
- research/parshiyot/bereshit-transcriptions/162000-1943.md
                                                  1943 Part 1 (verified by Lev), because its
                                                  digitization has no questions

Output: research/parshiyot/bereshit-harvest/<theme>/<year>.json, one per leaf. Every item
keeps its `i` (index into the raw sources[]) and a `basis`:
  "digitization"            no scan check flagged it
  "scan"                    the scan check recorded a different wording; `he` is the scan's,
                            `digitized_he` keeps the other
  "scan-only"               named in the scan, absent from the digitization
  "transcription"           1943 only
Items flagged `needs_human` are DIFF lines in her own words (questions, prose, headers) that
the scan check couldn't settle with confidence ([?] in the reading). They must not be quoted
until a person checks them.

Don't hand-edit the output; fix the inputs and re-run.
"""
import html, json, os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'parshiyot'))

# Theme → leaves (pack §7 / §7a). Sections as her letters in the digitization.
CHOSEN = {
    'creation': [('1943', 'תש"ג', 162000, ['א', 'ב', 'ג', 'ד']),
                 ('1954', 'תשי"ד', 161401, ['ב', 'ג', 'ד']),
                 ('1963', 'תשכ"ג', 160726, ['א', 'ג', 'ד', 'ה'])],
    'garden':   [('1952', 'תשי"ב', 161471, ['א', 'ב', 'ד', 'ו', 'ז', 'ח']),
                 ('1953', 'תשי"ג', 161223, ['ב', 'ג', 'ד', 'ו']),
                 ('1965', 'תשכ"ה', 160577, ['ג', 'ד', 'ו'])],
    'sin':      [('1944', 'תש"ד', 161941, ['_open', 'א', 'ב', 'ג', 'ד']),
                 ('1964', 'תשכ"ד', 160638, ['א', 'ג', 'ד']),
                 ('1968', 'תשכ"ח', 160442, ['ב', 'ד', 'ו'])],
    'cain':     [('1942', 'תש"ב', 161880, ['ב', 'ה', 'ז', 'ט']),
                 ('1956', 'תשט"ז', 161216, ['א', 'ב', 'ג']),
                 ('1958', 'תשי"ח', 161141, ['א', 'ב', 'ד'])],
    'flood':    [('1950', 'תש"י', 161438, ['א', 'ב', 'ג']),
                 ('1969', 'תשכ"ט', 160469, ['_open', 'א', 'ג', 'ד']),
                 ('1971', 'תשל"א', 162069, ['א', 'ב', 'ג'])],
}

HEB = 'אבגדהוזחטיכלמנסעפצקרשת'
HEADER_RE = re.compile(r'^([' + HEB + r'])\.\s*(.*)')


def strip(s):
    s = re.sub(r'<br\s*/?>', '\n', s or '')
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'[ \t‎‏]+', ' ', s).strip()


def raw_sections(sheet):
    """Group raw sources[] by her section letter; '_open' = before the first header."""
    secs, cur = {'_open': {'header': None, 'items': []}}, '_open'
    for i, src in enumerate(sheet['sources']):
        if 'ref' in src:
            t = src.get('text') or {}
            secs[cur]['items'].append({'i': i, 'kind': 'source', 'ref': src['ref'],
                                       'he': strip(t.get('he')), 'en': strip(t.get('en'))})
            continue
        h = src.get('outsideText') or (src.get('outsideBiText') or {}).get('he') or ''
        en = (src.get('outsideBiText') or {}).get('en')
        txt = strip(h)
        m = HEADER_RE.match(txt)
        if '<big>' in h and m:
            cur = m[1]
            secs[cur] = {'header': {'i': i, 'digitized': txt}, 'items': []}
            continue
        if txt:
            item = {'i': i, 'kind': 'text', 'he': txt}
            if en:
                item['en_nataf'] = strip(en)
            secs[cur]['items'].append(item)
    return secs


PAIR_RE = re.compile(r'«([^»]*)»\s*(?:/|→)\s*(?:scan:?\s*)?«([^»]*)»')


def clean_frag(t):
    return re.sub(r'\*\*|`', '', t).strip()


def parse_scancheck(path):
    """Read a scan-check file (format: bereshit-scancheck/README.md).

    - headers: the scan's section headers (first `…` or «…» on the "Scan header" line)
    - status:  per-item status from the tables
    - pairs:   per-item (digitized fragment, scan fragment) from every "- [i] …«A» / scan «B»"
               line in the file. A pair can be a whole item or just the differing words; a
               "…" inside both marks a gap.
    """
    if not os.path.exists(path):
        return None
    md = open(path).read()
    out = {'path': os.path.relpath(path, ROOT), 'pairs': {}, 'headers': {}, 'status': {},
           'additions': []}
    for sec in re.split(r'\n## ', md)[1:]:
        letter = sec.strip()[1:2] if sec.strip().startswith('§') else sec.strip()[:1]
        m = re.search(r'\*\*Scan header \(verbatim\):\*\*\s*(.+)', sec)
        if m:
            q = re.search(r'`([^`]+)`|«([^»]+)»', m[1])
            out['headers'][letter] = clean_frag(q[1] or q[2]) if q else clean_frag(m[1])
        for row in re.finditer(r'^\|\s*(\d+)\s*\|([^|]*)\|\s*([A-Z][A-Z-]+)[^|]*\|(.*)\|\s*$', sec, re.M):
            out['status'][int(row[1])] = {'status': row[3], 'note': row[4].strip()}
        block = re.search(r'### Digitizer additions.*?\n(.*?)(?=\n### |\n## |\Z)', sec, re.S)
        if block:
            out['additions'] += [f'§{letter}: ' + l[2:].strip() for l in block[1].splitlines() if l.startswith('- ')]
    for line in md.splitlines():
        m = re.match(r'^-\s*(?:§\S+\s*)?\[(\d+)\]', line)
        if not m:
            continue
        for a, b in PAIR_RE.findall(line):
            pair = (clean_frag(a), clean_frag(b))
            if pair[0] and pair[0] != pair[1] and pair not in out['pairs'].setdefault(int(m[1]), []):
                out['pairs'][int(m[1])].append(pair)
    return out


def norm(t):
    """Compare text ignoring nikkud and spacing (the digitizer's pointing isn't her text)."""
    t = re.sub(r'[\u0591-\u05C7]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def apply_pairs(he, pairs):
    """Apply (digitized → scan) fragments inside `he`. Returns (text, applied, unapplied, sics).

    "…" or "..." inside a fragment is a gap; the pieces are applied one by one. A piece whose
    scan reading is already in the text counts as applied (checkers often list the same fix
    twice, once whole and once as a fragment). `[[sic: …]]` notes are kept out of her text
    and returned separately.
    """
    applied, unapplied, sics = [], [], []
    split = lambda t: [x.strip() for x in re.split(r'…|\.\.\.', t)]
    for a, b in pairs:
        # "[[sic: X]]" = the scan shows X (her typo). Keep X in the text; note the sic. If X
        # already precedes the note ("רש"ע [[sic: רש"ע]]"), just drop the note.
        def unsic(m):
            sics.append(m[0])
            x = m[1].strip()
            return '' if b[:m.start()].rstrip().endswith(x) else ' ' + x
        b_clean = re.sub(r'\s*\[\[sic:?\s*([^\]]*)\]\]', unsic, b).strip()
        segs_a, segs_b = split(a), split(b_clean)
        if len(segs_a) != len(segs_b):
            segs_a, segs_b = [a], [b_clean]
        ok = True
        for x, y in zip(segs_a, segs_b):
            if not x or x == y or (y and norm(y) in norm(he)):
                continue
            if x in he:
                he = he.replace(x, y)
            elif norm(x) and norm(x) in norm(he):
                he = norm(he).replace(norm(x), y)
            else:
                ok = False
        (applied if ok else unapplied).append({'digitized': a, 'scan': b})
    return he, applied, unapplied, sics


ABBREV = [("פסוק", "פ'"), ("פסוק", "פס'"), ("עיין", "ע'"), ("עיין", "עי'"), ("עמוד", "עמ'"),
          ("עמוד", "ע'"), ("בראשית", "בר'"), ("בראשית רבה", "ב\"ר"), ("דברים", "דב'"),
          ("שמואל", "שמ'"), ("יתברך", "ית'"), ("פרשה", "פ'"), ("העבודה זרה", "הע\"ז"),
          ("זה מזה", "זמ\"ז"), ("כל אחת", "כ\"א"), ("בלשון", "בל'"), ("ספר", "ס'"),
          ("פסוק", "פס'"), ("עמוד", "עמ'"), ("ברוך הוא", "ב\"ה"), ("תהלים", "תהל'"),
          ("שנאמר", "שנ'"), ("שמות", "שמ'"), ("בנו", "ב.")]


def skeleton(t):
    """Letters only, without matres lectionis and with abbreviations expanded — two
    readings with the same skeleton differ only in spelling/punctuation."""
    t = norm(re.sub(r'\[\[[^\]]*\]\]', '', t)).replace('[?]', '')
    for full, ab in ABBREV:
        t = t.replace(ab, full)
    t = re.sub(r'[^\u05D0-\u05EA]', '', t)
    t = t.translate(str.maketrans('ךםןףץ', 'כמנפצ'))
    return re.sub('[יו]', '', t)


CITE_WORDS = {'פרשה', 'פרק', 'פסוק', 'פסוקים', 'עמוד', 'תרגום', 'מגרמנית', 'מאנגלית', 'שהובא',
              'בספרו', 'בספר', 'בפירושו', 'על', 'התורה', 'רבה', 'בראשית', 'שמות', 'ויקרא', 'במדבר',
              'דברים', 'ספר', 'הלכה', 'הלכות', 'פרקי', 'מסכת', 'דף', 'שם', 'ראה', 'עיין', 'מקטע',
              'אמונות', 'ודעות', 'בשם', 'כ', 'ב'}


def words(t):
    t = re.sub(r'\[\[sic:?\s*([^\]]*)\]\]', r' \1 ', t)      # the sic reading is what the scan shows
    t = norm(re.sub(r'\[\[[^\]]*\]\]', '', t)).replace('[?]', '')
    for full, ab in ABBREV:
        t = t.replace(ab, full)
    return [w for w in re.split(r'[^\u05D0-\u05EA"\'0-9]+', t) if w]


def is_numeral(w):
    return bool(re.fullmatch(r'[0-9]+|[\u05D0-\u05EA]{1,3}["\']?[\u05D0-\u05EA]?\'?', w)) and ('"' in w or "'" in w or w.isdigit())


def editorial(fix):
    """The digitizer *added* citation detail: every scan word appears, in order, in the
    digitized text, and everything extra is citation material (book/chapter/verse/page
    words, numerals, translator notes). A purposeful addition, not an error (Lev, 2026-10-06)."""
    # An added parenthesis is a citation gloss: "(שהובא בראב"ע)", "(תרגום מגרמנית)".
    added = [m for m in re.findall(r'\([^()]*\)', fix['digitized']) if norm(m) not in norm(fix['scan'])]
    if added and skeleton(re.sub(r'\([^()]*\)', lambda m: '' if m[0] in added else m[0], fix['digitized'])) == skeleton(fix['scan']):
        return True
    d, sc = words(fix['digitized']), words(fix['scan'])
    sk = lambda w: re.sub('[יו"\']', '', w)
    i, extra = 0, []
    for w in d:
        if i < len(sc) and sk(w) == sk(sc[i]):
            i += 1
        else:
            extra.append(w)
    return i == len(sc) and 0 < len(extra) <= 8 and all(
        is_numeral(w) or re.sub('^[בלמוה]', '', w) in CITE_WORDS or w in CITE_WORDS for w in extra)


def classify(fix):
    """editorial   — the digitizer added citation detail (keep theirs; not an error)
       spelling    — same words, her spelling/punctuation/abbreviation
       corroborated — same words; the scan has a doubtful letter [?] but the digitization's
                      independent reading supplies a word that fits, so two readings agree
       substantive — a different word, number, or content: a person decides"""
    if skeleton(fix['digitized']) != skeleton(fix['scan']):
        return 'editorial' if editorial(fix) else 'substantive'
    return 'corroborated' if '[?]' in fix['scan'] else 'spelling'


TRIAGE = {(d['sheet'], d['i']): d for d in
          json.load(open(os.path.join(ROOT, 'bereshit-scancheck', 'triage.json')))['decisions']}


def apply_triage(sid, key, it):
    d = TRIAGE.get((sid, key))
    if not d:
        return
    it['triage'] = {'use': d['use'], 'why': d['why']}
    if d['use'] in ('digitized', 'editorial') and it.get('digitized_he'):
        it['he'], it['scan_reading'] = it['digitized_he'], it['he']
        it['basis'] = 'digitization'
    if d['use'] == 'not-published':
        it['publish'] = False
    if d['use'] != 'open':
        it.pop('needs_human', None)


OVERRIDES = json.load(open(os.path.join(ROOT, 'bereshit-scancheck', 'overrides.json')))['insert']


def harvest_1943():
    """1943 Part 1 from the verified transcription; sources from the digitization by the ↔ map."""
    raw = json.load(open(os.path.join(ROOT, 'bereshit-raw', '162000.json')))
    md = open(os.path.join(ROOT, 'bereshit-transcriptions', '162000-1943.md')).read()
    part1 = md.split('## Part 1')[1].split('## Part 2')[0]
    blocks = re.split(r'\n(?=\*\*(?:\[\[)?[אבגד]\.)', part1)[1:]
    sections = []
    for b in blocks:
        letter = re.match(r'\*\*(?:\[\[)?([אבגד])', b)[1]
        lines = [l for l in b.strip().splitlines()]
        header = re.sub(r'\[\[.*?\]\]', '', lines[0]).replace('**', '').strip()
        idx = [int(x) for x in re.findall(r'\[(\d+)\]', next((l for l in lines if l.startswith('↔')), ''))]
        idx = list(range(idx[0], idx[-1] + 1)) if idx else []
        # Drop the ↔ mapping paragraph (it can wrap onto following lines) and editorial notes.
        body, in_map = [], False
        for l in lines[1:]:
            if l.startswith('↔'):
                in_map = True
            elif not l.strip():
                in_map = False
            if not in_map:
                body.append(re.sub(r'\[\[.*?\]\]', '', l).strip())
        # Re-join lines the transcription wrapped: a new item starts at "1." or after a line
        # that ends a sentence.
        joined = []
        for l in body:
            if not l:
                continue
            if joined and not re.match(r'^\d\.', l) and not re.search(r'[?.:!"״]$', joined[-1]):
                joined[-1] += ' ' + l
            else:
                joined.append(l)
        items, prose, asked = [], [], False
        for l in joined:
            if not l:
                continue
            # Once she has asked, the lines that follow are her tasks too ("איזו מלה … ." ends in a period).
            if re.match(r'^\d\.', l) or l.endswith('?') or asked:
                asked = True
                if prose:
                    items.append({'kind': 'text', 'he': ' '.join(prose), 'basis': 'transcription'}); prose = []
                items.append({'kind': 'question', 'he': l, 'basis': 'transcription'})
            else:
                prose.append(l)
        if prose:
            items.append({'kind': 'text', 'he': ' '.join(prose), 'basis': 'transcription'})
        for i in idx:
            src = raw['sources'][i]
            t = src.get('text') or {}
            items.append({'i': i, 'kind': 'source', 'ref': src['ref'], 'he': strip(t.get('he')),
                          'en': strip(t.get('en')), 'basis': 'digitization'})
        sections.append({'letter': letter, 'header_scan': header, 'header_digitized': None, 'items': items})
    return sections


def harvest(theme, year, year_he, sid, letters):
    raw = json.load(open(os.path.join(ROOT, 'bereshit-raw', f'{sid}.json')))
    pdf = re.search(r'pdf/(\d+)\.pdf', raw.get('summary', ''))[1]
    base = {'sheet_id': sid, 'year_g': year, 'year_he': year_he, 'theme': theme, 'title': raw['title'],
            'sefaria_url': f'https://www.sefaria.org/sheets/{sid}',
            'pdf_url': f'https://www.nechama.org.il/pdf/{pdf}.pdf'}
    if sid == 162000:
        return {**base, 'scancheck': 'bereshit-transcriptions/162000-1943.md (Part 1 verified by Lev, 2026-10-06)',
                'sections': harvest_1943(), 'missing_from_digitization': [
                    {'section': 'ב', 'note': 'מלבי"ם (quoted in the scan; see transcription)'},
                    {'section': 'ג', 'note': 'רש"י ד"ה אלה'}],
                'needs_human': []}
    sc = parse_scancheck(os.path.join(ROOT, 'bereshit-scancheck', f'{sid}-{year}.md'))
    secs = raw_sections(raw)
    out_secs, needs = [], []
    for L in letters:
        s = secs[L]
        items = []
        for it in s['items']:
            it = dict(it)
            st = (sc or {}).get('status', {}).get(it['i'])
            if st:
                it['scan_status'] = st['status']
            if it['kind'] == 'text' and (re.match(r'^\(?\d+[.)]', it['he']) or '?' in it['he']):
                it['kind'] = 'question'
            pairs = (sc or {}).get('pairs', {}).get(it['i'], [])
            # Editorial additions keep the digitizer's (richer) citation: don't apply them.
            edits = [p for p in pairs if classify({'digitized': p[0], 'scan': p[1]}) == 'editorial']
            if edits:
                it['editorial_additions'] = [{'digitized': a, 'scan': b} for a, b in edits]
            pairs = [p for p in pairs if p not in edits]
            if pairs:
                new, applied, unapplied, sics = apply_pairs(it['he'], pairs)
                if new != it['he']:
                    it['digitized_he'], it['he'] = it['he'], new
                if sics:
                    it['sic'] = sics
                it['scan_fixes'] = applied
                if unapplied:
                    it['scan_unapplied'] = unapplied
            it['basis'] = 'scan' if it.get('scan_fixes') else 'digitization'
            if it.get('scan_status') == 'NOT-IN-SCAN' and it['kind'] != 'source':
                it['exclude'] = 'not in the scan: not her words'
            mine = it['kind'] in ('text', 'question')
            for f in it.get('scan_fixes', []) + it.get('scan_unapplied', []):
                f['class'] = classify(f)
            # Unapplied spelling-only fixes: the meaning is unchanged, so keep the digitized
            # words rather than ask a person about a missing yod.
            hard = [f for f in it.get('scan_unapplied', []) if f['class'] == 'substantive']
            if mine and (hard or any(f['class'] == 'substantive' for f in it.get('scan_fixes', []))):
                it['needs_human'] = True
            apply_triage(sid, it['i'], it)
            if it.get('needs_human'):
                needs.append(it['i'])
            items.append(it)
            for ov in OVERRIDES:
                if ov['sheet'] == sid and ov['after'] == it['i']:
                    new = {'kind': ov['kind'], 'he': ov['he'], 'basis': 'scan-only',
                           'cite': 'bereshit-scancheck/' + ov['cite'],
                           **({'needs_human': True} if '[?]' in ov['he'] else {})}
                    apply_triage(sid, f"after {ov['after']}", new)
                    if new.get('needs_human'):
                        needs.append(f"after {ov['after']}")
                    items.append(new)
        out_secs.append({'letter': L,
                         'header_scan': (sc or {}).get('headers', {}).get(L),
                         'header_digitized': s['header']['digitized'] if s['header'] else None,
                         'items': items})
    return {**base, 'scancheck': sc['path'] if sc else None,
            'scancheck_missing': sc is None,
            'sections': out_secs,
            'digitizer_additions': (sc or {}).get('additions', []),
            'needs_human': needs}


if __name__ == '__main__':
    report = []
    for theme, leaves in CHOSEN.items():
        os.makedirs(os.path.join(ROOT, 'bereshit-harvest', theme), exist_ok=True)
        for year, year_he, sid, letters in leaves:
            h = harvest(theme, year, year_he, sid, letters)
            json.dump(h, open(os.path.join(ROOT, 'bereshit-harvest', theme, f'{year}.json'), 'w'),
                      ensure_ascii=False, indent=1)
            n = sum(len(s['items']) for s in h['sections'])
            scan = sum(1 for s in h['sections'] for it in s['items'] if it.get('basis') in ('scan', 'scan-only', 'transcription'))
            unap = sum(len(it.get('scan_unapplied', [])) for s in h['sections'] for it in s['items'])
            excl = sum(1 for s in h['sections'] for it in s['items'] if it.get('exclude'))
            report.append(f"{theme}/{year} {sid}: {len(h['sections'])} sections, {n} items, "
                          f"{scan} from scan, {excl} excluded, {unap} unapplied, "
                          f"needs_human={h['needs_human']}{'  [NO SCANCHECK]' if h.get('scancheck_missing') else ''}")
    print('\n'.join(report))

    # REVIEW.md: every substantive difference in her own words, for a person to settle.
    L = ['# Scan-check review list (GENERATED by harvest_bereshit.py — do not hand-edit)', '',
         'Only differences in **her own words** (questions, framing, headers, lines she wrote)',
         'that change a word, a number or content. Spelling/punctuation/abbreviation differences',
         'are applied from the scan automatically, and citation detail the digitizers *added* is',
         'kept as an editorial addition (Lev, 2026-10-06); neither is listed. For each line, check the',
         'scan and mark ✅ (scan reading right) or ✏️ (correction). Cites point into the scan-check',
         'files, which cite page and strip.', '',
         'Differences already settled by evidence (an independent text, a zoomed reading, her own',
         'recurring wording) are recorded with their reason in `triage.json` and are not listed here.', '']
    for theme, leaves in CHOSEN.items():
        for year, year_he, sid, letters in leaves:
            h = json.load(open(os.path.join(ROOT, 'bereshit-harvest', theme, f'{year}.json')))
            rows = []
            for sec in h['sections']:
                hs, hd = sec.get('header_scan'), sec.get('header_digitized')
                for it in sec['items']:
                    if it['kind'] not in ('text', 'question'):
                        continue
                    if it.get('triage', {}).get('use') not in (None, 'open'):
                        continue
                    if it.get('triage', {}).get('use') == 'open':
                        rows.append(f"- §{sec['letter']} [{it.get('i')}] **open, to settle when drafting**: {it['triage']['why']}")
                        continue
                    if it.get('basis') == 'scan-only':
                        rows.append(f"- §{sec['letter']} **missing from the digitization**: «{it['he']}»  ({it['cite']})")
                        continue
                    if it.get('exclude'):
                        rows.append(f"- §{sec['letter']} [{it['i']}] **not in the scan** (digitizer's?): «{it['he'][:120]}»")
                        continue
                    # One line per change: shortest fragment first; drop longer restatements
                    # that contain a fragment already listed.
                    subs = sorted((f for f in it.get('scan_fixes', []) + it.get('scan_unapplied', [])
                                   if f['class'] == 'substantive'), key=lambda f: len(f['scan']))
                    kept = []
                    for f in subs:
                        pieces = [norm(x) for x in re.split(r'…|\.\.\.', f['scan']) if x.strip()]
                        if any(all(p and p in norm(k['scan']) for p in pieces) or norm(k['scan']) in norm(f['scan']) for k in kept):
                            continue
                        kept.append(f)
                    for f in kept:
                        tag = '' if f in it.get('scan_fixes', []) else ' *(not auto-applied)*'
                        rows.append(f"- §{sec['letter']} [{it['i']}] digitized «{f['digitized'][:140]}» → scan «{f['scan'][:140]}»{tag}")
            if rows:
                L += [f"## {year} ({year_he}) · sheet {sid} · {theme}", f"Scan check: `{h.get('scancheck')}`", ''] + rows + ['']
    open(os.path.join(ROOT, 'bereshit-scancheck', 'REVIEW.md'), 'w').write('\n'.join(L) + '\n')
