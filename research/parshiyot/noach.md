# Parashat Noach — Nechama Leibowitz Research Pack

> Source of truth for `data/noach.json`. Every claim about Nechama in the Close Read must
> trace back to an entry here, and every entry here traces back to a raw file and a sheet
> index. If you can't cite it, don't ship it.

**Status (2026-10-12):** Stage 1 done (snapshot, survey, live verification). Stage 2 design
below (§7), **awaiting sign-off**.

The method, evidence layers (L0 scan → L1 digitization → L2 snapshot → L3 survey → L4 this
pack) and citation form (`161147[43]` = sheet 161147, `sources[43]`) are as in
[`bereshit.md`](bereshit.md) §0. Tags: **[extracted]**, **[PDF-checked]**, **[interpretation]**.

---

## 1. Provenance

- **Corpus:** local MongoDB `sefaria.sheets` (production restore), query
  `{"owner": 54380, "topics.slug": "parashat-noach"}` → 30 sheets, frozen in
  [`noach-raw/`](noach-raw/) with sha256s in `manifest.json` [extracted].
- **Live check (2026-10-12)** [extracted], in [`noach-raw/verification.json`](noach-raw/verification.json):
  - via `curl -A "Sefaria/close-read" https://www.sefaria.org/api/sheets/user/54380/`: 1455 live sheets;
  - the IDs tagged `parashat-noach` = the IDs titled `פרשת נח` = the 30 snapshot IDs;
  - content hash over every `sources[]` item, live vs snapshot: **30/30 identical**;
  - all 30 original scans (`nechama.org.il/pdf/<n>.pdf`) resolve as PDFs; sha256 recorded, not committed.
- **Reproduce:**
  ```bash
  python3 research/scripts/snapshot_parsha.py noach parashat-noach
  python3 research/scripts/survey_parsha.py noach Genesis 6:22,7:24,8:22,9:29,10:32,11:32
  ```
  (The span starts at 6:1; 6:1–8 belongs to Bereshit, so its "uncovered" verses mean nothing.)
- **Dating:** one sheet a year, **30 consecutive years, תש"ב (1942) → תשל"א (1971)**; the
  survey's gematria check passes for all 30. As in Bereshit, the Gregorian label is the year
  the Hebrew year *ends*; Noach is read in autumn, so "1942" was studied in autumn 1941.

## 2. Fidelity findings so far

Everything in [`bereshit.md`](bereshit.md) §2 applies (digitized headers are often the
digitizer's; pointer lists expanded into full texts; her ×/+ marks and footers dropped). New for Noach:

### 2.1 The editor's accent questions are not hers [PDF-checked]

From the 1960s her sheets carry an appended box, **"שאלות בטעמי המקרא — העורך: מיכאל
פרלמן"** (questions on the accents; editor Michael Perlman), with its own footer sending
answers to Perlman, not to her. The digitization folds it into her lettered sections as if
it were hers. Seen by eye on the scans:

| Sheet | Digitized as | Scan |
|---|---|---|
| 1963 (160727) | §ד "טעמי רשימה של שלושה שמות" `[27]–[40]` | p. 2, Perlman box |
| 1966 (160533) | §ה "הכלול באיסור 'אך בשר'" `[24]–[35]` | p. 2, Perlman box |
| 1967 (160496) | §ג "'איתם אל התבה', 'וימח'" `[25]–[39]` | p. 2, Perlman box |

This is the same finding as Bereshit 1964 §ד, and the same rule: **not rendered as
Nechama's.** It removes the three most natural Leningrad moments (the Minchat Shai in 1967
§ג even appeals to "accurate manuscripts" for the rafe mem of וימח, and folio 4v has it).
Every other 1960s sheet chosen below gets checked for a Perlman box in Stage 3.

### 2.2 Header example [PDF-checked]

1954 (161402) §א: the scan's header is **"שאלת מבנה כללי"**; the digitized "למבנה פרשת
המבול" is the digitizer's.

### 2.3 One bilingual edition

1970 (160445) is the Nataf English edition (`outsideBiText`); its section א has no
digitized header (item [0] is the prose "א. דברי ה'").

## 3. Inventory [extracted]

The 30-row table is generated at the top of [`noach-survey.md`](noach-survey.md); the
item-by-item detail follows it there. Not copied here, so it can't drift.

## 4. Tentative clustering [interpretation]

| Cluster | Passage | Sheets (year · id) | n |
|---|---|---|---|
| **A. Noah and his generation** | 6:9–7:5 | 1942 נח · 161881 — 1947 נח · 161777 — 1954 הסיבה למבול · 161402 — 1956 השינויים בפסוקים מקבילים · 161301 — 1958 "אלה תולדות נח" · 161147 — 1959 דור המבול + הפטרה · 161181 | 6 |
| **B. The flood and leaving the ark** | 7:6–8:19 | 1945 דור המבול · 161721 — 1952 היציאה מן התיבה · 161472 — 1953 המבול · 161275 — 1961 המבול · 160824 — 1962 אחר המבול · 160700 | 5 |
| **C. "Never again": the offering, the heart, the bow** | 8:20–9:17 | 1946 היציאה מן התיבה · 161548 (mostly 8:21) — 1951 אות הברית · 161581 — 1963 הברית · 160727 — 1964 היונה והברית · 160639 | 4 |
| **D. Blood and the image of God** | 9:1–7 | 1943 ברכת ה' · 162001 — 1948 "אך את דמכם" · 161496 — 1949 מצוות בני נח · 161835 — 1950 "ויברך אלקים את נח" · 161440 — 1957 ברכת ה' לנח · 161105 — 1970 מצוות בני נח · 160445 — 1971 "ואך את דמכם" · 162070 | 7 |
| **E. Babel** | 10:1–11:9 | 1944 · 161942 — 1955 · 161235 — 1960 נמרוד · 161686 — 1967 · 160496 — 1968 · 160443 — 1969 · 160481 | 6 |
| *(other)* | | 1965 תחילתו של אברם · 160578 (11:28–12:5); 1966 הפטרה · 160533 (Isaiah 55; one section on 9:4, Perlman's) | 2 |

Observations (all [interpretation] on [extracted] facts):
- **9:1–7 is her most-returned passage: seven sheets.** 9:5, "מיד כל חיה אדרשנו", gets a
  whole sheet in 1948 and again in 1971, with almost the same panel of ten voices 23 years apart.
- **Babel gets four sheets in four years running, 1967–69 plus 1960**, three of them titled
  identically "דור הפלגה" (1944, 1967, 1968, 1969).
- **She returns to "בדורותיו" (6:9)** in 1947 and 1958, both with the Bereshit Rabbah on
  Noah vs. Abraham.
- Her own cross-links [extracted]: 1949 → 1943, 1948; 1950 → 1948, 1949; 1953 → 1946, 1952;
  1955 → 1944; 1957 → 1948, 1949, 1950; 1959 → 1958 ("this sheet continues 1958"); 1964 → 1962;
  1967 → 1955, 1960.

## 5. Coverage and absences (candidates only)

From linked refs [extracted]; upper bounds, to confirm against the scans before anything is said:
- **Noah's drunkenness and the curse of Canaan (9:20–27): no sheet touches it.** The only
  9:18+ ref is 1963's list of the three sons (9:18), which is Perlman's section.
- **The table of nations (ch. 10)** is touched only for Nimrod (10:8–9) and in the Babel
  sheets' "ch. 10 vs ch. 11" questions.
- **The Shem genealogy (11:10–27)**: untouched.

## 5a. Masoretic layout (Leningrad Codex)

Source: tanach.us WLC `Genesis.xml` (retrieved 2026-10-12), a transcription; confirm on the
facsimile before showing anything. Breaks in the parsha: ס after 6:12, 6:22, 8:14, 9:7;
פ after 9:17, 9:29, 10:32, 11:9; then ס after each generation of 11:10–25 and after 11:32.

**So the flood story (6:9–9:17) is five Masoretic sections: 6:9–12 · 6:13–22 · 7:1–8:14 ·
8:15–9:7 · 9:8–17.** The middle one, the whole flood from "בא אתה" to the dry land, runs
36 verses with no break.

Folios (Sefaria manuscripts API, `leningrad-codex-(1008-ce)`): 4v = Gen 6:19–7:23
(`BIB_LENCDX_F004B.jpg`, 3590×4115), 5r = 7:23–9:2 (`F005A`, 3866×4231). On 4v, by eye: the
6:22 break is in column 1; 7:1 onward then runs through all three columns without a gap.
The 6:12 break is on folio 4r, so no single page shows both of the first two breaks.
**To confirm and measure in Stage 3, if used.**

Talmud: Sanhedrin 108a (1958 §ז's source) exists as Munich 95 (1342) p. 714, Bomberg and
Vilna. The Munich page carries 106b–108b in a small dense hand.

## 7. Stage 2 design proposal (awaiting sign-off)

**Shape (as Bereshit):** overview → root fork (5 themes) → per theme: intro → fork (3
gilyonot) → leaf. 15 leaves. Picks favor a spread of years, real mahloket, and at least 3 of
her sections. Section lists are from the digitization; each chosen sheet gets a full scan
check (every page, and a Perlman-box check) before drafting.

### Theme 1 — A righteous man in his generations (6:9–7:5)

| Leaf | Sheet | Sections to render | Why |
|---|---|---|---|
| **1947** | 161777 | א (ch. 6 vs ch. 7 parallels, Malbim) · ב ("תולדות": Ibn Ezra vs Ramban, 3 Qs) · ג (Rashi "בדורותיו", Levush HaOrah's question, Bereshit Rabbah: Noah and Abraham) | Early; the first pass at 6:9 |
| **1954** | 161402 | א (Cassuto's 12 paragraphs; *optional* Leningrad, see below) · ב ("כי השחית כל בשר": Rashi vs Ramban, 5 Qs) · ג (building the ark as a warning: Tanchuma, its variant, Rashi) | Structure, then the sin, then the ark |
| **1958** | 161147 | א ("תולדות": Rashi's two readings, Radak, Gur Aryeh) · ב–ג ("בדורותיו": Tanchuma's coin and balsam, Levush HaOrah) · ד (Noah vs Abraham, BR 30:10) · ו–ז (חמס: Rashi and Sanhedrin 108a) | 6:9 again, 11 years on, much denser |

Alternates: 1956 (praise to his face; "מפני מי המבול": Rashi, Radak, Ashtruk, Kli Yakar),
1959 ("הארץ", "לפני": Ibn Ezra, Cassuto, Ashtruk; Ramban on חמס), 1942 (her first; thin sections).

### Theme 2 — The flood (7:6–8:19)

| Leaf | Sheet | Sections | Why |
|---|---|---|---|
| **1945** | 161721 | א (structure and style: why the birds last, the waters' stages, Ramban's two readings) · ב (the flood generation in midrash, via Rashi) · ה ("ויסגור ה' בעדו": Onkelos, Malbim, Nachalat Yaakov, Ibn Ezra) | Early; literary questions |
| **1952** | 161472 | א ("ויזכור": Rashi vs Ramban, Ibn Ezra) · ב (leaving the ark: BR 33:6 on the dove; Aggadat Bereshit vs Tanchuma "I'd have broken the ark") · ג (raven vs dove, וישלח) | The midrashic mahloket on waiting for permission |
| **1962** | 160700 | א ("ויזכור": Ibn Ezra, Wessely, Cassuto, 7 Qs) · ב (what remembering means: Ibn Ezra, Ramban, Bahya, Ibn Kaspi, Cassuto) · ד (Noah's offering: BR 34:6, 34:9, Pirkei DeRabbi Eliezer) | Same verse as 1952, ten years on, wider panel |

Alternates: 1961 (the lists of the perished: Ibn Kaspi, Malbim, Cassuto; Noah's wife), 1953
(Akeidah's lessons, the drying stages, Ramban on offerings).

### Theme 3 — Never again: the heart, the dove's leaf, the bow (8:20–9:17)

| Leaf | Sheet | Sections | Why |
|---|---|---|---|
| **1946** | 161548 | א (Rashi, incl. which curse of the ground) · ב (the order of the animals) · ג ("כי יצר לב האדם רע מנעוריו": Abarbanel's question; Akeidah ×2, Hirsch, "יש מפרשים", Ibn Ezra; 9 Qs) | Early; the great crux of 8:21 |
| **1951** | 161581 | א (Cassuto's "אתכם" ↔ "חתכם") · ב (the rainbow: Abarbanel's question, Ramban) · ג ("בענני ענן": Radak) · ד ("וראיתיה": Radak vs Shadal) | The covenant sign |
| **1964** | 160639 | א ("טרף": Rashi vs Ramban, 10 Qs) · ב (Ibn Kaspi on "כי") · ג (youth of man and world: Abarbanel, Tedeschi, Shadal) · ד (does the earth end? Ibn Ezra vs Ibn Kaspi) | 8:21 again, 18 years after 1946 |

Alternate: 1963 (the covenant: Ibn Ezra, Radak, Ralbag, Abarbanel, Sforno, Cassuto, Shadal;
its §ד is Perlman's).

### Theme 4 — Your lifeblood: blood and the image of God (9:1–7)

| Leaf | Sheet | Sections | Why |
|---|---|---|---|
| **1948** | 161496 | א ("מיד כל חיה אדרשנו": BR, Midrash Aggadah, Rashi, Rambam Rotze'ach and Moreh, Ramban ×2, Radak, Ralbag, Melekhet Machshevet, Wessely) · ב (the blessing compared with Adam's) | One verse, ten voices: are animals answerable? |
| **1957** | 161105 | א (order of creatures in the two blessings) · ב ("ומיד האדם": Rashi, HaKtav VeHaKabbalah) · ג–ד ("ואך את דמכם": Ibn Ezra vs Rashi) · ה–ו ("בצלם אלקים": Avot, Maharsha's question; Radak, Chizkuni, Malbim: murdered, murderer or judge?) | Mid |
| **1970** | 160445 | א (God's first words to Adam and to Noah) · ב (meat permitted: Hirsch) · ג ("בנפשו דמו": Radak, Abarbanel, Ibn Kaspi) · ד ("ואך": Rashi, Bekhor Shor) | Late; English edition exists (Nataf) |

**Open: 1948 vs 1971.** 1971 is her last Noach sheet and returns to 9:5 with nearly 1948's
panel, plus BR 34:13 with Matnot Kehunah on Saul and Ibn Ezra's second commentary (7 Qs to
1948's 4). Options: keep 1948; swap 1957 or 1970 for 1971; or 1971 instead of 1948.
**1970 consequence:** it's the Nataf English edition, so its questions have a published
English; `en_basis` would need a `nataf` value that the lib and `test_provenance.py` accept.

Alternates: 1971 (9:5 again, nearly 1948's panel plus BR, Ibn Ezra's second commentary,
Chizkuni; the "23 years later" return, but it repeats 1948), 1949, 1950, 1943.

### Theme 5 — Babel (10:1–11:9)

| Leaf | Sheet | Sections | Why |
|---|---|---|---|
| **1944** | 161942 | א (their sin: BR, PdRE's bricks, Rashi, Ibn Ezra, Sforno, 5 Qs) · ב (Rashi) · ג ("וירד ה' לראות": Moreh 1:10, Rashi, Sforno) | Early |
| **1960** | 161686 | א (Abarbanel: Nimrod and Babel as one sin, inequality) · ב (Nimrod: BR, Maharzu, Rashi, Gur Aryeh) · ג ("שפה אחת": Abarbanel, PdRE) | Abarbanel's reading of civilization |
| **1968** | 160443 | א (the dispersion before Babel: Radak, Bekhor Shor, HaRekhasim LeBik'ah, Hirsch) · ג ("עיר ומגדל": HaRekhasim) · ד ("לא יבצר": Rashi, Wessely, Ibn Kaspi) | Late; ch. 10 vs ch. 11 |

Alternates: 1955 (PdRE, Malbim, Cassuto; Radak on "בני האדם"; Kaufmann on Isaiah 2), 1967
(Benno Jacob on ch. 10/11; the midrashim on their sin; Bahya; its §ג is Perlman's), 1969 (Buber's leitwords).

### Overview and image moments

- **Overview** (facts established), matching what Bereshit shipped: the span, "five passages,
  each read through the sources and questions Nechama Leibowitz set for it", and "she wrote
  on this parsha every year from 1942 to 1971" (Bereshit's keep-or-cut question on that card
  is still open; same answer applies here). Absences (9:20–27) only after the scan check.
- **Leningrad: none by default; one optional moment, 1954 §א.** Cassuto divides the flood
  story into 12 literary paragraphs, and her scaffold gives the first two (6:9–12, 6:13–22),
  which coincide with the Masoretes' first two sections. The codex then runs 7:1–8:14 with no
  break, where Cassuto finds several paragraphs. **Caveat:** unlike Bereshit 1963, where
  Benno Jacob's claim was itself about the paragraphing, the page here doesn't evidence her
  source; it offers a *different* division, and setting the two side by side is a contrast
  Nechama didn't draw. Folio 4v shows the 6:22 break and the unbroken run, not the 6:12 break
  (on 4r). Use only if Lev wants the contrast.
- **Talmud manuscript: none proposed.** The one candidate is Munich 95 for Sanhedrin 108a
  (1958 §ז, the source of Rashi's "לא נחתם גזר דינם אלא על הגזל"). Her question is about
  Rashi's style versus the Gemara's text, so the manuscript would illustrate, not evidence,
  and the line is hard to read at phone size. Available if wanted.
- **Not used:** the three Perlman accent sections (§2.1).

### 7a. Decisions (Lev, 2026-10-12)

1. **No manuscript images in Noach.** Her own questions never rest on page layout, and the strong
   accent moments are Perlman's (§2.1). The 1954 Leningrad contrast and the Munich Sanhedrin
   page stay unused.
2. **Blood theme: 1948, 1957, 1970.** 1971 stays an alternate. 1970 is the Nataf edition (§7).
3. **Everything else as proposed in §7.**

## 8. Stage 3: scan check, triage, harvest (2026-10-12)

**3a. Scan checks.** All 15 sheets, every section and every page, are checked against their scans in
[`noach-scancheck/`](noach-scancheck/) (five parallel checkers; method in its README). I
spot-checked one finding per checker on the scan, and all five held:
- 1968 §ד Q3 is a different question in the digitization;
- 1945 §ה Q2 is missing;
- 1946 §ג Q8 is cut to its tail;
- 1957 [27] «בבמה» is a typo for Rashi's «בבהמה»;
- 1958 §ג opens with a Rashi the digitization lost.

**What the scans show, beyond Bereshit's §2 findings:**
- **Lost or rewritten questions:**
  - 1968 §ד Q3 is replaced by an unrelated question ("the idea symbolized in this midrash"; there's no midrash in that section).
  - 1945 §ה Q2, 1951 §ב Q3, 1960 §ד's last question, and 1944 §ב Q5 and Q7 are missing.
  - 1946 §ב Q1 and §ג Q8 have lost their openings.
  - 1958 §ג Q3 is reworded.
- **Lost sources:** two Rashi passages she printed in full (1958, heads of §ג and §ד).
- **Other losses:**
  - Her underlining is dropped, and several questions ask about «המסומן בקו»; the checkers recorded the spans.
  - Her x/xx and +/++ difficulty marks, legends and footers are dropped (1946, 1951 and 1964 keep them as `*`).
  - 1970's section ה header is dropped, and its §ו is relettered ה.
  - 1960 has no section ג in the scan; the digitizer's ג is her ד.
- **Placement:** 1962 §ד's three midrash blocks are printed 2, 3, 1 in the scan.
- **Absences [PDF-checked, all 30 scans]:**
  - No sheet studies Noah's drunkenness or the curse of Canaan (9:20–27). The only trace is 1961's
    bare pointer «ט' כ'», given as an example of the word אדמה; the digitization links it to 6:20.
  - 11:10–25 is never quoted.
  - Ch. 10 appears only as context for Babel (Nimrod, 10:5, 10:32).
- **Perlman's box** is in exactly 1963, 1966 and 1967 (§2.1), and in no chosen sheet. 1968's boxed
  note is a subscription notice; 1953's scan shares its pages with Lech Lecha 1953.

**3b. Triage.** Each of the 114 substantive lines in her own words is decided in
[`noach-scancheck/triage.json`](noach-scancheck/triage.json), with its reason. Most are form-only:
plene/defective spelling, «מהן»/«מה הן», numbering, marks. For those **the digitization is kept**,
because applying the checkers' mark-laden fragments garbles her text. Real word differences take
the scan's reading. Five scan-only questions and two scan-only Rashi passages are inserted from
`overrides.json`, and two word-level fixes are applied by its new `replace` list:
- 1952's verse list: 37:13–14, not 17:13–14;
- 1958 §ג Q3 in her wording.

Every inserted question was read on the scan by Claude, not just by a checker, except 1944's two
short ones («מה קשה לו?», «מניין לו שאינו כמשמעו?»). **REVIEW.md is empty.**

**Harvest fixes** (in `harvest_noach.py`; `harvest_bereshit.py` has the same three bugs, harmless
there only because its differences were all triaged and its output reviewed):
1. Untriaged substantive differences used to be dropped silently; now they're held as
   `scan_pending` and listed in REVIEW.md.
2. Her difficulty marks used to be written into her text («1xx.», «xx צידה לדרך»); now they're stripped.
3. A fragment whose «…» gaps don't line up used to replace the whole fragment, writing the
   «…» in; now it's left unapplied.

**Source texts** (not her words) can still carry `scan_pending` differences, e.g. 1957's
«בבמה», 1964's Ramban «מהם בזרות», and 1968's Hirsch sentence. Drafters settle any they quote against
the source's own text and record it in the theme trail.

Verse texts for the parsha (plus Genesis 1) are cached in `noach-verses.json`.
