# Theme 3: the trees, the sin and its aftermath (Gen 2:9–3:24)

Leaves: `research/scripts/bereshit_leaves/sin.py` (`leaf_1944`, `leaf_1964`, `leaf_1968`).
Check: `python3 research/scripts/check_leaves.py sin` → 8 sections, 85 steps, 0 failing checks
(after the 2026-10-06 follow-ups and the harvest regeneration; see the end of this file).

All English is `en_basis: "ours"`. No Leningrad images. Narration only points at the verse.

---

## 1944 (תש"ד), sheet 161941 — `sn-1944`, 35 steps

**Sections rendered:** א, ב, ג, ד (all four). ב and ג share one section (`sn-1944-voice`) because
they share the panel (Gen 3:8–9); the ג cards follow the ב cards in her order.

| Section id | Panel | Steps |
|---|---|---|
| `sn-1944` "1944 · Eating from the Tree" | Gen 3:3–4, 6–7, 11 | 15 |
| `sn-1944-voice` "“They Heard the Sound”" | Gen 3:8–9 | 12 |
| `sn-1944-one-of-us` "“Like One of Us”" | Gen 3:22 | 8 |

**Cards → harvest** (`bereshit-harvest/sin/1944.json`):

| Card | Type · label | [i] | Slice |
|---|---|---|---|
| `-intro` | narration | — | — |
| `-rashi-3-3` | Rashi | [2] | whole |
| `-q-a1` | question | [3] | whole |
| `-rashi-3-4` | Rashi | [5] | whole |
| `-q-a2` | question | [6] | whole |
| `-q-a2-see` | question | [7] | start → `בבחירת המדרשים` (see harvest regressions) |
| `-rashi-3-6a` | Rashi | [8] | whole |
| `-q-a3` | question | [9] | whole |
| `-q-a3b` | question | [10] | whole |
| `-rashi-3-6b` | Rashi | [11] | whole |
| `-q-a4` | question | [12] | whole |
| `-rashi-3-7` | Rashi | [13] | from `לענין החכמה` |
| `-q-a5` | question | [14] | start → `את עיניה?` |
| `-rashi-3-11` | Rashi | [15] | whole |
| `-q-a6` | question | [16] | whole |
| `-b-intro` | narration | — | — |
| `-rashi-3-8a` | Rashi | [21] | whole |
| `-rashi-3-8b` | Rashi | [22] | whole |
| `-rashi-3-8c` | Rashi | [23] | whole |
| `-ibn-ezra-3-8` | Ibn Ezra | [24] | whole (= her stop; see below) |
| `-ramban-3-8` | Ramban | [25] | from `אמרו בבראשית רבה` (after the ד"ה) to end |
| `-q-b1` | question | [26] | whole |
| `-q-b2` | question | [27] | whole |
| `-br-19-8` | Bereshit Rabbah | [28] | whole |
| `-q-b3` | question | [29] | whole |
| `-rekhasim` | HaRekhasim LeBik'ah | [32] | from `המבקש` (after her label) to end |
| `-q-c` | question | [33] | whole |
| `-d-intro` | narration | — | — |
| `-rashi-3-22` | Rashi | [36] | whole |
| `-ibn-ezra-3-22` | Ibn Ezra | [37] | whole (see below) |
| `-q-d1` | question | [42] | whole |
| `-sforno` | Sforno | [40] | whole |
| `-rambam` | Rambam, Hilkhot Teshuvah | [41] | from `רשות לכל` |
| `-q-d2` | question | [43] | whole |
| `-q-d3` | question | [44] | whole |

**Her start/stop points (rule 5), settled against Sefaria's Ibn Ezra (Piotrkow):**
- **§ב Ibn Ezra [24], «עד גם הוא אחר».** Sefaria reads `…כי הטעם והאדם מתהלך בגן, גם הוא אמר שפי' ביום
  אכלך…`. Her «גם הוא אחר» is «גם הוא אמר» (ח/מ on this typewriter; the scan check notes the
  same blur for ה/ח). «עד» marks where she stops, and the digitized [24] ends exactly there
  (`והאדם מתהלך בגן.`). Quoting [24] whole is quoting her extent.
- **§ד Ibn Ezra [37], «עד כמו איש ממנו כ"ג ו' ועוד קרא להלן מן וטעם הפסוק כמו והייתם...».** Sefaria
  reads `…ראוי לדבק ממנו עם לדעת, ופי' ממנו לשון רבים, כמו איש ממנו (בראשית כג ו), וכבר ביארתי בס' היסוד…
  יטעו, וטעם הפסוק כמו והייתם…`. She reads through «כמו איש ממנו», skips the grammar aside, and
  resumes at «וטעם הפסוק». The digitizer cut earlier, at `לדעת...`, so **her clause «ופי' ממנו לשון רבים,
  כמו איש ממנו (בראשית כג ו)» is missing from [37].** It can't be restored (rule 1), so [37] is quoted as
  digitized, with its `...` standing for the gap. Worth knowing: her Q1 [42] asks about «ממנו», and
  the missing clause is Ibn Ezra's reading of it as plural.
- **Pointer lists.** All §א/§ב/§ד commentator texts except the Rambam are EXPANDED pointers (her
  `ד"ה` or `עיין רש"י, ראב"ע…, רמב"ן`); the digitized texts are the comments she pointed to. Ramban
  [25] has no stop; it's quoted from its first sentence after the ד"ה to the end.

**Other slices:**
- [7] is a parenthesis inside her question 2 (scan: `(וראה הכלל שלו בבחירת המדרשים פסוק ח' ד"ה וישמעו.)`).
  The regenerated harvest reads `פסוק ה'` again (the digitizer's typo; her correction `ח'` is no longer
  applied), so the slice **stops at `בבחירת המדרשים`** and the card reads only "And see his rule for
  choosing midrashim". When the harvest carries `פסוק ח'` again, extend the slice to `ד"ה וישמעו`
  ("…, verse 8, on 'And they heard'"). Rendered right after question 2; the Rashi it points to is [21], in §ב.
- [13] starts after the ד"ה, which the digitizer misspelled `ותפחקנה` (scan: `ותפקחנה`).
- [14] stops at `את עיניה?`, before her parenthetical `(ועי' מורה נבוכים … והועתקו דבריו בשאלון וירא תש"ג , עיין שם)`,
  a pointer to her Vayera sheet (as 1963 §ג Q1 stopped before the teacher's-guide pointer).
- [32] (HaRekhasim LeBik'ah) is quoted from `המבקש` (after her label) to the end, as one card. The
  regenerated harvest keeps the digitization's `כמוהו?` where the scan is doubtful (`כמ[?]הו.`).
- [41] starts after her label `רמב"ם, הלכות תשובה פרק חמישי הלכה א':`.
- [28] now reads the digitization's `קולו של אילנות` (scan: `קולן`); see harvest regressions below.
  The English ("the voice of the trees") is the same for both.

**Questions omitted:**
- §א [4] «ענה לשאלתם!»: excluded (not in the scan; triage not-published).
- §א item 7, Rashi [17] (`אשר נתת עמדי: כאן כפר בטובה`) with her question [18] «מה קשה לו?»: for density.
  The same Rashi, with three of her questions on it, is the heart of the 1968 leaf's §ד.

**Not quoted (not questions):** [38] (not-published). [39] «"מוכרת" – נפרד ולא נסמך.», her gloss on Ibn
Ezra's term, which stands without its partner [38]; its content is carried in our English of [37]
("its sense is absolute"). [0] (her opening note, which is about her sheet). [20], [31], [35] (verse
items; [31] is NOT-IN-SCAN).

**NOT-IN-SCAN sources quoted:** none.

**Open triage items:** none for this sheet. [27] is triage `digitized`: «רמבמ"ן» (Mendelssohn) is right;
her «רמב"ן» is a typo.

**Translation choices worth a second look:**
- [27]: «רמבמ"ן» → "Rambeman [Moses Mendelssohn]"; the German in Hebrew letters is transliterated
  back to German, with our bracketed English after it. Both brackets are editorial glosses (as 1963's
  question א). Her Hebrew is unchanged.
- [32]: her German glosses are given in German with English in quotes/brackets ("wo ist er
  geblieben, 'where has he got to?'"). «אלוקי אדוני אליהו» → "the God of my master Elijah" (her wording,
  not the verse's). «ואיה נפלאותיו אשר ספרו לנו» → "And where are His wonders that they told us of?"
  (her words, not JPS's Judges 6:13). «להושיעני כמוהו» → "to save me like him".
- [28]: «גנב דגנב דעתיה דברייה» → "The thief who stole the mind of his Creator!"
- [23]: «לרוח היום» glossed "[literally, 'to the wind of the day']", since the panel's JPS reads "at the
  breezy time of day". «(שם ל"ח)» → "(ibid. 38)", as printed.
- [40] Sforno «אחר הערב» → "the pleasant".
- [37] «או פירש על מחשבתו» → "Or: he explained it of his thought": left literal, because her Q1 asks
  the student to explain it. [42] keeps her «ועל» (for «ואל») in Hebrew; the English reads "and do not wonder".

---

## 1964 (תשכ"ד), sheet 160638 — `sn-1964`, 25 steps

**Sections rendered:** א, ב, ג. §ב is rendered in place of §ד (Lev/coordinator, 2026-10-06).
§ד («שאלות בטעמי המקרא», the accents on «דשא» in 1:11) is **dropped entirely**, with its Gen 1:11
continuation: in the scan it is an unlettered unit with an editor's credit (`העורך: מיכאל פו[?]ל[?]ן.`),
so its questions are the editor's, not hers.

| Section id | Panel | Steps |
|---|---|---|
| `sn-1964` "1964 · The Trees of the Garden" (§א and §ב) | Gen 2:9, 3:3 | 14 |
| `sn-1964-mimmenu` "“You Must Not Eat of It”" (§ג) | Gen 2:16–17, 3:12 | 11 |

§א and §ב share one section because both are headed by 2:9 in the scan and share the panel. Gen 3:3 is
on the panel because her §א Q4 [7] asks about «ולא תגעו בו» and her §ב question quotes 3:3 («ומפרי העץ
אשר בתוך הגן»). 3:12 is on the §ג panel because the Malbim cites it and her Q5 [25] asks about that proof.

**§ב scan check.** §ב was never scan-checked; I checked it (300 dpi strips page1_strip6–7, page2_strip0–1,
zoomed) and appended `## §ב` to `bereshit-scancheck/160638-1964.md`; `harvest_bereshit.py` now lists ב
for 1964 (one-line change to `CHOSEN`). Findings: [11] MATCH; [13] Ibn Kaspi MATCH; [12] Abarbanel DIFF,
spelling only (`ובמצוע`, `מהמצוע`), her underline on «כי הוא היה מטבע קצה ההפלגה – לא מהמצוע» (digitized
as bold); [14] her question DIFF: «האישה»→«האשה» (spelling), and her citation `ג' ג':` stands *before*
her quote of 3:3, which ends with `?`. The digitizer moved the citation after the quote, expanded it to
`(פרק ג' פסוק ג')`, and ended with `!`. No word of hers differs, but the regenerated harvest carries the
digitizer's citation and `!`, so **the card stops at `לנחש`** and points at 3:3 on the panel (`mipri`
highlight) instead of quoting her quotation of it. If the coordinator wants her full line, the harvest
needs the scan's form (`לנחש ג' ג': ומפרי … ולא תגעו בו?`) first.

**Cards → harvest** (`bereshit-harvest/sin/1964.json`):

| Card | Type · label | [i] | Slice |
|---|---|---|---|
| `-intro` | narration | — | — |
| `-akeidah-a` | Akeidat Yitzhak | [3] | `הצמיח לו` → `כי היו לאחדים.` |
| `-akeidah-b` | Akeidat Yitzhak | [3] | `והזכיר אצלם` → `ותכלית הכל.` |
| `-akeidah-c` | Akeidat Yitzhak | [3] | from `אמנם לצורך` to end |
| `-q-a1`…`-q-a6` | questions | [4]–[9] | whole |
| `-b-intro` | narration ("“In the middle of the garden.”") | — | — |
| `-abarbanel` | Abarbanel | [12] | whole, her underline reproduced |
| `-ibn-kaspi` | Ibn Kaspi | [13] | from `לא אמר` (after her label) |
| `-q-b` | question | [14] | start → `לנחש` |
| `-c-intro` | narration | — | — |
| `-ramban` | Ramban | [17] | whole |
| `-ibn-ezra` | Ibn Ezra | [18] | whole |
| `-shadal` | Shadal | [19] | whole |
| `-q-c1`, `-q-c2`, `-q-c3` | questions | [21], [22], [23] | whole |
| `-malbim` | Malbim | [20] | `והוא זרות` → `שעל זה לא נזהר;` |
| `-ayelet` | Ayelet HaShachar | [27] | from `כל מקום` |
| `-q-c4`, `-q-c5` | questions | [24], [25] | whole |

The three Akeidah cards are consecutive slices that together cover the item from `הצמיח לו` to its
end; only her label `עקדת יצחק, שער השביעי:` is left off.

**Akeidah «לעונשים».** Checked on Sefaria: *Akeidat Yitzchak* 7:1:6 (Pressburg 1849) reads
«היותר נאותים **לאנשים** לבלות ימיהם בטוב». The reading "people" is confirmed by the printed text, so the
English says "for people" with no bracket. Her Hebrew (as digitized, `לעונשים`; scan vav unclear) is
unchanged.

**The Malbim gap ([20]).** The scan check found that the digitization dropped the clause «פרושים בדבר ה'
מסברתו, שעל זה נענש הנביא בבית אל שפרש». After the harvest fix the item is the digitization again (gap
included). **The card stops at `שעל זה לא נזהר;`, before the gap**, which still carries what her Q4 and
Q5 ask about. Not quoted: the rest of Malbim's comment. Its `*` (her «(* עיין למטה)») is kept; it points
at the Ayelet HaShachar card that follows.

**Order.** Scan order is kept for sources (Akeidah; Abarbanel, Ibn Kaspi; Ramban, Ibn Ezra, Shadal,
Malbim, Ayelet HaShachar); the Ayelet HaShachar note precedes the questions, as in the scan. In §ג,
questions 1–3 follow Shadal; 4–5 follow the Malbim they ask about.

**Questions omitted:**
- §ג [26] «6. במה מנוגדת דעתו לדעת בעל העקדה (ע' שאלה א)?»: triage not-published (internal cross-reference).
- §ד [31], [33]: the whole section is out (the editor's).

**NOT-IN-SCAN sources quoted:** none. **Open triage items:** none.

**Translation choices worth a second look:**
- Akeidah «(משלי ה')» translated as printed, "(Proverbs 5)" (the verse is Prov 8:35). «הודה כי» → "He indicated that".
- Abarbanel «קצה ההפלגה – לא מהמצוע» → "the extreme of excess, not of the mean"; «בשווי ובמצוע מהאיכויות» →
  "in balance and in the mean among the qualities".
- Ibn Kaspi «כי אינו רק בקצה גבולו» → "for it is only at the edge of its border".
- Malbim «כלל ר"י» → "rule 210".
- Ayelet HaShachar «דרוש» → "a teaching"; «ממנו מן» → "“mimmenu… min”".

---

## 1968 (תשכ"ח), sheet 160442 — `sn-1968`, 25 steps

**Sections rendered:** ב, ד, ו.

| Section id | Panel | Steps |
|---|---|---|
| `sn-1968` "1968 · The Sound in the Garden" | Gen 3:8 | 11 |
| `sn-1968-gave` "“The Woman You Put at My Side”" | Gen 3:12 | 6 |
| `sn-1968-duped` "“The Serpent Duped Me”" | Gen 3:13–14 | 8 |

**Cards → harvest** (`bereshit-harvest/sin/1968.json`):

| Card | Type · label | [i] | Slice |
|---|---|---|---|
| `-intro` | narration | — | — |
| `-br-19-7` | Bereshit Rabbah | [6] | start → `בתחתונים היתה` |
| `-br-19-7b` | Bereshit Rabbah | [6] | from `כיון שחטא` |
| `-rashi` | Rashi | [7] | whole |
| `-moreh` | Rambam, Moreh Nevukhim | [8] | from `"ההליכה"` (after her label) |
| `-radak` | Radak | [9] | whole |
| `-ramban` | Ramban | [10] | from `(אחרי` (drops only the label `רמב"ן,`) |
| `-q-b1`…`-q-b4` | questions | [11]–[14] | whole |
| `-d-intro` | narration | — | — |
| `-rashi-3-12` | Rashi | [21] | whole |
| `-ramban-3-12` | Ramban | [22] | whole |
| `-q-d1`…`-q-d3` | questions | [23]–[25] | whole |
| `-f-intro` | narration | — | — |
| `-rashi-3-13` | Rashi | [40] | whole |
| `-mizrachi` | R. Eliyahu Mizrachi | [41] | from `לא לשון` |
| `-gur-aryeh` | Gur Aryeh | [42] | from `לא לשון` |
| `-rashi-3-14` | Rashi | [43] | from `ד"ה` |
| `-reem` | Re'em | [44] | from `יש לתמוה` |
| `-heilprin` | R. Eliezer Heilprin | [45] | from `לפי מה` |
| `-q-f2` | question | [47] | whole |

Slices that start late drop only her lead-ins (`ר' אליהו מזרחי, מפרש את דבריו:`, `גור אריה:`,
`והשווה פסוק י"ד, רש"י:`, `הרא"ם, מקשה על דברי רש"י האחרונים:`, `ר' אליעזר היילפרין, בפרושו לרש"י "באורי מוהרא"ל":`,
`רמב"ם מורה נבוכים א פרק כ"ד:`); each name is on the card's label. [41] «ר' אליהו מזרחי» and [44] «הרא"ם»
are **the same person**; each card keeps her attribution.

**Moreh Nevukhim ([8]).** Re-triaged `form` (publishable) after this leaf's first draft flagged the
old "verse-reference label" decision as a misfile. Now quoted in her order (after Rashi), with her two
glosses («(= שמוש זה שכיח בלשון)», «(=השמועה … פירוש אבן שמואל)») kept in Hebrew and English. Her Q2 [12]
("sort the commentators into groups") now has all its sources on screen.

**Bereshit Rabbah [6]** carries her `*` after «היתה» (a pointer to `* עיין עלון ההדרכה.`, not published).
It's shown as two consecutive slices, `… עיקר שכינה בתחתונים היתה` and `כיון שחטא …`, so the lone `*`
(and the comma after it) is the only thing not shown. Both halves are needed: R. Chalafon's "fire" for her
Q4, R. Abba bar Kahana's ascent of the Shekhinah for her Q3.

**Her spelling «נתת» (§ד).** The scan spells «נתת» throughout. After the harvest fix, only [25] (her
question) carries it; Rashi [21] and Ramban [22] now read the digitization's «נתתה» in their dibbur
(see harvest regressions). The panel is MAM («נָתַתָּה»).

**Questions omitted:**
- §ו [46] «1. התוכל ליישב את קושיית הרא"ם בהתאם לתשובתך לשאלה במקטע ה?»: depends on her §ה, which isn't
  rendered. Her Q2 [47] keeps its number «2.».

**NOT-IN-SCAN sources quoted:** none. **Open triage items:** none.

**Translation choices worth a second look:**
- [8] Moreh «להמשיך הגופות» → "for the flowing of bodies"; «להתפשט ענין אחד והראותו» → "for the spreading
  and showing of a thing". Verse citations translated as printed.
- [10] Ramban: «באיוב (ל"א א')» translated as printed, "(31:1)" (the verse is Job 38:1). The open quote
  «"כי שמעו…» is left unclosed, as in the text.
- [22] Ramban «בכבודך» → "in Your glory".
- [25]: the verse inside her question is translated literally ("whom You gave (natatta)… she gave
  (natenah)"), because her question turns on the double «נתן» that the panel's JPS ("put at my side")
  hides.
- [43] Rashi «אין מהפכין בזכותו של מסית» → "one does not plead in favor of the inciter".
- [45]: «משיא»/«מסית» glossed "[one who deceives]" / "[one who incites]".

---

## Harvest regressions after the 2026-10-06 regeneration (for the coordinator)

The fixed harvester (exact, unique fragment match) no longer applies some scan fixes these leaves had relied on:
- 1944 [7]: her «פסוק ח'» → back to the digitizer's «פסוק ה'». Card shortened to avoid showing it.
- 1944 [28]: her «קולן של אילנות» → back to «קולו». Quoted as is; the English doesn't change.
- 1968 [21], [22]: her «נתת» in the dibbur → back to «נתתה». Quoted as is; the English doesn't change.

## Lib gaps (not changed)

- No way to show non-adjacent slices of one item in one card; split cards are used for 1968 [6]
  (around her `*`).
