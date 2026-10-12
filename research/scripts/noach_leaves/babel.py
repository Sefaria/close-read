from noach_lib import *  # noqa: F401,F403
"""Theme 5 — Babel (Gen 10:1–11:9): leaves 1944, 1960, 1968.

Paper trail: research/parshiyot/noach-leaves/babel.md (slices, omissions, open items).
"""


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_11_1_3():
    return primary('Genesis 11:1-3', ['11:1', '11:2', '11:3'], {
        'safa': ('שפה אחת', 'the same language'),
        'devarim': ('ודברים אחדים', 'the same words'),
        'mikedem': ('ויהי בנסעם מקדם', 'as they migrated from the east'),
        'shinar': ('וימצאו בקעה בארץ שנער', 'they came upon a valley in the land of Shinar'),
        'ish-el-reehu': ('ויאמרו איש אל רעהו', 'They said to one another'),
        'levenim': ('הבה נלבנה לבנים ונשרפה לשרפה', 'Come, let us make bricks and burn them hard'),
        'levenah': ('ותהי להם הלבנה לאבן', 'Brick served them as stone'),
    })


def gen_11_4_9():
    return primary('Genesis 11:4-9', ['11:4', '11:5', '11:6', '11:7', '11:8', '11:9'], {
        'ir-migdal': ('הבה נבנה לנו עיר ומגדל', 'Come, let us build us a city, and a tower'),
        'rosho': ('וראשו בשמים', 'with its top in the sky'),
        'shem': ('ונעשה לנו שם', 'to make a name for ourselves'),
        'pen-nafutz': ('פן נפוץ על פני כל הארץ', 'else we shall be scattered all over the world'),
        'vayered': ('וירד יהוה לראת', 'The Lord came down to look'),
        'bnei-haadam': ('אשר בנו בני האדם', 'that the mortals had built'),
        'am-ehad': ('הן עם אחד ושפה אחת לכלם', 'as one people with one language for all'),
        'hahilam': ('וזה החלם לעשות', 'this is how they have begun to act'),
        'lo-yibatzer': ('ועתה לא יבצר מהם כל אשר יזמו לעשות',
                        'nothing that they may propose to do will be out of their reach'),
        'nerda': ('הבה נרדה ונבלה שם שפתם', 'Let us, then, go down and confound their speech there'),
        'vayafetz': ('ויפץ יהוה אתם משם', 'Thus the Lord scattered them from there'),
        'balal': ('כי שם בלל יהוה שפת כל הארץ', 'because there the Lord confounded the speech of the whole earth'),
        'hefitzam': ('ומשם הפיצם יהוה', 'and from there the Lord scattered them'),
    })


def gen_11_5_7():
    return primary('Genesis 11:5-7', ['11:5', '11:6', '11:7'], {
        'vayered': ('וירד יהוה לראת', 'The Lord came down to look'),
        'ir-migdal': ('את העיר ואת המגדל אשר בנו בני האדם', 'at the city and tower that the mortals had built'),
        'am-ehad': ('הן עם אחד ושפה אחת לכלם', 'as one people with one language for all'),
        'lo-yibatzer': ('ועתה לא יבצר מהם כל אשר יזמו לעשות',
                        'nothing that they may propose to do will be out of their reach'),
        'nerda': ('הבה נרדה', 'Let us, then, go down'),
        'navlah': ('ונבלה שם שפתם', 'confound their speech there'),
    })


# ─── 1944 ───────────────────────────────────────────────────────────────────

def leaf_1944(prefix='bb-1944'):
    """Gilayon תש"ד (161942): §א (two panels), §ב (one cluster), §ג. §ד is out (pack §7)."""
    h = harvest('babel', '1944')
    secs = []

    # §א — scan header: א. חטאו של דור הפלגה.  Her five questions stand at the end of the
    # section; here Q2–Q5 each follow the source they ask about, and Q1 ("according to the
    # above") closes the section.
    secs.append({'id': prefix, 'title': {'en': '1944 · The Builders’ Sin'},
                 'primaryText': gen_11_1_3(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 11:1–3: one language, a journey, and bricks.'),
        commentary(f'{prefix}-br', h, 1, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Elazar says: “One language and devarim ahadim”: dibburim ahadim. The deed of the '
                   'generation of the Flood was made explicit; the deed of the generation of the Dispersion '
                   'was not made explicit.',
                   'ours', highlight=['safa', 'devarim']),
        commentary(f'{prefix}-ahadim', h, 2, 'Nechama Leibowitz', 'נחמה ליבוביץ', 'Nechama Leibowitz',
                   '(The meaning of “ahadim”: closed, from the Aramaic, as in Genesis 18:10 [the verse is '
                   'Genesis 19:10], “and they shut the door,” which Targum Onkelos renders ahadu.)',
                   'ours', highlight=['devarim']),
        question(f'{prefix}-q-a2', h, 16, '2. Bring proofs from the wording of the text for the view of '
                 'R. Elazar in Bereshit Rabbah.', highlight=['devarim']),
        commentary(f'{prefix}-pdre', h, 3, 'Pirkei de-Rabbi Eliezer', 'פרקי דר\' אליעזר',
                   'Pirkei de-Rabbi Eliezer',
                   'The tower had seven steps on its east side and seven on its west. They carried the '
                   'bricks up on one side and came down on the other. If a man fell and died, they paid him '
                   'no mind; but if a single brick fell, they sat and wept and said: Woe to us! When will '
                   'another be brought up in its place?',
                   'ours', start='שבע מעלות', highlight=['levenim', 'levenah']),
        question(f'{prefix}-q-a3', h, 17, '3. What is the idea contained in the words of Pirkei de-Rabbi '
                 'Eliezer?', highlight=['levenah']),
        commentary(f'{prefix}-rashi-1a', h, 4, 'Rashi', 'רש"י', 'Rashi',
                   '“And devarim ahadim”: They came with one counsel and said: It is not all His, that He '
                   'should choose the upper realms for Himself. Let us go up to the firmament and make war '
                   'with Him.',
                   'ours', ref='Rashi on Genesis 11:1:2', highlight=['devarim']),
        commentary(f'{prefix}-rashi-1b', h, 5, 'Rashi', 'רש"י', 'Rashi',
                   'Another explanation: [words] about the Only One of the world.',
                   'ours', ref='Rashi on Genesis 11:1:2', highlight=['devarim']),
        commentary(f'{prefix}-rashi-1c', h, 6, 'Rashi', 'רש"י', 'Rashi',
                   'Another explanation: “devarim ahadim” (another reading: devarim haddim, sharp words): '
                   'they said, Once every 1,656 years the firmament totters, as it did in the days of the '
                   'Flood. Come, let us make supports for it (Bereshit Rabbah).',
                   'ours', ref='Rashi on Genesis 11:1:2', highlight=['devarim']),
    ]})

    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'The City and the Tower'},
                 'primaryText': gen_11_4_9(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 11:4–9: the city and the tower, and what the Lord did.'),
        # Her pointer reads «ב' ד"ה בני האדם»; the phrase is in 11:5.
        commentary(f'{prefix}-rashi-5', h, 7, 'Rashi', 'רש"י', 'Rashi',
                   '“The children of man”: Whose children, then? Perhaps the children of donkeys and '
                   'camels? Rather, the children of the first Adam, who was ungrateful for the good and '
                   'said, “The woman You put at my side.” These too were ungrateful for the good: they '
                   'rebelled against the One who showered good on them and saved them from the Flood.',
                   'ours', ref='Rashi on Genesis 11:5:2', highlight=['bnei-haadam']),
        commentary(f'{prefix}-rashi-9', h, 8, 'Rashi', 'רש"י', 'Rashi',
                   '“And from there He scattered them”: This teaches that they have no share in the World '
                   'to Come. And which was worse, the generation of the Flood or the generation of the '
                   'Dispersion? These did not lay a hand on the Root, and those laid a hand on the Root, to '
                   'make war on Him; yet these were swept away, and those were not lost from the world. But '
                   'the generation of the Flood were robbers, and there was strife among them; that is why '
                   'they were lost. These behaved with love and fellowship among themselves, as it says, '
                   '“one language and the same words.” You learn that strife is hateful and peace is great.',
                   'ours', ref='Rashi on Genesis 11:9:1', highlight=['hefitzam']),
        commentary(f'{prefix}-ie-a', h, 9, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'These builders of the tower were not fools, to think they could go up to heaven. Nor were '
                   'they afraid of the Flood, for Noah and his sons, to whom the Lord had sworn, were there, '
                   'and all of them obeyed them, for they were their children. Scripture has revealed what '
                   'they wanted and what they finally intended: to build a great city to live in, and to '
                   'build a high tower to be a sign for them, a name and a glory, so that those who went out '
                   'afield, like the herdsmen, would know where the city was; and also that their name would '
                   'endure after them for as long as the tower stood. That is what Scripture says: “to make '
                   'a name for ourselves.”',
                   'ours', ref='Ibn Ezra on Genesis 11:3:3', start='ואלה בוני המגדל', stop='ונעשה לנו שם.',
                   highlight=['ir-migdal', 'shem']),
        commentary(f'{prefix}-ie-b', h, 9, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And do not wonder at the words “with its top in the sky,” for so Moses spoke: “great '
                   'cities, fortified up to the sky.” These builders resolved among themselves that they '
                   'would not separate; but the Lord had not so counseled, and they did not know it.',
                   'ours', ref='Ibn Ezra on Genesis 11:3:3', start='ואל תתמה על מילת וראשו',
                   highlight=['rosho', 'pen-nafutz']),
        commentary(f'{prefix}-ie-7', h, 10, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'What is right in my eyes is that they were scattered from there; and after they were '
                   'scattered, Nimrod reigned over Babel, and other kings arose. And over many days, as the '
                   'first generation died, the first language was forgotten. The Lord scattered them, and '
                   'that was good for them; and so He had said, “and fill the earth.”',
                   'ours', ref='Ibn Ezra on Genesis 11:7', start='והנכון בעיני שנפוצו משם',
                   highlight=['nerda', 'vayafetz']),
        commentary(f'{prefix}-sf-4a', h, 11, 'Sforno', 'ספורנו', 'Sforno',
                   '“And they said, Come”: This was the counsel of the princes of the generation, to make '
                   'Nimrod king over the whole human race.',
                   'ours', ref='Sforno on Genesis 11:4:1', highlight=['ir-migdal']),
        commentary(f'{prefix}-sf-4b', h, 12, 'Sforno', 'ספורנו', 'Sforno',
                   '“And a tower with its top in the sky”: We will make a name (an idol) that will be in the '
                   'tower, and the fame of the height of its place and the greatness of its city will go out '
                   'through the whole human race, so that it will be thought the God of gods by all people, '
                   'and all will seek it. And the intention in this was that whoever ruled over that city '
                   'would rule over the whole human race, since all would seek there.',
                   'ours', ref='Sforno on Genesis 11:4:2', highlight=['rosho', 'shem']),
        commentary(f'{prefix}-sf-6a', h, 13, 'Sforno', 'ספורנו', 'Sforno',
                   '“Behold, one people”: For the undoing that frustrates the counsel of nations and thwarts '
                   'their designs is the strife that arises among them, whether because of religions or '
                   'because of languages. And these were one people in the matter of religion, for all of '
                   'them agreed with the opinion of the Sabians; and with that, all of them agreed in '
                   'language.',
                   'ours', ref='Sforno on Genesis 11:6:1', highlight=['am-ehad']),
        commentary(f'{prefix}-sf-6b', h, 14, 'Sforno', 'ספורנו', 'Sforno',
                   '“And now nothing will be withheld”: If so, nothing will prevent them from completing '
                   'their intention, and the idol they choose will be universal for all humankind, and not '
                   'one of them will turn to know the Creator, blessed be He, and to understand that He is '
                   'the Maker of all. The opposite will happen when there is strife among the nations over '
                   'foreign gods: for each will think that there is a God of gods, with whose will all the '
                   'deities agree, and through whom their order and the order of all existence is made '
                   'complete; as it says, “For from where the sun rises to where it sets, My name is great '
                   'among the nations.”',
                   'ours', ref='Sforno on Genesis 11:6:3', highlight=['lo-yibatzer']),
        question(f'{prefix}-q-a4', h, 18, '4. According to Sforno, how did the multiplicity of religions help '
                 'humanity advance?', highlight=['am-ehad', 'lo-yibatzer']),
        question(f'{prefix}-q-a5', h, 19, '5. What is the difficulty in the verse Malachi 1:1 [the verse is '
                 'Malachi 1:11] that Sforno cites, and how does he resolve the difficulty?'),
        question(f'{prefix}-q-a1', h, 15, '1. What was their sin, according to the above?',
                 highlight=['ir-migdal', 'rosho', 'shem', 'pen-nafutz']),
    ]})

    # §ב — scan header: ב. שאלות ודיוקים ברש"י:  Rendered: her item 2 only (Rashi on 11:2, the
    # midrash she quotes, Rashi on 13:11 and her question). Items 1, 3–7 are omitted; see babel.md.
    # Her question is typed inside the Rashi item [27]; it is cut out, and the Rashi quoted from
    # its own heading.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“As They Migrated From the East”'},
                 'primaryText': gen_11_1_3(), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 11:2: “And as they migrated from the east.”'),
        commentary(f'{prefix}-rashi-2', h, 25, 'Rashi', 'רש"י', 'Rashi',
                   '“As they migrated from the east”: for they had been living there, as is written above, '
                   '“Their settlements extended … the hill country to the east”; and they journeyed from there '
                   'to seek a place that would hold them all, and found none but Shinar.',
                   'ours', ref='Rashi on Genesis 11:2:1', highlight=['mikedem']),
        commentary(f'{prefix}-br-2', h, 26, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“They journeyed from one town to go into another town?” (They journeyed from the east, '
                   'for it is written, “their settlements … the hill country to the east,” to go eastward? It '
                   'is said in astonishment.) R. Elazar said: They removed themselves from the Ancient One of '
                   'the world. They said: We want neither Him nor His divinity.',
                   'ours', start='נסעו מן מדינתא', highlight=['mikedem']),
        commentary(f'{prefix}-rashi-13', h, 27, 'Rashi', 'רש"י', 'Rashi, on Genesis 13:11',
                   '“And Lot journeyed from the east [mi-kedem]”: He journeyed away from Abram (eastward) and '
                   'went to the west of Abram; so he was journeying from east to west. And a midrash '
                   'aggadah: he removed himself from the Ancient One [Kadmon] of the world, saying: I want '
                   'neither Abram nor his God.',
                   'ours', ref='Rashi on Genesis 13:11:2', start='ד"ה ויסע לוט מקדם', highlight=['mikedem']),
        question(f'{prefix}-q-b2', h, 27, 'Why does Rashi not bring the words of the midrash here, as he '
                 'brought them at chapter 13, verse 11?', stop='פסוק י"א', highlight=['mikedem']),
    ]})

    # §ג — scan header: ג. וירד ה' לראות.  The Moreh [38] is quoted in three slices, around two
    # source-text slips recorded in the scan check («כגדולה» for «בגדולה»; «תהלים ה'» for «ח'»).
    secs.append({'id': f'{prefix}-d', 'titleCard': False, 'title': {'en': '“The Lord Came Down to Look”'},
                 'primaryText': gen_11_5_7(), 'steps': [
        narration(f'{prefix}-g-intro', 'Genesis 11:5–7: the Lord comes down, and says, “Let us go down.”'),
        commentary(f'{prefix}-moreh-a', h, 38, 'Rambam', 'רמב"ם', 'Rambam, Moreh Nevukhim 1:10',
                   'Descending and ascending are two words set in the Hebrew language for a known matter: '
                   'when a body moves from one place to a place lower than it, one says “went down,” and '
                   'when it moves from one place to a place higher than it, one says “went up.”',
                   'ours', start='הירידה והעלייה', stop='יאמר "עלה".', highlight=['vayered']),
        commentary(f'{prefix}-moreh-b', h, 38, 'Rambam', 'רמב"ם', 'Rambam, Moreh Nevukhim 1:10',
                   'And likewise, when a blow comes down on a nation or a region by His eternal will, where '
                   'the books of prophecy, before telling of that blow, first tell that the Lord examined '
                   'their deeds and afterwards brought the punishment down on them (= as indeed we find the '
                   'books of prophecy bearing witness to this, that there is no punishment except for sin: '
                   'for before their account of the punishment God brought on people, they always give the '
                   'account of how God examined their deeds and found them flawed), this matter too is '
                   'called “descent,” for it is a lowering and a disgrace for a man that his deeds be '
                   'examined and that he be punished for them.',
                   'ours', start='וכן כשתרד מכה', stop='ויענש עליהם.', highlight=['vayered']),
        commentary(f'{prefix}-moreh-c', h, 38, 'Rambam', 'רמב"ם', 'Rambam, Moreh Nevukhim 1:10',
                   'And therefore (= for that reason) this matter is called “descent”: He said, “Let us go '
                   'down and confound their speech there”; “The Lord came down to look”; (18:21) “I will go '
                   'down and see.” And the whole matter is the coming of punishment on lowly people.',
                   'ours', start='ולזה', highlight=['vayered', 'nerda', 'navlah'], effect='glow'),
        question(f'{prefix}-q-g1', h, 40, '1. How does the Rambam interpret our verse?', highlight=['vayered']),
        question(f'{prefix}-q-g2', h, 41, '2. Which of our commentators also interprets in the Rambam’s way?'),
        commentary(f'{prefix}-g-rashi', h, 42, 'Rashi', 'רש"י', 'Rashi',
                   '“The Lord came down to look”: He had no need of this. Rather, it comes to teach judges '
                   'not to condemn the accused until they have seen and understood. In the Midrash of '
                   'R. Tanchuma.',
                   'ours', ref='Rashi on Genesis 11:5:1', highlight=['vayered']),
        commentary(f'{prefix}-g-sforno', h, 43, 'Sforno', 'ספורנו', 'Sforno',
                   '“The Lord came down to look”: The language of coming down to see is said of God, blessed '
                   'be He, when the matter does not yet deserve punishment at that time, except because of '
                   'the ruin that will follow from it in the end; like the wayward and rebellious son, of '
                   'whom they said: the Torah went down to his final mind. And so it was with Sodom, of which '
                   'it is written, “I will go down and see.” For their wickedness then was not greater than '
                   'that of the other idolaters, so as to punish them in this world, except in the matter of '
                   'cruelty toward the poor of the people, from which utter ruin would follow in the end; as '
                   'it says (Ezekiel 16:49), “Behold, this was the iniquity of your sister Sodom, and she did '
                   'not strengthen the hand of the poor and the needy.” And so was the punishment of Israel '
                   'when they were exiled, as it says, “I will see what their end shall be.”',
                   'ours', ref='Sforno on Genesis 11:5:1', highlight=['vayered']),
        question(f'{prefix}-q-g3', h, 44, 'How do they differ from the Rambam?', highlight=['vayered']),
    ]})
    return secs


# ─── 1960 ───────────────────────────────────────────────────────────────────

def leaf_1960(prefix='bb-1960'):
    """Gilayon תש"ך (161686): §א, §ב, and her §ד (digitized as ג). Her sheet has no §ג."""
    h = harvest('babel', '1960')
    secs = []

    # §א — scan header: א. אברבנאל.  Abarbanel on 10:8 [3] in four slices, on 11:1 [5] in two.
    secs.append({'id': prefix, 'title': {'en': '1960 · Nimrod'},
                 'primaryText': primary('Genesis 10:8-10, 11:1, 4, 9', ['10:8', '10:9', '10:10', '11:1', '11:4', '11:9'], {
                     'hehel': ('הוא החל להיות גבר בארץ', 'who was the first of the earth’s heroes'),
                     'gibor-tsayid': ('הוא היה גבר ציד לפני יהוה', 'He was a mighty hunter by the grace of the Lord'),
                     'kenimrod': ('כנמרד גבור ציד לפני יהוה', 'Like Nimrod a mighty hunter by the grace of the Lord'),
                     'reshit': ('ותהי ראשית ממלכתו בבל', 'The mainstays of his kingdom were Babylon'),
                     'safa': ('ויהי כל הארץ שפה אחת ודברים אחדים',
                              'Everyone on earth had the same language and the same words'),
                     'ir-migdal': ('הבה נבנה לנו עיר ומגדל', 'Come, let us build us a city, and a tower'),
                     'balal': ('כי שם בלל יהוה שפת כל הארץ', 'because there the Lord confounded the speech of the whole earth'),
                     'hefitzam': ('ומשם הפיצם יהוה על פני כל הארץ',
                                  'and from there the Lord scattered them over the face of the whole earth'),
                 }), 'steps': [
        narration(f'{prefix}-intro', 'Nimrod, son of Cush; and then the city and the tower.'),
        commentary(f'{prefix}-abar-a', h, 3, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   '…the Torah wished to tell our subject, which is this: until that time human beings were '
                   'all equal in rank, since all of them were the children of one man; and this Nimrod began '
                   'to make himself mighty and to rule over the people of his generation. Of this it is said, '
                   '“he began to be a mighty one in the earth,” meaning, an officer and ruler in it.',
                   'ours', start='שרצתה התורה', stop='שוטר ומושל בה.', highlight=['hehel']),
        commentary(f'{prefix}-abar-b', h, 3, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And it says further, “He was a mighty hunter before the Lord.” You already know how the '
                   'Sages interpreted it: that he hunted people’s minds with his schemes. But I think that '
                   'he was a great hunter of beasts. Scripture tells that he used two kinds of scheme to '
                   'make himself master over his people.',
                   'ours', start='ואמנם אמרו עוד', stop='להשתחרר על עמו:', highlight=['gibor-tsayid']),
        commentary(f'{prefix}-abar-c', h, 3, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'The first: he made himself a mighty hunter, hunting beasts and subduing them; and when '
                   'people saw that bears and lions, for all their strength, were subdued before him, they '
                   'too were afraid of him and were subdued before him. And this too is why it says, “He was '
                   'a mighty hunter before the Lord”: under all the heavens there was no mighty hunter like '
                   'him, so that he remained a byword among people until the time the Torah was written: '
                   '“Like Nimrod a mighty hunter before the Lord.” And perhaps Nimrod offered burnt '
                   'offerings to the Lord from his game, to make a show of piety and present himself as a '
                   'worshipper of God, for by this he would draw the people’s heart after him all the more; '
                   'and of this it says, “a mighty hunter before the Lord.”',
                   'ours', start='הראשון שעשה', stop='ועל זה אמר "גבור ציד לפני ה\'".',
                   highlight=['gibor-tsayid', 'kenimrod']),
        question(f'{prefix}-q-a3', h, 8, '3. How does Abarbanel interpret the expression “before the Lord”?',
                 highlight=['gibor-tsayid', 'kenimrod']),
        commentary(f'{prefix}-abar-d', h, 3, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'The second kind of scheme is that he built towers and strong fortified cities in the '
                   'land, to rule from there over all the land; for when he sits in a strong tower, dread and '
                   'fear of him fall on all who live in the plain. And of this it is said (10:10), “The '
                   'mainstays of his kingdom were Babel, Erech, Accad and Calneh”: for there, in the strong '
                   'cities that he built, he made the seat of his kingdom.',
                   'ours', start='והאופן השני', highlight=['reshit']),
        question(f'{prefix}-q-a4', h, 9, '4. How does Abarbanel see the beginning of inequality in the world, '
                 'and what are the ways by which people gained the power to rule over others?',
                 highlight=['hehel', 'reshit']),
        commentary(f'{prefix}-abar-e', h, 5, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And so the sin of the generation of the Dispersion was like the sin of Adam and of Cain '
                   'and his sons. For while they had from the Lord, from heaven, an abundance of the natural '
                   'things necessary for their existence, being free of work and of all toil and ready to '
                   'occupy themselves with the perfection of their souls, they were not content with what '
                   'their Creator had prepared for them in His broad, natural gift. They sought to put out '
                   'their hand and set all their thoughts on finding the crafts, in building a city, which '
                   'includes all the crafts, and a tower within it, so as to band together there and make '
                   'themselves city-dwellers instead of men of the field. They thought that the end proper to '
                   'them was the political community, so that partnership and society would extend among '
                   'them, and that this was the highest of human ends; together with all that follows from '
                   'it: titles and appointments and rulerships and imagined honors, the craving to gather '
                   'possessions, and the violence, robbery and bloodshed that follow, none of which existed '
                   'while they were in the field, each one on his own. As Solomon said (Ecclesiastes 7), “God '
                   'made man upright, but they have sought out many schemes.”',
                   'ours', start='וכן היה חטאת', stop='חשבונות רבים".', highlight=['safa', 'ir-migdal']),
        commentary(f'{prefix}-abar-f', h, 5, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And since all this is superfluous, not natural, hindering and burdening a person from '
                   'attaining his true perfection, the perfection of the soul, these sinful men were '
                   'punished in their souls, when the Lord confounded their language and scattered them over '
                   'the face of all the earth; as He drove the first Adam out of the Garden of Eden, and drove '
                   'Cain from the land where he lived, and drove his sons from the world with the waters of '
                   'the Flood. For their transgression was the same.',
                   'ours', start='ולהיות כל זה מותר', highlight=['balal', 'hefitzam']),
        question(f'{prefix}-q-a1', h, 6, '1. Explain: what is the shared transgression of the first Adam, '
                 'Cain, the sons of Cain (who is meant?), Nimrod and the generation of the Dispersion?'),
    ]})

    # §ב — scan header: ב. י' ט' הוא החל להיות גבור בארץ; הוא היה גבור ציד לפני ה'.
    # Her Q6 is numbered «5)» again on the scan (her duplicate numbering, kept).
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': 'A Mighty Hunter Before the Lord'},
                 'primaryText': primary('Genesis 10:8-9, 11:6', ['10:8', '10:9', '11:6'], {
                     'hehel': ('הוא החל להיות גבר בארץ', 'who was the first of the earth’s heroes'),
                     'gibor-tsayid': ('הוא היה גבר ציד', 'He was a mighty hunter'),
                     'lifnei': ('לפני יהוה על כן', 'by the grace of the Lord; hence'),
                     'kenimrod': ('כנמרד גבור ציד לפני יהוה', 'Like Nimrod a mighty hunter by the grace of the Lord'),
                     'hahilam': ('וזה החלם לעשות', 'this is how they have begun to act'),
                 }), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 10:8–9, and a phrase from the Babel story.'),
        commentary(f'{prefix}-br', h, 12, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '(Genesis 4): “Then men began to call on the name of the Lord.” R. Simon said: In three '
                   'places this wording is used, a wording of rebellion: (4:26) “Then men began [huhal] to '
                   'call on the name of the Lord”; (Genesis 6:1) “When men began [hehel] to multiply on the '
                   'face of the earth, and daughters were born to them…”; (10:8) “He began [hehel] to be a '
                   'mighty one in the earth.” They objected (and raise a difficulty with this): But it is '
                   'written (11:6), “and this is what they begin [hahillam] to do”? (If so, there are four '
                   'places and not three?) He struck at Nimrod’s head and said: “This one incited them to '
                   'rebel against Him!” (Matnot Kehunah: kippah is a word of striking; the Holy One, blessed '
                   'be He, struck at Nimrod’s head: “This one began them and led them to rebel against Me.” '
                   'And Nimrod was already counted among the three places, “he began,” and so he did not '
                   'count four places.)',
                   'ours', ref='Bereshit Rabbah 23:7', highlight=['hehel', 'hahilam']),
        commentary(f'{prefix}-maharzu', h, 13, 'Maharzu', 'מהרז"ו', 'Maharzu, on the midrash',
                   '“Huhal” is not from the sense of beginning but from the sense of profaning [hillul]. The '
                   'three places are: in the generation of Enosh, who worshipped idols, and the meaning of '
                   '“huhal” is that they made the worship of the Lord, blessed be He, profane; the second, in '
                   'the generation of the Flood, and this concerns sexual immorality; and the third, in the '
                   'generation of the Dispersion, as it is said of Nimrod, “he began to be a mighty one,” and '
                   'this is bloodshed: for by his might he overpowered the weak, and killed them, robbed them '
                   'and did them violence.',
                   'ours', start='"הוחל" אינו', highlight=['hehel']),
        question(f'{prefix}-q-b3', h, 20, '3. From where did the midrash learn to say that Nimrod was the one '
                 'who urged the plan of the tower on his generation?', highlight=['hehel', 'hahilam']),
        commentary(f'{prefix}-rashi-a', h, 14, 'Rashi', 'רש"י', 'Rashi',
                   '“To be a mighty one”: to make the whole world rebel against the Holy One, blessed be He, '
                   'by the counsel of the generation of the Dispersion (= by the counsel he gave, to build '
                   'the tower).',
                   'ours', ref='Rashi on Genesis 10:8:1', highlight=['hehel']),
        commentary(f'{prefix}-rashi-b', h, 15, 'Rashi', 'רש"י', 'Rashi',
                   '“A mighty hunter”: he trapped people’s minds with his mouth and misled them into '
                   'rebelling against the Omnipresent.',
                   'ours', ref='Rashi on Genesis 10:9:1', highlight=['gibor-tsayid']),
        commentary(f'{prefix}-rashi-c', h, 16, 'Rashi', 'רש"י', 'Rashi',
                   '“Before the Lord”: intending to provoke Him to His face.',
                   'ours', ref='Rashi on Genesis 10:9:2', highlight=['lifnei']),
        question(f'{prefix}-q-b4', h, 21, '4. What is difficult for Rashi in the comment on “before the Lord”?',
                 highlight=['lifnei']),
        question(f'{prefix}-q-b5', h, 22, '5. Why did he see fit to interpret the words “before the Lord” with '
                 'the words “to His face”? What did he correct by this?', highlight=['lifnei']),
        commentary(f'{prefix}-gur-aryeh', h, 17, 'Gur Aryeh', 'גור אריה', 'Gur Aryeh, on Rashi',
                   'And the plain sense of the text is that he was a powerful king. Even so, since Scripture '
                   'mentions his power and strength “before the Lord,” it implies that he incited rebellion '
                   'against the Holy One, blessed be He, <u>for might has no place “before the Lord.”</u> He '
                   'was mighty in a place where submission was fitting; this hints that his power was the '
                   'power of rebellion, akin to idolatry, for by this he incited rebellion against the Holy '
                   'One, blessed be He. And therefore he is called a “mighty hunter”: a mighty hunter is a '
                   'man of scheming and cunning who does not walk a simple, straight path, and this too was '
                   'his craft. And since it is written “before the Lord,” it comes to say that he was also a '
                   'man of scheming and cunning in divine matters, until he made people rebel against Him, '
                   'blessed be He.',
                   'ours', he=underline(cut(item(h, 17)[0], 'ופשוטו של מקרא'), 'דאין שייך גבורה לפני ה\''),
                   highlight=['gibor-tsayid', 'lifnei']),
        question(f'{prefix}-q-b2', h, 19, '2. Can you find a second reason, in addition to the reason of the '
                 'author of Gur Aryeh: what was the difficulty in our verse that led Rashi to bring the '
                 'words of the midrash here, and to interpret the verse not according to its plain meaning?',
                 highlight=['hehel']),
        question(f'{prefix}-q-b6', h, 23, '5) We have received: Rashi usually explains a difficult expression, '
                 'a strange word or a difficult form at its first appearance in the Torah, unless there was '
                 'a particular difficulty tied to the appearance of the word or expression in a second or '
                 'third place. Explain: what led Rashi here not to explain “before God” at the beginning of '
                 'the parasha (6:11–), “The earth became corrupt before God,” and to explain it in our '
                 'place?', highlight=['lifnei']),
    ]})

    # Her §ד — scan header: ד. י"א א' ויהי כל הארץ שפה אחת ודברים אחדים.  (Digitized as ג.)
    # Abarbanel [26] carries her underlining, recorded in the scan check; her Q4 asks about it.
    abar = item(h, 26)[0]
    abar_a = underline(underline(cut(abar, 'והיותר אמתי', 'נפרדו איש מאחיו.'),
                                 'ובאו לידי חילוף ויחוד'), '(פרקי אבות)')
    abar_b = underline(underline(cut(abar, 'וחז"ל דרשו'),
                                 'המנהג הטבעי הקדום להשתמש ולהסתפק בדברים הטבעיים'),
                       'הדברים המלאכותיים למלאות תאותם במותרות')
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“The Same Language and the Same Words”'},
                 'primaryText': primary('Genesis 11:1-4', ['11:1', '11:2', '11:3', '11:4'], {
                     'safa': ('שפה אחת', 'the same language'),
                     'devarim': ('ודברים אחדים', 'the same words'),
                     'mikedem': ('ויהי בנסעם מקדם', 'as they migrated from the east'),
                     'levenim': ('הבה נלבנה לבנים', 'Come, let us make bricks'),
                     'ir-migdal': ('הבה נבנה לנו עיר ומגדל', 'Come, let us build us a city, and a tower'),
                 }), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 11:1–4.'),
        commentary(f'{prefix}-c-abar-a', h, 26, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'What is truest in my view is that at that time they were of one language, that is, one '
                   'tongue for all people, created in the work of creation, common to all; and that the '
                   'things they had were likewise one, shared equally by all. For no person had a private '
                   'estate, nor any other private thing for his own use; everything was one, common and equal '
                   'to all, like the language. But when they turned to inventing the crafts, in building the '
                   'city and the tower, they removed themselves from brotherhood; possessions and estates '
                   'became private, and <u>they came to exchange and appropriation</u>, out of their desire '
                   'to take and assign to each one himself things of his own, and to say <u>(Pirkei '
                   'Avot)</u> “What is mine is mine, and what is yours is yours,” until because of this they '
                   'separated, each from his brother.',
                   'ours', he=abar_a, highlight=['safa', 'devarim', 'ir-migdal']),
        commentary(f'{prefix}-c-abar-b', h, 26, 'Abarbanel', 'אברבנאל', 'Abarbanel',
                   'And the Sages expounded (Bereshit Rabbah 38:7), “As they journeyed mi-kedem”: “they removed '
                   'themselves from the Kadmon, the Ancient One, of the world.” By this they meant that they '
                   'journeyed away from <u>the ancient, natural custom of using and making do with natural '
                   'things</u>, the necessary ones, and went after vanity and became vain, in seeking <u>the '
                   'artificial things, to fill their desire with superfluities</u>. And because by this they '
                   'distracted their minds from knowing the divine truths, the Sages expounded that they '
                   'removed themselves from the Ancient One of the world.',
                   'ours', he=abar_b, highlight=['mikedem'], effect='glow'),
        question(f'{prefix}-c-q1', h, 27, '1. How does his interpretation of our verse differ from the accepted '
                 'interpretation?', highlight=['safa', 'devarim']),
        question(f'{prefix}-c-q3', h, 29, '3) Compare with these words of Abarbanel the words of the Sages on '
                 'the sin of the generation of the Dispersion.'),
        commentary(f'{prefix}-c-pdre', h, 30, 'Pirkei de-Rabbi Eliezer', 'פרקי דר\' אליעזר',
                   'Pirkei de-Rabbi Eliezer',
                   'The tower had seven steps on its east side and seven on its west. They carried the '
                   'bricks up on one side and came down on the other. If a man fell and died, they paid him '
                   'no mind; but if a single brick fell, they sat and wept and said: Woe to us! When will '
                   'another be brought up in its place?',
                   'ours', start='שבע מעלות', highlight=['levenim', 'ir-migdal']),
        question(f'{prefix}-c-q3b', h, 'after 30', 'What is the difference between the approach of the midrash '
                 'and the approach of Abarbanel?'),
        question(f'{prefix}-c-q4', h, 31, '4. Explain the places in Abarbanel marked with a line.'),
    ]})
    return secs


# ─── 1968 ───────────────────────────────────────────────────────────────────

def leaf_1968(prefix='bb-1968'):
    """Gilayon תשכ"ח (160443): §א («שאלה כללית»), §ג, §ד. §ב (Mincha Belula) is out (pack §7)."""
    h = harvest('babel', '1968')
    secs = []

    # §א — scan: «שאלה כללית», then «א.» on the Radak line.
    secs.append({'id': prefix, 'title': {'en': '1968 · Scattered'},
                 'primaryText': primary('Genesis 10:5, 30, 32, 11:1, 6-7',
                                        ['10:5', '10:30', '10:32', '11:1', '11:6', '11:7'], {
                     'iyei': ('מאלה נפרדו איי הגוים', 'From these the maritime nations branched out'),
                     'lilshono': ('איש ללשנו', 'each with its language'),
                     'moshavam': ('ויהי מושבם ממשא', 'Their settlements extended from Mesha'),
                     'har-hakedem': ('הר הקדם', 'the hill country to the east'),
                     'niferdu': ('ומאלה נפרדו הגוים בארץ אחר המבול',
                                 'from these the nations branched out over the earth after the Flood'),
                     'achat': ('ויהי כל הארץ שפה אחת ודברים אחדים',
                               'Everyone on earth had the same language and the same words'),
                     'am-ehad': ('ושפה אחת לכלם', 'with one language for all'),
                     'lo-yishmeu': ('אשר לא ישמעו איש שפת רעהו', 'so that they shall not understand one another'),
                 }), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 10 sets out the nations descended from Noah’s sons. Genesis 11 '
                  'begins the story of Babel.'),
        commentary(f'{prefix}-radak-1', h, 1, 'Radak', 'רד"ק', 'Radak',
                   '“From these … branched out”: After their separation, the sons of Japheth chose islands '
                   'for themselves and lived on them; and “islands” are regions divided from one another.',
                   'ours', ref='Radak on Genesis 10:5:1', highlight=['iyei']),
        commentary(f'{prefix}-radak-2', h, 2, 'Radak', 'רד"ק', 'Radak',
                   '“Each with its language”: for they were not all of one language after the Dispersion; and '
                   'so each nation had a language of its own, even though they were all sons of Japheth.',
                   'ours', ref='Radak on Genesis 10:5:2', highlight=['lilshono']),
        commentary(f'{prefix}-radak-30', h, 3, 'Radak', 'רד"ק', 'Radak',
                   '“Their settlements extended”: After the Dispersion they chose for themselves the land '
                   'from Mesha to the hill country of the east…',
                   'ours', ref='Radak on Genesis 10:30:1', highlight=['moshavam', 'har-hakedem']),
        commentary(f'{prefix}-radak-32', h, 4, 'Radak', 'רד"ק', 'Radak',
                   '“And from these the nations branched out over the earth after the Flood”: But they branched '
                   'out only after the Dispersion! Rather, its meaning is: these families of Noah’s sons, who '
                   'were born after the Flood, branched out over the earth when they branched out, and that '
                   'was after the Dispersion.',
                   'ours', ref='Radak on Genesis 10:32:1', highlight=['niferdu']),
        commentary(f'{prefix}-bs-1', h, 5, 'Bekhor Shor', 'בכור שור', 'Bekhor Shor',
                   '“And all the earth was one language and the same words”: for all of them knew seventy '
                   'languages.',
                   'ours', ref='Bekhor Shor, Genesis 11:1:1', highlight=['achat']),
        # Her pointer is «י"א ו' ד"ה ושפה אחת» (11:6); the digitizer linked 11:1.
        commentary(f'{prefix}-bs-6', h, 6, 'Bekhor Shor', 'בכור שור', 'Bekhor Shor',
                   '“And one language”: for all of them know seventy languages and understand one another.',
                   'ours', highlight=['am-ehad']),
        commentary(f'{prefix}-bs-7', h, 7, 'Bekhor Shor', 'בכור שור', 'Bekhor Shor',
                   '“So that they shall not understand one another’s speech”: for each one forgot all the '
                   'languages but one, and what this one knew, that one did not know. But among all of them '
                   'they knew seventy languages. For it does not seem right to me to say, by the plain sense, '
                   'that the seventy languages were created for them only now.',
                   'ours', start='ד"ה אשר לא ישמע', highlight=['lo-yishmeu']),
        commentary(f'{prefix}-rekh-a', h, 8, 'HaRekhasim LeBik’ah', 'בעל רכסים לבקעה', 'HaRekhasim LeBik’ah',
                   'And therefore, if we are given leave to interpret this passage another way, since no '
                   'commandment of the Torah depends on it, only to make known His judgments, how He repays '
                   'the proud for the thing in which they acted presumptuously, “whether a nation or a man '
                   'alike”: it may be that the passages are written out of sequence, the earlier and the later. After '
                   'writing that the many sons of Joktan settled as far as the hill country to the east (see '
                   '10:30), it says, “And all the earth” — of the sons of Joktan — “was one language,” even '
                   'though they were many families. As in (Psalms 45:17), “You will make them princes in all '
                   'the earth”: in all the land of Israel; (Genesis 13) “Is not all the earth before you?”: '
                   'all of this land; (Genesis 41) “And all the earth came to Egypt”: not that they came from '
                   'the far end of the sea and the ends of the earth, but all the land of Canaan and its '
                   'surroundings. So too, “And all the earth” — that land — “was one language,” and so on…',
                   'ours', start='ולכן אם ניתן', stop='\'שפה אחת\' וגו\'...',
                   highlight=['achat', 'moshavam', 'har-hakedem']),
        commentary(f'{prefix}-rekh-b', h, 8, 'HaRekhasim LeBik’ah', 'בעל רכסים לבקעה', 'HaRekhasim LeBik’ah',
                   'And it says that there, in the valley of these sinners, the Lord confounded the language of '
                   'all that land like a kneaded dough, and from there He scattered them; and the rest of the '
                   'nations had no part with them. While the righteous of the generation, and their language, '
                   'will stand firm forever. So it may be interpreted; and let the one who chooses, choose.',
                   'ours', start='ואמר כי שם', highlight=['achat']),
        question(f'{prefix}-q-a3', h, 14, '3. In what is the author of HaRekhasim LeBik’ah close to Radak, and in '
                 'what does he differ from him?'),
        question(f'{prefix}-q-a4', h, 15, '4. Why does the author of HaRekhasim LeBik’ah stress that there are no '
                 'commandments in chapter 11?'),
        commentary(f'{prefix}-hirsch-a', h, 9, 'Hirsch', 'רש"ר הירש', 'R. S. R. Hirsch',
                   '“Branched out”: Only later will the scattering of the nations and the confounding of the '
                   'nations’ languages be told. Even so, it already says here that the nations branched out '
                   'by their lands and their languages. But later it will tell of a special intervention of '
                   'the divine guidance that educates man, and the result of that intervention differs from '
                   'what is stated in this verse. Here a natural phenomenon is told, which was to be expected '
                   'under the new conditions: the peoples spread out in their way and enlarged their borders '
                   'in the land. And as the lands and climates changed, the nations too changed from one '
                   'another. This was expected and necessary, and it came by design; and only of this does '
                   'this verse tell…',
                   'ours', start='ד"ה נפרדו', highlight=['iyei']),
        commentary(f'{prefix}-hirsch-b', h, 10, 'Hirsch', 'רש"ר הירש', 'R. S. R. Hirsch',
                   '“Each with its language”: their particular tongue was a result of the separation, not '
                   'the cause of the separation. When Noah’s sons multiplied they separated by their lands, '
                   'and under the influence of the soil their tongue too took on different shades. It seems '
                   'there is a great difference between “safah,” language, mentioned in the generation of the '
                   'Dispersion, and “lashon,” tongue, mentioned here. Safah means what it plainly means: the '
                   'German language, French, and so on. Whereas “lashon” is the dialect, the manner of the '
                   'tongue, the particular shade of the language…',
                   'ours', start='ד"ה איש ללשונו', stop='הגוון המיוחד של השפה...', highlight=['lilshono']),
        commentary(f'{prefix}-hirsch-c', h, 11, 'Hirsch', 'רש"ר הירש', 'R. S. R. Hirsch',
                   'We have already seen above: natural causes brought it about that people separated into '
                   'groups, and as a result the tongues separated. But the languages were not yet wholly '
                   'foreign. The language was one, but the tongues were different. They spoke one language '
                   'in different dialects.',
                   'ours', start='כבר ראינו', highlight=['achat']),
        question(f'{prefix}-q-a5', h, 16, '5. From Hirsch’s words it follows that there is a difference between '
                 '“hippared” [separating] and “nafotz” [scattering]. What is the difference?',
                 highlight=['iyei', 'niferdu']),
        question(f'{prefix}-q-a1', h, 12, '1. What is the question common to all four of them, which they are '
                 'trying to resolve?', highlight=['niferdu', 'achat']),
        question(f'{prefix}-q-a2', h, 13, '2. How many different views on solving the question were stated above, '
                 'and what are they?'),
        question(f'{prefix}-q-a6', h, 17, 'Can support for one of the views above be brought from what Zephaniah '
                 'prophesies for the end of days:'),
        commentary(f'{prefix}-zeph', h, 18, 'Tanakh', 'צפניה', 'Zephaniah 3:9',
                   '“For then I will turn to the peoples a pure language, so that all of them call on the name '
                   'of the Lord, to serve Him with one accord…”',
                   'ours', ref='Zephaniah 3:9', highlight=['achat']),
    ]})

    P = lambda: primary('Genesis 11:4-6', ['11:4', '11:5', '11:6'], {
        'ir': ('הבה נבנה לנו עיר', 'Come, let us build us a city'),
        'migdal': ('ומגדל וראשו בשמים', 'a tower with its top in the sky'),
        'shem': ('ונעשה לנו שם', 'to make a name for ourselves'),
        'pen-nafutz': ('פן נפוץ על פני כל הארץ', 'else we shall be scattered all over the world'),
        'am-ehad': ('הן עם אחד ושפה אחת לכלם', 'as one people with one language for all'),
        'hahilam': ('וזה החלם לעשות', 'this is how they have begun to act'),
        'lo-yibatzer': ('ועתה לא יבצר מהם כל אשר יזמו לעשות',
                        'nothing that they may propose to do will be out of their reach'),
    })

    # §ג — scan header: ג. ד', הבה נבנה לנו עיר ומגדל וראשו בשמים ונעשה לנו שם פן נפוץ על פני כל הארץ
    # Underlined span recorded in the scan check; her Q3 asks about it.
    rekh = underline(cut(item(h, 26)[0], 'ד"ה ונעשה לנו שם'), 'שכן מנהג הכתוב בכל מקום לפרש האחרון תחילה')
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“A City, and a Tower”'},
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-g-intro', 'Genesis 11:4: what they set out to build, and why.'),
        commentary(f'{prefix}-g-rekh', h, 26, 'HaRekhasim LeBik’ah', 'הרכסים לבקעה', 'HaRekhasim LeBik’ah',
                   '“To make a name for ourselves”: this is the reason for the tower; and “else we shall be '
                   'scattered” is the reason for building the city, <u>for it is the way of Scripture '
                   'everywhere to explain the last first</u>, as will be made clear at Massah and Meribah. '
                   'And therefore the etnachta accent is on the word “shem,” name, for it is joined to the '
                   'making of the tower, which is next to it.',
                   'ours', he=rekh, highlight=['ir', 'migdal', 'shem', 'pen-nafutz']),
        question(f'{prefix}-g-q1', h, 27, '1. What is the difficulty in our verse that he wished to resolve?',
                 highlight=['shem', 'pen-nafutz']),
        question(f'{prefix}-g-q2', h, 28, '2. What does Massah and Meribah have to do with our place?'),
        question(f'{prefix}-g-q3', h, 29, '3. Explain his words marked with a line, and bring an example of “the '
                 'way of Scripture” that he speaks of here, from the Torah or from the Prophets.'),
    ]})

    # §ד — scan header: ד. ו', ועתה לא יבצר מהם כל אשר יזמו לעשות.  Underlined spans in Ibn Kaspi
    # recorded in the scan check; her Q5 asks about them. Q4 is omitted (see babel.md).
    kaspi = underline(underline(cut(item(h, 34)[0], 'דע, כי'), 'אינו כלל לתימה ולגיזום'),
                      'ואמר זה אם על הנמנע אם על האפשר הרחוק אשר הוא לפעמים יתואר כנמנע מצד הסכמת העברי')
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Nothing Will Be Out of Their Reach”'},
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 11:6: the Lord speaks of the builders.'),
        commentary(f'{prefix}-d-rashi', h, 32, 'Rashi', 'רש"י', 'Rashi',
                   '“Lo yibbatzer”: said in astonishment, as a question. “Yibbatzer” is a word of withholding, '
                   'as the Targum renders it; and like it, (Psalms 76:13) “He curbs the princes.”',
                   'ours', ref='Rashi on Genesis 11:6:3', highlight=['lo-yibatzer']),
        commentary(f'{prefix}-d-wessely', h, 33, 'Wessely', 'רנה"ו', 'R. Naftali Herz Wessely',
                   'These are the words of the Lord, who searches the heart and knows what is in store for '
                   'them: that from now on they will do all the great abominations that come into any man’s '
                   'mind; nothing will be withheld from them. And the word “yibbatzer” speaks of lack, as in '
                   '“batzoret,” drought.',
                   'ours', start='אלו הם דברי השם', highlight=['lo-yibatzer']),
        commentary(f'{prefix}-d-kaspi', h, 34, 'Ibn Kaspi', 'אבן כספי', 'Ibn Kaspi, Mitzref LaKesef',
                   'Know that although it is in the nature of speech, and right, that it should take on change '
                   'by the speaker’s hints and allusions, whether by way of wonder, hyperbole or anger, as '
                   'Aristotle and Plato wrote, so that for this reason our Sages said, “from the mouth of '
                   'scribes and not from the mouth of books”; and some of this is necessarily found in the '
                   'Torah, in one hidden place, as I shall write, and all the more so in the Prophets and '
                   'Writings: here, <u>it is not at all for wonder or hyperbole</u>. Rather, the meaning here '
                   'is that the Lord said to Himself, or to His heavenly household: “See these foolish '
                   'humans: for nothing is great and high and lofty and out of reach for all that comes into '
                   'their minds to do!” <u>And He said this whether of the impossible or of the remotely '
                   'possible, which is sometimes described as impossible by the usage of Hebrew</u>, and by '
                   'the art of logic and the books of nature and of divinity. Happy is the believer!',
                   'ours', he=kaspi, highlight=['lo-yibatzer'], effect='glow'),
        question(f'{prefix}-d-q1', h, 35, '1. What is the difficulty in our verse?', highlight=['lo-yibatzer']),
        question(f'{prefix}-d-q2', h, 36, '2. What is the difference between Rashi’s answer and the two other '
                 'answers?'),
        question(f'{prefix}-d-q3', h, 37, '3. What is the difference between Ibn Kaspi’s interpretation and '
                 'Wessely’s?'),
        question(f'{prefix}-d-q5', h, 39, '5. Explain his words marked with a line.'),
        question(f'{prefix}-d-q6', h, 40, '6. Toward whom is “Happy is the believer” said here, and in what does '
                 'he believe?', highlight=['lo-yibatzer']),
    ]})
    return secs
