from noach_lib import *  # noqa: F401,F403
"""Theme 4 — Your lifeblood (Gen 9:1–7): leaves 1948, 1957, 1970.

Paper trail: research/parshiyot/noach-leaves/blood.md (slices, omissions, open items).
"""


def underline_every(he, span, n):
    """Underline each of the `n` occurrences of `span` (nechama_lib.underline marks only the first)."""
    assert he.count(span) == n, f'{span!r} occurs {he.count(span)}x, expected {n}'
    return he.replace(span, f'<u>{span}</u>')


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_9_5_6():
    return primary('Genesis 9:5-6', ['9:5', '9:6'], {
        'damchem': ('ואך את דמכם לנפשתיכם אדרש', 'But for your own life-blood I will require a reckoning'),
        'chaya': ('מיד כל חיה אדרשנו', 'I will require it of every animal'),
        'haadam': ('ומיד האדם', 'of humankind, too'),
        'nefesh': ('אדרש את נפש האדם', 'will I require a reckoning for human life'),
        'achiv': ('מיד איש אחיו', 'of everyone for each other'),
        'shofech': ('שפך דם האדם באדם דמו ישפך', 'Whoever sheds human blood, By human [hands] shall their blood be shed'),
        'tzelem': ('כי בצלם אלהים עשה את האדם', 'For in the image of God Was humankind made'),
    })


def gen_9_4_6():
    return primary('Genesis 9:4-6', ['9:4', '9:5', '9:6'], {
        'basar': ('אך בשר בנפשו דמו לא תאכלו', 'You must not, however, eat flesh with its life-blood in it'),
        'damchem': ('ואך את דמכם לנפשתיכם אדרש', 'But for your own life-blood I will require a reckoning'),
        'chaya': ('מיד כל חיה אדרשנו', 'I will require it of every animal'),
        'haadam': ('ומיד האדם', 'of humankind, too'),
        'nefesh': ('אדרש את נפש האדם', 'will I require a reckoning for human life'),
        'achiv': ('מיד איש אחיו', 'of everyone for each other'),
        'shofech': ('שפך דם האדם', 'Whoever sheds human blood'),
        'baadam': ('באדם דמו ישפך', 'By human [hands] shall their blood be shed'),
        'tzelem': ('כי בצלם אלהים עשה את האדם', 'For in the image of God Was humankind made'),
    })


def gen_9_6():
    return primary('Genesis 9:6', ['9:6'], {
        'shofech': ('שפך דם האדם', 'Whoever sheds human blood'),
        'baadam': ('באדם', 'By human [hands]'),
        'damo': ('דמו ישפך', 'shall their blood be shed'),
        'tzelem': ('כי בצלם אלהים', 'For in the image of God'),
        'asa': ('עשה את האדם', 'Was humankind made'),
    })


def _sides(left_keys, right_keys, left_spec, right_spec, ref, lref, rref):
    lhe, len_ = verse_set(left_keys)
    rhe, ren = verse_set(right_keys)
    left = words(lhe, len_, left_spec)
    right = words(rhe, ren, right_spec)
    for w in left.values():
        w['side'] = 'left'
    for w in right.values():
        w['side'] = 'right'
    return {'ref': ref, 'mode': 'comparison',
            'left': {'ref': lref, 'he': lhe, 'en': len_},
            'right': {'ref': rref, 'he': rhe, 'en': ren},
            # right side first: 1970's 'pru-a' (1:28) must wrap before its prefix 'pru-n' (9:1)
            'words': {**right, **left}}


def _frag(key, letters, en):
    """A pointed fragment of verse `key` found by its bare letters, with English that must occur
    verbatim in the cached English (verse text is never typed)."""
    assert en in VERSES[key]['en'], f'{en!r} not in the English of {key}'
    return vp(VERSES[key]['he'], letters), en


def _frag_sides(left_frags, right_frags, left_spec, right_spec, ref, lref, rref):
    join = lambda fs: (' … '.join(f[0] for f in fs), ' … '.join(f[1] for f in fs))
    (lhe, len_), (rhe, ren) = join(left_frags), join(right_frags)
    left, right = words(lhe, len_, left_spec), words(rhe, ren, right_spec)
    for w in left.values():
        w['side'] = 'left'
    for w in right.values():
        w['side'] = 'right'
    return {'ref': ref, 'mode': 'comparison',
            'left': {'ref': lref, 'he': lhe, 'en': len_},
            'right': {'ref': rref, 'he': rhe, 'en': ren},
            # right side first: 1970's 'pru-a' (1:28) must wrap before its prefix 'pru-n' (9:1)
            'words': {**right, **left}}


def comparison_1948():
    """1948 §ב (no table): her question names Noah's sons first, so Noah (9:2–3) is on the right and
    Adam (1:28–29) on the left. She cites the whole of 9:1–3 and 1:28–30; the panel keeps the
    phrases about the animals, which her question asks about, so it fits a phone."""
    return _frag_sides([
        _frag('1:28', 'ורדו בדגת הים ובעוף השמים ובכל חיה הרמשת על הארץ',
              'rule the fish of the sea, the birds of the sky, and all the living things that creep on earth'),
        _frag('1:29', 'הנה נתתי לכם את כל עשב זרע זרע', 'See, I give you every seed-bearing plant'),
    ], [
        _frag('9:2', 'ומוראכם וחתכם יהיה על כל חית הארץ',
              'The fear and the dread of you shall be upon all the animals of the earth'),
        _frag('9:2', 'בידכם נתנו', 'they are given into your hand'),
        _frag('9:3', 'כל רמש אשר הוא חי לכם יהיה לאכלה', 'Every creature that lives shall be yours to eat'),
    ], {
        'urdu': ('ורדו בדגת הים', 'rule the fish of the sea'),
        'esev': ('הנה נתתי לכם את כל עשב זרע זרע', 'See, I give you every seed-bearing plant'),
    }, {
        'mora': ('ומוראכם וחתכם', 'The fear and the dread of you'),
        'beyedchem': ('בידכם נתנו', 'they are given into your hand'),
        'remes': ('כל רמש אשר הוא חי לכם יהיה לאכלה', 'Every creature that lives shall be yours to eat'),
    }, 'Genesis 9:2-3; 1:28-29', 'Genesis 1:28-29', 'Genesis 9:2-3')


def comparison_1957():
    """1957 §א: her table, the blessing to Adam (1:28, first row; right) and to Noah (9:2; left)."""
    return _sides(['9:2'], ['1:28'], {
        'mora': ('ומוראכם וחתכם יהיה', 'The fear and the dread of you shall be'),
        'n-chaya': ('על כל חית הארץ', 'upon all the animals of the earth'),
        'n-birds': ('ועל כל עוף השמים', 'upon all the birds of the sky'),
        'n-remes': ('בכל אשר תרמש האדמה', 'everything with which the earth is astir'),
        'n-fish': ('ובכל דגי הים', 'upon all the fish of the sea'),
    }, {
        'a-fish': ('ורדו בדגת הים', 'rule the fish of the sea'),
        'a-birds': ('ובעוף השמים', 'the birds of the sky, and'),
        'a-chaya': ('ובכל חיה הרמשת על הארץ', 'all the living things that creep on earth'),
    }, 'Genesis 1:28; 9:2', 'Genesis 9:2', 'Genesis 1:28')


def comparison_1970():
    """1970 §א: her table, «לאדם» on the right, «לנח» on the left. Her table quotes 1:28–30 and 9:1–4;
    the panel keeps the rows the cards point at, as fragments, so it fits a phone (9:4 has its own
    panel next)."""
    return _frag_sides([
        _frag('9:1', 'פרו ורבו ומלאו את הארץ', 'Be fertile and increase, and fill the earth'),
        _frag('9:2', 'ומוראכם וחתכם יהיה על כל חית הארץ',
              'The fear and the dread of you shall be upon all the animals of the earth'),
        _frag('9:3', 'כל רמש אשר הוא חי לכם יהיה לאכלה', 'Every creature that lives shall be yours to eat'),
    ], [
        _frag('1:28', 'פרו ורבו ומלאו את הארץ וכבשה ורדו בדגת הים',
              'Be fertile and increase, fill the earth and master it; and rule the fish of the sea'),
        _frag('1:29', 'הנה נתתי לכם את כל עשב זרע זרע', 'See, I give you every seed-bearing plant'),
    ], {
        'pru-n': ('פרו ורבו ומלאו את הארץ', 'Be fertile and increase, and fill the earth'),
        'mora': ('ומוראכם וחתכם', 'The fear and the dread of you'),
        'remes': ('כל רמש אשר הוא חי לכם יהיה לאכלה', 'Every creature that lives shall be yours to eat'),
    }, {
        'pru-a': ('פרו ורבו ומלאו את הארץ וכבשה', 'Be fertile and increase, fill the earth and master it'),
        'urdu': ('ורדו בדגת הים', 'rule the fish of the sea'),
        'esev': ('הנה נתתי לכם את כל עשב זרע זרע', 'See, I give you every seed-bearing plant'),
    }, 'Genesis 1:28-29; 9:1-3', 'Genesis 9:1-3', 'Genesis 1:28-29')


# ─── 1948 ───────────────────────────────────────────────────────────────────

def leaf_1948(prefix='bl-1948'):
    """Gilayon תש"ח (161496): §א (one verse, her ten voices, Q1–4) and §ב (the two blessings)."""
    h = harvest('blood', '1948')
    secs = []

    # §א — scan header: א ה. אך את דמכם לנפשותיכם אדרש מיד כל חיה אדרשנו
    # Q3 follows Ralbag and Q4 Melekhet Machshevet, the sources they ask about; Q1 (what is the
    # problem?) and Q2 (sort them into groups) close the section.
    secs.append({'id': prefix, 'title': {'en': '1948 · Of Every Animal'},
                 'primaryText': gen_9_5_6(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 9:5–6. After the flood, God speaks of human blood.'),
        commentary(f'{prefix}-br', h, 3, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“Of every animal”: this is one who hands his fellow over to an animal to kill him.',
                   'ours', ref='Bereshit Rabbah 34:13', highlight=['chaya']),
        commentary(f'{prefix}-aggadah', h, 4, 'Midrash Aggadah', 'מדרש אגדה', 'Midrash Aggadah',
                   'That if the animals kill him — for instance, a lion or a snake mauled him and killed '
                   'him — I will require and claim his blood from the animals.',
                   'ours', start='שאם', highlight=['chaya']),
        commentary(f'{prefix}-rashi', h, 5, 'Rashi', 'רש"י', 'Rashi',
                   '“Of every animal”: Because the generation of the flood sinned, and were abandoned as '
                   'food for evil beasts, to rule over them, as it is said (Psalms 49:13), “ruled over like '
                   'the beasts, they perish” — therefore it was necessary to warn the animals concerning them.',
                   'ours', ref='Rashi on Genesis 9:5:3', highlight=['chaya']),
        commentary(f'{prefix}-rambam', h, 6, 'Rambam', 'רמב"ם, הלכות רוצח', 'Rambam, Hilkhot Rotze’ach',
                   'But one who hires a killer to kill his fellow… or who bound him and left him before a '
                   'lion or the like, and the beast killed him; and likewise one who kills himself — each of '
                   'these is a shedder of blood, and the sin of murder is in his hand, and he is liable to '
                   'death at the hands of Heaven; but there is no death by the court for them. And from where '
                   'do we know that this is the law? As it is said: “Whoever sheds the blood of man, by man '
                   'shall his blood be shed” — this is one who kills by his own hand, not through an agent; '
                   '“But your blood, of your lives, I will require” — this is one who kills himself; “of '
                   'every animal I will require it” — this is one who hands his fellow over before an animal '
                   'to devour him; “and of man, of every man’s brother, I will require the life of man” — '
                   'this is one who hires others to kill his fellow. And in all three the language of '
                   '“requiring” is used explicitly: their judgment is handed over to Heaven.',
                   'ours', start='אבל השוכר',
                   highlight=['shofech', 'damchem', 'chaya', 'haadam', 'achiv', 'nefesh']),
        commentary(f'{prefix}-moreh', h, 7, 'Rambam', 'רמב"ם, מורה נבוכים', 'Rambam, Moreh Nevukhim',
                   'However, this recompense for a non-speaking animal (which Rambam explained earlier that '
                   'some believe in) was never heard of at all in our faith before, and the sages of the '
                   'Talmud did not mention it at all. But some of the later Geonim, of blessed memory (some '
                   'say he means R. Saadia Gaon), when they heard it from the sect of the Mu’tazila (a Muslim '
                   'sect), it seemed right to them, and they believed it.',
                   'ours', start='אמנם זה הגמול', highlight=['chaya']),
        # Her start point «החל מן "ותמה אני"»; the digitized text reads «… תמה אני» (no ו).
        commentary(f'{prefix}-ramban-a', h, 8, 'Ramban', 'רמב"ן', 'Ramban',
                   'I wonder: if the requiring is in its plain sense, from the hand of the animal as from '
                   'the hand of man, to be a punishment in the matter — yet an animal has no understanding '
                   'to be punished or to receive reward. Perhaps it is so in the matter of human blood alone: '
                   'every animal that devours him shall be torn, for it is a king’s decree. And this is '
                   'the sense of “the ox shall surely be stoned, and its flesh shall not be eaten” (Exodus '
                   '21:28); and it is not to punish its owners with money, for even an ownerless ox is liable '
                   'to death (Bava Kamma 44b). And He commanded so for the children of Noah as for Israel.',
                   'ours', ref='Ramban on Genesis 9:5', start='תמה אני', highlight=['chaya']),
        commentary(f'{prefix}-ramban-b', h, 9, 'Ramban', 'רמב"ן', 'Ramban',
                   '“And the sense of ‘Whoever sheds the blood of man’”: every shedder, whether beast or '
                   'man — his blood is required, by the court and at the hands of Heaven. And it may be that '
                   'the sense of “of every animal” is that vengeance on the shedder of blood will come by the '
                   'hand of every animal, as in “for she has received of the Lord’s hand double for all her '
                   'sins” (Isaiah 40:2). And He said: But your blood I will require, and avenge it by the '
                   'hand of every animal, for I will send every beast of the earth against the murderer, and '
                   'I will send man against him too, and he will not be saved from their hand. And like it: '
                   '“because of all my adversaries I have become a reproach” (Psalms 31:12) — at their hand; '
                   '“this is the portion of a wicked man from God, and the heritage appointed him by God” '
                   '(Job 20:29).',
                   'ours', ref='Ramban on Genesis 9:5', stop='מאל (איוב כ\' כ"ט).',
                   highlight=['shofech', 'chaya']),
        commentary(f'{prefix}-ramban-c', h, 9, 'Ramban', 'רמב"ן', 'Ramban',
                   'Or perhaps the requiring from the hand of the animal is that it should not devour man, '
                   'for so He set it in their nature. And the secret of the matter: at the time of creation '
                   'He gave man every seed-bearing plant and every tree with seed-bearing fruit for food, and '
                   'He gave the animal every green plant for food; and Scripture said (above 1:30), “and it '
                   'was so,” for that is their nature and their custom. And now, when He said of man that he '
                   'would slaughter living creatures, and it was set in nature or in custom that living '
                   'creatures would be food for one another, He needed to command that the other living '
                   'creatures be prey for the teeth of human beings, and that they fear them and not devour '
                   'them. And He said “But your blood, of your lives,” to hint that He would not require the '
                   'blood of an animal from the hand of its fellow; so it remained with them to devour one '
                   'another. And this is the reason the prohibition of bloodshed is mentioned here: because of '
                   'the permission to slaughter, for the custom was to shed blood. For in the view of our '
                   'Rabbis (Sanhedrin 56b) Adam had already been warned about this; but because of slaughter '
                   'He needed to say: I have permitted you to shed the blood of every living thing except your '
                   'own blood, which shall be forbidden to you and to all living things, so that they have no '
                   'nature to shed it.',
                   'ours', ref='Ramban on Genesis 9:5', start='ואולי הדרישה', highlight=['damchem', 'chaya']),
        commentary(f'{prefix}-radak', h, 10, 'Radak', 'רד"ק', 'Radak',
                   'That He will give it into the hand of another animal to kill it, or into the hand of man. '
                   'And even though there is no reward and punishment for the other living creatures, only '
                   'for man, who possesses intellect, in a matter concerning man they have reward and '
                   'punishment, as it is said, “of every animal I will require it,” and it is said (Habakkuk '
                   '2), “and the destruction of beasts shall terrify them,” and it is said of reward (1 Kings '
                   '13), “and it had not broken the donkey.”',
                   'ours', ref='Radak on Genesis 9:5', highlight=['chaya']),
        commentary(f'{prefix}-ralbag', h, 11, 'Ralbag', 'רלב"ג', 'Ralbag',
                   'So that people should not think that, because the Lord, blessed be He, permitted them to '
                   'kill animals, the killing of human beings would be permitted them as well. Rather, the '
                   'Lord will punish them for this, and will make one of the beasts of prey the agent by which '
                   'the punishment reaches the one who kills his fellow.',
                   'ours', start='שלא יחשבו', highlight=['chaya']),
        question(f'{prefix}-q3', h, 16, '3. How does Ralbag explain the mem of “miyad kol chayah”?',
                 highlight=['chaya']),
        commentary(f'{prefix}-hefetz-a', h, 12, 'Melekhet Machshevet', 'ר\' משה חפץ, מלאכת מחשבת',
                   'R. Moshe Hefetz, Melekhet Machshevet',
                   'I am moved to protest against men who are “at peace with us,” of the children of Israel, '
                   'who are sorely afraid to say that the Lord, blessed be He, extends His providence over '
                   'every living thing, even those that are not human. Their only proof is that their '
                   'intellect cannot imagine that the Lord would lower His majesty to watch over a fly and a '
                   'creeping thing…',
                   'ours', start='ראיתי', stop='על זבוב ועל רמש...'),
        commentary(f'{prefix}-hefetz-b', h, 12, 'Melekhet Machshevet', 'ר\' משה חפץ, מלאכת מחשבת',
                   'R. Moshe Hefetz, Melekhet Machshevet',
                   '(He refutes this view at length, and concludes:) And it is right in my eyes that the '
                   'Lord, blessed be He, who lowers Himself to look upon heaven and earth, watches in His '
                   'might over all creatures, from the horns of wild oxen to the eggs of lice, and punishes '
                   'them if they sin with their limited sin; and if they do well, their reward is with them. '
                   'And the proofs from the words of the Sages are more than the locusts. I will dwell only on '
                   'proofs from the narratives of the Torah… “Of every animal I will require it”: these '
                   'words are as they are written and as they are worded, that the Lord will punish the '
                   'animal for the murder… And if the One higher than the high watches and looks upon our '
                   'lowliness — He who sits in heaven sees the children of men — why would He not watch over '
                   'animals? Is their worth as far from ours as we are from heaven? And how many of the '
                   'animals are more praiseworthy than some human beings?',
                   'ours', start='(מאריך', highlight=['chaya']),
        question(f'{prefix}-q4', h, 17, '4. Can you bring from our parasha further proof for the view of '
                 'the author of Melekhet Machshevet?'),
        commentary(f'{prefix}-wessely', h, 13, 'Wessely', 'ר\' נפתלי הרץ ויזל', 'R. Naftali Herz Wessely',
                   'I think that the word chayah in this verse is not an evil beast or a beast of the field, '
                   'but the human soul, for it is called chayah in Scripture, as (Psalms 143) “he has crushed '
                   'my life (chayati) to the ground,” (Psalms 74) “do not forget the life (chayat) of Your poor '
                   'forever”… For the name chayah for the human soul is a precious title: it indicates that it '
                   'is alive outside the body, and that it has the power to cleave to the higher life… Wherever '
                   'the word chayah is mentioned in the sense of “the beast and the cattle,” they attached a '
                   'qualifying noun to it and said “evil beast” or “beasts of the earth” or “beast of the '
                   'field,” or it is written alongside cattle and bird and is learned from its context; but the '
                   'name chayah is not mentioned alone, without being attached to something that indicates an '
                   'evil beast… “Of every chayah I will require it”: that if you see a murderer who lives long '
                   'and dies the death of all men, I will require the blood of the murdered from his chayah '
                   '[his soul], and he will in the future give account before Him, blessed be He.',
                   'ours', start='הנני חושב', highlight=['chaya'], effect='glow'),
        question(f'{prefix}-q1', h, 14, '1. What is the problem raised by our verse?'),
        question(f'{prefix}-q2', h, 15, '2. Arrange the above into groups, and explain their views! (In '
                 'Ramban, three views!)'),
    ]})

    # §ב — scan: the letter ב only, then her one question (marked xx).
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'To Adam, and to Noah'},
                 'primaryText': comparison_1948(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 9:1–3, God’s blessing to Noah and his sons, beside '
                  'Genesis 1:28–30, His blessing to Adam.'),
        narration(f'{prefix}-b-adam', '“Rule the fish of the sea.”', highlight=['urdu']),
        narration(f'{prefix}-b-noah', '“The fear and the dread of you.”', highlight=['mora']),
        question(f'{prefix}-q-b', h, 21, 'Compare God’s blessing to the sons of Noah with God’s blessing to '
                 'Adam, 1:28–30. What is the new relationship established here toward the animals, and what '
                 'is the reason for it?',
                 highlight=['urdu', 'esev', 'mora', 'beyedchem', 'remes']),
    ]})
    return secs


# ─── 1957 ───────────────────────────────────────────────────────────────────

def leaf_1957(prefix='bl-1957'):
    """Gilayon תשי"ז (161105): §א–§ו, all six sections."""
    h = harvest('blood', '1957')
    secs = []

    # §א — scan: «xא. השוה את הסדר…», then her table (1:28 / 9:2) and a question.
    secs.append({'id': prefix, 'title': {'en': '1957 · In God’s Image'},
                 'primaryText': comparison_1957(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 1:28, the blessing to Adam, beside Genesis 9:2, the blessing to Noah.'),
        question(f'{prefix}-q-a1', h, 2, 'Compare the order in which the creatures are brought in the blessing '
                 'to Adam in Parashat Bereshit with the order in which they are brought in the blessing spoken '
                 'to Noah after the flood:',
                 highlight=['a-fish', 'a-birds', 'a-chaya', 'n-chaya', 'n-birds', 'n-remes', 'n-fish']),
        question(f'{prefix}-q-a2', h, 4, 'Can you explain the reason for the changes in the order in which the '
                 'creatures are brought here and there?', highlight=['a-fish', 'n-fish']),
    ]})

    # §ב — scan header: ב. ה ומיד האדם מיד איש אחיו אדרוש את נפש האדם.
    # §ג — scan header: ג. ה: ואך את דמכם … את נפש האדם.  §ד — ד. ה ואך את דמכם לנפשותיכם אדרוש
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“Of Humankind, Too”'},
                 'primaryText': gen_9_4_6(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 9:4–6: flesh, blood, and a reckoning.'),
        commentary(f'{prefix}-rashi-adam', h, 9, 'Rashi', 'רש"י', 'Rashi',
                   '“And of man”: of one who kills deliberately, and there are no witnesses.',
                   'ours', ref='Rashi on Genesis 9:5:4', highlight=['haadam']),
        commentary(f'{prefix}-rashi-achiv', h, 10, 'Rashi', 'רש"י', 'Rashi',
                   '“Of every man’s brother”: who loves him like a brother, and killed him unintentionally — '
                   'I will require it, if he does not go into exile and ask forgiveness for his sin, for even '
                   'the unintentional killer needs atonement. And if there are no witnesses to make him liable '
                   'to exile, and he does not humble himself, the Holy One, blessed be He, requires it of him, '
                   'as our Rabbis expounded in tractate Makkot: “and God caused it to come to his hand” — the '
                   'Holy One, blessed be He, brings them together to one inn, etc.',
                   'ours', ref='Rashi on Genesis 9:5:5', highlight=['achiv']),
        # Her print reads «אם לדעת הנרצח»; corrected to the source's «לרעת» by overrides.json replace
        # (the contrast with «לטובת הנרצח» requires it). Both of her underlined spans are kept.
        commentary(f'{prefix}-haktav-a', h, 12, 'HaKtav VeHaKabbalah', 'הכתב והקבלה', 'HaKtav VeHaKabbalah',
                   '“And of man”: the doubled language, “adam” and “ish”; and He also joined to it the word '
                   '“his brother.” It seems to me that there are two kinds of murder: <u>either to the harm '
                   'of the murdered</u>, to take revenge on him, or to take his money and the like.',
                   'ours', ref='HaKtav VeHaKabalah, Genesis 9:5:2',
                   he=underline(cut(item(h, 12)[0], None, 'או לקחת ממונו וכדומה.'), 'אם לרעת הנרצח'),
                   highlight=['haadam', 'achiv']),
        commentary(f'{prefix}-haktav-b', h, 12, 'HaKtav VeHaKabbalah', 'הכתב והקבלה', 'HaKtav VeHaKabbalah',
                   '<u>Or for the good of the murdered</u>, when he is sunk in great suffering and would '
                   'choose death over life, like Abimelech, who said to the lad (Judges 9), “Draw your sword '
                   'and kill me,” and like Saul to the Amalekite, “Stand over me, and kill me” (2 Samuel 1). '
                   'Of these two Scripture spoke: of the one who kills to the harm of the murdered… and of the '
                   'second, done by the will of the murdered and for his good, where even an excellent man, '
                   'and even one who loves the murdered, would imagine that he is doing a mitzvah in killing '
                   'him, to quiet him from his suffering.',
                   'ours', ref='HaKtav VeHaKabalah, Genesis 9:5:2',
                   he=underline(cut(item(h, 12)[0], 'אם לטובת הנרצח'), 'אם לטובת הנרצח'),
                   highlight=['haadam', 'achiv']),
        question(f'{prefix}-q-b1', h, 13, '1. Explain what the difficulty is in these verses (4–5–6) that the '
                 'two commentators wanted to resolve.', highlight=['basar', 'damchem', 'haadam', 'achiv', 'shofech', 'baadam']),
        question(f'{prefix}-q-b2', h, 14, '2. What is the difference between these two interpretations?'),
        question(f'{prefix}-q-b3', h, 15, 'Can you resolve this difficulty another way, not like these two?'),

        narration(f'{prefix}-g-intro', '“But for your own life-blood I will require a reckoning.”',
                  highlight=['damchem']),
        commentary(f'{prefix}-ibn-ezra-a', h, 21, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“But your blood”: its meaning is: I have permitted you to shed the blood of every living '
                   'thing, except your blood, of your lives, for you are man — that I have not permitted; '
                   'rather, I will require it, in the sense of (Psalms 9:13) “for He who requires blood '
                   'remembers them.” <u>And this is a general statement. And afterward He explained</u> “of '
                   'man”: if many kill one, or one kills one, I will require the blood; I will also require it '
                   'of every animal, for I will command another to kill it. And so the animals are permitted to '
                   'you, and not you to them.',
                   'ours', ref='Ibn Ezra on Genesis 9:5:1',
                   he=underline(cut(item(h, 21)[0], None, 'ולא אתם להן.'), 'וזה כלל. ואחרי כן באר'),
                   highlight=['damchem', 'chaya', 'haadam']),
        question(f'{prefix}-q-g1', h, 22, '1. Explain the first place marked with a line in his words, and give '
                 'an example in the Torah written according to the same structure!'),
        commentary(f'{prefix}-ibn-ezra-b', h, 21, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the one who explains “your blood, of your lives” as one who kills himself — that is far '
                   'from right in my eyes. <u>And He went on to explain: or it is a commandment to the children '
                   'of Noah — and this is the right one — to kill the killer;</u> and the sense of “by man” is: '
                   'by witnesses, or before the eyes of all, or on account of the man whose blood was shed; and '
                   'there are many like it.',
                   'ours', ref='Ibn Ezra on Genesis 9:5:1',
                   he=underline(cut(item(h, 21)[0], 'והמפרש'),
                                'והוסיף לבאר, או היא מצוה לבני נח, והוא הישר להרג ההורג,'),
                   highlight=['shofech', 'baadam']),
        question(f'{prefix}-q-g2', h, 23, '2. Explain the second place marked with a line. What is the '
                 'difference between the two interpretations brought in his words? (“Or”!)'),
        question(f'{prefix}-q-g3', h, 24, '3. What are the three interpretations given in his words for the word '
                 '“ba-adam” in verse 6, and which of them agrees with Rashi?', highlight=['baadam']),

        commentary(f'{prefix}-rashi-damchem', h, 27, 'Rashi', 'רש"י', 'Rashi',
                   '“But your blood”: Even though I have permitted you to take the life of cattle, your blood '
                   'I will require of one who sheds his own blood.',
                   'ours', ref='Rashi on Genesis 9:5:1', highlight=['damchem']),
        commentary(f'{prefix}-rashi-nafshot', h, 28, 'Rashi', 'רש"י', 'Rashi',
                   '“Of your lives”: even one who strangles himself, though no blood came out of him.',
                   'ours', ref='Rashi on Genesis 9:5:2', highlight=['damchem']),
        question(f'{prefix}-q-d1', h, 29, '1. What made Rashi need to explain that the subject here is taking '
                 'one’s own life, and not murder?', highlight=['damchem']),
        question(f'{prefix}-q-d2', h, 30, '2. What is the difference between him and Ibn Ezra (brought in '
                 'question ג) in resolving this difficulty?'),
        question(f'{prefix}-q-d3', h, 31, '3. According to which of the two interpretations is the beginning of '
                 'the verse, “ve-akh,” better explained?', highlight=['damchem']),
    ]})

    # §ה — scan header: ה. ו. שופך דם האדם באדם דמו ישפך כי בצלם אלוקים עשה את האדם.
    # §ו — same header line.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“In the Image of God”'},
                 'primaryText': gen_9_6(), 'steps': [
        narration(f'{prefix}-h-intro', 'Genesis 9:6.'),
        commentary(f'{prefix}-avot', h, 34, 'Pirkei Avot', 'פרקי אבות', 'Pirkei Avot',
                   'He (R. Akiva) used to say: Beloved is man, for he was created in the image. An extra love '
                   'is made known to him, that he was created in the image, as it is said: “for in the image '
                   'of God He made man.”',
                   'ours', ref='Pirkei Avot 3:14', start='הוא (ר\' עקיבא)', highlight=['tzelem', 'asa']),
        commentary(f'{prefix}-maharsha', h, 35, 'Maharsha', 'מהרש"א', 'Maharsha',
                   'Why did he not bring proof from the earlier verses in the Torah, where it says (1:26) “Let '
                   'us make man in our image, after our likeness,” and it is written (1:27) “And God created man '
                   'in His image, in the image of God He created him,” but took this verse (9:6), which is the '
                   'last in the Torah?',
                   'ours', start='למה לא הביא', highlight=['tzelem']),
        question(f'{prefix}-q-h', h, 36, 'Try to resolve his difficulty!', highlight=['tzelem']),

        commentary(f'{prefix}-radak-baadam', h, 39, 'Radak', 'רד"ק', 'Radak',
                   '“By man”: through the judges.', 'ours', highlight=['baadam']),
        question(f'{prefix}-q-v1', h, 43, '1. How would Radak explain the bet of “ba-adam”?', highlight=['baadam']),
        # Underlines per the scan check: «והוא» ×2 and «וכן». The two «הוא» are left uncapitalized in
        # the English, so the translation doesn't answer Q2.
        commentary(f'{prefix}-radak-tzelem', h, 40, 'Radak', 'רד"ק', 'Radak',
                   '“For in the image of God”: for he is the most honored of all the lower creatures, so that '
                   'God created him in His image, in the intellect He gave him. Therefore the other creatures '
                   'should fear him; and also a man his brother, that he not destroy his body and his image. '
                   'For if he kills him, behold, he has destroyed the work of God, the most honored of all the '
                   'lower ones: <u>and he</u> made him in his image, <u>and he</u> destroyed it. And even with '
                   'those lower than man, man had no permission to destroy them until God commanded Noah; and '
                   'even with plants, which are lower than the animal, a command of God was needed to permit '
                   'them to Adam and Eve, as He said (chapter 1), “Behold, I have given you every plant.” '
                   '<u>And so</u> God commanded to shed the blood of a man for his sin, as He commanded in the '
                   'Torah of Moses — and this for those who deserve the death penalty according to their sin, '
                   'every sinner as befits him — because he destroyed his own image first, in transgressing '
                   'God’s commandment.',
                   'ours', ref='Radak on Genesis 9:6',
                   he=underline(underline_every(cut(item(h, 40)[0]), 'והוא', 2), 'וכן'),
                   highlight=['tzelem', 'asa']),
        question(f'{prefix}-q-v2', h, 44, '2. To whom do the two words “hu” marked with a line refer?'),
        question(f'{prefix}-q-v3', h, 45, '3. What is the meaning of the word “ve-khen” marked with a line? '
                 'Between which two matters (commands) does this “ve-khen” connect?'),
        commentary(f'{prefix}-chizkuni', h, 41, 'Chizkuni', 'חזקוני', 'Chizkuni',
                   '“Made man”: that he be a judge and a ruler, to be feared, and not that they despise him and '
                   'curse him.', 'ours', ref='Chizkuni, Genesis 9:6', highlight=['asa']),
        commentary(f'{prefix}-malbim', h, 42, 'Malbim', 'מלבי"ם', 'Malbim',
                   '…and he is a precious vessel; none who harms him shall go unpunished.',
                   'ours', start='...והוא', highlight=['tzelem']),
        question(f'{prefix}-q-v4', h, 46, '4. Who is meant here by the man who was created in the image — the '
                 'murdered, the murderer, or the judge — according to the views of the three commentators above?',
                 highlight=['tzelem', 'asa']),
    ]})
    return secs


# ─── 1970 ───────────────────────────────────────────────────────────────────

def leaf_1970(prefix='bl-1970'):
    """Gilayon תש"ל (160445), Nataf's bilingual edition: §א, §ב, §ג, §ד, §ה (her lettering)."""
    h = harvest('blood', '1970')
    secs = []

    # §א — scan: «א. השוה את דברי ה' הראשונים…», then her two-column table.
    secs.append({'id': prefix, 'title': {'en': '1970 · God’s First Words'},
                 'primaryText': comparison_1970(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 1:28–30, God’s first words to Adam, beside Genesis 9:1–4, His '
                  'first words to Noah and his sons.'),
        # Nataf's English here has a typo («Gods's»), so this one card is our translation.
        question(f'{prefix}-q-a0', h, 1, 'Compare God’s first words to Adam after the creation of the world '
                 'with God’s first words to Noah and his sons after the flood:'),
        narration(f'{prefix}-pru', 'Both open the same way: “Be fertile and increase.”',
                  highlight=['pru-a', 'pru-n']),
        question(f'{prefix}-q-a', h, 3, None, en_basis='nataf',
                 highlight=['urdu', 'esev', 'mora', 'remes']),
    ]})

    # §ב — scan header: ב. ג'. כל רמש אשר הוא חי לכם יהיה לאכלה.
    # §ג — scan header: ג. ד'. אך בשר בנפשו דמו לא תאכלו
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'Flesh with Its Life-Blood'},
                 'primaryText': primary('Genesis 9:3-4', ['9:3', '9:4'], {
                     'remes': ('כל רמש אשר הוא חי לכם יהיה לאכלה', 'Every creature that lives shall be yours to eat'),
                     'yerek': ('כירק עשב נתתי לכם את כל', 'as with the green grasses, I give you all these'),
                     'basar': ('אך בשר', 'You must not, however, eat flesh'),
                     'nafsho': ('בנפשו דמו', 'with its life-blood in it'),
                 }), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 9:3–4: meat is given, with one limit.'),
        commentary(f'{prefix}-hirsch', h, 6, 'Hirsch', 'רש"ר הירש', 'R. Samson Raphael Hirsch',
                   'Once human life changed, man merits a new food. It stands to reason that this depends on '
                   'the shortening of his life. What was done until now in the course of seven hundred years '
                   'will be done from now on in the course of seventy, eighty years, and rapid development '
                   'requires food from living creatures. And further: the differences of heat, the changing of '
                   'the seasons of the year and of climates — all these give reason to permit food from living '
                   'creatures. Through this, man depends less on food grown from the soil… The Torah does not '
                   'want vegetarians, and it does not recoil from eating meat. On the contrary: it is a mitzvah '
                   'to eat meat on a festival (see Sifrei Deuteronomy 16:11). Were we in our original physical '
                   'state, we would not be permitted to eat meat; but now meat is a human need. Yet as soon as '
                   'meat is permitted, the laws of forbidden foods come into force. And so we find afterward, '
                   'when the Torah was given to Israel: there is no food forbidden in the Torah that is not a '
                   'food from living creatures… Against this, there is no plant that is forbidden to eat in '
                   'itself.',
                   'ours', start='משנשתנו', highlight=['remes', 'yerek']),
        narration(f'{prefix}-g-intro', '“You must not, however, eat flesh with its life-blood in it.”',
                  highlight=['basar', 'nafsho']),
        commentary(f'{prefix}-radak', h, 11, 'Radak', 'רד"ק', 'Radak',
                   '“But flesh”: Even though I have given you all creeping flesh to eat, do not eat it with its '
                   'life, which is its blood — that is, all the while the flesh is with the life, while it is '
                   'still alive. Rather, first slaughter it, and afterward eat it, for it is a way of cruelty to '
                   'cut flesh from the living and eat it.',
                   'ours', ref='Radak on Genesis 9:4:1', highlight=['basar', 'nafsho']),
        commentary(f'{prefix}-abarbanel', h, 12, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And because in killing animals for their food they would learn the trait of cruelty, He '
                   'forbade them a limb from a living creature, which is a greater cruelty. And that is His '
                   'saying, “But flesh with its life, its blood, you shall not eat.” And the bet of “be-nafsho” '
                   'serves in place of “with,” as in (Exodus 14) “with his chariots and with his horsemen,” '
                   '(Exodus 15:20) “with timbrels and with dances.” Scripture says: and flesh, while it is with '
                   'its life, its blood — you shall not eat of that flesh. And this is truly a straight and true '
                   'interpretation.',
                   'ours', highlight=['basar', 'nafsho']),
        question(f'{prefix}-q-g1', h, 13, None, en_basis='nataf', highlight=['nafsho']),
        question(f'{prefix}-q-g2', h, 14, None, en_basis='nataf', highlight=['nafsho']),
        question(f'{prefix}-q-g3', h, 15, None, en_basis='nataf'),
        commentary(f'{prefix}-kaspi', h, 16, 'Ibn Kaspi', 'ר\' יוסף אבן כספי', 'R. Yosef Ibn Kaspi',
                   '“Be-nafsho damo”: as if it said: that is to say, “its blood.” And this explanation was '
                   'necessary, for “nefesh” is a name shared by “blood” and by something else, as the Moreh '
                   'wrote (I, 41).',
                   'ours', start='ד"ה', highlight=['nafsho'], effect='glow'),
        question(f'{prefix}-q-g4', h, 17, None, en_basis='nataf'),
        question(f'{prefix}-q-g5', h, 18, None, en_basis='nataf'),
        question(f'{prefix}-q-g6', h, 19, None, en_basis='nataf', highlight=['nafsho']),
    ]})

    # §ד — scan header: ד. ד'. אך בשר בנפשו דמו לא תאכלו / ה'. ואך את דמכם לנפשותיכם אדרוש
    # §ה — scan header (missing in the digitization): ה. ה'. ואך את דמכם לנפשותיכם אדרוש
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“But for Your Own Life-Blood”'},
                 'primaryText': primary('Genesis 9:4-5', ['9:4', '9:5'], {
                     'basar': ('אך בשר', 'You must not, however, eat flesh'),
                     'nafsho': ('בנפשו דמו', 'with its life-blood in it'),
                     'damchem': ('ואך את דמכם לנפשתיכם אדרש', 'But for your own life-blood I will require a reckoning'),
                 }), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 9:4–5: two verses, each opening with “akh.”'),
        question(f'{prefix}-q-d', h, 23, None, en_basis='nataf', highlight=['basar', 'damchem']),
        commentary(f'{prefix}-rashi', h, 24, 'Rashi', 'רש"י', 'Rashi',
                   '“But your blood”: Even though I have permitted you to take the life of cattle, your blood '
                   'I will require of one who sheds his own blood.',
                   'ours', ref='Rashi on Genesis 9:5:1', highlight=['damchem']),
        commentary(f'{prefix}-bekhor-shor', h, 25, 'Bekhor Shor', 'בכור שור', 'Bekhor Shor',
                   '“But your blood, of your lives, I will require”: Because He permitted shedding the blood of '
                   'cattle, He forbade shedding the blood of man, and even one’s own blood, so that they would '
                   'not say: Was not the blood of cattle permitted to us to shed, because they live through us? '
                   'A man who lives through himself — it is permitted too to kill himself. Therefore it says: '
                   '“of your lives I will require.”',
                   'ours', ref='Bekhor Shor, Genesis 9:5:1', highlight=['damchem'], effect='glow'),
        question(f'{prefix}-q-h1', h, 26, None, en_basis='nataf', highlight=['damchem']),
        question(f'{prefix}-q-h2', h, 27, None, en_basis='nataf'),
        question(f'{prefix}-q-h3', h, 28, None, en_basis='nataf'),
    ]})
    return secs
