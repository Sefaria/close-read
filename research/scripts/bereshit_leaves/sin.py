from bereshit_lib import *  # noqa: F401,F403
"""Theme 3: the trees, the sin and its aftermath (Gen 2:9–3:24): leaves 1944, 1964, 1968.

Paper trail: research/parshiyot/bereshit-leaves/sin.md.
"""


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_3_8_9():
    return primary('Genesis 3:8-9', ['3:8', '3:9'], {
        'kol': ('קול יהוה אלהים', 'the sound of the Lord God'),
        'mithalekh': ('מתהלך בגן', 'moving about in the garden'),
        'ruach': ('לרוח היום', 'at the breezy time of day'),
        'ayeka': ('איכה', 'Where are you?'),
    })


def gen_3_8():
    return primary('Genesis 3:8', ['3:8'], {
        'kol': ('קול יהוה אלהים', 'the sound of the Lord God'),
        'mithalekh': ('מתהלך בגן', 'moving about in the garden'),
        'ruach': ('לרוח היום', 'at the breezy time of day'),
    })


# ─── 1944 ───────────────────────────────────────────────────────────────────

def leaf_1944(prefix='sn-1944'):
    """Gilayon תש"ד (161941): §א, §ב, §ג, §ד (all four sections)."""
    h = harvest('sin', '1944')
    secs = []

    P_a = lambda: primary('Genesis 3:3-4, 6-7, 11', ['3:3', '3:4', '3:6', '3:7', '3:11'], {
        'lo-tigu': ('ולא תגעו בו', 'or touch it'),
        'lo-mot': ('לא מות תמתון', 'You are not going to die'),
        'vatere': ('ותרא האשה', 'When the woman saw'),
        'ki-tov': ('כי טוב העץ', 'that the tree was good'),
        'vatipakachna': ('ותפקחנה עיני שניהם', 'the eyes of both of them were opened'),
        'mi-higid': ('מי הגיד לך', 'Who told you'),
    })

    # §א — scan header: א. שאלות ודיוקים ברש"י:  (seven Rashi pointers, each with her question)
    secs.append({'id': prefix, 'title': {'en': '1944 · Eating from the Tree'}, 'primaryText': P_a(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 3: the woman and the serpent, the eating, and what follows.'),
        commentary(f'{prefix}-rashi-3-3', h, 2, 'Rashi', 'רש"י', 'Rashi',
                   '“Nor touch it”: She added to the command; therefore she came to diminish it. That is '
                   'what is said (Proverbs 30): “Do not add to His words.”',
                   'ours', ref='Rashi on Genesis 3:3:1', highlight=['lo-tigu']),
        question(f'{prefix}-q-a1', h, 3, 'Some of Rashi’s commentators ask: why did he bring a verse from '
                 'Proverbs (30:6) as proof for his words, and not the words of the Torah, Deuteronomy 4:2?'),
        commentary(f'{prefix}-rashi-3-4', h, 5, 'Rashi', 'רש"י', 'Rashi',
                   '“You are not going to die”: He pushed her until she touched it. He said to her: just as '
                   'there is no death in touching, so there is no death in eating (Bereshit Rabbah).',
                   'ours', ref='Rashi on Genesis 3:4:1', highlight=['lo-mot']),
        question(f'{prefix}-q-a2', h, 6, 'What led Rashi to bring this midrash?'),
        # Her parenthesis inside question 2. Stops before «פסוק ה'»: the harvest no longer carries her
        # «פסוק ח'» (see sin.md); the Rashi the digitizer attached after it is cut off too.
        question(f'{prefix}-q-a2-see', h, 7, 'And see his rule for choosing midrashim', stop='בבחירת המדרשים'),
        commentary(f'{prefix}-rashi-3-6a', h, 8, 'Rashi', 'רש"י', 'Rashi',
                   '“And the woman saw”: She saw the serpent’s words; they pleased her, and she believed '
                   'him (Bereshit Rabbah).',
                   'ours', ref='Rashi on Genesis 3:6:1', highlight=['vatere']),
        question(f'{prefix}-q-a3', h, 9, 'What troubles him?'),
        question(f'{prefix}-q-a3b', h, 10, 'These words of Rashi are taken from Bereshit Rabbah, parasha 19: '
                 '“She saw the serpent’s words.” What led Rashi to add further: “they pleased her and she '
                 'believed him”?'),
        commentary(f'{prefix}-rashi-3-6b', h, 11, 'Rashi', 'רש"י', 'Rashi',
                   '“That the tree was good”: for becoming like God.',
                   'ours', ref='Rashi on Genesis 3:6:2', highlight=['ki-tov']),
        question(f'{prefix}-q-a4', h, 12, 'Where does he get this from?'),
        # Starts after the dibbur, which the digitizer misspelled (ותפחקנה).
        commentary(f'{prefix}-rashi-3-7', h, 13, 'Rashi', 'רש"י', 'Rashi',
                   'Scripture is speaking of wisdom, and not of actual sight; and the end of the verse '
                   'proves it.',
                   'ours', ref='Rashi on Genesis 3:7:1', start='לענין החכמה', highlight=['vatipakachna']),
        question(f'{prefix}-q-a5', h, 14, 'Why did Rashi not explain it this way also at chapter 21, verse 19, '
                 '“And God opened her eyes”?', stop='את עיניה?'),
        commentary(f'{prefix}-rashi-3-11', h, 15, 'Rashi', 'רש"י', 'Rashi',
                   '“Who told you”: From where do you know what shame there is in standing naked?',
                   'ours', ref='Rashi on Genesis 3:11:1', highlight=['mi-higid']),
        question(f'{prefix}-q-a6', h, 16, 'And why did he not explain it according to its plain sense?'),
    ]})

    # §ב — scan header: ב. ח' וישמעו את קול ה' אלוקים מתהלך. עיין רש"י, ראב"ע (עד גם הוא אחר) רמב"ן
    # §ג — scan header: ג. איכה.  (same panel, so the two share a section)
    secs.append({'id': f'{prefix}-voice', 'titleCard': False,
                 'title': {'en': '“They Heard the Sound”'}, 'primaryText': gen_3_8_9(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 3:8–9: a sound in the garden, and a call.'),
        commentary(f'{prefix}-rashi-3-8a', h, 21, 'Rashi', 'רש"י', 'Rashi',
                   '“And they heard”: There are many aggadic midrashim, and our Rabbis have already set them '
                   'in their proper places in Bereshit Rabbah and in other midrashim. But I have come only for '
                   'the plain sense of Scripture, and for such aggada as settles the words of Scripture, each '
                   'word in its fitting way.',
                   'ours', ref='Rashi on Genesis 3:8:1'),
        commentary(f'{prefix}-rashi-3-8b', h, 22, 'Rashi', 'רש"י', 'Rashi',
                   '“And they heard”: What did they hear? They heard the voice of the Holy One, blessed be He, '
                   'who was walking in the garden.',
                   'ours', ref='Rashi on Genesis 3:8:1', highlight=['kol', 'mithalekh']),
        commentary(f'{prefix}-rashi-3-8c', h, 23, 'Rashi', 'רש"י', 'Rashi',
                   '“At the breezy time of day” [literally, “to the wind of the day”]: toward that direction '
                   'from which the sun comes (another reading: “to which,” and look closely, for that is the '
                   'main reading). And this is the west, for toward evening the sun is in the west; and they '
                   'sinned in the tenth hour (ibid. 38).',
                   'ours', ref='Rashi on Genesis 3:8:2', highlight=['ruach']),
        # Her stop «עד גם הוא אחר» is Ibn Ezra's «גם הוא אמר», the words right after this item ends.
        commentary(f'{prefix}-ibn-ezra-3-8', h, 24, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“And they heard… moving about in the garden”: the voice of the Lord. And this was close to '
                   'evening, when the wind of the day blows. And we find walking said of a voice, as in “Her '
                   'sound shall go like the serpent’s,” “the sound of the horn going on and growing very loud.” '
                   'And R. Yonah, the Spanish grammarian, says that the meaning is: and the man was walking in '
                   'the garden.',
                   'ours', ref='Ibn Ezra on Genesis 3:8:1', highlight=['mithalekh', 'ruach']),
        commentary(f'{prefix}-ramban-3-8', h, 25, 'Ramban', 'רמב"ן', 'Ramban',
                   'They said in Bereshit Rabbah (19:12): R. Chilfai said, we have learned that a voice has '
                   'walking, as it says, “And they heard the voice of the Lord God walking in the garden.” And '
                   'so the Rav wrote in the Guide of the Perplexed (1:24), and so is the view of R. Avraham, '
                   'that “walking” is a term for the voice, as in “Her sound shall go like the serpent’s” '
                   '(Jeremiah 46:22). And he said that the sense of “to the wind of the day” is that they '
                   'heard the voice toward evening. And he cited in the name of R. Yonah that the meaning is: '
                   'and the man was walking in the garden to the wind of the day. '
                   'And in my view, the sense of “walking in the garden of Eden” is like the sense of “And I '
                   'will walk among you” (Leviticus 26:12), “And the Lord went, when He had finished speaking '
                   'to Abraham” (below, 18:33), “I will go and return to My place” (Hosea 5:15): it concerns '
                   'the revelation of the Shekhinah in that place, or its withdrawal from the place where it '
                   'was revealed. '
                   'And the sense of “to the wind of the day”: when the Shekhinah is revealed, a great and '
                   'strong wind comes, as it is said (1 Kings 19:11), “And behold, the Lord passed by, and a '
                   'great and strong wind, rending mountains and shattering rocks before the Lord”; and so “He '
                   'soared on the wings of the wind” (Psalms 18:11); and it is written in Job (38:1), “And the '
                   'Lord answered Job out of the whirlwind.” Therefore it says here that they heard the voice '
                   'of the Lord, for the Shekhinah was revealed in the garden as drawing near to them “to the '
                   'wind of the day”: the wind of the Lord blew in the garden like the wind of the days, not a '
                   'great and strong wind as in the vision of the other prophecies, so that they would not fear '
                   'and be terrified. And it says that even so, they hid because of their nakedness. '
                   'And in Bereshit Rabbah (19:7) too they said: R. Abba bar Kahana said, “mehalekh” is not '
                   'written here, but “mithalekh”: it leaped and rose. So R. Abba made it like the language of '
                   '“And the Lord went” (below, 18:33), as we explained the language of going, except that he '
                   'interpreted the verse as the withdrawal of the Shekhinah, which had dwelt in the garden of '
                   'Eden and withdrew from it through the sin of Adam, as in “I will go and return to My place” '
                   '(Hosea 5:15); and we interpret it as the revelation of the Shekhinah in that place, and '
                   'that is the correct and fitting sense of the verse.',
                   'ours', ref='Ramban on Genesis 3:8:1', start='אמרו בבראשית רבה',
                   highlight=['kol', 'mithalekh', 'ruach']),
        question(f'{prefix}-q-b1', h, 26, '1. On what do the commentators disagree?'),
        question(f'{prefix}-q-b2', h, 27, '2. Following which of them did Rambeman [Moses Mendelssohn] '
                 'translate: “Da hörten sie die Stimme des ewigen Wesens, Gott, wandelnd zur Seite des Tages” '
                 '[Then they heard the voice of the Eternal Being, God, walking toward the side of the day]?',
                 highlight=['mithalekh']),
        commentary(f'{prefix}-br-19-8', h, 28, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '… They heard the voice of the trees, which were saying: “The thief who stole the mind of '
                   'his Creator!” (= the knowledge of his Creator).',
                   'ours', ref='Bereshit Rabbah 19:8', highlight=['kol']),
        question(f'{prefix}-q-b3', h, 29, 'What is the idea contained in the words of the midrash?'),

        # §ג — scan header: ג. איכה.
        commentary(f'{prefix}-rekhasim', h, 32, 'HaRekhasim LeBik\'ah', 'הרכסים לבקעה',
                   'HaRekhasim LeBik’ah',
                   'One who seeks to know the place of what is sought will say “Where (eifo) is he?”, “Where '
                   '(eifo) are they pasturing?” (Genesis 37), “Where (eifo) did you glean today?” (Ruth). But '
                   'one who asks “Where (ayyeh) is he?” is only expressing astonishment that he did not find '
                   'him in the usual place (German: wo ist er geblieben, “where has he got to?”): “And where '
                   '(ve-ayyeh) are His wonders that they told us of?” (Judges 6), wo bleiben seine Wunder '
                   '[“what has become of His wonders?”]; “Where (ayyeh) is Sarah your wife?” (Genesis 18) = why '
                   'is she not here with you? “Where (ayyeh) is the Lord, the God of my master Elijah?” (2 Kings '
                   '2) = why is He not with me, to save me like him? And so this “Ayyekah” = why are you '
                   'not in your usual place…',
                   'ours', start='המבקש', highlight=['ayeka'], effect='glow'),
        question(f'{prefix}-q-c', h, 33, 'What is the difficulty that this explanation of the word “Ayyekah” '
                 'resolves?', highlight=['ayeka']),
    ]})

    # §ד — scan header: ד. כ"ב הן האדם היה כאחד ממנו לדעת טוב ורע.
    # Her pointer: עיין רש"י, ראב"ע (עד כמו איש ממנו כ"ג ו' ועוד קרא להלן מן וטעם הפסוק כמו והייתם...) ספורנו;
    secs.append({'id': f'{prefix}-one-of-us', 'titleCard': False, 'title': {'en': '“Like One of Us”'},
                 'primaryText': primary('Genesis 3:22', ['3:22'], {
                     'kechad': ('היה כאחד ממנו', 'has become like any of us'),
                     'ladaat': ('לדעת טוב ורע', 'knowing good and bad'),
                     'pen': ('פן ישלח ידו', 'what if one should stretch out a hand'),
                 }), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 3:22: the Lord God speaks of the human.'),
        commentary(f'{prefix}-rashi-3-22', h, 36, 'Rashi', 'רש"י', 'Rashi',
                   '“Has become like one of us”: Behold, he is unique among the lower beings as I am unique '
                   'among the upper beings. And what is his uniqueness? To know good and evil, which is not so '
                   'of cattle and beasts.',
                   'ours', ref='Rashi on Genesis 3:22:1', highlight=['kechad', 'ladaat']),
        commentary(f'{prefix}-ibn-ezra-3-22', h, 37, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“And [the Lord God] said”: When “eḥad” has a small pataḥ, it carries the accent and its '
                   'sense is absolute; and if it has a large pataḥ, it is construct, as in “as one of the '
                   'tribes of Israel.” Therefore, by the grammar of the language, its meaning cannot be “like '
                   'one”; and what sense would it have? And the master of the accents would have had to join '
                   '“mimmenu” to “to know”… And the sense of the verse is like “and you will be like God, '
                   'knowing good and evil.” Or: he explained it of his thought. And do not wonder at the word '
                   '“mimmenu” [“of us”], for it is like “Let us make man in our image,” “Come, let us go down”: '
                   'and this is the Name speaking with the angels.',
                   'ours', ref='Ibn Ezra on Genesis 3:22:1', highlight=['kechad', 'ladaat']),
        question(f'{prefix}-q-d1', h, 42, '1. Explain Ibn Ezra’s words: “Or: he explained it of his thought,” '
                 'and do not wonder at the word “mimmenu.”', highlight=['kechad']),
        commentary(f'{prefix}-sforno', h, 40, 'Sforno', 'ספורנו', 'Sforno',
                   '“Like one of us, to know good and evil”: He knows good and evil while being in our image; '
                   'and if he were eternal in this condition, he would pursue the pleasant all his days, and '
                   'cast behind his back every intellectual attainment and every good deed, and would not attain '
                   'the spiritual bliss that God, blessed be He, intended in His image and likeness.',
                   'ours', ref='Sforno on Genesis 3:22:1', highlight=['kechad', 'pen']),
        commentary(f'{prefix}-rambam', h, 41, 'Rambam', 'רמב"ם', 'Rambam, Hilkhot Teshuvah',
                   'Free will is given to every person: if he wishes to incline himself to the good way and be '
                   'righteous, the power is in his hand; and if he wishes to incline himself to the evil way and '
                   'be wicked, the power is in his hand. That is what is written in the Torah: “Behold, the man '
                   'has become like one of us, to know good and evil.” That is to say: behold, this species, '
                   'man, has become unique in the world, and there is no second species like it in this '
                   'respect: that he, of himself, by his own mind and thought, knows good and evil and does '
                   'whatever he wishes, and there is none who can hold him back from doing good or evil…',
                   'ours', ref='Mishneh Torah, Repentance 5:1', start='רשות לכל', highlight=['kechad', 'ladaat'],
                   effect='glow'),
        question(f'{prefix}-q-d2', h, 43, '2. How does the Rambam’s view in understanding the verse differ from '
                 'that of all the others? Copy out the verse with punctuation marks according to his '
                 'understanding.', highlight=['kechad', 'ladaat']),
        question(f'{prefix}-q-d3', h, 44, '3. What compels him not to go the way of the other commentators?'),
    ]})
    return secs


# ─── 1964 ───────────────────────────────────────────────────────────────────

def leaf_1964(prefix='sn-1964'):
    """Gilayon תשכ"ד (160638): §א, §ב, §ג. §ד (the accents unit) is the editor's, not hers."""
    h = harvest('sin', '1964')
    secs = []

    # §א — scan header: the verse itself (2:9). Her quote of the Akeidat Yitzhak is one item ([3]),
    # shown in three consecutive slices so each can point at its phrase.
    secs.append({'id': prefix, 'title': {'en': '1964 · The Trees of the Garden'},
                 'primaryText': primary('Genesis 2:9, 3:3', ['2:9', '3:3'], {
                     'min-haadama': ('מן האדמה', 'from the ground'),
                     'nechmad': ('כל עץ נחמד למראה', 'every tree that was pleasing to the sight'),
                     'tov': ('וטוב למאכל', 'good for food'),
                     'chayim': ('ועץ החיים בתוך הגן', 'the tree of life in the middle of the garden'),
                     'daat': ('ועץ הדעת טוב ורע', 'the tree of knowledge of good and bad'),
                     'lo-tigu': ('ולא תגעו בו', 'or touch it'),
                     'mipri': ('ומפרי העץ אשר בתוך הגן', 'fruit of the tree in the middle of the garden'),
                 }), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 2:9: the trees the Lord God causes to grow in the garden.'),
        commentary(f'{prefix}-akeidah-a', h, 3, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   'He caused to grow for him there every tree pleasing to the sight and good for food. He put '
                   'first what belongs to the better, because of its rank; for it is known that such a thing is '
                   'superior to what exists for him by way of necessity, as the Philosopher wrote in the first '
                   'chapter of the Ethics, on friendship: “and it is not only a necessary thing, but also a good '
                   'thing”… And so the things “pleasing to the sight” are the additions to food and their '
                   'variations, the change of flavors and the kinds of their sweetness; and likewise in other '
                   'matters, of clothing and dwelling and the like, those most fitting for people to spend '
                   'their days in good and their years in pleasantness. And of the necessary need he said “and '
                   'good for food,” for this includes food and the other necessary needs without which one '
                   'cannot survive, for they are all necessary like it. And since these two kinds of needs '
                   'belong to the material part, he included them in the mention of one tree, saying “every '
                   'tree pleasing to the sight and good for food,” for they had become one.',
                   'ours', ref='Akeidat Yitzhak, Gate 7', start='הצמיח לו', stop='כי היו לאחדים.',
                   highlight=['nechmad', 'tov']),
        commentary(f'{prefix}-akeidah-b', h, 3, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   'And with them he mentioned “from the ground,” to say that they serve the earthly faculty, '
                   'which he did not say of the other two. But for the absolute intellectual faculty He caused '
                   'to grow for him the tree of life, which is in the middle of the garden; it is what will '
                   'strengthen the intellectual faculty, which gives him the power to grasp the truth of '
                   'intelligible things, to distinguish between truth and falsehood, and to cleave always to '
                   'eternal life, for that is his portion, and “it is a tree of life to those who hold fast to '
                   'it.” And indeed the Lord showed him the tree of life, which is the food of the intellectual '
                   'faculty, as the Torah said of itself (Proverbs 5): “For whoever finds me finds life.” And he '
                   'said that it is “in the middle of the garden,” for so the whole garden will revolve around '
                   'it, for it is the inwardness of all, the root of all and the purpose of all.',
                   'ours', ref='Akeidat Yitzhak, Gate 7', start='והזכיר אצלם', stop='ותכלית הכל.',
                   highlight=['min-haadama', 'chayim']),
        commentary(f'{prefix}-akeidah-c', h, 3, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   'But for reflection by the practical intellect (in all that a person needs, people with '
                   'one another, for a fitting human life, by which he orders the crafts and the laws, the '
                   'settling of states and their governance; for it is necessary that the human intellect be '
                   'perfected in this in order to reach the purely intellectual life; and this is the matter '
                   'the divine Torah strove for in wondrous measure), God saw fit and caused to grow beside the '
                   'tree of life the tree of knowledge of good and evil. He indicated that it is a property of '
                   'this tree that by using it, by its appearance, its smell and its touch, and perhaps by '
                   'merely tasting of it, a person acquires a spirit of knowing good and evil in all these '
                   'matters; for this knowledge is not complete except by knowing both: the good, to cleave to '
                   'it, and the evil, to despise it. '
                   'And so the tree of knowledge was beside the tree of life, to direct him to what is fitting '
                   'of it for reaching the true life, which is the good; not that he should sink into it and '
                   'think it his purpose, for that is the evil, and it is forbidden to him. And this was in the '
                   'manner of what is said in the divine Torah, “See, I set before you this day life and good” '
                   '(Deuteronomy 30), teaching that they are two matters near each other and bordering on each '
                   'other, which do not come apart except for one who knows how to use it properly. '
                   'And most of the Torah, or all of it, is nothing but the ordering of this good, which brings '
                   'a person to life. '
                   'And so with this he has already drawn and engraved, in the making of this garden, the form '
                   'of the world as a whole, and with it the form of the small world, which is man, and all the '
                   'kinds of his life.',
                   'ours', ref='Akeidat Yitzhak, Gate 7', start='אמנם לצורך', highlight=['daat']),
        question(f'{prefix}-q-a1', h, 4, '1. What are the stylistic puzzles in our verse that the author of the '
                 'Akeidah addresses?'),
        question(f'{prefix}-q-a2', h, 5, '2. In his view, what is the relationship between the tree of life and '
                 'the tree of knowledge?', highlight=['chayim', 'daat']),
        question(f'{prefix}-q-a3', h, 6, '3. How does his understanding of the prohibition on eating from the '
                 'tree of knowledge differ from the usual understanding?'),
        question(f'{prefix}-q-a4', h, 7, '4. According to his interpretation, what was the woman’s error in '
                 'saying “nor touch it”?', highlight=['lo-tigu']),
        question(f'{prefix}-q-a5', h, 8, '5. What, in his view, is the aim of the whole Torah, or of most of it, '
                 'and what occasion did he find in our verse to speak of the aim of the whole Torah?'),
        question(f'{prefix}-q-a6', h, 9, '6. How does the author of the Akeidah interpret the verse '
                 'Deuteronomy 30:15?'),

        # §ב — scan header: the verse 2:9 again (digitized: ב. הדגשת "בתוך הגן"). Same panel as §א.
        narration(f'{prefix}-b-intro', '“In the middle of the garden.”', highlight=['chayim']),
        commentary(f'{prefix}-abarbanel', h, 12, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And it is possible to say that “in the middle of the garden” refers to the tree of life alone, '
                   'because it was in the middle of the garden, as Onkelos translated; for life is only in balance '
                   'and in the mean among the qualities. But of the tree of knowledge it did not say that it was '
                   '“in the middle of the garden,” either because it was not in its middle but at its end or near '
                   'its edge, <u>for it was of the nature of the extreme of excess, not of the mean</u>.',
                   'ours', ref='Abarbanel on Torah, Genesis 2:8:1',
                   he=underline(cut(item(h, 12)[0]), 'כי הוא היה מטבע קצה ההפלגה – לא מהמצוע'),
                   highlight=['chayim', 'daat']),
        commentary(f'{prefix}-ibn-kaspi', h, 13, 'Ibn Kaspi', 'אבן כספי', 'Ibn Kaspi',
                   'He did not say of the tree of knowledge that it too was “in the middle of the garden,” for it '
                   'is only at the edge of its border.',
                   'ours', start='לא אמר', highlight=['daat']),
        # Stops at «לנחש»: the rest (her citation and quote of 3:3) is flagged in REVIEW; the panel shows 3:3.
        question(f'{prefix}-q-b', h, 14, 'Explain accordingly why the woman said to the serpent:',
                 stop='לנחש', highlight=['mipri']),
    ]})

    # §ג — scan header: ג. י"ז ומעץ הדעת טוב ורע לא תאכל ממנו...
    secs.append({'id': f'{prefix}-mimmenu', 'titleCard': False, 'title': {'en': '“You Must Not Eat of It”'},
                 'primaryText': primary('Genesis 2:16-17, 3:12', ['2:16', '2:17', '3:12'], {
                     'vaytzav': ('ויצו יהוה אלהים', 'the Lord God commanded'),
                     'lo-tochal': ('לא תאכל ממנו', 'you must not eat of it'),
                     'beyom': ('ביום אכלך ממנו', 'as soon as you eat of it'),
                     'natna': ('הוא נתנה לי מן העץ', 'she gave me of the tree'),
                 }), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 2:16–17: the command. And 3:12: the man’s answer, after the eating.'),
        commentary(f'{prefix}-ramban', h, 17, 'Ramban', 'רמב"ן', 'Ramban',
                   '“You must not eat of it”: He warns him about the fruit, for the tree is not eaten. And so it '
                   'says below, “the fruit of the tree that is in the middle of the garden”; and like it '
                   '(Isaiah 36): “and eat, each of his vine and each of his fig tree”; and so (Genesis 3:17) '
                   '“in toil shall you eat of it”: eat its fruit.',
                   'ours', ref='Ramban on Genesis 2:17:1', highlight=['lo-tochal']),
        commentary(f'{prefix}-ibn-ezra', h, 18, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“And [the Lord God] commanded”: … And since He said “of the tree of knowledge you must not '
                   'eat,” what need is there for the word “mimmenu” [“of it”]? He only added it to make it clear. '
                   'And so (Exodus 2): “she opened it and saw him, the child.” Or its sense is: even a little '
                   'of it.',
                   'ours', ref='Ibn Ezra on Genesis 2:17:1', highlight=['vaytzav', 'lo-tochal']),
        commentary(f'{prefix}-shadal', h, 19, 'Shadal', 'שד"ל', 'Shadal',
                   '“You must not eat of it”: The word “mimmenu” is doubled for emphasis, as below…',
                   'ours', ref='Shadal on Genesis 2:17:1', highlight=['lo-tochal']),
        question(f'{prefix}-q-c1', h, 21, '1. What troubles them?', highlight=['lo-tochal']),
        question(f'{prefix}-q-c2', h, 22, '2. What is the difference between the Ramban and Ibn Ezra in '
                 'resolving the difficulty?'),
        question(f'{prefix}-q-c3', h, 23, '3. Where in our parasha did Shadal find another example of a '
                 'doubling of this kind?'),
        # Stops before the clause the digitization dropped (scan check [20]); see sin.md.
        commentary(f'{prefix}-malbim', h, 20, 'Malbim', 'מלבי"ם', 'Malbim',
                   'And this is a strangeness in the language, as I wrote in my book Ayelet HaShachar, rule '
                   '210 * This was a test for Adam: for Adam erred from this wording, [thinking] that it comes to teach that '
                   'only “of it” you must not eat, that is, from what is attached to the tree; but if the woman '
                   'picks of its fruit and gives it to him, he is permitted to eat. And therefore he said '
                   '(3:12), “The woman gave me of the tree,” for his opinion was that he had not been warned '
                   'about this;',
                   'ours', ref='Malbim on Genesis 2:16:2', start='והוא זרות', stop='שעל זה לא נזהר;',
                   highlight=['lo-tochal', 'natna']),
        commentary(f'{prefix}-ayelet', h, 27, 'Ayelet HaShachar', 'אילת השחר', 'Ayelet HaShachar',
                   'Wherever the pronoun is doubled with the object itself, there is a teaching in it: '
                   '(Leviticus 25:46) “But over your brothers… you shall not rule over him”; and likewise the '
                   'doubling of the pronoun, “mimmenu… min.”',
                   'ours', start='כל מקום', highlight=['lo-tochal']),
        question(f'{prefix}-q-c4', h, 24, '4. How does the Malbim differ from all the other commentators we have '
                 'brought, in resolving this difficulty?'),
        question(f'{prefix}-q-c5', h, 25, '5. What is his proof from Genesis 3:12?', highlight=['natna']),
    ]})

    return secs


# ─── 1968 ───────────────────────────────────────────────────────────────────

def leaf_1968(prefix='sn-1968'):
    """Gilayon תשכ"ח (160442): §ב, §ד, §ו. The other sections are out (pack §7)."""
    h = harvest('sin', '1968')
    secs = []

    # §ב — scan header: ב. ח' וישמעו את קול ה' אלוקים מתהלך בגן לרוח היום.
    secs.append({'id': prefix, 'title': {'en': '1968 · The Sound in the Garden'}, 'primaryText': gen_3_8(),
                 'steps': [
        narration(f'{prefix}-intro', 'Genesis 3:8: after the eating, a sound in the garden.'),
        # [6] is shown in two slices around her «*» (a pointer to the teacher's guide).
        commentary(f'{prefix}-br-19-7', h, 6, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And they heard the voice of the Lord God walking in the garden”: R. Chalafon said, we have '
                   'learned that a voice has walking, as it says, “And they heard the voice of the Lord… '
                   'walking…”; and fire has walking, as it says (Exodus 9), “and fire walked down to the '
                   'earth.” R. Abba bar Kahana said: “mehalekh” is not written here, but “mithalekh”: it leaped '
                   'and rose. The essential place of the Shekhinah was among the lower beings',
                   'ours', ref='Bereshit Rabbah 19:7', stop='בתחתונים היתה', highlight=['kol', 'mithalekh']),
        commentary(f'{prefix}-br-19-7b', h, 6, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'when the first Adam sinned, the Shekhinah withdrew to the first firmament; Cain sinned, it '
                   'withdrew to the second firmament; the generation of Enosh, to the third; the generation of '
                   'the flood, to the fourth…',
                   'ours', ref='Bereshit Rabbah 19:7', start='כיון שחטא', highlight=['mithalekh']),
        commentary(f'{prefix}-rashi', h, 7, 'Rashi', 'רש"י', 'Rashi',
                   '“And they heard”: They heard the voice of the Holy One, blessed be He, who was walking in '
                   'the garden.',
                   'ours', ref='Rashi on Genesis 3:8:1', highlight=['kol', 'mithalekh']),
        commentary(f'{prefix}-moreh', h, 8, 'Rambam', 'רמב"ם', 'Rambam, Moreh Nevukhim',
                   '“Walking” is likewise one of the terms laid down for particular movements of living beings: '
                   '(Genesis 32) “And Jacob went on his way”; and this is frequent (= this usage is common in the '
                   'language). And the term was then borrowed for the flowing of bodies finer than the bodies of '
                   'living beings: (Genesis 8:5) “And the waters went on diminishing,” (Exodus 9:23) “and fire went '
                   'down to the earth.” And after that it was borrowed for the spreading and showing of a thing, '
                   'even though it is no body at all: it says (Jeremiah 46) “Her sound shall go like the '
                   'serpent’s” (= the report of the calamity coming upon them, upon Egypt, comes and spreads like '
                   'the hissing of a snake. Commentary of Even Shmuel); and so they said (Genesis 3): “the voice '
                   'of the Lord God walking in the garden”: it is the “voice” of which it is said that it is '
                   '“walking.”',
                   'ours', ref='Moreh Nevukhim 1:24', start='"ההליכה"', highlight=['kol', 'mithalekh']),
        commentary(f'{prefix}-radak', h, 9, 'Radak', 'רד"ק', 'Radak',
                   '“And they heard”: Some explain: while Adam was walking in the garden he heard the voice of '
                   'God. But since it says “they heard,” it should have said “mithalkhim” [they were walking]. '
                   'The correct view is that “mithalekh” refers to the voice of the Lord, for we find “walking” '
                   'said of it: (Jeremiah 46:22) “Her sound shall go like the serpent’s”…',
                   'ours', ref='Radak on Genesis 3:8:1', highlight=['mithalekh']),
        commentary(f'{prefix}-ramban', h, 10, 'Ramban', 'רמב"ן', 'Ramban',
                   '(After citing the midrash and the Rambam:) “And they heard the voice of the Lord God walking '
                   'in the garden”: And in my view, the sense of “walking in the garden of Eden” is like the '
                   'sense of (Leviticus 26:12) “And I will walk among you,” (Genesis 18:33) “And the Lord went, '
                   'when He had finished speaking to Abraham,” (Hosea 5:15) “I will go and return to My place”: '
                   'it concerns the revelation of the Shekhinah in that place, or its withdrawal from the place '
                   'where it was revealed. And the sense of “to the wind of the day”: when the Shekhinah is '
                   'revealed, a great and strong wind comes, as it is said (1 Kings 19:11), “And behold, the '
                   'Lord passed by, and a great and strong wind, rending mountains and shattering rocks before '
                   'the Lord”; and so (Psalms 18:11), “He soared on the wings of the wind.” And it is written '
                   'in Job (31:1), “And the Lord answered Job out of the whirlwind.” And therefore they said here '
                   '“that they heard the voice of the Lord, for the Shekhinah was revealed in the garden as '
                   'drawing near to them to the wind of the day: for the wind of the Lord blew in it, in the '
                   'garden, like the wind of the days, not a great and strong wind in a vision, as in the other '
                   'prophecies, so that they would not fear and be terrified.',
                   'ours', ref='Ramban on Genesis 3:8:1', start='(אחרי', highlight=['mithalekh', 'ruach']),
        question(f'{prefix}-q-b1', h, 11, '1. What is the syntactic difficulty in our verse?',
                 highlight=['mithalekh']),
        question(f'{prefix}-q-b2', h, 12, '2. How many different views were stated above in resolving the '
                 'syntactic question? Sort the commentators into groups!'),
        question(f'{prefix}-q-b3', h, 13, '3. How does the Ramban’s view differ from that of R. Abba bar Kahana '
                 '(apart from the syntactic question)? Which of the two seems to you better suited to the '
                 'context?'),
        question(f'{prefix}-q-b4', h, 14, '4. Why does R. Chalafon mention “fire” too in his words? What has it '
                 'to do with our matter?'),
    ]})

    # §ד — scan header: ד. י"ב האשה אשר נתת עמדי.
    secs.append({'id': f'{prefix}-gave', 'titleCard': False, 'title': {'en': '“The Woman You Put at My Side”'},
                 'primaryText': primary('Genesis 3:12', ['3:12'], {
                     'natatta': ('אשר נתתה עמדי', 'You put at my side'),
                     'natna': ('הוא נתנה לי מן העץ', 'she gave me of the tree'),
                 }), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 3:12: the man answers.'),
        commentary(f'{prefix}-rashi-3-12', h, 21, 'Rashi', 'רש"י', 'Rashi',
                   '“Whom You put at my side”: Here he denied the good done him.',
                   'ours', ref='Rashi on Genesis 3:12:1', highlight=['natatta']),
        commentary(f'{prefix}-ramban-3-12', h, 22, 'Ramban', 'רמב"ן', 'Ramban',
                   '“The woman You put at my side”: That is to say: the woman whom You, in Your glory, gave me as '
                   'a helper, she gave me of the tree; and I thought that whatever she would say to me would be '
                   'a help to me and of benefit. And this is what He said in his punishment, “Because you '
                   'listened to the voice of your wife”: that you were not careful against transgressing My '
                   'commandments on account of her counsel. And our Rabbis call him in this “ungrateful” '
                   '(Avodah Zarah 5b): they mean to explain that he answered Him, You caused me this stumbling, '
                   'for You gave me a woman as a helper, and she counseled me to do wrong.',
                   'ours', ref='Ramban on Genesis 3:12:1', highlight=['natatta', 'natna']),
        question(f'{prefix}-q-d1', h, 23, '1. What troubles both of them in our verse?'),
        question(f'{prefix}-q-d2', h, 24, '2. What is the difference between the two interpretations?'),
        question(f'{prefix}-q-d3', h, 25, '3. For which of the two can proof be brought from the double use of '
                 'the root “natan” [give] in our verse: “The woman whom You gave (natatta) to be with me, she '
                 'gave (natenah) me of the tree”?', highlight=['natatta', 'natna']),
    ]})

    # §ו — scan header: ו. י"ג ותאמר האשה הנחש השיאני
    secs.append({'id': f'{prefix}-duped', 'titleCard': False, 'title': {'en': '“The Serpent Duped Me”'},
                 'primaryText': primary('Genesis 3:13-14', ['3:13', '3:14'], {
                     'hishiani': ('הנחש השיאני', 'The serpent duped me'),
                     'ki-asita': ('כי עשית זאת', 'Because you did this'),
                 }), 'steps': [
        narration(f'{prefix}-f-intro', 'Genesis 3:13–14: the woman answers; then the Lord God turns to the serpent.'),
        commentary(f'{prefix}-rashi-3-13', h, 40, 'Rashi', 'רש"י', 'Rashi',
                   '“Duped me” (hishi’ani): misled me, as in (2 Kings 18) “Let not Hezekiah deceive (yashi) you.”',
                   'ours', ref='Rashi on Genesis 3:13:1', highlight=['hishiani']),
        commentary(f'{prefix}-mizrachi', h, 41, 'Mizrachi', 'ר\' אליהו מזרחי', 'R. Eliyahu Mizrachi',
                   'Not in the sense of incitement and enticement, for if so, this is no answer to the words of '
                   'the Lord!',
                   'ours', ref='Mizrachi, Genesis 3:13:1', start='לא לשון', highlight=['hishiani']),
        commentary(f'{prefix}-gur-aryeh', h, 42, 'Gur Aryeh', 'גור אריה', 'Gur Aryeh',
                   'Not in the sense of incitement, for that is no answer for a sinner: they say to him, “Why '
                   'did you sin?” and he replies, “So-and-so incited me.”',
                   'ours', start='לא לשון', highlight=['hishiani']),
        commentary(f'{prefix}-rashi-3-14', h, 43, 'Rashi', 'רש"י', 'Rashi',
                   '“Because you did this”: From here, that one does not plead in favor of the inciter…',
                   'ours', ref='Rashi on Genesis 3:14:1', start='ד"ה', highlight=['ki-asita']),
        commentary(f'{prefix}-reem', h, 44, 'Re\'em', 'הרא"ם', 'Re’em',
                   'One may wonder at Rashi’s words on “Because you did this”: if so, this “deceiving” '
                   '(hashsha’ah) is “inciting” (hasatah)?',
                   'ours', start='יש לתמוה', highlight=['ki-asita', 'hishiani']),
        commentary(f'{prefix}-heilprin', h, 45, 'R. Eliezer Heilprin', 'ר\' אליעזר היילפרין',
                   'R. Eliezer Heilprin',
                   'According to what the masters of the language have established about the difference between '
                   '“mashi” [one who deceives] and “mesit” [one who incites], the Re’em’s complaint against Rashi '
                   'falls away.',
                   'ours', start='לפי מה', highlight=['hishiani']),
        question(f'{prefix}-q-f2', h, 47, '2. If so, why did the woman say “hishi’ani” [he deceived me] and not '
                 '“hesitani” [he incited me]?', highlight=['hishiani'], effect='glow'),
    ]})
    return secs
