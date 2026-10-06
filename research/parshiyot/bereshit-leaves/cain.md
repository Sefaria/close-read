# Cain and Abel (Gen 4:1–16): leaves 1942, 1956, 1958

Built by `research/scripts/bereshit_leaves/cain.py`. Checked with
`python3 research/scripts/check_leaves.py cain`: 10 sections, 82 steps, 0 failing checks
(1942: 25 steps · 1956: 30 · 1958: 27). This was re-checked against the regenerated harvest
(2026-10-06), which no longer writes doubtful scan readings into her text: where the scan
check had a `[?]`, the digitization's reading stands. Every commentary and question card slices a harvest item
verbatim. All English is ours (`en_basis: "ours"`), the brief's default. No card needed Sefaria's,
and most quotes are abridged or carry her framing.

**What the harvest regeneration changed in these leaves.** The first draft was built on a
harvest that kept the scan's `[?]` markers. That blocked 1942 §ב's two questions and forced
§ט's midrash into two slices around her gloss. In the regenerated harvest, the affected items
([7], [15], [32], [51] in 1942; [4], [19], [20], [24], [26] in 1956; [3], [4], [8] in 1958)
carry the **digitization's wording**, not the scan's. So the 1942 §ב questions are back. In
exchange, three 1942 items lose her scan wording: [7] reads «לפי כל אחד מהפרשנים הבאים», not her
list of four names; [32] drops her Ramban stop-pointer; and [51] reads «ר' איבו», «ר' חנינא בר
ר' יצחק», «העליונה», not her «ר' איבא», «ר' חננא בר יצחק», «העליונים». The scan-only 1956
question «(א) מה קשה לו[?]» still carries its mark, and `item()` now refuses it.

---

## 1942 (תש"ב) · sheet 161880 · `leaf_1942`, prefix `cn-1942`

**Sections rendered:** §ב (4:7), §ה (4:13), §ז (4:15), §ט (4:16). The panels are 4:5–7, then
4:13–15 (§ה and §ז together: Ramban [43] on 4:13 answers §ז), then 4:16.

**Leaf title:** "Sin Couches at the Door". Her prose line [6] («יש אומרים שפסוק זה הוא הקשה
ביותר בכל ספר בראשית») isn't a question and has no card type of its own. It isn't on screen; the
branch blurb can carry it.

**Slices and start/stop points:**
- §ב Ramban [10] is split at «ועל דעתי»: (a) his account of the others' readings, through
  «( ויקרא יט טו ).»; (b) his own reading. Both are his whole comment, in two cards.
- §ב Ramban on 49:3 [11] starts at «שיעור הפסוק הזה»: her lead-in «להבנת הרמב"ן עיין גם…» is a
  pointer, not a quote. The scan prints only the pointer, so the text is the digitizer's
  EXPANDED reading of where she pointed. 49:3 isn't in the verse cache, so both 49:3 cards light
  «שאת» in 4:7, after a narration that points at Jacob's words to Reuben.
- §ה Ramban [30]: her stop «עד למלים חרפת נעורי» is where the digitized item already ends, so the
  card is the whole item, with `stop='חרפת נעורי'` stated.
- §ב question 1 [7] ("…according to each of the following commentators?") leads the section,
  as on her sheet, because it introduces the sources. Question 2 [15] (Rashi and Sforno on
  «תשוקתו» / «בו») closes it, after Sforno. Both use the digitization's wording.
- §ה question [32] is one card, in the digitization's wording. Her stop-pointer («/ רמב"ן עד
  למלים חרפת נעורי"/», between its two sentences in the scan) isn't in it, but the Ramban card
  honors it.
- §ז her start points are honored: Ibn Ezra [42] from «ויש אומר, כי האות», Ramban [43] from
  «כי בעבור שאהיה נע ונד». Her question [39] is quoted whole, pointers included, and translated.
  Here it follows the three sources (in the scan it precedes them).
- §ז Rashi: [40] only. [41] (Rashi's «ס"א» variant) is the digitizer's choice; the scan says only
  «רש"י».
- §ט Bereshit Rabbah [51] is one card from «ויצא קין.» to the end. Her lead-in («ישנה מחלוקת
  במדרש בראשית רבה:») isn't shown; her parenthetical gloss on הפשיל is, translated as "(that is,
  …)". It's in the digitization's wording (R. Aibu, R. Chanina bar R. Yitzhak, «העליונה»), which
  matches the canonical names of Bereshit Rabbah 22:13. Her scan spellings («ר' איבא», «ר' חננא בר
  יצחק», «העליונים») were dropped in the regeneration, along with a doubtful letter in the same
  passage. The English follows the Hebrew on screen.
- §ט question [52] is a digitization MATCH, but the scan check couldn't read «לפשוטו» on the
  faded line. The digitized reading fits the question and is quoted; worth a look by a person.

**Questions omitted:** none. All five of her questions in §ב, §ה, §ז and §ט are rendered.

**NOT-IN-SCAN sources quoted:** none. (Every 1942 source is EXPANDED: she named it and the
digitizer supplied the text.)

**Translation choices to check:**
- Lemmas are rendered literally, not with JPS ("Surely, if you do well", not "if you do right"),
  since the commentators disagree about these words. In the questions, «גדול עוני מנשא» is
  transliterated ("gadol avoni mi-neso"), because JPS's "punishment" decides the dispute.
- Ibn Ezra [9] cites «( איוב י"ד טו )» for «כי אז תשא פניך ממום», which is Job 11:15; the English
  reads "(Job 14:15 [the verse is Job 11:15])".
- Ibn Ezra [31]: «העקב» is rendered "the consequence [of a deed]", and «אמתחת» (for אמתת) as "the
  truth".
- «כגונב דעת העליונה» is rendered "like one who deceives the One above".
- 1942 [7] «אם תיטיב – שאת» is transliterated ("im teitiv – se'et"), as is [15]'s «תשוקתו» / «בו».

---

## 1956 (תשט"ז) · sheet 161216 · `leaf_1956`, prefix `cn-1956`

**Sections rendered:** §א (4:8: Bereshit Rabbah on what the brothers fought about), §ב (Rashi,
chosen comments), §ג (4:7 again: Rashi, Onkelos, Malbim). The panels are 4:8, then 4:1, 7–8, 10,
then 4:5–7 (her §ג Q3 asks how the verse connects to verses 5–6).

**Slices:**
- §א Bereshit Rabbah [3] is split into its three views, which her Q1 asks about one by one:
  through the first «ויהרגהו"»; «ר' יהושע דסכנין» through the second «ויהרגהו"»; «יהודה בר' אמי»
  to the end. The Hebrew glosses of the Aramaic in parentheses are translated once, with the
  Aramaic.
- §ג: in the scan, [30] is «רש"י ד"ה הלא אם תטיב שאת: כתרגומו פרושו.», and [32]–[34] follow
  with ditto marks. The digitization files [30] as Genesis 4:7 and labels [32]–[34] «(תרגום
  אונקלוס:». **They are labeled Rashi here, by the scan.** Corroboration: Sefaria's Rashi on
  Genesis 4:7 has exactly these four comments as segments 1–4, and her Q4 asks about Rashi on
  «ואתה תמשל בו». [34] is sliced from «ד"ה ואתה», which drops the digitizer's label. [31] is
  genuinely Onkelos (scan «(תרגום אונקלוס: …»).
- §ג [32] and [33] repeat Rashi 4:7:2–3, which §ב quotes as [17] and [18], so they are omitted
  here.

**§ב, chosen (her numbering: Rashi 1, 5, 6, 7):**
- Rashi 1 (4:1, [7]) with (א) [8] and (ב) [9]. [9] uses the digitized «רש"י»: her «רש"ע» is a
  typo (triage `digitized`).
- Rashi 5 (4:7, [17], [18]) with (א) [19], (ב) [20], (ג) [21].
- Rashi 6 (4:8, [22]) with (א) [23] and (ב) [24]. [24] points back to §א's three views.
- Rashi 7 (4:10, [25]) with (ב) [26] and (ג) [27].

**Questions omitted:**
- Rashi 2 (4:2 «רועה צאן», [10]) and its question [11]: for density.
- Rashi 3 (4:3 «מפרי האדמה», [12]) and its question [13]: for density.
- Rashi 4 (4:4 «וישע», [14]), the Sefer HaZikaron emendation [15] and her question [16]: for
  density. It's a text-critical aside (Exodus 5 vs Isaiah 17).
- Rashi 7 (א), the scan-only «(א) מה קשה לו[?]» (`after 25`). The regenerated harvest still marks
  its smudged last word, and `item()` refuses marked items, so it can't be quoted. (ב) and (ג)
  stand without it.

Of her 13 §ב questions ([8], [9], [11], [13], [16], [19]–[21], [23], [24], `after 25`, [26], [27]), 9 are rendered.

**NOT-IN-SCAN sources quoted:** none.

**Translation choices to check:**
- Malbim [35] cites «( שמואל א' י"ג )» for «הנה שמוע מזבח טוב», which is 1 Samuel 15:22. The
  English reads "(1 Samuel 13 [the verse is 1 Samuel 15:22])". «העוז והמשוה» is rendered "the
  strength and the equal power". «המשוה» is uncertain; the canonical text should be checked.
- Rashi 4:10: «דמי» is glossed "[demei, literally 'bloods']", the only gloss added in this leaf.
- Rashi [22]'s lemma is the digitizer's «ואמר קין» (scan «ויאמר קין»), translated "And Cain
  said" either way.
- The §ב sub-question prefixes are the digitization's «א.» / «ב.» / «ג.» (her scan has «(א)»…);
  the English uses "a." / "b." / "c." to match the Hebrew on screen.
- [24] «(ע' שאלה א)» is rendered "(see question A)". Her §א is headed «שאלה כללית לפרקנו», so
  "question א" is §א.

---

## 1958 (תשי"ח) · sheet 161141 · `leaf_1958`, prefix `cn-1958`

**Sections rendered:** §א (structure: her Cassuto quotes), §ב (comparing verses), §ד (the curse:
Rashi vs Ramban). The panels are 4:2–5 (the chiasm of her Q1), then 4:10–11 (Cassuto's
parallel), then a **side-by-side comparison panel** for §ב (her table: chapter 4, 9–10, on the
right; chapter 3, 9 and 13, on the left, as she set it), then 4:11–12.

**Slices:**
- §א [3] (kind "question" in the harvest: «2. קאסוטו, תורת התעודות, 80-90: "…"») is shown as a
  Cassuto commentary card, `start='כשבא'`, `stop='מלה אחרת'`. Her underline on «בהקבלה» (scan
  check) is reproduced, as `<u>` in Hebrew and English. Label: "Cassuto, Torat HaTe'udot", her
  attribution. No `ref`, so there's no Sefaria link.
- §א her item 3: [6] (her lead-in) and [7] (Cassuto's printed layout of 4:10–11) are **not
  shown**. `cut()` flattens [7]'s line breaks, and the layout *is* its content. Instead, the
  4:10–11 panel lights the four line-endings, «קול דמי אחיך» / «צעקים אלי מן האדמה» / «ארור אתה
  מן האדמה» / «לקחת את דמי אחיך», as Cassuto's paragraph [8] (from «סידרתי», after «ואלה דבריו
  (עמוד 124):») names them. Label: "Cassuto, From Adam to Noah" (her «בספרו "מאדם עד נח"»).
- §ב Rashi [16] (two comments printed side by side) is two cards: 4:9 (`stop='וחטאתי לך'`) and
  3:9 (`start='ד"ה איכה'`). Her Q3 is [15] «השווה את דברי רש"י…» + the two Rashis + [17] «הסבר את
  השוני…», shown in that order.
- §ד Ramban [28] starts after her note «רמב"ן, (אחרי הביאו דברי רש"י הנ"ל):», at «ארור אתה מן
  האדמה: ואיננו נכון». It is split where her own questions divide it: (1) through «בהיותו עובד
  אותה...»; (2) «וייתכן שאיררו» … «עונש הרוצחים גלות.» (her Q4 names it); (3) «בטעם "אשר פצתה» to
  the end (her Q5 names it «וטעם "אשר פצתה את פיה"»; the scan's first letter is overtyped, and the
  harvest has «בטעם»). Her underline («ואמר כן כנגד אומנותו, כי הוא היה עובד אדמה, והנה ארר
  מעשיו») is reproduced, since Q3 asks about "the words marked with a line". **«אומנותו» is the
  scan's reading, confirmed in Sefaria's Ramban;** the digitization had «אמונתו».
- §ד questions are placed after the part each asks about: Q1–Q3 after part 1, Q4 after part 2, Q5
  after part 3, Q6 last. Her numbering order is unchanged.

**Questions omitted:** none of §א, §ב or §ד's questions. Not shown: [19] «העזר במקומות הבאים:»
and the list [20] (see the open item below). [19] means nothing without the list.

**NOT-IN-SCAN sources quoted:** none.

### Open triage item [20], settled (and still not quoted)

**What her list says.** Her §ב Q4 [18] asks why both places use «איה» and not «איפה»; [20] lists
the verses to use. Every verse was fetched from Sefaria (`/api/v3/texts/<Ref>`, 2026-10-06):

| Her citation (scan) | Verse | MT text | Her quote vs MT |
|---|---|---|---|
| ב"ר ל"ז "איפה הם רועים" | **Genesis 37:16** | אֵיפֹה הֵם רֹעִים | matches. «ב"ר» is her abbreviation for the book of Bereshit, not Bereshit Rabbah (BR 37 has no such line; Gen 37:16 is exact). Her «רועים» is plene. |
| רות ב' י"ט | Ruth 2:19 | אֵיפֹה לִקַּטְתְּ הַיּוֹם | matches |
| שמואל א' י"ט כ"ב | 1 Samuel 19:22 | אֵיפֹה שְׁמוּאֵל וְדָוִד | matches |
| איוב ל"ח ד' | Job 38:4 | אֵיפֹה הָיִיתָ בְּיׇסְדִי־אָרֶץ | matches |
| שופטים ו' (no verse) | **Judges 6:13** | וְאַיֵּה כׇל־נִפְלְאֹתָיו אֲשֶׁר סִפְּרוּ־לָנוּ אֲבוֹתֵינוּ | matches. The digitizer's added «י"ג» is right (an editorial addition). |
| מלכים ב' י"ח | **2 Kings 18:34** | אַיֵּה אֱלֹהֵי חֲמָת וְאַרְפָּד | matches (also Isaiah 36:19) |
| מלכים ב' ב' "איה ה' אלוקי אדוני אליהו" | **2 Kings 2:14** | אַיֵּה יְהֹוָה אֱלֹהֵי אֵלִיָּהוּ | **her slip:** MT has no «אדוני» |
| ירמיהו ב' כ"ח "…יקומו ויושיעוך" | Jeremiah 2:28 | יָקוּמוּ אִם־יוֹשִׁיעוּךָ | **her slip:** MT reads «אם יושיעוך» |

**Settled:** eight verses, four with «איפה» (Gen 37:16, Ruth 2:19, 1 Sam 19:22, Job 38:4) and
four with «איה» (Judg 6:13, 2 Kgs 18:34, 2 Kgs 2:14, Jer 2:28). All her citations point to the
right verses. Two of her quotations misquote MT (2 Kgs 2:14 «אדוני»; Jer 2:28 «ויושיעוך»), and
the digitizer silently corrected both. **Proposed triage decision for 161141 [20]: `use:
digitized`.** The digitizer's text gives her verses correctly, and its fuller citations (Genesis
37, Judges 6:13) are editorial additions; her two slips get recorded in `why`.

**Why it's still not quoted:** `item()` refuses any item whose triage is `open`, and changing
`triage.json` (then re-running the harvester, which rewrites every theme) is outside this task.
Once the decision above is applied, [19]+[20] can follow [18] as a question card. Its Hebrew is
the digitized pointed text, which has newlines that `cut()` will flatten.

**Translation choices to check:**
- Cassuto [3]: «בעתיד מהופך לעבר» → "in the future converted to past" (the vav-consecutive
  imperfect).
- Rashi 4:11 lemma «מן האדמה» is transliterated ("Min ha-adamah"), since her Q1 asks about the
  word «מן».
- Ramban part 3: «כי תיענש בה ובכל אשר תכסה בה» is read as feminine, with the ground as subject, like the verbs before it: "for it will be punished for it, and in all that it covers in it".
- Her Q4 [18], «בלשון 'איה' ולא בלשון 'איפה'» → "with the word 'ayeh' and not with the word
  'eifo'".
- Titles are reviewer's calls: the 1958 leaf title "“Where Is Your Brother Abel?”" opens on the
  4:2–5 panel; 1956 §ב is titled "Rashi, from Cain's Birth to Abel's Blood".
- The 1958 §ב comparison panel passed the structural tests but has not been seen in a browser
  (`check_leaves.py` doesn't run `test_render.py`).

---

## Every card → harvest item

### 1942

| Card | Type | [i] | Slice (start … stop) |
|---|---|---|---|
| `cn-1942-intro` | narration | — | — |
| `cn-1942-q-b1` | question | 7 | «1. מה פירוש … אחד מהפרשנים הבאים?» |
| `cn-1942-rashi` | commentary · Rashi | 8 | «ד"ה הלוא אם … תיטיב: כתרגומו פירושו.» |
| `cn-1942-ibn-ezra` | commentary · Ibn Ezra | 9 | «ד"ה הלוא: ופירוש … (איוב י"ד טו).» |
| `cn-1942-ramban-a` | commentary · Ramban | 10 | «ד"ה הלא אם … (ויקרא יט טו).» |
| `cn-1942-ramban-b` | commentary · Ramban | 10 | «ועל דעתי, "אם … שירצה, ויסלח לו.» |
| `cn-1942-reuben` | narration | — | — |
| `cn-1942-ramban-49` | commentary · Ramban | 11 | «שיעור הפסוק הזה … (ישעיה מב כה).» |
| `cn-1942-ibn-ezra-49` | commentary · Ibn Ezra | 12 | «ד"ה יתר שאת: … הכל שתהיה נישא.» |
| `cn-1942-sforno-a` | commentary · Sforno | 13 | «ד"ה הלא אם … גם אתה לרצון.» |
| `cn-1942-sforno-b` | commentary · Sforno | 14 | «ד"ה שאת: רום … של יצר הרע.» |
| `cn-1942-q-b2` | question | 15 | «2. אל מי … לפי רש"י וספורנו?» |
| `cn-1942-h-intro` | narration | — | — |
| `cn-1942-h-rashi` | commentary · Rashi | 29 | «בתמיה, אתה טוען … אי אפשר לטעון.» |
| `cn-1942-h-ramban` | commentary · Ramban | 30 | «בתמיה, אתה טוען … נשאתי חרפת נעורי» |
| `cn-1942-h-ibn-ezra` | commentary · Ibn Ezra | 31 | «על דעת כל … הפסוק הבא אחריו.» |
| `cn-1942-q-h` | question | 32 | «מה ההבדל בין … בפירוש המילים האלה?» |
| `cn-1942-z-intro` | narration | — | — |
| `cn-1942-z-rashi` | commentary · Rashi | 40 | «חקק לו אות … אות משמו במצחו» |
| `cn-1942-z-ibn-ezra` | commentary · Ibn Ezra | 42 | «ויש אומר, כי … לא גילה האות.» |
| `cn-1942-z-ramban` | commentary · Ramban | 43 | «כי בעבור שאהיה … בשמירת עליון עליו.» |
| `cn-1942-q-z` | question | 39 | «פליגי חכמים בענין … שאהיה נע ונד"./» |
| `cn-1942-t-intro` | narration | — | — |
| `cn-1942-br` | commentary · Bereshit Rabbah | 51 | «ויצא קין. מהיכן … טוב להודות לה'".» |
| `cn-1942-q-t` | question | 52 | «איזו משתי התשובות … שעשה קין תשובה?» |

### 1956

| Card | Type | [i] | Slice (start … stop) |
|---|---|---|---|
| `cn-1956-intro` | narration | — | — |
| `cn-1956-br-1` | commentary · Bereshit Rabbah | 3 | «"ויאמר קין אל … הבל אחיו ויהרגהו"» |
| `cn-1956-br-2` | commentary · Bereshit Rabbah | 3 | «ר' יהושע דסכנין … הבל אחיו ויהרגהו"» |
| `cn-1956-br-3` | commentary · Bereshit Rabbah | 3 | «יהודה בר' אמי … הראשונה היו מדיינין.» |
| `cn-1956-q-a1` | question | 4 | «1. המדרש דן … הדעות הנאמרות בזה.» |
| `cn-1956-q-a2` | question | 5 | «2. מה ראה … הדעות בסדר זה?» |
| `cn-1956-b-intro` | narration | — | — |
| `cn-1956-rashi-4-1` | commentary · Rashi | 7 | «ד"ה והאדם ידע: … היו לו בנים.» |
| `cn-1956-q-b1a` | question | 8 | «א. הבא דוגמאות … אחרים בספר בראשית!» |
| `cn-1956-q-b1b` | question | 9 | «ב. הסבר, מהי … אלה מבחינה רעיונית?» |
| `cn-1956-rashi-4-7a` | commentary · Rashi | 17 | «ד"ה לפתח חטאת … קברך חטאתך שמור.» |
| `cn-1956-rashi-4-7b` | commentary · Rashi | 18 | «ד"ה ואליך תשוקתו: … שוקק ומתאווה להכשילך.» |
| `cn-1956-q-b5a` | question | 19 | «א. למה לא … תמיד בצאתך ובבואך?» |
| `cn-1956-q-b5b` | question | 20 | «ב. הסבר, למה … חטאת בלא כנוי.» |
| `cn-1956-q-b5c` | question | 21 | «ג. מה ראה … ולא הסתפק באחד?» |
| `cn-1956-rashi-4-8` | commentary · Rashi | 22 | «ד"ה ואמר קין: … יישובו של מקרא.» |
| `cn-1956-q-b6a` | question | 23 | «א. מה קשה … מה קשה לו?» |
| `cn-1956-q-b6b` | question | 24 | «ב. ב"מדרשי אגדה" … פרושו עקרונית מהן?» |
| `cn-1956-rashi-4-10` | commentary · Rashi | 25 | «ד"ה דמי אחיך: … דמו ודם זרעותיו.» |
| `cn-1956-q-b7b` | question | 26 | «ב. הסבר את … המסומל בדבריו אלה.» |
| `cn-1956-q-b7c` | question | 27 | «ג. היכן מצינו … התורה במקום אחר?» |
| `cn-1956-c-intro` | narration | — | — |
| `cn-1956-c-rashi-a` | commentary · Rashi | 30 | «ד"ה הלוא אם … שאת: כתרגומו פירושו.» |
| `cn-1956-c-onkelos` | commentary · Onkelos | 31 | «הלוא אם תטיב … לך (יסולח לך).» |
| `cn-1956-c-rashi-b` | commentary · Rashi | 34 | «ד"ה ואתה תמשל … – תתגבר עליו.» |
| `cn-1956-c-malbim` | commentary · Malbim | 35 | «ד"ה הלוא: גילו … בהמתו מושלת עליו.» |
| `cn-1956-q-c1` | question | 36 | «1. העתק את … מן המפרשים הנ"ל.» |
| `cn-1956-q-c2` | question | 37 | «2. הסבר מה … אחת משתי ההוראות.» |
| `cn-1956-q-c3` | question | 38 | «3. הסבר כיצד … אחד משני הפרושים.» |
| `cn-1956-q-c4` | question | 39 | «4. מה תיקן … חסר בלי פרושו?» |

### 1958

| Card | Type | [i] | Slice (start … stop) |
|---|---|---|---|
| `cn-1958-intro` | narration | — | — |
| `cn-1958-q-a1` | question | 2 | «1. הפסוקים ב-ה … מתוך פרשת בראשית.» |
| `cn-1958-cassuto-1` | commentary · Cassuto, Torat HaTe’udot | 3 | «כשבא איזה פעל … איזו מלה אחרת» |
| `cn-1958-q-a1a` | question | 4 | «א. הסבר מהי … הֶבֶל... וְקַיִן הָיָה..."» |
| `cn-1958-q-a1b` | question | 5 | «ב. הבא דוגמאות … זו מתוך פרקנו.» |
| `cn-1958-a2-intro` | narration | — | — |
| `cn-1958-cassuto-2` | commentary · Cassuto, From Adam to Noah | 8 | «סידרתי את חלקיו … האדמה" ו"דמי אחיך".» |
| `cn-1958-q-a3` | question | 9 | «הסבר מה משמעותה … של הקבלה זו?» |
| `cn-1958-b-intro` | narration | — | — |
| `cn-1958-q-b1` | question | 13 | «1. האם השאלות … דבריך מן הכתוב.» |
| `cn-1958-q-b2` | question | 14 | «2. הבא דוגמאות … זה מספר בראשית.» |
| `cn-1958-q-b3` | question | 15 | «השווה את דברי … למקום שבפרק ג':» |
| `cn-1958-rashi-4-9` | commentary · Rashi | 16 | «ד"ה אי הבל … הרגתיו וחטאתי לך» |
| `cn-1958-rashi-3-9` | commentary · Rashi | 16 | «ד"ה איכה: יודע … בשלוחי מרודך בלאדן.» |
| `cn-1958-q-b3b` | question | 17 | «הסבר את השוני … בדבריו כאן וכאן!» |
| `cn-1958-q-b4` | question | 18 | «הסבר למה נשאלה … ולא בלשון 'איפה'?» |
| `cn-1958-d-intro` | narration | — | — |
| `cn-1958-d-rashi` | commentary · Rashi | 27 | «ד"ה מן האדמה: … תת כוחה לך".» |
| `cn-1958-ramban-1` | commentary · Ramban | 28 | «ארור אתה מן … בהיותו עובד אותה...» |
| `cn-1958-q-d1` | question | 29 | «1) מה ההבדל … מלת "מן" בפרט?» |
| `cn-1958-q-d2` | question | 30 | «2. התוכל להסביר … רש"י מבחינה לשונית?» |
| `cn-1958-q-d3` | question | 31 | «3) לשם מה … ("ואמר כן כנגד...")» |
| `cn-1958-ramban-2` | commentary · Ramban | 28 | «וייתכן שאיררו מן … עונש הרוצחים גלות.» |
| `cn-1958-q-d4` | question | 32 | «4) מה ההבדל … שאררו מן האדמה").» |
| `cn-1958-ramban-3` | commentary · Ramban | 28 | «בטעם "אשר פצתה … פורה והייתה עשרים".» |
| `cn-1958-q-d5` | question | 33 | «5) לשם מה … על האמור כבר?» |
| `cn-1958-q-d6` | question | 34 | «6) איך יפרש … קללת "נע ונד".» |

---

## Lib and input gaps (not fixed here; reported)

1. **`[?]` in scan-basis `he`**: fixed upstream during this task (the harvest regeneration);
   the leaves were rebuilt on it. What remains is that a scan-only item with a mark (1956 `after
   25`) is now refused outright, even where triage settled the reading («לו»). The harvester could
   write the triaged reading into `he`.
2. **No comparison-panel helper.** `primary()` builds only single mode. 1958 §ב builds its
   side-by-side panel in `cain.py` (`comparison_4_3`) from `verse_set()` + `words()`, adding
   `side`. A `comparison(left_keys, right_keys, left_spec, right_spec)` in the lib would serve
   any leaf.
3. **Laid-out quotations can't be shown.** `cut()` flattens whitespace, so a quotation whose
   layout is its content (1958 [7], Cassuto's line-by-line printing of 4:10–11) can't be shown.
4. **Verse cache leak.** `bereshit-verses.json` 4:13 Hebrew ends with a variant note,
   «*(בספרי ספרד ואשכנז מִנְּשׂוֹא)», which will show in the 1942 panel. `clean_verses.py` should
   strip it.
5. **Out-of-range verses.** Genesis 49:3 (1942 §ב) isn't in the verse cache, which covers
   1:1–6:8, so it can't be a panel.
6. **Wrong harvest refs.** 1956 [30] is `ref: Genesis 4:7`, but the item is Rashi on Genesis
   4:7:1, and [32]–[34] have no ref. The cards set their refs by hand.
