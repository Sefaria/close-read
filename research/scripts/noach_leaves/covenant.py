from noach_lib import *  # noqa: F401,F403
"""Theme 3 — Never again (Gen 8:20–9:17): leaves 1946, 1951, 1964.

Paper trail: research/parshiyot/noach-leaves/covenant.md (slices, omissions, open items).
"""


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_8_16_19():
    return primary('Genesis 8:16-19', ['8:16', '8:17', '8:18', '8:19'], {
        'ishtecha': ('צא מן התבה אתה ואשתך', 'Come out of the ark, together with your wife'),
        'lemishpechotehem': ('למשפחתיהם', 'by families'),
    })


def gen_8_21_9_11():
    return primary('Genesis 8:21; 9:11', ['8:21', '9:11'], {
        'lo-osif': ('לא אסף לקלל עוד את האדמה', 'Never again will I doom the earth'),
        'baavur': ('בעבור האדם', 'because of humankind'),
        'velo-osif': ('ולא אסף עוד להכות את כל חי', 'nor will I ever again destroy every living being'),
        'velo-yikaret': ('ולא יכרת כל בשר עוד', 'never again shall all flesh be cut off'),
        'velo-yihyeh': ('ולא יהיה עוד מבול', 'never again shall there be a flood'),
    })


def gen_7_14_8_19():
    return primary('Genesis 7:14; 8:16-17, 19', ['7:14', '8:16', '8:17', '8:19'], {
        'list-7': ('וכל החיה למינה וכל הבהמה למינה וכל הרמש הרמש על הארץ למינהו וכל העוף למינהו',
                   'all beasts of every kind, all cattle of every kind, all creatures of every kind that '
                   'creep on the earth, and all birds of every kind'),
        'banecha': ('אתה ואשתך ובניך ונשי בניך אתך', 'together with your wife, your sons, and your sons’ wives'),
        'kol-17': ('כל החיה אשר אתך', 'every living thing of all flesh that is with you'),
        'list-17': ('בעוף ובבהמה ובכל הרמש הרמש על הארץ', 'birds, animals, and everything that creeps on earth'),
        'peru': ('ושרצו בארץ ופרו ורבו על הארץ', 'let them swarm on the earth and be fertile and increase on earth'),
        'kol-19': ('כל החיה כל הרמש וכל העוף', 'Every animal, every creeping thing, and every bird'),
    })


def gen_6_5_8_21():
    return primary('Genesis 6:5; 8:21', ['6:5', '8:21'], {
        'raba': ('וירא יהוה כי רבה רעת האדם בארץ', 'the Lord saw how great was human wickedness on earth'),
        'kol-yetzer': ('וכל יצר מחשבת לבו רק רע כל היום',
                       'how every plan devised by the human mind was nothing but evil all the time'),
        'reiach': ('וירח יהוה את ריח הניחח', 'The Lord smelled the pleasing odor'),
        'lo-osif': ('לא אסף לקלל עוד את האדמה בעבור האדם', 'Never again will I doom the earth because of humankind'),
        'yetzer': ('כי יצר לב האדם רע', 'since the devisings of the human mind are evil'),
        'mineurav': ('מנעריו', 'from youth'),
        'velo-osif': ('ולא אסף עוד להכות את כל חי', 'nor will I ever again destroy every living being'),
    })


def gen_9_2_11():
    return primary('Genesis 9:2, 7-11', ['9:2', '9:7', '9:8', '9:9', '9:10', '9:11'], {
        'chitchem': ('ומוראכם וחתכם', 'The fear and the dread of you'),
        'veatem': ('ואתם פרו ורבו', 'Be fertile, then, and increase'),
        'vaani': ('ואני הנני מקים את בריתי', 'I now establish My covenant'),
        'itchem-1': ('אתכם ואת זרעכם אחריכם', 'with you and your offspring to come'),
        'itchem-2': ('כל נפש החיה אשר אתכם', 'every living thing that is with you'),
        'itchem-3': ('ובכל חית הארץ אתכם', 'every wild beast as well'),
        'itchem-4': ('והקמתי את בריתי אתכם', 'I will maintain My covenant with you'),
    })


def gen_9_12_16():
    return primary('Genesis 9:12-16', ['9:12', '9:13', '9:14', '9:15', '9:16'], {
        'zot-ot': ('זאת אות הברית אשר אני נתן', 'This is the sign that I set for the covenant'),
        'kashti': ('את קשתי נתתי בענן', 'I have set My bow in the clouds'),
        'leot': ('והיתה לאות ברית', 'it shall serve as a sign of the covenant'),
        'beanani': ('והיה בענני ענן על הארץ', 'When I bring clouds over the earth'),
        'vezacharti': ('וזכרתי את בריתי', 'I will remember My covenant'),
        'ureitiha': ('וראיתיה לזכר ברית עולם', 'I will see it and remember the everlasting covenant'),
    })


def gen_8_11():
    return primary('Genesis 8:11', ['8:11'], {
        'yonah': ('ותבא אליו היונה לעת ערב', 'The dove came back to him toward evening'),
        'bepiha': ('בפיה', 'in its bill'),
        'taraf': ('טרף', 'plucked-off'),
        'aleh-zayit': ('עלה זית', 'olive leaf'),
    })


def gen_8_21():
    return primary('Genesis 8:21', ['8:21'], {
        'lo-osif': ('לא אסף לקלל עוד את האדמה בעבור האדם', 'Never again will I doom the earth because of humankind'),
        'yetzer': ('כי יצר לב האדם רע', 'since the devisings of the human mind are evil'),
        'mineurav': ('מנעריו', 'from youth'),
        'velo-osif': ('ולא אסף עוד להכות את כל חי', 'nor will I ever again destroy every living being'),
    })


# ─── 1946 ───────────────────────────────────────────────────────────────────

def leaf_1946(prefix='cv-1946'):
    """Gilayon תש"ו (161548): §א (Rashi), §ב (structure and style), §ג (8:21, "evil from his youth")."""
    h = harvest('covenant', '1946')
    secs = []

    # §א — scan header: «שאלות ברש"י:». Her pointers are bare (verse, ד"ה); the texts are the digitizer's.
    secs.append({'id': prefix, 'title': {'en': '1946 · Coming Out of the Ark'},
                 'primaryText': gen_8_16_19(), 'steps': [
        narration(f'{prefix}-intro', 'God tells Noah to come out of the ark.'),
        commentary(f'{prefix}-rashi-16', h, 1, 'Rashi', 'רש"י', 'Rashi',
                   'On “you and your wife”: man and his wife together. Here He permitted them marital relations.',
                   'ours', ref='Rashi on Genesis 8:16:1', highlight=['ishtecha']),
        question(f'{prefix}-q-a1', h, 2, 'What is his difficulty?', highlight=['ishtecha']),
        commentary(f'{prefix}-gen-6-18', h, 4, 'Tanakh', 'בראשית', 'Genesis 6:18',
                   '“And I will establish My covenant with you, and you shall come into the ark, you and your '
                   'sons and your wife and your sons’ wives with you.”', 'ours'),
        commentary(f'{prefix}-gen-7-7', h, 5, 'Tanakh', 'בראשית', 'Genesis 7:7',
                   '“And Noah went in, and his sons and his wife and his sons’ wives with him, into the ark, '
                   'because of the waters of the Flood.”', 'ours'),
        commentary(f'{prefix}-rashi-19', h, 6, 'Rashi', 'רש"י', 'Rashi',
                   'On “by their families”: they took it upon themselves to keep to their own kind.',
                   'ours', ref='Rashi on Genesis 8:19:1', highlight=['lemishpechotehem']),
        question(f'{prefix}-q-a2', h, 7, 'What is his difficulty?', highlight=['lemishpechotehem']),
    ]})

    # §א continued: Rashi on 8:21, the curse of the ground, and the צידה לדרך question on 9:11.
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“Never Again”'},
                 'primaryText': gen_8_21_9_11(), 'steps': [
        narration(f'{prefix}-b-intro', 'After Noah’s offering, the Lord resolves; later, He makes a covenant.'),
        commentary(f'{prefix}-rashi-21', h, 8, 'Rashi', 'רש"י', 'Rashi',
                   'On “I will not again… and I will not again”: He repeated the matter, as an oath. This is '
                   'what is written (Isaiah 54:9), “as I swore that the waters of Noah [would never again '
                   'pass over the earth],” and we find no oath about it except this, that He repeated His '
                   'words, and that is an oath. And so the Sages expounded in Tractate Shevuot (36a).',
                   'ours', ref='Rashi on Genesis 8:21:2', highlight=['lo-osif', 'velo-osif']),
        question(f'{prefix}-q-a3', h, 9, 'What is his difficulty?', highlight=['lo-osif', 'velo-osif']),
        # Her pointer is the whole Rashi on 6:13 («ע' רש"י ו' י"ג»); the card quotes the comment on
        # «את הארץ», the one that speaks of the ground.
        commentary(f'{prefix}-rashi-6-13', h, 10, 'Rashi', 'רש"י', 'Rashi',
                   'On “with the earth” [et ha-aretz]: like “from the earth.” Similar to it: “as I go out of '
                   'the city [et ha-ir]” (Exodus 9:29), that is, from the city; “he was diseased in his feet '
                   '[et raglav]” (1 Kings 15:23), that is, from his feet. Another explanation: “et ha-aretz,” '
                   'with the earth, for even the three handbreadths of the plow’s depth were washed away and '
                   'wiped out.',
                   'ours', ref='Rashi on Genesis 6:13:3', start='ד"ה את הארץ', highlight=['lo-osif']),
        # Her start point: «החל מן וטעם לא אוסיף».
        commentary(f'{prefix}-ibn-ezra', h, 11, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the sense of “I will not again curse”: as He cursed it through Adam, for so it is '
                   'written, “Cursed be the ground.”',
                   'ours', ref='Ibn Ezra on Genesis 8:21:4', start='וטעם לא אוסיף', highlight=['lo-osif']),
        question(f'{prefix}-q-a4', h, 12, 'To which curse of the ground does the verse refer, in their view? '
                 'Bring proofs for Rashi’s view!', highlight=['lo-osif', 'baavur']),
        question(f'{prefix}-q-a5', h, 13, 'Tzeidah LaDerekh asks: Why did Rashi not follow the Gemara, and '
                 'bring proof from the doubling in 9:11, “never again shall be cut off,” “never again shall '
                 'there be…”?', highlight=['velo-yikaret', 'velo-yihyeh']),
        question(f'{prefix}-q-a6', h, 14, 'Resolve his difficulty.'),
    ]})

    # §ב — scan header: «ב. שאלות מבנה וסגנון:». Q1 ([17]) in the scan's wording (triage: use scan).
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': 'Every Living Thing'},
                 'primaryText': gen_7_14_8_19(), 'steps': [
        narration(f'{prefix}-c-intro', 'The creatures go into the ark, and come out of it.'),
        question(f'{prefix}-q-b1', h, 17, '1. Can you explain the absence of the connective vav at the '
                 'beginning of verse 17 and at the beginning of verse 19 (and see also 7:8), as against the '
                 'frequent use of the connective vav within 16 and within 17?',
                 highlight=['kol-17', 'kol-19', 'banecha', 'peru']),
        commentary(f'{prefix}-gen-7-8', h, 16, 'Tanakh', 'בראשית', 'Genesis 7:8',
                   '“Of the pure animals, and of the animals that are not pure, and of the birds, and '
                   'everything that creeps on the ground.”', 'ours'),
        question(f'{prefix}-q-b2', h, 18, 'Explain the order in which the living creatures are listed in '
                 'verse 17, and why they are listed in a different order in chapter 7, verse 14.',
                 highlight=['list-17', 'list-7']),
    ]})

    # §ג — scan header: «ג. כ"א. לא אוסיף לקלל עוד את האדמה בעבור האדם כי יצר לב האדם רע מנעוריו».
    # The digitization prints the Abarbanel lead-in twice ([23], [24]) and the Akeidah label twice
    # ([27], [28]); the scan has each once. [23] keeps the lead-in; [24] and [28] start after it.
    secs.append({'id': f'{prefix}-d', 'titleCard': False, 'title': {'en': '“Evil from Youth”'},
                 'primaryText': gen_6_5_8_21(), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 6:5, before the Flood; and 8:21, after it.'),
        commentary(f'{prefix}-abarbanel-a', h, 23, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'Abarbanel raises two questions on this verse: (a) Why did the Lord not consider this at '
                   'the outset, until the generation of the Flood, and not punish them with total '
                   'destruction, since man’s inclination is evil from his youth?',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:4', highlight=['yetzer', 'mineurav']),
        commentary(f'{prefix}-abarbanel-b', h, 24, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   '(b) Why did He give as His reason that He will not curse because of man’s evil '
                   'inclination? On the contrary, that is the very thing that makes it fitting to curse them '
                   'and destroy them! And see, (6:5) it said: “The Lord saw… and every devising of the '
                   'thoughts of man was only evil… And the Lord said, I will blot out…” So you see that there '
                   'He, blessed be He, made the evil of the inclination a cause of curse and destruction, and '
                   'in our verse He made the evil of the inclination a cause of not cursing. How could one '
                   'thing be the cause of two opposites?',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:5', start='ב. למה נתן טעם',
                   highlight=['kol-yetzer', 'yetzer']),
        commentary(f'{prefix}-akeidah-a', h, 27, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   'When the Lord brought the Flood upon the world, the nature of the human species was '
                   'mended, and came out of the corruption that had been in it from the beginning, in two '
                   'ways. The first: from the nature of youth that was in it at the beginning. For just as '
                   'the first decade, and most of the second, of the years of a person’s life go by in '
                   'vanity, in the play of childhood and the folly of youth, but from then on (that is, from '
                   'age 20) the intellect grows stronger, and he becomes another man and is ashamed of the '
                   'deeds of his childhood, so in truth it was with the world as a whole. For in the first '
                   'thousand years and most of the second, the world was young and empty of discipline, and '
                   'they had no strength to grasp the true good, neither by themselves nor with others, for '
                   'it is hard to grasp this at the beginning. And this is the sense of “since the devising of '
                   'man’s heart is evil from his youth”: because of its youth. But in the course of time its '
                   'nature will rebuke it (its inclination), so that they will not return to folly again.',
                   'ours', start='בהביא ה\' המבול', highlight=['yetzer', 'mineurav']),
        commentary(f'{prefix}-akeidah-b', h, 28, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   'And the second: from the strong and wondrous impression left in the memory of mankind by '
                   'the hard and terrible punishment that the Creator’s hand dealt to those who angered Him '
                   '(that is, the Flood), by which fear, submission and dread were fixed in them for all '
                   'generations, to know that every man who walks in the stubbornness of his heart, the Lord '
                   'has destroyed from before Him. And this mending of man (that is, the mending that came '
                   'through the shock to the soul caused by the Flood), joined to the former one (to the '
                   'mending that came through mankind’s growing up in the later generations), was the '
                   '“pleasing odor” that came before Him, blessed be He; and because of it He said: “I will '
                   'not again curse… since the devising…” The meaning is that the devising of their heart was '
                   'evil and bitter at the beginning of the world and in its youth, and from now on “I will '
                   'not again smite every living thing,” for a steadfast spirit and a new temperament have '
                   'already been renewed in them.',
                   'ours', start='והשני מצד', highlight=['reiach', 'lo-osif', 'velo-osif']),
        commentary(f'{prefix}-hirsch', h, 29, 'Hirsch', 'רש"ר הירש', 'R. Samson Raphael Hirsch',
                   'The words “since the devising of man’s heart is evil from his youth” are a parenthetical '
                   'clause: if such a thing should happen again, that the devising of man’s heart is evil, '
                   'and even from his youth (against nature, for youth by its nature strives for the good), '
                   'and there would be no rescue and redemption for the world except in destroying that whole '
                   'generation, even if such a thing should happen again, even then, “I will not again '
                   'smite…”',
                   'ours', start='המלים', highlight=['yetzer', 'mineurav', 'velo-osif']),
        # Q6 ([37], scan wording via overrides.json replace) stands in her order, between Q5 and Q7.
        commentary(f'{prefix}-some', h, 31, 'Some commentators', 'יש מפרשים', 'Some commentators',
                   '“Since the devising of man’s heart…” is not the reason for “I will not again”; rather it '
                   'is the reason for “to curse…”: that is, I will not again curse, as I cursed in the past '
                   'because of his evil inclination.',
                   'ours', highlight=['lo-osif', 'yetzer']),
        question(f'{prefix}-q-c1', h, 32, '1. How does each of the above resolve Abarbanel’s difficulties?'),
        question(f'{prefix}-q-c2', h, 33, '2. In which direction does the development of mankind go, in the '
                 'Akeidah’s view: are the later generations (after the Flood) better than those before them, '
                 'or worse?'),
        question(f'{prefix}-q-c3', h, 34, '3. Do you know of another view on this matter, besides that of the '
                 'author of the Akeidah?'),
        question(f'{prefix}-q-c4', h, 35, '4. In what do the last two interpretations differ from every usual '
                 'interpretation of the verse?'),
        question(f'{prefix}-q-c5', h, 36, '5. Can you bring proof from the structure of the verse for the '
                 'words of the last two?', highlight=['lo-osif', 'yetzer', 'velo-osif']),
        question(f'{prefix}-q-c6', h, 37, '6. In what sense is the “ki” of “ki yetzer lev…” to be read, '
                 'according to Hirsch?', highlight=['yetzer']),
        question(f'{prefix}-q-c7', h, 38, '7. Can you answer Abarbanel’s second question by an exact '
                 'comparison between verse 6:5 and our verse?', highlight=['kol-yetzer', 'yetzer']),
        # Her stop «עד "ועל דעתי"»: Ibn Ezra continues «ולפי דעתי אין צורך», exactly where the
        # digitized item ends, so the whole item is her excerpt.
        commentary(f'{prefix}-ibn-ezra-ex', h, 39, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'On “ki karov” [“for it was near”]: R. Moshe said: although it is near. And like it, in my '
                   'view: “although it is a stiff-necked people” (below, 34:9); “heal my soul, although I '
                   'have sinned against You” (Psalms 41:5); “although they have iron chariots” (Joshua '
                   '17:18).',
                   'ours', ref='Ibn Ezra on Exodus 13:17:2'),
        question(f'{prefix}-q-c8', h, 40, '8. Try to explain our verse in Ibn Ezra’s way (Exodus 13:17, on “ki '
                 'karov,” up to “and in my view”), and thereby resolve Abarbanel’s difficulty!',
                 highlight=['yetzer']),
        question(f'{prefix}-q-c9', h, 41, '9. What is the meaning of “The Lord smelled the pleasing odor” '
                 'according to the author of the Akeidah?', highlight=['reiach']),
    ]})
    return secs


# ─── 1951 ───────────────────────────────────────────────────────────────────

def leaf_1951(prefix='cv-1951'):
    """Gilayon תשי"א (161581): §א (Cassuto, "אתכם"), §ב (the bow), §ג ("בענני ענן"), §ד ("וראיתיה")."""
    h = harvest('covenant', '1951')
    secs = []

    # §א — scan header: «שאלת מבנה וסגנון:». [1] is her Q1 with Cassuto's set-out lines; cut()
    # collapses the layout, so the English marks his line breaks with " / ".
    secs.append({'id': prefix, 'title': {'en': '1951 · The Sign of the Covenant'},
                 'primaryText': gen_9_2_11(), 'steps': [
        narration(f'{prefix}-intro', 'God speaks to Noah and his sons after the Flood.'),
        question(f'{prefix}-q-a1', h, 1, '1. Cassuto, in his book From Noah to Abraham, page 72, prints these '
                 'verses of ours in this form: “And God said / to Noah and to his sons with him / saying: / '
                 'And I — / I now establish My covenant / with you / and with your offspring / after you / '
                 'and with every living thing / that is with you / birds, cattle / and every wild beast / '
                 'with you / of all that came out of the ark / every living thing of the earth / I will '
                 'maintain My covenant / with you…”',
                 highlight=['itchem-1', 'itchem-2', 'itchem-3', 'itchem-4']),
        commentary(f'{prefix}-cassuto', h, 2, 'Cassuto', 'קאסוטו', 'Cassuto',
                   'Perhaps there is a kind of wordplay here with “ve-chittekhem” [“and the dread of you”] '
                   'in verse 2.',
                   'ours', start='אולי', highlight=['chitchem'], effect='glow'),
        question(f'{prefix}-q-a1b', h, 3, 'Explain accordingly the intent of the many repetitions of the word '
                 '“ittekhem” [“with you”], and what the connection between it and “chittekhem” might be.',
                 highlight=['chitchem', 'itchem-1', 'itchem-2', 'itchem-3', 'itchem-4']),
        # Q2's sentence sits inside the Genesis 1:28 item [7]; the verse labels around it («2. פסוק ז:»,
        # «והשוה למקומנו:») are lost in the digitization.
        question(f'{prefix}-q-a2', h, 7, 'Explain: why do the pronouns “I” and “you” come in these verses, '
                 'against the usual usage of the language in the Bible, as in Genesis 1:28: “Be fertile and '
                 'increase…”', highlight=['veatem', 'vaani']),
        commentary(f'{prefix}-gen-9-1', h, 8, 'Tanakh', 'בראשית', 'Genesis 9:1',
                   '“Be fertile and increase.”', 'ours'),
        commentary(f'{prefix}-gen-6-13', h, 9, 'Tanakh', 'בראשית', 'Genesis 6:13',
                   '“And behold, I am about to destroy them…”', 'ours'),
        commentary(f'{prefix}-gen-17-4', h, 10, 'Tanakh', 'בראשית', 'Genesis 17:4',
                   '“As for Me, behold, My covenant is with you.”', 'ours', highlight=['vaani']),
        commentary(f'{prefix}-gen-17-9', h, 11, 'Tanakh', 'בראשית', 'Genesis 17:9',
                   '“And as for you, you shall keep My covenant.”', 'ours', highlight=['veatem']),
    ]})

    # §ב — scan header: «ב. י"ג את קשתי נתתי בענן.»  §ג: «ג. י"ד והיה בענני ענן.»
    # §ד: «ד. ט"ז וראיתיה לזכור ברית עולם.»
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'The Bow in the Clouds'},
                 'primaryText': gen_9_12_16(), 'steps': [
        narration(f'{prefix}-b-intro', 'The sign of the covenant.'),
        commentary(f'{prefix}-abarbanel', h, 14, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'On the matter of the sign of the bow, which the Holy One, blessed be He, gave to Noah and '
                   'his sons to assure them that a flood would not come again: the point is that the bow is a '
                   'natural thing, born of the sun’s rays striking something moist. It forms on vessels of '
                   'water, where the sun is imprinted in its roundness and its colors, and that is the bow. '
                   'And of it the prophet said (Ezekiel 1:28): “like the appearance of the bow that is in the '
                   'cloud on a day of rain”… What, then, is this sign of the covenant that was made with Noah '
                   'as an assurance?',
                   'ours', start='בענין', highlight=['kashti', 'leot']),
        question(f'{prefix}-q-b1', h, 15, '1. Explain: what is his difficulty?'),
        question(f'{prefix}-q-b2', h, 16, '2. What contradiction does he see between Ezekiel 1:28 and our '
                 'passage?', highlight=['kashti']),
        # Her stop «עד "אבל יש לרבותינו"» (in her Q3) is where Ramban's next sentence begins; the
        # digitized item ends just before it (checked on Sefaria), so the three cards cover her excerpt.
        commentary(f'{prefix}-ramban-a', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   'On “This is the sign of the covenant that I set”: what this sign implies is that there was '
                   'no bow in the cloud from the work of creation, and now the Lord created something new, '
                   'making a bow in the sky on a cloudy day. And they said, on the reason for this sign, that '
                   'He did not make the bow with its ends upward, so that it would look as though they were '
                   'shooting with it from heaven, “and He sent out His arrows and scattered them” (Psalms '
                   '18:15); rather He made it the reverse of this, to show that they would not shoot with it '
                   'from heaven. And such is the way of warriors, to turn it over in their hand like this when '
                   'they call for peace to those facing them. Moreover, the bow has no string for setting '
                   'arrows on it.',
                   'ours', ref='Ramban on Genesis 9:12:1', stop='לכונן חצים עליו.', highlight=['zot-ot']),
        commentary(f'{prefix}-ramban-b', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   'But we are compelled to believe the words of the Greeks, that from the blaze of the sun in '
                   'moist air the bow comes about by nature, for in a vessel of water before the sun something '
                   'like the appearance of a bow is seen. And when we look further at the language of '
                   'Scripture we will understand it so, for it said “I have set My bow in the cloud,” and did '
                   'not say “I set in the cloud,” as it said “This is the sign of the covenant that I set.” '
                   'And the word “My bow” indicates that He had the bow beforehand. Therefore we will '
                   'interpret the verse: the bow that I set in the cloud from the day of creation shall be, '
                   'from this day on, a sign of a covenant between Me and you, so that whenever I see it I '
                   'will remember that there is a covenant of peace between Me and you.',
                   'ours', ref='Ramban on Genesis 9:12:1', start='ואנחנו על כרחנו',
                   stop='כי ברית שלום ביני וביניכם.', highlight=['kashti', 'zot-ot'], effect='glow'),
        commentary(f'{prefix}-ramban-c', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   'And if you ask what the reason is for the bow to be a sign: it is like “this heap is a '
                   'witness and the pillar is a witness” (below, 31:52), and likewise “you shall take these '
                   'seven ewes from my hand, that it may be a witness for me” (below, 21:30). For any visible '
                   'thing that is set before two parties to remind them of a matter vowed between them is '
                   'called a sign, and every agreement a covenant. And so of circumcision He said, “and it '
                   'shall be a sign of the covenant between Me and you” (below, 17:11), because of the '
                   'agreement that all the seed of Abraham would be circumcised, to serve Him with one '
                   'accord. And moreover, when it is seen in the reversed shape mentioned above, it will be a '
                   'reminder of peace, as we wrote. And whether the bow is new now or was always in nature, '
                   'the meaning of the sign in it is the same.',
                   'ours', ref='Ramban on Genesis 9:12:1', start='ואם תבקש', highlight=['leot']),
        question(f'{prefix}-q-b3', h, 'after 17', '3. How is the difficulty resolved in Ramban (verse 12, on '
                 '“This is the sign of the covenant,” up to “But our Rabbis have”)?'),
        question(f'{prefix}-q-b4', h, 18, '4. What proof does Ramban bring for his view from the language of '
                 'Scripture?', highlight=['kashti', 'zot-ot']),
        question(f'{prefix}-q-b5', h, 19, '5. What is the second difficulty arising in the matter of the bow, '
                 'which Ramban resolves?'),

        narration(f'{prefix}-c-intro', '“When I bring clouds over the earth.”', highlight=['beanani']),
        commentary(f'{prefix}-radak-14', h, 22, 'Radak', 'רד"ק', 'Radak',
                   'I will bring clouds through intermediate causes that I have commanded.',
                   'ours', ref='Radak on Genesis 9:14:1', highlight=['beanani']),
        # Stops before the pointer to her Vayigash 1947 gilayon («שהובאו בגליון ויגש תש"ז שאלה ד.»).
        question(f'{prefix}-q-c', h, 23, 'Explain what is difficult for him in our verse, and what he set right '
                 'in his words. To understand these words of his, see Sforno on Genesis 45:8, on “So it was '
                 'not you who sent me here,” and likewise the Guide of the Perplexed 2:48 on that verse.',
                 stop='לפסוק ההוא', highlight=['beanani']),

        narration(f'{prefix}-d-intro', '“I will see it and remember the everlasting covenant.”',
                  highlight=['ureitiha']),
        commentary(f'{prefix}-radak-15', h, 26, 'Radak', 'רד"ק', 'Radak',
                   'The Torah speaks in human language, for there is no forgetting before the throne of His '
                   'glory. And so (Leviticus 26:42): “Then I will remember My covenant with Jacob, and also My '
                   'covenant with Isaac, and also My covenant with Abraham I will remember, and I will '
                   'remember the land.” It is all by way of figure.',
                   'ours', ref='Radak on Genesis 9:15:1', highlight=['ureitiha', 'vezacharti']),
        commentary(f'{prefix}-shadal', h, 27, 'Shadal', 'שד"ל', 'Shadal',
                   'Shadal wants to explain this figure of speech another way, on the basis of the following '
                   'verses, so that we need not interpret it in the manner of “the Torah speaks in human '
                   'language”:', 'ours', highlight=['ureitiha']),
        commentary(f'{prefix}-gen-2-19', h, 28, 'Tanakh', 'בראשית', 'Genesis 2:19',
                   '“And He brought them to the man to see what he would call them.”', 'ours'),
        commentary(f'{prefix}-gen-2-3', h, 29, 'Tanakh', 'בראשית', 'Genesis 2:3',
                   '“Which God created, to make.”', 'ours'),
        commentary(f'{prefix}-ps-104', h, 30, 'Tanakh', 'תהלים', 'Psalms 104:27',
                   '“All of them look to You to give them their food in its season.”', 'ours'),
        question(f'{prefix}-q-d1', h, 31, '1. Explain: what is difficult for Radak?'),
        question(f'{prefix}-q-d2', h, 32, '2. How does Shadal explain our verse on the basis of the three '
                 'verses above?', highlight=['ureitiha']),
        question(f'{prefix}-q-d3', h, 33, '3. What is the weakness of this interpretation, and in what are '
                 'those verses unlike our verse?'),
    ]})
    return secs


# ─── 1964 ───────────────────────────────────────────────────────────────────

def leaf_1964(prefix='cv-1964'):
    """Gilayon תשכ"ד (160639): §א ("טרף"), §ב (Ibn Kaspi on "כי"), §ג (youth), §ד (the earth's end)."""
    h = harvest('covenant', '1964')
    secs = []

    # §א — scan header: «א י"א והנה עלה זית טרף בפיה». Ramban [5] is shown in four slices; the third
    # starts at «ולשון בראשית רבה» («אמר ר' אבהו» fixed in the harvest by overrides.json replace).
    secs.append({'id': prefix, 'title': {'en': '1964 · The Dove and the Covenant'},
                 'primaryText': gen_8_11(), 'steps': [
        narration(f'{prefix}-intro', 'The dove comes back to the ark a second time.'),
        commentary(f'{prefix}-rashi-a', h, 3, 'Rashi', 'רש"י', 'Rashi',
                   'On “plucked-off in its bill”: I say that it was a male, and that is why Scripture calls '
                   'it sometimes in the masculine and sometimes in the feminine; because every dove in '
                   'Scripture is feminine, as in (Song of Songs 5) “like doves by the watercourses, bathing” '
                   '[feminine]; (Ezekiel 7:16) “like doves of the valleys, all of them moaning” [feminine]; '
                   '(Hosea 7) “like a silly dove” [feminine].',
                   'ours', ref='Rashi on Genesis 8:11:1', highlight=['bepiha', 'yonah']),
        commentary(f'{prefix}-rashi-b', h, 4, 'Rashi', 'רש"י', 'Rashi',
                   'On “taraf”: snatched. And a midrash aggadah: it is a word for food. And they expounded '
                   '“in its mouth” as a word for speech: it said, Let my food be bitter as an olive, in the '
                   'hand of the Holy One, blessed be He, and not sweet as honey in the hands of flesh and '
                   'blood.',
                   'ours', ref='Rashi on Genesis 8:11:2', highlight=['taraf', 'bepiha']),
        commentary(f'{prefix}-ramban-a', h, 5, 'Ramban', 'רמב"ן', 'Ramban',
                   'On “plucked-off in its bill”: Rashi wrote: “I say…” (see above). None of this seems right '
                   'to me, for the doves’ being switched from feminine to masculine in one place in the '
                   'passage has no reason. And if the language calls them (that is, if it is the way of the '
                   'language to call them, to refer to them) all by the feminine, why did it change here?',
                   'ours', ref='Ramban on Genesis 8:11:1', stop='למה שינה בכאן?', highlight=['bepiha', 'yonah']),
        question(f'{prefix}-q-a1', h, 6, '1. Explain what the grammatical and linguistic difficulties in our '
                 'verse are that confront Rashi and Ramban, and what the difficulty of substance is.',
                 highlight=['taraf', 'bepiha']),
        commentary(f'{prefix}-ramban-b', h, 5, 'Ramban', 'רמב"ן', 'Ramban',
                   'And so too their midrash in the aggadah: it is not that they make “in its mouth” a word '
                   'for speech at all. Rather, their midrash is because it brought this leaf. For if we say '
                   'that this is what happened, Scripture did not spell it out for nothing, since it could '
                   'have said “and there was a plucked leaf in its bill.” And the olive is not one of the very '
                   'tall trees in whose long branches birds dwell; and so they said there was a hint in this: '
                   'that the birds would rather have their food bitter as wormwood in the hand of the Holy '
                   'One, blessed be He, than good in the hands of man. And all the more so human beings, who '
                   'do not wish to be supported by one another.',
                   'ours', ref='Ramban on Genesis 8:11:1', start='וכן מדרשם', stop='להתפרנס זה מזה.',
                   highlight=['aleh-zayit', 'bepiha']),
        question(f'{prefix}-q-a2', h, 7, '2. On “taraf” Rashi brings two interpretations: his own (“snatched”) '
                 'and the midrash aggadah. Does Ramban oppose both of them, or only one of them?',
                 highlight=['taraf']),
        question(f'{prefix}-q-a3', h, 8, '3. What are the two linguistic arguments that Ramban raises against '
                 'Rashi’s interpretation?'),
        question(f'{prefix}-q-a4', h, 9, '4. What is the difference between Rashi’s understanding of our Sages’ '
                 'midrash and Ramban’s understanding of their words?'),
        question(f'{prefix}-q-a5', h, 10, '5. Explain Ramban’s words “for if we say that this is what '
                 'happened”: what is the thing that was so? And why does he open with “for if we say”? What '
                 'in this is characteristic of Ramban’s way of interpreting?'),
        question(f'{prefix}-q-a6', h, 11, '6. Why does Ramban need to tell us that the olive is not one of the '
                 'tall trees? What importance does this have for the interpretation of our verse?',
                 highlight=['aleh-zayit']),
        commentary(f'{prefix}-ramban-c', h, 5, 'Ramban', 'רמב"ן', 'Ramban',
                   'And in the words of Bereshit Rabbah (33:6): R. Abbahu said… but it hinted a hint to him; '
                   'it said to him: “Noah! Better bitter from under the hand of the Holy One, blessed be He, '
                   'than sweet from under your hand.” But in the Gemara (Sanhedrin 108b) they added: How do we know that this “taraf” is a word '
                   'for food? Because it is written (Proverbs 30:8), “hatrifeni lechem chukki,” “give me my '
                   'daily bread.” For because of the reason we gave, they make a support for this from the '
                   'word “hatrifeni”: it hints as if it had said, “and there was an olive leaf; it was food '
                   'in its mouth.”',
                   'ours', ref='Ramban on Genesis 8:11:1', start='ולשון בראשית רבה', stop='היה טרף בפיה".',
                   highlight=['taraf', 'bepiha']),
        question(f'{prefix}-q-a8', h, 13, '8. What distinguishes the Gemara’s interpretation in Sanhedrin, '
                 'Ramban’s interpretation and “the plain sense of Scripture,” on the meaning of the word '
                 'taraf?', highlight=['taraf']),
        commentary(f'{prefix}-ramban-d', h, 5, 'Ramban', 'רמב"ן', 'Ramban',
                   'And the plain sense of Scripture, as they explained it, is that it is an adjective of the '
                   'leaf: “and there was a plucked [taruf] olive leaf in its bill”; and a support for this is '
                   'that it has a kamatz, for such is its rule. (His meaning: such is the rule of an '
                   'adjective, that it comes with two kamatzes, like chakham, katan.) But some of them are '
                   'found irregularly: (Hosea 6:1) “for He has torn [taraf] and He will heal us”; (Leviticus '
                   '5:23) “and he shall return the stolen thing that he stole [gazal]”; (Leviticus 5:18) “for '
                   'his error that he erred [shagag].” And many others besides.',
                   'ours', ref='Ramban on Genesis 8:11:1', start='ופשוטו של מקרא',
                   highlight=['taraf', 'aleh-zayit'], effect='glow'),
        question(f'{prefix}-q-a9', h, 14, '9. Explain Ramban’s words “but some of them are found irregularly”: '
                 'to whom does the pronoun “of them” refer? Of whom?'),
        question(f'{prefix}-q-a10', h, 15, '10. What do the three verses (from Hosea and from Leviticus) brought '
                 'at the end of Ramban’s words have in common?'),
    ]})

    # §ב — scan header: «ב כ' כי יצר לב האדם רע מנעוריו».  §ג: «ג' כ"א כי יצר לב האדם רע מנעוריו.»
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“Evil from Youth”'},
                 'primaryText': gen_8_21(), 'steps': [
        narration(f'{prefix}-b-intro', 'After Noah’s offering, the Lord resolves never again to doom the earth.'),
        commentary(f'{prefix}-kaspi-ki', h, 18, 'Ibn Kaspi', 'אבן כספי, משנה כסף', 'Ibn Kaspi, Mishneh Kesef',
                   'It is right in my view that it gives the reason for “I will not again.”',
                   'ours', start='נכון אצלי', highlight=['yetzer', 'lo-osif']),
        question(f'{prefix}-q-b', h, 19, 'Explain: what is the possible interpretation of our verse that he '
                 'opposes?', highlight=['yetzer']),
        commentary(f'{prefix}-abarbanel-a', h, 22, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   '…The second way of interpreting it is this: what happens to the individual person happened '
                   'to the world as a whole, since the whole world was like one man, so that man is called “a '
                   'small world” and the world “a great man”; and therefore the days of our years are seventy '
                   'years, corresponding to the seven days of creation.',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:20', start='והאופן השני',
                   stop='כנגד שבעת ימי בראשית.', highlight=['mineurav']),
        commentary(f'{prefix}-abarbanel-b', h, 22, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'Now the individual person knows from his own affairs that the first decade of his days, '
                   'and most of the second too, are years of rashness without rational conduct, for they all '
                   'pass in great play and childishness and in the folly of youth, which one cannot escape at '
                   'the beginning of one’s days. But from then on the intellect grows stronger, and the man '
                   'changes in himself and turns into another man, and is ashamed of the disgrace of his '
                   'youth. And so it truly was with the world at large: the first thousand years and most of '
                   'the second thousand were young and empty, lacking intellect. And so the Sages called them: '
                   '“two thousand years of chaos.” And for the deficiency of the people in them (= in those '
                   'two thousand years) they were condemned to the destruction and ruin of the Flood. But '
                   'afterward, in the course of time, it will forget the shame of its youth, and its intellect '
                   'will surely rebuke it, so that it will not transgress again as at first.',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:20', start='והנה האדם הפרט',
                   stop='שלא יפשע עוד כבראשונה.', highlight=['yetzer', 'mineurav']),
        commentary(f'{prefix}-abarbanel-c', h, 22, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And this is the matter of the covenant that the Lord made, not to bring a flood upon the '
                   'earth again: it was not by way of kindness, for Noah’s merit, but by way of telling the '
                   'future. For at first, when He, blessed be He, saw that the wickedness of man was great on '
                   'the earth and every devising of the thoughts of his heart was only evil all the day, He '
                   'said “I will blot out man,” that is, I will destroy, and I will blot out the whole '
                   'generation, since it was corrupt as a whole. But after the Flood had passed, the Holy One, '
                   'blessed be He, judged in His wisdom and said: “There is no need to curse the ground again '
                   'because of man with another flood, since this was done because of the youth of the world; '
                   'and without doubt people will not again commit so total a corruption, of the whole '
                   'species: whether because of the great lesson they saw in the Flood, so that all the people '
                   'of the world will take it to heart and not return to folly; or because from now on the '
                   'generations and families will branch out from three heads, Shem, Ham and Japheth, by whose '
                   'nature there will always be difference among them and no agreement on any one matter, '
                   'whether good or bad. And so it will be impossible for them all to agree on a shared intent '
                   'of total corruption, as the people of the Flood did, and so they will not incur a general '
                   'destruction like theirs.”',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:20', start='וזה עניין הברית',
                   stop='הפסד כללי כמוהם.', highlight=['lo-osif']),
        commentary(f'{prefix}-abarbanel-d', h, 22, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'So it has become clear that He said, by way of telling the future: “I will not again curse '
                   'the ground because of man,” for what happened in the Flood was “because the devising of '
                   'man’s heart is evil from his youth,” that is, from its youth in the world, the beginning '
                   'of its times; and therefore “I will not again smite every living thing,” for the youth of '
                   'the world has already passed.',
                   'ours', ref='Abarbanel on Torah, Genesis 8:15:20', start='הנה התבהר',
                   highlight=['lo-osif', 'mineurav', 'velo-osif'], effect='glow'),
        commentary(f'{prefix}-tedeschi', h, 23, 'Tedeschi', 'משה יצחק אשכנזי (טדסקי), הואיל משה',
                   'Moshe Yitzhak Ashkenazi (Tedeschi), Ho’il Moshe',
                   'On “from his youth”: One of my students wished to explain this phrase not of the days of '
                   'youth of each and every man, but generally, of all mankind: that is, people in the first '
                   'years [of the world], who did not yet have understanding, when the world was in its youth; '
                   'their inclination was evil. And I answered that then he should have said “bi-ne’urav” '
                   '[“in his youth”], with a bet; and the verse (1 Samuel 17:32 [the words are in 17:33]) “and '
                   'he has been a man of war from his youth” proves it.',
                   'ours', start='ד"ה מנעוריו', highlight=['mineurav']),
        commentary(f'{prefix}-shadal', h, 24, 'Shadal', 'שד"ל', 'Shadal',
                   'Already from the time of his youth his heart plows and fashions evil thoughts. Note that it '
                   'did not say that the heart of man is evil by nature, but that his thoughts are evil from '
                   'the days of his youth, without this being necessary and natural in man.',
                   'ours', ref='Shadal on Genesis 8:21:4', highlight=['yetzer', 'mineurav']),
        question(f'{prefix}-q-c1', h, 25, '1. What is the difficulty that occupies Abarbanel and Ashkenazi, and '
                 'what is the difficulty that occupies Shadal?', highlight=['mineurav']),
        question(f'{prefix}-q-c2', h, 26, '2. Abarbanel resolves his difficulty in three different ways. What '
                 'are they?'),
        question(f'{prefix}-q-c3', h, 27, '3. Ho’il Moshe refutes the interpretation of one of his students, '
                 'which is Abarbanel’s interpretation. Is there an answer to his argument in Abarbanel’s '
                 'words?'),
        question(f'{prefix}-q-c4', h, 28, '4. What blessing does Abarbanel see in the lack of unity?'),
    ]})

    # §ד — scan header: «ד כ"ב עוד כל ימי הארץ זרע וקציר …». The unlettered last section (8:22,
    # «לא ישבותו», Rashi) is outside the §7 design and is not rendered.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“So Long as the Earth Endures”'},
                 'primaryText': primary('Genesis 8:22', ['8:22'], {
                     'kol-yemei': ('עד כל ימי הארץ', 'So long as the earth endures'),
                 }), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 8:22: the seasons shall not cease.'),
        commentary(f'{prefix}-ibn-ezra', h, 31, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'On “So long as the earth endures”: a sign that it has a fixed end.',
                   'ours', ref='Ibn Ezra on Genesis 8:22:1', highlight=['kol-yemei']),
        commentary(f'{prefix}-kaspi-end', h, 32, 'Ibn Kaspi', 'אבן כספי', 'Ibn Kaspi',
                   'On “So long as the earth endures”: this does not imply, neither by the Hebrew nor by '
                   'logic, that it has an end. Rather the view of the Guide, and it is the truth, is that the '
                   'earth as a whole stands forever, and in general that the world is eternal in the time to '
                   'come; for we agree with Aristotle on half of his view.',
                   'ours', start='ד"ה עוד', highlight=['kol-yemei']),
        question(f'{prefix}-q-d1', h, 33, '1. What is the dispute between the two of them, and what is the '
                 'linguistic basis of each of the two views?', highlight=['kol-yemei']),
        question(f'{prefix}-q-d2', h, 34, '2. What is the other half of Aristotle’s view, on which we do not '
                 'agree with him?'),
    ]})
    return secs
