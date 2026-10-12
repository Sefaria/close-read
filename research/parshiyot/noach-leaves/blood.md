# Blood: "Your Lifeblood" (Genesis 9:1–7): paper trail

Module: `research/scripts/noach_leaves/blood.py` (prefix `bl-`). Harvests: `noach-harvest/blood/<year>.json`.
Scan checks: `noach-scancheck/161496-1948.md`, `161105-1957.md`, `160445-1970.md`.
`python3 research/scripts/check_leaves.py noach blood` gives 0 failing checks: 8 sections, 79 steps.

Shared panels: `gen_9_5_6()` (1948 §א), `gen_9_4_6()` (1957 §ב–ד), `gen_9_6()` (1957 §ה–ו), and
three comparison panels built like `comparison_4_3()`. **Sides:** 1970 has a two-column table
with «לאדם» on the right and «לנח» on the left, so the panel matches that layout. 1957's table
is in rows, and 1948 has no table, so on those panels the side named first in her wording is
on the right: Adam in 1957 [2], Noah's sons in 1948 [21]. Word groups are merged right side
first, because 1970's 1:28 phrase «פרו ורבו ומלאו את הארץ וכבשה» has to wrap before 9:1's
«פרו ורבו ומלאו את הארץ», which is a prefix of it. The phrases on a comparison panel are
lengthened until each one is unique across *both* sides ("rule the fish of the sea", "upon all
the fish of the sea"), because the uniqueness test counts both sides together.

Local helper: `underline_every(he, span, n)`. `nechama_lib.underline()` marks only the first
occurrence of a span, so it can't mark 1957 Radak's two «והוא». **Lib gap:** an `nth`/`all`
option on `underline()` would make this helper unnecessary.

---

## 1948 (תש"ח, sheet 161496): `leaf_1948`, 22 steps

Rendered: §א (all of her sources, Q1–4) and §ב (her one question, on a comparison panel).

### §א `bl-1948`: panel Genesis 9:5–6
| card | harvest | slice |
|---|---|---|
| br | [3] Bereshit Rabbah | whole |
| aggadah | [4] Midrash Aggadah | from «שאם» (drops her label line) |
| rashi | [5] Rashi 9:5 ד"ה מיד כל חיה | whole. The scan gives only a bare pointer, with no stop |
| rambam | [6] Hilkhot Rotze'ach 2 | from «אבל השוכר» (drops her label and the leading «...»). The harvest has `kind: question`, but it's a source |
| moreh | [7] Moreh 3:17 | from «אמנם זה הגמול». Her glosses «(…שכונתו לרב סעדיה גאון)», «(כתה מוסלימית)» stay, as triaged |
| ramban-a | [8] | from «תמה אני». Her start is «החל מן "ותמה אני"»; the digitization has no ו |
| ramban-b | [9] | start through «מאל (איוב כ' כ"ט).» (her bare pointer ד"ה ויהיה טעם שופך דם האדם, with no stop) |
| ramban-c | [9] | from «ואולי הדרישה» to the end |
| radak | [10] | whole |
| ralbag | [11] | from «שלא יחשבו» |
| q3 | [16] | whole. Placed after Ralbag, the source it asks about |
| hefetz-a | [12] Melekhet Machshevet | «ראיתי» through «על זבוב ועל רמש...» |
| hefetz-b | [12] | from «(מאריך» (her gloss) to the end |
| q4 | [17] | whole. Placed after Melekhet Machshevet |
| wessely | [13] | from «הנני חושב» (with the triaged «היותה») |
| q1, q2 | [14], [15] | whole. They close the section: Q1 asks what the problem is, and Q2 asks the reader to sort all the views. Q1 has no highlight, as with 1963's find-the-question card |

- Ramban is split three ways so each of the "three views" in her Q2 has its own card: the
  decree ([8]), vengeance *by means of* the animals ([9] first half), and animals restrained
  by nature ([9] from «ואולי»).
- Not quoted: [2], her prose «נחלקו החכמים… ואלה קצת דעותיהם:», which describes the sheet's
  structure; [18]–[19], the «עצה טובה» box with the Aptowitzer reference (as assigned).
- **Possible slip, quoted anyway:** [12] «אלו דברים ככתבם». The scan check reads the last
  letter of «דברי?» as ח or ה, not ם. It's a source text, so I haven't fixed it. The English
  ("these words are as they are written") holds for either reading. Lev may want to look at the scan.

### §ב `bl-1948-b`: comparison panel, 9:1–3 (right) and 1:28–30 (left)
These are her own ranges; she cites «א כ'ח-ל'». The panel is long, so expect the Hebrew-only
fallback on mobile.
- intro (no highlight), then two narrations that only quote the verse: "“Rule the fish of the
  sea.”" (`urdu`) and "“The fear and the dread of you.”" (`mora`). They follow 1963's
  bare-quote pattern. An earlier draft also summarized each side ("…and plants for food"); that
  was cut because it set out the answer to her question.
- q-b: [21], whole, in the scan's wording («א כ'ח-ל'», «הסבה»).

### Translation choices worth a second look
- Rashi [5]: «נמשל כבהמות נדמו» is translated "ruled over like the beasts, they perish", which is
  Rashi's reading of נמשל, not "likened".
- Ramban [8]: «כל החיה שתטרוף אותו תטרף» is "every animal that devours him shall be torn".
  «שור המדבר» is "an ownerless ox".
- Melekhet Machshevet: «אנשים שלמים הם אתנו» is "men who are 'at peace with us'" (an echo of
  Genesis 34:21).
- Wessely: "chayah" is left transliterated so that his argument can be followed. "[his soul]"
  is our gloss.

---

## 1957 (תשי"ז, sheet 161105): `leaf_1957`, 34 steps

Rendered: all six sections, §א–§ו.

Leaf title: "1957 · Murdered, Murderer, or Judge" (her §ו Q4).

### §א `bl-1957`: comparison panel, 1:28 (right) and 9:2 (left)
These are her table's two verses. [3], the table text, is `publish: false`; the panel shows the verses.
- q-a1: [2], whole. It's her "השווה" instruction (the digitization's wording, as triaged), rendered as a question card.
- q-a2: [4], whole (the scan's wording).
- Not quoted: [5]–[6] (the «עצה טובה» on Meir Weiss, which points outside the sheet).

### §ב–§ד `bl-1957-b`: panel Genesis 9:4–6
Her §ב Q1 names verses ד–ו, and her §ג Q3 names «באדם» in verse 6. Verse 4 is on the panel
because of Q1, so q-b1 highlights it (`basar`) together with the phrases of 9:5–6.
| card | harvest | slice |
|---|---|---|
| rashi-adam | [9] | whole |
| rashi-achiv | [10] | whole (the scan's spelling, as triaged) |
| haktav-a | [12] | start through «שני אופני רציחה:» |
| haktav-b | [12] | from «אם לטובת הנרצח» to the end; «אם לטובת הנרצח» underlined (scan) |
| q-b1, q-b2, q-b3 | [13], [14], [15] | whole. [15] has no number, as in the harvest (the scan has «3xx)») |
| g-intro | narration | the verse phrase, highlighting `damchem` |
| ibn-ezra-a | [21] | start through «ולא אתם להן.»; underline 1 «וזה כלל. ואחרי כן באר» (scan check) |
| q-g1 | [22] | whole |
| ibn-ezra-b | [21] | from «והמפרש»; underline 2 is the scan's full span «והוסיף לבאר, או היא מצוה לבני נח, והוא הישר להרג ההורג,» (the digitizer's bold was shorter) |
| q-g2, q-g3 | [23], [24] | whole |
| rashi-damchem, rashi-nafshot | [27], [28] | whole ([27] with the triaged «בבהמה») |
| q-d1, q-d2, q-d3 | [29], [30], [31] | whole |

- **HaKtav VeHaKabbalah, sliced around a slip.** [12] reads «אם לדעת הנרצח לנקום נקמתו ממנו».
  The source (Sefaria, Frankfurt 1880) reads «אם לרעת הנרצח», as [12] itself does further on
  («על ההורג לרעת הנרצח»). The scan check records the underline «אם לדעת הנרצח» but doesn't say
  whether her print has ד or ר. I haven't typed a fix. The quote stops at «שני אופני רציחה:» and
  resumes at «אם לטובת הנרצח», so it leaves out «אם לדעת הנרצח לנקום נקמתו ממנו; או לקחת ממונו
  וכדומה.» The first kind of murder still appears in the second card («על ההורג לרעת הנרצח»).
  Her first underline is lost with it; the second is kept.
- Omitted: [11] (`publish: false`, a cross-reference to Rashi on Exodus 21), and [16]–[18], the
  «וע'» prooftext verses (Genesis 1:27 under a wrong digitized ref of 1:1, Leviticus 20:9 and 20:10).
  They were left out for density: with them the leaf runs to 37 steps, and no question of hers
  names them.
- The §ג and §ד sources keep her order, and each question follows the source it asks about.

### §ה–§ו `bl-1957-c`: panel Genesis 9:6
| card | harvest | slice |
|---|---|---|
| avot | [34] | from «הוא (ר' עקיבא)» (drops her label line) |
| maharsha | [35] | from «למה לא הביא» (drops «מקשה המהרש"א:»); a source, though the harvest's kind is question |
| q-h | [36] | whole |
| radak-baadam | [39] | whole. No ref: the digitizer's 9:1:2 is wrong, and the scan gives none |
| q-v1 | [43] | after the Radak it asks about |
| radak-tzelem | [40] | whole. «והוא» ×2 and «וכן» underlined (scan check) |
| q-v2, q-v3 | [44], [45] | |
| chizkuni | [41] | whole |
| malbim | [42] | from «...והוא» (drops the lemma). No ref: the digitizer's 9:5:1 is wrong |
| q-v4 | [46] | closes the section |

### Translation choices worth a second look
- Radak [40]: «והוא עשה אותו בצלמו והוא השחיתו» is "and he made him in his image, and he
  destroyed it". Both pronouns are left lowercase on purpose, so the English doesn't answer her
  Q2 ("to whom do the two 'hu' refer?"). Elsewhere in the card, God's pronouns are capitalized.
- HaKtav VeHaKabbalah b: «הנעשה לרצון הנרצח» is "done by the will of the murdered".
- Ibn Ezra a: «וזה כלל» is "And this is a general statement".
- Q d2 [30]: «שהובא בשאלה ג» is kept literally, "(brought in question ג)", although the reader
  doesn't see section letters. "quoted above" would read better but is less literal; Lev's call.
- Q b1 [13]: «(ד'-ה'-ו')» is "(4–5–6)", her verse numbers.

---

## Open question for Lev: long comparison panels
1948 §ב (1:28–30 against 9:1–3) and 1970 §א (1:28–30 against 9:1–4) show the full ranges she
gives, against the brief's "each side a few short lines". On a phone they will fall back to Hebrew
only. To shorten them, trim to 1:28–29 against 9:2–3 (1948) and drop 1:30 (1970).

---

## 1970 (תש"ל, sheet 160445; Nataf's bilingual edition): `leaf_1970`, 23 steps

Rendered: her §א, ב, ג, ד, ה. Her §ו (Meshekh Chokhmah) isn't in this theme's harvest. All her
own items use `en_basis: 'nataf'` (the whole item, with Nataf's English). Sources get our English.

### §א `bl-1970`: comparison panel, 1:28–30 (right) and 9:1–4 (left), as she set the table
This is her full table. [2], the table text, isn't quoted; the panel shows the verses.
Expect the Hebrew-only fallback on mobile.
- q-a0: [1], her "השוה" instruction (nataf). Nataf's English contains a typo, "Gods's first words";
  the nataf basis requires the whole item verbatim, so it appears on screen. Fixing it means editing
  `en_nataf` in the harvest. Narration "Both open the same way: 'Be fertile and
  increase'" points at the verse. q-a: [3] (nataf; the Hebrew is the scan's «ע"פ זמנם והקשרם», as triaged).

### §ב–§ג `bl-1970-b`: panel Genesis 9:3–4
- hirsch: [6], from «משנשתנו» (drops the label). Our English: Hirsch is a source. Nataf's English
  for this item was not used.
- **Omitted:** [7] (compare Rav Kook, in the Acharei Mot–Kedoshim 1969 sheet) and [8] (the
  difference between Hirsch and Rav Kook). Both depend on a source that isn't on this sheet.
- radak [11], abarbanel [12], both whole. q-g1–q-g3 [13]–[15] (nataf). kaspi [16], from «ד"ה»
  (drops the name line). q-g4–q-g6 [17]–[19] (nataf).

### §ד–§ה `bl-1970-c`: panel Genesis 9:4–5
Her §ה header is missing from the digitization. [24]–[28] are her §ה, following the scan check.
- q-d: [23] (her §ד, alone). Then rashi [24] and bekhor-shor [25], both whole. Then q-h1–q-h3 [26]–[28] (nataf).

### Numbering in 1970: can't be settled within my remit
The rule is whole items, Nataf's English and the harvest's number prefix. Under it, the cards show:
- [23]: Hebrew has no number (as in the scan); Nataf's English reads "1.".
- [26] «2.», [27] «3.», [28] «3.»: two consecutive cards both read «3.» in Hebrew. The scan numbers
  her §ה questions 1, 2, 3. The harvest kept the digitization's «2.» on [26] (triage: "nothing
  differs") and «3.» on [27], but applied the scan's «3.» to [28]. Nataf's English reads 2, 3, 4.
- **Fix belongs in the harvest/triage** (not touched here): [26] → «1.», [27] → «2.» per the scan.
  Nataf's 2/3/4 will still differ from the Hebrew whatever is done to the harvest.
- Also §ג: the scan letters the questions (א)(ב)(ג) twice; the harvest and Nataf number them 1–6.
  Kept as in the harvest.

### Translation choices worth a second look
- Abarbanel: «ובי"ת "בנפשו" תשמש במקום "עם"» is "the bet of 'be-nafsho' serves in place of 'with'".
- Ibn Kaspi: «שם משותף» is "a name shared by", i.e. a homonym.
- Hirsch: «הבדלי החום» is "the differences of heat". The source is Hirsch in Hebrew translation,
  and our English translates the Hebrew.

## Review fixes (Claude, 2026-10-12)

- **1957 HaKtav VeHaKabbalah [12]:** her print reads «אם לדעת הנרצח» (underlined; seen on the
  scan). The source reads «לרעת», and the contrast with «אם לטובת הנרצח» requires it, so this is a
  slip in her typing. `overrides.json` `replace` corrects it, and the first card now carries her
  first underlined span as well.
- **1970 numbering:** the digitizer's Hebrew numbers ([26] «2.», [27] «3.», [28] «3.») and Nataf's
  English numbers (2/3/4) disagree with each other and with her scan, which letters them. Nataf
  cards now drop the leading number on both sides (`nechama_lib.unnumber`; the provenance test
  allows exactly that).
- **1970 [1]:** Nataf's English has a typo («Gods's»), so this one card uses our translation.
