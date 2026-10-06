# Theme 5 leaves: from Cain's line to the Flood (Gen 4:17–6:8)

Code: `research/scripts/bereshit_leaves/flood.py` (`leaf_1950`, `leaf_1969`, `leaf_1971`).
Check: `python3 research/scripts/check_leaves.py flood` → 9 sections, 88 steps, 0 failing checks (rerun after the harvest was regenerated, 2026-10-06).

All English is `en_basis: "ours"`. Labels (`label_he`) are typed; every card's Hebrew is a `cut()`
slice of its harvest item. "Whole" below means the whole item, no start/stop.

---

## 1950 (תש"י), sheet 161438: `fl-1950`, 30 steps

**Title:** `1950 · The Sons of Cain` (scan title line «בני קין»).

**Sections rendered:** א, ב, ג. One panel per section:
- §א `fl-1950`: Genesis 4:17–22.
- §ב `fl-1950-song`: Genesis 4:23–24, titled "Apology or Boast?".
- §ג `fl-1950-story`: Genesis 4:17–24, titled "The Story as a Whole".

Scan headers: §א «שאלות ודיוקים ברש"י»; §ב «כ"ג - כ"ד» (the digitizer's «התנצלות או התפארות?» isn't
hers); §ג has no header line of its own («ג. בכונת הספור כולו אומר המלבי"ם: …» runs on into the quote).

**§ב's title** comes from her framing sentence [16] («נחלקו המפרשים בכונת שיר זה, אם הם דברי התנצלות של
למך או דברי התפארות»). [16] is her prose, neither a source nor a question, so it has no card: the
library has no builder for her framing prose. Her two words carry the section as its title instead.

**Rashi on 4:23–24 is rendered once, in §ב.** §א's pointer «3) כ"ג דבריו לכל הפסוק / כ"ד " " "» and
§ב's pointer cover the same Rashi comments ([7]–[11] ≡ [19]–[22]). §ב's pointer is the more
precise one: it splits Rashi into her "1." and "2." with explicit start and stop points. So the Rashi
cards sit in §ב. §א's question (א) [12], on how "the two interpretations" agree and differ, follows
them there; rule 8 lets a question follow its source. Rashi [9] (ד"ה פצע) isn't rendered.

| Card | Type | [i] | Slice |
|---|---|---|---|
| `fl-1950-intro` | narration | — | — |
| `fl-1950-rashi-17` | Rashi | [1] | whole |
| `fl-1950-q-a0` | question | [2] | whole |
| `fl-1950-rashi-20` | Rashi | [3] | whole |
| `fl-1950-q-a1` | question (א) | [4] | whole |
| `fl-1950-q-a2` | question (ב) | [5] | whole |
| `fl-1950-q-a3` | question (ג) | [6] | whole («בפרושו הראשון», per the scan; triage `use: scan`) |
| `fl-1950-b-intro` | narration | — | — |
| `fl-1950-q-b0` | question | [17] | whole («עיין בדברי המפרשים האלה וסדרם לקבוצות:») |
| `fl-1950-saadia` | R. Saadia Gaon, Sefer ha-Galui | [18] | start «הכוונה בזה» (skips her label) |
| `fl-1950-rashi-23a` | Rashi | [19] | whole |
| `fl-1950-rashi-23b` | Rashi | [20] | whole |
| `fl-1950-rashi-24a` | Rashi | **[10]** (§א) | whole: see below |
| `fl-1950-rashi-24b` | Rashi | [21] | whole (it already ends at her stop «…דרש ר' תנחומא») |
| `fl-1950-rashi-24c` | Rashi | [22] | start «ומדרש בראשית רבה» (her «החל מן ומדרש בראשית רבה») |
| `fl-1950-q-a4` | question (א) | [12] | whole |
| `fl-1950-ibn-ezra` | Ibn Ezra | [24] | start «והטעם כאשר אמרו חכמינו» (her start; no stop) |
| `fl-1950-ramban-1` | Ramban | [26] | start «אבל ענין למך», stop «ישמע תפלתו» (hers) |
| `fl-1950-ramban-2` | Ramban | [27] | start «אבל הנראה בעיני» (hers; no stop) |
| `fl-1950-ralbag` | Ralbag | [28] | whole |
| `fl-1950-sforno-23` | Sforno | [29] | whole (her «דבריו לכל פסוק כ"ג») |
| `fl-1950-sforno-24` | Sforno | [30] | whole (her «כל פ' כ"ד») |
| `fl-1950-malbim` | Malbim | [31] | whole |
| `fl-1950-q-b1` | question | [32] | whole |
| `fl-1950-q-b2` | question | [33] | whole |
| `fl-1950-g-intro` | narration | — | — |
| `fl-1950-malbim-story` | Malbim | [35] | whole, including her lead-in «בכונת הספור כולו אומר המלבי"ם:» (the 1963 Benno Jacob precedent) |
| `fl-1950-cassuto` | Cassuto | [36] | whole, including her lead-in «והשוה לדבריו דברי קאסוטו…» |
| `fl-1950-q-g1` | question | [37] | whole |
| `fl-1950-q-g2` | question | [38] | whole |

**Rashi 4:24:1 cites §א's item.** Her §ב pointer begins at ד"ה כי שבעתים (Rashi 4:24:1, «קין שהרג
מזיד…») and runs to «…דרש ר' תנחומא». §ב's digitization starts at ד"ה שבעים ושבעה, so it lacks
4:24:1 (scan check, "Sources she named that the digitization lacks"). The same Rashi text is
digitized in §א as [10], so that card cites [10].

**Questions omitted:**
- §א (ב) [13] («כידוע אין רש"י מביא שני פרושים…»): `publish: false`, because the item carries a
  cross-reference to another gilayon («השוה שאלה זו גיליון תולדות תש"ד ב'»). Omitted whole, since
  `item()` refuses it.

**Open triage item [23], settled.** Her Ibn Ezra pointer reads, in the scan, «ראב"ע כ"[?] החל מן
"והטעם כאשר אמרו חכמינו"». The digitizer printed «ראב"ע, פסוק כ"א:».
- Fetched `https://www.sefaria.org/api/v3/texts/Ibn_Ezra_on_Genesis.4` (Piotrkow 1907–1911).
- Her start phrase occurs **once** in Ibn Ezra on chapter 4, in the comment on **4:23**: «…וכן ואתחנן
  (דברים ג כג) **והטעם כאשר אמרו חז"ל** כי עדה וצלה נמנעו…». Piotrkow abbreviates חז"ל where
  she, and harvest [24], have «חכמינו».
- There is no Ibn Ezra comment on 4:21 that matches. The 4:21 comment is «כנור ועוגב. מיני כלי
  נגינות…».
- So the illegible verse number is כ"ג. The digitizer's «כ"א» is a misreading, and harvest [24]
  (`Ibn Ezra on Genesis 4:23:1`) is the passage she meant.
- [24] is quoted from her start phrase. [23] itself is only a label and isn't quoted (its triage
  stays `open` in `triage.json`, which this stage doesn't touch).

**NOT-IN-SCAN source not quoted: [25]**, Ibn Ezra «ואם עד שבעתים יקם קין…». She gives no separate
pointer, and no question in §ב names Ibn Ezra, so rule 6 bars it. Two facts for Lev to weigh:
- her pointer has no stop («החל מן…» only);
- in Sefaria's Piotrkow text, [25] is the *continuation of the same comment* (4:23:2), not a new
  comment.

She may well have meant it to run on. If so, it can be added as a second Ibn Ezra card.

**Not quoted: the verse [15]** (the panel shows it).

**Scan readings the harvest keeps (quoted as the harvest has them):**
- Saadia [18]: the harvest has «ולא ילד **הוא** הלא»; the scan has no «הוא».
- Ralbag [28]: the harvest has «כי **ב**כל דור המבול»; the scan has «כי כל דור המבול». Our English,
  "in all the generation," reads the same either way.

**Translation choices worth a second look:**
- Sforno [29]: the harvest has digitizer slips: «חבלתי **בצמי** ממש שהיה הרוג **אביו**» and
  «**במצמי**». Sefaria's Sforno reads «בעצמי … שהיה ההרוג **אבי**» and «בעצמי». Translated by the
  canonical sense: "I have truly wounded myself, for the one slain was my father."
- Malbim [35]: the harvest reads «ויגזרו משפט וצדק»; Sefaria's Malbim on 4:23 reads «ויגזול».
  Translated "they will rob justice and righteousness."
- Malbim [31]: «כי איש אחד ועשה לי פצע» → "For a man [came] and dealt me a wound" (the bracket
  covers the stray ו).
- Rashi [20]: «בתמיה» → "[This is read] as a question."
- Q (א) [12], moved into §ב after Saadia (who also gives two readings), carries an editorial
  bracket in English only: "a. In what are [Rashi's] two interpretations alike…". Her Hebrew is unchanged.
- Ibn Ezra [24]: «שיהיו שבועיים לקין» → "lest they be the seventh [generation] from Cain"
  (Piotrkow «שביעיים»).
- Saadia: her label is «רב סעדיא גאון ספר הגלוי», so `label_en` is "R. Saadia Gaon, Sefer ha-Galui".
- Her lettered questions (א)(ב)(ג) are rendered "a." "b." "c."; numbered ones "1." "2.".

---

## 1969 (תשכ"ט), sheet 160469: `fl-1969`, 29 steps

**Title:** `1969 · Where the Story Ends`.

**Sections rendered:** א, ג, ד. ב is out (pack §7).
- §א `fl-1969` and §ג `fl-1969-name` ("Calling on the Name") share one panel: Genesis 4:25–26, 6:5–8.
  That's the last verses of chapter 4 and the last verses of the parasha, the two endings her §א asks
  about; 4:26 also carries §ג.
- §ד `fl-1969-enoch` ("Enoch Walked with God") moves to a new panel, Genesis 5:23–24. 5:22 is left out
  because its «ויתהלך חנוך את האלהים» would light up twice.
- No image (decided).

**Scan headers:**
- §א is «שאלות מבנה» (a structure question). The digitizer's «קין והבל» isn't hers. The section title
  is a content title, per the 1963 practice; her header is recorded here.
- §ג is «ד' כ"ו אז הוחל לקרא בשם ה'».
- §ד is «ויתהלך חנוך את האלקים ואיננו כי לקח אותו אלוקים».

**Not quoted:** [0], the opening cross-reference to the 1950 and 1951 gilyonot (`publish: false`);
the verses [15], [30].

| Card | Type | [i] | Slice |
|---|---|---|---|
| `fl-1969-intro` | narration | — | — |
| `fl-1969-cassuto-div` | Cassuto | [2] | whole (her description of his division) |
| `fl-1969-cassuto-end` | Cassuto | [6] | whole (her lead-in «לפסקה אחרונה … הוא מעיר: (במהדורה רביעית עמ' 127).» + the quote) |
| `fl-1969-q-a1`…`q-a4` | questions 1–4 | [7]–[10] | whole |
| `fl-1969-g-intro` | narration | — | — |
| `fl-1969-br` | Bereshit Rabbah | [16] | whole |
| `fl-1969-q-g1` | question 1 | [23] | whole (moved up to follow the midrash it asks about) |
| `fl-1969-rashi` | Rashi | [17] | whole |
| `fl-1969-q-g2` | question 2 | [24] | whole (moved up to follow the Rashi it asks about; the regenerated harvest reads «ברלינר», the digitization's reading, with no checker mark) |
| `fl-1969-ibn-ezra` | Ibn Ezra | [18] | whole |
| `fl-1969-bekhor-shor` | R. Yosef Bekhor Shor | [19] | whole |
| `fl-1969-wessely` | R. Naftali Hirz Wessely, Imrei Shefer | [20] | start «...ולדעתי» (after her label) |
| `fl-1969-shadal` | Shadal, HaMishtadel | [21] | whole |
| `fl-1969-hirsch` | R. Samson Raphael Hirsch | [22] | start «...(אחרי הביאו» (keeps her note "after citing Rashi's interpretation", which "this interpretation too" depends on) |
| `fl-1969-q-g3`…`q-g6` | questions 3–6 | [25]–[28] | whole |
| `fl-1969-d-intro` | narration | — | — |
| `fl-1969-br-25` | Bereshit Rabbah | [31] | whole (keeps her footnote mark `*`) |
| `fl-1969-kings` | II Kings 2:3 | [37] | whole: her footnote to the midrash, placed where the scan prints it, right after the midrash |
| `fl-1969-rashi-24a` | Rashi | [32] | start «ד"ה ויתהלך חנוך» (after the label «רש"י:») |
| `fl-1969-rashi-24b` | Rashi | [33] | whole: **Sefaria tags it Bereshit Rabbah 25:1**, but the scan (a ditto mark under רש"י) and the text are Rashi on 5:24, ד"ה כי לקח אותו. Labeled Rashi, `ref` "Rashi on Genesis 5:24" |
| `fl-1969-q-d1`…`q-d3` | questions 1–3 | [34]–[36] | whole |

**Bereshit Rabbah 23:7 [16] is rendered in §ג** even though the assignment listed only the
commentators. Her Q1 asks how the midrash reads «הוחל» as rebellion, and her Q3 asks who follows
R. Acha, so the questions need it.

**§ג source order is hers**: BR, Rashi, Ibn Ezra, Bekhor Shor, Wessely, Shadal, Hirsch. Her Q4's
"the last three commentators" depends on this order.

**§א questions are kept as questions**:
- 1–3 ask about the endings of the two units and their "something like the opening" and "good
  note";
- 4 asks why Cassuto, with the sedra division and against most scholars, keeps 6:5–8 with "The Book
  of the Generations of Adam".

No card states an answer. Q1's highlight marks the two closing verses she names, 4:26 and 6:8; Q4's
highlight marks 6:5–8.

**Questions omitted:** none. (The first draft omitted Q2 [24], whose harvest text carried `[?]` around
the overtyped name «ב[?]לינר[?]». The regenerated harvest keeps the digitization's «ברלינר», so it's
quoted, translated "Berliner".)

**Translation choices worth a second look:**
- [2]: the English ends with an editorial bracket, "[5:1–32; 6:1–4; 6:5–8]". Her three "matters"
  are separate one-line items [3]–[5] («ה', א'-ל"ב», «ו', א'-ד'», «ו', ה'-ח'»), and a card can quote only
  one item. Her Hebrew on the card is unchanged and ends at «לשלש "ענינים":». Same treatment as the
  1963 bracket in question א.
- Q1 [34] says «ר' איבו» («R. Aibo»), but in the midrash R. Abbahu gives the answer that R. Tanchuma
  praises. Translated as she wrote it, "R. Aibo". The midrash card has R. Aibo's opening and R. Abbahu's
  answer, both as the text has them.
- [31]: the harvest has the digitization's «אייבו»; her question has «איבו» (scan). Both are
  "Aibo".
- Rashi [32]: «וזהו ששינה הכתוב במיתתו לכתוב "ואיננו" בעולם, למלאות שנותיו» → "writing 'and he was
  not': he was not in the world to fill out his years."
- Bereshit Rabbah [16]: «אתם עשיתם עצמכם עבודת כוכבים וקראתם לשמכם» → "You have made yourselves into
  idols and called [them] by your own name."
- Q6 [28] names Rashbam and Ibn Caspi. Neither is on the sheet, but the question asks only about
  Ibn Ezra's weakness, so it's kept.

---

## 1971 (תשל"א), sheet 162069: `fl-1971`, 29 steps

**Title:** `1971 · The Sons of God` (scan masthead «בני האלוהים»).

**Sections rendered:** א, ב, ג, all on one panel, Genesis 6:1–4.
- §א `fl-1971`: the midrash.
- §ב `fl-1971-who`: "Who Are the 'Sons of God'?".
- §ג `fl-1971-yadon`: "'My Spirit Shall Not Abide'".

**Scan headers:**
- §א: «ויראו בני האלוהים את בנות האדם» (digitizer: «מדברי המדרש»).
- §ב: the whole of 6:2 (digitizer: «"בני האלוהים"»).
- §ג: «ג'. לא ידון רוחי באדם לעולם בשגם הוא בשר» (digitizer: «השוואת מפרשים»).

**Not quoted:** the verses [1], [9], [20].

| Card | Type | [i] | Slice |
|---|---|---|---|
| `fl-1971-intro` | narration | — | — |
| `fl-1971-br` | Bereshit Rabbah | [2] | whole |
| `fl-1971-q-a1`…`q-a5` | questions 1–5 | [3]–[7] | whole |
| `fl-1971-b-intro` | narration | — | — |
| `fl-1971-sifrei` | Sifrei | [10] | start «"ויראו בני האלוהים"» (after her label «ספרי בהעלותך י"א ו':»). The harvest has `kind: question`, but it's her Sifrei quotation, so it's rendered with `commentary()` |
| `fl-1971-radak-1` | Radak | [11] | whole |
| `fl-1971-radak-2` | Radak | [12] | whole |
| `fl-1971-shadal` | Shadal | [13] | whole |
| `fl-1971-malbim` | Malbim | [14] | whole |
| `fl-1971-jacob` | Benno Jacob | [15] | start «ייתכן» (after her label) |
| `fl-1971-q-b1`, `q-b2` | questions 1–2 | [16], [17] | whole |
| `fl-1971-q-b3` | question 3 | [18] | stop «י"ז-כ"ד»: see below |
| `fl-1971-g-intro` | narration | — | — |
| `fl-1971-mishnah` | Mishnah Sanhedrin | [21] | whole |
| `fl-1971-gemara` | Gemara, Sanhedrin | [22] | whole |
| `fl-1971-br-26` | Bereshit Rabbah | [23] | whole |
| `fl-1971-rashi-1`…`rashi-3` | Rashi | [24]–[26] | whole |
| `fl-1971-q-g1`…`q-g5` | questions 1–5 | [27]–[31] | whole |

**Urbach** appears only inside her §א Q3 [5]. Its Hebrew keeps the digitizers' subtitle «חז"ל: אמונות
ודעות» and «כותב» (triage `editorial`). The English gives the book's English title, *The Sages: Their
Concepts and Beliefs*.

**Questions omitted:** none. §ב Q3 [18] is quoted through «ד' י"ז-כ"ד» only. Its tail, «ועיין גליון
בראשית תש"י שאלות ב, ג, ביחוד דברי הרלב"ג ודברי המלבי"ם שם!», is a cross-reference to another gilayon
(the 1950 leaf above). It's cut, as 1963 cut its pointer to the teacher's guide.

**Scan vs harvest, «בל תדרוש»:** in Bereshit Rabbah 26:6 [23], the scan reads «אמר בלבו **בל** תדרוש»
and the harvest (digitization) has «**לא** תדרוש». As instructed, the harvest is authoritative for
what's quoted. The card has «לא תדרוש», translated "You will not call to account". Ps 10:13 itself
reads «לא תדרש», so the harvest agrees with the verse.

**Translation choices worth a second look:**
- Benno Jacob [15]: she cites «(תהל' ע"ח)», but the verse quoted is Psalms 82:6–7. The English keeps
  her "Psalms 78" and adds "[82:6–7]".
- Bereshit Rabbah [2]: the Aramaic proverb and her glosses: "'The priests have stolen the god — who
  will swear by it (= who will swear by it, by the idol), or who will offer' (= or who will bring it
  an offering)." Her Q5 asks the student to punctuate this proverb, and any English already
  punctuates it, choosing a reading: check that ours ("who will swear by it, or who will offer")
  doesn't pre-empt her question.
- Sifrei [10]: «ומענים אותן» → "and violate them".
- Malbim [14]: «ידוע ביקורת העמים הקדמונים, שהיו מאמינים…» → "It is known from the study of the ancient
  peoples that they believed…" (ביקורת as inquiry, not criticism).
- Malbim [14]: «והיו מהבילים» → "they would spin fables"; «עם אנשים שההבילו עליהם, שהם בני אלוהים» →
  "with men who deluded them into thinking that they were sons of gods". Her scan underlines
  «מהבילים». The underline isn't reproduced, because no question of hers asks about it.
- Bereshit Rabbah [23]: «רבי אומר: "ויאמר" דור המבול לה': "לא ידון!"» → "Rabbi says: 'And [he]
  said' — the generation of the Flood said to the Lord: 'Lo yadon!' [He will not judge!]".
- The panel's English is JPS ("divine beings", "My breath shall not abide"). The cards translate the
  sources' own readings ("sons of God", "My spirit").

---

## Gaps found (not fixed here)

- **Library:** no builder for her own framing prose that is neither a source nor a question (1950 [16]).
  No card can quote several consecutive items (1969 [2]+[3]–[5]).
- **Harvest (fixed upstream during drafting):** the checker's `[?]` markers sat inside quotable text,
  in 1969 [24] mid-question and in 1950 [18]'s label. The regenerated harvest drops them, and
  1969 Q2 is now quoted.
- **Verse cache:** `bereshit-verses.json` 5:1 Hebrew carries a leaked note,
  «סֵפֶר*(בספרי תימן סֵפֶר בסמ״ך גדולה)», although `meta.footnote_suspects` is empty. 1969 avoids 5:1
  for this reason.
