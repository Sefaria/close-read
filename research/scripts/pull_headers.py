"""Fetch all Nasso sheets and extract internal section headers."""
import json, re, os, urllib.request, time

INV_DIR = '/tmp/nechama/sheets'
os.makedirs(INV_DIR, exist_ok=True)

d = json.load(open('/tmp/nechama/all-sheets.json'))
nasso = [s for s in d['sheets'] if any(
    isinstance(t, dict) and t.get('slug') == 'parashat-naso' for t in (s.get('topics') or [])
)]

def fetch(sid):
    fp = f'{INV_DIR}/{sid}.json'
    if os.path.exists(fp):
        return json.load(open(fp))
    req = urllib.request.Request(
        f'https://www.sefaria.org/api/sheets/{sid}',
        headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read().decode()
    open(fp, 'w').write(data)
    time.sleep(0.2)
    return json.loads(data)

def strip_html(s):
    return re.sub(r'<[^>]+>', ' ', s or '').strip()

# Hebrew letter prefix as a section header
HEB_LETTERS = "אבגדהוזחטיכלמנסעפצקרשת"
SEC_RE = re.compile(r'^([' + HEB_LETTERS + r'])[.׳״\'”]\s+(.+)')

results = []
for s in nasso:
    sid = s['id']
    try:
        sheet = fetch(sid)
    except Exception as e:
        print(f'FAIL {sid}: {e}')
        continue
    headers = []
    for src in sheet.get('sources', []):
        if 'outsideText' in src:
            txt = strip_html(src['outsideText'])
            txt = re.sub(r'^[\s‎‏]+', '', txt)
            m = SEC_RE.match(txt)
            if m:
                headers.append(txt[:120])
    g_year = None
    m = re.search(r'(\d{4})', s.get('summary', '') or '')
    if m:
        g_year = int(m.group(1))
    results.append({
        'id': sid,
        'title': s['title'],
        'g_year': g_year,
        'headers': headers,
        'num_sources': len(sheet.get('sources', [])),
    })

results.sort(key=lambda r: (r['g_year'] or 9999, r['id']))
json.dump(results, open('/tmp/nechama/nasso-inventory.json', 'w'),
          ensure_ascii=False, indent=2)
print(f'wrote {len(results)} entries to /tmp/nechama/nasso-inventory.json')

# Print summary
for r in results:
    print(f"\n{r['g_year']} | id {r['id']} | {r['title']}")
    print(f"  sources: {r['num_sources']}, sections found: {len(r['headers'])}")
    for h in r['headers']:
        print(f"    - {h}")
