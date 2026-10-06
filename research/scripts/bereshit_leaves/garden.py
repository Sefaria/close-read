from bereshit_lib import *  # noqa: F401,F403
# Theme 2 — Adam, the garden and the woman (Gen 2:4–25): leaves 1952, 1953, 1965.
# Paper trail (every card → harvest item, slices, omissions): research/parshiyot/bereshit-leaves/garden.md.


def leaf_1952(prefix='gd-1952'):
    """Gilayon תשי"ב (161471): §א, §ב, §ד, §ו, §ז, §ח."""
    h = harvest('garden', '1952')
    P1 = lambda: primary('Genesis 2:5-8', ['2:5', '2:6', '2:7', '2:8'], {
        'terem-yihyeh': ('שיח השדה טרם יהיה בארץ', 'no shrub of the field was yet on earth'),
        'terem-yitzmach': ('עשב השדה טרם יצמח', 'no grasses of the field had yet sprouted'),
        'lo-himtir': ('כי לא המטיר', 'had not sent rain upon the earth'),
        'adam-ayin': ('ואדם אין לעבד את האדמה', 'there were no human beings to till the soil'),
        'vayitzer': ('וייצר יהוה אלהים את האדם', 'The Lord God formed a Human'),
        'gan-mikedem': ('גן בעדן מקדם', 'a garden in Eden, in the east'),
    })
    P2 = lambda: primary('Genesis 2:15-18', ['2:15', '2:16', '2:17', '2:18'], {
        'leovdah': ('לעבדה ולשמרה', 'to till it and tend it'),
        'mikol-etz': ('מכל עץ הגן אכל תאכל', 'Of every tree of the garden you are free to eat'),
        'lo-tov': ('לא טוב היות האדם לבדו', 'It is not good for the Human to be alone'),
        'ezer': ('אעשה לו עזר כנגדו', 'I will make a fitting counterpart for him'),
    })
    secs = []

    secs.append({'id': prefix, 'title': {'en': '1952 · Chapter 1 and Chapter 2'}, 'primaryText': P1(), 'steps': [
        # §א — scan header: א. ה': וכל שיח השדה טרם יהיה
        narration(f'{prefix}-intro', 'Genesis 2:5 to 2:8: before the garden, and the garden.'),
        narration(f'{prefix}-a-verse', '“No shrub of the field was yet on earth.”', highlight=['terem-yihyeh']),
        commentary(f'{prefix}-rashi', h, 2, 'Rashi', 'רש"י', 'Rashi',
                   'Every “terem” in Scripture means “not yet”; it does not mean “before,” and it cannot be '
                   'made into a verb, to say “hitrim” as one says “hikdim.” This verse proves it, and another '
                   'besides (Exodus 9): “ki terem tire’un,” you do not yet fear. So explain this one too: it '
                   'was not yet on the earth when the creation of the world was completed on the sixth day, '
                   'before man was created; and every herb of the field had not yet sprouted. And on the '
                   'third day, where it is written “[the earth] brought forth,” they did not come out, but '
                   'stood at the opening of the ground until the sixth day.',
                   'ours', ref='Rashi on Genesis 2:5', start='כל טרם', stop="עמדו עד יום ו'",
                   highlight=['terem-yihyeh', 'terem-yitzmach']),
        commentary(f'{prefix}-ramban', h, 3, 'Ramban', 'רמב"ן', 'Ramban',
                   'According to our Rabbis (in Bereshit Rabbah) [see Chullin 60b], on the third day they '
                   'stood at the opening of the ground, and on the sixth they sprouted, after He brought rain '
                   'upon them. But in my view, according to the plain sense: on the third day the earth '
                   'brought forth the grass and the fruit trees in their full stature and form, as He had '
                   'commanded them; and now Scripture tells that there is no one to plant and sow them, and '
                   'the earth will not make them sprout until a flow rose from it and watered it, and the man '
                   'was formed who works it, to sow and to plant and to keep. And this is the sense of '
                   '“no shrub of the field had yet sprouted”: it did not say “shrub of the ground,” because a '
                   'worked place is called “field” (sadeh): “which you sow in the field” (Exodus 23:16); “we '
                   'will not pass through field or vineyard” (Numbers 20:17). And this is the working of the '
                   'world that came to be from after the six days of creation onward, all the days of the '
                   'world: by means of the flow the heavens give rain, and by means of them the earth makes '
                   'its seeds sprout.',
                   'ours', ref='Ramban on Genesis 2:5', start='על דעת רבותינו',
                   highlight=['terem-yihyeh', 'adam-ayin']),
        question(f'{prefix}-q-a1', h, 4, '1. What is difficult for both of them?'),
        question(f'{prefix}-q-a2', h, 5, '2. What separates them in resolving the difficulty?'),
        question(f'{prefix}-q-a3', h, 6, '3. What support does each of the two commentators find in the '
                 'language of the verse?', highlight=['terem-yihyeh', 'lo-himtir', 'adam-ayin']),
        # [7] is NOT-IN-SCAN: quoted under brief rule 6, because her Q4 names Sforno.
        commentary(f'{prefix}-sforno', h, 7, 'Sforno', 'ספורנו', 'Sforno',
                   'Indeed, the meaning is that when they were created they existed in potential and not in '
                   'actuality, so that every shrub of the field was not yet on the earth',
                   'ours', ref='Sforno on Genesis 2:5', start='אמנם', stop='עדיין לא היה בארץ',
                   highlight=['terem-yihyeh']),
        question(f'{prefix}-q-a4', h, 'after 6', '4. In whose footsteps, of the two, does Sforno follow?'),

        # §ב — scan header: ב. ה'... טרם יהיה...טרם יצמח
        narration(f'{prefix}-b-intro', '“Not yet… not yet.”', highlight=['terem-yihyeh', 'terem-yitzmach']),
        commentary(f'{prefix}-jacob', h, 10, 'Benno Jacob', 'בנו יעקב', 'Benno Jacob',
                   'It does not say that vegetation did not yet exist; on the contrary, it says that it did '
                   'exist, but was still in an undeveloped state. And no wonder: the two factors that bear on '
                   'the development of vegetation had not yet acted, for the Lord had not sent rain and man '
                   'had not worked the ground. So the meaning of “terem yihyeh” is not: it was not in being, '
                   'it did not exist; but rather: it had not reached what it was destined to be. So too '
                   'Isaiah 15:6; Jeremiah 14:5.',
                   'ours', start='לא נאמר', stop='י"ד ה\'',
                   highlight=['terem-yihyeh', 'lo-himtir', 'adam-ayin']),
        question(f'{prefix}-q-b1', h, 11, '1. With which of our commentators does Benno Jacob agree?'),
        question(f'{prefix}-q-b2', h, 12, '2. What is his proof from the two verses in Isaiah and Jeremiah?'),
        question(f'{prefix}-q-b3', h, 13, '3. Against which approach in the scholarly literature is Benno '
                 'Jacob turning here?'),

        # §ד — scan header: ד. ח' רש"י ד"ה מקדם החל מן "ואם תאמר" עד "וללמד על העופות".
        narration(f'{prefix}-d-intro', '“A garden in Eden, in the east.”', highlight=['gan-mikedem']),
        commentary(f'{prefix}-rashi-mikedem', h, 20, 'Rashi', 'רש"י', 'Rashi',
                   'And if you say: but it has already been said, “And [God] created … the man” — I have seen '
                   'in the Baraita of R. Eliezer son of R. Yose the Galilean, on the thirty-two rules by which '
                   'the Torah is expounded, and this is one of them: a general statement followed by an '
                   'account of the act is the detail of the first. “And [God] created … the man” is a general '
                   'statement: it left unstated from where he was created, and left unstated what was done '
                   'with him. It went back and explained: “And the Lord God formed…,” and made the garden of '
                   'Eden grow for him, and placed him in the garden of Eden, and cast a deep sleep upon him. '
                   'One who hears it supposes it is another act, but it is only the detail of the first. And '
                   'so with the beasts: it went back and wrote, “And the Lord … formed out of the earth all '
                   'the wild beasts,” in order to explain “and brought [them] to the man” to give '
                   '[them] names, and to teach about the birds',
                   'ours', ref='Rashi on Genesis 2:8', start='ואם תאמר', stop='וללמד על העופות',
                   highlight=['vayitzer', 'gan-mikedem']),
        question(f'{prefix}-q-d1', h, 21, '1. Rashi wanted to resolve two difficulties with this; explain '
                 'what they are.'),
        question(f'{prefix}-q-d2', h, 22, '2. What is his answer to each of the two difficulties?'),
        question(f'{prefix}-q-d3', h, 23, '3. Give more examples in Parashat Bereshit (or in other parashiyot '
                 'of the book of Genesis) of this rule by which the Torah is expounded, which Rashi '
                 'mentions here.'),
    ]})

    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'To Till It and Tend It'},
                 'primaryText': P2(), 'steps': [
        # §ו — scan header: ו. ט"ו לעבדה ולשמרה
        narration(f'{prefix}-v-intro', 'Genesis 2:15 to 2:18: the Human in the garden.'),
        commentary(f'{prefix}-chizkuni', h, 34, 'Chizkuni', 'חזקוני', 'Chizkuni',
                   '“To till it” (le-ovdah): after “Six days you shall labor” (ta’avod); “and to tend it” '
                   '(u-le-shomrah): after “Observe (shamor) the Sabbath day.”',
                   'ours', ref='Chizkuni, Genesis 2:15', highlight=['leovdah']),
        question(f'{prefix}-q-v1', h, 35, '1. How did he interpret the letter heh of le-ovdah and of '
                 'le-shomrah?', highlight=['leovdah']),
        question(f'{prefix}-q-v2', h, 36, '2. In what does he depart from the usual interpretation, and what '
                 'moved him to it?'),

        # §ז — scan header: ז. ט"ו "לעבדה ולשמרה"
        question(f'{prefix}-q-z', h, 39, 'Explain that our verse does not contradict what is said in chapter 3, '
                 'verse 19.', highlight=['leovdah']),
        commentary(f'{prefix}-adrn', h, 40, 'Avot de-Rabbi Natan', 'אבות דר\' נתן', 'Avot de-Rabbi Natan',
                   'Shemaiah says: “Love work.” How so? A person should love work and not hate work; for just '
                   'as the Torah was given with a covenant, so work was given with a covenant, as it is said '
                   '(Exodus 31): “Six days shall work be done… an everlasting covenant.” R. Shimon ben Elazar '
                   'says: Even the first man <u>tasted nothing until he had done work</u>, as it is said, '
                   '“and placed him in the garden of Eden to till it and tend it,” and after that, “Of every '
                   'tree of the garden you are free to eat.”',
                   'ours', ref='Avot de-Rabbi Natan 11',
                   he=underline(cut(item(h, 40)[0], 'שמעיה אומר', 'אכול תאכל"'), 'לא טעם כלום עד שעשה מלאכה'),
                   highlight=['leovdah', 'mikol-etz']),

        # §ח — scan: banner בריאת האשה, then ח. עקדת יצחק:
        narration(f'{prefix}-h-intro', '“It is not good for the Human to be alone.”', highlight=['lo-tov']),
        commentary(f'{prefix}-akeidah', h, 42, 'Akeidat Yitzhak', 'עקדת יצחק', 'Akeidat Yitzhak',
                   '…And therefore His wisdom, may He be blessed, saw fit that the pairing of man and his wife '
                   'should not rest on the sexual bond alone, as with the other living creatures, but that they '
                   'should have a special personal bond, one that would strengthen their love and companionship, '
                   'to help one another in all their affairs with a help complete and whole, as befits them; '
                   'so that neither the male nor the female should be on its own, like the other animals '
                   'grazing beside them, which have no need of companionship with one another. Rather, it is '
                   'fitting that he have a companion suited to him and sharing with him according to his need; '
                   'and for this, “I will make him” the helper fitting and suited to him, his equal.',
                   'ours', start='ולזה ראתה', highlight=['ezer']),
        question(f'{prefix}-q-h', h, 43, 'Explain which verses in our chapter state this idea, explicitly or '
                 'by hint.'),
    ]})
    return secs


def leaf_1953(prefix='gd-1953'):
    """Gilayon תשי"ג (161223): §ב, §ג, §ד, §ו."""
    h = harvest('garden', '1953')
    P1 = lambda: primary('Genesis 2:18-20', ['2:18', '2:19', '2:20'], {
        'lo-tov': ('לא טוב היות האדם לבדו', 'It is not good for the Human to be alone'),
        'ezer': ('אעשה לו עזר כנגדו', 'I will make a fitting counterpart for him'),
        'shemot': ('ויקרא האדם שמות', 'the Human gave names'),
        'velaadam': ('ולאדם לא מצא עזר כנגדו', 'but no fitting counterpart for a human being was found'),
    })
    P2 = lambda: primary('Genesis 2:23-24', ['2:23', '2:24'], {
        'etzem': ('עצם מעצמי ובשר מבשרי', 'Is bone of my bones And flesh of my flesh'),
        'yaazov': ('על כן יעזב איש את אביו ואת אמו', 'Hence a man leaves his father and mother'),
        'vedavak': ('ודבק באשתו', 'clings to his wife'),
        'basar-echad': ('והיו לבשר אחד', 'they become one flesh'),
    })
    ga = item(h, 16)[0]
    secs = []

    secs.append({'id': prefix, 'title': {'en': '1953 · A Helper Against Him'}, 'primaryText': P1(), 'steps': [
        # §ב — scan header: ב. י"ח לא טוב היות האדם לבדו
        narration(f'{prefix}-intro', 'Genesis 2:18 to 2:20: “It is not good,” the naming of the animals, '
                  'and what was not found.'),
        commentary(f'{prefix}-rashi', h, 6, 'Rashi', 'רש"י', 'Rashi',
                   'So that they should not say there are two powers: the Holy One, blessed be He, is alone '
                   'among the upper beings and has no mate, and this one is alone among the lower beings and '
                   'has no mate.', 'ours', ref='Rashi on Genesis 2:18', highlight=['lo-tov']),
        commentary(f'{prefix}-sforno', h, 7, 'Sforno', 'ספורנו', 'Sforno',
                   'The good of the purpose intended in his likeness and his image will not be attained if he '
                   'himself must busy himself with the needs of his life.',
                   'ours', ref='Sforno on Genesis 2:18', highlight=['lo-tov']),
        question(f'{prefix}-q-b1', h, 10, '1. Rashi’s commentators ask: what made Rashi bring these words of '
                 'the Sages here, and explain that it is “not good” in this respect, and not explain it in its '
                 'plain sense, as Sforno explained? Answer their question! (Pay attention to the wording of '
                 'the verse, and be precise!)', highlight=['lo-tov']),
        commentary(f'{prefix}-chizkuni', h, 8, 'Chizkuni', 'חזקוני', 'Chizkuni',
                   'From the start it was in [God’s] thought to make him a mate, but He found no opening to do '
                   'it until after the naming, so that he would long for her and cherish her the more.',
                   'ours', ref='Chizkuni, Genesis 2:18', highlight=['lo-tov', 'shemot']),
        question(f'{prefix}-q-b2', h, 11, '2. What is the difficulty that Chizkuni wanted to resolve in his '
                 'words?'),
        commentary(f'{prefix}-shadal', h, 9, 'Shadal', 'שד"ל', 'Shadal',
                   'The intent is not to say that God reconsidered in His thought; rather, the intent is to '
                   'make us aware of the preciousness of the pairing, and to make known that it is not good '
                   'for the man to be alone. Therefore the Holy One, blessed be He, wanted the man to dwell '
                   'for a time without a wife, and afterward prepared her for him, so that she would be dear '
                   'to him, after he had felt that without her he was lacking.',
                   'ours', ref='Shadal on Genesis 2:18', highlight=['lo-tov']),
        question(f'{prefix}-q-b3', h, 12, '3. What is the difficulty that Shadal wanted to resolve in his words?'),

        # §ג — scan header: ג. י"ח אעשה לו עזר כנגדו
        narration(f'{prefix}-g-intro', '“A fitting counterpart for him”: in Hebrew, ezer kenegdo, a helper '
                  'against him.', highlight=['ezer']),
        commentary(f'{prefix}-rashi-ezer', h, 15, 'Rashi', 'רש"י', 'Rashi',
                   'If he is worthy, “a helper”; if he is not worthy, “against him,” to fight.',
                   'ours', ref='Rashi on Genesis 2:18', highlight=['ezer']),
        question(f'{prefix}-q-g2', h, 19, '2. In what does the midrash cited in Rashi’s words depart from the '
                 'plain sense of Scripture?'),
        commentary(f'{prefix}-gur-aryeh-a', h, 16, 'Gur Aryeh', 'גור אריה', 'Gur Aryeh',
                   'And this is the meaning of Rashi’s words: I will make him a helper that is a helper '
                   'against him. For this helper is not a helper like a father to a son or a son to a father, '
                   'who never oppose each other; but this helper will be “a helper against him,” for the '
                   'woman, who is <u>of worth and of equal weight with the man</u> and helps the man, or the '
                   'man brings and the woman prepares for him: this is called “a helper against him.” And so, '
                   'if he is not worthy, she is entirely against him; but a father to a son is never against '
                   'him. This is how it should be explained according to its plain sense; and were it not so, '
                   'Rashi would not have brought <u>this midrash, which is not close to the plain sense</u>.',
                   'ours', ref='Gur Aryeh on Genesis 2:18',
                   he=underline(underline(cut(ga, 'וכך פירוש', 'קרוב לפשוטו.'), 'חשובה ושקולה כמו האיש'),
                                'מדרש זה, שאינו קרוב לפשוטו'),
                   highlight=['ezer']),
        commentary(f'{prefix}-gur-aryeh-b', h, 16, 'Gur Aryeh', 'גור אריה', 'Gur Aryeh',
                   'And there is a further hidden matter in this: the male and the female are two opposites, '
                   'this one male and that one female. If he is worthy, they join entirely into a single '
                   'power, <u>for any two opposites join into a single power</u> when they are worthy; that '
                   'is, <u>God, may He be blessed, who makes peace between opposites, binds and joins '
                   'them</u>. But when they are not worthy, then, because they are opposites, it causes her '
                   'to be “against him.”',
                   'ours', ref='Gur Aryeh on Genesis 2:18',
                   he=underline(underline(cut(ga, 'ויש בזה דבר נעלם'), 'כי כל שני הפכים מתחברים בכח אחד'),
                                "שהשם ית' שעושה שלום בין ההפכים מקשר ומחבר אותם"),
                   highlight=['ezer'], effect='glow'),
        question(f'{prefix}-q-g3', h, 20, '3. Explain the idea in the words of the midrash according to the '
                 'Gur Aryeh’s interpretation! (Pay attention especially to his words from “And there is a '
                 'further hidden matter.”) What do the underlined words mean?'),
        commentary(f'{prefix}-shadal-ezer', h, 17, 'Shadal', 'שד"ל', 'Shadal',
                   'It seems to me that it is from “keneged” in the language of the Sages, as in “The Torah '
                   'spoke keneged four sons”: its sense is “with regard to four sons.” A helper related to him '
                   'and fitted to his needs.',
                   'ours', ref='Shadal on Genesis 2:18', highlight=['ezer']),
        question(f'{prefix}-q-g1', h, 18, '1. What is difficult for the commentators in our verse?'),

        # §ד — scan header: ד. כ' ולאדם לא מצא עזר כנגדו
        narration(f'{prefix}-d-intro', '“But no fitting counterpart for a human being was found.”',
                  highlight=['velaadam']),
        commentary(f'{prefix}-ibn-ezra', h, 23, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the sense of “u-le-adam lo matza” is: and for himself he did not find; for such is the '
                   'way of the holy tongue, as in “And the Lord sent Jerubbaal and Bedan and Jephthah and '
                   'Samuel” (I Samuel 12:11). And it is far-fetched in my eyes that it should refer back to God.',
                   'ours', ref='Ibn Ezra on Genesis 2:18', start='וטעם ולאדם לא מצא', stop='אל השם',
                   highlight=['velaadam']),
        question(f'{prefix}-q-d3', h, 27, '3. Explain Ibn Ezra’s words, “that it should refer back to God.”'),
        commentary(f'{prefix}-ramban', h, 24, 'Ramban', 'רמב"ן', 'Ramban',
                   'And what is right in my eyes is that it was not His will, blessed be He, to take his rib '
                   'from him until the man knew that among the creatures there was no helper for him, and '
                   'longed to have a helper like them. And because of this it was necessary to take one of his '
                   'ribs from him. And this is the sense of “u-le-adam lo matza ezer kenegdo”: that is, for '
                   'the name of Adam he did not find a helper that would be fit against him and be called by '
                   'his name, one by whom he would beget. And there is no need here for the words of the '
                   'commentators who say that a noun comes here in place of the pronoun, and “he did not find '
                   'a helper against him,” in the manner of “the wives of Lamech” (Genesis 4:23) and “and '
                   'Jephthah and Samuel” (I Samuel 12:11).',
                   'ours', ref='Ramban on Genesis 2:20', start='והנכון בעיני', stop='ואת שמואל',
                   highlight=['velaadam']),
        commentary(f'{prefix}-nechama-verses', h, 'after 24', 'Nechama Leibowitz', 'נחמה ליבוביץ',
                   'Nechama Leibowitz',
                   'And the two verses Ramban brings are: Genesis 4:23; I Samuel 12:11.', 'ours'),
        commentary(f'{prefix}-nechama-note', h, 'after 24.2', 'Nechama Leibowitz', 'נחמה ליבוביץ',
                   'Nechama Leibowitz',
                   '(At the end of these words of Ramban a printing error has crept into our editions of the '
                   'Humash, and it should be corrected to read: “ve-lo matza kenegdo, be-derekh ‘neshei '
                   'Lemekh’”… And so the author of Kur ha-Zahav corrected it.)',
                   'ours', highlight=['velaadam']),
        question(f'{prefix}-q-d4', h, 28, '4. Explain Ramban’s words, “that a noun comes here in place of a '
                 'pronoun.”'),
        question(f'{prefix}-q-d5', h, 29, '5. In what are the two verses Ramban brings similar to our verse, '
                 'according to the commentators whom Ramban opposes?'),
        question(f'{prefix}-q-d1', h, 25, '1. What is difficult for the commentators in our verse?'),
        question(f'{prefix}-q-d2', h, 26, '2. Who is the subject of “u-le-adam lo matza,” according to the two '
                 'commentators above?', highlight=['velaadam']),
        question(f'{prefix}-q-d6', h, 30, 'With which of the two commentators do the Masoretes agree, in '
                 'pointing “u-le-adam” with a shva and not with a kamatz?', highlight=['velaadam']),
        commentary(f'{prefix}-jacob', h, 32, 'Benno Jacob', 'בנו יעקב', 'Benno Jacob',
                   'But for “man” he found no help, as it were his counterpart.',
                   'ours', start='Aber', stop='Gegenstueck', highlight=['velaadam'], he_dir='ltr'),
        commentary(f'{prefix}-buber', h, 33, 'Buber-Rosenzweig', 'בובר-רוזנצווייג', 'Buber-Rosenzweig',
                   'But for a human being no help was found, at his side.',
                   'ours', start='Aber', stop='zuseiten', highlight=['velaadam'], he_dir='ltr'),
        question(f'{prefix}-q-d-a', h, 34, '(a) In whose footsteps, of our two commentators, does B. Jacob '
                 'follow?'),
        question(f'{prefix}-q-d-b', h, 35, 'b. In what does Buber differ from both of them in his interpretation?'),
    ]})

    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'One Flesh'},
                 'primaryText': P2(), 'steps': [
        # §ו — scan header: ו. כ"ד על כן יעזב איש את אביו ואת אמו ודבק באשתו.
        narration(f'{prefix}-v-intro', 'Genesis 2:23 and 2:24: the man’s words, and what follows from them.'),
        commentary(f'{prefix}-pdre', h, 43, 'Pirkei de-Rabbi Eliezer', 'פרקי דר\' אליעזר',
                   'Pirkei de-Rabbi Eliezer',
                   'From here you learn: before a man has taken a wife, his love goes after his parents; once '
                   'he has taken a wife, his love goes after his wife, as it is said, “Hence a man leaves… and '
                   'clings to his wife.” And would a man leave his father and his mother, [and so depart] from '
                   'the commandment of honoring [them]? Rather, the love of his soul cleaves to his wife, as it '
                   'is said, “and clings to his wife.”',
                   'ours', ref='Pirkei de-Rabbi Eliezer 32', start='מכאן אתה למד',
                   highlight=['yaazov', 'vedavak']),
        commentary(f'{prefix}-rashi-24', h, 44, 'Rashi', 'רש"י', 'Rashi',
                   'The holy spirit says this, to forbid the forbidden unions to the children of Noah '
                   '(Sanhedrin 57).',
                   'ours', ref='Rashi on Genesis 2:24', start='רוח הקודש', stop='(סנהדרין נ"ז).',
                   highlight=['yaazov']),
        question(f'{prefix}-q-v1', h, 46, '1. Explain the expression “the holy spirit” in Rashi’s words here. '
                 'And why does he need to stress that this verse is the words of “the holy spirit”?',
                 highlight=['yaazov']),
        commentary(f'{prefix}-ramban-24', h, 45, 'Ramban', 'רמב"ן', 'Ramban',
                   'This [Rashi’s explanation of “one flesh,” that the child is formed by both of them] has no '
                   'reason in it, for domestic and wild animals too become one flesh in their offspring. And '
                   'what is right in my eyes is that domestic and wild animals have no attachment to their '
                   'females: the male comes upon whatever female he finds, and they go their way. And for this '
                   'reason Scripture said: because the man’s female was bone of his bones and flesh of his '
                   'flesh, he clung to her, and she was in his bosom like his own flesh, and he desired her to '
                   'be with him always. And as this was so in Adam, it was set as nature in his descendants, '
                   'that their males cling to their wives, leaving their father and their mother, and regard '
                   'their wives as though they were one flesh with them. And so, “for he is our brother, our '
                   'flesh” (below, 37:27); “to any that is near of his flesh” (Leviticus 18:6): relatives in a '
                   'family are called “she’er basar.” So he will leave the kin of his father and mother and '
                   'their closeness, and will see that his wife is closer to him than they are.',
                   'ours', ref='Ramban on Genesis 2:24', start='ואין בזה טעם',
                   highlight=['etzem', 'vedavak', 'basar-echad']),
        question(f'{prefix}-q-v2', h, 47, '2. What is between Rashi and Ramban in interpreting our verse, and '
                 'which of the two agrees with the words of Pirkei de-Rabbi Eliezer?'),
    ]})
    return secs


def leaf_1965(prefix='gd-1965'):
    """Gilayon תשכ"ה (160577): §ג, §ד, §ו."""
    h = harvest('garden', '1965')
    taanit = item(h, 16)[0]
    br14 = item(h, 17)[0]
    secs = []

    secs.append({'id': prefix, 'title': {'en': '1965 · The Human Being'},
                 'primaryText': primary('Genesis 2:7', ['2:7'], {
                     'nishmat': ('ויפח באפיו נשמת חיים', 'blowing into his nostrils the breath of life'),
                     'nefesh-chayah': ('ויהי האדם לנפש חיה', 'the Human became a living being'),
                 }), 'steps': [
        # §ג — scan header: ג. ז' ויהי האדם לנפש חיה
        narration(f'{prefix}-intro', 'Genesis 2:7: the Human is formed, and becomes a living being.'),
        commentary(f'{prefix}-taanit', h, 16, 'Taanit', 'תענית', 'Taanit',
                   'R. Yose says: An individual is not permitted to <u>afflict</u> himself with fasting, lest '
                   'he come to depend on other people [Rashi: for he has no strength to earn and make his '
                   'living from his labor], and people will not have mercy on him. [Maharsha: for he himself '
                   'caused his illness through self-affliction.] Rav Yehuda said in the name of Rav: What is '
                   'the reason of R. Yose? For it is written (Genesis 2), “and the Human became a living '
                   'being”: <u>the soul I gave you, keep it alive</u>!',
                   'ours', ref='Taanit 22b',
                   he=underline(underline(cut(taanit), 'לסגף'), 'נשמה שנתתי בך – החייה'),
                   highlight=['nefesh-chayah']),
        commentary(f'{prefix}-br-14', h, 17, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And the Human became a living being”: R. Yehuda said: He made him a slave sold '
                   '(<u>sold in perpetuity, bound in servitude</u>) to himself: if he does not toil, he does '
                   'not eat (= if he does not labor and toil, he does not eat). This is the view of R. Huna '
                   '(and some read: of R. Chanina), who said (Lamentations 1): “The Lord has given me into '
                   'the hands of… I am not able (lo ukhal) to rise”…',
                   'ours', ref='Bereshit Rabbah 14:10',
                   he=underline(cut(br14), 'מכור לצמיתות, משועבד'), highlight=['nefesh-chayah']),
        question(f'{prefix}-q-g3', h, 21, '3. How does R. Huna expound the verse Lamentations 1:14?'),
        commentary(f'{prefix}-david-hanagid', h, 18, 'R. David HaNagid', 'ר\' דוד הנגיד בן רבנו אברהם בן הרמב"ם',
                   'R. David HaNagid, son of Rabbenu Avraham ben HaRambam',
                   'And I say further: “and the Human became a living being” means that a person is obliged '
                   'to strive for the life of his soul: to keep his soul alive and not kill it, to heal it and '
                   'not make it ill. For the soul has health and illness: the illness of the soul is folly and '
                   'foolishness, and the acquiring of corrupt traits, licentiousness and wickedness; and its '
                   'cure is the acquiring of virtues and good traits, and walking after people of knowledge. '
                   'And the aim of the Creator, may He be blessed, for man is that he walk in His ways, may He '
                   'be blessed, and that all his deeds be whole and healthy, and his soul whole and set right, '
                   'and that it continue in eternal life, as it says, “and the Human became a living being.”',
                   'ours', start='ואני אומר', highlight=['nefesh-chayah']),
        question(f'{prefix}-q-g1', h, 19, '1. What is the difficulty in our verse that all of the above '
                 'addressed?', highlight=['nefesh-chayah']),
        question(f'{prefix}-q-g2', h, 20, '2. What is the difference between them in interpreting our verse?'),
    ]})

    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'Taken into the Garden'},
                 'primaryText': primary('Genesis 2:8, 15', ['2:8', '2:15'], {
                     'vayasem': ('וישם שם את האדם אשר יצר', 'placed there the Human who had been fashioned'),
                     'vayikach': ('ויקח יהוה אלהים את האדם וינחהו בגן עדן',
                                  'The Lord God settled the Human in the garden of Eden'),
                     'leovdah': ('לעבדה ולשמרה', 'to till it and tend it'),
                 }), 'steps': [
        # §ד — scan header: ד. ט"ו ויקח ה' אלוקים את האדם ויניחהו בגן עדן לעבדה ולשמרה.
        narration(f'{prefix}-d-intro', 'Genesis 2:8 and 2:15. In Hebrew, 2:15 opens with va-yikkah, '
                  '“and He took.”'),
        commentary(f'{prefix}-br-16', h, 24, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“And the Lord took the man”: R. Yehuda says: He raised him up, as you say (Isaiah 63:3 '
                   '[14:2]), “And peoples shall take them and bring them…” R. Nehemiah says: He enticed him, as '
                   'you say (Hosea 4:3 [14:3]), “Take words with you and return to the Lord…”',
                   'ours', ref='Bereshit Rabbah 16:5', highlight=['vayikach']),
        commentary(f'{prefix}-rashi', h, 25, 'Rashi', 'רש"י', 'Rashi',
                   'He took him with fine words, and enticed him to enter.',
                   'ours', ref='Rashi on Genesis 2:15', highlight=['vayikach']),
        question(f'{prefix}-q-d2', h, 28, '2. The words of R. Yehuda and R. Nehemiah are cited in Bereshit '
                 'Rabbah on verse 8 of our chapter too; explain why Rashi did not bring them there.',
                 highlight=['vayasem']),
        question(f'{prefix}-q-d3', h, 29, '3. Explain what led Rashi to change from the wording of his source '
                 '(the words of R. Nehemiah).'),
        commentary(f'{prefix}-radak', h, 26, 'Radak', 'רד"ק', 'Radak',
                   'Although it already mentioned above (2:8) “and placed there,” it repeated and said again '
                   '“took,” because it wants to mention the commandment that God commanded him. And it further '
                   'added “to till it and tend it,” which it did not mention at first. And the meaning of '
                   '“and put him”: that He took him from the place where he was created, near the garden of '
                   'Eden, and put him in the garden of Eden. And why did He not form him in the garden of Eden '
                   'in the first place, since in the end He was going to put him there? So that that place '
                   'would be dearer to him, being new to him, and so that he would recognize that God goes on '
                   'doing him good. And the sense of “took” is as in (Joshua 24) “And I took your father from '
                   'beyond the River.”',
                   'ours', ref='Radak on Genesis 2:15', highlight=['vayasem', 'vayikach', 'leovdah']),
        question(f'{prefix}-q-d4', h, 30, '4. Why did Radak bring his proof from Joshua, and not bring it from '
                 'the Torah, Genesis 16:3?'),
        question(f'{prefix}-q-d1', h, 27, '1. What are the difficulties in our verse that confront the author '
                 'of the midrash and the commentators?', highlight=['vayikach']),
    ]})

    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': 'What He Would Call Them'},
                 'primaryText': primary('Genesis 2:19', ['2:19'], {
                     'vayitzer': ('ויצר יהוה אלהים מן האדמה כל חית השדה ואת כל עוף השמים',
                                  'the Lord God formed out of the earth all the wild beasts and all the birds of the sky'),
                     'lirot': ('ויבא אל האדם לראות מה יקרא לו', 'brought them to the Human to see what he would call them'),
                     'shemo': ('וכל אשר יקרא לו האדם נפש חיה הוא שמו',
                               'whatever the Human called each living creature, that would be its name'),
                 }), 'steps': [
        # §ו — scan header: ו. י"ט ויצר ה' אלוקים מן האדמה כל חית השדה ואת כל עוף השמים / ויבא אל האדם לראות מה יקרא לו.
        narration(f'{prefix}-v-intro', 'Genesis 2:19: the beasts and the birds are brought to the Human.'),
        commentary(f'{prefix}-wessely', h, 40, 'Wessely', 'ר\' נפתלי הירץ ויזל, אמרי שפר',
                   'R. Naftali Hirz Wessely, Imrei Shefer',
                   'The Lord wished that man should call names to the wild beasts and the cattle and the birds '
                   'of the sky; therefore He brought them to him, to see what name he would call each one of '
                   'them. And He, blessed be He, foresees and knows all, and knew what he would call them, and '
                   'that he would aim in each name at what befits that species. If so, the word “to see” is as '
                   'in (chapter 11) “to see the city and the tower that the children of man had built”; (Psalms '
                   '14:2) “to see if there is anyone wise, seeking God”; and so, “to see what he would call '
                   'them”: for He watches at every moment. For the calling of names is not only so that they '
                   'be told apart by their names, to know which is which; rather, the name is its inner nature, '
                   'and what it was created to serve…',
                   'ours', start="חפץ ה'", highlight=['lirot']),
        commentary(f'{prefix}-sforno', h, 41, 'Sforno', 'ספורנו', 'Sforno',
                   'So that he would see and consider what name befits each one of them, according to the '
                   'particular rank of its form.',
                   'ours', ref='Sforno on Genesis 2:19', highlight=['lirot']),
        question(f'{prefix}-q-v1', h, 42, '1. What is the difference between the two interpretations, '
                 'syntactically?', highlight=['lirot']),
        question(f'{prefix}-q-v2', h, 43, '2. Shadal brings proof for Sforno’s interpretation from the following '
                 'two verses: II Samuel 24:13; Psalms 104:28. Explain how each of these verses supports '
                 'Sforno’s interpretation.'),
        question(f'{prefix}-q-v3', h, 44, '3. According to several of our commentators, this verse is the '
                 'carrying out of what is said in Genesis 1:28. Explain!', highlight=['shemo']),
    ]})
    return secs
