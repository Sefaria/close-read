# Parashat Bereshit — Nechama Leibowitz Research Pack

> Source of truth for the future `data/bereshit.json`. Every claim about Nechama in the
> Close Read must trace back to an entry here, and every entry here traces back to a
> raw file and a sheet index. If you can't cite it, don't ship it.

**Status:** Stage 1 (Survey) complete. Stage 2 (design) **decided 2026-10-06 (§7a)**; Stage 3
(scan check + harvest) is next. Nothing is harvested or drafted beyond the 1963 demo (§5b).

---

## 0. The evidence chain and how to cite it

The pack is built in layers. Each layer is derived from the one below it, and each can be
checked against that lower layer:

| Layer | What | Where | Who made it |
|---|---|---|---|
| **L0** | Original gilayon (typewritten scan) | `https://www.nechama.org.il/pdf/<n>.pdf`, linked from each sheet's summary; sha256 in `bereshit-raw/verification.json` | Nechama |
| **L1** | Sefaria digitization | `https://www.sefaria.org/sheets/<id>` (digitized 2019) | Sefaria digitizers |
| **L2** | Raw snapshot of L1, frozen in this repo | `bereshit-raw/<id>.json` + `manifest.json` (sha256 per file) | `research/scripts/snapshot_parsha.py` |
| **L3** | Mechanical extraction of L2: every header, ref, question and prose item, each with its index `[i]` into `sources[]` | `bereshit-survey.json`, `bereshit-survey.md` | `research/scripts/survey_parsha.py` |
| **L4** | This file: survey findings and the tentative clustering | `bereshit.md` | human/agent; interpretation is marked |

**Citation form** used here and in later stages: `161941[32]` means sheet 161941,
`sources[32]` in `bereshit-raw/161941.json`. Claims are tagged:

- **[extracted]**: produced mechanically from L2 by the scripts and reproducible by re-running them.
- **[PDF-checked]**: compared by eye against the L0 scan (5 of 30 so far; see §2.8).
- **[interpretation]**: a judgment by me (the survey author). Tentative, to be confirmed in review.

The **L1 digitization is not the same thing as Nechama's sheet.** §2 lists the ways it differs.
Anything that goes into the Close Read as "Nechama said/asked/chose" must be confirmed
against L0 for that specific sheet (Stage 3).

---

## 1. Provenance and method

### 1.1 How the corpus was found

- **Source:** local MongoDB `sefaria.sheets`, a production restore whose newest
  `dateModified` is 2026-08-15. Query: `{"owner": 54380, "topics.slug": "parashat-bereshit"}`.
- **Why not the API:** the first fetch attempt sent `User-Agent: Mozilla/5.0`, which
  Cloudflare challenges with a 403. Main has since standardized on
  `User-Agent: Sefaria/close-read`, which works (confirmed 2026-10-06), so the API is a
  valid source again. The Mongo snapshot was kept because it's verified identical to live (below).
- **Completeness sweeps** [extracted]:
  - Mongo: owner 54380 AND (title contains `בראשית` OR topic `parashat-bereshit` OR
    `includedRefs` matches `Genesis 1–6`). This returned the 30 tagged sheets plus sheets
    of *other* parshiyot that merely cite Genesis 1–6 (Noach, Vayera, Korach, …).
    No sheet titled `פרשת בראשית` is missing the tag.
  - Live (browser, 2026-10-06): of the user's 1455 live sheets, the set tagged
    `parashat-bereshit` and the set titled `פרשת בראשית` are identical, and both equal the
    30 snapshot IDs. (Mongo has 1456 sheets for the user; the one extra isn't in this set.)
- **Live content check** [extracted]: for all 30 sheets, a sha256 over every `sources[]`
  item's (ref, outsideText, outsideBiText.he/en, text.he/en) from the **live API** matches
  the same hash over the snapshot. **30/30 identical.** Method and hashes are in
  `bereshit-raw/verification.json`.
- **Original PDFs:** all 30 URLs resolve (HTTP 200, `application/pdf`); sha256 + size are
  recorded in `verification.json`. The PDFs are *not* committed to the repo (rights); the
  hashes let a later reader confirm they are looking at the same scan.

### 1.2 Reproduce

```bash
python3 research/scripts/snapshot_parsha.py bereshit parashat-bereshit   # L2 (needs local mongo)
python3 research/scripts/survey_parsha.py bereshit Genesis 1:31,2:25,3:24,4:26,5:32,6:8   # L3 (span = Gen 1:1–6:8)
```

### 1.3 Dating

- One sheet per year, **30 consecutive years, תש"ב (1942) → תשל"א (1971)** [extracted:
  Hebrew year from each title, Gregorian year from each summary. The survey script
  checks gematria(title year) + 5000 == Gregorian + 3760 and fails if they disagree.
  All 30 pass. See the "Year check" line in `bereshit-survey.md`].
- **Caveat:** the Gregorian label is the year in which the Hebrew year *ends*. Parashat
  Bereshit is read in the autumn, so the sheet labeled "1942 (תש"ב)" was studied in
  autumn **1941**. This survey keeps Sefaria's labels and doesn't silently re-date them.
  Narration should say "תש"ב" or "her first year", not "in 1942".
- The scan mastheads count the series' years [PDF-checked, read by eye]: 1943 `שנה שניה`,
  1944 `שנה שלישית`, 1951 `שנה עשירית`. So the תש"ב sheets are the series' first year
  (consistent with 1942 being the earliest Bereshit sheet).
- `dateCreated`/`dateModified` in the raw files (2019) are **digitization** dates, not
  authorship dates. Don't use them.

---

## 2. Fidelity findings: how L1 differs from L0

These govern every later stage.

### 2.1 `ref` labels are Sefaria's link layer and can be wrong

`161941[7]` is labeled `Rashi on Genesis 3:7:3-8:1`, but its text opens with her own note
`וראה הכלל שלו בבחירת המדרשים פסוק ה'` before the Rashi. In the scan, that note is a
parenthesis *inside* her question 2 (on ד"ה לא מות תמותון), not a separate source.

The same note also carries a **transcription error inside her own words**. The scan reads
`פסוק ח' ד"ה וישמעו` [PDF-checked, 1944, read at high resolution]. That's correct, since
Rashi's ד"ה וישמעו is on Gen 3:8, but the digitization has `פסוק ה'`.

**Rule:** treat `ref` as a hint and `text.he`/`outsideText` as the digitizer's rendering,
which can contain typos. Confirm against the PDF what she actually wrote and cited.

### 2.2 The digitization *expands* her pointers into full texts

[PDF-checked, 1944] Section ב of the scan reads, roughly, `עיין רש"י, ראב"ע (עד גם הוא אחר) רמב"ן`.
That is a *pointer* list, with an explicit stopping point for Ibn Ezra. The digitization
(`161941[21]–[25]`) inserts full Rashi, Ibn Ezra and Ramban texts in its place.
**Rule:** the extent she specified ("עד …") is the extent we quote. The digitizer's
full text is a convenience, not her selection.

### 2.3 The 1943 digitization dropped all her framing

[PDF-checked] Sheet **162000 (תש"ג, הבריאה ועץ הדעת)** is digitized as 36 ref items only,
with **no section headers and no questions**. The scan has lettered sections א through ט,
each with numbered questions, and a closing note. Her questions for this sheet exist
**only in the PDF**. A full transcription is now in
[`bereshit-transcriptions/162000-1943.md`](bereshit-transcriptions/162000-1943.md), cross-checked
section by section against the digitized sources. **Part 1 (א–ד), the part the leaf uses, was
verified against the scan by Lev Israel on 2026-10-06. Part 2 is still a draft.** It shows the sheet is two questionnaires (2:1–6; the
tree, 2:9–3:10), that the digitization also dropped Malbim, Rashi and Onkelos, and that
**her section ג asks whether 2:4 closes the creation account or heads what follows**.

### 2.4 Digitizer-added and digitizer-dropped structure

- [PDF-checked, 1951] Sheet 161580: the scan's masthead carries the title `בני האלוהים`,
  but the scan has **no lettered sections**. The `א.` in the digitized header
  `א. בני האלוהים` is the digitizer's. The digitized letters aren't always hers.
- [PDF-checked, 1944] The scan marks harder questions with `+` and ends with a footer
  explaining the marking and inviting answers by mail. Both are absent from the digitization.
- **Section headers are sometimes the digitizer's, not hers.** [PDF-checked] 1963 (160726)
  §א is headed `שאלת מבנה` in the scan but `פתיחת הפרק ב"ויכולו"` in the digitization.
  1959 (161180) §ב is `שאלה כללית` in the scan but `בעשרה מאמרות נברא העולם` in the
  digitization. The body text of both sections matches the scan. **Rule:** a leaf's section
  title comes from the scan.

### 2.5 Her panel is bigger than the ref items

Many sources she quoted are typed into prose items instead of linked refs. The
digitizers often marked these with a grey label. Examples [extracted]:
`161941[32]` *הרכסים לבקעה* (on איכה), `161941[41]` Rambam, Hilkhot Teshuvah 5:1,
`161580[2]` Sifrei Beha'alotekha, `161580[17]` Benno Jacob, `160441[13]` Cassuto,
`160441[17]` R. S. R. Hirsch, `160441[26]` the Biur (R. Shlomo Dubno).
Counts of "refs" in the table below **understate her panel**. The `.md` survey lists
every prose item verbatim so none are hidden.

### 2.6 One bilingual edition

160441 (תש"ל, 1970) is the R. Francis Nataf English edition. Its framing is in
`outsideBiText` (he + en). It's the only sheet where an English rendering of her own
questions exists. Elsewhere, any English we write is our translation and must be labeled as such.

### 2.7 Her own cross-references between sheets [extracted]

These are explicit links she made, so they're evidence of how she saw the corpus:

- `161941[0]`: the 1944 sheet opens by declaring itself **the continuation of the 1943 sheet** (162000).
- 1945 (161672) → 1944, 1943 · 1963 (160726) → 1943 · 1955 (161233) → 1943, 1946 (161545)
- 1948 (161495) → 1947 (161776) · 1959 (161180) → 1954 (161401)
- 1957 (161104) → 1956 (161216) · 1958 (161141) → 1957, 1956
- 1951 (161580) → 1950 (161438) · 1969 (160469) → 1950, 1951
- 1964 (160638) → 1946, 1960 (161685)
- Out-of-parsha links (to her sheets on Noach, Vayera, Toldot, Re'eh, Vayikra, Ha'azinu,
  Pinchas, Nasso, Miketz, Chayei Sarah) are listed per sheet in `bereshit-survey.md`.

### 2.8 Spot-check coverage and heuristic limits

- Only **5 of 30** PDFs (1943, 1944, 1951, 1959 §א–ב, 1963 §א–ב) have been compared by eye. The other 27 have
  only been confirmed to exist and hashed. Stage 3 must compare **every chosen sheet**
  against its PDF before drafting from it.
- In `bereshit-survey.md`, "Q" (question/task) vs. "prose" vs. "quote-like" is a
  **heuristic** classification (see the script docstring). Some quotations that contain "?" are
  tagged Q, and some tasks may be tagged prose. The verbatim text is always there; read it rather than trusting the label.
- "Genesis verses (ref items)" counts only linked refs. A sheet can discuss a verse in
  prose without a ref, so coverage gaps (§5) are *upper bounds on absence*, not proof of it.

---

## 3. Inventory [extracted]

30 sheets. **Copied verbatim from the generated table** at the top of
[`bereshit-survey.md`](bereshit-survey.md). If they ever differ, the generated one wins;
regenerate it there rather than editing here. Section labels are verbatim from the
digitization (with §2.4's caveat). Refs/Qs are counts of linked ref items and heuristic
question items. The item-by-item detail is below the table in the same file.

| Year | Sheet | PDF | Sub-topic (her title) | Genesis verses (ref items) | Her sections (verbatim, digitized) | refs / Qs | Flags |
|---|---|---|---|---|---|---|---|
| **תש"ב / 1942** | [161880](https://www.sefaria.org/sheets/161880) | [1229.pdf](https://www.nechama.org.il/pdf/1229.pdf) | קין והבל | 3:9, 4:3, 4:7–10, 4:13, 4:15–16, 49:3 | א. שאלה כללית · ב. השוואת מפרשים · ג. שאלות ודיוקים ברש"י · ד. "אי הבל" - שאלות ברש"י · ה. "גדול עוני מנשוא" · ו. שאלות ודיוקים ברש"י · ז. אות קין · ח. שאלות לשון וסגנון · ט. "ויצא קין מלפני ה'" | 30 / 11 |  |
| **תש"ג / 1943** | [162000](https://www.sefaria.org/sheets/162000) | [1351.pdf](https://www.nechama.org.il/pdf/1351.pdf) | הבריאה ועץ הדעת | 2:2–4, 2:6, 2:9, 2:16–17, 3:1–2 | *(none digitized)* | 36 / 0 | NO_SECTION_HEADERS, NO_QUESTIONS_IN_DIGITIZATION |
| **תש"ד / 1944** | [161941](https://www.sefaria.org/sheets/161941) | [1291.pdf](https://www.nechama.org.il/pdf/1291.pdf) | החטא | 3:3–4, 3:6–9, 3:11–12, 3:22 | א. שאלות ודיוקים ברש"י · ב. "קול א-להים מתהלך" · ג. ביאור מילת "איכּה" · ד. "האדם היה כאחד ממנו" | 20 / 17 |  |
| **תש"ה / 1945** | [161672](https://www.sefaria.org/sheets/161672) | [1021.pdf](https://www.nechama.org.il/pdf/1021.pdf) | העונש | 2:17, 3:11, 3:14–18, 3:20, 3:22, 4:1, 5:29, 8:21 | א. שאלות מבנה וסגנון · ב. שאלות ודיוקים ברש"י · ג. "הוא ישופך ראש..." · ד. "בעבורך" · ה. "...כאחד ממנו..." · ו. שאלות בקיאות | 27 / 17 |  |
| **תש"ו / 1946** | [161545](https://www.sefaria.org/sheets/161545) | [894.pdf](https://www.nechama.org.il/pdf/894.pdf) | איסור אכילת הפרי | 2:9, 2:15–17, 3:6, 3:23 | א. "לעבדה ולשמרה" · ב. עץ הדעת · ג. "עץ הדעת טוב ורע" · ד. טעם המצוה · ה. שאלות לשון וסגנון | 9 / 16 |  |
| **תש"ז / 1947** | [161776](https://www.sefaria.org/sheets/161776) | [1125.pdf](https://www.nechama.org.il/pdf/1125.pdf) | יום השישי | 1:22, 1:24–28, 2:8 | א. שאלות כלליות · ב. שאלות מבנה וסגנון · ג. ללשון הרבים "נעשה אדם" · ד. הטעם שאדם נברא יחידי | 22 / 14 |  |
| **תש"ח / 1948** | [161495](https://www.sefaria.org/sheets/161495) | [844.pdf](https://www.nechama.org.il/pdf/844.pdf) | יום חמישי, יום השישי | 1:20, 1:22, 1:27–29, 1:31 | א. סדר הבריאה · ב. שאלות סגנון · ג. "ישרצו המים" · ד. הכוונה בפירוט התנינים · ה. "וכבשוה" - כח וממשלה · ו. עמדת התורה כלפי הצמחונות - שאלות ברש"י · ז. "יום הששי" | 19 / 14 |  |
| **תש"ט / 1949** | [161834](https://www.sefaria.org/sheets/161834) | [1183.pdf](https://www.nechama.org.il/pdf/1183.pdf) | בריאת האישה | 2:8, 2:18–19, 2:22 | א. שאלות כלליות בהשוואת פרק ב' לפרק א' · ב. בריאת האשה · ג. מונוגמיה מן התורה · ד. שאלות לשון וסגנון · ה. שאלות ודיוקים ברש"י | 13 / 18 |  |
| **תש"י / 1950** | [161438](https://www.sefaria.org/sheets/161438) | [787.pdf](https://www.nechama.org.il/pdf/787.pdf) | בני קין | 4:17, 4:20, 4:23–24 | א. שאלות ודיוקים ברש"י · ב. התנצלות או התפארות? · ג. בכוונת הסיפור כולו | 21 / 10 |  |
| **תשי"א / 1951** | [161580](https://www.sefaria.org/sheets/161580) | [929.pdf](https://www.nechama.org.il/pdf/929.pdf) | בני האלוהים | 6:1–2, 6:4 | א. בני האלוהים | 13 / 5 |  |
| **תשי"ב / 1952** | [161471](https://www.sefaria.org/sheets/161471) | [820.pdf](https://www.nechama.org.il/pdf/820.pdf) | בהשוואת פרק א' ופרק ב' | 2:5, 2:8, 2:15, 28:10 | א. "טרם יהיה" · ב. "טרם יצמח" · ג. "ואדם אין" · ד. "גן בעדן מקדם" - שאלות ברש"י · ה. שאלת מבנה · ו. "לעבדה ולשמרה" (1) · ז. "לעבדה ולשמרה" (2) · ח. בריאת האשה · ט. המונוגומיה כאידאל · י. הערה כללית לפרק ב' | 14 / 18 |  |
| **תשי"ג / 1953** | [161223](https://www.sefaria.org/sheets/161223) | [570.pdf](https://www.nechama.org.il/pdf/570.pdf) | בריאת האישה | 2:18, 2:20, 2:22, 2:24 | א. קשר האיש והאשה · ב. "לא טוב היות האדם לבדו" · ג. בביאור הביטוי "עזר כנגדו" · ד. "ולאדם לא מצא עזר כנגדו" · ה. בינה יתירה באשה · ו. "ודבק באשתו" | 16 / 22 |  |
| **תשי"ד / 1954** | [161401](https://www.sefaria.org/sheets/161401) | [750.pdf](https://www.nechama.org.il/pdf/750.pdf) | סדר הבריאה | 1:1, 1:3 | א. מזמור ק"ד לפי סדר הבריאה · ב. "בראשית" - קושיית ר' יצחק · ג. כוונת "ויאמר" ביחס לה' · ד. "ויהי אור" | 6 / 15 |  |
| **תשט"ו / 1955** | [161233](https://www.sefaria.org/sheets/161233) | [581.pdf](https://www.nechama.org.il/pdf/581.pdf) | החטא | 3:1, 3:4–5, 3:8, 18:15 | א. דברי ה' ודברי האשה · ב. הסתת הנחש: "אף כי" וכו' · ג. תחילת דברי הנחש · ד. "אל תוסף על דבריו" · ה. "כי יודע אלוקים" · ו. כיון שחטא אדם - נתיירא | 12 / 18 |  |
| **תשט"ז / 1956** | [161216](https://www.sefaria.org/sheets/161216) | [563.pdf](https://www.nechama.org.il/pdf/563.pdf) | קין והבל | 4:1–2, 4:4, 4:7–8, 4:10 | א. מדברי המדרש · ב. שאלות ודיוקים ברש"י · ג. "הלא אם תטיב שאת..." | 13 / 19 |  |
| **תשי"ז / 1957** | [161104](https://www.sefaria.org/sheets/161104) | [451.pdf](https://www.nechama.org.il/pdf/451.pdf) | קין והבל | 4:3–4, 4:9, 4:13 | א. "...השומר אחי אנכי" · ב. גאולת הדם · ג. קורבנות · ד. שאלות ודיוקים ברש"י · ה. "גדול עווני מנשוא" | 9 / 18 |  |
| **תשי"ח / 1958** | [161141](https://www.sefaria.org/sheets/161141) | [488.pdf](https://www.nechama.org.il/pdf/488.pdf) | קין והבל | 4:9, 4:11–12 | א. שאלות מבנה וסגנון · ב. השוואת פסוקים · ג. "אי הבל אחיך ..." · ד. הקללה · ה. "נע ונד תהיה בארץ" | 7 / 17 |  |
| **תשי"ט / 1959** | [161180](https://www.sefaria.org/sheets/161180) | [527.pdf](https://www.nechama.org.il/pdf/527.pdf) | בריאת העולם + הפטרה | 1:4 | א. בראשית וירמיהו · ב. בעשרה מאמרות נברא העולם · ג. "וירא, ויבדל" - שאלות ברש"י · ד. הנמלך ה' בדעתו? · ה. איזכור בריאת החושך · ו. ה"טוב" בלידת משה · ז. המקשר בין הפרשה להפטרה · ח. בביאור "הנותן נשמה" וכו' · ט. בביאור "כי תעבור" וכו' | 16 / 13 |  |
| **תש"כ / 1960** | [161685](https://www.sefaria.org/sheets/161685) | [1034.pdf](https://www.nechama.org.il/pdf/1034.pdf) | עץ הדעת טוב ורע | 1:28, 2:7, 3:3, 3:6, 4:2, 4:4–5, 4:25 | א. אדם ובניו סטו מן התכלית · ב. עץ הדעת - שמו ומהותו · ג. "אל תוסף על דבריו" · ד. שאלות ודיוקים ברש"י | 13 / 15 |  |
| **תשכ"א / 1961** | [160823](https://www.sefaria.org/sheets/160823) | [378.pdf](https://www.nechama.org.il/pdf/378.pdf) | וינחם ה' כי עשה את האדם | 6:5–8 | א. "כי רבה רעת האדם" · ב. לשון "יצר" · ג. לא אדם הוא להנחם · ד. הפעלים: נחם, עשה, עצב · ה. "ויתעצב אל לבו" - מבנה תחבירי · ו. צחות לשון העברי | 11 / 9 |  |
| **תשכ"ב / 1962** | [160699](https://www.sefaria.org/sheets/160699) | [274.pdf](https://www.nechama.org.il/pdf/274.pdf) | מזונם של הבריות | 1:26, 1:29–30 | א. ממתי הותרה אכילת בשר (1) · ב. ממתי הותרה אכילת בשר (2) · ג. ממתי הותרה אכילת בשר (3) - שאלות ברש"י | 11 / 13 |  |
| **תשכ"ג / 1963** | [160726](https://www.sefaria.org/sheets/160726) | [302.pdf](https://www.nechama.org.il/pdf/302.pdf) | היום השישי והיום השביעי | 1:31, 2:2 | א. פתיחת הפרק ב"ויכולו" · ב. "כי טוב" בבריאת האדם · ג. "והנה טוב מאד" - המוות ויצר הרע · ד. "והנה טוב מאוד" דווקא ביום הששי · ה. "ויכל אלוקים ביום השביעי" | 9 / 18 |  |
| **תשכ"ד / 1964** | [160638](https://www.sefaria.org/sheets/160638) | [212.pdf](https://www.nechama.org.il/pdf/212.pdf) | עצי הגן | 1:11, 2:9, 2:16–17 | א. עץ הדעת ועץ החיים · ב. הדגשת "בתוך הגן" · ג. הדגשת "ממנו" · ד. שאלות בטעמי המקרא | 9 / 18 |  |
| **תשכ"ה / 1965** | [160577](https://www.sefaria.org/sheets/160577) | [148.pdf](https://www.nechama.org.il/pdf/148.pdf) | האדם | 2:7–8, 2:15, 2:18–19 | א. סיפור יצירת החיות · ב. שאלות ודיוקים ברש"י · ג. "ויהי האדם לנפש חיה" · ד. "ויקח ה'" · ה. "לעבדה ולשמרה" · ו. קריאת שמות לחיות | 17 / 17 |  |
| **תשכ"ו / 1966** | [160515](https://www.sefaria.org/sheets/160515) | [84.pdf](https://www.nechama.org.il/pdf/84.pdf) | בצלם אלוקים | 1:26–27 | א. בצלם אלקים - שאלות ברש"י · ב. בצלמנו כדמותנו | 11 / 11 |  |
| **תשכ"ז / 1967** | [160495](https://www.sefaria.org/sheets/160495) | [62.pdf](https://www.nechama.org.il/pdf/62.pdf) | האכילה מעץ הדעת | 2:25, 3:1, 3:3–7, 3:11 | א. כוונת "ולא יתבוששו" · ב. בביאור דברי הנחש · ג. "ותפקחנה... וידעו" - שאלות ברש"י · ד. הוראת "עירומים" · ה. שיחת האישה עם הנחש - שאלות ברש"י | 21 / 24 |  |
| **תשכ"ח / 1968** | [160442](https://www.sefaria.org/sheets/160442) | [2.pdf](https://www.nechama.org.il/pdf/2.pdf) | אחרי החטא... | 3:8, 3:11–14 | א. "ויתחבא האדם..." · ב. "קול אלוקים מתהלך..." · ג. "כי עירום אתה..." - שאלות ברש"י · ד. "אשר נתתה עמדי..." · ה. הנחש השיאני (1) · ו. הנחש השיאני (2) | 25 / 14 |  |
| **תשכ"ט / 1969** | [160469](https://www.sefaria.org/sheets/160469) | [30.pdf](https://www.nechama.org.il/pdf/30.pdf) | בני קין | 4:26, 5:24 | א. קין והבל · ב. בני קין ובני שת · ג. אז הוחל לקרא בשם ה' · ד. "ויתהלך חנוך את האלוקים" | 10 / 14 |  |
| **תש"ל / 1970** | [160441](https://www.sefaria.org/sheets/160441) | [1.pdf](https://www.nechama.org.il/pdf/1.pdf) | קין וצאצאיו | 4:17, 4:22–23 | א. אדם וקין · ב. "ותלד את חנוך" · ג. "...ותהר ותלד... ויהי בונה עיר..." · ד. "ויהי בונה עיר" · ה. "לוטש כל חורש..." · ו. "...לוטש כל חורש..." · ז. "ויאמר למך לנשיו" | 15 / 17 | BILINGUAL_EDITION |
| **תשל"א / 1971** | [162069](https://www.sefaria.org/sheets/162069) | [1420.pdf](https://www.nechama.org.il/pdf/1420.pdf) | בני האלוהים | 6:2–3 | א. מדברי המדרש · ב. "בני האלוהים" · ג. השוואת מפרשים | 13 / 14 |  |

---

## 4. Tentative clustering [interpretation]

Grouped by **the passage each sheet anchors on**, using her title (L1) and the verses its
ref items touch (§3). This is a reading aid for Stage 2, not a finding about Nechama. The
boundaries are my calls and several sheets straddle two groups (noted).

| Cluster | Passage | Sheets (year · id) | Count |
|---|---|---|---|
| **A. The days of creation** | Gen 1:1–2:3 | 1947 יום השישי · 161776 — 1948 יום חמישי, יום השישי · 161495 — 1954 סדר הבריאה · 161401 — 1959 בריאת העולם + הפטרה · 161180 — 1962 מזונם של הבריות · 160699 — 1963 היום השישי והיום השביעי · 160726 — 1966 בצלם אלוקים · 160515 | 7 |
| **B. Adam, the garden, the woman** | Gen 2:4–25 | 1949 בריאת האישה · 161834 — 1952 בהשוואת פרק א' ופרק ב' · 161471 — 1953 בריאת האישה · 161223 — 1965 האדם · 160577 | 4 |
| **C. The trees and the prohibition** | Gen 2:9, 2:16–17, 3:1–6 | 1943 הבריאה ועץ הדעת · 162000 *(straddles A: opens on 2:2–3)* — 1946 איסור אכילת הפרי · 161545 — 1960 עץ הדעת טוב ורע · 161685 — 1964 עצי הגן · 160638 | 4 |
| **D. The sin and its aftermath** | Gen 3 | 1944 החטא · 161941 — 1945 העונש · 161672 — 1955 החטא · 161233 — 1967 האכילה מעץ הדעת · 160495 — 1968 אחרי החטא… · 160442 | 5 |
| **E. Cain and Abel** | Gen 4:1–16 | 1942 קין והבל · 161880 — 1956 קין והבל · 161216 — 1957 קין והבל · 161104 — 1958 קין והבל · 161141 | 4 |
| **F. Cain's line, Lamech, Enoch** | Gen 4:17–26 (+ 5:24) | 1950 בני קין · 161438 — 1969 בני קין · 160469 — 1970 קין וצאצאיו · 160441 | 3 |
| **G. The sons of God and the regret** | Gen 6:1–8 | 1951 בני האלוהים · 161580 — 1961 וינחם ה' כי עשה את האדם · 160823 — 1971 בני האלוהים · 162069 | 3 |

Total 30. C and D are closely linked by her own cross-references (§2.7) and could
reasonably merge into one "Eden" cluster of 9. That's a Stage 2 call.

Observations a design might use (all [interpretation] built on [extracted] facts):

- **She returned to Cain and Abel four times in her first 17 years** (1942, 1956, 1957, 1958),
  three of them consecutive (1956–58). The 1957 and 1958 sheets link back to their predecessors (§2.7).
- **Bnei ha-Elohim (Gen 6:1–4) gets two sheets 20 years apart** (1951, 1971), and the 1971
  one is her last Bereshit sheet.
- **The 1969 Cain-line sheet links back to 1950 and 1951** (§2.7), tying cluster F to G in her own hand.

---

## 5. Coverage and absences [extracted, with §2.8's caveat]

Verses of Gen 1:1–6:8 touched by **no linked ref** in any of the 30 sheets, counting both
ref items and links inside her prose. The script generates this; see "Coverage" in
`bereshit-survey.md`.

- **Gen 5 (the genealogy Adam → Noah): almost entirely untouched.** Only 5:1, 5:24 (Enoch)
  and 5:29 appear anywhere. No sheet is titled on it.
- **Gen 2:10–14 (the four rivers of Eden):** untouched, and no sheet is titled on it.
- Gen 1:5–19 (days one through four in detail) has few linked refs, but 1954 סדר הבריאה and
  1959 בריאת העולם are on the creation order as a whole and may discuss them in prose.
  **Not a confirmed absence.**

Before any absence is stated in narration (as Nasso's overview did for Sotah), confirm it
against the PDFs of the cluster's sheets.

---

## 5a. Masoretic layout notes (for a possible manuscript-image feature)

Source: the tanach.us *Unicode/XML Leningrad Codex* (WLC), `https://www.tanach.us/Books/Genesis.xml`
(© C.V. Kimball 2013), retrieved 2026-10-06. This is a **transcription** of the Leningrad Codex.
Confirm against a facsimile before showing an image. Sefaria's "Tanach with Ta'amei Hamikra"
comes from the same source but **drops the פ/ס markers**. Sefaria's MAM has them but follows
the Aleppo tradition, and Aleppo lacks Genesis. On 5:20, 5:24 and 5:27 MAM has ס where WLC has פ.

| WLC fact | Which of her sheets it bears on |
|---|---|
| פ (open break) after 1:5, 1:8, 1:13, 1:19, 1:23, 1:31 **and 2:3**. So 1:1–2:3 is **seven open paragraphs**, the seventh being ויכולו (2:1–3) alone | 1963 `160726[2]` (Benno Jacob: the chapter break at ויכולו "separates what belongs together"; her question is why the division doesn't fit the parsha's structure). 1959 `161180[7]` (Cassuto: the number 7 recurs "in the number of paragraphs"). |
| פ after 6:4 and 6:8. 6:5–8 is its own open paragraph and closes the parsha | 1969 `160469[2]–[10]` (Cassuto keeps 6:5–8 with ספר תולדות אדם, "like the sedra-dividers", against most scholars who join it to the flood) |
| פ after 4:26 (end of Cassuto's קין והבל unit 4:1–26) | 1969 `160469[2]` |
| 1:11 `דֶּ֗שֶׁא` carries **revia**, not zakef katan | 1964 `160638[30]–[31]` (Minchat Shai on the two accent traditions; "how is the verse read under each?") |
| 2:20 `וּלְאָדָ֕ם`: **shva** under the ל | 1953 `161223[30]` ("with which commentator do the Masoretes agree in vocalizing ולְאדם with shva, not kamatz?") |
| 2:2 reads `בַּיּוֹם הַשְּׁבִיעִי` (cf. the Mekhilta's report that the LXX translators wrote "sixth") | 1943 `162000[1]` (her questions on it survive only in the PDF, §2.3); 1963 `160726[23]–[29]` |

## 5b. Image demo: `data/bereshit-chapter-break.json`

This is a one-section demo of the new image panel. It is **not** a Stage 2 design decision, so
fold it into the garden or delete it. Everything attributed to Nechama comes from 1963
(160726) §א, [PDF-checked] against `302.pdf`:

| Card | Source |
|---|---|
| Section title "שאלת מבנה" | the scan's header (not the digitized one; see §2.4) |
| Intro: range 1:31–2:3 | the scan's heading `א' ל"א ב' א-ג` |
| Benno Jacob commentary | `160726[2]`, first sentence, checked word by word against the scan. Where they differ the scan wins: it spells `בפרושו` (digitization `בפירושו`) and `הפותח` (digitization `הפותחת`). The second I missed in my own check; the Stage 3 scan checker caught it (`bereshit-scancheck/160726-1963.md`), and I confirmed it on a zoomed crop. Punctuation (`ב'`, `"ויכולו"`) as in the source. English is our translation (recorded here; the card no longer labels it, per Lev 2026-10-06) |
| Question | `160726[2]`, second sentence, verbatim. English is ours |
| Codex narration (folio 1v: 2 cards, folio 2r: 3 cards) | our addition; the codex isn't in her sheet (the card no longer says so, per Lev). Only what's visible on the folios and matches WLC (§5a) |

Structure: three sections, with the two folios as `"titleCard": false` sections so each page
scrolls in and locks before any zoom. On 2r the sixth-day card boxes only `day-6`, and 2:1–3
is boxed only once the zoom pulls back out (`cb-seventh`).

Not used: Cassuto's "7 in the number of paragraphs" (1959, `161180[7]`). It's a different
gilayon, and there it frames a question about the ten utterances, not about paragraphs.

**Primary text:** MAM Hebrew for Gen 1:31–2:3 with cantillation stripped and maqaf replaced
by a space. `clean_verses.py` had a bug: it stripped `{ף}` instead of `{פ}`, so it left the
פ markers in. That's fixed now. English: Sefaria default (JPS gender-sensitive), with one
leaked footnote removed from 2:2 ("ceasingaceasing Or 'resting.'" → "ceasing").

**Images** (public domain; credit text is the `description` of Sefaria's manuscripts API record, verbatim, prefixed with its `title`, for
`leningrad-codex-(1008-ce)`): `LC_Folio_1v` = `BIB_LENCDX_F001B.jpg` (3683×4224,
anchorRef Gen 1:1–26) and `LC_Folio_2r` = `BIB_LENCDX_F002A.jpg` (3958×4248, Gen 1:26–2:19).

**Region derivation.** Measured on the full-resolution JPEGs against a 0.01 fractional grid,
then drawn back onto the images and checked by eye. Columns are numbered right to left.

| Region | Folio, column | Covers |
|---|---|---|
| `day-1` | 1v, col 1 | `יום אחד` (1:5), short line, rest open |
| `day-2` | 1v, col 1 | `יום שני` (1:8), short line, rest open |
| `day-3` | 1v, col 2 | `ויהי בקר יום שלישי` (1:13), full line, then a blank line |
| `day-4` | 1v, col 3 | `ויהי בקר יום רביעי` (1:19), full line, then a blank line |
| `day-5` | 1v, col 3 | `יום חמישי` (1:23), short line, rest open |
| `day-6` | 2r, col 1 | `יום הששי` (1:31), short line, rest open |
| `vayechulu-a` | 2r, col 1 | `ויכלו השמים…` to `…מלאכתו אשר` (2:1–2a), 3 lines |
| `vayechulu-b` | 2r, col 2 | `עשה וישבת…` to `…ברא אלהים לעשות` (2:2b–3), 6 lines |
| `toldot` | 2r, col 2 | `אלה תולדת השמים והארץ` (2:4), first line. *Removed from the demo; reserved for the 1943 leaf: x 0.37, y 0.314, w 0.2, h 0.03* |

**Observation, not in the narration:** a full line followed by a blank line (days 3, 4) versus
a short line with the rest left open (days 1, 2, 5, 6) is the standard open-paragraph form.
After 2:3, though, a *short* line is **also** followed by a full blank line, and there's a
large mark in the right margin beside 2:4. Whether either means anything (seder sign?
scribal habit?) needs a Masoretic source before it's said anywhere.

## 6. What this survey does *not* establish

- Which of her questions are the heart of each sheet. That's Stage 3, done against the PDF.
- English translations of anything. None have been made. Apart from 160441's Nataf
  English, any English in the Close Read will be ours and must be labeled as such.
- Commentator identities beyond Sefaria's ref labels. Era/school attributions get
  looked up when a source is actually used.

## 7. Stage 2 design proposal (awaiting sign-off)

**Shape:** overview → root fork (5 themes) → per theme: intro → fork (3 gilyonot) → leaf.
That's 15 leaves. Themes follow the clusters in §4, with C+D merged (her own cross-links tie
them) and F+G merged. Picks favor a spread of years within each theme, sheets that ask
*different* questions, and at least 3 lettered sections with a real panel of commentators.
Every "sections to render" entry below is from the digitization (§3). **Before drafting, each
chosen sheet gets a scan check (§2.8), and leaf section titles come from the scan (§2.4).**
All English renderings of her questions are ours, except 1970's (Nataf), which isn't a pick.

### Theme 1: The days of creation (Gen 1:1–2:3), 8 sheets

| Leaf | Sheet | Her sections to render | Why this one |
|---|---|---|---|
| **1943 (תש"ג)** Where creation ends | 162000 | **Part 1 only, from the transcription** (`bereshit-transcriptions/162000-1943.md`): א ("ויכל ביום השביעי": the Mekhilta's "sixth", Rashi, Ibn Ezra, Sforno) · ב ("לעשות": Rashi, Ibn Ezra, Ramban, Radak, Malbim) · ג ("אלה תולדות": closing or heading? Rashi, Ramban, Sforno; **Leningrad folio 2r: 2:4 opens a new paragraph**) · ד ("ואד יעלה": Ibn Ezra, Saadia) | Early (her second year). Chosen over 1947 (Lev, 2026-10-06). Part 1 transcription **verified by Lev, 2026-10-06** |
| **1954 (תשי"ד)** Why begin with creation | 161401 | ב (R. Yitzhak's question: Rashi vs Ramban) · ג (what "ויאמר" means for God: Ibn Ezra, Ramban, 7 Qs) · ד ("ויהי אור") | Mid. Theology of the opening verse |
| **1963 (תשכ"ג)** The sixth day and the seventh | 160726 | א (the chapter break + **Leningrad 1v/2r**, the existing demo) · ג ("טוב מאד" = death: Bereshit Rabbah, Maharzu, Matnot Kehunah) · ד (why on the sixth day: Ralbag) · ה ("ויכל ביום השביעי": BR, Rashi, Efodi, Ibn Ezra, R. Avraham b. HaRambam, 7 Qs) | Late. Already started; ה continues straight out of the codex |

Alternates: 1947 ("Let us make": Cassuto, Rashi, Ibn Ezra, Ramban, Shadal, Sanhedrin), 1948
(days 5–6, Cassuto, Wessely), 1962 (when was meat permitted, 13 Qs), 1966 (image of God; dense
but only 2 sections), 1959 (Cassuto's sevens + haftarah).

### Theme 2: Adam, the garden and the woman (Gen 2:4–25), 4 sheets

| Leaf | Sheet | Her sections to render | Why this one |
|---|---|---|---|
| **1952 (תשי"ב)** Chapter 1 and chapter 2 | 161471 | א–ב ("טרם": Rashi, Ramban, Sforno, Benno Jacob) · ד ("גן בעדן מקדם", Rashi) · ו–ז ("לעבדה ולשמרה": Chizkuni, Avot de-R. Natan) · ח (woman: Akeidat Yitzhak) | Densest sheet in the theme (10 sections) |
| **1953 (תשי"ג)** "A helper against him" | 161223 | ב ("לא טוב": Rashi, Chizkuni, Sforno, Shadal) · ג ("עזר כנגדו": Rashi, Gur Aryeh, Shadal) · ד ("ולאדם לא מצא": Ramban vs Ibn Ezra, Benno Jacob, Buber-Rosenzweig; **her question on the Masoretes' shva in וּלְאָדָם, a Leningrad moment, folio 2v**) · ו ("ודבק") | Mid. Her one vocalization question |
| **1965 (תשכ"ה)** The human being | 160577 | ג ("לנפש חיה": BR, Taanit) · ד ("ויקח": BR, Radak, Rashi) · ו (naming the animals: Sforno, Wessely) | Late |

Alternate: 1949 (also titled בריאת האישה, overlapping 1953's questions on "לא טוב").

### Theme 3: The trees, the sin and its aftermath (Gen 2:9–3:24), 9 sheets

| Leaf | Sheet | Her sections to render | Why this one |
|---|---|---|---|
| **1944 (תש"ד)** The sin | 161941 | א (Rashi precision, 7 Qs) · ב ("קול ה' מתהלך": Rashi, Ibn Ezra, Ramban, BR) · ג ("איכה": HaRekhasim LeBik'ah) · ד ("כאחד ממנו": Rashi, Ibn Ezra, Sforno, Rambam Teshuvah 5:1) | Early. Opens by calling itself 1943's continuation |
| **1964 (תשכ"ד)** The trees of the garden | 160638 | א (two trees: Akeidat Yitzhak) · ג ("ממנו": Ibn Ezra, Ramban, Malbim, Shadal, Ayelet HaShachar) · ד (**the two accent traditions on "דשא", 1:11: Minchat Shai, HaRekhasim; Leningrad moment, folio 1v, already in hand**) | Mid-late |
| **1968 (תשכ"ח)** After the sin | 160442 | ב ("קול": Rashi, Ramban, Radak, BR, Moreh Nevukhim) · ד ("אשר נתתה עמדי": Rashi vs Ramban) · ו ("הנחש השיאני": Mizrachi, Gur Aryeh, R. Eliezer Heilprin) | Late |

Alternates: 1955 (the serpent's dialogue, many voices), 1967 (eating from the tree, 23 Qs),
1945 (the punishments), 1946, 1960.

### Theme 4: Cain and Abel (Gen 4:1–16), 4 sheets

| Leaf | Sheet | Her sections to render | Why this one |
|---|---|---|---|
| **1942 (תש"ב)** Her first | 161880 | ב (4:7, "the hardest verse in Genesis": Rashi, Ibn Ezra, Ramban, Sforno) · ה ("גדול עוני": Rashi, Ramban, Ibn Ezra; "the weakness of each") · ז (Cain's sign) · ט ("ויצא קין": the Bereshit Rabbah dispute) | The earliest sheet of all 30 |
| **1956 (תשט"ז)** | 161216 | א (midrash) · ב (Rashi, 12 Qs) · ג (**4:7 again**: Onkelos, Malbim) | Same verse 14 years later, which is the "returning across decades" this format exists for |
| **1958 (תשי"ח)** | 161141 | א (structure) · ב (verse comparison) · ד (the curse: Rashi vs Ramban) | Third of three years running (1956–58) |

Alternate: 1957 (blood redemption, sacrifices: Cassuto, Ramban).

### Theme 5: From Cain's line to the Flood (Gen 4:17–6:8), 6 sheets

| Leaf | Sheet | Her sections to render | Why this one |
|---|---|---|---|
| **1950 (תש"י)** Lamech's song | 161438 | א (Rashi) · ב (apology or boast? Saadia, Rashi, Ibn Ezra, Ramban, Ralbag, Sforno, Malbim) · ג (the story's purpose: Malbim) | Early; a classic mahloket |
| **1969 (תשכ"ט)** Where the parsha ends | 160469 | א (Cassuto's paragraphs; **6:5–8 with the sedra division against most scholars, a Leningrad moment, folio 4r, Gen 5:26–6:19**) · ג ("אז הוחל": Rashi, Ibn Ezra, Bekhor Shor, Shadal, Hirsch, Wessely) · ד (Enoch) | Late; links back to 1950/1951 in her hand |
| **1971 (תשל"א)** The sons of God | 162069 | א (midrash) · ב ("בני האלוהים": Radak, Malbim, Shadal, Sifrei, Benno Jacob) · ג (comparing commentators: Rashi, Sanhedrin) | Her last Bereshit sheet; 20 years after 1951 on the same topic |

Alternates: 1951 (sons of God, one long section), 1961 (God's regret, "וינחם"), 1970 (Nataf
bilingual edition). **Option:** split into "Cain's line" (1950, 1969, 1970) and "The sons of
God and the regret" (1951, 1961, 1971) for 6 themes and 18 leaves.

### Overview and image moments

- **Overview** (facts already established): 30 sheets, one a year from תש"ב to תשל"א; the
  five themes with their counts. Absences (Gen 5's genealogy, the rivers of Eden) go in only
  after the scan check in §5.
- **Leningrad moments** (all our addition, kept to what's visible and matches WLC §5a): 1963 א
  (1v/2r, built), 1964 ד (1v, in hand), 1953 ד (2v, to fetch), 1969 א (4r, to fetch). Each new
  folio gets the same treatment: confirm against the facsimile, then measure, draw and record regions (§5b).

### 7a. Decisions (Lev, 2026-10-06)

1. **3 leaves per theme**, 15 in all, as in the tables above.
2. **Theme 5 stays one theme.**
3. **Leningrad once or twice, not four times.**
4. **1943 becomes a Theme 1 leaf, replacing 1947** (option (a)).

**Consequences (Claude's call, to confirm):** the two Leningrad moments are **1963 א**
(2:1, the chapter break; folios 1v and 2r) and **1943 ג** (2:4 opens a new paragraph; folio 2r,
reusing the `toldot` region from §5b). Both images are in hand. The 1969 folio-4r moment is
dropped: 1969 א renders as text, and the 1964 ד and 1953 ד moments are dropped too. The 2:4 card
was removed from the 1963 demo, so that leaf ends at her question. The 1943 card may say only
what's visible, that 2:4 opens a new paragraph. The unexplained blank line before it stays out
of the narration (§5b).

### Original questions (answered above)

1. 15 leaves (3 per theme), or trim to 2–3 per theme?
2. Merge or split Theme 5 (5 or 6 themes)?
3. All four Leningrad moments, or only the ones where the layout is the evidence (1963, 1969)?
4. Transcribe 1943 from the scan so it can be a leaf or sibling? It's referenced by 1944, 1945, 1955 and 1963.

## 8. Stage 3: scan check and harvest (2026-10-06)

**3a. Scan checks.** All 15 leaves are checked against their scans, in
[`bereshit-scancheck/`](bereshit-scancheck/), one file per sheet, using the method and format in
its README. It's a verification, not a transcription: the digitization is an independent
reading, so agreement is evidence and disagreement is flagged. Five checker agents read every
page at 300 dpi (most scans are two pages, which the Stage 1 checks missed). I spot-checked one
finding per agent against the scan, or against an independent text, and all five held:
1952 §א's lost Q4, 1963 `הפותח`, 1944 `[4]`/`[10]`, 1950 `הראשון`, and 1958 `אומנותו`
(confirmed in Sefaria's own Ramban edition).

**What the scans show, across all 14:**
- **Headers.** Nearly every section header in the digitization is the digitizer's. Hers are a
  verse pointer plus the verse's words.
- **Spelling.** Her spelling (defective forms, abbreviations like פ', ע', ית') was normalized.
- **Marks.** Her ×/×× and + difficulty marks and her footers (send answers to…) are dropped.
- **Real losses:** a question (1952 §א Q4, 1956 §ב), two prose passages (1953 §ד), her
  start and stop points in pointer lists (1942 §ז).
- **Word changes:** 1950 "האחרון"→"הראשון", 1956 "לו"→"לא", 1958 "אמונתו"→"אומנותו",
  1965 Psalms 104:25 vs 104:28.
- **Not hers:** 1944's "ענה לשאלתם!" is not in the scan, so it's excluded.
- **Editorial additions (Lev, 2026-10-06):** where the digitizers *added* citation detail, it's
  a purposeful editorial service, not an error. Examples: "בראשית רבה **פרשה י"ט**", "**פרק**
  כ"א **פסוק** י"ט", "(תרגום מגרמנית)", 1954's "(שהובא בראב"ע)". Their richer citation is kept,
  recorded as `editorial_additions`, and not sent for review. A *changed* citation (1954's
  verse כ"ב→כ"ג, 1965's 104:28→25) is still substantive.
- **Digitizer slips** inside quoted sources, e.g. 1964's Malbim lost a clause.

**3b. Harvest.** `research/scripts/harvest_bereshit.py` writes
[`bereshit-harvest/<theme>/<year>.json`](bereshit-harvest/) from the digitization, the scan
checks, `bereshit-scancheck/overrides.json` (the 5 lost items, each cited), and the 1943
transcription. Each item records its basis: digitization, scan, scan-only or transcription.
Each scan fix is classed:
- **editorial:** the digitizers added citation detail; theirs is kept;
- **spelling:** applied automatically;
- **corroborated:** a doubtful letter, but the digitization's reading fits;
- **substantive:** listed for a person in the generated
  [`bereshit-scancheck/REVIEW.md`](bereshit-scancheck/REVIEW.md).

**Triage (Claude, 2026-10-06), asked "are all of these relevant to what we publish?"** No.
The 86 substantive lines were 64 distinct items. Each is now decided in
[`bereshit-scancheck/triage.json`](bereshit-scancheck/triage.json), with its evidence:
- **41 form:** same meaning in another form (word form, grammar, punctuation, word order).
  Her words from the scan are used.
- **8 settled from the scan:** read by Claude zoomed, e.g. 1950 "הראשון", 1956 "למה לא"; or
  confirmed by the cited source, e.g. Shadal cites Ps 104:28 and Ramban 2:20 cites Gen 4:23.
- **4 digitizer corrections:** her typos fixed, e.g. Ramban cites Deut 2:23, not her 2:22, and
  the German line is Mendelssohn's, so "רמבמ"ן" is right. The digitized text is kept, with her
  reading noted.
- **3 spelling or editorial.**
- **7 not published:** cross-references to other sheets and the teacher's guide, labels, a
  grammatical aside, and the digitizer's "ענה לשאלתם!".
- **2 open:** 1958 §ב's verse list and 1950 §ב's Ibn Ezra start point. Both get settled from
  the cited texts when those leaves are drafted.

**Nothing is left for Lev to review.**

Verse texts for Gen 1:1–6:8 are cached in `bereshit-verses.json` (`fetch_verses.py`): MAM
Hebrew plus the JPS gender-sensitive English, with leaked footnotes removed and the divine name
rendered "the Lord" (the Nasso convention, recorded in its meta).

**Rule for drafting:** a line of her words is quotable only if its basis is digitization or
spelling-class, or its REVIEW line has been checked by a person. Items marked `exclude` are not
hers.

## 9. Stage 4: the 1963 leaf (2026-10-06, for Lev's review)

Built by `research/scripts/build_bereshit.py` → `data/bereshit-chapter-break.json` (same slug
as the demo, which it replaces; the slug goes when the garden is assembled). Her Hebrew is never
typed: every commentary and question card slices a harvest item verbatim, and
`tests/test_provenance.py` re-checks each one. That test is proven to fail when four words are
appended to a question or when our English is relabeled as Sefaria's.

**What's rendered, and what's left out (gilayon 160726):**
- **Sections:** א, ג, ד, ה. ב (Abarbanel: why no "כי טוב" for man) is out, per the §7 design.
- **Her questions omitted** (omitted, never altered):
  - §ג Q4, on how Ecclesiastes 4 helps the second midrash;
  - §ה Q4, which rests on the Akeidat Yitzhak, a source not on her sheet;
  - §ה Q7, the verse list, for density.
- **Order:** her sources keep her order. In §ה her questions stand together at the end; here
  each follows the source it asks about. Her Q1 ("what is the question they deal with?") closes
  the section. The narration deliberately doesn't name the puzzle, because her Q1 asks the
  student to.
- **No sheet narration (Lev, 2026-10-06):** the reader experiences the content, not her sheet.
  Narration only points at the verse or the page. Section titles are content titles ("Where
  Does Chapter 2 Begin?"), not her structural headers. Everything about how her sheet is built
  stays here in the pack.
- **Slices:** question א is the tail of item [2] (from "הסבר, למה"); the Jacob quote is its
  head. §ג Q1 stops before "(עיין גם עלון ההדרכה!)", a pointer to the teacher's guide. In
  §ה, the Bereshit Rabbah card starts after her label "בראשית רבה:".
- **Editorial gloss:** the English of question א carries a bracket, "[the chapter beginning
  at 2:1, with 'Va-yekhullu']" (Lev, 2026-10-06). Her Hebrew is unchanged.
- **Ralbag:** her underline («ולא נשלם הטוב… שלפני התכלית») is reproduced in Hebrew and English,
  since her §ד Q1 asks about "the underlined words" (scan check `160726-1963.md`).
- **Translation choices:** אתמהא → "Astonishing!"; "רבי שאליה" → "Rabbi asked". Labels give
  names only: Maharzu and Matnot Kehunah are labeled as commentaries on the midrash; Efodi as
  "R. Yitzhak Profiat Duran, Ma'aseh Efod", her own attribution.
- **English basis:** all ours. Rashi's Sefaria English was rejected because it translates the
  canonical comment ("R. Simeon says…"), not her abridged quote.

**Every card → harvest item:**

| Card | Type | Harvest [i] | English |
|---|---|---|---|
| `cr-1963-intro` | narration | — | — |
| `cr-1963-jacob` | commentary · Benno Jacob | [2] | ours |
| `cr-1963-codex` | narration | — | — |
| `cr-1963-days` | narration | — | — |
| `cr-1963-2r-intro` | narration | — | — |
| `cr-1963-day-6` | narration | — | — |
| `cr-1963-seventh` | narration | — | — |
| `cr-1963-q-a` | question | [2] | ours |
| `cr-1963-g-intro` | narration | — | — |
| `cr-1963-br-9-5` | commentary · Bereshit Rabbah | [9] | ours |
| `cr-1963-br-9-7` | commentary · Bereshit Rabbah | [10] | ours |
| `cr-1963-maharzu` | commentary · Maharzu, on the midrash | [12] | ours |
| `cr-1963-matnot` | commentary · Matnot Kehunah, on the midrash | [13] | ours |
| `cr-1963-q-g1` | question | [14] | ours |
| `cr-1963-q-g2` | question | [15] | ours |
| `cr-1963-q-g3` | question | [16] | ours |
| `cr-1963-ralbag` | commentary · Ralbag | [20] | ours |
| `cr-1963-q-d1` | question | [21] | ours |
| `cr-1963-q-d2` | question | [22] | ours |
| `cr-1963-h-intro` | narration | — | — |
| `cr-1963-br-10-9` | commentary · Bereshit Rabbah | [25] | ours |
| `cr-1963-q-h2` | question | [31] | ours |
| `cr-1963-q-h3` | question | [32] | ours |
| `cr-1963-rashi` | commentary · Rashi | [26] | ours |
| `cr-1963-q-h5` | question | [34] | ours |
| `cr-1963-efodi` | commentary · R. Yitzhak Profiat Duran, Ma’aseh Efod | [27] | ours |
| `cr-1963-ibn-ezra` | commentary · Ibn Ezra | [28] | ours |
| `cr-1963-q-h6` | question | [35] | ours |
| `cr-1963-r-avraham` | commentary · R. Avraham ben HaRambam | [29] | ours |
| `cr-1963-q-h1` | question | [30] | ours |

## 10. Stage 4: the garden (2026-10-06)

`data/bereshit.json`, assembled by `research/scripts/build_bereshit.py`:
- an overview, then a fork with 5 themes, each theme with an intro and a fork of 3 years;
- 15 leaves, 54 sections, 446 steps;
- the demo slug `bereshit-chapter-break` retired; its content is the 1963 leaf.

Leaves are in `research/scripts/bereshit_leaves/<theme>.py`. Each leaf's paper trail (cards →
harvest items, slices and start/stop points, omitted questions and why, translation choices) is
in [`bereshit-leaves/`](bereshit-leaves/): `creation.md`, `garden.md`, `sin.md`, `cain.md`,
`flood.md`. The drafting rules are in `bereshit-leaves/BRIEF.md`.

**Decisions made during drafting** (each recorded with its evidence in triage.json or the theme
trail):
- **1964 §ד was dropped** (the sheet's editor wrote it, not Nechama), and §ב is rendered
  instead, after its own scan check.
- **1968 [8] (Moreh 1:24) was re-triaged to publishable.** It had been misfiled as a
  verse-reference label.
- **1953 [46] was re-triaged to spelling.** A mis-paired checker fragment had garbled it.
- **1958 [20], her comparison verses, keeps the digitized text.** She misquotes 2 Kings 2:14
  and Jer 2:28, and the digitizers corrected the quotes.
- **1950 [23], her Ibn Ezra pointer, is on 4:23.** Her start phrase occurs once in the
  chapter, so the verse number is כ"ג.
- **Her slips in references** are translated as written, with the right reference in
  brackets: 1943 Judges 13:9 (the card is omitted), 1965 Isaiah and Hosea in Bereshit Rabbah
  16:5, 1971 Psalms 78→82, 1956 Job and 1 Samuel. The 1954 Moreh's «האמונה» (Ibn Tibbon has
  «האמירה») is translated as written and flagged.

**Harvest fixes found by drafting** (all in `harvest_bereshit.py`):
- a doubtful scan reading no longer writes `[?]` into her text; a doubtful letter is
  corroborated by the digitization's word when they agree;
- fragment fixes apply only on an exact, unique match, and word-level fixes only where
  triage says the scan wins (an earlier normalized fallback mangled items);
- inline tags no longer split words;
- scan-only items have explicit keys;
- the 1943 transcription items have keys;
- the checkers' " / " line-break marks are removed.

The verse cache now strips MAM's variant notes (4:13, 5:1).

**Open for Lev:**
1. **1950:** her Ibn Ezra pointer has no stop. Item [25] continues the same comment but isn't
   in her scan and no question names it, so it isn't quoted. Should it run on?
2. **1942 [52]:** a faded word, «לפשוטו»; the digitized reading is used.
3. **1964 «לעונשים»:** the Akeidah on Sefaria (Pressburg) reads «לאנשים», and the English
   follows it.
