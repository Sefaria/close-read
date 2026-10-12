# Theme 2: The Flood (Genesis 7:1–8:21). Paper trail for the leaves

Module: `research/scripts/noach_leaves/flood.py` (`leaf_1945`, `leaf_1952`, `leaf_1962`, prefix `fl-`).
Check: `python3 research/scripts/check_leaves.py noach flood` → 10 sections, 88 steps, **0 failing checks**
(1945: 29 steps, 1952: 27, 1962: 32).

All Hebrew is a `cut()` slice of `noach-harvest/flood/<year>.json`. All English is ours (`en_basis: "ours"`);
no item is quoted whole *and* canonical, so no Sefaria English is used. Verse Hebrew and English come from
`primary()`. Every card's `[i]` below is the harvest index.

---

## 1945 (תש"ה), sheet 161721. Sections א, ב, ה

Scan check: `noach-scancheck/161721-1945.md`. §ג (Rashi details), §ד («בעצם») and §ו (בקיאות) are not rendered (pack §7).

### Panels (five sections: one title card, four continuations)

| Section id | Title | Panel | Her section |
|---|---|---|---|
| `fl-1945` | 1945 · How the Flood Is Told | Genesis 6:22; 7:1, 5, 16 | §א Q1–Q2 |
| `fl-1945-order` | Beasts, Cattle, Birds | Genesis 7:14, 21, 23 | §א Q3–Q4 |
| `fl-1945-forty` | The Waters Swelled | Genesis 7:17–20 | §א Q5, Ramban |
| `fl-1945-perished` | All Flesh Perished | Genesis 7:21–24 | §א Q6 |
| `fl-1945-shut` | The Lord Shut Him In | Genesis 7:13, 16 | §ב, then §ה |

Her §א pointers [2]–[6] (6:11, 6:12, 6:13, 6:22, 7:1/7:5) and [8], [11]–[13], [19] (verse excerpts) are
verse text: they are the panels, not cards ([2] is also `publish: false`). The first panel shows the verses
whose divine name differs: 6:22 (אלהים) against 7:1, 7:5 (ה'), and 7:16 (אלהים again). 6:11–13, which
she also pointed at (each with «אלוקים»), are left out to keep the panel short; 6:22 carries the contrast.

### Cards

| Step | [i] | Slice | Note |
|---|---|---|---|
| q-a1 | 1 | whole | Q1, scan wording (number "1." from the harvest) |
| q-a2 | 7 | whole | Q2, digitized wording (triage: form only) |
| q-a3 | 9 | whole | Q3 (no number: the digitizer dropped it) |
| q-a4 | 10 | whole | Q4 lead «הסבר את הסדר השונה בפסוקים הבאים:»; the verses she lists (7:21, 7:23) are lit |
| q-a5-lead | 14 | whole | «שים לב לתאור» (her lead to Q5), lit on 7:17–20 |
| q-a5a | 15 | whole | |
| q-a5b | 16 | whole | |
| ramban-a | 17 | to «בריבוי גדול.» | Ramban on 7:18; her pointer «עיין רמב"ן י"ח וטעם ויגברו המים» = the item's start |
| ramban-b | 17 | from «וייתכן כי טעם» | his second interpretation |
| q-a5c | 18 | whole | «שים לב לשני פרושיו!», after the two Ramban cards |
| q-a6 | 20 | whole | Q6 |
| b-rashi-13 | 22 | from «לימדך» | Rashi 7:13 (her pointer, no stop) |
| b-rashi-16 | 23 | from «הגין» | Rashi 7:16; her stop «עד "ופשוטו"» = where the digitized item ends |
| b-rashi-ezek-a | 24 | «נח נמלט משלושתן» … «כו' בבראשית רבה.» | Rashi on Ezekiel 14:14 (her «וע'»), the passage on Noah and the beasts |
| b-rashi-ezek-b | 24 | from «מן החרב» to end | the generation's threat; «בעצם היום הזה» |
| q-b1 | 25 | whole | |
| q-b2 | 26 | whole | |
| h-onkelos | 46 | from «ואגן» | EXPANDED (her «ע' ת"א»); her Q1 counts him among «שלשת המפרשים» |
| h-malbim | 47 | whole | scan wording |
| h-nachalat | 48 | from «על ידי» | |
| q-h1 | 49 | whole | scan wording (triage: scan) |
| h-ibn-ezra | 50 | «וטעם "ויסגור» … «כולם מתים» | exactly her range «החל מן "וטעם ויסגר ה' בעדו" עד "כלם מתים"»; the item's trailing «?» belongs to her lost Q2 and is left out |
| q-h2 | 'after 50' | whole | scan-only Q2 |

The Ezekiel Rashi is sliced, not quoted whole: the item opens with the first reading of the verse and carries
a printer's gloss «(הרי זה מהלך סדר פרשה זו כולה לשון זה אין ליישבו ונראה שאינו לשון הרב…)». The famine
paragraph between the two slices («מן הרעב…») is left out as off the Flood.

### Omitted
- [5], [6]: verse pointers (the digitizer labelled [5] «Rashi on Genesis 7:5:1»; it is 6:22). In the panel.
- Nothing of her §א, §ב, §ה questions is omitted.

### Settled / worth a look
- **Q3's verse.** The scan's number before Q3 reads «י"ז[?]»; the digitizer linked 7:14. 7:17 names no
  creatures; 7:14 is where the birds come last after beasts, cattle and creeping things. Q3 is bound to 7:14,
  and Q4 (7:21, birds first; 7:23, birds last) follows it on the same panel.
- **Ramban's ref.** The harvest says «Ramban on Genesis 7:16:1»; her pointer says verse י"ח, and Sefaria's
  Ramban on Genesis 7:18 is this comment («[יח-יט] וטעם ויגברו המים…»). Card ref: `Ramban on Genesis 7:18`.
- **Translation.** «ר,ב,ה – ג,ב,ר» → "r-b-h (rabah) – g-b-r (gavar)"; Ramban's prooftexts keep the Hebrew word
  in transliteration (yitgabberu, gavar, bi-gvurot) because his point is the root. Ezekiel Rashi «ודרגיש ליה
  ימלל» → "whoever has the strength to stir, let him speak!"; «ליזדווג לו» → "set upon him"; the Daniel
  citation printed «(דניאל ז')» is glossed "[6:23]". Ibn Ezra «והעד ראש הפסוק» → "the evidence is the
  beginning of the verse" (left literal; the card lights 7:16's opening «והבאים» with «ויסגר»).
  Onkelos «ואגן ה' (במימרה) עלוהי» → "And the Lord (by His Word) shielded him."

---

## 1952 (תשי"ב), sheet 161472. Sections א, ב, ג (her whole sheet)

Scan check: `noach-scancheck/161472-1952.md`. The pre-section note [0] (pointer to her 1946 sheet on 8:21) is
not rendered.

| Section id | Title | Panel | Her section |
|---|---|---|---|
| `fl-1952` | 1952 · God Remembered Noah | Genesis 8:1 | §א |
| `fl-1952-b` | “Come Out of the Ark” | Genesis 8:5, 9, 15–16 | §ב |
| `fl-1952-c` | The Raven and the Dove | Genesis 8:7–8, 13–14 | §ג |

### Cards

| Step | [i] | Slice | Note |
|---|---|---|---|
| rashi | 3 | from «מה זכר» | EXPANDED pointer, no stop |
| ramban | 4 | «אבל הזכירה» … «שלא יכלו בתיבה» | exactly her range |
| q-a-a … q-a-d | 5, 6, 7, 8 | whole | her (א)–(ד), harvest letters «א.»–«ד.» → "a."–"d." |
| ibn-ezra | 9 | from «כלל» | her stop «עד "וטעם"»: the digitized item already ends before it |
| q-ie-a, q-ie-b | 10, 11 | whole | |
| br | 14 | whole | ref BR 33:6 (triaged; her citation is «ל"ג ח'»); digitized «ישבה» stands (triage: Sefaria's reading; her «יצאה» is a slip) |
| q-b-a, q-b-b | 15, 16 | whole | |
| aggadat | 18 | from «"צא מן התבה"» | drops the item's «2. אגדת בראשית פרק ז'» label; ref Aggadat Bereshit 7:1 (her text is an abridgment of 7:1's close) |
| tanchuma | 20 | from «"בעשירי» | drops the «תנחומא ישן פרשת נח י"ד:» label; label "Tanchuma Yashan" (hers); no ref given |
| q-b2-a … c | 21, 22, 23 | whole | |
| q-c1 | 28 | whole | lit on «וישלח את הערב» / «וישלח את היונה מאתו» |
| q-c2 | 30 | whole | verse list fixed by overrides (37:13–14) |
| c-rashbam | 31 | from «משקל דגש» | her «וע' רשב"ם … ד"ה וישלחנו» |
| q-c2-rashi | 32 | to «כאן:» | her pointer, cut out as a question card (brief) |
| c-rashi | 32 | from «אין זה» | Rashi 8:8 |
| q-c3 | 37 | whole | lit on 8:13 «חרבו פני האדמה» / 8:14 «יבשה הארץ» |

### Omitted
- [25] «1. השוה:», [34] «השוה:», [29] the lemma «וישלח את היונה», and the verse items [2], [13], [17],
  [26], [27], [35], [36]: carried by the panel and its highlights. Consequence: the "1." of §ג Q1 isn't shown
  (the digitizer had already dropped numbers 2 and 3).
- [19] her parenthesis «(פרופ' הינמן: דרכי האגדה 86 מעיר, שפילון משבח את נח…)»: her own pointer to
  Heinemann on Philo, not a quoted source; a card would have to label her sentence with Heinemann's name.
- [33] «ועיין גליון וירא תש"י שאלה ב' 1, תולדות תשי"א ה.»: a pointer to two other gilyonot, which the reader
  doesn't have.
- No question is omitted.

### Settled / worth a look
- **Rashbam's chapter.** The scan's chapter letter is broken («י"ח[?]»); the digitizer has 19:13. «וישלחנו»
  (the angels sent to destroy Sodom) is 19:13, and the Rashbam text is about exactly that; 19:13 stands.
- **«מאתו».** She underlines it in 8:8; JPS doesn't translate it, so the English side of the `yona` group can
  only be "Then he sent out the dove" (the Hebrew group includes מאתו).
- **Translation.** BR «וכדכוותיה ( = וכיוצא בו)» → "And likewise (= and similarly)", keeping her gloss;
  «ר"ש» → "R. Shimon". Aggadat Bereshit «אני פי מלך שמור» → "I [say]: keep the king's command."
  Rashbam's «כאילו כתב משקל דגש» → "it is written as if in the heavy form" (the digitized sentence is
  compressed; we didn't fill it out). Q c2 «בלשון קל וישלח במקום פיעל» → "the qal, 'va-yishlach,' instead of
  the pi'el".

---

## 1962 (תשכ"ב), sheet 160700. Sections א, ב, ד

Scan check: `noach-scancheck/160700-1962.md`. §ג (Ibn Kaspi on «עד») is not rendered (pack §7). No Perlman box.

| Section id | Title | Panel | Her section |
|---|---|---|---|
| `fl-1962` | 1962 · A Hundred and Fifty Days | Genesis 7:24–8:2 | §א, then §ב (8:1 is in the panel) |
| `fl-1962-d` | Noah’s Offering | Genesis 8:16, 20–21 | §ד, in the scan's order |

### Cards

| Step | [i] | Slice | Note |
|---|---|---|---|
| ibn-ezra | 3 | from «ויגברו המים חמשים» | drops «ראב"ע: ד"ה (ז' כ"ד)»; her printed text |
| wessely | 4 | from «השומע» | drops the label/bibliography; label "R. Naftali Hirz Wessely, Imrei Shefer" |
| cassuto-a | 5 | «ד"ה ויזכור» … «של ירידת הגשם.» | first paragraph |
| cassuto-b | 5 | from «הפירוש של פעלים» | second paragraph (her Q7 names it) |
| q-a1 … q-a7 | 6–12 | whole | her order, after all three sources |
| b-ibn-ezra | 17 | from «חלילה» | drops «פסוק א'»; label "Ibn Ezra, in his other commentary" (her «בפרושו בשיטה אחרת») |
| b-ramban | 18 | from «הזכירה בנח» | the whole of her printed excerpt, minus the lemma |
| b-bahya | 19 | from «להורות» | |
| b-kaspi | 20 | from «חלילה שיהיה» | |
| b-cassuto | 21 | from «זכירה זו» | |
| q-b | 22 | whole | |
| q-d2 | 32 | whole | «2) השוה את שני המדרשים הבאים:» |
| br-34-9a | 33 | from «"ויבן" כתיב» | the verse quote that opens the item is in the panel |
| pdre | 34 | from «ישב נח» | harvest `kind: question`, but it is the PdRE text |
| q-d2-q | 35 | whole | |
| br-34-9b | 36 | from «"וירח ה'» | |
| q-d3a … c | 37, 38, 39 | whole | |
| br-34-6 | 28 | from «"צא מן התיבה", כתיב» | ref BR 34:6 (triaged; her citation «ל"ד (ד'[?])» is smudged) |
| q-d1a … c | 29, 30, 31 | whole | |

**Her order in §ד.** The scan prints block 2) ([32]–[35]), then 3) ([36]–[39]), then 1) ([28]–[31]) last;
the digitization moves 1) first. The leaf follows the scan.

### Omitted
- [1], [2], [14]: verse items (panel). [15] «ראב"ע» and [16] «בפרושו בשיטה אחרת (הוצאת מ. פרידלנדר…»:
  label and edition note, carried by the card's label.
- No question is omitted (all 7 of §א, the one of §ב, all 7 of §ד).

### Settled / worth a look
- **Wessely «למטרות עוזו».** Triage kept the digitization; the scan's first word has an ink spot. It is Job
  37:6, «וגשם מטר וגשם מטרות עזו»: "to make an end of 'the rains of His might'". Translated so, with the
  citation added in parentheses.
- **Cassuto's «(בראשית ו' א'-ב' ג')».** Both the scan and the digitization read ו' for the creation account
  (1:1–2:3). Not typed over; the English gives "Genesis 1:1–2:3 [printed as 6:1]".
- **BR 34:9 on 8:21 [36].** The digitized text is her abridgment and has an unbalanced quote mark
  («דסבך" וירח ה'…»); quoted as is. «דורן של שמד» → "the gift of the persecution" (i.e. the martyrs of the
  persecution); «מה דמי דורון דידך לדורון דסבך» → "How like your gift is to your grandfather's gift!".
- **BR 34:9 on 8:20 [33].** «"ויבן" כתיב – נתבונן» kept as wordplay: "'Va-yiven' [and he built] is written:
  nitbonen [he considered]."
- Ibn Kaspi «ויותר נמרץ מזה אמרו עוד… "כריתת ברית"» → "more forcefully than this, it says further, of the
  beasts and the cattle, 'making a covenant'" (9:10's covenant).

---

## Lib / harness notes
- Nothing missing from the lib.
