from bereshit_lib import *  # noqa: F401,F403
"""Theme 4 — Cain and Abel (Gen 4:1–16): leaves 1942, 1956, 1958.

Paper trail: research/parshiyot/bereshit-leaves/cain.md (slices, omissions, open items).
"""


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_4_5_7():
    return primary('Genesis 4:5-7', ['4:5', '4:6', '4:7'], {
        'yafelu': ('ויחר לקין מאד ויפלו פניו', 'Cain was much distressed and his face fell'),
        'lama': ('למה חרה לך ולמה נפלו פניך', 'Why are you distressed, And why is your face fallen?'),
        'seet': ('הלוא אם תיטיב שאת', 'Surely, if you do right, There is uplift'),
        'lo-teitiv': ('ואם לא תיטיב', 'But if you do not do right'),
        'lapetach': ('לפתח חטאת רבץ', 'Sin couches at the door'),
        'teshukato': ('ואליך תשוקתו', 'Its urge is toward you'),
        'timshol': ('ואתה תמשל בו', 'Yet you can be its master'),
    })


def gen_4_13_15():
    return primary('Genesis 4:13-15', ['4:13', '4:14', '4:15'], {
        'gadol': ('גדול עוני מנשא', 'My punishment is too great to bear'),
        'gerashta': ('הן גרשת אתי היום מעל פני האדמה', 'Since You have banished me this day from the soil'),
        'esater': ('ומפניך אסתר', 'I must avoid Your presence'),
        'na-vanad': ('והייתי נע ונד בארץ', 'become a restless wanderer on earth'),
        'motsi': ('והיה כל מצאי יהרגני', 'anyone who meets me may kill me'),
        'shivatayim': ('לכן כל הרג קין שבעתים יקם', 'if anyone kills Cain, sevenfold vengeance shall be exacted'),
        'ot': ('וישם יהוה לקין אות', 'the Lord put a mark on Cain'),
    })


def gen_4_16():
    return primary('Genesis 4:16', ['4:16'], {
        'vayetze': ('ויצא קין מלפני יהוה', 'Cain left the Lord’s presence'),
        'nod': ('וישב בארץ נוד קדמת עדן', 'settled in the land of Nod, east of Eden'),
    })


def comparison_4_3():
    """1958 §ב: her two-column table, chapter 4 on the right and chapter 3 on the left, as she set it."""
    lhe, len_ = verse_set(['3:9', '3:13'])
    rhe, ren = verse_set(['4:9', '4:10'])
    left = words(lhe, len_, {
        'ayekah': ('ויאמר לו איכה', 'said to him, “Where are you?”'),
        'ma-zot': ('מה זאת עשית', 'What is this you have done!'),
    })
    right = words(rhe, ren, {
        'ei-hevel': ('אי הבל אחיך', 'Where is your brother Abel?'),
        'meh-asita': ('מה עשית', 'What have you done?'),
    })
    for w in left.values():
        w['side'] = 'left'
    for w in right.values():
        w['side'] = 'right'
    return {'ref': 'Genesis 4:9-10; 3:9, 13', 'mode': 'comparison',
            'left': {'ref': 'Genesis 3:9, 13', 'he': lhe, 'en': len_},
            'right': {'ref': 'Genesis 4:9-10', 'he': rhe, 'en': ren},
            'words': {**left, **right}}


# ─── 1942 ───────────────────────────────────────────────────────────────────

def leaf_1942(prefix='cn-1942'):
    """Gilayon תש"ב (161880), her earliest Bereshit sheet: §ב, §ה, §ז, §ט (pack §7)."""
    h = harvest('cain', '1942')
    secs = []

    # §ב — scan header: ב. פסוק ז.  Her Q1 ([7]) names the commentators that follow, so it leads;
    # Q2 ([15]) asks about Rashi and Sforno and closes the section. Both are the digitization's
    # wording (the scan's doubtful letters were not carried into the harvest); see cain.md.
    secs.append({'id': prefix, 'title': {'en': '1942 · Sin Couches at the Door'},
                 'primaryText': gen_4_5_7(), 'steps': [
        narration(f'{prefix}-intro', 'Cain’s offering is not accepted, and his face falls. God speaks to him.'),
        question(f'{prefix}-q-b1', h, 7, '1. What is the meaning of the words “im teitiv – se’et” according to Rashi, Ramban, Ibn Ezra, Sforno?', highlight=['seet']),
        commentary(f'{prefix}-rashi', h, 8, 'Rashi', 'רש"י', 'Rashi',
                   '“Surely, if you do well”: its meaning is as the Targum renders it.',
                   'ours', ref='Rashi on Genesis 4:7:1', highlight=['seet']),
        commentary(f'{prefix}-ibn-ezra', h, 9, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'On “Surely”: In the view of many commentators, se’et means [the bearing of] your sin. '
                   'What is right in my eyes is the lifting of the face, for it is written just before, '
                   '“and his face fell,” and that is the way of shame, as in “how could I lift up my face.” '
                   'And its sense: if you have done good, you will lift up your face; and so “for then you '
                   'will lift up your face without blemish” (Job 14:15 [the verse is Job 11:15]).',
                   'ours', ref='Ibn Ezra on Genesis 4:7:1', highlight=['seet', 'yafelu']),
        commentary(f'{prefix}-ramban-a', h, 10, 'Ramban', 'רמב"ן', 'Ramban',
                   '“Surely, if you do well, se’et”: In the view of the commentators (Onkelos, Rashi and '
                   'Radak), se’et is [the bearing of] your sin. In the view of R. Avraham [Ibn Ezra], it is '
                   'the lifting of your face, answering “why is your face fallen,” for one who is ashamed '
                   'bows his face downward, as in “and the light of my face they did not cast down” (Job '
                   '29:24); and one who honors another, as it were, lifts his face upward. And this is the '
                   'sense of “perhaps he will lift up my face” (below, 32:21), “you shall not lift up the '
                   'face of the poor” (Leviticus 19:15).',
                   'ours', ref='Ramban on Genesis 4:7:1', stop='ויקרא יט טו).', highlight=['seet', 'lama']),
        commentary(f'{prefix}-ramban-b', h, 10, 'Ramban', 'רמב"ן', 'Ramban',
                   'But in my view: “if you do well,” you will have se’et over and above your brother, for '
                   'you are the firstborn. And this is the sense of “why are you distressed”: for in his '
                   'shame before his brother his face fell, and in his jealousy of him he killed him. So He '
                   'said to him: “Why are you distressed” about your brother, “and why is your face fallen” '
                   'before him? “Surely, if you do well,” you will have se’et over and above your brother; '
                   '“and if you do not do well,” not with him alone will harm come to you, for at the door '
                   'of your house your sin couches, to make you stumble in all your ways. “And its urge is '
                   'toward you”: it will long to cling to you all your days; but “you can rule over it,” if '
                   'you wish, for you will mend your ways and remove it from you. He taught him about '
                   'repentance: that it is in his hand to return whenever he wishes, and He will forgive him.',
                   'ours', ref='Ramban on Genesis 4:7:1', start='ועל דעתי',
                   highlight=['seet', 'lo-teitiv', 'lapetach', 'teshukato', 'timshol']),
        narration(f'{prefix}-reuben', 'Genesis 49:3 uses the same word, in Jacob’s words to Reuben, his '
                  'firstborn: “exceeding in rank,” yeter se’et.', highlight=['seet']),
        commentary(f'{prefix}-ramban-49', h, 11, 'Ramban', 'רמב"ן', 'Ramban',
                   'The construction of this verse: “Reuben, you are my firstborn and my might and the '
                   'first of my vigor, in the excess of my se’et and the excess of my strength.” And its '
                   'meaning: you are the firstborn of my might and the first of my vigor, when I was in an '
                   'excess of se’et and eminence (as in the language “Shall not His se’et terrify you” (Job '
                   '13:11), “at his se’et the mighty are afraid” (ibid. 41:17): loftiness and greatness), and '
                   'when I was in an excess of strength for war, as in “and He will give strength to His '
                   'king” (1 Samuel 2:10), “and the might of war” (Isaiah 42:25).',
                   'ours', ref='Ramban on Genesis 49:3:1', start='שיעור הפסוק הזה', highlight=['seet']),
        commentary(f'{prefix}-ibn-ezra-49', h, 12, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'On “exceeding in se’et”: you were fit for pre-eminence over all, to be raised up.',
                   'ours', ref='Ibn Ezra on Genesis 49:3:2', highlight=['seet']),
        commentary(f'{prefix}-sforno-a', h, 13, 'Sforno', 'ספורנו', 'Sforno',
                   'On “Surely, if you do well”: [improve] yourself, and strive that you too be found pleasing.',
                   'ours', ref='Sforno on Genesis 4:7:1', highlight=['seet']),
        commentary(f'{prefix}-sforno-b', h, 14, 'Sforno', 'ספורנו', 'Sforno',
                   'On “se’et”: the height of eminence and of being raised up couches before you, ready to '
                   'be yours. “And if you do not do well, sin couches at the door”: sin, too, is ready before '
                   'you, for you will add willful transgression to your sin; for such is the way of the evil '
                   'inclination.',
                   'ours', ref='Sforno on Genesis 4:7:2-3', highlight=['seet', 'lo-teitiv', 'lapetach']),
        question(f'{prefix}-q-b2', h, 15, '2. To whom does the pronoun in the word “teshukato” and in the word '
                 '“bo” refer, according to Rashi and Sforno?', highlight=['teshukato', 'timshol']),
    ]})

    # §ה — scan header: ה. פסוק י"ג.  §ז — scan header: ז. פסוק ט"ו.
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“Too Great to Bear”'},
                 'primaryText': gen_4_13_15(), 'steps': [
        narration(f'{prefix}-h-intro', 'Cain answers his sentence.'),
        commentary(f'{prefix}-h-rashi', h, 29, 'Rashi', 'רש"י', 'Rashi',
                   'As a question: You bear the worlds above and below, and my sin cannot be borne?',
                   'ours', ref='Rashi on Genesis 4:13:1', highlight=['gadol']),
        # Her stop «עד למלים חרפת נעורי» is where the digitized item ends.
        commentary(f'{prefix}-h-ramban', h, 30, 'Ramban', 'רמב"ן', 'Ramban',
                   '“As a question: You bear the worlds above and below, and my sin cannot be borne?” — '
                   'Rashi’s wording, from Bereshit Rabbah (22:11). But the right plain sense is that it is a '
                   'confession. He said: True, my sin is too great to be forgiven, and You are righteous, O '
                   'Lord, and Your judgments are upright, even though You have punished me very greatly. And '
                   'behold, “You have banished me this day from the face of the soil,” for since I am a '
                   'wanderer and a fugitive and cannot stay in one place, I am driven from the soil and have '
                   'no place of rest; “and from Your face I shall be hidden,” for I cannot stand before You '
                   'to pray or to bring a sacrifice and an offering, for I am ashamed and also confounded, '
                   'for I bear the disgrace of my youth.',
                   'ours', ref='Ramban on Genesis 4:13:1', stop='חרפת נעורי',
                   highlight=['gadol', 'gerashta', 'esater']),
        commentary(f'{prefix}-h-ibn-ezra', h, 31, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'In the view of all the commentators, he confessed his sin, and neso has the sense of '
                   'forgiving, as in “forgiving iniquity.” But in my view: the Hebrews call the consequence '
                   '[of a deed] “reward,” and the evil punishment that comes because of iniquity, “sin.” And '
                   'so “for the iniquity of the Amorites is not yet complete,” “if iniquity befalls you,” '
                   '“the iniquity of the daughter of my people was great.” And the sense is: this punishment '
                   'is great, I cannot endure it. And the verse that follows shows the truth of this '
                   'interpretation.',
                   'ours', ref='Ibn Ezra on Genesis 4:13:1', highlight=['gadol', 'gerashta']),
        # [32] in the digitization's wording, which drops her Ramban stop-pointer (honored above).
        question(f'{prefix}-q-h', h, 32, 'What is the difference between Rashi, Ramban and Ibn Ezra in '
                 'explaining the words “gadol avoni mi-neso”? What is the weakness of Rashi, and what is the '
                 'weakness of Ramban, in explaining these words?', highlight=['gadol']),

        narration(f'{prefix}-z-intro', '“And the Lord put a mark on Cain.”', highlight=['ot']),
        # [41], the variant reading of Rashi, is the digitizer's addition; the scan says only «רש"י».
        commentary(f'{prefix}-z-rashi', h, 40, 'Rashi', 'רש"י', 'Rashi',
                   'He engraved on his forehead a letter of His Name.',
                   'ours', ref='Rashi on Genesis 4:15:3', highlight=['ot']),
        commentary(f'{prefix}-z-ibn-ezra', h, 42, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And one says that the sign was a horn. And others said that He put strength in his heart '
                   'and removed his fear from him. And what is right in my eyes is that God made him a sign '
                   'until he believed, and Scripture did not reveal the sign.',
                   'ours', ref='Ibn Ezra on Genesis 4:15:2', start='ויש אומר, כי האות',
                   highlight=['ot', 'shivatayim']),
        commentary(f'{prefix}-z-ramban', h, 43, 'Ramban', 'רמב"ן', 'Ramban',
                   'For since I shall be a wanderer and a fugitive, and shall not build myself a house and '
                   'walls in any place, the beasts will kill me, for Your shadow has departed from me. He '
                   'acknowledged that man is not exalted and saved by his own strength, but only by the '
                   'protection of the Most High over him.',
                   'ours', ref='Ramban on Genesis 4:13:1', start='כי בעבור שאהיה נע ונד',
                   highlight=['na-vanad', 'motsi']),
        question(f'{prefix}-q-z', h, 39, 'The sages differ about Cain’s sign, since it is not spelled out in '
                 'the Torah. What is the sign according to the interpretation of Rashi; Ibn Ezra (on '
                 '“sevenfold,” from the words “And one says that the sign…”); Ramban (verse 13, on “gadol '
                 'avoni mi-neso,” from the words “for since I shall be a wanderer and a fugitive”)?',
                 highlight=['ot']),
    ]})

    # §ט — scan: ט. על הפסוק ט"ז "ויצא קין מלפני ה'", ישנה מחלוקת במדרש רבה:
    # [51] in the digitization's wording (R. Aibu, R. Chanina bar R. Yitzhak), her gloss on הפשיל
    # included; it starts after the lead-in «ישנה מחלוקת במדרש בראשית רבה:».
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Cain Left the Lord’s Presence”'},
                 'primaryText': gen_4_16(), 'steps': [
        narration(f'{prefix}-t-intro', 'Genesis 4:16.'),
        commentary(f'{prefix}-br', h, 51, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And Cain went out.” From where did he go out? R. Aibu says: He threw the words behind '
                   'him (that is, he cast the words of the Holy One, blessed be He, behind his back, like a '
                   'man who slings his gear behind him), and went out like one who deceives the One above. '
                   'R. Chanina bar R. Yitzhak says: He went out rejoicing… Adam the first man met him. He said '
                   'to him: What became of your judgment? He said to him: I repented, and came to terms. Adam '
                   'began to strike his face, and said: “A psalm, a song for the Sabbath day: it is good to '
                   'give thanks to the Lord.”',
                   'ours', ref='Bereshit Rabbah 22:13', start='ויצא קין.', highlight=['vayetze']),
        question(f'{prefix}-q-t', h, 52, 'Which of these two answers is closer to the plain sense of Scripture? '
                 'Which of our commentators also leans toward the view that Cain repented?',
                 highlight=['vayetze']),
    ]})
    return secs


# ─── 1956 ───────────────────────────────────────────────────────────────────

def leaf_1956(prefix='cn-1956'):
    """Gilayon תשט"ז (161216): §א, §ב (chosen Rashi questions), §ג (4:7 again)."""
    h = harvest('cain', '1956')
    secs = []

    # §א — scan header: א. שאלה כללית לפרקנו:
    secs.append({'id': prefix, 'title': {'en': '1956 · “In the Field”'},
                 'primaryText': primary('Genesis 4:8', ['4:8'], {
                     'vayomer': ('ויאמר קין אל הבל אחיו', 'Cain said to his brother Abel'),
                     'basadeh': ('ויהי בהיותם בשדה', 'when they were in the field'),
                     'vayakom': ('ויקם קין אל הבל אחיו ויהרגהו', 'Cain set upon his brother Abel and killed him'),
                 }), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 4:8: in the field, Cain kills his brother.'),
        # The parenthetical Hebrew glosses of the Aramaic are translated once, with the Aramaic.
        commentary(f'{prefix}-br-1', h, 3, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And Cain said to Abel his brother, and when they were in the field” — what were they '
                   'quarreling about? They said: “Come, let us divide the world.” One took the land and one '
                   'took the movable goods. This one said: “The land you are standing on is mine.” And that '
                   'one said: “What you are wearing is mine.” This one said: “Strip!” That one said: “Fly!” '
                   'Out of this, “Cain rose up against Abel his brother and killed him.”',
                   'ours', ref='Bereshit Rabbah 22:7', stop='ויהרגהו"', highlight=['vayomer', 'vayakom']),
        commentary(f'{prefix}-br-2', h, 3, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Yehoshua of Sikhnin said in the name of R. Levi: Both took the land, and both took '
                   'the movable goods. So what were they quarreling about? This one said: “The Temple will '
                   'be built in my territory,” and that one said: “The Temple will be built in my '
                   'territory,” as it is said, “and when they were in the field,” and “field” means nothing '
                   'but the Temple, as it is written (Micah 3), “Zion shall be plowed as a field.” And out of '
                   'this, “Cain rose up against Abel his brother and killed him.”',
                   'ours', ref='Bereshit Rabbah 22:7', start='ר\' יהושע דסכנין', stop='ויהרגהו"',
                   highlight=['basadeh', 'vayakom']),
        commentary(f'{prefix}-br-3', h, 3, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'Yehudah bar Ami said: They were quarreling over the first Eve.',
                   'ours', ref='Bereshit Rabbah 22:7', start='יהודה בר\' אמי', highlight=['vayakom']),
        question(f'{prefix}-q-a1', h, 4, '1. The midrash deals with the causes of hatreds, quarrels, wars and '
                 'killings between human beings. Explain the intent of each of the three views stated here.'),
        question(f'{prefix}-q-a2', h, 5, '2. Why did the midrash see fit to bring the views in this order?'),
    ]})

    # §ב — scan header: ב. שאלות ודיוקים ברש"י:  Chosen: Rashi on 4:1, 4:7 (two comments), 4:8, 4:10.
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'From Cain’s Birth to Abel’s Blood'},
                 'primaryText': primary('Genesis 4:1, 7-8, 10', ['4:1', '4:7', '4:8', '4:10'], {
                     'yada': ('והאדם ידע את חוה אשתו', 'Now the Human knew his wife Eve'),
                     'lapetach': ('לפתח חטאת רבץ', 'Sin couches at the door'),
                     'teshukato': ('ואליך תשוקתו', 'Its urge is toward you'),
                     'vayomer': ('ויאמר קין אל הבל אחיו', 'Cain said to his brother Abel'),
                     'demei': ('קול דמי אחיך', 'your brother’s blood'),
                 }), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 4:1 to 4:10, from Cain’s birth to Abel’s blood.'),
        commentary(f'{prefix}-rashi-4-1', h, 7, 'Rashi', 'רש"י', 'Rashi',
                   '“And the man knew” (ve-ha-adam yada): already before the matter above, before he sinned '
                   'and was driven out of the Garden of Eden; and so too the conception and the birth. For '
                   'had it written “va-yeda ha-adam,” it would imply that he had children after he was '
                   'driven out.',
                   'ours', ref='Rashi on Genesis 4:1:1', highlight=['yada']),
        question(f'{prefix}-q-b1a', h, 8, 'a. Bring examples of this linguistic rule, on which Rashi’s words are '
                 'built, from other places in the book of Genesis!', highlight=['yada']),
        question(f'{prefix}-q-b1b', h, 9, 'b. Explain: what is the significance of these words of Rashi from the '
                 'standpoint of ideas?'),
        commentary(f'{prefix}-rashi-4-7a', h, 17, 'Rashi', 'רש"י', 'Rashi',
                   '“Sin couches at the door”: at the door of your grave, your sin is kept.',
                   'ours', ref='Rashi on Genesis 4:7:2', highlight=['lapetach']),
        commentary(f'{prefix}-rashi-4-7b', h, 18, 'Rashi', 'רש"י', 'Rashi',
                   '“And its urge is toward you”: [the urge] of sin — that is the evil inclination — it '
                   'always longs and yearns to make you stumble.',
                   'ours', ref='Rashi on Genesis 4:7:3', highlight=['teshukato']),
        question(f'{prefix}-q-b5a', h, 19, 'a. Why did he not explain it according to its plain sense: that sin '
                 'couches at the door of your house, and you will stumble on it always, in your going out and '
                 'your coming in?', highlight=['lapetach']),
        question(f'{prefix}-q-b5b', h, 20, 'b. Explain why Rashi interpreted “sin” as the evil inclination in his '
                 'comment on “and its urge is toward you,” and did not so interpret it in his comment on “sin '
                 'couches at the door,” where the word “sin” appears. Note that in the comment on “at the door” '
                 'Rashi said “your sin,” and in the comment on “and its urge is toward you” he said: sin, '
                 'without a pronoun.', highlight=['lapetach', 'teshukato']),
        question(f'{prefix}-q-b5c', h, 21, 'c. Why did Rashi see fit to use two verbs, “longs and yearns,” and not '
                 'make do with one?', highlight=['teshukato']),
        commentary(f'{prefix}-rashi-4-8', h, 22, 'Rashi', 'רש"י', 'Rashi',
                   '“And Cain said”: he entered into words of quarrel and strife with him, to find a pretext '
                   'against him to kill him. There are aggadic midrashim on this, but this is the plain '
                   'settling of the verse.',
                   'ours', ref='Rashi on Genesis 4:8:1', highlight=['vayomer']),
        question(f'{prefix}-q-b6a', h, 23, 'a. What is difficult for him?', highlight=['vayomer']),
        question(f'{prefix}-q-b6b', h, 24, 'b. By “aggadic midrashim” he meant the three views stated in '
                 'Bereshit Rabbah (see question A). Why did Rashi not bring one of them, and in what does his '
                 'interpretation differ from them in principle?'),
        commentary(f'{prefix}-rashi-4-10', h, 25, 'Rashi', 'רש"י', 'Rashi',
                   '“Your brother’s blood” [demei, literally “bloods”]: his blood and the blood of his '
                   'descendants.',
                   'ours', ref='Rashi on Genesis 4:10:1', highlight=['demei']),
        question(f'{prefix}-q-b7b', h, 26, 'b. Explain the idea symbolized in these words of his.'),
        question(f'{prefix}-q-b7c', h, 27, 'c. Where do we find this idea elsewhere in Rashi on the Torah?'),
    ]})

    # §ג — scan: ג. ז הלא אם תטיב שאת ... (the verse). [30] and [32]–[34] are Rashi in the scan
    # («רש"י ד"ה …», then ditto marks); the digitization mislabels them. [32]–[33] repeat [17]–[18]
    # above and are omitted; [34] is kept because her question 4 asks about it.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Surely, If You Do Right”'},
                 'primaryText': gen_4_5_7(), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 4:5–7: God speaks to Cain.'),
        commentary(f'{prefix}-c-rashi-a', h, 30, 'Rashi', 'רש"י', 'Rashi',
                   '“Surely, if you do well, se’et”: its meaning is as its Targum renders it.',
                   'ours', ref='Rashi on Genesis 4:7:1', highlight=['seet']),
        commentary(f'{prefix}-c-onkelos', h, 31, 'Onkelos', 'תרגום אונקלוס', 'Onkelos',
                   'Surely, if you do well in your work (your deeds), it will be forgiven you (it will be '
                   'pardoned you).',
                   'ours', ref='Onkelos Genesis 4:7', highlight=['seet']),
        commentary(f'{prefix}-c-rashi-b', h, 34, 'Rashi', 'רש"י', 'Rashi',
                   '“And you can rule over it”: if you wish, you will overcome it.',
                   'ours', ref='Rashi on Genesis 4:7:4', start='ד"ה ואתה', highlight=['timshol']),
        commentary(f'{prefix}-c-malbim', h, 35, 'Malbim', 'מלבי"ם', 'Malbim',
                   'On “Surely”: He revealed to him that the Lord has no desire for the offering, but rather '
                   '“behold, to obey is better than sacrifice” (1 Samuel 13 [the verse is 1 Samuel 15:22]); '
                   'and the main thing is that you improve your deeds, not improving the gift (mas’et) and the '
                   'offering. If you improve the gift, it will not be accepted in His eyes; for whether you '
                   'improve the gift or do not improve it, there is no merit in it, since at the door sin '
                   'couches to accuse you… And he made three things clear in this: (a) that the evil '
                   'inclination couches at the door, and a person must look to the beginning of all his deeds, '
                   'that he not make the servant king over his master; for it lies in wait at the door, so '
                   'that whenever the door is opened it will come in to you and cast into you the venom of '
                   'desire and sin. (b) He further informed him that on the one side, the inclination longs '
                   'for you, to make you sin and bring you down. (c) That on the other side, you have in your '
                   'hand the strength and the equal power to rule over it, by the power of freedom that is in '
                   'man; for only in this respect is man called free: if he rules over his beast, not if his '
                   'beast rules over him.',
                   'ours', ref='Malbim on Genesis 4:7:1', highlight=['seet', 'lapetach', 'teshukato', 'timshol']),
        question(f'{prefix}-q-c1', h, 36, '1. Copy our verse twice, and mark it with punctuation according to each '
                 'of the commentators above.'),
        question(f'{prefix}-q-c2', h, 37, '2. Explain what the word “se’et” means according to each of the two '
                 'interpretations, and bring proofs from other places in the Torah for each of the two meanings.',
                 highlight=['seet']),
        question(f'{prefix}-q-c3', h, 38, '3. Explain how our verse connects to verses 5–6, according to each of '
                 'the two interpretations.', highlight=['yafelu', 'lama']),
        question(f'{prefix}-q-c4', h, 39, '4. What did Rashi correct in his words on “and you can rule over it”; '
                 'what would Scripture lack without his interpretation?', highlight=['timshol']),
    ]})
    return secs


# ─── 1958 ───────────────────────────────────────────────────────────────────

def leaf_1958(prefix='cn-1958'):
    """Gilayon תשי"ח (161141): §א (structure, Cassuto), §ב (comparing verses), §ד (the curse)."""
    h = harvest('cain', '1958')
    secs = []

    # §א — scan header: א. שאלות מבנה וסגנון:
    secs.append({'id': prefix, 'title': {'en': '1958 · The Shape of the Story'},
                 'primaryText': primary('Genesis 4:2-5', ['4:2', '4:3', '4:4', '4:5'], {
                     'hevel-roeh': ('ויהי הבל רעה צאן', 'Abel became a keeper of sheep'),
                     'kayin-oved': ('וקין היה עבד אדמה', 'Cain became a tiller of the soil'),
                     'kayin-mevi': ('ויבא קין מפרי האדמה מנחה', 'Cain brought an offering'),
                     'hevel-hevi': ('והבל הביא גם הוא', 'Abel, for his part, brought'),
                     'vayisha': ('וישע יהוה אל הבל ואל מנחתו', 'The Lord paid heed to Abel and his offering'),
                     'lo-shaah': ('ואל קין ואל מנחתו לא שעה', 'but paid no heed to Cain and his offering'),
                 }), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 4:2–5: the two brothers, their work, and their offerings.'),
        question(f'{prefix}-q-a1', h, 2, '1. Verses 2–5 in our chapter are built according to the order “he '
                 'opens with what he closed” (chiastic order). Explain how, and bring further examples of this '
                 'order from Parashat Bereshit.',
                 highlight=['hevel-roeh', 'kayin-oved', 'kayin-mevi', 'hevel-hevi', 'vayisha', 'lo-shaah']),
        # Her underline on «בהקבלה» (scan check) is reproduced.
        commentary(f'{prefix}-cassuto-1', h, 3, 'Cassuto', 'קאסוטו, תורת התעודות', 'Cassuto, Torat HaTe’udot',
                   'When some verb comes twice, one after the other, <u>in parallel</u>, Scripture is wont to '
                   'vary its tense and its position: once it comes in the future converted to past, and once in '
                   'the past; once at the start of the sentence, and once after some other word.',
                   'ours', he=underline(cut(item(h, 3)[0], 'כשבא', 'מלה אחרת'), 'בהקבלה'),
                   highlight=['hevel-roeh', 'kayin-oved']),
        question(f'{prefix}-q-a1a', h, 4, 'a. Explain the special meaning of this form, in verse 2: “Abel '
                 'became… and Cain became…”', highlight=['hevel-roeh', 'kayin-oved']),
        question(f'{prefix}-q-a1b', h, 5, 'b. Bring further examples of this form from our chapter.'),
    ]})

    # §א cont. — her item 3: Cassuto's layout of 4:10–11 ([7]) can't be shown (the harvest flattens its
    # line breaks); the panel's highlights carry the parallel instead. [6], her lead-in, is not a card.
    secs.append({'id': f'{prefix}-a2', 'titleCard': False, 'title': {'en': '“From the Ground”'},
                 'primaryText': primary('Genesis 4:10-11', ['4:10', '4:11'], {
                     'demei-10': ('קול דמי אחיך', 'Hark, your brother’s blood'),
                     'adamah-10': ('צעקים אלי מן האדמה', 'cries out to Me from the ground'),
                     'adamah-11': ('ארור אתה מן האדמה', 'more cursed than the ground'),
                     'demei-11': ('לקחת את דמי אחיך', 'to receive your brother’s blood'),
                 }), 'steps': [
        narration(f'{prefix}-a2-intro', 'Genesis 4:10–11: what God says to Cain after the killing.'),
        commentary(f'{prefix}-cassuto-2', h, 8, 'Cassuto', 'קאסוטו, מאדם עד נח', 'Cassuto, From Adam to Noah',
                   'I have arranged the parts of verse 11 in a form that brings out the parallel between it and '
                   'the preceding verse. The two members of verse 10 end with the words “your brother’s blood” '
                   'and “from the ground.” And here in verse 11 they come in reverse order, of which we have '
                   'already found an example: two members ending with the words “from the ground” and “your '
                   'brother’s blood.”',
                   'ours', start='סידרתי', highlight=['demei-10', 'adamah-10', 'adamah-11', 'demei-11']),
        question(f'{prefix}-q-a3', h, 9, 'Explain: what is the meaning of this parallel?',
                 highlight=['demei-10', 'adamah-10', 'adamah-11', 'demei-11']),
    ]})

    # §ב — scan header: ב. השוה:  Her table ([12]) is the comparison panel. [19]–[20], her list of
    # verses with איפה / איה, are not quoted: [20] is an open triage item (settled in cain.md).
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'Two Questions, Twice'},
                 'primaryText': comparison_4_3(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 4:9–10, beside Genesis 3:9 and 3:13.'),
        question(f'{prefix}-q-b1', h, 13, '1. Are these questions rhetorical questions or not? Prove your words '
                 'from the text.', highlight=['ei-hevel', 'meh-asita', 'ayekah', 'ma-zot']),
        question(f'{prefix}-q-b2', h, 14, '2. Bring further examples of questions of this kind from the book of '
                 'Genesis.'),
        question(f'{prefix}-q-b3', h, 15, 'Compare Rashi’s words in our place with the place in chapter 3:'),
        commentary(f'{prefix}-rashi-4-9', h, 16, 'Rashi', 'רש"י', 'Rashi',
                   '“Where is Abel your brother?”: He entered into gentle words with him; perhaps he would '
                   'repent and say: I killed him, and I have sinned against You.',
                   'ours', ref='Rashi on Genesis 4:9:1', stop='וחטאתי לך', highlight=['ei-hevel']),
        commentary(f'{prefix}-rashi-3-9', h, 16, 'Rashi', 'רש"י', 'Rashi',
                   '“Where are you?”: He knew where he was, but [asked] to enter into words with him, so that '
                   'he would not be too alarmed to answer if He punished him suddenly. And so with Cain He '
                   'said, “Where is Abel your brother?”; and so with Balaam (Numbers 22), “Who are these men,” '
                   'to enter into words with them; and so with Hezekiah, concerning the envoys of '
                   'Merodach-baladan.',
                   'ours', ref='Rashi on Genesis 3:9:1', start='ד"ה איכה', highlight=['ayekah']),
        question(f'{prefix}-q-b3b', h, 17, 'Explain the difference in his words here and there!',
                 highlight=['ei-hevel', 'ayekah']),
        question(f'{prefix}-q-b4', h, 18, 'Explain why the question was asked in both places with the word '
                 '“ayeh” and not with the word “eifo”?', highlight=['ei-hevel', 'ayekah']),
    ]})

    # §ד — scan: ד. י"א ועתה ארור אתה מן האדמה … (the verse). Ramban [28] is split at her own seams:
    # Q4 names the second part («ויתכן שאררו»), Q5 the third («וטעם "אשר פצתה"»).
    secs.append({'id': f'{prefix}-d', 'titleCard': False, 'title': {'en': 'The Curse'},
                 'primaryText': primary('Genesis 4:11-12', ['4:11', '4:12'], {
                     'arur': ('ועתה ארור אתה מן האדמה', 'you shall be more cursed than the ground'),
                     'patsta': ('אשר פצתה את פיה לקחת את דמי אחיך', 'which opened its mouth to receive your brother’s blood'),
                     'taavod': ('כי תעבד את האדמה', 'If you till the soil'),
                     'lo-tosef': ('לא תסף תת כחה לך', 'it shall no longer yield its strength to you'),
                     'na-vanad': ('נע ונד תהיה בארץ', 'You shall become a ceaseless wanderer on earth'),
                 }), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 4:11–12: Cain’s sentence.'),
        commentary(f'{prefix}-d-rashi', h, 27, 'Rashi', 'רש"י', 'Rashi',
                   '“Min ha-adamah”: more than it [the ground] has already been cursed for its sin; and in '
                   'this, too, it has sinned again. “Which opened its mouth to receive your brother’s blood”: '
                   'and I am adding a curse to it with regard to you: “it shall no longer yield its strength '
                   'to you.”',
                   'ours', ref='Rashi on Genesis 4:11:1-2', highlight=['arur', 'patsta']),
        commentary(f'{prefix}-ramban-1', h, 28, 'Ramban', 'רמב"ן', 'Ramban',
                   '“Cursed are you min ha-adamah”: And this is not right; for here He did not curse the '
                   'ground on his account, as with his father, but said that he would be cursed from it. And '
                   'the meaning of the curse: that it would no longer give its strength to him, and that he '
                   'would be a wanderer and a fugitive on it. And He said, “when you till the soil”: however '
                   'much you toil over it to work it properly, with plowing and hoeing and all the work of the '
                   'field, and sow it as is fit, “it shall no longer yield its strength to you”; rather, you '
                   'will sow much and bring in little, and that is the cursing. <u>And He said this against his '
                   'craft, for he was a tiller of the soil; and so He cursed his work.</u> And this is the '
                   'sense of “it shall no longer yield its strength to you”: that it will not give its strength '
                   'to you as it did until now, when he worked it…',
                   'ours', ref='Ramban on Genesis 4:11:1',
                   he=underline(cut(item(h, 28)[0], 'ארור אתה מן האדמה: ואיננו', 'בהיותו עובד אותה...'),
                                'ואמר כן כנגד אומנותו, כי הוא היה עובד אדמה, והנה ארר מעשיו'),
                   highlight=['arur', 'taavod', 'lo-tosef']),
        question(f'{prefix}-q-d1', h, 29, '1) What is the difference between Rashi and Ramban in explaining the '
                 'curse as a whole, and in explaining the word “min” in particular?', highlight=['arur']),
        question(f'{prefix}-q-d2', h, 30, '2. Can you explain the weakness of Rashi’s interpretation from a '
                 'linguistic standpoint?', highlight=['arur']),
        question(f'{prefix}-q-d3', h, 31, '3) Why did Ramban add the words marked with a line (“And He said this '
                 'against…”)'),
        commentary(f'{prefix}-ramban-2', h, 28, 'Ramban', 'רמב"ן', 'Ramban',
                   'And it may be that He cursed him from the ground: that it would not of itself give its '
                   'strength to him — fig and vine would not yield their wealth in his holding, and the tree of '
                   'the field would not give him its fruit — and He went on to say also that when you work it, '
                   'to plow and to sow, “it shall no longer yield its strength to you” as at first. So these '
                   'are two curses on his craft; and the third, that he would be a wanderer and a fugitive on '
                   'it. And the sense: that his heart would not rest nor be quiet to stay in one place on it, '
                   'but he would be an exile forever, for the punishment of murderers is exile.',
                   'ours', ref='Ramban on Genesis 4:11:1', start='וייתכן שאיררו', stop='עונש הרוצחים גלות.',
                   highlight=['lo-tosef', 'na-vanad']),
        question(f'{prefix}-q-d4', h, 32, '4) What is the difference between Ramban’s two interpretations (the '
                 'second begins with “And it may be that He cursed him from the ground”).'),
        commentary(f'{prefix}-ramban-3', h, 28, 'Ramban', 'רמב"ן', 'Ramban',
                   'The sense of “which opened its mouth” is to say: You killed your brother and covered his '
                   'blood in the ground; and I will decree on it that it reveal its blood, and no longer cover '
                   'its slain; for it will be punished for it, and in all that it covers in it, such '
                   'as sowing and planting. And this is the punishment for bloodshed in the land, as it is '
                   'written (Numbers 35), “for blood pollutes the land”; and the pollution of the land is a '
                   'blight on its fruits, as in (Haggai 2:16) “when one came to a heap of twenty, there were '
                   'ten; when one came to the winepress to draw fifty from the vat, there were twenty.”',
                   'ours', ref='Ramban on Genesis 4:11:1', start='בטעם "אשר פצתה', highlight=['patsta']),
        question(f'{prefix}-q-d5', h, 33, '5) Why does Ramban add the third passage, And the sense of “which '
                 'opened its mouth”; what did he add by this to what was already said?', highlight=['patsta']),
        question(f'{prefix}-q-d6', h, 34, '6) How would Ramban interpret the curse of “na va-nad” [a wanderer and '
                 'a fugitive].', highlight=['na-vanad']),
    ]})
    return secs
