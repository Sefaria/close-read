from bereshit_lib import *  # noqa: F401,F403
# Theme 5 — from Cain's line to the Flood (Gen 4:17–6:8): leaves 1950, 1969, 1971.
# Paper trail: research/parshiyot/bereshit-leaves/flood.md.


# ─── 1950 ───────────────────────────────────────────────────────────────────

def _gen_4_17_22():
    return primary('Genesis 4:17-22', ['4:17', '4:18', '4:19', '4:20', '4:21', '4:22'], {
        'boneh-ir': ('ויהי בנה עיר', 'And he then founded a city'),
        'named-enoch': ('ויקרא שם העיר כשם בנו חנוך', 'named the city after his son Enoch'),
        'ohel-mikneh': ('אבי ישב אהל ומקנה', 'the ancestor of those who dwell in tents and amidst herds'),
        'kinor': ('תפש כנור ועוגב', 'all who play the lyre and the pipe'),
        'lotesh': ('לטש כל חרש נחשת וברזל', 'who forged all implements of copper and iron'),
    })


def _gen_4_23_24():
    return primary('Genesis 4:23-24', ['4:23', '4:24'], {
        'lamech-said': ('ויאמר למך לנשיו', 'And Lamech said to his wives'),
        'shmaan': ('שמען קולי', 'hear my voice'),
        'imrati': ('האזנה אמרתי', 'give ear to my speech'),
        'ish': ('כי איש הרגתי לפצעי', 'I have slain a rival for wounding me'),
        'yeled': ('וילד לחברתי', 'And a lad for bruising me'),
        'shivatayim': ('כי שבעתים יקם קין', 'If Cain is avenged sevenfold'),
        'shivim': ('ולמך שבעים ושבעה', 'Then Lamech seventy-sevenfold'),
    })


def _gen_4_17_24():
    return primary('Genesis 4:17-24', ['4:17', '4:18', '4:19', '4:20', '4:21', '4:22', '4:23', '4:24'], {
        'boneh-ir': ('ויהי בנה עיר', 'And he then founded a city'),
        'ohel-mikneh': ('אבי ישב אהל ומקנה', 'the ancestor of those who dwell in tents and amidst herds'),
        'kinor': ('תפש כנור ועוגב', 'all who play the lyre and the pipe'),
        'lotesh': ('לטש כל חרש נחשת וברזל', 'who forged all implements of copper and iron'),
        'lamech-said': ('ויאמר למך לנשיו', 'And Lamech said to his wives'),
        'shivim': ('ולמך שבעים ושבעה', 'Then Lamech seventy-sevenfold'),
    })


def leaf_1950(prefix='fl-1950'):
    """Gilayon תש"י (161438): §א, §ב, §ג. Rashi on 4:23–24 is rendered once, in §ב, with her §ב
    start/stop points; §א's question on his two interpretations follows it there."""
    h = harvest('flood', '1950')
    secs = []

    # §א — scan header: א. שאלות ודיוקים ברש"י:
    secs.append({'id': prefix, 'title': {'en': '1950 · The Sons of Cain'},
                 'primaryText': _gen_4_17_22(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 4:17–22: the line of Cain, from Enoch to Tubal-cain.'),
        commentary(f'{prefix}-rashi-17', h, 1, 'Rashi', 'רש"י', 'Rashi',
                   '“And he was building a city”: Cain was building a city, and he called the name of the '
                   'city as a memorial of his son, Enoch.',
                   'ours', ref='Rashi on Genesis 4:17:1', highlight=['boneh-ir', 'named-enoch']),
        question(f'{prefix}-q-a0', h, 2, 'What is difficult for him?', highlight=['boneh-ir']),
        commentary(f'{prefix}-rashi-20', h, 3, 'Rashi', 'רש"י', 'Rashi',
                   '“The ancestor of those who dwell in tents and amidst herds”: He was the first of the '
                   'herders of cattle in the wildernesses, dwelling in tents, a month here and a month '
                   'there, for the sake of pasture for his flock; and when the pasture ran out in one place, '
                   'he would go and pitch his tent in another place. And a midrash aggadah: building houses '
                   'for idol worship, as you say (Ezekiel 8), “the image of jealousy, which provokes '
                   'jealousy” (ha-mekneh). And likewise his brother, “who plays the lyre and the pipe”: to '
                   'make music for idol worship.',
                   'ours', ref='Rashi on Genesis 4:20:1', highlight=['ohel-mikneh', 'kinor']),
        question(f'{prefix}-q-a1', h, 4, 'a. What is difficult for him?', highlight=['ohel-mikneh']),
        question(f'{prefix}-q-a2', h, 5, 'b. Why did he change the word “tent” (ohel) in the verse to the '
                 'plural, “tents”?', highlight=['ohel-mikneh']),
        question(f'{prefix}-q-a3', h, 6, 'c. Why was he not content with his first interpretation, and added '
                 'to it a midrash aggadah as well?'),
    ]})

    # §ב — scan header: ב. כ"ג - כ"ד. The title comes from her framing sentence [16]
    # («…אם הם דברי התנצלות של למך או דברי התפארות»), which has no card of its own.
    secs.append({'id': f'{prefix}-song', 'titleCard': False, 'title': {'en': 'Apology or Boast?'},
                 'primaryText': _gen_4_23_24(), 'steps': [
        narration(f'{prefix}-b-intro', 'Lamech speaks to his wives, Adah and Zillah.'),
        question(f'{prefix}-q-b0', h, 17, 'Study the words of these commentators and sort them into groups:'),
        commentary(f'{prefix}-saadia', h, 18, 'Saadia Gaon', 'רב סעדיה גאון', 'R. Saadia Gaon, Sefer ha-Galui',
                   'The intent of this is one of two things: Lamech’s repentance of his sins, so that we '
                   'may turn back from our sins. “If we interpret ‘for I have slain a man’ absolutely (= in '
                   'the affirmative), we say: if the one who kills Cain is killed, great vengeance is taken '
                   'from him — even though Cain himself had killed; then Lamech, who killed a man and a lad, '
                   'all the more will they take vengeance from him on their account, more and more, and '
                   'especially since the lad had no sin at all… And if we translate ‘for I have slain a '
                   'man’ in the negative, then we say: if Cain, who killed a person, will be greatly avenged '
                   'on his murderer because he repented, then Lamech, who killed neither a man nor a lad, '
                   'all the more will he be avenged, more and more, on whoever murders him.',
                   'ours', start='הכוונה בזה', highlight=['ish', 'yeled', 'shivatayim', 'shivim']),
        # Her Rashi pointer 1: 4:23 ד"ה שמען קולי (both comments) and 4:24 from ד"ה כי שבעתים
        # through «…דרש ר' תנחומא». §ב's digitization lacks 4:24:1, so that card cites §א's [10].
        commentary(f'{prefix}-rashi-23a', h, 19, 'Rashi', 'רש"י', 'Rashi',
                   '“Hear my voice”: For his wives were separating from him, refusing marital relations, '
                   'because he had killed Cain and Tubal-cain his son. For Lamech was blind, and Tubal-cain '
                   'would lead him; and he saw Cain, who looked to him like an animal, and told his father '
                   'to draw the bow, and he killed him. And when he learned that it was Cain his '
                   'grandfather, he struck his hands together and clapped his son between them, and killed '
                   'him. And his wives were separating from him, and he was appeasing them.',
                   'ours', ref='Rashi on Genesis 4:23:1', highlight=['shmaan']),
        commentary(f'{prefix}-rashi-23b', h, 20, 'Rashi', 'רש"י', 'Rashi',
                   '“Hear my voice”: to obey me in marital relations. And the man whom I killed — was he '
                   'killed “for my wounding”? Did I wound him deliberately, that the wound should be called '
                   'by my name? And the lad whom I killed — was he killed “for my bruising,” that is, by my '
                   'blow? [This is read] as a question: am I not unwitting and not deliberate? This is not my '
                   'wound, and this is not my bruise.',
                   'ours', ref='Rashi on Genesis 4:23:2', highlight=['ish', 'yeled']),
        commentary(f'{prefix}-rashi-24a', h, 10, 'Rashi', 'רש"י', 'Rashi',
                   '“If Cain is avenged sevenfold”: Cain, who killed deliberately, had his punishment '
                   'suspended for seven generations; I, who killed unwittingly, how much more should many '
                   'sevens be suspended for me.',
                   'ours', ref='Rashi on Genesis 4:24:1', highlight=['shivatayim']),
        commentary(f'{prefix}-rashi-24b', h, 21, 'Rashi', 'רש"י', 'Rashi',
                   '“Seventy-seven”: a term for many sevens he took for himself. So R. Tanchuma expounded.',
                   'ours', ref='Rashi on Genesis 4:24:2', highlight=['shivim']),
        # Her Rashi pointer 2: ד"ה כי שבעתים «החל מן ומדרש בראשית רבה».
        commentary(f'{prefix}-rashi-24c', h, 22, 'Rashi', 'רש"י', 'Rashi',
                   'And the midrash of Bereshit Rabbah: Lamech killed no one, and his wives were separating '
                   'from him once they had fulfilled [the duty of] being fruitful and multiplying, because a '
                   'decree had been issued to destroy the seed of Cain after seven generations. They said: '
                   'Why should we give birth for destruction? Tomorrow the Flood comes and sweeps everything '
                   'away! And he says to them: “Have I killed a man for my wounding?” Did I kill Abel, who was '
                   'a man in stature and a lad in years, that my seed should be destroyed for that sin? And '
                   'if Cain, who killed, had [punishment] suspended for seven generations, I, who did not '
                   'kill, how much more should many sevens be suspended for me! And this is a foolish '
                   'a fortiori argument: if so, the Holy One, blessed be He, would not collect His debt and '
                   'fulfill His word.',
                   'ours', ref='Rashi on Genesis 4:24:2', start='ומדרש בראשית רבה',
                   highlight=['ish', 'shivatayim', 'shivim']),
        question(f'{prefix}-q-a4', h, 12, 'a. In what are [Rashi’s] two interpretations alike, and in what do they '
                 'differ from each other in principle?', highlight=['ish']),
        commentary(f'{prefix}-ibn-ezra', h, 24, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   'And the meaning is as our Sages said: that Adah and Zillah held back, for they were '
                   'afraid to bear children, lest they be the seventh [generation] from Cain and be killed '
                   'or die. And therefore Lamech said to his wives: I am in truth the seventh, and if a man '
                   'who is grown wounds me, or a lad makes a bruise on me, then I will kill him. And the word '
                   '“I have slain” (haragti) stands in place of “I will slay”; and like it: “I have given the '
                   'price of the field,” “which I took from the hand of the Amorite,” and many like them.',
                   'ours', ref='Ibn Ezra on Genesis 4:23:1', start='והטעם כאשר אמרו חכמינו',
                   highlight=['ish', 'yeled']),
        commentary(f'{prefix}-ramban-1', h, 26, 'Ramban', 'רמב"ן', 'Ramban',
                   'But the matter of Lamech with his wives, Scripture did not mention explicitly. We may '
                   'also say that they were afraid of punishment, lest Lamech be killed for the sin of his '
                   'father; for God did not say to Cain “I have pardoned you,” only that he would not be '
                   'killed, but He would collect His debt from his descendants, and they did not know when. '
                   'And so it came to pass. And Lamech comforted them, saying that God would have mercy on '
                   'him as He had mercy on Cain, for his hands were cleaner than his, and he too would pray '
                   'before Him, and He would hear his prayer.',
                   'ours', ref='Ramban on Genesis 4:23:1', start='אבל ענין למך', stop='ישמע תפלתו',
                   highlight=['lamech-said', 'ish']),
        commentary(f'{prefix}-ramban-2', h, 27, 'Ramban', 'רמב"ן', 'Ramban',
                   'But what seems right in my eyes is that Lamech was a very wise man in every skilled '
                   'craft. He taught his firstborn son the matter of herding, according to the nature of the '
                   'animals; and taught the second the wisdom of music; and taught the third to forge and make '
                   'swords and spears and lances and all the weapons of war. And his wives were afraid that he '
                   'would be punished, for he had brought the sword and murder into the world; here he was, '
                   'grasping in his hand the deeds of his fathers, for he was the son of the first murderer, '
                   'and he had created a destroyer to wreak havoc. And he said to them: I have not killed a '
                   'man with wounds, nor a lad with bruises, as Cain did, and God will not punish me, but will '
                   'guard me from being killed more than him. And he mentioned this to say that it is not by '
                   'sword and spear that a person can kill with wounds and bruises, putting [someone] to a '
                   'death worse than the sword; the sword does not cause murder, and the one who makes it '
                   'bears no sin.',
                   'ours', ref='Ramban on Genesis 4:23:1', start='אבל הנראה בעיני',
                   highlight=['ish', 'yeled']),
        commentary(f'{prefix}-ralbag', h, 28, 'Ralbag', 'רלב"ג', 'Ralbag',
                   '… What Lamech said to his wives is to show how little he feared the Lord’s punishment, '
                   'and that he did not strive with all his strength to return to the Lord, so that the '
                   'Lord’s burning anger would turn from him. For without doubt, had he done so, he would have '
                   'escaped the evil decreed to come upon him, for the Lord is gracious and relents of evil. '
                   'And the Torah has already testified, in a general statement, that in all the generation of '
                   'the Flood they were corrupting their way, and no righteous man was found then except '
                   'Noah…',
                   'ours', ref='Ralbag on Torah, Genesis 4:1:4', highlight=['lamech-said']),
        commentary(f'{prefix}-sforno-23', h, 29, 'Sforno', 'ספורנו', 'Sforno',
                   '“Hear my voice”: crying out in grief. “My speech”: that I may tell my sorrow. “I have '
                   'slain a man for my wounding”: I have truly wounded myself, for the one slain was my '
                   'father. “And a lad for my bruising”: the bruise was truly in myself, in that the one '
                   'slain was my son.',
                   'ours', ref='Sforno on Genesis 4:23:1-3', highlight=['shmaan', 'imrati', 'ish', 'yeled']),
        commentary(f'{prefix}-sforno-24', h, 30, 'Sforno', 'ספורנו', 'Sforno',
                   '“And Lamech seventy-sevenfold”: that the sorrow I shall suffer over this all my days will '
                   'be far greater than the sorrow Cain suffered at being a wanderer and a fugitive. And this '
                   'is because Lamech grieved all his days that he had killed Cain his grandfather and '
                   'Tubal-cain his son, as has come down in the tradition.',
                   'ours', ref='Sforno on Genesis 4:24:1', highlight=['shivim']),
        commentary(f'{prefix}-malbim', h, 31, 'Malbim', 'מלבי"ם', 'Malbim',
                   '“Hear my voice”: and do not defy my word. For a man [came] and dealt me a wound, and I '
                   'killed him; and at the time of the killing he gave me a bruise — which is lighter than a '
                   'wound — and I killed his child as well. And there was no one to rise against me and demand '
                   'their blood from my hand, for there is no judgment against me in the land, for my arm is '
                   'raised high. And should you say that I will be punished by the laws of Heaven, then I '
                   'answer: if Cain, who was the first murderer, nevertheless the Lord said that whoever kills '
                   'him will be avenged sevenfold — how much more Lamech, who is mightier than Cain and rules '
                   'with great dominion: whoever kills him will be avenged seventy-seven times, for his sons '
                   'and servants will take his vengeance… And with this [Scripture] tells how the sons of '
                   'Cain went out to an evil way and to boasting of murder, until they terrified even their '
                   'wives with killing and slaughter…',
                   'ours', ref='Malbim on Genesis 4:23:1-24:1', highlight=['shmaan', 'ish', 'shivim'],
                   effect='glow'),
        question(f'{prefix}-q-b1', h, 32, '1. After you have divided all the commentators above into groups, '
                 'explain which view seems to you to fit better the connection between our passage and '
                 'what comes before it and after it!'),
        question(f'{prefix}-q-b2', h, 33, '2. What is the meaning of “ki” in verse 23 (“ki ish haragti”) '
                 'according to each of the views above?', highlight=['ish']),
    ]})

    # §ג — no separate header in the scan: «ג. בכונת הספור כולו אומר המלבי"ם: …» runs on.
    secs.append({'id': f'{prefix}-story', 'titleCard': False, 'title': {'en': 'The Story as a Whole'},
                 'primaryText': _gen_4_17_24(), 'steps': [
        narration(f'{prefix}-g-intro', 'Genesis 4:17–24: a city, herds and tents, the lyre and the pipe, '
                  'copper and iron, and Lamech’s song.'),
        commentary(f'{prefix}-malbim-story', h, 35, 'Malbim', 'מלבי"ם', 'Malbim',
                   'On the intent of the whole story, Malbim says: Although Cain and his sons founded a city '
                   'and a civic community, and instituted laws and crafts for the conduct of society — '
                   'nevertheless, if understanding does not lift up its voice, and if people are not upright '
                   'and lovers of justice by nature, the laws will be of no avail; for if a tyrant arises, he '
                   'will laugh at every statute and law, and they will rob justice and righteousness…',
                   'ours', ref='Malbim on Genesis 4:23',
                   highlight=['boneh-ir', 'ohel-mikneh', 'kinor', 'lotesh']),
        commentary(f'{prefix}-cassuto', h, 36, 'Cassuto', 'קאסוטו', 'Cassuto',
                   'Compare with his words those of Cassuto, From Adam to Noah, p. 130: After (the Torah) has '
                   'mentioned the innovations that Cain and his sons introduced into human civilization, it '
                   'brings the song of Lamech, which shows that alongside material progress no moral progress '
                   'was felt. Violence reigned, and in deeds of violence those generations took pride; '
                   'precisely the base qualities, hateful in the eyes of the Lord, were counted a virtue in '
                   'the eyes of human beings. In such a state it was impossible that the Judge of all the '
                   'earth would not do justice. All the achievements of material civilization are worth '
                   'nothing without good qualities in the ways of morality…',
                   'ours', highlight=['lamech-said', 'shivim']),
        question(f'{prefix}-q-g1', h, 37, '1. What is the fine difference between these two views, which are '
                 'so similar to each other?'),
        question(f'{prefix}-q-g2', h, 38, '2. Where in the Torah shall we meet the idea in Cassuto’s words '
                 'a second time?'),
    ]})
    return secs


# ─── 1969 ───────────────────────────────────────────────────────────────────

def _gen_4_25_26_6_5_8():
    return primary('Genesis 4:25-26, 6:5-8', ['4:25', '4:26', '6:5', '6:6', '6:7', '6:8'], {
        'shet': ('ותקרא את שמו שת', 'named him Seth'),
        'tachat-hevel': ('זרע אחר תחת הבל', 'another offspring in place of Abel'),
        'enosh': ('ויקרא את שמו אנוש', 'he named him Enosh'),
        'huchal': ('אז הוחל לקרא בשם יהוה', 'It was then that the Lord began to be invoked by name'),
        'raah': ('וירא יהוה כי רבה רעת האדם בארץ', 'the Lord saw how great was human wickedness on earth'),
        'vayinachem': ('וינחם יהוה כי עשה את האדם בארץ', 'And the Lord regretted having made humankind on earth'),
        'emcheh': ('אמחה את האדם', 'I will blot out from the earth humankind'),
        'noach-chen': ('ונח מצא חן בעיני יהוה', 'But Noah found favor with the Lord'),
    })


def _gen_5_23_24():
    return primary('Genesis 5:23-24', ['5:23', '5:24'], {
        'days': ('ויהי כל ימי חנוך חמש וששים שנה ושלש מאות שנה', 'All the days of Enoch came to 365 years'),
        'walked': ('ויתהלך חנוך את האלהים', 'Enoch walked with God'),
        'einennu': ('ואיננו', 'then he was no more'),
        'lakach': ('כי לקח אתו אלהים', 'for God took him'),
    })


def leaf_1969(prefix='fl-1969'):
    """Gilayon תשכ"ט (160469): §א, §ג, §ד. §ב is out (pack §7). The opening cross-reference [0]
    isn't published. No image (decided)."""
    h = harvest('flood', '1969')
    P = _gen_4_25_26_6_5_8
    secs = []

    # §א — scan header: א. שאלות מבנה:
    secs.append({'id': prefix, 'title': {'en': '1969 · Where the Story Ends'}, 'primaryText': P(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 4:25–26, the last verses of chapter 4; and 6:5–8, the last '
                  'verses of the parasha.'),
        commentary(f'{prefix}-cassuto-div', h, 2, 'Cassuto', 'קאסוטו', 'Cassuto',
                   'Cassuto (in his book From Adam to Noah) divides the parasha of “Cain and Abel” (4:1–4:26) '
                   'into six paragraphs, and the following parasha (5:1–6:8), “The Book of the Generations of '
                   'Adam,” into three “matters”: [5:1–32; 6:1–4; 6:5–8]',
                   'ours', highlight=['huchal', 'noach-chen']),
        commentary(f'{prefix}-cassuto-end', h, 6, 'Cassuto', 'קאסוטו', 'Cassuto',
                   'On the last paragraph of the parasha of “Cain and Abel” he remarks (fourth edition, '
                   'p. 127): A great rule in the Torah requires that at the close of a story there come '
                   'something like its opening… And another rule requires that the stories end on a good '
                   'note.',
                   'ours', highlight=['shet', 'tachat-hevel', 'enosh', 'huchal']),
        question(f'{prefix}-q-a1', h, 7, '1. Explain in what way the endings of the two parashiyot, the '
                 'parasha of “Cain and Abel” and the parasha of “The Book of the Generations of Adam,” have '
                 '“something like the opening.”', highlight=['huchal', 'noach-chen']),
        question(f'{prefix}-q-a2', h, 8, '2. What is the ending “on a good note” in each of the two '
                 'parashiyot above?'),
        question(f'{prefix}-q-a3', h, 9, '3. In his view there is also a parallel between the ending of the '
                 'parasha of Cain and Abel and the ending of the parasha that comes after it. What is the '
                 'parallel?'),
        question(f'{prefix}-q-a4', h, 10, '4. Cassuto disagrees with most Bible scholars, who hold — against '
                 'those who divided the Pentateuch into sedrot — that verses 6:5–8 belong to the parasha of '
                 'the Flood and not to the parasha of “The Book of the Generations of Adam.” What could the '
                 'reasons be for the division above (Cassuto’s)?',
                 highlight=['raah', 'vayinachem', 'emcheh', 'noach-chen']),
    ]})

    # §ג — scan header: ג. ד' כ"ו אז הוחל לקרא בשם ה'.
    secs.append({'id': f'{prefix}-name', 'titleCard': False, 'title': {'en': 'Calling on the Name'},
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-g-intro', 'Seth’s son Enosh, and the end of chapter 4.'),
        commentary(f'{prefix}-br', h, 16, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“Then it was begun (huchal) to call on the name of the Lord”: R. Simon said: In three '
                   'places this expression is used, a term of rebellion: (Genesis 4:26) “Then it was begun to '
                   'call on the name of the Lord”; (6:1) “And it came to pass, when man began”; (10:8) “He '
                   'began to be a mighty one in the earth.” R. Acha said: You have made yourselves into idols '
                   'and called [them] by your own name; I too will call the waters of the sea by My name, and '
                   'wipe those people out of the world.',
                   'ours', ref='Bereshit Rabbah 23:7', highlight=['huchal']),
        question(f'{prefix}-q-g1', h, 23, '1. How does the midrash arrive at its interpretation of “huchal” '
                 'as a term of rebellion?', highlight=['huchal']),
        commentary(f'{prefix}-rashi', h, 17, 'Rashi', 'רש"י', 'Rashi',
                   '“Then it was begun”: a term of profaneness (chullin): calling the names of men and the '
                   'names of idols by the name of the Holy One, blessed be He, making them idols and calling '
                   'them deities.',
                   'ours', ref='Rashi on Genesis 4:26:1', highlight=['huchal']),
        question(f'{prefix}-q-g2', h, 24, '2. In the view of Shadal (and also Berliner, in the scholarly '
                 'edition of Rashi), the first two words, “a term of profaneness,” are not Rashi’s words but '
                 'the addition of some student. How, on this view, does Rashi interpret our verse, without the '
                 'grammatical explanation above?', highlight=['huchal']),
        commentary(f'{prefix}-ibn-ezra', h, 18, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“It was begun” (huchal): it is from the root of “beginning” (techillah), and the meaning '
                   'is that they began to pray. Had it been from “profaning” (chillul), the Name would have '
                   'been joined to the word.',
                   'ours', ref='Ibn Ezra on Genesis 4:26:1', highlight=['huchal']),
        commentary(f'{prefix}-bekhor-shor', h, 19, 'Bekhor Shor', 'ר\' יוסף בכור שור', 'R. Yosef Bekhor Shor',
                   '“Then it was begun to call on the name of the Lord”: It tells you the importance of Seth, '
                   'who called his son “Enosh,” that is, “man,” as in (Psalms 8) “What is man (enosh) that '
                   'You are mindful of him” — even though in his generation they began to call their own '
                   'names by the name of the Holy One, blessed be He, for they would join the name of Heaven '
                   'to their names, as in “Mehujael,” “Mahalalel.”',
                   'ours', ref='Bekhor Shor, Genesis 4:26:1', highlight=['enosh', 'huchal']),
        commentary(f'{prefix}-wessely', h, 20, 'Wessely', 'ר\' נפתלי הירש ויזל', 'R. Naftali Hirz Wessely, Imrei Shefer',
                   '…And in my opinion, “to call on the name of the Lord” is as in (Zephaniah 3:9) “For then '
                   'I will turn to the peoples a pure language, that they may all call on the name of the '
                   'Lord, to serve Him with one accord,” and likewise “And he built there an altar to the Lord '
                   'and called there on the name of the Lord, the everlasting God”: all of them concern '
                   'proclaiming His divinity and His exaltedness, blessed be He, to teach the wayward the way '
                   'of the Lord. And Scripture made known that in the days of Enosh many people, and of the '
                   'sons of Cain, had already strayed from the way of the Lord; and the pious of the '
                   'generations, such as Adam, Seth, Enosh — and perhaps individuals joined them — taught the '
                   'name of the Lord and His ways to the people of the world. And so the matter rolled on from '
                   'generation to generation: there were exceptional individuals teaching and showing the way '
                   'of the Lord, but it availed nothing. And the Torah made known to us that we should not '
                   'think that the wickedness of man became great on the earth because they had no teacher '
                   'and righteous guide — and that this would be an everlasting disgrace to the righteous of '
                   'those generations, who knew the work of the Lord, that it is awesome, and did not make '
                   'known to them the way of the Lord; rather, they all called on the name of the Lord, and it '
                   'availed nothing. But before Enosh was born there were only a few in the world, and they '
                   'had not yet corrupted their way; and it seems this was before “they took wives for '
                   'themselves from all whom they chose,” and the holy ones did not need to call on the name '
                   'of the Lord to humankind. And Scripture taught us that in the days of Enosh people had '
                   'already strayed from the way of truth.',
                   'ours', start='...ולדעתי', highlight=['huchal', 'raah']),
        commentary(f'{prefix}-shadal', h, 21, 'Shadal', 'שד"ל', 'Shadal, HaMishtadel',
                   '“To call on the name of the Lord”: its sense, as in most places, is speaking to the '
                   'people, to proclaim and make known the attributes of God and what He desires… And the '
                   'intent is that then people began to err in matters of the knowledge of God and of the '
                   'good ways before Him, and then the wise and the upright began to proclaim the truth in the '
                   'assembly of the people. And this fits also with what the Sages said, that in the days of '
                   'Enosh idol worship began.',
                   'ours', ref='Shadal on Genesis 4:26:1', highlight=['huchal']),
        commentary(f'{prefix}-hirsch', h, 22, 'Hirsch', 'ר\' שמשון רפאל הירש', 'R. Samson Raphael Hirsch',
                   '…(after citing Rashi’s interpretation) But this interpretation too is difficult, and the '
                   'interpretation I heard from my master and teacher, the sage Bernays, of blessed memory, is '
                   'without doubt the correct one. Calling on the name of the Lord was a merit in the days of '
                   'Abraham, a sign of the generation’s return. It heralded the beginning of repair, after the '
                   'name of the Lord had been forgotten from people’s mouths. But in the generation of Enosh '
                   'it heralded the beginning of corruption. In this generation the need was felt for the '
                   'first time: to call on the name of the Lord. Until then it had been superfluous — as it is '
                   'destined to be superfluous (Jeremiah 31:33): “And they shall teach no more every man his '
                   'neighbor and every man his brother, saying: ‘Know the Lord,’ for they shall all know Me, '
                   'from the least of them to the greatest.”',
                   'ours', start='...(אחרי הביאו', highlight=['huchal'], effect='glow'),
        question(f'{prefix}-q-g3', h, 25, '3. Which of the commentators we have brought follows in the '
                 'footsteps of R. Acha!'),
        question(f'{prefix}-q-g4', h, 26, '4. The last three commentators we have brought all agree with the '
                 'view of the Sages that idol worship began in the generation of Enosh. Why do they not '
                 'follow Rashi’s way?'),
        question(f'{prefix}-q-g5', h, 27, '5. Which of the commentators above could rely on Exodus 34:5?',
                 highlight=['huchal']),
        question(f'{prefix}-q-g6', h, 28, '6. Most commentators oppose Ibn Ezra’s interpretation (except '
                 'Rashbam and Ibn Caspi, who follow in his footsteps). What is the weakness of his '
                 'interpretation?'),
    ]})

    # §ד — scan header: ד. ויתהלך חנוך את האלקים ואיננו כי לקח אותו אלוקים.
    secs.append({'id': f'{prefix}-enoch', 'titleCard': False, 'title': {'en': 'Enoch Walked with God'},
                 'primaryText': _gen_5_23_24(), 'steps': [
        narration(f'{prefix}-d-intro', 'Genesis 5:23–24.'),
        commentary(f'{prefix}-br-25', h, 31, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Aibo: Enoch was a flatterer (chanef), sometimes righteous, sometimes wicked. The Holy '
                   'One, blessed be He, said: While he is righteous, I will remove him. R. Aibo said: He '
                   'judged him on Rosh Hashanah, at the hour when He judges the whole world. The sectarians '
                   '(minim) asked R. Abbahu; they said to him: “We do not find death for Enoch.” He said to '
                   'them: “Why?” They said to him: “‘Taking’ is said here, and ‘taking’ is said of Elijah.”* '
                   'He said to them: “If it is ‘taking’ you expound — ‘taking’ is said here, and ‘taking’ is '
                   'said in Ezekiel (24:16): ‘Behold, I take from you the delight of your eyes with a '
                   'plague.’” R. Tanchuma said: “R. Abbahu answered them well.”',
                   'ours', ref='Bereshit Rabbah 25:1', highlight=['lakach']),
        commentary(f'{prefix}-kings', h, 37, 'II Kings', 'מלכים ב ב, ג', 'II Kings 2:3',
                   '“For today the Lord is taking your master from over your head.”',
                   'ours', ref='II Kings 2:3', highlight=['lakach']),
        commentary(f'{prefix}-rashi-24a', h, 32, 'Rashi', 'רש"י', 'Rashi',
                   '“And Enoch walked”: He was righteous, but light-minded, apt to turn back and become '
                   'wicked; therefore the Holy One, blessed be He, hastened and removed him, and caused him to '
                   'die before his time. And this is why Scripture changed [its language] at his death, '
                   'writing “and he was not”: he was not in the world to fill out his years.',
                   'ours', ref='Rashi on Genesis 5:24', start='ד"ה ויתהלך חנוך',
                   highlight=['walked', 'einennu']),
        # Sefaria tags [33] Bereshit Rabbah 25:1; the scan (a ditto mark under רש"י) and the text are
        # Rashi on 5:24, ד"ה כי לקח אותו.
        commentary(f'{prefix}-rashi-24b', h, 33, 'Rashi', 'רש"י', 'Rashi',
                   '“For God took him”: before his time, as in (Ezekiel 24) “Behold, I take from you the '
                   'delight of your eyes with a plague.”',
                   'ours', ref='Rashi on Genesis 5:24', highlight=['lakach']),
        question(f'{prefix}-q-d1', h, 34, '1. Why did R. Tanchuma see fit to praise R. Aibo for his answer?'),
        question(f'{prefix}-q-d2', h, 35, '2. Why did Rashi see fit to bring the words of the midrash about his '
                 'being a righteous man liable to turn back and become wicked — does not Scripture praise '
                 'Noah too in this same language? And does not Rashi himself say that he brings a midrash '
                 'only where it is needed to settle the verses, each word in its place (and see in our '
                 'parasha Rashi on 3:8, “Va-yishme’u”)? And what is the linguistic and substantive difficulty '
                 'that needs settling here?', highlight=['walked']),
        question(f'{prefix}-q-d3', h, 36, '3. Where do we find in Scripture this meaning of “ve-einennu” '
                 '(“and he was not”)?', highlight=['einennu']),
    ]})
    return secs


# ─── 1971 ───────────────────────────────────────────────────────────────────

def _gen_6_1_4():
    return primary('Genesis 6:1-4', ['6:1', '6:2', '6:3', '6:4'], {
        'bnei-elohim': ('ויראו בני האלהים את בנות האדם כי טבת הנה',
                        'the divine beings saw how pleasing the human women were'),
        'vayikchu': ('ויקחו להם נשים מכל אשר בחרו', 'took wives from among those who delighted them'),
        'lo-yadon': ('לא ידון רוחי באדם לעלם', 'My breath shall not abide in humankind forever'),
        'besh-gam': ('בשגם הוא בשר', 'since it too is flesh'),
        'shana-120': ('והיו ימיו מאה ועשרים שנה', 'let the days allowed them be one hundred and twenty years'),
        'nefilim': ('הנפלים היו בארץ', 'the Nephilim appeared on earth'),
        'gibborim': ('המה הגברים אשר מעולם אנשי השם', 'Such were the heroes of old, the men of renown'),
    })


def leaf_1971(prefix='fl-1971'):
    """Gilayon תשל"א (162069), her last Bereshit sheet: §א, §ב, §ג."""
    h = harvest('flood', '1971')
    P = _gen_6_1_4
    secs = []

    # §א — scan header: א. ויראו בני האלוהים את בנות האדם
    secs.append({'id': prefix, 'title': {'en': '1971 · The Sons of God'}, 'primaryText': P(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 6:1–4: the “sons of God” and the daughters of men.'),
        commentary(f'{prefix}-br', h, 2, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Shimon ben Yochai called them “sons of judges” (benei dayyanaya). R. Shimon ben Yochai '
                   'cursed anyone who called them “sons of God” (benei elahaya). R. Shimon ben Yochai taught: '
                   'Any breach that does not come from the great ones is no breach. “The priests have stolen '
                   'the god — who will swear by it (= who will swear by it, by the idol), or who will offer” '
                   '(= or who will bring it an offering).',
                   'ours', ref='Bereshit Rabbah 26:5', highlight=['bnei-elohim']),
        question(f'{prefix}-q-a1', h, 3, '1. Where do we find in the Torah “elohim” in the sense in which '
                 'R. Shimon ben Yochai interprets the word “elohim” in our verse?', highlight=['bnei-elohim']),
        question(f'{prefix}-q-a2', h, 4, '2. Why does R. Shimon ben Yochai curse those who interpret our verse '
                 'otherwise than he does?'),
        question(f'{prefix}-q-a3', h, 5, '3. E. E. Urbach, in his book The Sages: Their Concepts and Beliefs, '
                 'p. 147, writes: “The Aramaic translations took account of R. Shimon ben Yochai’s curse.” '
                 'Prove his words.'),
        question(f'{prefix}-q-a4', h, 6, '4. Explain the idea contained in R. Shimon ben Yochai’s words, “Any '
                 'breach that does not…”'),
        question(f'{prefix}-q-a5', h, 7, '5. Copy out the Aramaic proverb brought at the end of the midrash, '
                 'and mark it with punctuation.'),
    ]})

    # §ב — scan header: ב. ויראו בני האלוהים את בנות האדם כי טובות הנה - ויקחו להם נשים מכל אשר בחרו
    secs.append({'id': f'{prefix}-who', 'titleCard': False, 'title': {'en': 'Who Are the “Sons of God”?'},
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 6:2.'),
        commentary(f'{prefix}-sifrei', h, 10, 'Sifrei', 'ספרי', 'Sifrei',
                   '“And the sons of God saw” — what were the judges doing? They would seize women from the '
                   'marketplace and violate them. If the sons of the judges did so, how much more the common '
                   'people.',
                   'ours', start='"ויראו בני האלוהים"',
                   highlight=['bnei-elohim', 'vayikchu']),
        commentary(f'{prefix}-radak-1', h, 11, 'Radak', 'רד"ק', 'Radak',
                   '“And the sons of God saw”: the sons of the judges and the great ones and the leaders of '
                   'the states, for they are called “elohim,” as in (Exodus 22) “You shall not curse elohim” '
                   '[the judges], and the like…',
                   'ours', ref='Radak on Genesis 6:2:1', highlight=['bnei-elohim']),
        commentary(f'{prefix}-radak-2', h, 12, 'Radak', 'רד"ק', 'Radak',
                   '“The daughters of men”: the daughters of the multitude of weak people, who had no strength '
                   'to stand against them. And when the sons of the great ones saw the daughters of the poor, '
                   'that they were “good,” meaning beautiful of form and appearance, they would oppress them '
                   'and take whichever of them were good, from all the people, and those that were pleasing in '
                   'their eyes, whether unmarried or married to a husband; for whoever was greater than his '
                   'fellow oppressed his fellow, and there was none to rescue from their hand. And “adam” is '
                   'said of the lesser and the weak, as it says (Psalms 49) “both benei adam and benei ish”: '
                   '“benei adam,” the lesser; “benei ish,” the great.',
                   'ours', ref='Radak on Genesis 6:2:2', highlight=['bnei-elohim', 'vayikchu']),
        commentary(f'{prefix}-shadal', h, 13, 'Shadal', 'שד"ל', 'Shadal',
                   '“The sons of God”: … It seems to me that the “sons of God” were some of the descendants of '
                   'Cain, who wandered the earth, and whose nature was hard and evil like Cain their father; '
                   'and the descendants of Seth were settled in a civic community and were called “sons of '
                   'man” (benei adam). And some of the descendants of Cain were stronger and taller than they, '
                   'and the sons of man were afraid and terrified of them, and called them “sons of God” '
                   'because of their height, their terror and their wildness (for those who dwell in the '
                   'wilderness, in heat by day and frost by night, are of greater stature and strength than '
                   'those who live in the society of the city and conduct themselves with wisdom). Now at '
                   'first the descendants of Seth did not intermingle with the descendants of Cain; but in the '
                   'course of time the descendants of Cain began to snatch for themselves from the daughters '
                   'of men, and some of these remained with their husbands, and some returned to their '
                   'mother’s house and gave birth there. And then there were born within the society of the '
                   'sons of man men taller, harder and more evil than the rest of the descendants of Seth, and '
                   'from then on human society began to be corrupted.',
                   'ours', ref='Shadal on Genesis 6:2:1', highlight=['bnei-elohim', 'vayikchu']),
        commentary(f'{prefix}-malbim', h, 14, 'Malbim', 'מלבי"ם', 'Malbim',
                   'It is known from the study of the ancient peoples that they believed in sons of gods who '
                   'desire the daughters of men; and they would spin fables: when a beautiful woman found favor in the '
                   'eyes of gods, they would come to them and they would bear them children. And [Scripture] '
                   'tells that, according to the thinking of that generation and their vanities, they said '
                   'that the sons of gods see the daughters of men, that they are good, and they find favor in '
                   'their eyes, and they take them as wives; in this way the women went astray from under '
                   'their husbands with men who deluded them into thinking that they were sons of gods. And '
                   'such legends existed in those days and afterwards too; for it is known that in all the '
                   'stories of the ancient peoples they tell that in ancient days sons of gods, who came from '
                   'heaven to earth, reigned over their land and married wives from the daughters of men, and '
                   'from them arose mighty men and rulers — as is found in the stories of Egypt and China and '
                   'the kingdom of Greece, of the gods and demigods who walked upon the high mountains and over '
                   'their land in ancient days. And these became idols for them, and they told of them deeds '
                   'of murder and adultery and every evil trait, until even their worshippers made themselves '
                   'like them in their abominations — like the goddess whose worship was in adultery, and the '
                   'god whom they worshipped with human sacrifices; and these forms of worship lasted until '
                   'the middle of the Roman kingdom, and all the more were they in their strength in the days '
                   'of Moses… Therefore Moses our teacher, peace be upon him, informed us that these Nephilim, '
                   'who are the giants and the tyrants, were in those days and afterwards too; for then there '
                   'were found mighty men of fearsome strength, who said of themselves that they were sons of '
                   'gods who had fallen from heaven, and the people began to worship them. And they were the '
                   'sons of God who came to the daughters of men and they bore them children, until even the '
                   'sons were reckoned as idols. — But know that all these stories and legends, on which the '
                   'priests of the idols built all the matters of idol worship and the stories of the idols '
                   'and mythology, are all a lie and a falsehood: “Can a man make gods for himself, when they '
                   'are no gods?!” Only “they were the mighty men of old, the men of renown”: every mighty man '
                   'who arose in those days, or a man who made a name for himself through his wisdom, they '
                   'would ascribe divinity to him and say that he had fallen from heaven. And this was the '
                   'root of the corruption of humankind, and of idol worship and false belief and vanity; and '
                   'therefore the Lord saw fit to shorten the days of man, so that they would see that they '
                   'are human and mortal, and not gods.',
                   'ours', ref='Malbim on Genesis 6:2:1', highlight=['bnei-elohim', 'nefilim', 'gibborim']),
        commentary(f'{prefix}-jacob', h, 15, 'Benno Jacob', 'בנו יעקב', 'Benno Jacob',
                   'It may be that the epithet “sons of God” is meant here ironically, as in (Psalms 78 '
                   '[82:6–7]) “I said, you are gods, and all of you sons of the Most High — yet you shall die '
                   'like men…”',
                   'ours', start='ייתכן', highlight=['bnei-elohim'], effect='glow'),
        question(f'{prefix}-q-b1', h, 16, '1. Explain: what are the different views in understanding the '
                 'concept “sons of God”? Sort them into groups.', highlight=['bnei-elohim']),
        question(f'{prefix}-q-b2', h, 17, '2. Find proof from the language of our verse that the sons of God '
                 'did violence, as it is explained in the Sifrei on Beha’alotekha.',
                 highlight=['bnei-elohim', 'vayikchu']),
        question(f'{prefix}-q-b3', h, 18, '3. Explain what the connection is between our parasha and the '
                 'parasha of Lamech, 4:17–24.', stop='י"ז-כ"ד'),
    ]})

    # §ג — scan header: ג. ג'. לא ידון רוחי באדם לעולם בשגם הוא בשר
    secs.append({'id': f'{prefix}-yadon', 'titleCard': False, 'title': {'en': '“My Spirit Shall Not Abide”'},
                 'primaryText': P(), 'steps': [
        narration(f'{prefix}-g-intro', 'Genesis 6:3.'),
        commentary(f'{prefix}-mishnah', h, 21, 'Mishnah Sanhedrin', 'משנה סנהדרין', 'Mishnah Sanhedrin',
                   'The generation of the Flood has no share in the World to Come, and they will not stand in '
                   'judgment, as it says, “My spirit shall not abide (yadon) in man forever”: neither judgment '
                   '(din) nor spirit.',
                   'ours', ref='Mishnah Sanhedrin 10:3', highlight=['lo-yadon']),
        commentary(f'{prefix}-gemara', h, 22, 'Sanhedrin', 'גמרא סנהדרין', 'Gemara, Sanhedrin',
                   'R. Yehudah ben Beteira says: They will neither live again nor be judged, as it says, “My '
                   'spirit shall not abide (yadon) in man forever”: neither judgment nor spirit. Another '
                   'explanation: that their soul will not return to its sheath.',
                   'ours', ref='Sanhedrin 108a', highlight=['lo-yadon']),
        commentary(f'{prefix}-br-26', h, 23, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Yishmael son of R. Yose said: I will not put My spirit in them at the time when I give '
                   'the reward of the righteous in the time to come… Rabbi says: “And [he] said” — the '
                   'generation of the Flood said to the Lord: “Lo yadon!” [He will not judge!] R. Akiva said: '
                   '(Psalms 10) “Why does the wicked man scorn God? He says in his heart: You will not call to '
                   'account” — there is no judgment and there is no judge. But there is judgment, and there is '
                   'a judge.',
                   'ours', ref='Bereshit Rabbah 26:6', highlight=['lo-yadon']),
        commentary(f'{prefix}-rashi-1', h, 24, 'Rashi', 'רש"י', 'Rashi',
                   '“My spirit shall not strive (lo yadon) in man”: My spirit shall not be aggrieved and '
                   'contend within Me on account of man.',
                   'ours', ref='Rashi on Genesis 6:3:1', highlight=['lo-yadon']),
        commentary(f'{prefix}-rashi-2', h, 25, 'Rashi', 'רש"י', 'Rashi',
                   '“Forever”: for length of days. Behold, My spirit is in contention within Me, whether to '
                   'destroy or to have mercy; this contention shall not be in My spirit forever, that is, for '
                   'length of days.',
                   'ours', ref='Rashi on Genesis 6:3:2', highlight=['lo-yadon']),
        commentary(f'{prefix}-rashi-3', h, 26, 'Rashi', 'רש"י', 'Rashi',
                   '“And his days shall be a hundred and twenty years”: For up to a hundred and twenty years '
                   'I will be patient with them, and if they do not repent, I will bring a flood upon them…',
                   'ours', ref='Rashi on Genesis 6:3:4', highlight=['shana-120']),
        question(f'{prefix}-q-g1', h, 27, '1. What is the difference in understanding the word “ruchi” (“My '
                 'spirit”) between the words of the Gemara and Rashi’s interpretation?',
                 highlight=['lo-yadon']),
        question(f'{prefix}-q-g2', h, 28, '2. What is the difference in understanding the verb “yadon” between '
                 'the words of the Gemara and Rashi’s interpretation?', highlight=['lo-yadon']),
        question(f'{prefix}-q-g3', h, 29, '3. In what do the words of Rabbi and of R. Akiva differ from all '
                 'the rest? And what compelled them to expound so?'),
        question(f'{prefix}-q-g4', h, 30, '4. Where did R. Akiva find a hint for the answer: “But there is '
                 'judgment and there is a judge!”?'),
        question(f'{prefix}-q-g5', h, 31, '5. Among the commentators on the Mishnah, there are some who rely '
                 'on Ezekiel 37 to interpret the words of the Mishnah. What support is given there for '
                 'understanding the words of the Mishnah here?'),
    ]})
    return secs
