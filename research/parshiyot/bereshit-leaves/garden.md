# Theme 2: Adam, the garden and the woman (Gen 2:4–25), Stage 4 leaves

Code: `research/scripts/bereshit_leaves/garden.py` (`leaf_1952`, `leaf_1953`, `leaf_1965`).
Check: `python3 research/scripts/check_leaves.py garden` → 7 sections, 86 steps, 0 failing checks
(1952: 28 steps; 1953: 37; 1965: 21).

Every commentary and question card is a verbatim `cut()` of a harvest item
(`bereshit-harvest/garden/<year>.json`). All English is ours (`en_basis: "ours"`): no card quotes
a whole item whose Sefaria English matches her slice. Section titles are content titles; her scan
headers are kept as comments in the code.

## Harvest regeneration (2026-10-06, second pass)

The first draft worked around defects in the harvest: checker `[?]` marks written into her text,
scan fixes applied to the wrong fragments, and bold tags turned into spaces. The harvest was then
fixed and regenerated: doubtful readings are no longer written in, only exact fragment matches are
applied, scan-only items have explicit keys (`after 24`, `after 24.2`, …), `item()` refuses any
item carrying checker marks, and `commentary()` takes `he_dir='ltr'`. This pass re-reads the
regenerated files, restores the full quotes and the omitted questions, and adds 1953's
printing-error note.

Where an item fell back to the digitization's reading, the card now shows the digitized spelling,
for example 1953 [10] «אינו … שפירש» and 1965 [24] «עילה».

**Third regeneration:** 1953 [46] (§ו Q1) now reads cleanly, in the digitized wording (a
spelling-only difference; triage updated). `after 24` (Ramban's verse list) is settled as «כ"ג»,
with no `[?]`. Both are now quoted.

---

## leaf_1952: gilayon תשי"ב (161471), «בהשואת שני הפרקים»

**Sections rendered:** §א, §ב, §ד (panel Genesis 2:5–8); §ו, §ז, §ח (continuation panel Genesis
2:15–18, titled "To Till It and Tend It"). Leaf title: "1952 · Chapter 1 and Chapter 2".

| Card | Type | Harvest [i] | Slice (start → stop) | Notes |
|---|---|---|---|---|
| `gd-1952-intro` | narration | — | — | |
| `gd-1952-a-verse` | narration | — | — | |
| `gd-1952-rashi` | Rashi | [2] | `כל טרם` → `עמדו עד יום ו'` | her pointer is one ד"ה (`טרם יהיה בארץ`); the digitizer's ref is `2:5:1-2`, so I stop before `ולמה, כי לא המטיר` (the next ד"ה) |
| `gd-1952-ramban` | Ramban | [3] | `על דעת רבותינו` → end | bare pointer, no stop |
| `gd-1952-q-a1` | question | [4] | whole | |
| `gd-1952-q-a2` | question | [5] | whole | |
| `gd-1952-q-a3` | question | [6] | whole | |
| `gd-1952-sforno` | Sforno | [7] | `אמנם` → `עדיין לא היה בארץ` | **NOT-IN-SCAN, quoted under rule 6** (her Q4 names Sforno). The stop drops the tail clause, which ends in the digitizer's typo `צמא` (for צמח) |
| `gd-1952-q-a4` | question | `after 6` (scan-only) | whole | her lost Q4, placed after Sforno, the source it asks about |
| `gd-1952-b-intro` | narration | — | — | |
| `gd-1952-jacob` | Benno Jacob | [10] | `לא נאמר` → `י"ד ה'` | skips the attribution line; the stop omits a trailing ` .`. Still shows the harvest's double comma `קיימת,,` |
| `gd-1952-q-b1`–`b3` | question | [11], [12], [13] | whole | |
| `gd-1952-d-intro` | narration | — | — | |
| `gd-1952-rashi-mikedem` | Rashi | [20] | `ואם תאמר` → `וללמד על העופות` | **her start and stop** (scan header); the digitized text runs on past her stop |
| `gd-1952-q-d1`–`d3` | question | [21], [22], [23] | whole | |
| `gd-1952-v-intro` | narration | — | — | |
| `gd-1952-chizkuni` | Chizkuni | [34] | whole | |
| `gd-1952-q-v1` | question | [35] | whole | |
| `gd-1952-q-v2` | question | [36] | whole | |
| `gd-1952-q-z` | question | [39] | whole | harvest `kind: text`, but it's her §ז question (unnumbered on the scan too); now reads «בפרק ג' י"ט,», the scan's punctuation |
| `gd-1952-adrn` | Avot de-Rabbi Natan | [40] | `שמעיה אומר` → `אכול תאכל"` | harvest `kind: question`, but it's the source. Skips her `(והשוה … בשבח העבודה:` lead-in and closing `).`. **Her underline** `לא טעם כלום עד שעשה מלאכה` is reproduced in Hebrew and English. Follows her question, as on the scan |
| `gd-1952-h-intro` | narration | — | — | |
| `gd-1952-akeidah` | Akeidat Yitzhak | [42] | `ולזה ראתה` → end | the full quote, skipping her label `עקדת יצחק:` and the opening `...` (the English keeps "…") |
| `gd-1952-q-h` | question | [43] | whole | restored. The digitized reading «מהם» stands, since the scan's punctuation mark was doubtful |

**Questions omitted:** none.

**Not quoted:** [1], [19], [33], [38] (the verses, which are on the panel); [9] (the verse pointer).
[19] Genesis 2:8 is NOT-IN-SCAN anyway.

**Translation choices worth a second look:**
- Rashi [2]: «ואינו נפעל לומר הטרים כאשר יאמר הקדים» → "it cannot be made into a verb, to say
  'hitrim' as one says 'hikdim'".
- Ramban [3]: «אד» → "flow", matching the panel's JPS 2:6; «תשמישו של עולם» → "the working of the world".
- Jacob [10]: «כנגד איזו שיטה בספרות המדעית» (Q3) → "which approach in the scholarly literature".
- Akeidah [42]: «היחס המיני» → "the sexual bond"; «יחס אישי מיוחד» → "a special personal bond";
  «הרועים על ידיהם» → "grazing beside them"; «ולזה אעשה לו» → "and for this, 'I will make him'…".
- Rashi [20] ends at her stop, "and to teach about the birds", mid-thought, as she cut it.

---

## leaf_1953: gilayon תשי"ג (161223), «בריאת האשה»

**Sections rendered:** §ב, §ג, §ד (panel Genesis 2:18–20); §ו (continuation panel Genesis
2:23–24, titled "One Flesh"). Leaf title: "1953 · A Helper Against Him". No Leningrad image
(§7a dropped the 1953 moment); her shva question is text only.

| Card | Type | Harvest [i] | Slice (start → stop) | Notes |
|---|---|---|---|---|
| `gd-1953-intro` | narration | — | — | |
| `gd-1953-rashi` | Rashi | [6] | whole | |
| `gd-1953-sforno` | Sforno | [7] | whole | |
| `gd-1953-chizkuni` | Chizkuni | [8] | whole | |
| `gd-1953-q-b1` | question | [10] | whole | restored. Placed after Sforno, since it sets Rashi against Sforno |
| `gd-1953-q-b2` | question | [11] | whole | after Chizkuni, the source it asks about |
| `gd-1953-shadal` | Shadal | [9] | whole | |
| `gd-1953-q-b3` | question | [12] | whole | |
| `gd-1953-g-intro` | narration | — | — | gives the Hebrew *ezer kenegdo*, "a helper against him", because the JPS "fitting counterpart" hides the word the sources are about |
| `gd-1953-rashi-ezer` | Rashi | [15] | whole | |
| `gd-1953-q-g2` | question | [19] | whole | moved up to follow Rashi (rule 8); on the scan all three questions follow Shadal |
| `gd-1953-gur-aryeh-a` | Gur Aryeh | [16] | `וכך פירוש` → `קרוב לפשוטו.` | skips her intro line. **Her underlines** `חשובה ושקולה כמו האיש` and `מדרש זה, שאינו קרוב לפשוטו` are reproduced |
| `gd-1953-gur-aryeh-b` | Gur Aryeh | [16] | `ויש בזה דבר נעלם` → end | starts where her Q3 points. **Her underlines** `כי כל שני הפכים מתחברים בכח אחד` and `שהשם ית' שעושה שלום…מקשר ומחבר אותם`. The one `glow` in this leaf |
| `gd-1953-q-g3` | question | [20] | whole | restored |
| `gd-1953-shadal-ezer` | Shadal | [17] | whole | |
| `gd-1953-q-g1` | question | [18] | whole | the checker couldn't read the last word (`ב[?]נו`); the digitization reads `בפסוקנו`, and `basis: digitization` is quotable |
| `gd-1953-d-intro` | narration | — | — | |
| `gd-1953-ibn-ezra` | Ibn Ezra | [23] | `וטעם ולאדם לא מצא` → `אל השם` | **her start and stop** (scan: `ראב"ע: י"ח ד"ה ויאמר החל מן … עד "אל השם"`) |
| `gd-1953-q-d3` | question | [27] | whole | follows Ibn Ezra |
| `gd-1953-ramban` | Ramban | [24] | `והנכון בעיני` → `ואת שמואל` | **her start and stop**. The harvest has `ואת שמואל ( שמואל א' י"ב י"א ).`; the stop drops the citation, as she did |
| `gd-1953-nechama-verses` | Nechama Leibowitz | `after 24` (scan-only) | whole | her list of the two verses Ramban cites (Gen 4:23; I Sam 12:11), in her order, before the printing-error note |
| `gd-1953-nechama-note` | Nechama Leibowitz | `after 24.2` (scan-only) | whole | her printing-error note, right after the Ramban sentence it corrects; Q4/Q5 lean on that sentence. The English transliterates the corrected reading («ולא מצא כנגדו בדרך "נשי למך"») so the correction stays visible |
| `gd-1953-q-d4`, `d5` | question | [28], [29] | whole | follow Ramban |
| `gd-1953-q-d1`, `d2` | question | [25], [26] | whole | |
| `gd-1953-q-d6` | question | [30] | whole | her Masoretes/shva question. The harvest has no `6.` (the digitizer dropped it; the scan has it) and keeps the digitized `המסורת … ולְאדם בשווא`; quoted as the harvest has it |
| `gd-1953-jacob` | Benno Jacob | [32] | `Aber` → `Gegenstueck` | German, `he_dir='ltr'`; the stop omits the final period, which would jump to the wrong side in an RTL block |
| `gd-1953-buber` | Buber-Rosenzweig | [33] | `Aber` → `zuseiten` | `he_dir='ltr'` |
| `gd-1953-q-d-a` | question | [34] | whole | |
| `gd-1953-q-d-b` | question | [35] | whole | restored |
| `gd-1953-v-intro` | narration | — | — | |
| `gd-1953-pdre` | Pirkei de-Rabbi Eliezer | [43] | `מכאן אתה למד` → end | the full quote, skipping her label line |
| `gd-1953-rashi-24` | Rashi | [44] | `רוח הקודש` → `(סנהדרין נ"ז).` | her pointer is `ד"ה על כן יעזב` only; the digitizer added `ד"ה לבשר אחד`, which is left out |
| `gd-1953-q-v1` | question | [46] | whole | restored; placed after Rashi, the source it asks about |
| `gd-1953-ramban-24` | Ramban | [45] | `ואין בזה טעם` → end | bare pointer (ditto of `ד"ה על כן יעזב`). Skips the digitizer's `(אחרי הביאו לשון רש"י)`. The English carries a bracket, "[Rashi's explanation of 'one flesh', that the child is formed by both of them]", because Ramban rejects Rashi's second comment, which he quotes in full and which is not on the panel |
| `gd-1953-q-v2` | question | [47] | whole | |

**Questions omitted:** none.

**Her prose not quoted:**
- [31] «(והשוה את דברי המתרגמים:», a dangling lead-in. The Jacob and Buber cards follow it directly.

**Translation choices worth a second look:**
- Ibn Ezra [23]: «ולנפשו לא מצא» → "and for himself he did not find".
- Ramban [24]: «ולשם האדם… ותקרא בשמו שיוליד ממנו» → "for the name of Adam … and be called by his
  name, one by whom he would beget".
- Buber-Rosenzweig [33]: the harvest reads «erfand sich» (probably «fand sich»). It's rendered
  impersonally, "no help was found", against Jacob's "he found", because that contrast is what her
  (ב) asks about.
- Gur Aryeh: «חשובה ושקולה כמו האיש» → "of worth and of equal weight with the man".
- Pirkei de-R. Eliezer: «ממצות כבוד» → "[and so depart] from the commandment of honoring [them]".
- Q6 [30]: «בנקדם ולְאדם בשוא ולא בקמץ» → "in pointing 'u-le-adam' with a shva and not with a kamatz".

---

## leaf_1965: gilayon תשכ"ה (160577), «האדם»

**Sections rendered:** §ג (panel Genesis 2:7); §ד (continuation panel Genesis 2:8, 15, "Taken
into the Garden"); §ו (continuation panel Genesis 2:19, "What He Would Call Them"). Leaf title:
"1965 · The Human Being". Sources are in **her order**, which differs from the order in the
assignment: §ג Taanit, Bereshit Rabbah, R. David HaNagid; §ד Bereshit Rabbah, Rashi, Radak; §ו
Wessely, Sforno.

| Card | Type | Harvest [i] | Slice (start → stop) | Notes |
|---|---|---|---|---|
| `gd-1965-intro` | narration | — | — | |
| `gd-1965-taanit` | Taanit | [16] | whole | her bracketed Rashi/Maharsha glosses kept. **Her underlines:** `נשמה שנתתי בך – החייה` (digitized bold, MATCH) and `לסגף` (scan only, per the scan check) |
| `gd-1965-br-14` | Bereshit Rabbah | [17] | whole | her glosses kept. **Her underline** `מכור לצמיתות, משועבד` |
| `gd-1965-q-g3` | question | [21] | whole | follows the midrash it asks about |
| `gd-1965-david-hanagid` | R. David HaNagid, son of Rabbenu Avraham ben HaRambam | [18] | `ואני אומר` → end | skips her attribution line; the label is her attribution |
| `gd-1965-q-g1`, `g2` | question | [19], [20] | whole | |
| `gd-1965-d-intro` | narration | — | — | notes that 2:15 opens with *va-yikkah*, "and He took", since JPS renders it "settled" |
| `gd-1965-br-16` | Bereshit Rabbah | [24] | whole | restored in full (R. Yehuda's «עילה», the digitized reading) |
| `gd-1965-rashi` | Rashi | [25] | whole | |
| `gd-1965-q-d2` | question | [28] | whole | restored. Placed after Rashi, since it asks why Rashi didn't bring the midrash on 2:8 |
| `gd-1965-q-d3` | question | [29] | whole | follows Rashi |
| `gd-1965-radak` | Radak | [26] | whole | |
| `gd-1965-q-d4` | question | [30] | whole | |
| `gd-1965-q-d1` | question | [27] | whole | closes the section |
| `gd-1965-v-intro` | narration | — | — | |
| `gd-1965-wessely` | R. Naftali Hirz Wessely, Imrei Shefer | [40] | `חפץ ה'` → end | skips the attribution line; the label is hers |
| `gd-1965-sforno` | Sforno | [41] | whole | |
| `gd-1965-q-v1` | question | [42] | whole | |
| `gd-1965-q-v2` | question | [43] | whole | **[43] Psalms reference:** the harvest carries the scan's «תהלים ק"ד כ"ח» (triage `use: scan`: Shadal on 2:19 cites 104:28). English "Psalms 104:28" |
| `gd-1965-q-v3` | question | [44] | whole | |

**Questions omitted:** none.

**Translation choices worth a second look:**
- Bereshit Rabbah 16:5: the Hebrew cites «(ישעיהו ס"ג ג')» and «(הושע ד' ג')». The verses are
  Isaiah 14:2 and Hosea 14:3. The English translates what's written and adds the correct reference
  in brackets: "(Isaiah 63:3 [14:2])", "(Hosea 4:3 [14:3])", following the coordinator's ruling.
  «עילה אותו» → "He raised him up".
- Bereshit Rabbah 14:10: Lam 1:14 is rendered "“The Lord has given me into the hands of… I am not
  able (lo ukhal) to rise”…", literally and with the transliteration, so the English doesn't settle
  how R. Huna reads it (her Q3).
- Radak: «ופירוש "ויניחה"» (the digitizer's spelling) → "and the meaning of 'and put him'".
- Q4 [30]: «מחמש בראשית ט"ז ג'» → "from the Torah, Genesis 16:3".
- Q1 [42]: «מבחינה תחבירית» → "syntactically".

---

## Lib gaps

The first pass reported three: the second scan-only item was unreachable, there was no LTR slot for
German, and checker marks went undetected. All three are closed by the regeneration (explicit
`after N.k` keys, `he_dir`, the markup check in `item()`). Nothing open.
