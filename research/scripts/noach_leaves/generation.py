from noach_lib import *  # noqa: F401,F403
"""Theme 1 — A righteous man in his generations (Gen 6:9–7:5): leaves 1947, 1954, 1958.

Paper trail: research/parshiyot/noach-leaves/generation.md (slices, omissions, translation notes).
"""
from nechama_lib import VERSES


# ─── panels ─────────────────────────────────────────────────────────────────

def gen_6_9_10():
    return primary('Genesis 6:9-10', ['6:9', '6:10'], {
        'toldot': ('אלה תולדת נח', 'This is the line of Noah'),
        'tzadik': ('נח איש צדיק', 'Noah was a righteous man'),
        'tamim': ('תמים היה', 'he was blameless'),
        'bedorotav': ('בדרתיו', 'in his age'),
        'et-haelohim': ('את האלהים התהלך נח', 'Noah walked with God'),
        'vayoled': ('ויולד נח שלשה בנים', 'Noah begot three sons'),
    })


def gen_6_9():
    return primary('Genesis 6:9', ['6:9'], {
        'toldot': ('אלה תולדת נח', 'This is the line of Noah'),
        'tzadik': ('נח איש צדיק', 'Noah was a righteous man'),
        'tamim': ('תמים היה', 'he was blameless'),
        'bedorotav': ('בדרתיו', 'in his age'),
        'et-haelohim': ('את האלהים התהלך נח', 'Noah walked with God'),
    })


def gen_6_9_13():
    return primary('Genesis 6:9-13', ['6:9', '6:10', '6:11', '6:12', '6:13'], {
        'toldot': ('אלה תולדת נח', 'This is the line of Noah'),
        'vayomer': ('ויאמר אלהים לנח', 'God said to Noah'),
    })


def gen_6_11_13_19():
    return primary('Genesis 6:11-13, 19', ['6:11', '6:12', '6:13', '6:19'], {
        'hishchit': ('כי השחית כל בשר את דרכו על הארץ', 'for all flesh had corrupted its ways on earth'),
        'ketz': ('קץ כל בשר', 'put an end to all flesh'),
        'mipneihem': ('חמס מפניהם', 'lawlessness because of them'),
        'mikol-hachai': ('ומכל החי מכל בשר', 'And of all that lives, of all flesh'),
    })


def gen_6_13_14():
    return primary('Genesis 6:13-14', ['6:13', '6:14'], {
        'ketz': ('קץ כל בשר בא לפני', 'I have decided to put an end to all flesh'),
        'hineni': ('והנני משחיתם את הארץ', 'I am about to destroy them with the earth'),
        'aseh': ('עשה לך תבת עצי גפר', 'Make yourself an ark of gopher wood'),
    })


def gen_6_11_13():
    return primary('Genesis 6:11-13', ['6:11', '6:12', '6:13'], {
        'vatimale': ('ותמלא הארץ חמס', 'the earth was filled with lawlessness'),
        'ketz': ('קץ כל בשר בא לפני', 'I have decided to put an end to all flesh'),
        'ki-male': ('כי מלאה הארץ חמס מפניהם', 'for the earth is filled with lawlessness because of them'),
        'hineni': ('והנני משחיתם את הארץ', 'I am about to destroy them with the earth'),
    })


def frag(key, letters, en):
    """The pointed fragment of verse `key` whose bare letters are `letters`, and the matching
    English, which must occur verbatim in the cached English (verse text is never typed)."""
    assert en in VERSES[key]['en'], f'{en!r} not in the English of {key}'
    return vp(VERSES[key]['he'], letters), en


def side(frags):
    return ' … '.join(f[0] for f in frags), ' … '.join(f[1] for f in frags)


def comparison_6_7():
    """1947 §א: her table of parallel verses, chapter 6 in the right column and chapter 7 in the
    left, as she set it (her 6:18 and 6:21 rows and the end of 6:20 are left out so the panel fits a phone).
    Each row is the fragment she quoted (with a little more of the verse where
    her fragment would not make sense alone), joined with " … " as her ellipses join them."""
    rhe, ren = side([
        frag('6:13', 'ויאמר אלהים לנח', 'God said to Noah'),
        frag('6:19', 'ומכל החי מכל בשר שנים מכל תביא אל התבה',
             'And of all that lives, of all flesh, you shall take two of each into the ark'),
        frag('6:20', 'מהעוף למינהו ומן הבהמה למינה מכל רמש האדמה למינהו',
             'From birds of every kind, cattle of every kind, every kind of creeping thing on earth'),
        frag('6:22', 'ויעש נח ככל אשר צוה אתו אלהים כן עשה', 'Noah did so; just as God commanded him, so he did.'),
    ])
    lhe, len_ = side([
        frag('7:1', 'ויאמר יהוה לנח', 'the Lord said to Noah'),
        frag('7:2', 'מכל הבהמה הטהורה תקח לך שבעה שבעה', 'Of every pure animal you shall take seven pairs'),
        frag('7:3', 'גם מעוף השמים שבעה שבעה', 'of the birds of the sky also, seven pairs'),
        frag('7:5', 'ויעש נח ככל אשר צוהו יהוה', 'And Noah did just as the Lord commanded him.'),
    ])
    right = words(rhe, ren, {
        'r-elohim': ('ויאמר אלהים לנח', 'God said to Noah'),
        'r-shnayim': ('מכל בשר שנים מכל תביא אל התבה', 'of all flesh, you shall take two of each into the ark'),
        'r-lemino': ('מהעוף למינהו ומן הבהמה למינה מכל רמש האדמה למינהו',
                     'From birds of every kind, cattle of every kind, every kind of creeping thing on earth'),
        'r-vayaas': ('ויעש נח ככל אשר צוה אתו אלהים', 'Noah did so; just as God commanded him'),
    })
    left = words(lhe, len_, {
        'l-hashem': ('ויאמר יהוה לנח', 'the Lord said to Noah'),
        'l-tahor': ('מכל הבהמה הטהורה', 'Of every pure animal'),
        'l-tikach': ('תקח לך שבעה שבעה', 'you shall take seven pairs'),
        'l-of': ('גם מעוף השמים שבעה שבעה', 'of the birds of the sky also, seven pairs'),
        'l-vayaas': ('ויעש נח ככל אשר צוהו יהוה', 'And Noah did just as the Lord commanded him'),
    })
    for w in left.values():
        w['side'] = 'left'
    for w in right.values():
        w['side'] = 'right'
    return {'ref': 'Genesis 6:13-22; 7:1-5', 'mode': 'comparison',
            'left': {'ref': 'Genesis 7:1-3, 5', 'he': lhe, 'en': len_},
            'right': {'ref': 'Genesis 6:13, 19-20, 22', 'he': rhe, 'en': ren},
            'words': {**left, **right}}


# ─── 1947 ───────────────────────────────────────────────────────────────────

def leaf_1947(prefix='gn-1947'):
    """Gilayon תש"ז (161777): §א (ch. 6 and ch. 7, Malbim), §ב (toledot: Ibn Ezra, Ramban), §ג (Rashi)."""
    h = harvest('generation', '1947')
    secs = []

    # §א — scan header: א. שאלה כללית:  Her table ([3]) is the comparison panel; [4] «ועוד ועוד
    # ועוד...» is not rendered. The German-reading tip [0] is not in the harvest's sections.
    secs.append({'id': prefix, 'title': {'en': '1947 · God Speaks to Noah Twice'},
                 'primaryText': comparison_6_7(), 'steps': [
        narration(f'{prefix}-intro', 'God speaks to Noah in chapter 6, and again in chapter 7.'),
        question(f'{prefix}-q-a0', h, 2, 'Compare the parallel verses in chapter 6 and in chapter 7, for example:'),
        narration(f'{prefix}-row-said', '“God said to Noah” … “the Lord said to Noah.”',
                  highlight=['r-elohim', 'l-hashem']),
        narration(f'{prefix}-row-did', '“Just as God commanded him” … “just as the Lord commanded him.”',
                  highlight=['r-vayaas', 'l-vayaas']),
        narration(f'{prefix}-row-pairs', '“Two of each,” of every kind … “seven pairs” of the pure.',
                  highlight=['r-shnayim', 'r-lemino', 'l-tahor', 'l-tikach', 'l-of']),
        narration(f'{prefix}-row-take', '“You shall take two of each into the ark” … “you shall take seven pairs.”',
                  highlight=['r-shnayim', 'l-tikach']),
        commentary(f'{prefix}-malbim', h, 5, 'Malbim', 'מלבי"ם', 'Malbim',
                   'Now the Lord’s speech in chapter 7 is not of the same kind as the preceding speech (in '
                   'chapter 6). For the first speech came from His aspect as Elohim, Creator of the world, for '
                   'the world was created and is sustained by the name Elohim; as we heard throughout the '
                   'section of Bereshit, only the name Elohim is mentioned. And that is what He now saw to: '
                   'that when the flood came, not one species would be missing from existence. And in the '
                   'second speech (chapter 7) He said another thing, a particular one, from His individual '
                   'providence over Noah, who was righteous before Him; and the Lord watches over the affairs '
                   'of the righteous man, his possessions and the needs of his household.',
                   'ours', start='והנה דיבור',
                   highlight=['r-elohim', 'l-hashem']),
        question(f'{prefix}-q-a1', h, 6, '1. What are the differences in content and in style between the two '
                 'chapters that are explained by this fundamental distinction, and how are they explained by it?'),
        question(f'{prefix}-q-a2', h, 7, '2. Can you explain, according to the words of Malbim above, what the '
                 'extra emphasis on “of its kind” (three times!) in chapter 6, verse 20 is for?',
                 highlight=['r-lemino']),
    ]})

    # §ב — scan header: ב. ו' ט' אלה תולדות  ראב"ע - רמב"ן.  The scan names Ibn Ezra and Ramban only;
    # [11] and [12] are the digitizer's expansion of those names, quoted whole. [13], her Q1, has no
    # number in the harvest (the digitization dropped her «1.»; triage keeps the digitization).
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“This Is the Line of Noah”'},
                 'primaryText': gen_6_9_10(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 6:9–10.'),
        commentary(f'{prefix}-ibn-ezra', h, 11, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra',
                   '“These are the toledot”: like “the events,” in the sense of “what a day may bring forth” '
                   '(yeled). And likewise “These are the toledot of Jacob.”',
                   'ours', ref='Ibn Ezra on Genesis 6:9:1', start='אלה תולדות:', highlight=['toldot']),
        commentary(f'{prefix}-ramban-a', h, 12, 'Ramban', 'רמב"ן', 'Ramban',
                   '“These are the toledot of Noah”: Its sense, some explained (Ibn Ezra and Radak), is his '
                   'events, in the sense of “what a day may bring forth” (Proverbs 27:1), and it alludes to the '
                   'whole section. But this is not right in my eyes, for a person’s events are not his toledot. '
                   'What is right is that it is in its plain meaning, as in “These are the toledot of the sons of '
                   'Noah” (below, 10:1), “And these are the toledot of Ishmael” (below, 25:12): it says, “These '
                   'are the toledot of Noah: Shem, Ham and Japheth.” But it repeated “and Noah begot” because it '
                   'broke off and said “Noah was a righteous man, blameless,” to make known why He commanded him '
                   'about the ark.',
                   'ours', ref='Ramban on Genesis 6:9:1', start='אלה תולדות נח:', stop='למה ציוהו בתיבה.',
                   highlight=['toldot', 'tzadik', 'vayoled']),
        commentary(f'{prefix}-ramban-b', h, 12, 'Ramban', 'רמב"ן', 'Ramban',
                   'And even though it already said above (5:32), “And Noah was five hundred years old, and Noah '
                   'begot Shem, Ham and Japheth,” it mentioned them once more, to tell that he was not like all '
                   'his forefathers, who begot sons and daughters. And this is the sense of “three sons”: it '
                   'mentions their number to say that these three alone were his offspring, and they were saved '
                   'by his merit, and from these the whole earth was spread abroad.',
                   'ours', ref='Ramban on Genesis 6:9:1', start='ואף על פי', highlight=['vayoled']),
        question(f'{prefix}-q-b1', h, 13, 'What is the difference between Ibn Ezra and Ramban in explaining the '
                 'word “toledot”?', highlight=['toldot']),
        commentary(f'{prefix}-ibn-ezra-37', h, 14, 'Ibn Ezra', 'ראב"ע', 'Ibn Ezra, on Genesis 37:1',
                   'And the sense of “These are the toledot of Jacob”: these are the happenings that befell him '
                   'and the events that came upon him; from the same root as “what a day may bring forth” '
                   '(Proverbs 27:1).',
                   'ours', ref='Ibn Ezra on Genesis 37:1:1', start='והטעם אלה תולדות', highlight=['toldot']),
        question(f'{prefix}-q-b1b', h, 15, 'Explain Ramban’s words here: “What is right is that it is in its '
                 'plain meaning.”', highlight=['toldot']),
        question(f'{prefix}-q-b2', h, 16, '2. What are Ramban’s arguments against Ibn Ezra?'),
        question(f'{prefix}-q-b3', h, 17, '3. Can you remove Ramban’s complaints against Ibn Ezra?'),
    ]})

    # §ג — scan header: ג. שאלות ודיוקים ברש"י:  The scan has two bare pointers, «1) ט ד"ה אלה תולדות
    # נח» and «2) "בדורותיו"»; [19], [20], [22] are the digitizer's Rashi texts for them.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Righteous in His Age”'},
                 'primaryText': gen_6_9(), 'steps': [
        narration(f'{prefix}-c-intro', '“Noah was a righteous man; he was blameless in his age.”'),
        commentary(f'{prefix}-rashi-a', h, 19, 'Rashi', 'רש"י', 'Rashi',
                   '“These are the toledot of Noah”: Since it mentioned him, it told his praise, as it is said '
                   '(Proverbs 10:7), “The mention of the righteous is for a blessing.”',
                   'ours', ref='Rashi on Genesis 6:9:1', start='אלה תולדות נח:', highlight=['toldot', 'tzadik']),
        commentary(f'{prefix}-rashi-b', h, 20, 'Rashi', 'רש"י', 'Rashi',
                   'Another explanation: to teach you that the chief toledot of the righteous are good deeds.',
                   'ours', ref='Rashi on Genesis 6:9:1', highlight=['toldot', 'tzadik']),
        question(f'{prefix}-q-c1', h, 21, 'What is difficult for him? What is the fundamental difference between '
                 'his two explanations? (And see Rashi on 18:18.) Copy out our verse twice, and punctuate it to '
                 'match each of Rashi’s explanations!', highlight=['toldot', 'tzadik']),
        commentary(f'{prefix}-rashi-dor', h, 22, 'Rashi', 'רש"י', 'Rashi',
                   '“In his generations”: (Sanhedrin 109) Some of our Rabbis expound it to his credit: all the '
                   'more so, had he been in a generation of righteous people, he would have been more righteous. '
                   'And some expound it to his discredit: by the measure of his generation he was righteous, but '
                   'had he been in the generation of Abraham, he would have counted for nothing.',
                   'ours', ref='Rashi on Genesis 6:9:2', start='בדורותיו:', highlight=['bedorotav']),
        commentary(f'{prefix}-levush', h, 23, 'Levush HaOrah', 'לבוש האורה', 'Levush HaOrah (R. Mordechai Yaffe)',
                   'Why did the one who expounds it to his credit say, “if he had been in a generation of '
                   'righteous people…,” while the one who expounds it to his discredit said, “but if he had been '
                   'in the generation of Abraham…”? Why did he change his wording, to say “in the generation of '
                   'Abraham,” and not say there too “in a generation of righteous people”?',
                   'ours', start='מאי טעמא', highlight=['bedorotav']),
        question(f'{prefix}-q-c2', h, 24, 'Try to answer his difficulty!'),
        commentary(f'{prefix}-br', h, 25, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'A parable of a king who had two sons, one grown and one small. He said to the small one: '
                   'Walk with me! And he said to the grown one: Come and walk before me! So Abraham, whose '
                   'strength was good: “Walk before Me and be blameless”; but Noah, whose strength was poor: '
                   '“Noah walked with God.”',
                   'ours', ref='Bereshit Rabbah 30:10', start='"משל', highlight=['et-haelohim'], effect='glow'),
        question(f'{prefix}-q-c3', h, 26, 'a. What is the meaning of “et” (“with”) in our verse, according to the '
                 'expounder, and where do we find this use of “et” in the Torah?', highlight=['et-haelohim']),
        question(f'{prefix}-q-c4', h, 27, 'b. Can you explain, from a comparison of chapter 6 with chapter 18, '
                 'that Noah’s strength was not as good as Abraham’s?'),
    ]})
    return secs


# ─── 1954 ───────────────────────────────────────────────────────────────────

def leaf_1954(prefix='gn-1954'):
    """Gilayon תשי"ד (161402): §א (Cassuto's twelve paragraphs), §ב (6:12: Rashi, Ramban), §ג (6:14:
    Tanchuma, its variant, Rashi). No manuscript image (pack §7a)."""
    h = harvest('generation', '1954')
    secs = []

    # §א — scan header: א. שאלת מבנה כללי:  Q1 [2] is cut before her blank table; the two rows she
    # filled in (6:9–12, 6:13–22) and the start of the third (7:1) are given by the narration after it.
    secs.append({'id': prefix, 'title': {'en': '1954 · The Flood’s Shape'},
                 'primaryText': gen_6_9_13(), 'steps': [
        narration(f'{prefix}-intro', 'The flood story opens: Genesis 6:9.'),
        commentary(f'{prefix}-cassuto', h, 1, 'Cassuto', 'קאסוטו', 'Cassuto, From Noah to Abraham',
                   'The structure of the section in the form before us is a refined structure, ordered in its '
                   'parts and in its details… The section divides clearly into twelve paragraphs. Each paragraph '
                   'contains a particular episode in the course of events, and all of them are bound to one '
                   'another by parallels in words and in expressions… The series of paragraphs divides into two '
                   'sets of six paragraphs each: a numerical harmony worthy of attention.',
                   'ours', start='מבנה הפרשה', highlight=['toldot']),
        question(f'{prefix}-q-a1', h, 2, '1. Go through the flood story up to 9:17, and mark the division into '
                 'twelve paragraphs and the two sets', stop='ואת שתי המערכות'),
        narration(f'{prefix}-rows', 'Set A: paragraph 1, 6:9–12; paragraph 2, 6:13–22; paragraph 3 from 7:1. '
                  'Set B: paragraphs 7 to 12.', highlight=['toldot', 'vayomer']),
        question(f'{prefix}-q-a2', h, 3, 'b) Explain what unites the first six paragraphs into one set, “which '
                 'describe, stage after stage, a single action,” and what, again, unites the last six paragraphs, '
                 '“which shows us, one after another, the different phases of a single action” (Cassuto).'),
        question(f'{prefix}-q-a3', h, 4, '3. What are the parallels in words and in expressions between the '
                 'different paragraphs?'),
        question(f'{prefix}-q-a4', h, 5, '4. Explain what the parallels of substance are between the beginning '
                 'of set A and the end of set B; between the middle of set A (paragraphs 3–4) and the middle of '
                 'set B (paragraphs 8–9); and so on.'),
    ]})

    # §ב — scan header: ב. י"ב כי השחית כל בשר את דרכו על הארץ.  Bare pointers to Rashi and Ramban;
    # the digitizer split Ramban into [9] and [10]. Her cross-reference [16] to another gilayon is not
    # rendered.
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“All Flesh Had Corrupted Its Ways”'},
                 'primaryText': gen_6_11_13_19(), 'steps': [
        narration(f'{prefix}-b-intro', 'Genesis 6:11–13, and the command to bring the creatures into the ark.'),
        commentary(f'{prefix}-rashi', h, 8, 'Rashi', 'רש"י', 'Rashi',
                   '“For all flesh had corrupted”: even cattle, beasts and birds mated with those not of their kind.',
                   'ours', ref='Rashi on Genesis 6:12:1', start='כי השחית כל בשר:', highlight=['hishchit']),
        question(f'{prefix}-q-b1', h, 11, '1. What is difficult for Rashi?', highlight=['hishchit']),
        commentary(f'{prefix}-ramban-a', h, 9, 'Ramban', 'רמב"ן', 'Ramban',
                   '“For all flesh had corrupted its ways”: If we take “all flesh” in its plain meaning, and say '
                   'that even cattle, beasts and birds corrupted their ways by mating with those not of their '
                   'kind, as Rashi explained, then we must say that “the earth is filled with chamas because of '
                   'them” means not because of all of them but because of some of them, and that it told the '
                   'punishment of man alone. Or we may say that in this too they did not keep to their nature: '
                   'every beast preyed and every bird tore. And so they too were doing chamas.',
                   'ours', ref='Ramban on Genesis 6:12:1', start='כי השחית כל בשר את דרכו:',
                   highlight=['hishchit', 'mipneihem']),
        question(f'{prefix}-q-b2', h, 12, '2. In Ramban’s view, the verse does not sit well with Rashi’s '
                 'explanation. What is the difficulty that Ramban found in Rashi’s explanation?'),
        question(f'{prefix}-q-b3', h, 13, '3. In two ways Ramban tries to settle our verse according to Rashi. '
                 'What are they?'),
        question(f'{prefix}-q-b4', h, 14, '4. Can you bring support for Rashi’s explanation from other places in '
                 'our parasha?'),
        commentary(f'{prefix}-ramban-b', h, 10, 'Ramban', 'רמב"ן', 'Ramban',
                   'And by way of the plain sense, “all flesh” is all mankind. Further on it explains “all flesh '
                   'in which there is the breath of life” (below, 7:15) and “of all that lives, of all flesh” '
                   '(below, verse 19): every living thing with a body. But here “all flesh” is all mankind; and '
                   'so “all flesh shall come to bow down before Me” (Isaiah 66:23), and so “flesh, when there is '
                   'in its skin” (Leviticus 13:24).',
                   'ours', ref='Ramban on Genesis 6:12:1', start='ועל דרך הפשט',
                   highlight=['hishchit', 'ketz', 'mikol-hachai'], effect='glow'),
        question(f'{prefix}-q-b5', h, 15, '5. What support does Ramban bring for his explanation “by way of the '
                 'plain sense” from Isaiah 66? Try to bring more verses as proof for his explanation.',
                 highlight=['hishchit']),
    ]})

    # §ג — scan header: ג. י"ד עשה לך תיבה.  Tanchuma [19] and «נוסח אחר» [20] (harvest kind
    # "question", but they are the midrash she printed) are commentary cards; [21] is the digitizer's
    # Rashi for her pointer «רש"י: י"ד ד"ה עשה לך». Q1–Q2 follow the midrash they ask about.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Make Yourself an Ark”'},
                 'primaryText': gen_6_13_14(), 'steps': [
        narration(f'{prefix}-c-intro', 'God tells Noah what is coming, and what to build.'),
        commentary(f'{prefix}-tanchuma', h, 19, 'Tanchuma', 'תנחומא', 'Tanchuma',
                   'Come and see: why did the Holy One, blessed be He, tell Noah to make an ark? So that they '
                   'would see him sitting and busy with it, and repent. Could the Holy One, blessed be He, not '
                   'have saved them by His word, or raised them to heaven by His faithfulness, that He told him, '
                   '“Make yourself an ark of gopher wood”? Why so? Rather, the Holy One, blessed be He, said: '
                   'Since I tell him, “Make yourself an ark of gopher wood,” and he stands and busies himself '
                   'with it and cuts down cedars, they will gather around him and say to him: Noah! What are you '
                   'doing?! And he will say: An ark! For the Holy One, blessed be He, told me that He is bringing '
                   'a flood on the world. And through this they will hear and repent. So the Holy One, blessed '
                   'be He, reckoned… and they paid him no heed.',
                   'ours', start='בא וראה', highlight=['aseh']),
        commentary(f'{prefix}-tanchuma-b', h, 20, 'Tanchuma', 'נוסח אחר', 'Tanchuma, another version',
                   'Noah went and planted cedars, and they would say to him: These cedars, what are they for? He '
                   'said to them: The Holy One, blessed be He, means to bring a flood, and He told me '
                   'to make an ark, so that I and my household may escape. And they would laugh at him and mock '
                   'his words. And he would water those cedars, and they grew, and they would say to him: What '
                   'are you doing? And he would answer them in the same way. And they would mock him. At the end '
                   'of his days he cut them down and was sawing them, and they would say to him: What are you '
                   'doing? And he would tell them so, and he warned them. Since they did not repent…',
                   'ours', start='עמד נח', highlight=['aseh', 'hineni']),
        question(f'{prefix}-q-c1', h, 22, '1. Explain what the idea of this midrash is.'),
        question(f'{prefix}-q-c2', h, 23, '2. What trait of the people of the generation of the flood stands out '
                 'in this midrash?'),
        commentary(f'{prefix}-rashi-c', h, 21, 'Rashi', 'רש"י', 'Rashi',
                   '“Make yourself an ark”: He has many ways of relief and rescue; why did He trouble him with '
                   'this building? So that the people of the generation of the flood would see him busy with it '
                   'for 120 years and ask him, “What is this to you?” And he says to them: The Holy One, blessed '
                   'be He, is going to bring a flood on the world. Perhaps they would repent.',
                   'ours', ref='Rashi on Genesis 6:14:1', start='עשה לך תבת:', highlight=['aseh'], effect='glow'),
        question(f'{prefix}-q-c3', h, 24, '3. Where do we find this idea again in Rashi on chapter 7?'),
        question(f'{prefix}-q-c4', h, 25, '4. Where do we find this idea in the words of the prophets?'),
    ]})
    return secs


# ─── 1958 ───────────────────────────────────────────────────────────────────

def leaf_1958(prefix='gn-1958'):
    """Gilayon תשי"ח (161147): §א (toledot), §ב–ג (bedorotav), §ד (Noah and Abraham), §ה–ז (chamas).
    Omitted for density: §א Q3 [6], her aside [10], §ו Q2 [38] and «ענה לשאלתו» [40]; see generation.md."""
    h = harvest('generation', '1958')
    secs = []

    # §א — scan header: א. רש"י ד"ה אלה תולדות נח נח איש צדיק.  Rashi [2] is split at «דבר אחר».
    # Q1–Q5 ask about Rashi and follow him; Radak [3] then precedes Q6–Q7, which ask about him.
    secs.append({'id': prefix, 'title': {'en': '1958 · In His Generations'},
                 'primaryText': gen_6_9(), 'steps': [
        narration(f'{prefix}-intro', 'Genesis 6:9.'),
        commentary(f'{prefix}-rashi-a', h, 2, 'Rashi', 'רש"י', 'Rashi',
                   '“These are the toledot of Noah: Noah was a righteous man”: Since it mentioned him, it told '
                   'his praise, as it is said (Proverbs 10), “The mention of the righteous is for a blessing.”',
                   'ours', ref='Rashi on Genesis 6:9:1', start='אלה תולדות נח נח איש צדיק:', stop='לברכה".',
                   highlight=['toldot', 'tzadik']),
        commentary(f'{prefix}-rashi-b', h, 2, 'Rashi', 'רש"י', 'Rashi',
                   'Another explanation: to teach you that the chief toledot of the righteous are good deeds.',
                   'ours', ref='Rashi on Genesis 6:9:1', start='דבר אחר', highlight=['toldot', 'tzadik']),
        question(f'{prefix}-q-a1', h, 4, '1. What is difficult for him?', highlight=['toldot', 'tzadik']),
        question(f'{prefix}-q-a2', h, 5, '2. What is the fundamental difference between his two explanations?'),
        question(f'{prefix}-q-a4', h, 7, '4. By the rule that Rashi brings two explanations only if he was not '
                 'at ease with either one of them alone: what is the weakness of each of his two explanations?'),
        question(f'{prefix}-q-a5', h, 8, '5. The Maharal of Prague, in his book Gur Aryeh on Rashi, raises a '
                 'difficulty about Rashi’s style in his second explanation: Why did he say “the chief toledot of '
                 'the righteous,” and not say: to teach you that the toledot of the righteous are good deeds?'),
        commentary(f'{prefix}-tanchuma', h, 9, 'Tanchuma', 'תנחומא', 'Tanchuma',
                   '“A person’s toledot are good deeds.”',
                   'ours', ref='Midrash Tanchuma, Noach 2', start='"תלדותיו', highlight=['toldot']),
        commentary(f'{prefix}-radak', h, 3, 'Radak', 'רד"ק', 'Radak',
                   '“These are the toledot of Noah”: “toledot” means the events that befell him in the matter of '
                   'the flood and after it; and so (Genesis 37) “These are the toledot of Jacob,” for events are '
                   'the offspring (toledot) of the days; and so it says (Proverbs 27), “for you do not know what a '
                   'day may bring forth (yeled).”',
                   'ours', ref='Radak on Genesis 6:9:1', start='אלה תולדות נח:', highlight=['toldot']),
        question(f'{prefix}-q-a6', h, 12, '6. Does Radak, in his explanation of the word “toledot,” agree with one '
                 'of Rashi’s two explanations, or did he choose another way of his own?', highlight=['toldot']),
        question(f'{prefix}-q-a7', h, 13, '7. How is the difficulty that faced Rashi (question 1) resolved '
                 'according to Radak’s words?'),
    ]})

    # §ב — scan header: ב. צדיק תמים היה בדורותיו.  §ג — same verse; it opens with the Rashi she
    # printed ('before 19', lost in the digitization). §ד — scan header: ד. ט ד"ה את האלוקים התהלך נח:
    # opens with the Rashi she printed ('before 24'), then Bereshit Rabbah [24], split at R. Nechemiah.
    secs.append({'id': f'{prefix}-b', 'titleCard': False, 'title': {'en': '“In His Generations”'},
                 'primaryText': gen_6_9(), 'steps': [
        narration(f'{prefix}-b-intro', '“He was blameless in his age.”'),
        commentary(f'{prefix}-tanchuma-buber', h, 16, 'Tanchuma Buber', 'תנחומא באבער', 'Tanchuma Buber',
                   'What is “in his generations”? Some expound it to his credit and some expound it to his '
                   'discredit. Righteous in his generations, and not in other generations. A parable: what is the '
                   'matter like? If a person puts a silver sela among copper selas, that silver one looks fine. So '
                   'was Noah: he looked righteous in the generation of the flood. Some expound it to his credit. '
                   'How? A parable of a jar of balsam that lay in a grave, and its scent was good; had it been in '
                   'a house, how much more so.',
                   'ours', ref='Tanchuma Buber, Noach 5', start='מהו', highlight=['bedorotav']),
        question(f'{prefix}-q-b', h, 17, 'Explain why the one who expounds it to his discredit chose the parable '
                 'of the coin (a thing given to sight), and the one who expounds it to his credit chose balsam oil '
                 '(a thing that spreads scent)?', highlight=['bedorotav']),
        commentary(f'{prefix}-rashi-dor', h, 'before 19', 'Rashi', 'רש"י', 'Rashi',
                   '“In his generations”: Some of our Rabbis expound it to his credit: all the more so, had he '
                   'been in a generation of righteous people, he would have been more righteous. And some expound '
                   'it to his discredit: by the measure of his generation he was righteous, but had he been in '
                   'the generation of Abraham, he would have counted for nothing.',
                   'ours', ref='Rashi on Genesis 6:9:2', start='"בדורותיו":', highlight=['bedorotav']),
        commentary(f'{prefix}-levush', h, 19, 'Levush HaOrah', 'לבוש האורה', 'Levush HaOrah, on Rashi',
                   'And know that these two views, that is, those who expound to his credit and those who '
                   'expound to his discredit, give Noah one and the same rank in his righteousness, and do not '
                   'differ over the level of Noah’s righteousness: by the words of both, he was no more than a '
                   'middling righteous man. Only, the one who expounds to his credit says that the verse’s '
                   'intent is: had he been in generations of righteous people and learned from their deeds, he '
                   'would surely have been a greater righteous man than he was. And the one who expounds to his '
                   'discredit says that the meaning of “in his generations” is: by the measure of his generation '
                   'he was righteous, and the verse disparages him, saying that he was not steadfast in his '
                   'righteousness, so that even had he been in the generation of Abraham he would not have been '
                   'more righteous, for he would not have learned from his deeds, and he would have counted for '
                   'nothing.',
                   'ours', start='ודע', highlight=['tzadik', 'bedorotav']),
        question(f'{prefix}-q-c1', h, 20, '1. Explain: if, as the author of Levush HaOrah says, there is no '
                 'dispute among our Rabbis about Noah’s character and worth, then what did they disagree about, '
                 'that they reached opposite conclusions?', highlight=['bedorotav']),
        question(f'{prefix}-q-c2', h, 21, '2. What are the proofs, from what is told in our parasha (chapters 6–7), '
                 'of the “middling-ness” of this righteous man?'),
        question(f'{prefix}-q-c3', h, 22, '3. What are the places in Rashi on chapters 6–7 where Rashi follows '
                 'this view (that he was righteous only up to a middling level)?'),
        commentary(f'{prefix}-rashi-et', h, 'before 24', 'Rashi', 'רש"י', 'Rashi',
                   'And of Abraham it says (Genesis 24), “before whom I have walked.” '
                   'Noah needed support to hold him up, but Abraham strengthened himself and walked in his '
                   'righteousness on his own.',
                   'ours', ref='Rashi on Genesis 6:9:3', start='ובאברהם', highlight=['et-haelohim']),
        commentary(f'{prefix}-br-a', h, 24, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   '“Noah walked with God” (Genesis 6:9). R. Yehuda and R. Nechemiah. R. Yehuda said: A parable '
                   'of a king who had two sons, one grown and one small. He said to the small one: Walk with me. '
                   'And he said to the grown one: Come and walk before me. So Abraham, whose strength was good: '
                   '“Walk before Me and be blameless”; but Noah, whose strength was poor: “Noah walked with God.”',
                   'ours', ref='Bereshit Rabbah 30:10', stop='שהיה כוחו רע – "את האלוקים התהלך נח".',
                   highlight=['et-haelohim']),
        commentary(f'{prefix}-br-b', h, 24, 'Bereshit Rabbah', 'בראשית רבה', 'Bereshit Rabbah',
                   'R. Nechemiah said: A parable of a king’s friend who was sinking in thick mud. The king looked '
                   'out and saw him. He said to him: Rather than sink in the mud, walk with me. That is what is '
                   'written: “Noah walked with God.” And what is Abraham like? Like a king’s friend who saw the '
                   'king walking in dark alleys. His friend looked out and began to light the way for him through '
                   'the window. The king looked out and saw him, and said to him: Rather than light for me through '
                   'the window, come and light the way before me. So the Holy One, blessed be He, said to Abraham: '
                   'Rather than light for Me from Mesopotamia and its neighbors, come and light before Me in the '
                   'land of Israel!',
                   'ours', ref='Bereshit Rabbah 30:10', start="ר' נחמיה אמר", highlight=['et-haelohim'],
                   effect='glow'),
        question(f'{prefix}-q-d1', h, 25, '1. What is the difficulty that faced the midrash and Rashi, which they '
                 'wanted to resolve?', highlight=['et-haelohim']),
        question(f'{prefix}-q-d2', h, 26, '2. What is the meaning of the word “et” in our verse in their view, and '
                 'where do we find “et” in the Torah in this meaning?', highlight=['et-haelohim']),
        question(f'{prefix}-q-d3', h, 27, '3. Can you prove, from a comparison of our parasha with Parashat '
                 'Vayera, this difference that the Sages found between Noah and Abraham?'),
        question(f'{prefix}-q-d4', h, 28, '4. According to R. Yehuda and according to R. Nechemiah alike, Abraham '
                 'is greater than Noah. Explain, then, what is the difference between their views?',
                 stop='בין דעותיהם?'),
    ]})

    # §ה — scan header: ה. י"א. ותמלא הארץ חמס.  §ו — ו. יג ויאמר אלוהים אל נח: קץ כל בשר…
    # §ז — ז. יג קץ כל בשר בא לפני כי מלאה הארץ חמס מפניהם, והנני משחיתם את הארץ.
    secs.append({'id': f'{prefix}-c', 'titleCard': False, 'title': {'en': '“Filled with Lawlessness”'},
                 'primaryText': gen_6_11_13(), 'steps': [
        narration(f'{prefix}-c-intro', 'Genesis 6:11–13. The word for lawlessness is chamas.'),
        commentary(f'{prefix}-rashi-chamas', h, 31, 'Rashi', 'רש"י', 'Rashi', '“Chamas”: robbery.',
                   'ours', start='חמס: גזל', highlight=['vatimale']),
        commentary(f'{prefix}-rashi-chamas-b', h, 32, 'Rashi', 'רש"י', 'Rashi, in some editions',
                   'Robbery, as it is said (Jonah 3), “and of the chamas that is in their hands.”',
                   'ours', start='גזל, שנאמר', highlight=['vatimale']),
        question(f'{prefix}-q-e', h, 33, 'Explain how the verse in Jonah can prove that his explanation is right '
                 '(“as it is said”): is it not so that there too, as in our verse, the word “chamas” appears '
                 'without any added explanation, as in our verse?', highlight=['vatimale']),
        commentary(f'{prefix}-rashi-gezel', h, 36, 'Rashi', 'רש"י', 'Rashi',
                   'Their sentence was sealed only for robbery.',
                   'ours', ref='Rashi on Genesis 6:13:2', highlight=['ketz', 'ki-male']),
        question(f'{prefix}-q-f1', h, 37, '1. What is difficult for him in the verse?', highlight=['ki-male']),
        question(f'{prefix}-q-f3', h, 39, '3. The author of Sefer HaZikaron raises a difficulty about Rashi’s '
                 'wording: Why does Rashi enter into the negative, saying “Their sentence was sealed only for…,” '
                 'and why did he not say it in the positive: their sentence was sealed for robbery.'),
        commentary(f'{prefix}-sanhedrin', h, 43, 'Sanhedrin', 'סנהדרין', 'Sanhedrin',
                   'R. Yochanan said: Come and see how great is the power of chamas! For the generation of the '
                   'flood transgressed everything, and their sentence was not sealed against them until they '
                   'stretched out their hands in robbery, as it is said: “For the earth is filled with chamas '
                   'because of them, and I am about to destroy them with the earth.”',
                   'ours', ref='Sanhedrin 108a', highlight=['ki-male', 'hineni'], effect='glow'),
        question(f'{prefix}-q-g1', h, 44, '1. What is the difference in style between Rashi’s words on our verse '
                 '(see question 3) and his source, these words of the Gemara?', stop='דברי הגמרא האלה?'),
        question(f'{prefix}-q-g2', h, 45, '2. Where do we find, in our prayers, robbery singled out as the '
                 'greatest of sins?'),
    ]})
    return secs
