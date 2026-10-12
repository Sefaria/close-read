# Noach scan checks (Stage 3a)

One file per chosen gilayon: `<sheet_id>-<year>.md`. Each file checks **Sefaria's
digitization** (`../noach-raw/<id>.json`, listed item by item in `../noach-survey.md`)
against **Nechama's original scan** (`https://www.nechama.org.il/pdf/<n>.pdf`), covering only
the sections the leaf renders (pack §7).

This is **verification, not transcription.** The digitization is an independent reading of
the same scan by Sefaria's digitizers. Where the checker's reading of the scan agrees with it,
that agreement is the evidence. Where they disagree, the line is flagged for a person to settle.
A DIFF is a flag, not a ruling.

## Method (every checker follows this)

1. Read the scan from the 300 dpi page strips (`page<N>_strip<k>.png`, 8 strips per page,
   overlapping by about 30 px). For any single doubtful word, crop and zoom it from
   `page<N>.png`. **Read every page**: most scans are two pages.
2. Typewriter confusions to watch for: **ש/ט/ס**, **ד/ז/ר**, **ב/נ/כ**, **ת/ח**, **ו/ן/ז**,
   **ה/ח**. Resolve by context only when the scan is truly ambiguous, and mark the letter `[?]`.
3. Record what the scan **shows**, including her own typos, marked `[[sic: …]]`. Don't
   normalize spelling, defective/plene forms, or punctuation.
4. No English, no interpretation, and no judgment about which reading is better.
5. Write only your own file(s) in this folder. Touch nothing else.

## Calibration examples (already found)

- **Typo inside her words:** 1944 (161941) `[7]` digitized `פסוק ה'`, scan `פסוק ח'`
  (Rashi's וישמעו is 3:8). Status: DIFF.
- **Renamed header:** 1963 (160726) §א digitized `פתיחת הפרק ב"ויכולו"`, scan `שאלת מבנה`.
  1959 (161180) §ב digitized `בעשרה מאמרות נברא העולם`, scan `שאלה כללית`. Status: DIFF (header).
- **Spelling:** 1963 `[2]` digitized `בפירושו`, scan `בפרושו`. Status: DIFF.
- **Expanded pointer:** 1944 §ב scan says `עיין רש"י, ראב"ע (עד גם הוא אחר) רמב"ן`, and the
  digitization has full Rashi/Ibn Ezra/Ramban texts. The scan names the source and a stopping
  point; the full text is the digitizer's. Status for each ref item: EXPANDED (stop: …).
- **Dropped sources:** 1943 named Malbim, Rashi and Onkelos, none of them digitized. Status: MISSING-IN-DIGITIZATION.
- **Digitizer lettering:** 1951 `א.` is not in the scan (single unlettered section).
- **Dropped marks/footer:** 1944 `+` difficulty marks and footer note.

## Editorial additions are not errors (Lev, 2026-10-06)

When the digitization **adds** citation detail the scan doesn't have, record it as a DIFF as
usual, but it's a purposeful editorial addition, not a mistake. Examples: "פרשה י"ט" after
"בראשית רבה", "פרק … פסוק …" around a bare reference, "(תרגום מגרמנית)", "(שהובא בראב"ע)". The
harvest keeps the digitizer's richer citation and leaves it off the review list. A citation
that is *changed* (a different number or book) is still a real difference.

## File format

```markdown
---
sheet: 160726
year: 1963 (תשכ"ג)
pdf: 302.pdf
pdf_sha256: <from ../noach-raw/verification.json>
pages: 2
sections_checked: [א, ג, ד, ה]
checked_by: <agent>, 2026-10-06
---

## §א (scan page 1)

**Scan header (verbatim):** …
**Digitized header:** [1] …

| [i] | kind | status | scan reading (only if not MATCH) |
|---|---|---|---|
| 2 | prose | DIFF | … |
| 4 | ref Abarbanel on Genesis 1:1:8 | EXPANDED (stop: …) / MATCH / NOT-IN-SCAN | … |

### Her words: scan ≠ digitization
- [i] digitized: «…» / scan: «…»

### Sources she named that the digitization lacks
- name, pointer as written, `עד` stopping point if any

### Digitizer additions / omissions
- lettering, expanded pointers, dropped `+` marks, footers, numbering
```

Status values: **MATCH** (scan and digitization agree, allowing for the digitizer's
punctuation of quote marks and gershayim); **DIFF**; **EXPANDED** (the scan names or
excerpts the source more briefly; give the stopping point if one is written); **NOT-IN-SCAN**;
**MISSING-IN-DIGITIZATION** (the item is in the scan only; put it in the list). For a ref item,
compare what the scan prints for that source (full quote, excerpt, or bare pointer).

At the end of each file, add **Summary**: counts per status, and the list of `[i]` lines whose
words are **quotable** (questions, her prose, headers) and are DIFF or MISSING. Those go to Lev.

## Noach additions (2026-10-12)

- The calibration examples above are Bereshit's; the method is unchanged.
- **Editor's box.** From the 1960s a sheet may end with a box headed «שאלות בטעמי המקרא —
  העורך: מיכאל פרלמן», with its own footer. It is the editor's, not Nechama's (pack §2.1).
  If a checked sheet has one, say so at the top of the file and list the `[i]` range it covers;
  those items are **EDITOR**, not hers, and are never quoted.
- PDFs are in the session scratchpad (`noach-pdf/<n>.pdf`); render pages with PyMuPDF (`fitz`)
  at 300 dpi. `qlmanage` renders only page 1.
