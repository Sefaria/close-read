"""Stage 4 — assemble data/noach.json, the Noach garden (template: build_bereshit.py).

    overview → root fork (5 themes) → per theme: intro → fork (3 years) → leaves

Leaves live in research/scripts/noach_leaves/<theme>.py (one function per gilayon,
`leaf_<year>()`, returning its sections, the first being the branch target). The shared
helpers and the rules they enforce are in nechama_lib.py; the drafting rules are in
research/parshiyot/noach-leaves/BRIEF.md.

The overview, theme intros and forks written here follow the same rule as the leaves: they
point at the content (the verse, the question a path explores), not at how her sheets are
built. Fork labels come from each leaf's own title, so they can't drift from it.
"""
import importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from noach_lib import REPO, narration, primary  # noqa: E402

THEMES = [
    {'id': 'generation', 'abbr': 'gn', 'label': 'A Righteous Man in His Generations', 'range': 'Genesis 6:9–7:5',
     'years': ['1947', '1954', '1958'],
     'panel': ('Genesis 6:9, 11, 13', ['6:9', '6:11', '6:13'], {
         'tzadik': ('נח איש צדיק תמים היה בדרתיו', 'Noah was a righteous man; he was blameless in his age'),
         'vatishachet': ('ותשחת הארץ לפני האלהים', 'The earth became corrupt before God'),
         'ketz': ('קץ כל בשר בא לפני', 'I have decided to put an end to all flesh'),
     }),
     'intro': [('One man, and his generation.', None),
               ('A righteous man, blameless “in his age.”', ['tzadik']),
               ('And an earth corrupt before God, whose end has come.', ['vatishachet', 'ketz'])]},
    {'id': 'flood', 'abbr': 'fl', 'label': 'The Flood', 'range': 'Genesis 7:1–8:19',
     'years': ['1945', '1952', '1962'],
     'panel': ('Genesis 7:23-8:1', ['7:23', '7:24', '8:1'], {
         'vayimach': ('וימח את כל היקום', 'All existence on earth was blotted out'),
         'vayishaer': ('וישאר אך נח', 'Only Noah was left'),
         'vayizkor': ('ויזכר אלהים את נח', 'God remembered Noah'),
     }),
     'intro': [('The waters rise, and everything is blotted out.', ['vayimach']),
               ('Only Noah is left, and those with him in the ark.', ['vayishaer']),
               ('And then: God remembered Noah.', ['vayizkor'])]},
    {'id': 'covenant', 'abbr': 'cv', 'label': 'Never Again', 'range': 'Genesis 8:20–9:17',
     'years': ['1946', '1951', '1964'],
     'panel': ('Genesis 8:21-22, 9:13', ['8:21', '8:22', '9:13'], {
         'lo-osif': ('לא אסף לקלל עוד את האדמה', 'Never again will I doom the earth'),
         'yetzer': ('כי יצר לב האדם רע מנעריו', 'since the devisings of the human mind are evil from youth'),
         'keshet': ('את קשתי נתתי בענן', 'I have set My bow in the clouds'),
     }),
     'intro': [('After the flood, a resolve.', None),
               ('“Never again,” and the reason given for it.', ['lo-osif', 'yetzer']),
               ('And a sign in the clouds.', ['keshet'])]},
    {'id': 'blood', 'abbr': 'bl', 'label': 'Your Lifeblood', 'range': 'Genesis 9:1–7',
     'years': ['1948', '1957', '1970'],
     'panel': ('Genesis 9:1, 5-6', ['9:1', '9:5', '9:6'], {
         'vayevarech': ('ויברך אלהים את נח ואת בניו', 'God blessed Noah and his sons'),
         'damchem': ('ואך את דמכם לנפשתיכם אדרש', 'But for your own life-blood I will require a reckoning'),
         'tzelem': ('כי בצלם אלהים עשה את האדם', 'For in the image of God Was humankind made'),
     }),
     'intro': [('A new blessing, for a world begun again.', ['vayevarech']),
               ('With it, a reckoning for blood.', ['damchem']),
               ('And the reason: the image of God.', ['tzelem'])]},
    {'id': 'babel', 'abbr': 'bb', 'label': 'Babel', 'range': 'Genesis 10:1–11:9',
     'years': ['1944', '1960', '1968'],
     'panel': ('Genesis 11:1, 4, 9', ['11:1', '11:4', '11:9'], {
         'safa': ('שפה אחת ודברים אחדים', 'the same language and the same words'),
         'migdal': ('נבנה לנו עיר ומגדל וראשו בשמים', 'let us build us a city, and a tower with its top in the sky'),
         'balal': ('כי שם בלל יהוה שפת כל הארץ', 'because there the Lord confounded the speech of the whole earth'),
     }),
     'intro': [('One language, and one plan.', ['safa']),
               ('A city, and a tower with its top in the sky.', ['migdal']),
               ('And the name the place was given.', ['balal'])]},
]

# One line per leaf for its branch button: the passage or question it explores. Written with the leaves.
BLURBS = {}


def leaf_sections(theme, year):
    mod = importlib.import_module(f'noach_leaves.{theme}')
    return getattr(mod, f'leaf_{year}')()


def build():
    sections = [{
        'id': 'ov', 'title': {'he': 'פרשת נח', 'en': 'Noach'},
        'primaryText': primary('Genesis 6:9', ['6:9'], {
            'tzadik': ('נח איש צדיק', 'Noah was a righteous man')}),
        'steps': [
            narration('ov-1', 'Genesis 6:9 to 11:32: from Noah to the tower of Babel.'),
            narration('ov-2', 'Five passages, each read through the sources and questions Nechama Leibowitz '
                      'set for it.', highlight=['tzadik']),
            narration('ov-3', 'She wrote on this parsha every year from 1942 to 1971. Each path below follows '
                      'one of those years.'),
        ]}]
    sections.append({
        'id': 'root-fork', 'type': 'decision', 'level': 0,
        'prompt': {'en': 'Where would you like to begin?'},
        'branches': [{'id': t['id'], 'label': {'en': t['label']}, 'blurb': {'en': t['range']},
                      'target': f"section-{t['id']}"} for t in THEMES]})
    missing = []
    for t in THEMES:
        ref, keys, spec = t['panel']
        sections.append({
            'id': f"section-{t['id']}", 'title': {'en': t['label']},
            'primaryText': primary(ref, keys, spec),
            'steps': [narration(f"{t['abbr']}-intro-{k}", en, highlight=hl)
                      for k, (en, hl) in enumerate(t['intro'], 1)]})
        leaves, branches = [], []
        for y in t['years']:
            try:
                secs = leaf_sections(t['id'], y)
            except (ImportError, AttributeError):
                missing.append(f"{t['id']}/{y}")
                continue
            branches.append({'id': f"{t['abbr']}-{y}", 'label': {'en': secs[0]['title']['en']},
                             **({'blurb': {'en': BLURBS[y]}} if y in BLURBS else {}),
                             'target': secs[0]['id']})
            leaves += secs
        sections.append({'id': f"{t['id']}-fork", 'type': 'decision', 'level': 1,
                         'prompt': {'en': f"{t['label']}: which year?"}, 'branches': branches})
        sections += leaves
    return sections, missing


if __name__ == '__main__':
    sections, missing = build()
    sheet = {
        'title': {
            'he': 'פרשת נח', 'en': 'Parashat Noach',
            'subtitle': {'he': 'עם נחמה ליבוביץ', 'en': 'Genesis 6:9–11:32, with Nechama Leibowitz'},
            'author': {'he': 'נחמה ליבוביץ', 'en': 'From the work of Nechama Leibowitz'},
            'sourceUrl': 'https://www.sefaria.org/profile/nechama-leibowitz',
            'sourceLabel': 'Nechama Leibowitz’s gilyonot on Sefaria',
            'questionLabel': {'he': 'נחמה שואלת', 'en': 'Nechama asks'},
        },
        'sections': sections,
    }
    out = os.path.join(REPO, 'data', 'noach.json')
    with open(out, 'w') as f:
        json.dump(sheet, f, ensure_ascii=False, indent=2)
        f.write('\n')
    n = sum(len(s.get('steps', [])) for s in sections)
    print(f'data/noach.json: {len(sections)} sections, {n} steps; missing leaves: {missing or "none"}')
