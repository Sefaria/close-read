# Theme 3 — Never again (Gen 8:20–9:17): paper trail

Module: `research/scripts/noach_leaves/covenant.py` (prefix `cv-`). Check:
`python3 research/scripts/check_leaves.py noach covenant` → 9 sections, 101 steps, 0 failing checks.
All English is ours (`en_basis: "ours"`); no card uses Sefaria's or Nataf's English.

---

## 1946 (תש"ו), sheet 161548 — 36 steps

Harvest `noach-harvest/covenant/1946.json`; scan check `noach-scancheck/161548-1946.md`.

**Sections rendered:** all three of hers: א (Rashi questions), ב (structure and style), ג (8:21).
§א is split over two panels by verse.

| Panel section | Panel | Her section |
|---|---|---|
| `cv-1946` "1946 · Coming Out of the Ark" | Genesis 8:16-19 | §א, Rashi 8:16 and 8:19 |
| `cv-1946-b` "“Never Again”" | Genesis 8:21; 9:11 | §א, Rashi 8:21, the curse of the ground, Tzeidah LaDerekh (9:11 is in the panel for her «ולא יכרת… ולא יהיה») |
| `cv-1946-c` "Every Living Thing" | Genesis 7:14; 8:16-17, 19 | §ב |
| `cv-1946-d` "“Evil from Youth”" | Genesis 6:5; 8:21 | §ג (6:5 for Abarbanel's second question and her Q7) |

**Cards → harvest:**

| Step | [i] | Slice | Note |
|---|---|---|---|
| rashi-16 | 1 | whole | bare pointer in scan; digitizer's text |
| q-a1 | 2 | whole | «מה קשה לו?» |
| gen-6-18 | 4 | whole | her «והשוה ו' י"ח; ז' ז'»; our English keeps the Hebrew order (you, sons, wife), which JPS doesn't |
| gen-7-7 | 5 | whole | as above |
| rashi-19 | 6 | whole | |
| q-a2 | 7 | whole | |
| rashi-21 | 8 | whole | |
| q-a3 | 9 | whole | |
| rashi-6-13 | 10 | start «ד"ה את הארץ» | her pointer is the whole Rashi on 6:13 with no stop; the card quotes only the comment on «את הארץ» (the one about the ground) |
| ibn-ezra | 11 | start «וטעם לא אוסיף» | her start point «החל מן וטעם לא אוסיף» |
| q-a4 | 12 | whole | digitized wording (triage: form only) |
| q-a5 | 13 | whole | Tzeidah LaDerekh's question, as she frames it (scan form, no «5.») |
| q-a6 | 14 | whole | «תרץ קושיתו.» |
| q-b1 | 17 | whole | her Q1 in the scan's wording (triage: use scan) |
| gen-7-8 | 16 | whole | her «(ועי' גם ז' ח')» inside Q1 |
| q-b2 | 18 | whole | |
| abarbanel-a | 23 | whole | keeps the lead-in «אברבנאל, מקשה לפסוק זה שתי שאלות:» once |
| abarbanel-b | 24 | start «ב. למה נתן טעם» | drops the digitizer's second copy of the lead-in |
| akeidah-a | 27 | start «בהביא ה' המבול» | drops the label line «עקדת יצחק:» (it's in the card label) |
| akeidah-b | 28 | start «והשני מצד» | drops the digitizer's second «עקדת יצחק:» label |
| hirsch | 29 | start «המלים» | label: her «רש"ר הירש, (תרגום מגרמנית)»; the parenthetical is in the scan, so it's hers, but it isn't shown |
| q-c6 | 37 | whole | Q6 in the scan's wording; follows the Hirsch card it asks about (see "Changes after the scan-wording fixes") |
| some | 31 | whole | label «יש מפרשים» from her [30] |
| q-c1 … q-c5 | 32–36 | whole | Q2 [33] and Q3 [34] in the scan's wording |
| q-c7 | 38 | whole | |
| ibn-ezra-ex | 39 | whole | see "stop points" below |
| q-c8 | 40 | whole | Q8 restored from the scan |
| q-c9 | 41 | whole | |

**Not quoted:** [3] «והשוה» (her connective; the two verse cards stand in for it), [19] 8:17 and [20]
7:14 (both in the panel), [22] 8:21 (the panel), [25] «(שאלה זו נשאלת גם במפרשים אחרים)» and [26]
«והנה אחדות מן התשובות…» (her framing), [30] (used as the label).

**Questions omitted:** none. (Q6 [37] was first held back: triage took her wording from the scan,
but the harvest still had the digitized wording. The harvest now carries the scan wording via an
`overrides.json` `replace`, and Q6 is in.)

**Stop points:**
- Ibn Ezra on Exodus 13:17 ([39]): her stop «עד "ועל דעתי"» isn't in the digitized text. Sefaria's
  text (Piotrkow) goes on «…כי רכב ברזל לו (יהושע יז יח) ולפי דעתי אין צורך…», and the digitized item
  ends exactly before «ולפי דעתי אין צורך», so the item is her excerpt as she marked it. Quoted whole.

**Source-text differences I quoted around, or quoted as they stand (not her words):**
- [24] digitized «ואיך היה הדבר אחד סיבה» vs scan «ואיך יהיה דבר אחד סבה». The English ("How could one
  thing be the cause of two opposites?") fits both readings.
- [28] digitized «הוא היה ה"ריח הניחוח"» vs scan «הוא הוא ה"ריח ניחוח"». The English ("was the 'pleasing
  odor'") fits both.
- [29] Hirsch: digitized «(כנגד הטבע, כי הנוער…)» vs scan «(שזהו[?] נגד הטבע, כי נוער…)»; same sense.

**Translation choices worth a second look:**
- [1] «איש ואשתו» → "man and his wife together" ("together" makes Rashi's point explicit).
- [6] «קיבלו עליהם על מנת לידבק במינן» → "they took it upon themselves to keep to their own kind".
- [8] Isaiah 54:9 completed in brackets.
- [23] «למה לא חשב ה' כזאת בתחילה עד דור המבול, ולא יענישם…» → "Why did the Lord not consider this at
  the outset, until the generation of the Flood, and not punish them…".
- [28] «רוח נכון» → "a steadfast spirit" (Ps 51:12).
- [39] «כי» rendered "although" in Ibn Ezra's examples, since that's his claim; the lemma is given as
  "ki karov".
- [13] the 9:11 quotations follow JPS ("never again shall be cut off", "never again shall there be"),
  so they match the lit phrases.

---

## 1951 (תשי"א), sheet 161581 — 31 steps

Harvest `noach-harvest/covenant/1951.json`; scan check `noach-scancheck/161581-1951.md`.

**Sections rendered:** all four: א (Cassuto, «אתכם» / «חתכם»; the pronouns), ב (the bow), ג
(«בענני ענן»), ד («וראיתיה»).

| Panel section | Panel | Her sections |
|---|---|---|
| `cv-1951` "1951 · The Sign of the Covenant" | Genesis 9:2, 7-11 | §א (9:2 for «וחתכם»; 9:7 «ואתם») |
| `cv-1951-b` "The Bow in the Clouds" | Genesis 9:12-16 | §ב, §ג, §ד (9:12 «אשר אני נותן» vs 9:13 «נתתי» for Ramban's proof) |

**Cards → harvest:**

| Step | [i] | Slice | Note |
|---|---|---|---|
| q-a1 | 1 | whole | her Q1 with Cassuto's set-out lines. `cut()` collapses the layout into one line; the English marks his line breaks with " / ". All four «אתכם» phrases light. |
| cassuto | 2 | start «אולי» | drops her «ולכך הוא מעיר:» |
| q-a1b | 3 | whole | scan wording «של מלת» (triage) |
| q-a2 | 7 | whole | her Q2 sentence plus «כגון בר' א' כ"ח: "פרו ורבו..."» |
| gen-9-1 | 8 | whole | |
| gen-6-13 | 9 | whole | |
| gen-17-4 | 10 | whole | in the scan under «והשוה למקומנו:» (label lost in the digitization) |
| gen-17-9 | 11 | whole | |
| abarbanel | 14 | start «בענין» | drops «אברבנאל, שואל:» |
| q-b1, q-b2 | 15, 16 | whole | |
| ramban-a | 17 | stop «לכונן חצים עליו.» | |
| ramban-b | 17 | «ואנחנו על כרחנו» … «כי ברית שלום ביני וביניכם.» | |
| ramban-c | 17 | start «ואם תבקש» | to the end of the item |
| q-b3 | 'after 17' | whole | scan-only Q3 |
| q-b4, q-b5 | 18, 19 | whole | |
| radak-14 | 22 | whole | |
| q-c | 23 | stop «לפסוק ההוא» | drops only the pointer to her own Vayigash 1947 gilayon («שהובאו בגליון ויגש תש"ז שאלה ד.») |
| radak-15 | 26 | whole | |
| shadal | 27 | whole | her own sentence reporting Shadal, labeled Shadal (as 1943's Malbim) |
| gen-2-19, gen-2-3, ps-104 | 28–30 | whole | the three verses she quotes for Shadal |
| q-d1 … q-d3 | 31–33 | whole | |

**Not quoted:** [4] (pointer to her Beshalach 1948 gilayon), [5], [6] (9:7, 9:9: in the panel), [13], [21],
[25] (verses in the panel).

**Questions omitted:** none.

**Stop points:**
- Ramban 9:12 ([17]): her stop (in Q3) «עד "אבל יש לרבותינו"» isn't in the digitized text. Sefaria's
  Ramban continues «…הטעם באות שבה אחד הוא. אבל יש לרבותינו בפרשה הזאת סוד נעלם…», and the digitized
  item ends exactly before «אבל יש לרבותינו». So the item is her excerpt; quoted whole across three cards.

**Source-text differences:**
- [14] the digitization read «ומה אם כן אותה הברית הזה»; the scan has «אות הברית». The harvest now has
  the scan reading (`overrides.json` `replace`), and the English is "What, then, is this sign of the
  covenant…".
- [22] «סיבות» / scan «סבות»; [26] «דיברה» / scan «דברה»: spelling only.

**Translation choices worth a second look:**
- JPS flattens the pronouns her Q2 asks about: 9:7 «ואתם פרו ורבו» is "Be fertile, then, and increase",
  9:9 «ואני הנני» is "I now establish". The cards light those phrases anyway; our card English for
  17:4 and 17:9 keeps "As for Me" / "And as for you".
- Cassuto's layout in English (q-a1) is our line-by-line rendering of his lines.
- [14] «והוא, כי הקשת…» → "the point is that the bow…"; «במראיו» → "its colors".
- [17] «רגליו» → "its ends"; «יתר» → "string".
- [29] Genesis 2:3 «אשר ברא אלהים לעשות» → "Which God created, to make" (literal, for Shadal's point).

---

## 1964 (תשכ"ד), sheet 160639 — 34 steps

Harvest `noach-harvest/covenant/1964.json`; scan check `noach-scancheck/160639-1964.md`.

**Sections rendered:** א («טרף»), ב (Ibn Kaspi on «כי»), ג (youth of man and world), ד (does the earth
end?), in her order. Her unlettered last section (8:22 «לא ישבותו», Rashi) is outside the §7 design.

| Panel section | Panel | Her sections |
|---|---|---|
| `cv-1964` "1964 · The Dove and the Covenant" | Genesis 8:11 | §א |
| `cv-1964-b` "“Evil from Youth”" | Genesis 8:21 | §ב, §ג |
| `cv-1964-c` "“So Long as the Earth Endures”" | Genesis 8:22 | §ד |

**Cards → harvest:**

| Step | [i] | Slice | Note |
|---|---|---|---|
| rashi-a, rashi-b | 3, 4 | whole | |
| ramban-a | 5 | stop «למה שינה בכאן?» | |
| q-a1 | 6 | whole | |
| ramban-b | 5 | «וכן מדרשם» … «להתפרנס זה מזה.» | |
| q-a2 … q-a6 | 7–11 | whole | Q5 [10] in the digitizer's corrected «לו» (triage) |
| ramban-c | 5 | «ולשון בראשית רבה» … «היה טרף בפיה".» | Bereshit Rabbah and the Gemara (see below) |
| q-a8 | 13 | whole | |
| ramban-d | 5 | start «ופשוטו של מקרא» | includes her gloss «(כוונתו: …)», translated in parentheses; «נמצא מהם בזרות» per the triaged fix |
| q-a9, q-a10 | 14, 15 | whole | |
| kaspi-ki | 18 | start «נכון אצלי» | label her «אבן כספי, משנה כסף» |
| q-b | 19 | whole | |
| abarbanel-a | 22 | «והאופן השני» … «כנגד שבעת ימי בראשית.» | |
| abarbanel-b | 22 | «והנה האדם הפרט» … «שלא יפשע עוד כבראשונה.» | |
| abarbanel-c | 22 | «וזה עניין הברית» … «הפסד כללי כמוהם.» | |
| abarbanel-d | 22 | start «הנה התבהר» | |
| tedeschi | 23 | start «ד"ה מנעוריו» | label from her attribution «משה יצחק אשכנזי, טדסקי (תלמיד שד"ל) "הואיל משה"» |
| shadal | 24 | whole | |
| q-c1 … q-c4 | 25–28 | whole | |
| ibn-ezra | 31 | whole | |
| kaspi-end | 32 | start «ד"ה עוד» | drops the label line |
| q-d1, q-d2 | 33, 34 | whole | |

Abarbanel is shown in four slices so that her Q2's three resolutions (the world's youth; the lesson of the
Flood; the three heads) and Q4's "blessing in the lack of unity" each have a card to point at.

**Questions omitted:** §א Q7 ([12], «באיזו הוראה משתמש הרמב"ן כאן בבטוי "להתפרנס זה מזה"?»), for density.
It's a lexical point on a single phrase, and §א already has nine questions. Nothing else is omitted.

**Source-text slips:**
- Ramban [5]: the digitization read «אמר רק אבהו» for «אמר ר' אבהו». The harvest now has «ר' אבהו»
  (`overrides.json` `replace`), so ramban-c starts at «ולשון בראשית רבה» and shows the Bereshit Rabbah
  quotation («נח! מר מזה…»).
- Abarbanel [22]: the scan check reports the digitization cut off at «…משותפת כמו »; the harvest item
  carries the full tail through «…כי נעורי העולם כבר עברו.», so I quoted it. It reads «הנה התבהר» where
  the scan has «הנה התבאר», and «בזכות נוח» for the scan's «בזכות נח». Both are quoted as they stand;
  the English ("So it has become clear", "for Noah's merit") fits both readings. Worth a look.
- Tedeschi [23]: the citation «(שמואל א' י"ז ל"ב)» (scan possibly «י"ד[?]»); the quoted words are 1 Samuel
  17:33. The English gives "1 Samuel 17:32 [the words are in 17:33]", as 1942 did for Job.

**Translation choices worth a second look:**
- [3] the feminine forms Rashi cites are marked "[feminine]", since English can't show them.
- [5] «חזרת זכר היונים מנקבה לזכר» → "the doves' being switched from feminine to masculine".
- [5] «טרוף» in the plain-sense reading → "plucked [taruf]".
- [22] «שנות הבהלה» → "years of rashness"; «שני אלפים – תוהו» → "two thousand years of chaos".
- [32] «דעת המורה» → "the view of the Guide" (Maimonides' Guide).

---

## Changes after the scan-wording fixes (2026-10-12)

The coordinator applied three `overrides.json` `replace` fixes and re-harvested. These changes followed:
1. **1946 [37]** now has her scan wording. Q6 is restored as `cv-1946-q-c6`, right after the Hirsch card
   it asks about: "6. In what sense is the “ki” of “ki yetzer lev…” to be read, according to Hirsch?"
   The 1946 leaf is now 36 steps.
2. **1964 [5]** now reads «אמר ר' אבהו». `cv-1964-ramban-c` now starts at «ולשון בראשית רבה», which
   restores the Bereshit Rabbah lines: "And in the words of Bereshit Rabbah (33:6): R. Abbahu said… but it
   hinted a hint to him; it said to him: “Noah! Better bitter from under the hand of the Holy One, blessed
   be He, than sweet from under your hand.”"
3. **1951 [14]** now reads «אות הברית». The English of `cv-1951-abarbanel` is now "What, then, is this
   sign of the covenant that was made with Noah as an assurance?"
