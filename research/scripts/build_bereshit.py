"""Stage 4 — build the Bereshit Close Read from the checked harvest.

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

What *is* authored here: English translations marked en_basis "ours", and narration, which
names the gilayon, the passage, and who speaks next. It doesn't explain the sources, and
it never states her question for her.

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
            key = it.get('i', None)
            if key == i or (isinstance(i, str) and it.get('basis') == 'scan-only'
                            and k and sec['items'][k - 1].get('i') == int(i.split()[1])):
                bad = it.get('exclude') or it.get('publish') is False or it.get('triage', {}).get('use') == 'open'
                assert not bad, f'{path} [{i}] is not publishable: {it.get("exclude") or it.get("triage")}'
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
               highlight=None, effect=None, start=None, stop=None):
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


# ─── leaves ────────────────────────────────────────────────────────────────

def leaf_1963(prefix='cr-1963', title_card=True):
    """Gilayon תשכ"ג (160726): §א (with the Leningrad Codex), §ג, §ד, §ה. §ב is out (pack §7)."""
    h = harvest('creation', '1963')
    P = gen_1_31_2_3
    jacob_q_start = 'הסבר, למה אין חלוקה'
    secs = []

    secs.append({'id': prefix, 'title': {'he': 'שאלת מבנה', 'en': 'A Question of Structure'},
                 **({} if title_card else {'titleCard': False}),
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-intro', 'Gilayon תשכ"ג (1963). Her sheet takes in Genesis 1:31 to 2:3, '
                  'and its first section is headed simply “a question of structure.”'),
        commentary(f'{prefix}-jacob', h, 2, 'Benno Jacob', 'בנו יעקב', 'Benno Jacob',
                   'Benno Jacob, in his commentary on Genesis 2:3, remarks: the chapter division '
                   '(that of the Christian bishop of the early thirteenth century), which opens a new '
                   'chapter at “Va-yekhullu,” is not correct, and separates things that belong together.',
                   'ours', stop='בין הדבקים.', highlight=['vayechulu']),
    ]})

    secs.append({'id': f'{prefix}-1v', 'titleCard': False, 'title': {'en': 'The Leningrad Codex, folio 1v'},
                 'primaryText': FOLIO_1V, 'steps': [
        narration(f'{prefix}-codex', 'This is the opening of Genesis in the Leningrad Codex, a complete '
                  'Hebrew Bible copied in 1008, centuries before chapter numbers existed.'),
        narration(f'{prefix}-days', 'The scribe ends each day with an open break. After “and there was '
                  'evening and there was morning,” the rest of the line, or the next line, is left blank, '
                  'and the next day starts on a fresh line.',
                  highlight=['day-1', 'day-2', 'day-3', 'day-4', 'day-5']),
    ]})

    secs.append({'id': f'{prefix}-2r', 'titleCard': False, 'title': {'en': 'The Leningrad Codex, folio 2r'},
                 'primaryText': FOLIO_2R, 'steps': [
        narration(f'{prefix}-2r-intro', 'The next page, folio 2r, carries Genesis 1:26 to 2:19.'),
        narration(f'{prefix}-day-6', 'The sixth day closes the same way. “Va-yekhullu” begins on the line below it.',
                  highlight=['day-6']),
        narration(f'{prefix}-seventh', 'This is where the chapter changes: chapter 2 begins here, with '
                  '“Va-yekhullu.” Genesis 2:1–3 runs from the foot of this column to the top of the next, a '
                  'paragraph of its own. Counting from the first verse of the book, it is the seventh.',
                  highlight=['vayechulu-a', 'vayechulu-b'], effect='glow'),
        question(f'{prefix}-q-a', h, 2, 'Explain why this division [the chapter beginning at 2:1, with '
                 '“Va-yekhullu”] does not fit the structure of our parasha.', start=jacob_q_start),
    ]})

    secs.append({'id': f'{prefix}-good', 'titleCard': False,
                 'title': {'he': 'והנה טוב מאד', 'en': '“And behold, it was very good”'},
                 'primaryText': P(), 'steps': [
        # §ג — scan header: ג. א' ל"א וירא אלו-הים את כל אשר עשה והנה טוב מאד.
        narration(f'{prefix}-g-intro', 'Her next section stays on 1:31, the end of the sixth day.'),
        commentary(f'{prefix}-br-9-5', h, 9, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'In the Torah of R. Meir they found written (Matnot Kehunah: in his Torah scroll he '
                   'wrote this in the margin) “and behold, it was very good” — “and behold, death is '
                   'good.” R. Shmuel bar Nachman said: I was riding on my grandfather’s shoulder, going up '
                   'from his town to Kefar Chanan by way of Beit She’an, and I heard R. Shimon ben Elazar '
                   'sitting and expounding in the name of R. Meir: “and behold, it was very good” — “and '
                   'behold, death is good.”',
                   'ours', ref='Bereshit Rabbah 9:5', highlight=['tov-meod']),
        commentary(f'{prefix}-br-9-7', h, 10, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Nachman bar Shmuel… said: “Behold, it was good” — this is the good inclination; '
                   '“and behold, it was very good” — this is the evil inclination. Is the evil inclination '
                   'very good? Astonishing! But were it not for the evil inclination, a person would not '
                   'build a house, nor marry, nor have children, nor do business. And so Solomon says '
                   '(Ecclesiastes 4): “it is a man’s rivalry with his neighbor.”',
                   'ours', ref='Bereshit Rabbah 9:7', highlight=['tov-meod']),
        narration(f'{prefix}-g-on-first', 'On the first midrash she adds two of its commentators.'),
        commentary(f'{prefix}-maharzu', h, 12, 'Maharzu', 'מהרז"ו', 'Maharzu, on the midrash',
                   'As it is written (Ecclesiastes), “and the day of death than the day of one’s birth” — '
                   'and he no longer sins.', 'ours', start='דכתיב'),
        commentary(f'{prefix}-matnot', h, 13, 'Matnot Kehunah', 'מתנות כהונה', 'Matnot Kehunah, on the midrash',
                   'For it separates him from this passing world and brings him to the enduring world, '
                   'and there too he no longer comes to sin.', 'ours', start='שמפרידו'),
        question(f'{prefix}-q-g1', h, 14, '1. Can you explain the first midrash another way, not as the '
                 'commentators on the midrash above do?', stop='הנ"ל'),
        question(f'{prefix}-q-g2', h, 15, '2. On what linguistic basis in our verse are the midrashim above built?',
                 highlight=['tov-meod']),
        question(f'{prefix}-q-g3', h, 16, '3. Explain the idea of the second midrash.'),

        # §ד — scan header: ד. והנה טוב מאד.
        narration(f'{prefix}-d-intro', 'She returns to the same three words with Ralbag.', highlight=['tov-meod']),
        commentary(f'{prefix}-ralbag', h, 20, 'Ralbag', 'רלב"ג', 'Ralbag',
                   'He already included in this statement all that He made, because some of what He made '
                   'of the world was not intended for its own sake, <u>and the good was not complete until '
                   'the purpose was complete, for whose sake what came before the purpose existed</u>. And '
                   'likewise the complete good was not completed for the world as a whole until it was in '
                   'its wholeness and perfection. And he already ascribed this coming-into-being to the '
                   'sixth day. And He thereby informed us of a root on which all natural science is built: '
                   'that among natural things nothing is in vain.',
                   'ours', ref='Ralbag on Torah, Genesis 1:24:6',
                   he=underline(cut(item(h, 20)[0]), 'ולא נשלם הטוב עד השלם התכלית אשר בעבורו היה מה שלפני התכלית'),
                   highlight=['tov-meod', 'yom-hashishi']),
        question(f'{prefix}-q-d1', h, 21, '1. Explain the underlined words.'),
        question(f'{prefix}-q-d2', h, 22, '2. Explain how he differs from the midrashim.'),

        # §ה — scan header: ה. ויכל אלו-הים ביום השביעי.
        # Her questions stand together at the end of the section; here each follows the source it
        # asks about, and her first question, which asks what the question is, closes the section.
        narration(f'{prefix}-h-intro', 'Her last section turns to 2:2: “And on the seventh day God finished.”',
                  highlight=['vaychal']),
        narration(f'{prefix}-h-order', 'Her questions for this section stand together at its end. Here each '
                  'follows the source it asks about.'),
        commentary(f'{prefix}-br-10-9', h, 25, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'Rabbi asked R. Yishmael son of R. Yose: Have you heard from your father what “And on the '
                   'seventh day God finished” means? Astonishing! Rather, it is like one who strikes with a '
                   'hammer on the anvil: he raised it while it was still day and brought it down after dark. '
                   'R. Shimon bar Yochai said: Flesh and blood, who knows neither its times nor its moments '
                   'nor its hours, adds from the weekday onto the holy; but the Holy One, blessed be He, who '
                   'knows His moments, His times and His hours, enters it by a hair’s breadth. Geniva and '
                   'the Rabbis — Geniva said: A parable of a king who made himself a bridal canopy, painted it '
                   'and adorned it; and what did it lack? A bride to enter it. So, what did the world lack? '
                   'Shabbat. The Rabbis said: A parable of a king who had a ring made; what did it lack? A '
                   'seal. So, what did the world lack? Shabbat.',
                   'ours', ref='Bereshit Rabbah 10:9', start='רבי שאליה', highlight=['vaychal']),
        question(f'{prefix}-q-h2', h, 31, '2. In what do Geniva and the Rabbis both differ from the view of '
                 'R. Shimon bar Yochai?'),
        question(f'{prefix}-q-h3', h, 32, '3. What is the difference in idea between the parable of the bride '
                 'and the parable of the seal?'),
        # Not Sefaria's English: it translates the canonical comment ("R. Simeon says…", with
        # cross-references), not the abridged text she quoted.
        commentary(f'{prefix}-rashi', h, 26, 'Rashi', 'רש"י', 'Rashi',
                   '“And on the seventh day God finished”: Flesh and blood, who does not know his times and '
                   'moments, must add from the weekday onto the holy; the Holy One, blessed be He, who knows '
                   'His times and moments, entered it by a hair’s breadth, and it seemed as though He finished '
                   'on that very day. Another explanation: What did the world lack? Rest. Shabbat came, rest '
                   'came; the work was finished and completed.',
                   'ours', ref='Rashi on Genesis 2:2:1', highlight=['vaychal']),
        question(f'{prefix}-q-h5', h, 34, '5. What is Rashi’s way of reworking his source?'),
        commentary(f'{prefix}-efodi', h, 27, 'Profiat Duran', 'ר\' יצחק פריפוט דוראן',
                   'R. Yitzhak Profiat Duran, Ma’aseh Efod',
                   'And he (R. Yonah ibn Janach, in Sefer HaRikmah) already brought other uses of the letter '
                   'bet: that it (= the letter bet) carries the sense of “before” and “after”: “And on the '
                   'seventh day God finished”; (Exodus 12:15) “But on the first day you shall put away '
                   'leaven” — in the sense of “before.”',
                   'ours', start='וכבר הביא', highlight=['vaychal']),
        commentary(f'{prefix}-ibn-ezra', h, 28, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'Some say that the days are created, and with the creation of the seventh day the work '
                   'was complete; and this interpretation is tasteless. And some say there is a bet whose '
                   'sense is “before,” as in (Deuteronomy 25:4) “You shall not muzzle an ox in its '
                   'threshing,” (Exodus 12:15) “But on the first day you shall put away.” And why this '
                   'trouble? Finishing a work is not a work; it is as if it said: He did no work. And so too '
                   'the meaning of “finished,” and also of “ceased.” And the sense of “His work which He had '
                   'done” is: on the sixth day, before the Sabbath day.',
                   'ours', ref='Ibn Ezra on Genesis 2:2', start='יש אומרים', highlight=['vaychal', 'vayishbot']),
        question(f'{prefix}-q-h6', h, 35, '6. To which of the commentators mentioned in our gilayon does Ibn '
                 'Ezra allude in the first “some say,” and to which in the second?'),
        commentary(f'{prefix}-r-avraham', h, 29, 'R. Avraham ben HaRambam', 'ר\' אברהם בן הרמב"ם',
                   'R. Avraham ben HaRambam',
                   'The ancients and the commentators, of blessed memory, were perplexed about the reason '
                   'for His saying “and He finished on the seventh day”… And I too will answer, even though '
                   'what my predecessor said about it is not far from what I say: every completion between '
                   'two boundaries stands in one and the same relation to those two boundaries. This is '
                   'plain, and only one who does not understand it doubts it. The completion of creation '
                   'came with the end of the sixth day and the beginning of the seventh day; therefore the '
                   'relation of the completion of creation to the end of the sixth day and to the beginning '
                   'of the seventh day is one. Therefore: had Scripture said “God finished on the sixth day,” '
                   'its sense would be with the end of the sixth day; and when it says “God finished on the '
                   'seventh day,” its sense is that at the beginning of the seventh day creation was '
                   'complete — not that there was a new creation on the seventh day.',
                   'ours', start='ונבוכו', highlight=['vaychal'], effect='glow'),
        question(f'{prefix}-q-h1', h, 30, '1. What is the question they deal with, and how many different '
                 'answers were given above?'),
    ]})
    return secs


# ─── output ────────────────────────────────────────────────────────────────

def build_review_1963():
    sheet = {
        'title': {
            'he': 'בראשית תשכ"ג: היום השישי והיום השביעי',
            'en': 'Bereshit 1963: The Sixth Day and the Seventh',
            'subtitle': {'he': 'גיליון בראשית תשכ"ג', 'en': 'One leaf of the Bereshit garden, for review'},
            'author': {'he': 'נחמה ליבוביץ', 'en': 'From the work of Nechama Leibowitz'},
            'sourceUrl': 'https://www.sefaria.org/sheets/160726',
            'sourceLabel': 'View the original gilayon on Sefaria',
            'questionLabel': {'he': 'נחמה שואלת', 'en': 'Nechama asks'},
        },
        'sections': leaf_1963(),
    }
    out = os.path.join(REPO, 'data', 'bereshit-chapter-break.json')
    json.dump(sheet, open(out, 'w'), ensure_ascii=False, indent=2)
    open(out, 'a').write('\n')
    n = sum(len(s['steps']) for s in sheet['sections'])
    print(f'{os.path.relpath(out, REPO)}: {len(sheet["sections"])} sections, {n} steps')


if __name__ == '__main__':
    build_review_1963()
