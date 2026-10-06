"""Stage 1a — snapshot every Nechama gilayon for one parsha into the repo.

Writes research/parshiyot/<parsha>-raw/<sheet_id>.json (one sheet document each,
unmodified from Mongo apart from key order) plus manifest.json recording where the
data came from, the exact query, and a sha256 per file. These raw files are the
bottom of the paper trail: every later claim cites a sheet id + source index into them.

Source: the local `sefaria` DB, a production restore (see the restore-prod-mongo
skill). The live API (`User-Agent: Sefaria/close-read`; a bare Mozilla UA gets a
Cloudflare 403) is equivalent. Check the snapshot against live and record the result
in <parsha>-raw/verification.json.

Usage: python3 research/scripts/snapshot_parsha.py <parsha-name> <topic-slug>
   e.g. python3 research/scripts/snapshot_parsha.py bereshit parashat-bereshit
"""
import datetime, hashlib, json, os, subprocess, sys

NECHAMA = 54380
parsha, slug = sys.argv[1], sys.argv[2]
root = os.path.join(os.path.dirname(__file__), '..', 'parshiyot', f'{parsha}-raw')
os.makedirs(root, exist_ok=True)

query = {"owner": NECHAMA, "topics.slug": slug}
out = subprocess.run(
    ['mongoexport', '--quiet', '-d', 'sefaria', '-c', 'sheets',
     '-q', json.dumps(query), '--jsonFormat=relaxed'],
    check=True, capture_output=True, text=True).stdout
docs = [json.loads(l) for l in out.splitlines() if l.strip()]

# Freshness of the DB as a whole (not just these sheets)
fresh = subprocess.run(
    ['mongo', 'sefaria', '--quiet', '--eval',
     'print(db.sheets.find({},{dateModified:1}).sort({dateModified:-1}).limit(1).next().dateModified)'],
    check=True, capture_output=True, text=True).stdout.strip()

# Volatile engagement fields change without the sheet content changing; drop them
VOLATILE = {'views', 'likes', 'llm_scoring', '_id'}
files = []
for d in sorted(docs, key=lambda d: d['id']):
    clean = {k: v for k, v in d.items() if k not in VOLATILE}
    body = json.dumps(clean, ensure_ascii=False, indent=1, sort_keys=True)
    fn = f"{d['id']}.json"
    open(os.path.join(root, fn), 'w').write(body + '\n')
    files.append({'id': d['id'], 'file': fn, 'title': d['title'],
                  'n_sources': len(d.get('sources', [])),
                  'sha256': hashlib.sha256(body.encode()).hexdigest()})

manifest = {
    'parsha': parsha,
    'source': 'local MongoDB `sefaria.sheets` (production restore)',
    'db_latest_dateModified': fresh,
    'query': query,
    'dropped_fields': sorted(VOLATILE),
    'exported_at': datetime.datetime.now().isoformat(timespec='seconds'),
    'count': len(files),
    'files': files,
}
json.dump(manifest, open(os.path.join(root, 'manifest.json'), 'w'),
          ensure_ascii=False, indent=1)
print(f'wrote {len(files)} sheets to {os.path.normpath(root)}')
