"""Stage 4 — assemble data/bereshit.json, the Bereshit garden.

    overview → root fork (5 themes) → per theme: intro → fork (3 years) → leaves

Leaves live in research/scripts/bereshit_leaves/<theme>.py (one function per gilayon,
`leaf_<year>()`, returning its sections, the first being the branch target). The shared
helpers and the rules they enforce are in bereshit_lib.py; the drafting rules are in
research/parshiyot/bereshit-leaves/BRIEF.md.

The overview, theme intros and forks written here follow the same rule as the leaves: they
point at the content (the verse, the question a path explores), not at how her sheets are
built. Fork labels come from each leaf's own title, so they can't drift from it.
"""
import importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from bereshit_lib import REPO, narration, primary  # noqa: E402

THEMES = [
    {'id': 'creation', 'abbr': 'cr', 'label': 'The Days of Creation', 'range': 'Genesis 1:1–2:3',
     'years': ['1943', '1954', '1963'],
     'panel': ('Genesis 1:1-3, 2:1-3', ['1:1', '1:2', '1:3', '2:1', '2:2', '2:3'], {
         'bereshit': ('בראשית ברא אלהים את השמים ואת הארץ', 'When God began to create heaven and earth'),
         'yehi-or': ('ויאמר אלהים יהי אור', 'God said, “Let there be light”'),
         'vayechulu': ('ויכלו השמים והארץ וכל צבאם', 'The heaven and the earth were finished'),
         'vaychal': ('ויכל אלהים ביום השביעי', 'On the seventh day God finished'),
     }),
     'intro': [('Six days of making, and a seventh.', None),
               ('It begins with heaven and earth, and with a word: “Let there be light.”', ['bereshit', 'yehi-or']),
               ('It ends with a finishing, on the seventh day.', ['vayechulu', 'vaychal'])]},
    {'id': 'garden', 'abbr': 'gd', 'label': 'Adam, the Garden, the Woman', 'range': 'Genesis 2:4–25',
     'years': ['1952', '1953', '1965'],
     'panel': ('Genesis 2:7-8, 15, 18', ['2:7', '2:8', '2:15', '2:18'], {
         'yitzer': ('וייצר', 'formed a Human'),
         'gan': ('ויטע יהוה אלהים גן בעדן מקדם', 'planted a garden in Eden, in the east'),
         'leovda': ('לעבדה ולשמרה', 'to till it and tend it'),
         'ezer': ('אעשה לו עזר כנגדו', 'I will make a fitting counterpart for him'),
     }),
     'intro': [('The human, the garden, and the woman.', None),
               ('A human is formed from the soil, and a garden is planted.', ['yitzer', 'gan']),
               ('“To till it and tend it.” And then: it is not good to be alone.', ['leovda', 'ezer'])]},
    {'id': 'sin', 'abbr': 'sn', 'label': 'The Trees and the Sin', 'range': 'Genesis 2:9–3:24',
     'years': ['1944', '1964', '1968'],
     'panel': ('Genesis 2:16-17, 3:6', ['2:16', '2:17', '3:6'], {
         'mikol': ('מכל עץ הגן אכל תאכל', 'Of every tree of the garden you are free to eat'),
         'umeetz': ('ומעץ הדעת טוב ורע לא תאכל ממנו', 'but as for the tree of knowledge of good and bad, you must not eat of it'),
         'vatikach': ('ותקח מפריו ותאכל', 'she took of its fruit and ate'),
     }),
     'intro': [('Every tree but one.', None),
               ('One command, with one exception.', ['mikol', 'umeetz']),
               ('And then she took of its fruit and ate.', ['vatikach'])]},
    {'id': 'cain', 'abbr': 'cn', 'label': 'Cain and Abel', 'range': 'Genesis 4:1–16',
     'years': ['1942', '1956', '1958'],
     'panel': ('Genesis 4:3-5, 8', ['4:3', '4:4', '4:5', '4:8'], {
         'minchat-hevel': ('וישע יהוה אל הבל ואל מנחתו', 'The Lord paid heed to Abel and his offering'),
         'kayin': ('ואל קין ואל מנחתו לא שעה', 'but paid no heed to Cain and his offering'),
         'vayaharge': ('ויקם קין אל הבל אחיו ויהרגהו', 'Cain set upon his brother Abel and killed him'),
     }),
     'intro': [('Two brothers, two offerings.', None),
               ('One is accepted; the other is not.', ['minchat-hevel', 'kayin']),
               ('And in the field, the first killing.', ['vayaharge'])]},
    {'id': 'flood', 'abbr': 'fl', 'label': 'From Cain’s Line to the Flood', 'range': 'Genesis 4:17–6:8',
     'years': ['1950', '1969', '1971'],
     'panel': ('Genesis 4:23, 6:2, 6:6', ['4:23', '6:2', '6:6'], {
         'lemech': ('ויאמר למך לנשיו', 'And Lamech said to his wives'),
         'bnei-haelohim': ('ויראו בני האלהים את בנות האדם', 'the divine beings saw how pleasing the human women were'),
         'vayinachem': ('וינחם יהוה כי עשה את האדם בארץ', 'the Lord regretted having made humankind on earth'),
     }),
     'intro': [('From Lamech’s song to the eve of the Flood.', None),
               ('A man’s song to his wives.', ['lemech']),
               ('Divine beings and human daughters; and a regret.', ['bnei-haelohim', 'vayinachem'])]},
]

# One line per leaf for its branch button: the passage or question it explores.
BLURBS = {
    '1943': '“And on the seventh day God finished,” and “These are the generations of heaven and earth.”',
    '1954': 'Why does the Torah begin with creation? And what does “God said” mean?',
    '1963': 'The chapter break at “Va-yekhullu,” the Leningrad Codex, and “very good.”',
    '1952': '“No shrub of the field was yet”: the second account, the garden, and the work of tending it.',
    '1953': '“It is not good for the human to be alone”: a helper, against him.',
    '1965': 'A living being, taken into the garden, naming the animals.',
    '1944': 'The serpent, the fruit, the sound in the garden, and “Where are you?”',
    '1964': 'The two trees, and the one that must not be eaten.',
    '1968': 'After the eating: hiding, and blame.',
    '1942': '“Surely, if you do right”: what Genesis 4:7 means, and Cain’s punishment and sign.',
    '1956': 'The causes of the quarrel, Rashi’s reading of the brothers, and 4:7 once more.',
    '1958': 'The story’s shape, its parallels with Eden, and the curse.',
    '1950': 'The line of Cain, its arts, and Lamech’s song: apology or boast?',
    '1969': 'Where the units of the story end, calling on the name of the Lord, and Enoch.',
    '1971': 'Who are the “sons of God,” and “My spirit shall not abide in man forever.”',
}


def leaf_sections(theme, year):
    mod = importlib.import_module(f'bereshit_leaves.{theme}')
    return getattr(mod, f'leaf_{year}')()


def build():
    sections = [{
        'id': 'ov', 'title': {'he': 'פרשת בראשית', 'en': 'Bereshit'},
        'primaryText': primary('Genesis 1:1', ['1:1'], {
            'bereshit': ('בראשית ברא אלהים', 'When God began to create')}),
        'steps': [
            narration('ov-1', 'Genesis 1:1 to 6:8: from the first creation to the eve of the Flood.'),
            narration('ov-2', 'Five passages, each read through the sources and questions Nechama Leibowitz '
                      'set for it.', highlight=['bereshit']),
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
            'he': 'פרשת בראשית', 'en': 'Parashat Bereshit',
            'subtitle': {'he': 'עם נחמה ליבוביץ', 'en': 'Genesis 1:1–6:8, with Nechama Leibowitz'},
            'author': {'he': 'נחמה ליבוביץ', 'en': 'From the work of Nechama Leibowitz'},
            'sourceUrl': 'https://www.sefaria.org/profile/nechama-leibowitz',
            'sourceLabel': 'Nechama Leibowitz’s gilyonot on Sefaria',
            'questionLabel': {'he': 'נחמה שואלת', 'en': 'Nechama asks'},
        },
        'sections': sections,
    }
    out = os.path.join(REPO, 'data', 'bereshit.json')
    with open(out, 'w') as f:
        json.dump(sheet, f, ensure_ascii=False, indent=2)
        f.write('\n')
    n = sum(len(s.get('steps', [])) for s in sections)
    print(f'data/bereshit.json: {len(sections)} sections, {n} steps; missing leaves: {missing or "none"}')
