"""Theme 1 — the days of creation (Gen 1:1–2:3): leaves 1943, 1954, 1963."""
from bereshit_lib import *  # noqa: F401,F403


def leaf_1963(prefix='cr-1963', title_card=True):
    """Gilayon תשכ"ג (160726): §א (with the Leningrad Codex), §ג, §ד, §ה. §ב is out (pack §7)."""
    h = harvest('creation', '1963')
    P = gen_1_31_2_3
    jacob_q_start = 'הסבר, למה אין חלוקה'
    secs = []

    secs.append({'id': prefix, 'title': {'en': '1963 · Where Does Chapter 2 Begin?'},
                 **({} if title_card else {'titleCard': False}),
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 1:31 to 2:3: the end of the sixth day, and the seventh.'),
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
                 'title': {'en': '“Very Good,” and the Seventh Day'},
                 'primaryText': P(), 'steps': [
        # §ג — scan header: ג. א' ל"א וירא אלו-הים את כל אשר עשה והנה טוב מאד.
        narration(f'{prefix}-g-intro', 'The end of the sixth day.'),
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
        narration(f'{prefix}-h-intro', '“And on the seventh day God finished.”', highlight=['vaychal']),
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




def leaf_1943(prefix='cr-1943'):
    """Gilayon תש"ג (162000), Part 1: §א, §ב, §ג (with the Leningrad Codex, folio 2r), §ד.

    Her questions and prose survive only in the scan; the harvest carries them as transcription
    items keyed '<letter>/q<n>' and '<letter>/text1'.
    """
    h = harvest('creation', '1943')
    P = lambda: primary('Genesis 2:2-4', ['2:2', '2:3', '2:4'], {
        'vaychal': ('ויכל אלהים ביום השביעי', 'On the seventh day God finished'),
        'vayishbot': ('וישבת ביום השביעי', 'ceasing on the seventh day'),
        'laasot': ('אשר ברא אלהים לעשות', 'the work of creation that God had done'),
        'toldot': ('אלה תולדות השמים והארץ', 'Such is the story of heaven and earth'),
    })
    secs = []

    secs.append({'id': prefix, 'title': {'en': '1943 · Where Creation Ends'}, 'primaryText': P(), 'steps': [
        # §א — scan header: פסוק ב' ויכל אלקים ביום השביעי.
        narration(f'{prefix}-intro', 'Genesis 2:2 to 2:4: the seventh day, and the verse after it.'),
        commentary(f'{prefix}-mekhilta', h, 'א/text1', 'Mekhilta', 'מכילתא', 'Mekhilta',
                   '“The dwelling of the children of Israel who dwelt in Egypt was thirty years and four '
                   'hundred years” (Exodus 12:40). This is one of the things that the seventy elders who '
                   'translated the Torah into Greek for King Ptolemy changed, and wrote: “The dwelling of '
                   'the children of Israel who dwelt in Egypt and in other lands was thirty years and four '
                   'hundred years.” In the same way they wrote for him: “God created in the beginning,” '
                   '“I will make man in image and in likeness”… “And He finished on the sixth day, and He '
                   'rested on the seventh day”…',
                   'ours', ref='Mekhilta DeRabbi Yishmael, Tractate Pischa 14', start='ומושב',
                   highlight=['vaychal']),
        question(f'{prefix}-q-a1', h, 'א/q1', '1. What is the difficulty that brought them to this change?'),
        # Not Sefaria's English: it adds the lemma and Rashi's sources, which aren't in her text.
        commentary(f'{prefix}-a-rashi', h, 2, 'Rashi', 'רש"י', 'Rashi',
                   'R. Shimon says: Flesh and blood, who does not know his times and moments, must add from '
                   'the weekday onto the holy; the Holy One, blessed be He, who knows His times and moments, '
                   'entered it by a hair’s breadth, and it seemed as though He finished on that very day. '
                   'Another explanation: What did the world lack? Rest. Shabbat came, rest came; the work was '
                   'finished and completed.',
                   'ours', ref='Rashi on Genesis 2:2:1', highlight=['vaychal']),
        commentary(f'{prefix}-a-ibn-ezra', h, 3, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'Some say that the days are created, and with the creation of the seventh day the work '
                   'was complete; and this interpretation is tasteless. And some say there is a bet whose '
                   'sense is “before,” as in “You shall not muzzle an ox in its threshing” (Deuteronomy '
                   '25:4); “But on the first day you shall put away leaven” (Exodus 12:15). And why this '
                   'trouble? Finishing a work is not a work; it is as if it said: He did no work. And so too '
                   'the meaning of “finished,” and also of “ceased.” And the sense of “His work which He had '
                   'done” is: on the sixth day, before the Sabbath day. And the sense of “and He ceased on '
                   'the seventh day from all His work” is: from all the creatures He had created.',
                   'ours', ref='Ibn Ezra on Genesis 2:2', highlight=['vaychal', 'vayishbot']),
        # Sefaria's English is a paraphrase with an editor's note; ours translates her text.
        commentary(f'{prefix}-a-sforno', h, 4, 'Sforno', 'ספורנו', 'Sforno',
                   'At the beginning of the seventh day, which is the indivisible instant that is the start '
                   'of the time to come and is not a part of it; as the Sages, of blessed memory, said: He '
                   'entered it by a hair’s breadth.',
                   'ours', ref='Sforno on Genesis 2:2:1', highlight=['vaychal']),
        question(f'{prefix}-q-a2', h, 'א/q2', '2. How do they resolve this difficulty: Rashi (two '
                 'interpretations), Ibn Ezra (three interpretations), Sforno?'),
        question(f'{prefix}-q-a3', h, 'א/q3', '3. Explain the expressions in Ibn Ezra’s words: “And why this '
                 'trouble?” “Finishing a work is not a work.”'),

        # §ב — scan header: ב. פסוק ג' אשר ברא אלקים לעשות.
        narration(f'{prefix}-b-intro', 'Genesis 2:3 ends “asher bara Elohim la’asot”: literally, “which God '
                  'created, to make.”', highlight=['laasot']),
        commentary(f'{prefix}-b-rashi', h, 6, 'Rashi', 'רש"י', 'Rashi',
                   'The work that was fit to be done on Shabbat, He doubled and did on the sixth day, as is '
                   'explained in Bereshit Rabbah (11:10).',
                   'ours', ref='Rashi on Genesis 2:3:2', highlight=['laasot']),
        # Her stop is «עד לעשות אותם»; the digitized text reads «לעשות דמותם», so the card stops
        # at the end of that first sentence.
        commentary(f'{prefix}-b-ibn-ezra', h, 7, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'The roots in all the species, into which He put the power to make their likeness.',
                   'ours', ref='Ibn Ezra on Genesis 2:3', stop='לעשות דמותם.', highlight=['laasot']),
        commentary(f'{prefix}-b-ramban', h, 8, 'Ramban', 'רמב"ן', 'Ramban',
                   'The work that was fit to be done on Shabbat He doubled and did on the sixth day, as is '
                   'explained in Bereshit Rabbah (11:9): the wording of Rashi. But R. Avraham [Ibn Ezra] said it '
                   'according to its plain sense: that His work is “the roots in all the species, into which '
                   'He put the power to make their like.” And to me its meaning appears to be: that He ceased '
                   'from all His work which He had created from nothing, to make from it all the works '
                   'mentioned in the six days.',
                   'ours', ref='Ramban on Genesis 2:3:1', stop='בששת הימים.', highlight=['laasot']),
        commentary(f'{prefix}-b-radak', h, 9, 'Radak', 'רד"ק', 'Radak',
                   '“To make” from now on: He created them in the six days of making, so that they would '
                   'make from now on, each species its offspring, according to what they are.',
                   'ours', ref='Radak on Genesis 2:3', highlight=['laasot']),
        # Malbim isn't digitized; his words are her own quotation, inside her §ב prose.
        commentary(f'{prefix}-b-malbim', h, 'ב/text1', 'Malbim', 'מלבי"ם', 'Malbim',
                   'It was not a resting of idleness, but “to make”: He ceased from all His work, which is '
                   'the work of nature, so as to make new makings, which are the work of the governance of '
                   'Providence, which conducts itself according to deeds, and according to reward and '
                   'punishment.',
                   'ours', start='לא היתה שביתה', highlight=['laasot']),
        question(f'{prefix}-q-b1', h, 'ב/q1', '1. What is the difference between the views above?'),
        question(f'{prefix}-q-b2', h, 'ב/q2', 'Can support for one of them be brought from the verses: Judges '
                 '13:9; Jeremiah 16:12; Joel 2:20; Psalms 126:3?'),
        # [10] Judges 13:9 is left out: it has no «לעשות» (13:19 has «ומפלא לעשות»); see creation.md.
        commentary(f'{prefix}-b-jer', h, 11, 'Tanakh', 'ירמיהו', 'Jeremiah 16:12',
                   '“And you have done worse than your fathers: here you are, each walking after the '
                   'stubbornness of his evil heart, not listening to Me.”',
                   'ours', ref='Jeremiah 16:12'),
        commentary(f'{prefix}-b-joel', h, 12, 'Tanakh', 'יואל', 'Joel 2:20',
                   '“And the northerner I will remove far from you, and drive him into a land of drought and '
                   'desolation, his face toward the eastern sea and his rear toward the western sea; and his '
                   'stench shall rise, and his foul smell shall rise, for he has done great things.”',
                   'ours', ref='Joel 2:20'),
        commentary(f'{prefix}-b-ps', h, 13, 'Tanakh', 'תהלים', 'Psalms 126:3',
                   '“The Lord has done great things for us; we were glad.”',
                   'ours', ref='Psalms 126:3', stop='שְׂמֵחִים"'),

        # §ג — scan header: ג. פסוק ז' [sic] אלה תולדות. Rashi (ד"ה אלה) isn't digitized.
        narration(f'{prefix}-g-intro', '“Such is the story of heaven and earth when they were created.”',
                  highlight=['toldot']),
        commentary(f'{prefix}-g-ramban', h, 15, 'Ramban', 'רמב"ן', 'Ramban',
                   'It tells the generations of the heaven and the earth, in rain and in growth, as they were '
                   'created and made in their proper order: for the heavens give their dew and their rain, '
                   'and the earth gives its produce, and they are the sustenance of every living thing.',
                   'ours', ref='Ramban on Genesis 2:4:1', start='יספר', stop='כל חי.', highlight=['toldot']),
        commentary(f'{prefix}-g-sforno', h, 16, 'Sforno', 'ספורנו', 'Sforno',
                   'These, the plants and the living creatures of which we spoke, were the generations of '
                   'the heaven and the earth, by a power present in them from the moment they were created; '
                   'for from then there were in them active and passive forces, for things that come to be '
                   'and pass away, as the Sages said: “‘the heaven,’ to include its generations, and ‘the '
                   'earth,’ to include its generations.” Yet they came out into actuality [only later].',
                   'ours', ref='Sforno on Genesis 2:4:1', highlight=['toldot']),
    ]})

    secs.append({'id': f'{prefix}-2r', 'titleCard': False, 'title': {'en': 'The Leningrad Codex, folio 2r'},
                 'primaryText': {**FOLIO_2R, 'regions': {'toldot': {'x': 0.37, 'y': 0.314, 'w': 0.2, 'h': 0.03}}},
                 'steps': [
        narration(f'{prefix}-codex', 'This is a page of the Leningrad Codex, a complete Hebrew Bible copied '
                  'in 1008. It carries Genesis 1:26 to 2:19.'),
        narration(f'{prefix}-toldot', 'Genesis 2:4, “Such is the story of heaven and earth,” begins on this '
                  'line. In this codex it starts a new paragraph, after an open break.',
                  highlight=['toldot']),
        question(f'{prefix}-q-g', h, 'ג/q1', 'What is the construction of this verse according to the views '
                 'above: is it the close of the account of the works of creation, or the heading of the '
                 'following verse?'),
    ]})

    secs.append({'id': f'{prefix}-ed', 'titleCard': False, 'title': {'en': 'A Flow from the Ground'},
                 'primaryText': primary('Genesis 2:5-6', ['2:5', '2:6'], {
                     'lo-himtir': ('כי לא המטיר', 'had not sent rain'),
                     'ed': ('ואד יעלה מן הארץ', 'a flow would well up from the ground'),
                     'haadamah': ('את כל פני האדמה', 'the whole surface of the earth'),
                 }), 'steps': [
        # §ד — scan header: ד. בפרק [sic] ו'. ואד יעלה מן הארץ והשקה את כל פני האדמה.
        narration(f'{prefix}-d-intro', 'Genesis 2:5–6: before any shrub of the field, and the flow from the ground.'),
        question(f'{prefix}-q-d1', h, 'ד/q1', '1. Why is “ha-aretz” [the earth] said at the beginning of the '
                 'verse, and “ha-adamah” [the ground] at its end?', highlight=['ed', 'haadamah']),
        commentary(f'{prefix}-d-ibn-ezra', h, 18, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the Gaon said that its meaning is: “and no ed [flow] would go up from the earth.”',
                   'ours', ref='Ibn Ezra on Genesis 2:6', start='והגאון אמר', highlight=['ed']),
        # Stops before «וכן אני מתי מספר», whose digitized citation (בראשית ל"ד ד') is a slip for 34:30.
        commentary(f'{prefix}-d-ibn-ezra-deut', h, 19, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra, on Deuteronomy 33:6',
                   '“And may his men be a number”: and may his men not be a number; as in “And I have not '
                   'learned wisdom” (Proverbs 30:3), and the bet in “as El Shaddai” (Exodus 6:3), as I have '
                   'explained many times. For it is possible that he live forever and yet they be few, and '
                   'anything that can be counted is few.',
                   'ours', ref='Ibn Ezra on Deuteronomy 33:6', start='ויהי מתיו מספר:', stop='הוא מעט.',
                   highlight=['ed']),
        question(f'{prefix}-q-d2', h, 'ד/q2', '2. Read Ibn Ezra, on “Ve-ed,” from “And the Gaon said,” and also '
                 'his words on Deuteronomy 33:6, on “And may his men be a number.”'),
        question(f'{prefix}-q-d3', h, 'ד/q3', 'Which word from the preceding verses must be put into our verse '
                 'according to the method of Rav Saadia Gaon (in place of “lo” [not], according to Ibn Ezra’s '
                 'version), to resolve the contradiction between verse 5 and verse 6?'),
    ]})
    return secs


def leaf_1954(prefix='cr-1954'):
    """Gilayon תשי"ד (161401): §ב, §ג, §ד. §א (Psalm 104) is out (pack §7)."""
    h = harvest('creation', '1954')
    P = lambda: primary('Genesis 1:1-3', ['1:1', '1:2', '1:3'], {
        'bereshit': ('בראשית ברא אלהים', 'When God began to create'),
        'vayomer': ('ויאמר אלהים', 'God said'),
        'vayehi-or': ('ויהי אור', 'and there was light'),
    })
    moreh = ('Rambam', 'רמב"ם', 'Rambam, Moreh Nevukhim')
    return [{'id': prefix, 'title': {'en': '1954 · Why Begin with Creation?'}, 'primaryText': P(), 'steps': [
        # §ב — scan header: ב. בראשית ברא אלוקים. [4] (Rashi 1:1:2) is NOT-IN-SCAN: not quoted.
        narration(f'{prefix}-intro', 'Genesis 1:1–3: the opening of the Torah.'),
        commentary(f'{prefix}-rashi', h, 5, 'Rashi', 'רש"י', 'Rashi',
                   'R. Yitzhak said: The Torah need not have begun except from “This month shall be for you” '
                   '(Exodus 12:2), which is the first commandment Israel was commanded. And why did it open '
                   'with “In the beginning”? Because of (Psalms 111) “He declared to His people the power of '
                   'His works, to give them the inheritance of nations.” For if the nations of the world say '
                   'to Israel, “You are robbers, for you conquered the lands of the seven nations,” they say '
                   'to them: “All the earth belongs to the Holy One, blessed be He. He created it and gave it '
                   'to whomever was right in His eyes. By His will He gave it to them, and by His will He '
                   'took it from them and gave it to us.”',
                   'ours', ref='Rashi on Genesis 1:1:1', start='אמר רבי יצחק', highlight=['bereshit']),
        commentary(f'{prefix}-ramban-1', h, 6, 'Ramban', 'רמב"ן', 'Ramban',
                   'R. Yitzhak said: The Torah need not have begun except from “This month shall be for you,” '
                   'which is the first commandment Israel was commanded. And why did it open with “In the '
                   'beginning”? Because of “He declared to His people the power of His works”: so that if the '
                   'nations of the world say, “You are robbers, for you conquered for yourselves the lands of '
                   'the seven nations,” they say to them: “All the earth belongs to the Holy One, blessed be '
                   'He, and He gave it to whomever was right in His eyes; by His will He gave it to them, and '
                   'by His will He took it from them and gave it to us.” This is an aggadah, in the wording in '
                   'which our Rabbi Shlomo [Rashi] wrote it in his commentaries. And one may ask about it: '
                   'there is great need to begin the Torah with “In the beginning God created,” for it is the '
                   'root of faith, and one who does not believe this, and thinks the world is eternal, denies '
                   'the fundamental principle and has no Torah at all. And the answer: because the work of '
                   'creation is a deep secret, not understood from the verses, and it cannot be known fully '
                   'except through the tradition reaching back to Moses our teacher from the mouth of the '
                   'Almighty, and those who know it are obliged to conceal it. Therefore R. Yitzhak said that '
                   'the beginning of the Torah has no need of “In the beginning God created,” and of the '
                   'account of what was created on the first day and what was made on the second day and the '
                   'other days, and of the length at which it tells of the forming of Adam and Eve, their sin '
                   'and their punishment, and the story of the garden of Eden and Adam’s expulsion from it; for '
                   'none of this can be fully understood from the Scriptures. All the more so the story of the '
                   'generation of the Flood and of the Dispersion, for which the need is not great. The people '
                   'of the Torah would have managed without these Scriptures, and would believe, in general '
                   'terms, what is mentioned to them in the Ten Commandments (Exodus 20:11): “For in six days '
                   'the Lord made heaven and earth, the sea and all that is in them, and He rested on the '
                   'seventh day”; and the knowledge would remain with the few among them, as a law given to '
                   'Moses at Sinai, together with the Oral Torah.',
                   'ours', ref='Ramban on Genesis 1:1:1', start='אמר רבי יצחק', stop='עם התורה שבעל פה.',
                   highlight=['bereshit']),
        question(f'{prefix}-q-b1', h, 7, '1. Ramban wonders at R. Yitzhak’s question about the beginning of '
                 'the Torah. Explain what his (Ramban’s) wonder is.'),
        question(f'{prefix}-q-b2', h, 8, '2. Ramban deepens and explains R. Yitzhak’s question, to remove the '
                 'wonder. Explain what Ramban corrected, in his words, in R. Yitzhak’s question (as cited in '
                 'Rashi).'),
        commentary(f'{prefix}-ramban-2', h, 6, 'Ramban', 'רמב"ן', 'Ramban',
                   'And R. Yitzhak gave a reason for it: the Torah began with “In the beginning God created” '
                   'and the account of the whole matter of creation up to the creation of man, and that He made '
                   'him ruler over the works of His hands and put all things under his feet; and that the '
                   'garden of Eden, the choicest of the places created in this world, was made the seat of his '
                   'dwelling, until his sin drove him out from there; and the people of the generation of the '
                   'Flood, for their sin, were driven out of the whole world, and only the righteous one among '
                   'them escaped, he and his sons; and the sin of their descendants caused them to be scattered '
                   'across places and dispersed among lands, and they took places for themselves, by their '
                   'families in their nations, as it happened to fall to them. If so, it is fitting that when a '
                   'nation goes on sinning it should lose its place, and another nation come to inherit its '
                   'land, for such has been God’s judgment on the earth from of old. All the more so with what '
                   'Scripture tells, that Canaan is cursed and sold as a slave forever (9:27): it is not fitting '
                   'that he inherit the choicest of the settled places; rather, the servants of the Lord, the '
                   'seed of His beloved, should inherit it, as it is written (Psalms 105:44): “He gave them the '
                   'lands of nations; they inherited the toil of peoples, that they might keep His laws and '
                   'observe His teachings.” That is: He drove out from there those who rebel against Him, and '
                   'settled in it those who serve Him, so that they would know that by serving Him they inherit '
                   'it, and that if they sin against Him the land will vomit them out, as it vomited out the '
                   'nation that was before them.',
                   'ours', ref='Ramban on Genesis 1:1:1', start='ונתן רבי יצחק טעם לזה', stop='אשר לפניהם.',
                   highlight=['bereshit']),
        commentary(f'{prefix}-ramban-3', h, 6, 'Ramban', 'רמב"ן', 'Ramban',
                   'And what makes clear the interpretation I have written is their wording in Bereshit Rabbah '
                   '(1:3), where they said it thus: R. Yehoshua of Sikhnin opened in the name of R. Levi: “He '
                   'declared to His people the power of His works” (Psalms 111:6). Why did the Holy One, blessed '
                   'be He, reveal to Israel what was created on the first day and what was created on the '
                   'second day? Because of the seven nations, so that they would not taunt Israel and say to '
                   'them, “Are you not a nation of plunderers?” And Israel answers them: “And you, is it not '
                   'plunder in your hands? Did not the Caphtorim, who came out of Caphtor, destroy them and '
                   'settle in their place (Deuteronomy 2:23)? The world and all that fills it belongs to the '
                   'Holy One, blessed be He. When He wished He gave it to you; when He wished He took it from '
                   'you and gave it to us.” That is what is written: “to give them the inheritance of nations, '
                   'He declared to His people the power of His works” (Psalms 111:6): in order to give them the '
                   'inheritance of nations, He told them of Bereshit [the beginning].',
                   'ours', ref='Ramban on Genesis 1:1:1', start='ואשר יבאר הפירוש', stop='הגיד להם את בראשית.',
                   highlight=['bereshit']),
        # Her stop: «עד "אם כן נתבאר מה שאמרנו"».
        commentary(f'{prefix}-ramban-4', h, 6, 'Ramban', 'רמב"ן', 'Ramban',
                   'And they already have, from another place, the matter I mentioned about the hidden things '
                   'of the work of creation. Our Rabbis, of blessed memory, said (see the introduction to the '
                   'Guide of the Perplexed): “He declared to His people the power of His works”: to tell the '
                   'power of the work of creation to flesh and blood is impossible; therefore Scripture told it '
                   'to you closed: “In the beginning God created.” If so, what we said has been made clear',
                   'ours', ref='Ramban on Genesis 1:1:1', start='וכבר בא להם', stop='אם כן נתבאר מה שאמרנו',
                   highlight=['bereshit']),
        question(f'{prefix}-q-b3', h, 9, '3. Ramban, in explaining the words of R. Yitzhak above, cites the words '
                 'of R. Yehoshua of Sikhnin in the name of R. Levi, from the Midrash Rabbah. How do the words '
                 'of this midrash help us understand R. Yitzhak’s question?'),
        question(f'{prefix}-q-b4', h, 10, '4. How does R. Yitzhak answer his question (within Rashi’s words), '
                 'and how does Ramban deepen and broaden this answer of his?'),
        # Her scan reads דברים ב' כ"ב; the digitizers corrected it to כ"ג (triage: use digitized).
        question(f'{prefix}-q-b5', h, 11, '5. For what purpose does Ramban draw on Deuteronomy 2:23?'),

        # §ג — scan header: ג. ג. ויאמר אלוקים יהי אור ויהי אור ("ויאמר" underlined).
        narration(f'{prefix}-g-intro', '“God said.”', highlight=['vayomer']),
        commentary(f'{prefix}-ibn-ezra', h, 14, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'The Gaon said that the meaning of “va-yomer” [“said”] is like “and He willed.” But were '
                   'that so, it ought to have said “for there to be light.”',
                   'ours', ref='Ibn Ezra on Genesis 1:3', start='אמר הגאון', highlight=['vayomer']),
        commentary(f'{prefix}-ramban-or', h, 15, 'Ramban', 'רמב"ן', 'Ramban',
                   'The word “saying” here indicates desire, as in (I Samuel 20) “Whatever your soul says, I '
                   'will do for you”: whatever you will and desire. And so (Genesis 24:51) “and let her be a '
                   'wife to your master’s son, as the Lord has spoken”: as He willed. For such is will before '
                   'Him.',
                   'ours', ref='Ramban on Genesis 1:3:1', highlight=['vayomer']),
        commentary(f'{prefix}-moreh-1', h, 16, *moreh,
                   '“Speech” and “belief” [so in the text; Ibn Tibbon has “saying”] are an equivocal term (one with several meanings). It is used of '
                   'speech with the tongue, as in “Moses spoke” (Exodus 19:19), “And Pharaoh said” (Exodus '
                   '5:5). It is used of a notion pictured in the mind without being spoken, as it says '
                   '(Ecclesiastes 3): “And I said in my heart,” “And I spoke in my heart”; (Genesis 27:41) '
                   '“And Esau said in his heart”; and this is frequent. And it is used of will: (II Samuel '
                   '21:16) “And he said to strike David,” as if it said: and he willed to kill him, that is, he '
                   'thought in his heart to kill him. (Even Shmuel’s comment: the third meaning of “speech” is '
                   'will, that is, apprehension that strives toward action.) (Exodus 3): “Do you say to kill '
                   'me?” means: Do you will to kill me?',
                   'ours', start='ה"דיבור"', stop='התרצה להרגני.', highlight=['vayomer']),
        commentary(f'{prefix}-moreh-2', h, 16, *moreh,
                   'And every “saying” and “speech” ascribed to the Lord belongs to the last two meanings; I '
                   'mean, they are either a figure for will and desire (of God) or a figure for a notion '
                   'understood from the Lord… And as for the figure of will and desire by “saying” and '
                   '“speech”… for at first thought (before going deeply into the matter) a person does not '
                   'understand how the thing that the one who wills wishes to do is done by will alone. (A '
                   'person does not at all understand how, when something arises in the will of one who wills, '
                   'the thing can be done by will alone, without action joined to it: a person knows from his '
                   'limited experience that his own will does not bring about the things he wills, unless he '
                   'labors and toils at them.) Rather, at first knowledge it is impossible but that the one who '
                   'wills does the thing he wills to bring into being, or commands another to do it. (On '
                   'superficial thought it is quite impossible that, when one who wills wishes to bring '
                   'something into being, the thing come into being without doing, whether on the part of the '
                   'one who wills or on the part of someone else who was commanded to do it.) And therefore '
                   '(since there are only these two possibilities) command was borrowed for the Lord, for the '
                   'coming-to-be of what He willed to be, and it was said that He commanded that it be so. '
                   '(They ascribed command to God, “saying” and “speech” in the sense of command, whenever they '
                   'came to tell of the coming-to-be of what God willed to come to be, and said that God '
                   'commanded that this thing come to be. For example: “And God said, ‘Let there be light’” '
                   'means He commanded that the light come to be. And it is understood that one is not to think '
                   'of a real command, and that this is only a borrowing, from a likeness to our own actions, '
                   'which are not the fruit of will alone, but the fruit of doing or of a command to do.)… And '
                   'all that comes in the work of creation, “And He said,” “And He said,” means: He willed, or '
                   'He desired.',
                   'ours', start='וכל "אמירה', stop='רצה או חפץ.', highlight=['vayomer']),
        commentary(f'{prefix}-moreh-3', h, 16, *moreh,
                   '…And the proof of it, that these “sayings” are acts of will and not utterances: utterances '
                   'of command are made only to an existing thing that would receive that command. So they '
                   'said (Psalms 33:6): “By the word of the Lord the heavens were made, and by the breath of His '
                   'mouth all their host”: just as “His mouth” and “the breath of His mouth” are a borrowing, so '
                   '“His word” and “His saying” are a borrowing…',
                   'ours', start='והמופת עליו', highlight=['vayomer']),
        question(f'{prefix}-q-g1', h, 17, '1. Do Rav Saadia (cited in Ibn Ezra), Rambam and Ramban here agree '
                 'in their interpretation of “va-yomer”?'),
        question(f'{prefix}-q-g2', h, 18, '2. What is Ibn Ezra’s claim against Rav Saadia, and how can his '
                 'complaint be removed from the interpretation of Rav Saadia Gaon?'),
        question(f'{prefix}-q-g3', h, 19, '3. The two verses that Ramban brings as proof that “va-yomer” comes '
                 'in the sense of “willed” are not brought in Rambam’s list of verses for this sense. Can you '
                 'guess why Rambam refrained from bringing precisely these?'),
        question(f'{prefix}-q-g4', h, 20, '4. Explain: what is Rambam’s proof that “va-yomer” in our chapter '
                 'cannot be interpreted as “va-yetzav” [“and He commanded”]?'),
        question(f'{prefix}-q-g5', h, 21, '5. Explain why the Torah borrowed, for the act of the Creator’s '
                 'will, precisely the verb of “saying.”', highlight=['vayomer']),
        # Stops before her parenthetical, whose last word is unresolved in the scan («הקבה"ו[?]»).
        question(f'{prefix}-q-g6', h, 22, '6. On the basis of our verse, the Sages added another name for God. '
                 'Which is it?', stop='איזהו?'),
        question(f'{prefix}-q-g7', h, 23, '7. Our verse, and all that is bound up with it, left its stamp on one '
                 'place in the morning prayer. Which is it?'),

        # §ד — scan header: ד. ד. יהי אור ויהי אור.
        narration(f'{prefix}-d-intro', '“And there was light.”', highlight=['vayehi-or']),
        question(f'{prefix}-q-d', h, 26, 'Why is it said only on the first day in this form, and not, as on the '
                 'second, third and fourth days, “and it was so”?', highlight=['vayehi-or']),
    ]}]
