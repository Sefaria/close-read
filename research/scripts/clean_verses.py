"""Clean verse texts pulled from Sefaria into the form data/nasso.json needs.

- Strip cantillation marks (U+0591..U+05AF, U+05BD, U+05C0, U+05C3, U+05C6)
- Strip HTML tags from English (footnote markers, small caps GOD, etc)
- Strip Hebrew typographical inserts (samekh markers from the masoretic text)
- Replace 'GOD' rendering with 'the Lord' (matches existing nasso skeleton style)
- Return clean strings ready to drop into data/nasso.json
"""
import re

# Hebrew cantillation per hard-rules.md
CANT = re.compile(r'[֑-ֽ֯׀׃׆]')

def strip_cant(s):
    return CANT.sub('', s)

def clean_he(s):
    s = strip_cant(s)
    # Strip masoretic markers/spans like {ס}, {פ}, &nbsp;, etc.
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{[סף]\}', '', s)
    s = s.replace('&nbsp;', ' ').replace('&thinsp;', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def clean_en(s):
    # Strip HTML
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    # Restore GOD's name from the various small-caps fragments
    s = s.replace('GOD ', 'the Lord ').replace('GOD,', 'the Lord,')
    s = s.replace('GOD.', 'the Lord.').replace('GOD:', 'the Lord:')
    s = s.replace('GOD!', 'the Lord!').replace('GOD ', 'the Lord ')
    # Remove footnote letter markers (already stripped by HTML strip)
    return s.strip()

# Sources (paste from MCP results above)
VERSE_TEXTS = {
    # Numbers 5:5-8 — the gezel hager passage proper. (Verses 9-10 about priestly
    # contributions are unrelated to the leaves and only bloat the sticky panel.)
    'num-5-5-10': {
        'he': [
            "וַיְדַבֵּ֥ר יְהֹוָ֖ה אֶל־מֹשֶׁ֥ה לֵּאמֹֽר׃",
            "דַּבֵּר֮ אֶל־בְּנֵ֣י יִשְׂרָאֵל֒ אִ֣ישׁ אֽוֹ־אִשָּׁ֗ה כִּ֤י יַעֲשׂוּ֙ מִכׇּל־חַטֹּ֣את הָֽאָדָ֔ם לִמְעֹ֥ל מַ֖עַל בַּיהֹוָ֑ה וְאָֽשְׁמָ֖ה הַנֶּ֥פֶשׁ הַהִֽוא׃",
            "וְהִתְוַדּ֗וּ אֶֽת־חַטָּאתָם֮ אֲשֶׁ֣ר עָשׂוּ֒ וְהֵשִׁ֤יב אֶת־אֲשָׁמוֹ֙ בְּרֹאשׁ֔וֹ וַחֲמִישִׁת֖וֹ יֹסֵ֣ף עָלָ֑יו וְנָתַ֕ן לַאֲשֶׁ֖ר אָשַׁ֥ם לֽוֹ׃",
            "וְאִם־אֵ֨ין לָאִ֜ישׁ גֹּאֵ֗ל לְהָשִׁ֤יב הָאָשָׁם֙ אֵלָ֔יו הָאָשָׁ֛ם הַמּוּשָׁ֥ב לַיהֹוָ֖ה לַכֹּהֵ֑ן מִלְּבַ֗ד אֵ֚יל הַכִּפֻּרִ֔ים אֲשֶׁ֥ר יְכַפֶּר־בּ֖וֹ עָלָֽיו׃",
        ],
        'en': [
            "The Lord spoke to Moses, saying:",
            "Speak to the Israelites: When a man or woman has committed any wrong toward a fellow human being, thus breaking faith with the Lord, and they have realized their guilt,",
            "they shall confess the wrong that they have done. They shall make restitution in the principal amount and add one-fifth to it, giving it to the one who was wronged.",
            "If that party has no kin to whom restitution can be made, the amount repaid shall go to the Lord for the priest — in addition to the ram of expiation with which expiation is made on their behalf.",
        ],
    },
    # Numbers 6:1-3, 5, 7, 11 — verses the Nazir leaves actually anchor on:
    # 1-3 (the vow + abstentions), 5 (hair / consecrated), 7 (nezer Elohav),
    # 11 (sin-offering, chata-al-hanefesh). Verses 4, 6, 8-10, 12 are skipped
    # with an ellipsis to keep the panel from overflowing on tall content.
    'num-6-1-12': {
        'he': [
            "וַיְדַבֵּ֥ר יְהֹוָ֖ה אֶל־מֹשֶׁ֥ה לֵּאמֹֽר׃",
            "דַּבֵּר֙ אֶל־בְּנֵ֣י יִשְׂרָאֵ֔ל וְאָמַרְתָּ֖ אֲלֵהֶ֑ם אִ֣ישׁ אֽוֹ־אִשָּׁ֗ה כִּ֤י יַפְלִא֙ לִנְדֹּר֙ נֶ֣דֶר נָזִ֔יר לְהַזִּ֖יר לַֽיהֹוָֽה׃",
            "מִיַּ֤יִן וְשֵׁכָר֙ יַזִּ֔יר חֹ֥מֶץ יַ֛יִן וְחֹ֥מֶץ שֵׁכָ֖ר לֹ֣א יִשְׁתֶּ֑ה וְכׇל־מִשְׁרַ֤ת עֲנָבִים֙ לֹ֣א יִשְׁתֶּ֔ה וַעֲנָבִ֛ים לַחִ֥ים וִיבֵשִׁ֖ים לֹ֥א יֹאכֵֽל׃",
            "…",
            "כׇּל־יְמֵי֙ נֶ֣דֶר נִזְר֔וֹ תַּ֖עַר לֹא־יַעֲבֹ֣ר עַל־רֹאשׁ֑וֹ עַד־מְלֹ֨את הַיָּמִ֜ם אֲשֶׁר־יַזִּ֤יר לַיהֹוָה֙ קָדֹ֣שׁ יִהְיֶ֔ה גַּדֵּ֥ל פֶּ֖רַע שְׂעַ֥ר רֹאשֽׁוֹ׃",
            "…",
            "לְאָבִ֣יו וּלְאִמּ֗וֹ לְאָחִיו֙ וּלְאַ֣חֹת֔וֹ לֹא־יִטַּמָּ֥א לָהֶ֖ם בְּמֹתָ֑ם כִּ֛י נֵ֥זֶר אֱלֹהָ֖יו עַל־רֹאשֽׁוֹ׃",
            "…",
            "וְעָשָׂ֣ה הַכֹּהֵ֗ן אֶחָ֤ד לְחַטָּאת֙ וְאֶחָ֣ד לְעֹלָ֔ה וְכִפֶּ֣ר עָלָ֔יו מֵאֲשֶׁ֥ר חָטָ֖א עַל־הַנָּ֑פֶשׁ וְקִדַּ֥שׁ אֶת־רֹאשׁ֖וֹ בַּיּ֥וֹם הַהֽוּא׃",
        ],
        'en': [
            "The Lord spoke to Moses, saying:",
            "Speak to the Israelites and say to them: If any man or woman explicitly utters a Nazirite's vow, to set themselves apart for the Lord,",
            "they shall abstain from wine and any other intoxicant; they shall not drink vinegar of wine or of any other intoxicant, neither shall they drink anything in which grapes have been steeped, nor eat grapes fresh or dried.",
            "…",
            "Throughout the term of their vow as Nazirite, no razor shall touch their head; it shall remain consecrated until the completion of their term as Nazirite of the Lord, the hair of their head being left to grow untrimmed.",
            "…",
            "Even if their father or mother, or their brother or sister should die, they must not become defiled for any of them, since hair set apart for their God is upon their head.",
            "…",
            "The priest shall offer one as a sin offering and the other as a burnt offering, and make expiation on the Nazirite's behalf for that they sinned by reason of a soul. That same day their head shall be reconsecrated.",
        ],
    },
    # Numbers 6:22-27
    'num-6-22-27': {
        'he': [
            "וַיְדַבֵּ֥ר יְהֹוָ֖ה אֶל־מֹשֶׁ֥ה לֵּאמֹֽר׃",
            "דַּבֵּ֤ר אֶֽל־אַהֲרֹן֙ וְאֶל־בָּנָ֣יו לֵאמֹ֔ר כֹּ֥ה תְבָרְכ֖וּ אֶת־בְּנֵ֣י יִשְׂרָאֵ֑ל אָמ֖וֹר לָהֶֽם׃",
            "יְבָרֶכְךָ֥ יְהֹוָ֖ה וְיִשְׁמְרֶֽךָ׃",
            "יָאֵ֨ר יְהֹוָ֧ה ׀ פָּנָ֛יו אֵלֶ֖יךָ וִֽיחֻנֶּֽךָּ׃",
            "יִשָּׂ֨א יְהֹוָ֤ה ׀ פָּנָיו֙ אֵלֶ֔יךָ וְיָשֵׂ֥ם לְךָ֖ שָׁלֽוֹם׃",
            "וְשָׂמ֥וּ אֶת־שְׁמִ֖י עַל־בְּנֵ֣י יִשְׂרָאֵ֑ל וַאֲנִ֖י אֲבָרְכֵֽם׃",
        ],
        'en': [
            "The Lord spoke to Moses, saying:",
            "Speak to Aaron and his sons: Thus shall you bless the children of Israel. Say to them:",
            "May the Lord bless you and keep you.",
            "May the Lord make His face shine upon you and be gracious to you.",
            "May the Lord lift up His face upon you and grant you peace.",
            "So shall they put My name upon the children of Israel, and I will bless them.",
        ],
    },
    # Numbers 7:1-3 (Nesi'im opening)
    'num-7-1-3': {
        'he': [
            "וַיְהִ֡י בְּיוֹם֩ כַּלּ֨וֹת מֹשֶׁ֜ה לְהָקִ֣ים אֶת־הַמִּשְׁכָּ֗ן וַיִּמְשַׁ֨ח אֹת֜וֹ וַיְקַדֵּ֤שׁ אֹתוֹ֙ וְאֶת־כׇּל־כֵּלָ֔יו וְאֶת־הַמִּזְבֵּ֖חַ וְאֶת־כׇּל־כֵּלָ֑יו וַיִּמְשָׁחֵ֖ם וַיְקַדֵּ֥שׁ אֹתָֽם׃",
            "וַיַּקְרִ֙יבוּ֙ נְשִׂיאֵ֣י יִשְׂרָאֵ֔ל רָאשֵׁ֖י בֵּ֣ית אֲבֹתָ֑ם הֵ֚ם נְשִׂיאֵ֣י הַמַּטֹּ֔ת הֵ֥ם הָעֹמְדִ֖ים עַל־הַפְּקֻדִֽים׃",
            "וַיָּבִ֨יאוּ אֶת־קׇרְבָּנָ֜ם לִפְנֵ֣י יְהֹוָ֗ה שֵׁשׁ־עֶגְלֹ֥ת צָב֙ וּשְׁנֵ֣י עָשָׂ֣ר בָּקָ֔ר עֲגָלָ֛ה עַל־שְׁנֵ֥י הַנְּשִׂאִ֖ים וְשׁ֣וֹר לְאֶחָ֑ד וַיַּקְרִ֥יבוּ אוֹתָ֖ם לִפְנֵ֥י הַמִּשְׁכָּֽן׃",
        ],
        'en': [
            "On the day that Moses finished setting up the Mishkan, he anointed and consecrated it and all its furnishings, as well as the altar and its utensils. When he had anointed and consecrated them,",
            "the princes of Israel, the heads of ancestral houses, namely, the princes of the tribes, those who were in charge of enrollment, drew near",
            "and brought their offering before the Lord: six draught carts and twelve oxen, a cart for every two princes and an ox for each one. They brought them before the Mishkan.",
        ],
    },
    # Numbers 7:10-12 (the dedication daily command + Nahshon)
    'num-7-10-12': {
        'he': [
            "וַיַּקְרִ֣יבוּ הַנְּשִׂאִ֗ים אֵ֚ת חֲנֻכַּ֣ת הַמִּזְבֵּ֔חַ בְּי֖וֹם הִמָּשַׁ֣ח אֹת֑וֹ וַיַּקְרִ֧יבוּ הַנְּשִׂיאִ֛ם אֶת־קׇרְבָּנָ֖ם לִפְנֵ֥י הַמִּזְבֵּֽחַ׃",
            "וַיֹּ֥אמֶר יְהֹוָ֖ה אֶל־מֹשֶׁ֑ה נָשִׂ֨יא אֶחָ֜ד לַיּ֗וֹם נָשִׂ֤יא אֶחָד֙ לַיּ֔וֹם יַקְרִ֙יבוּ֙ אֶת־קׇרְבָּנָ֔ם לַחֲנֻכַּ֖ת הַמִּזְבֵּֽחַ׃",
            "וַיְהִ֗י הַמַּקְרִ֛יב בַּיּ֥וֹם הָרִאשׁ֖וֹן אֶת־קׇרְבָּנ֑וֹ נַחְשׁ֥וֹן בֶּן־עַמִּינָדָ֖ב לְמַטֵּ֥ה יְהוּדָֽה׃",
        ],
        'en': [
            "The princes also brought the dedication offering for the altar upon its being anointed. As the princes were presenting their offerings before the altar,",
            "the Lord said to Moses: Let them present their offerings for the dedication of the altar, one prince each day, one prince each day.",
            "The one who presented his offering on the first day was Nahshon son of Amminadab of the tribe of Judah.",
        ],
    },
}

# Apply cleaning
import json
cleaned = {}
for k, v in VERSE_TEXTS.items():
    cleaned[k] = {
        'he': [clean_he(s) for s in v['he']],
        'en': [clean_en(s) for s in v['en']],
    }

# Also save concatenated forms for primaryText use
for k, v in cleaned.items():
    v['he_full'] = ' '.join(v['he'])
    v['en_full'] = ' '.join(v['en'])

with open('/tmp/nechama/verses.json', 'w') as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

# Print quick samples
for k, v in cleaned.items():
    print(f'\n{k}:')
    print(f'  HE: {v["he_full"][:200]}')
    print(f'  EN: {v["en_full"][:200]}')
