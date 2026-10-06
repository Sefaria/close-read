# Theme 1, the days of creation: paper trail

Leaves live in `research/scripts/bereshit_leaves/creation.py`. Check with
`python3 research/scripts/check_leaves.py creation` (0 failing checks, 2026-10-06).
The 1963 leaf's trail is in `../bereshit.md` §9.

---

## 1943 (תש"ג), sheet 162000: `leaf_1943(prefix='cr-1943')`

**Sources of her words:** the harvest `bereshit-harvest/creation/1943.json`. Her questions and prose
are transcription items (from `bereshit-transcriptions/162000-1943.md` Part 1, verified by Lev,
2026-10-06), keyed `'<letter>/q<n>'` and `'<letter>/text1'`. Her sources come from the digitization.

**Sections rendered:** א, ב, ג (with the Leningrad Codex, folio 2r), ד. 3 panel sections, 31 steps.

| Section id | Panel | Covers |
|---|---|---|
| `cr-1943` | Genesis 2:2–4 (title "1943 · Where Creation Ends") | §א, §ב, and the §ג sources |
| `cr-1943-2r` | Leningrad folio 2r, `regions` = `toldot` only (x 0.37, y 0.314, w 0.2, h 0.03) | §ג: the codex, then her question |
| `cr-1943-ed` | Genesis 2:5–6 (title "A Flow from the Ground") | §ד |

### Every card

| Card | Type · label | Harvest [i] | Slice | English |
|---|---|---|---|---|
| `cr-1943-intro` | narration | — | — | — |
| `cr-1943-mekhilta` | commentary · Mekhilta | `א/text1` | from `ומושב` (after her lead-in «איתא במכילתא לשמות יב' מ':») to end | ours |
| `cr-1943-q-a1` | question | `א/q1` | whole | ours |
| `cr-1943-a-rashi` | commentary · Rashi | [2] | whole | ours |
| `cr-1943-a-ibn-ezra` | commentary · Ibn Ezra | [3] | whole | ours |
| `cr-1943-a-sforno` | commentary · Sforno | [4] | whole | ours |
| `cr-1943-q-a2` | question | `א/q2` | whole | ours |
| `cr-1943-q-a3` | question | `א/q3` | whole | ours |
| `cr-1943-b-intro` | narration | — | — | — |
| `cr-1943-b-rashi` | commentary · Rashi | [6] | whole | ours |
| `cr-1943-b-ibn-ezra` | commentary · Ibn Ezra | [7] | start to `לעשות דמותם.` | ours |
| `cr-1943-b-ramban` | commentary · Ramban | [8] | start to `בששת הימים.` (her stop; the item ends there) | ours |
| `cr-1943-b-radak` | commentary · Radak | [9] | whole | ours |
| `cr-1943-b-malbim` | commentary · Malbim | `ב/text1` | from `לא היתה שביתה` to end (her own quotation of Malbim) | ours |
| `cr-1943-q-b1` | question | `ב/q1` | whole | ours |
| `cr-1943-q-b2` | question (unnumbered in the scan) | `ב/q2` | whole | ours |
| `cr-1943-b-jer` | commentary · Jeremiah 16:12 | [11] | whole | ours |
| `cr-1943-b-joel` | commentary · Joel 2:20 | [12] | whole | ours |
| `cr-1943-b-ps` | commentary · Psalms 126:3 | [13] | to `שְׂמֵחִים"`, dropping the trailing «?» (her question mark, carried into the item) | ours |
| `cr-1943-g-intro` | narration | — | — | — |
| `cr-1943-g-ramban` | commentary · Ramban | [15] | from `יספר` (after the digitizer's «ד"ה אלה תולדות:») to `כל חי.` (her stop) | ours |
| `cr-1943-g-sforno` | commentary · Sforno | [16] | whole | ours |
| `cr-1943-codex` | narration (no highlight) | — | — | — |
| `cr-1943-toldot` | narration, highlight `toldot` | — | — | — |
| `cr-1943-q-g` | question (no highlight; last on the folio) | `ג/q1` | whole | ours |
| `cr-1943-d-intro` | narration | — | — | — |
| `cr-1943-q-d1` | question, highlight `ed`, `haadamah` | `ד/q1` | whole | ours |
| `cr-1943-d-ibn-ezra` | commentary · Ibn Ezra | [18] | from `והגאון אמר` (her «החל מן "והגאון אמר"») to end | ours |
| `cr-1943-d-ibn-ezra-deut` | commentary · Ibn Ezra, on Deuteronomy 33:6 | [19] | from `ויהי מתיו מספר:` to `הוא מעט.` | ours |
| `cr-1943-q-d2` | question | `ד/q2` | whole | ours |
| `cr-1943-q-d3` | question (unnumbered in the scan) | `ד/q3` | whole | ours |

### Order

Sources keep her order: in §ב, Rashi, Ibn Ezra, Ramban, Radak, Malbim, as in her pointer list.
Each question follows the material it asks about, and her question order is unchanged:
- §א: her Mekhilta passage comes before her questions in the scan. Q1 (the translators' difficulty)
  follows it; Q2–Q3 (Rashi, Ibn Ezra, Sforno) follow those sources.
- §ב: her four verses follow `ב/q2`, the question that names them.
- §ג: the question closes the folio-2r continuation, after the codex cards.
- §ד: Q1 (הארץ / האדמה) asks about the verse alone, so it comes straight after the verse narration.
  Q2 and Q3 follow the two Ibn Ezra passages they ask the reader to read.

### Start/stop points

- **§ב Ibn Ezra, her stop «עד לעשות אותם»:** not in the digitized text, which reads «לעשות דמותם»
  (and Ramban [8], quoting him, has «כמותן»). Per rule 5 the card quotes less: the first sentence,
  through «לעשות דמותם.», which is the sentence her stop evidently marks. It leaves out the rest of
  [7] («והמפרש לעשות… ואמר הגאון…»), which runs past her stop.
- **§ב Ramban, her stop «עד בששת הימים»:** honored; digitized [8] ends exactly there.
- **§ג Ramban, her stop «עד כל חי»:** honored; [15] ends there.
- **§ד Ibn Ezra, her start «החל מן "והגאון אמר"»:** honored.
- **§ד Ibn Ezra on Deut 33:6:** the card drops the digitizer's lead-in «וגם דבריו לדברים פרק ל"ג
  פסוק ו' :» (her question's words, moved into the item) and stops before «וכן אני מתי מספר ( בראשית
  ל"ד ד' )», whose citation is a slip for Genesis 34:30. She gives no stop here.

### Mekhilta: her text, not the digitized one

The Mekhilta card quotes her own text (`א/text1`), not digitized [1]. The two are the same
passage; hers has her spelling («ליונית», «הששי») where [1] has «ליוונית», «השישי». Only one is
used. [1] is not quoted.

### Malbim

Malbim isn't in the digitization. Her §ב prose (`ב/text1`) gives her pointer list, then her own
quotations: «ואלה דברי הרד"ק: …» and «מלבי"ם: …». The Malbim card slices from «לא היתה שביתה» to
the end, which is Malbim's words as she quoted them. Her Radak quotation matches digitized [9]
word for word, so the Radak card uses [9].

### What's left out, and why

- **No questions omitted.** All 9 are in.
- **§ב [10] Judges 13:9:** her question lists «שופטים יג' ט'», and the digitizer linked Judges 13:9
  («וישמע האלהים בקול מנוח…»). That verse has no «לעשות», which is the point of her list; Judges
  13:19 («ומפלא לעשות») does. This is probably her slip for 13:19, but the harvest has only 13:9,
  so it isn't quoted. Her question's English keeps "Judges 13:9", as she wrote it. Not settled.
- **§ג Rashi (ד"ה אלה):** on her list, but not in the digitization or the harvest, so it can't be
  quoted.
- **[1]** (see Mekhilta above); **[0], [5], [14], [17]:** the digitizer's verse items. The panel
  shows the verses.
- **Her pointer lists** (the start of `ב/text1`, and `ג/text1`): structure, not content. They're
  recorded here, not shown.
- **NOT-IN-SCAN sources:** none. The ↔ map in the transcription matches every digitized source to
  her pointers.
- **Triage:** no open items for this sheet.

### The Leningrad cards

`cr-1943-toldot` says only what's visible: 2:4 begins on that line and, in this codex, starts a
new paragraph after an open break (WLC פ after 2:3, pack §5a). It doesn't mention the blank line
before 2:4 or the large marginal mark (pack §5b), and it doesn't answer her question, which follows
it. `cr-1943-codex` names the codex and its range only. It doesn't assume the reader has seen 1963.

### Translation choices worth a second look

- **Rashi 2:2 / Ibn Ezra 2:2:** adapted from 1963's English for the same texts (1963 [26], [28]).
  Rashi here begins «רבי שמעון אומר», so "R. Shimon says:" is added. Ibn Ezra adds its closing
  clause ("from all the creatures He had created"). The citations in parentheses are our aid; the
  Hebrew has none.
- **Sforno 2:4:** the digitized text has «הצמים», a slip for «הצמחים» ("the plants"); translated as
  "plants". "Yet they came out into actuality [only later]" renders «אמנם יצאו לפועל»; the bracket
  is ours.
- **Ibn Ezra 2:3:** «לעשות דמותם» → "to make their likeness"; Ramban's quotation («כמותן») → "to
  make their like". «רבי אברהם» in Ramban is glossed "[Ibn Ezra]".
- **Malbim:** «לא היתה שביתה של בטלה, רק לעשות» → "It was not a resting of idleness, but 'to
  make'"; «מעשה הנהגת ההשגחה» → "the work of the governance of Providence".
- **Her §ג question:** «מה שעור הפסוק הזה» → "What is the construction of this verse".
- **Her §א Q1:** «שנוי» → "change".
- **The verses (Jeremiah, Joel, Psalms):** our plain translation, keeping «לעשות» visible as "done"
  ("done worse", "done great things"). Labels are the verse refs; `source` is 'Tanakh'.
- **Ibn Ezra 2:6:** «אד» is left as "ed [flow]" because the JPS panel reads "flow" and Saadia's
  reading turns on the word.
- **Panel English, 2:6:** JPS renders מן הארץ "from the ground" and פני האדמה "surface of the
  earth", the reverse of the pair in her §ד Q1. The word groups bind the Hebrew correctly (`ed` =
  «ואד יעלה מן הארץ», `haadamah` = «את כל פני האדמה»). Q1's English names the Hebrew words
  ("ha-aretz [the earth]", "ha-adamah [the ground]"), so the swap is visible, not hidden.
- **Panel English, 2:4:** JPS puts a full stop after "when they were created", which itself reads
  2:4a as a close. That's the translation's choice, not ours, and no card comments on it.

---

## 1954 (תשי"ד), sheet 161401: `leaf_1954(prefix='cr-1954')`

**Sources:** `bereshit-harvest/creation/1954.json`; scan check `bereshit-scancheck/161401-1954.md`.

**Sections rendered:** ב, ג, ד on one panel, Genesis 1:1–3 (title "1954 · Why Begin with
Creation?"). 26 steps. §א (Psalm 104 in the order of creation) is out, per the pack §7 design.

### Every card

| Card | Type · label | Harvest [i] | Slice | English |
|---|---|---|---|---|
| `cr-1954-intro` | narration | — | — | — |
| `cr-1954-rashi` | commentary · Rashi | [5] | from `אמר רבי יצחק` (after «ד"ה בראשית:») to end | ours |
| `cr-1954-ramban-1` | commentary · Ramban | [6] | `אמר רבי יצחק` → `עם התורה שבעל פה.` | ours |
| `cr-1954-q-b1` | question | [7] | whole | ours |
| `cr-1954-q-b2` | question | [8] | whole | ours |
| `cr-1954-ramban-2` | commentary · Ramban | [6] | `ונתן רבי יצחק טעם לזה` → `אשר לפניהם.` | ours |
| `cr-1954-ramban-3` | commentary · Ramban | [6] | `ואשר יבאר הפירוש` → `הגיד להם את בראשית.` | ours |
| `cr-1954-ramban-4` | commentary · Ramban | [6] | `וכבר בא להם` → `אם כן נתבאר מה שאמרנו` (her stop) | ours |
| `cr-1954-q-b3` | question | [9] | whole | ours |
| `cr-1954-q-b4` | question | [10] | whole | ours |
| `cr-1954-q-b5` | question | [11] | whole (digitized כ"ג; see triage) | ours |
| `cr-1954-g-intro` | narration | — | — | — |
| `cr-1954-ibn-ezra` | commentary · Ibn Ezra | [14] | from `אמר הגאון` (after «ד"ה ויאמר:») to end | ours |
| `cr-1954-ramban-or` | commentary · Ramban | [15] | whole | ours |
| `cr-1954-moreh-1` | commentary · Rambam, Moreh Nevukhim | [16] | `ה"דיבור"` → `התרצה להרגני.` | ours |
| `cr-1954-moreh-2` | commentary · Rambam, Moreh Nevukhim | [16] | `וכל "אמירה` → `רצה או חפץ.` | ours |
| `cr-1954-moreh-3` | commentary · Rambam, Moreh Nevukhim | [16] | `והמופת עליו` → end | ours |
| `cr-1954-q-g1` … `q-g5` | questions | [17]–[21] | whole | ours |
| `cr-1954-q-g6` | question | [22] | start → `איזהו?` | ours |
| `cr-1954-q-g7` | question | [23] | whole | ours |
| `cr-1954-d-intro` | narration | — | — | — |
| `cr-1954-q-d` | question | [26] | whole | ours |

### Start/stop points

- **Ramban [6], her stop «עד "אם כן נתבאר מה שאמרנו"»:** honored (the item's last word «בזה» is left off).
- **Rashi [5]:** the scan gives no stop; it prints the opening «אמר ר' יצחק: לא היה צריך להתחיל...»
  and trails off, so the full passage is the digitizer's expansion. It's quoted to the end because
  her Q4 («כיצד מתרץ ר' יצחק את קושיתו (בתוך דברי רש"י)») asks about R. Yitzhak's answer, which is in
  the rest of the passage.

Ramban [6] is one long item that her stop runs to. It is split into four consecutive cards,
contiguous and in order, which together cover «אמר רבי יצחק» through «אם כן נתבאר מה שאמרנו»,
dropping only the digitizer's «ד"ה בראשית ברא אלוהים:».

### Order

Sources keep her order. In §ב her five questions follow all her sources. Here Q1–Q2 (Ramban's
wonder and his deepening of the question) follow the first Ramban card, which contains both, and
Q3–Q5 follow the rest of Ramban. Her question order is unchanged. In §ג the sources come first and
all seven questions follow, in her order.

### Calls I made (flag for review)

- **The Moreh (Rambam, Moreh Nevukhim 1:65, with Even Shmuel's notes) is included,** though the
  assignment listed §ג as "Ibn Ezra, Ramban, her questions". It's on her sheet (prose item [16],
  digitization basis; the scan has it under her label «רמב"ם»), and her Q1, Q3 and Q4 ask about
  Rambam. Without it, three of her seven questions would have nothing to stand on. It's split into
  three cards (the meanings of "saying"; why command is borrowed for God's will; the proof), each
  labeled «רמב"ם» / "Rambam, Moreh Nevukhim" (names only). The parenthetical notes are Even
  Shmuel's, as her scan's closing credit line says; the first card's own text names him («פירוש
  אבן שמואל»). The digitizer's relocated credit line at the top of [16] is not quoted. If you'd rather drop the Moreh, Q1, Q3 and Q4 must go with it.
- **Q6 stops at «איזהו?»:** her parenthetical «(כנוי: כגון - הבורא ית', הקבה"ו[?])» ends in a
  word the scan checker couldn't resolve, and the `[?]` marker can't be displayed. The 1963 §ג Q1
  precedent (stopping before a parenthetical) applies.

### NOT-IN-SCAN and triage

- **[4] Rashi 1:1:2 is NOT-IN-SCAN** (the digitizer's; its text repeats the section's lemma). No
  question names it, so it isn't quoted (rule 6).
- **[11] (Q5), triage `use: digitized`:** her scan reads «דברים ב' כ"ב»; Ramban's verse («כפתרים
  היצאים מכפתור השמידם») is Deut 2:23, and the digitizers corrected it. The card quotes the
  digitized «כ"ג» and translates "Deuteronomy 2:23". Evidence: triage.json, and Ramban [6] itself
  cites «( דברים ב' כ"ג )».
- **[22] (Q6), triage `use: form`:** her scan spelling «כנוי» is in the harvest and is what's quoted.
- **[17] (Q1):** the digitizer's «(שהובא בראב"ע)» is an editorial addition (pack §8) and is kept,
  translated "(cited in Ibn Ezra)".
- No open triage items for this sheet.

### What's left out

- **No questions omitted.** All five of §ב, all seven of §ג (Q6 trimmed as above) and §ד's one
  question are in.
- **[4]** (NOT-IN-SCAN), **[13]** (the digitizer's verse item for 1:3), **[25]** (the digitizer's
  «פסוק ד'» label, not in the scan).
- §ד has no sources on her sheet, only the question, so it's a narration and the question.

### Translation choices worth a second look

- **Moreh, «ה"דיבור" ו"האמונה"»:** the harvest, and her scan (per the scan check), read «האמונה»
  ("belief"). Ibn Tibbon's text reads «כי ה׳דיבור׳ וה׳אמירה׳ מלה משותפת» (Sefaria, *Moreh Nevuchim,
  translated by Ibn Tibon*, Guide for the Perplexed, Part 1 65, fetched 2026-10-06). So «האמונה» is
  a slip, hers or her typist's, for «האמירה». The card translates what's written and says so: "“Speech” and
  “belief” [so in the text; Ibn Tibbon has “saying”] are an equivocal term". The Hebrew is unchanged.
- **Moreh, «(קהלת ג')» and «(שמות ג')»:** kept as printed, "(Ecclesiastes 3)" and "(Exodus 3)",
  though "Do you say to kill me?" is Exodus 2:14. Not corrected in the English.
- **Moreh, «שבעלות דבר מה ברצונו»:** read as «שבעלות» = "when something arises in the will".
- **Ramban 1:1, «לפיכך סתם לך הכתוב»:** "therefore Scripture told it to you closed", i.e. without
  explanation. A plainer alternative: "Scripture left it unexplained for you".
- **Ramban 1:1, «(ט' כ"ז)»:** kept as "(9:27)" as printed, though the curse of Canaan is 9:25–27.
- **Ramban card 4** ends mid-sentence ("…what we said has been made clear"), because her stop
  leaves off «בזה».
- **Ibn Ezra 1:3, «היה ראוי "להיות אור"»:** "it ought to have said “for there to be light”".
- **Questions:** «קושית» → "question", «תמיהה» → "wonder", «תרוצו» → "answer". "va-yomer" is
  transliterated in the questions, as she quotes the word.
- **Panel:** the JPS 1:1 ("When God began to create") is itself a reading of «בראשית». The
  `bereshit` group binds the Hebrew «בראשית ברא אלהים» to that phrase. No card comments on it.

---

## Lib gaps

- **Transcription items (resolved, 2026-10-06):** 1943's transcription items are now keyed
  (`'א/q1'`, `'ב/text1'`, …), and `item()` and `find_item()` resolve string keys by exact match.
  No other gaps.
