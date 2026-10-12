from noach_lib import *  # noqa: F401,F403
"""Theme 2 — the Flood (Gen 7:1–8:21): leaves 1945, 1952, 1962.

Paper trail: research/parshiyot/noach-leaves/flood.md (slices, omissions, settled items).
"""


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_6_22_7_16():
    """1945 §א: her verse pointers, chapter 6's «אלוקים» against chapter 7's «ה'»."""
    return primary('Genesis 6:22; 7:1, 5, 16', ['6:22', '7:1', '7:5', '7:16'], {
        'tziva-e': ('ככל אשר צוה אתו אלהים', 'just as God commanded him'),
        'vayomer-h': ('ויאמר יהוה לנח', 'Then the Lord said to Noah'),
        'tziva-h': ('ככל אשר צוהו יהוה', 'just as the Lord commanded him'),
        'tziva-16': ('באו כאשר צוה אתו אלהים', 'as God had commanded him'),
        'vayisgor': ('ויסגר יהוה בעדו', 'And the Lord shut him in'),
    })


def gen_7_14_21_23():
    return primary('Genesis 7:14, 21, 23', ['7:14', '7:21', '7:23'], {
        'list-14': ('וכל החיה למינה וכל הבהמה למינה וכל הרמש הרמש על הארץ למינהו',
                    'all beasts of every kind, all cattle of every kind, all creatures of every kind that creep on the earth'),
        'of-14': ('וכל העוף למינהו כל צפור כל כנף', 'and all birds of every kind, every bird, every winged thing'),
        'list-21': ('בעוף ובבהמה ובחיה ובכל השרץ השרץ על הארץ וכל האדם',
                    'birds, cattle, beasts, and all the things that swarmed upon the earth, and all humankind'),
        'list-23': ('מאדם עד בהמה עד רמש ועד עוף השמים', 'humans, cattle, creeping things, and birds of the sky'),
    })


def gen_7_17_20():
    return primary('Genesis 7:17-20', ['7:17', '7:18', '7:19', '7:20'], {
        'yirbu-17': ('וירבו המים וישאו את התבה', 'and the waters increased and raised the ark'),
        'yigberu-18': ('ויגברו המים וירבו מאד על הארץ', 'The waters swelled and increased greatly upon the earth'),
        'gavru-19': ('והמים גברו מאד מאד על הארץ', 'When the waters had swelled much more upon the earth'),
        'harim-19': ('ויכסו כל ההרים הגבהים', 'all the highest mountains everywhere under the sky were covered'),
        'gavru-20': ('חמש עשרה אמה מלמעלה גברו המים', 'Fifteen cubits higher did the waters swell'),
    })


def gen_7_21_24():
    return primary('Genesis 7:21-24', ['7:21', '7:22', '7:23', '7:24'], {
        'vayigva': ('ויגוע כל בשר', 'And all flesh that stirred on earth perished'),
        'kol-21': ('בעוף ובבהמה ובחיה ובכל השרץ השרץ על הארץ וכל האדם',
                   'birds, cattle, beasts, and all the things that swarmed upon the earth, and all humankind'),
        'metu': ('כל אשר נשמת רוח חיים באפיו מכל אשר בחרבה מתו',
                 'All in whose nostrils was the merest breath of life, all that was on dry land, died'),
        'vayimach': ('וימח את כל היקום', 'All existence on earth was blotted out'),
        'vayimachu': ('וימחו מן הארץ', 'they were blotted out from the earth'),
        'nishar': ('וישאר אך נח ואשר אתו בתבה', 'Only Noah was left, and those with him in the ark'),
    })


def gen_7_13_16():
    return primary('Genesis 7:13, 16', ['7:13', '7:16'], {
        'beetsem': ('בעצם היום הזה בא נח', 'That same day Noah'),
        'habaim': ('והבאים זכר ונקבה', 'Thus they that entered comprised male and female'),
        'vayisgor': ('ויסגר יהוה בעדו', 'And the Lord shut him in'),
    })


def gen_8_1():
    return primary('Genesis 8:1', ['8:1'], {
        'vayizkor': ('ויזכר אלהים את נח', 'God remembered Noah'),
        'chaya': ('ואת כל החיה ואת כל הבהמה אשר אתו בתבה',
                  'and all the beasts and all the cattle that were with him in the ark'),
    })


def gen_8_5_9_15_16():
    return primary('Genesis 8:5, 9, 15-16', ['8:5', '8:9', '8:15', '8:16'], {
        'niru': ('בעשירי באחד לחדש נראו ראשי ההרים',
                 'in the tenth month, on the first of the month, the tops of the mountains became visible'),
        'manoach': ('ולא מצאה היונה מנוח לכף רגלה', 'But the dove could not find a resting place for its foot'),
        'vatashov': ('ותשב אליו אל התבה', 'and returned to him to the ark'),
        'vaydaber': ('וידבר אלהים אל נח', 'God spoke to Noah'),
        'tzei': ('צא מן התבה', 'Come out of the ark'),
    })


def gen_8_7_8_13_14():
    return primary('Genesis 8:7-8, 13-14', ['8:7', '8:8', '8:13', '8:14'], {
        'orev': ('וישלח את הערב', 'and sent out the raven'),
        # JPS doesn't render «מאתו» (her underlined word); the English phrase can only be the clause.
        'yona': ('וישלח את היונה מאתו', 'Then he sent out the dove'),
        'charvu': ('חרבו פני האדמה', 'the surface of the ground was drying'),
        'yavsha': ('יבשה הארץ', 'the earth was dry'),
    })


def gen_7_24_8_2():
    return primary('Genesis 7:24–8:2', ['7:24', '8:1', '8:2'], {
        'yigberu': ('ויגברו המים על הארץ חמשים ומאת יום',
                    'And when the waters had swelled on the earth one hundred and fifty days'),
        'vayizkor': ('ויזכר אלהים את נח', 'God remembered Noah'),
        'chaya': ('ואת כל החיה ואת כל הבהמה', 'and all the beasts and all the cattle'),
        'ruach': ('ויעבר אלהים רוח על הארץ', 'God caused a wind to blow across the earth'),
        'vayisachru': ('ויסכרו מעינת תהום וארבת השמים', 'The fountains of the deep and the floodgates of the sky were stopped up'),
        'vayikale': ('ויכלא הגשם מן השמים', 'the rain from the sky was held back'),
    })


def gen_8_16_20_21():
    return primary('Genesis 8:16, 20-21', ['8:16', '8:20', '8:21'], {
        'tzei': ('צא מן התבה', 'Come out of the ark'),
        'vayiven': ('ויבן נח מזבח ליהוה', 'Then Noah built an altar to the Lord'),
        'tehorim': ('ויקח מכל הבהמה הטהרה ומכל העוף הטהור', 'taking of every pure animal and of every pure bird'),
        'olot': ('ויעל עלת במזבח', 'he offered burnt offerings on the altar'),
        'vayarach': ('וירח יהוה את ריח הניחח', 'The Lord smelled the pleasing odor'),
    })


# ─── 1945 ───────────────────────────────────────────────────────────────────

def leaf_1945(prefix='fl-1945'):
    """Gilayon תש"ה (161721): §א, §ב, §ה (pack §7). §ג (Rashi details), §ד («בעצם») and §ו are out."""
    h = harvest('flood', '1945')
    secs = []

    # §א — scan header: א. שאלות מבנה וסגנון. Her pointers [2]–[6] (6:11–13, 6:22, 7:1, 7:5) are
    # verse text; they are the panel, not cards.
    secs.append({'id': prefix, 'title': {'en': '1945 · How the Flood Is Told'},
                 'primaryText': gen_6_22_7_16(), 'steps': [
        narration(f'{prefix}-intro', 'The end of chapter 6, and chapter 7: Noah does as he is commanded.'),
        question(f'{prefix}-q-a1', h, 1, '1. Try to explain why Scripture changed, in our chapter, from the '
                 'previous chapter.', highlight=['tziva-e', 'vayomer-h', 'tziva-h']),
        question(f'{prefix}-q-a2', h, 7, '2. And why did it change again in our chapter, verse 16: “as God '
                 'commanded him”?', highlight=['tziva-h', 'tziva-16']),
    ]})

    secs.append({'id': f'{prefix}-order', 'titleCard': False, 'title': {'en': 'Beasts, Cattle, Birds'},
                 'primaryText': gen_7_14_21_23(), 'steps': [
        narration(f'{prefix}-order-intro', 'Those who go into the ark, and those who perish.'),
        # Her verse number reads «י"ז[?]» on the scan; the digitizer linked 7:14, where the birds do
        # come last (see flood.md).
        question(f'{prefix}-q-a3', h, 9, 'Why does Scripture mention the birds at the end, not in the order '
                 'of their creation in chapter 1:20–25?', highlight=['list-14', 'of-14']),
        question(f'{prefix}-q-a4', h, 10, 'Explain the different order in the following verses:',
                 highlight=['list-21', 'list-23']),
    ]})

    secs.append({'id': f'{prefix}-forty', 'titleCard': False, 'title': {'en': 'The Waters Swelled'},
                 'primaryText': gen_7_17_20(), 'steps': [
        narration(f'{prefix}-forty-intro', 'The forty days of the Flood.'),
        question(f'{prefix}-q-a5-lead', h, 14, 'Note the description.',
                 highlight=['yirbu-17', 'yigberu-18', 'gavru-19', 'gavru-20']),
        question(f'{prefix}-q-a5a', h, 15, 'In how many stages is the flooding of the earth described in these '
                 'verses, over the forty days?', highlight=['yirbu-17', 'yigberu-18', 'gavru-19', 'gavru-20']),
        question(f'{prefix}-q-a5b', h, 16, 'What is the difference between the two verbs mentioned in the '
                 'verses: r-b-h (rabah) – g-b-r (gavar)?', highlight=['yirbu-17', 'yigberu-18']),
        commentary(f'{prefix}-ramban-a', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   'And the sense of “va-yigberu ha-mayim” [the waters prevailed] and “ve-ha-mayim gaveru”: that '
                   'they increased greatly; for great increase is called, in the language, gevurah [might]. And '
                   'so “and their transgressions, ki yitgabberu” (Job 36:9): they have increased greatly; “His '
                   'steadfast love gavar over those who fear Him” (Psalms 103:11): it is great; and so “or, '
                   'bi-gvurot, eighty years” (ibid. 90:10): in great increase.',
                   'ours', ref='Ramban on Genesis 7:18', stop='בריבוי גדול.',
                   highlight=['yigberu-18', 'gavru-19']),
        commentary(f'{prefix}-ramban-b', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   'And it may be that the sense of “va-yigberu” is that they came in a torrent, uprooting the '
                   'trees and toppling the buildings; for strength is called gevurah, because might lies in '
                   'strength. And so “they even grow mighty (gaveru) in power” (Job 21:7); “and he shall make '
                   'a firm (ve-higbir) covenant with many for one week” (Daniel 9:27): he will uphold it in '
                   'strength. And the language of the Sages (Ta’anit 2a), “the gevurot of the rains,” because '
                   'they come down with might. And it is possible that “or, bi-gvurot, eighty years” is from '
                   'this: that if his bones and body were strong and he is a man of strength, he will live '
                   'eighty. And if so, the meaning of “gaveru over the earth” will be that they were in all '
                   'their might, even over the high mountains, and swept them away.',
                   'ours', ref='Ramban on Genesis 7:18', start='וייתכן כי טעם',
                   highlight=['gavru-19', 'harim-19', 'gavru-20']),
        question(f'{prefix}-q-a5c', h, 18, 'Note his two interpretations!', highlight=['yigberu-18', 'gavru-19']),
    ]})

    secs.append({'id': f'{prefix}-perished', 'titleCard': False, 'title': {'en': 'All Flesh Perished'},
                 'primaryText': gen_7_21_24(), 'steps': [
        narration(f'{prefix}-perished-intro', 'All flesh perishes, and the waters swell a hundred and fifty days.'),
        question(f'{prefix}-q-a6', h, 20, 'By what literary means is the horrifying impression of total '
                 'annihilation created in the reader’s heart?',
                 highlight=['vayigva', 'kol-21', 'metu', 'vayimach', 'vayimachu', 'nishar']),
    ]})

    # §ב — scan header: ב. דור המבול («שאלות ברש"י» is the digitizer's). Her source line: Rashi on
    # 7:13 «בעצם»; 7:16 «ויסגר ה' בעדו» to «ופשוטו» (the digitized text ends there); and Rashi on
    # Ezekiel 14:14, sliced to the passage on Noah (the item also carries a printer's gloss).
    # §ה — scan header: ה. ט"ז ויסגר ה' בעדו. ע' ת"א נחלת יעקב, מלבי"ם.
    secs.append({'id': f'{prefix}-shut', 'titleCard': False, 'title': {'en': 'The Lord Shut Him In'},
                 'primaryText': gen_7_13_16(), 'steps': [
        narration(f'{prefix}-b-intro', 'Noah goes into the ark.'),
        commentary(f'{prefix}-b-rashi-13', h, 22, 'Rashi', 'רש"י', 'Rashi',
                   'Scripture teaches you that the people of his generation were saying: “If we see him going '
                   'into the ark, we will smash it and kill him.” The Holy One, blessed be He, said: “I will '
                   'bring him in before the eyes of them all, and we shall see whose word will stand.”',
                   'ours', ref='Rashi on Genesis 7:13:1', start='לימדך', highlight=['beetsem']),
        commentary(f'{prefix}-b-rashi-16', h, 23, 'Rashi', 'רש"י', 'Rashi',
                   'He shielded him, so that they would not smash it: He surrounded the ark with bears and '
                   'lions, and they were killing some of them.',
                   'ours', ref='Rashi on Genesis 7:16:1', start='הגין', highlight=['vayisgor']),
        commentary(f'{prefix}-b-rashi-ezek-a', h, 24, 'Rashi', 'רש"י', 'Rashi, on Ezekiel 14:14',
                   'Noah escaped from all three. From wild beasts: how do you know? When he went into the ark, '
                   'all the beasts sought to come in, and the Holy One, blessed be He, did not let them, as it '
                   'is written, “And the Lord shut him in” (Genesis 7). “Shut” is said only of beasts, as it is '
                   'said, “and shut the lions’ mouths, and they did not harm me” (Daniel 7 [6:23]). A lion came '
                   'to go in, and its teeth were blunted; a bear came to go in, and its legs gave way, and so '
                   'on, in Bereshit Rabbah.',
                   'ours', ref='Rashi on Ezekiel 14:14:1', start='נח נמלט משלושתן',
                   stop='כו\' בבראשית רבה.', highlight=['vayisgor']),
        commentary(f'{prefix}-b-rashi-ezek-b', h, 24, 'Rashi', 'רש"י', 'Rashi, on Ezekiel 14:14',
                   'From the sword: this is the Flood. And moreover, his generation were seeking to set upon '
                   'him, and they were saying: “We will not let him go in.” But the Holy One, blessed be He, '
                   'saved him. The Holy One, blessed be He, said: “I will let him go in only at midday, and '
                   'whoever has the strength to stir, let him speak!” That is what is written, “In the very '
                   'same day Noah entered” (Genesis 7): in the very midst of the day…',
                   'ours', ref='Rashi on Ezekiel 14:14:1', start='מן החרב', highlight=['beetsem']),
        question(f'{prefix}-q-b1', h, 25, '1. Give a psychological explanation of the behavior of the generation '
                 'of the Flood as it is described in the midrash!'),
        question(f'{prefix}-q-b2', h, 26, '2. Try to explain: why did the Torah not describe at all the behavior '
                 'of the generation of the Flood when the punishment came?', highlight=['beetsem']),

        narration(f'{prefix}-h-intro', '“And the Lord shut him in.”', highlight=['vayisgor']),
        commentary(f'{prefix}-h-onkelos', h, 46, 'Onkelos', 'תרגום אונקלוס', 'Onkelos',
                   'And the Lord (by His Word) shielded him.',
                   'ours', ref='Onkelos Genesis 7:16', start='ואגן', highlight=['vayisgor']),
        commentary(f'{prefix}-h-malbim', h, 47, 'Malbim', 'מלבי"ם', 'Malbim',
                   'And from then on they were as though they had gone out of the old world, on which '
                   'destruction had been decreed; they were outside the world, destined to travel on the face '
                   'of the waters, and shut in by the Lord’s providence, so that the destroyer would not come '
                   'near them. And of this it says, “And the Lord shut him in”: this is the individual '
                   'providence that hovered over Noah.',
                   'ours', ref='Malbim on Genesis 7:16:1', highlight=['vayisgor']),
        commentary(f'{prefix}-h-nachalat', h, 48, 'Nachalat Yaakov', 'נחלת יעקב', 'Nachalat Yaakov',
                   'By His commanding him to make the ark and to go into it: that is His shutting him in.',
                   'ours', start='על ידי', highlight=['vayisgor']),
        question(f'{prefix}-q-h1', h, 49, '1. What difficulty do the three commentators face, and in what '
                 'direction does each try to resolve it, each in his own way?', highlight=['vayisgor']),
        commentary(f'{prefix}-h-ibn-ezra', h, 50, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the sense of “And the Lord shut him in” is for praise: the shutting, at this time, was '
                   'better than opening. At another time it is for disgrace: “He shuts in a man” (Job 12:14), '
                   '“and whom God has hedged in” (Job 3:23). And the evidence is the beginning of the verse. '
                   'And so, he shut the door, and the Lord helped him so that no place in the ark opened; for '
                   'at once they would all have died.',
                   'ours', ref='Ibn Ezra on Genesis 7:16', start='וטעם "ויסגור', stop='כולם מתים',
                   highlight=['habaim', 'vayisgor'], effect='glow'),
        question(f'{prefix}-q-h2', h, 'after 50', '2. In what does Ibn Ezra (on verse 16, s.v. “And they that '
                 'entered, male and female,” from “And the sense of ‘And the Lord shut him in’” to “they would '
                 'all have died”) differ from them?', highlight=['vayisgor']),
    ]})
    return secs


# ─── 1952 ───────────────────────────────────────────────────────────────────

def leaf_1952(prefix='fl-1952'):
    """Gilayon תשי"ב (161472): §א, §ב, §ג — all of her sections (pack §7)."""
    h = harvest('flood', '1952')
    secs = []

    # §א — scan header: א. א ויזכור אלוהים את נח ואת כל החיה ואת כל הבהמה אשר אתו בתיבה.
    # Her sub-questions are lettered (א)–(ד); the harvest keeps «א.»–«ד.», rendered "a."–"d.".
    secs.append({'id': prefix, 'title': {'en': '1952 · God Remembered Noah'},
                 'primaryText': gen_8_1(), 'steps': [
        narration(f'{prefix}-intro', 'The waters have covered the earth a hundred and fifty days.'),
        commentary(f'{prefix}-rashi', h, 3, 'Rashi', 'רש"י', 'Rashi',
                   'What did He remember for them, for the cattle? The merit that they had not corrupted their '
                   'way before that, and that they did not mate in the ark.',
                   'ours', ref='Rashi on Genesis 8:1:2', start='מה זכר', highlight=['vayizkor', 'chaya']),
        commentary(f'{prefix}-ramban', h, 4, 'Ramban', 'רמב"ן', 'Ramban',
                   'But the remembering it speaks of with the beasts and the cattle is not by merit, for in '
                   'living creatures there is no merit or guilt, except in man alone. Rather, the remembering '
                   'in them is that He remembered His holy word, by which He spoke and the world came to be; '
                   'and the will He had in creating the world came up before Him, and He desired the world’s '
                   'continuance in the kinds He had created in it. And so He saw fit now to bring them out, so '
                   'that they would not perish in the ark.',
                   'ours', ref='Ramban on Genesis 8:1:1', start='אבל הזכירה', stop='שלא יכלו בתיבה',
                   highlight=['chaya']),
        question(f'{prefix}-q-a-a', h, 5, 'a. What is the difficulty that both of them wanted to resolve?',
                 highlight=['vayizkor', 'chaya']),
        question(f'{prefix}-q-a-b', h, 6, 'b. What is the difference between the two interpretations?'),
        question(f'{prefix}-q-a-c', h, 7, 'c. Find another verse in our parasha (in chapter 6) in whose '
                 'interpretation, too, we find the same difference in principle between Rashi and Ramban that '
                 'we find here.'),
        question(f'{prefix}-q-a-d', h, 8, 'd. Can you find a different answer to their question (a) with the help '
                 'of the following verses: Psalms 36:7; Psalms 145:9; Jonah, the end of chapter 4?'),
        commentary(f'{prefix}-ibn-ezra', h, 9, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'A general term, for the beasts of the field, and the birds of the sky, and every creeping '
                   'thing on the earth.',
                   'ours', ref='Ibn Ezra on Genesis 8:1:2', start='כלל', highlight=['chaya']),
        question(f'{prefix}-q-ie-a', h, 10, 'a. What is difficult for him?', highlight=['chaya']),
        question(f'{prefix}-q-ie-b', h, 11, 'b. What is the weakness of his interpretation?'),
    ]})

    # §ב — scan header: ב. [?]רי המדרשים: («היציאה מן התיבה» is the digitizer's).
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“Come Out of the Ark”'},
                 'primaryText': gen_8_5_9_15_16(), 'steps': [
        narration(f'{prefix}-b-intro', 'The dove goes out of the ark, and comes back.'),
        # Her citation is «ל"ג ח'»; the triaged ref is 33:6.
        commentary(f'{prefix}-br', h, 14, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Yehudah son of R. Nachman said in the name of R. Shimon: Had she found rest, she would '
                   'not have come back. And likewise (= and similarly): (Lamentations 1) “She dwells among the '
                   'nations, she has found no rest”: had she found rest, they would not have come back. And '
                   'likewise: (Deuteronomy 28) “Among those nations you shall find no peace, and there shall '
                   'be no rest for the sole of your foot”: so, had they found rest, they would not have come '
                   'back.',
                   'ours', ref='Bereshit Rabbah 33:6', highlight=['manoach', 'vatashov']),
        question(f'{prefix}-q-b-a', h, 15, 'a. Explain: what symbolic meaning do the Sages give here to the '
                 'dove’s flight and its return to the ark?', highlight=['manoach', 'vatashov']),
        question(f'{prefix}-q-b-b', h, 16, 'b. Bring examples of this idea from the sources of our people.'),
        narration(f'{prefix}-tzei', '“Come out of the ark.”', highlight=['vaydaber', 'tzei']),
        commentary(f'{prefix}-aggadat', h, 18, 'Aggadat Bereshit', 'אגדת בראשית', 'Aggadat Bereshit',
                   '“Come out of the ark.” This is what Scripture says (Ecclesiastes 8): “I [say]: keep the '
                   'king’s command.” When Noah went into the ark, he went in by permission of the Holy One, '
                   'blessed be He, as it is said (7): “And the Lord said to Noah: Go into the ark, you and all '
                   'your household.” Once the earth had dried and the ark had come to rest on the mountains of '
                   'Ararat, his sons said to him: “Let us go out of here.” He said to them: “Heaven forbid! By '
                   'permission of the Holy One, blessed be He, we went in, and by His permission we go out.” '
                   'As soon as the Holy One, blessed be He, heard this, at once: “And God spoke to Noah: Come '
                   'out of the ark…” That is why it is said: “I [say]: keep the king’s command.”',
                   'ours', ref='Aggadat Bereshit 7:1', start='"צא מן התבה"', highlight=['vaydaber', 'tzei']),
        commentary(f'{prefix}-tanchuma', h, 20, 'Tanchuma', 'תנחומא ישן', 'Tanchuma Yashan',
                   '“In the tenth month, on the first of the month, the tops of the mountains became visible”: '
                   'and he did not go out of there, but waited in the ark, so as to be given permission. The '
                   'Holy One, blessed be He, said to him: “Is it permission you are asking for? Come out of the '
                   'ark!” R. Yehudah bar Il’ai said: Had I been there, I would have broken the ark and gone out '
                   'of there.',
                   'ours', start='"בעשירי', highlight=['niru', 'tzei'], effect='glow'),
        question(f'{prefix}-q-b2-a', h, 21, 'a. What is the difference in principle between the two outlooks '
                 'expressed in these two midrashim?', highlight=['tzei']),
        question(f'{prefix}-q-b2-b', h, 22, 'b. What is symbolized by Noah’s sons, and by their claim, in the '
                 'midrash Aggadat Bereshit?'),
        question(f'{prefix}-q-b2-c', h, 23, 'c. Do you know midrashim and sayings of the Sages that also give '
                 'expression to the outlook contained in the words of the Tanchuma above?'),
    ]})

    # §ג — scan header: ג שאלות סגנון ולשון. The bare «השוה:» leads [25], [34] and the lemma [29] are
    # carried by the highlights; [33] (pointers to two other gilyonot) is left out.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': 'The Raven and the Dove'},
                 'primaryText': gen_8_7_8_13_14(), 'steps': [
        narration(f'{prefix}-c-intro', 'Noah sends out the raven, then the dove.'),
        question(f'{prefix}-q-c1', h, 28, 'Explain the reason for the change in style.',
                 highlight=['orev', 'yona']),
        question(f'{prefix}-q-c2', h, 30, 'Explain why the Torah did not use here the language of the qal, '
                 '“va-yishlach,” instead of the pi’el, since “every expression of the sending of messengers” '
                 'is said in the qal. And so Genesis 32:4; 37:13–14; 46:28.', highlight=['yona']),
        commentary(f'{prefix}-c-rashbam', h, 31, 'Rashbam', 'רשב"ם', 'Rashbam, on Genesis 19:13',
                   'The heavy (dagesh) form. And although every sending of messengers who come back is written '
                   '“va-yishlach,” in the light (rafe) form, it is written as if in the heavy form, because it '
                   'is a sending-forth to destroy, as it is written, “and the teeth of beasts I will send '
                   '(ashallach) against them”; “He sends (yeshallach) against them swarms of insects.”',
                   'ours', ref='Rashbam on Genesis 19:13:1', start='משקל דגש'),
        question(f'{prefix}-q-c2-rashi', h, 32, 'Use, in your answer, the words of Rashi here:',
                 stop='כאן:', highlight=['yona']),
        commentary(f'{prefix}-c-rashi', h, 32, 'Rashi', 'רש"י', 'Rashi',
                   'This is not a term of sending on an errand, but of sending off: he let her go on her way, '
                   'and by this he would see whether the waters had abated; for if she found a resting place, '
                   'she would not come back to him.',
                   'ours', ref='Rashi on Genesis 8:8:2', start='אין זה', highlight=['yona'], effect='glow'),
        question(f'{prefix}-q-c3', h, 37, 'What is the difference between the two expressions?',
                 highlight=['charvu', 'yavsha']),
    ]})
    return secs


# ─── 1962 ───────────────────────────────────────────────────────────────────

def leaf_1962(prefix='fl-1962'):
    """Gilayon תשכ"ב (160700): §א, §ב, §ד (pack §7). §ג (Ibn Kaspi on «עד») is out."""
    h = harvest('flood', '1962')
    secs = []

    # §א — scan header: א. ז' כ"ד ויגברו המים על הארץ חמשים ומאת יום. / ח' א ויזכר אלוקים את נח
    # §ב — scan header: ב. ח' א' ויזכר אלוקים את נח ואת כל החיה ואת כל הבהמה אשר אתו בתיבה.
    secs.append({'id': prefix, 'title': {'en': '1962 · A Hundred and Fifty Days'},
                 'primaryText': gen_7_24_8_2(), 'steps': [
        narration(f'{prefix}-intro', 'The end of chapter 7, and the start of chapter 8.'),
        commentary(f'{prefix}-ibn-ezra', h, 3, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“And the waters prevailed a hundred and fifty days”: because the fountains had burst '
                   'apart; and also rain was falling one day and stopping one day. For the meaning of “I will '
                   'make it rain upon the earth…” (7:4) is: constantly, without a break; and the evidence is '
                   'that it says “and the rain was held back” (8:2).',
                   'ours', ref='Ibn Ezra on Genesis 7:24', start='ויגברו המים חמשים',
                   highlight=['yigberu', 'vayikale']),
        commentary(f'{prefix}-wessely', h, 4, 'Wessely', 'ר\' נפתלי הירץ ויזל',
                   'R. Naftali Hirz Wessely, Imrei Shefer',
                   'The listener supposes that at the end of a hundred and fifty days God remembered Noah and '
                   'those with him in the ark, and made a wind pass, and stilled the might of the waters, and '
                   'then the fountains of the deep were closed and the rain from the sky ended… But the truth, '
                   'clear in my eyes, about the order of the verses is not so. Rather, having closed the story '
                   'of the Flood, how far the waters prevailed and how many days they stood in their might, it '
                   'goes on to tell in order the rescue of Noah and those with him in the ark, and how things '
                   'went on: the Flood stopped, and the waters lessened until the earth was dry. And it begins '
                   '“And God remembered Noah”; and this was at the end of the forty days in which the rain came '
                   'down and the waters prevailed fifteen cubits above all the high mountains, by means of '
                   'which He wiped out all existence, and none remained but Noah and those with him. Then He '
                   'remembered His holy word: to make an end of “the rains of His might” (Job 37:6), and He did '
                   'not want the waters to prevail and come down on the earth any more, to destroy it. And then '
                   '“God made a wind pass over the earth,” and this wind cleared the skies…',
                   'ours', start='השומע', highlight=['vayizkor', 'ruach', 'vayisachru']),
        commentary(f'{prefix}-cassuto-a', h, 5, 'Cassuto', 'קאסוטו', 'Cassuto, From Noah to Abraham',
                   '“And He remembered”: it is not meant that He remembered after those hundred and fifty days '
                   'spoken of in the previous verse had passed; for it is said afterwards (8:2), “The fountains '
                   'of the deep and the floodgates of the sky were stopped up, and the rain was held back,” and '
                   'this belongs, of course, to the end of the forty days of the rain’s falling.',
                   'ours', start='ד"ה ויזכור', stop='של ירידת הגשם.',
                   highlight=['vayizkor', 'vayisachru', 'vayikale']),
        commentary(f'{prefix}-cassuto-b', h, 5, 'Cassuto', 'קאסוטו', 'Cassuto, From Noah to Abraham',
                   'Reading these verbs (“va-yizkor,” “va-yissakheru,” “va-yikkale”) as a pluperfect (“He had '
                   'already remembered before,” “they had already been stopped up before”…) is certainly not '
                   'right, and does not suit the nature of the Hebrew language, as we have already seen… Here '
                   'one must interpret on the pattern of the interpretation we have already proposed for the '
                   'relation between the account of creation (Genesis 1:1–2:3 [printed as 6:1]) and the '
                   'account of the garden of Eden (Genesis 2:4–3:24): the subject of the previous paragraph is '
                   'the prevailing of the waters over the earth, and it is told in that paragraph to its end; '
                   'whereas this new paragraph deals with another matter, the beginning of the rescue of the '
                   'remnant that escaped, and begins to tell it from its beginning, although its beginning '
                   'comes earlier in time than the end of the subject told above.',
                   'ours', start='הפירוש של פעלים', highlight=['yigberu', 'vayizkor'], effect='glow'),
        question(f'{prefix}-q-a1', h, 6, '1. What is the difficulty in the verses of our chapters (chapters 7–8) '
                 'that the three commentators wanted to resolve?', highlight=['yigberu', 'vayizkor']),
        question(f'{prefix}-q-a2', h, 7, '2. Are there in their words three different resolutions of the '
                 'difficulty, or two?'),
        question(f'{prefix}-q-a3', h, 8, '3. How is the word “va-yigberu” at the end of chapter 7 interpreted '
                 'according to each of the three?', highlight=['yigberu']),
        question(f'{prefix}-q-a4', h, 9, '4. In Ibn Ezra’s view, what does verse 2 of chapter 8 attest?',
                 highlight=['vayisachru', 'vayikale']),
        question(f'{prefix}-q-a5', h, 10, '5. What is the likeness, in Cassuto’s view, between the relation of '
                 'chapter 1 of Genesis to chapter 2 and the relation of what is told in our parasha in '
                 'chapter 7 to chapter 8?'),
        question(f'{prefix}-q-a6', h, 11, '6. Where in Parashat Bereshit did we find such a relation between two '
                 'chapters again?'),
        question(f'{prefix}-q-a7', h, 12, '7. Against the method of which commentator are Cassuto’s words '
                 'directed, in the paragraph “Reading these verbs as a pluperfect…”, and how can one prove '
                 'that this interpretation does not suit the nature of the Hebrew language?'),

        narration(f'{prefix}-b-intro', '“God remembered Noah and all the beasts and all the cattle.”',
                  highlight=['vayizkor', 'chaya']),
        commentary(f'{prefix}-b-ibn-ezra', h, 17, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra, in his other commentary',
                   'Far be it that there be forgetting for the least of the ministering angels, all the more so '
                   'for the Maker of all, before whom there is no forgetting. And so the poet said (Psalms '
                   '94:9): “He who plants the ear, shall He not hear?” Rather, Scripture speaks so when the '
                   'Lord’s goodness is seen on the earth: for the remembrance of the good He did him came '
                   'before the Lord.',
                   'ours', start='חלילה', highlight=['vayizkor']),
        commentary(f'{prefix}-b-ramban', h, 18, 'Ramban', 'רמב"ן', 'Ramban',
                   'The remembering of Noah is because he was a righteous man, wholehearted, and He had made a '
                   'covenant with him to save him; and “Noah” includes his offspring who were with him there, '
                   'and it did not mention them because they were saved by his merit. But the remembering it '
                   'speaks of with the beasts and the cattle is not by merit, for in living creatures there is '
                   'no merit or guilt, except in man alone. Rather, the remembering in them is that He '
                   'remembered His holy word, by which He spoke and the world came to be; and the will He had '
                   'in creating the world came up before Him, and He desired the world’s continuance in the way '
                   'He had created it. And so He saw fit now to bring them out, so that they would not perish '
                   'in the ark. And it did not mention the birds and the creeping things, because the '
                   'remembering of the beasts is the same as theirs, and the one speaks for the other.',
                   'ours', ref='Ramban on Genesis 8:1:1', start='הזכירה בנח', highlight=['vayizkor', 'chaya']),
        commentary(f'{prefix}-b-bahya', h, 19, 'Rabbeinu Bahya', 'רבנו בחיי', 'Rabbeinu Bahya',
                   'To teach that all of them are equal under the general providence.',
                   'ours', ref='Rabbeinu Bahya, Bereshit 8:1:1', start='להורות', highlight=['chaya']),
        commentary(f'{prefix}-b-kaspi', h, 20, 'Ibn Kaspi', 'ר\' יוסף אבן כספי',
                   'R. Yosef Ibn Kaspi, Mitzref la-Kesef',
                   'Far be it that the Lord’s remembering of Noah, the righteous man, and His remembering, '
                   'blessed be He, of the beasts and the cattle, should be on one level. For this too we need '
                   'understanding, that is, logic. And more forcefully than this, it says further, of the '
                   'beasts and the cattle, “making a covenant”; and all this is plain to those who have eyes.',
                   'ours', start='חלילה שיהיה', highlight=['vayizkor', 'chaya']),
        commentary(f'{prefix}-b-cassuto', h, 21, 'Cassuto', 'קאסוטו', 'Cassuto, From Noah to Abraham',
                   'This remembering is like what is written below of Sarah (Genesis 21): “The Lord took note '
                   'of Sarah as He had said, and the Lord did for Sarah as He had spoken… at the set time of '
                   'which God had spoken to him.” Taking note here means doing, as comes out clearly from the '
                   'parallel “took note – did”; and specifically doing at a time fixed in advance. And the '
                   'same holds for the remembering of Noah, for taking note and remembering are synonymous '
                   'concepts: as the Lord had announced to Noah in advance, so He did. He had told him that the '
                   'Flood would come down for forty days, and at the end of forty days He put an end to the '
                   'falling of the waters of the Flood.',
                   'ours', start='זכירה זו', highlight=['vayizkor', 'vayikale'], effect='glow'),
        question(f'{prefix}-q-b', h, 22, 'What are the difficulties that each of the commentators above '
                 'resolves?', highlight=['vayizkor', 'chaya']),
    ]})

    # §ד — scan header: ד. מדברי המדרשים: («קרבן נח» is the digitizer's). The scan prints the blocks
    # 2) [32]–[35], 3) [36]–[39], then 1) [28]–[31] last; rendered in that order.
    secs.append({'id': f'{prefix}-d', 'titleCard': False, 'title': {'en': 'Noah’s Offering'},
                 'primaryText': gen_8_16_20_21(), 'steps': [
        narration(f'{prefix}-d-intro', 'Noah comes out of the ark, builds an altar, and offers.'),
        question(f'{prefix}-q-d2', h, 32, '2) Compare the two following midrashim:',
                 highlight=['vayiven', 'olot']),
        commentary(f'{prefix}-br-34-9a', h, 33, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“Va-yiven” [and he built] is written: nitbonen [he considered]. He said: Why did the Holy '
                   'One, blessed be He, command me, and make the pure ones more than the impure? Only so as to '
                   'bring an offering from them. At once: “and he took of every pure animal and of every pure '
                   'bird…”',
                   'ours', ref='Bereshit Rabbah 34:9', start='"ויבן" כתיב', highlight=['vayiven', 'tehorim']),
        commentary(f'{prefix}-pdre', h, 34, 'Pirkei DeRabbi Eliezer', 'פרקי דר\' אליעזר',
                   'Pirkei DeRabbi Eliezer',
                   'Noah sat and searched in his heart and said: The Holy One, blessed be He, saved me from the '
                   'waters of the Flood and brought me out of that prison, and am I not obliged to bring burnt '
                   'offerings before Him? At once Noah brought of the kinds of pure cattle, ox and sheep and '
                   'goat, and of the kinds of pure bird, turtledoves and young pigeons… And he built the first '
                   'altar, on which Cain and Abel had offered burnt offerings.',
                   'ours', ref='Pirkei DeRabbi Eliezer 23', start='ישב נח', highlight=['tehorim', 'olot']),
        question(f'{prefix}-q-d2-q', h, 35, 'What is the difference between the two midrashim in how they '
                 'understand the burnt offering that Noah offered?', highlight=['olot']),
        commentary(f'{prefix}-br-34-9b', h, 36, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And the Lord smelled the pleasing odor”: He smelled the fragrance of Abraham our father '
                   'coming up from the fiery furnace; and He smelled the fragrance of Hananiah, Mishael and '
                   'Azariah coming up from the fiery furnace. A parable of a king’s friend who honored him and '
                   'sent him a fine gift, a fine platter; and his son arose and did not honor him; his grandson '
                   'arose and honored him. He said to him: “How like your gift is to your grandfather’s gift!” '
                   '“And the Lord smelled the pleasing odor”: He smelled the fragrance of the gift of the '
                   'persecution.',
                   'ours', ref='Bereshit Rabbah 34:9', start='"וירח ה\'', highlight=['vayarach'], effect='glow'),
        question(f'{prefix}-q-d3a', h, 37, 'a. What is the meaning of “korban” [offering] according to this '
                 'midrash?', highlight=['vayarach']),
        question(f'{prefix}-q-d3b', h, 38, 'b. What is the sense of the parable of the father, his son, and his '
                 'grandson?'),
        question(f'{prefix}-q-d3c', h, 39, 'c. What is the difficulty in our verse on which the midrash is built?',
                 highlight=['vayarach']),
        # Her citation is «ל"ד (ד'[?])», smudged; the triaged ref is 34:6.
        commentary(f'{prefix}-br-34-6', h, 28, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“Come out of the ark.” It is written (Ecclesiastes 3): “A season is set for everything, a '
                   'time for every experience under heaven.” There was a time for Noah to go into the ark, as '
                   'it is said, “Go into the ark, you and all your household,” and there was a time for him to '
                   'go out of it, as it is said, “Come out of the ark.” A parable of a parnas [a community '
                   'leader] who went away from the place and seated another in his stead. When he came back, '
                   'he said to him: “Leave your place.” So Noah: “Come out of the ark,” and he would not '
                   'accept going out. He said: Shall I go out and be fruitful and multiply for a curse? — until '
                   'the Omnipresent swore to him that He would not bring a flood on the world, as it is said '
                   '(Isaiah 54): “For this is to Me like the waters of Noah: as I swore that the waters of '
                   'Noah would never again pass.”',
                   'ours', ref='Bereshit Rabbah 34:6', start='"צא מן התיבה", כתיב', highlight=['tzei']),
        question(f'{prefix}-q-d1a', h, 29, 'a. What hint did the midrash find in the verses for this refusal of '
                 'Noah’s?', highlight=['tzei']),
        question(f'{prefix}-q-d1b', h, 30, 'b. What support did the midrash find for its words in Isaiah 54? Use '
                 'Isaiah 48!'),
        question(f'{prefix}-q-d1c', h, 31, 'c. Why did the midrash choose a “parnas” for its parable?'),
    ]})
    return secs
