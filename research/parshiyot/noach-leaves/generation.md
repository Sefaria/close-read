# A righteous man in his generations (Gen 6:9–7:5): leaves 1947, 1954, 1958

Built by `research/scripts/noach_leaves/generation.py`. Checked with
`python3 research/scripts/check_leaves.py noach generation`: 9 sections, 89 steps, 0 failing checks
(1947: 29 steps · 1954: 24 · 1958: 36). Every commentary and question card slices a harvest item
verbatim. All English is ours (`en_basis: "ours"`): every quote is abridged, carries her framing,
or is the digitizer's expansion of a bare pointer.

**Render risk.** `check_leaves` doesn't run `test_render.py`. The 1947 comparison panel's right
side is six fragments (about 45 Hebrew words); if the mobile check complains, cut the 6:21 row
first (her parenthetical «והשוה», not a table row proper) and drop `r-kach` from `row-take`.

**Checker note.** At the time of drafting, `data/index.json` (modified in the working tree by
another session) lists `noach`, but `data/noach.json` doesn't exist yet, so `check_leaves.py`
fails on import (test_data.py parametrizes over every listed sheet). I ran it through a scratchpad
wrapper that drops missing slugs from `sheetmodel.sheet_slugs()`; the checks themselves are
unchanged. Nothing in `data/` or `tests/` was touched.

**Open triage in this theme:** none. Every item quoted is `digitized`, `scan`, `editorial` or
untriaged MATCH/EXPANDED. **NOT-IN-SCAN sources quoted:** none (the only NOT-IN-SCAN item, 1958
[11], is `publish: false` and not used).

**Card type follows what the item is, not the harvest `kind`.** Her questions held as `text`
(1947 [2], [13], [15], [24]) are `question` cards; sources held as `question` (1947 [23] Levush
HaOrah; 1954 [19], [20] Tanchuma; 1958 [16] Tanchuma Buber) are `commentary` cards.

**Local helper.** `frag()`/`side()` in `generation.py` build the 1947 comparison panel from verse
*fragments*: Hebrew via `vp()` on the cached verse, English asserted to be a verbatim substring of
the cached JPS. Not in the lib; it could move there if other themes want fragment tables.

---

## 1947 (תש"ז) · sheet 161777 · `leaf_1947`, prefix `gn-1947`

**Sections rendered:** §א (comparison panel, ch. 6 right / ch. 7 left, as her table), §ב (panel
6:9–10), §ג (panel 6:9). All her sections.

**Panel §א.** Her table [3] is the panel: right column 6:13, 18, 19, 20, 21, 22; left 7:1, 2, 3, 5,
each the fragment she quoted, extended where hers would not stand alone (6:13 through «בא לפני»,
6:19 through «תביא אל התבה», 6:20 through «יבאו אליך», 6:21 «ואתה קח לך מכל מאכל אשר יאכל» — her
«והשוה ו' כ"א»). The word group `r-lemino` spans the whole «מהעוף למינהו … למינהו» run so that
"of every kind" (three times in the JPS) is one group: that's what Q2 [7] asks about.

**Slices:**
- [2] whole («השוה את הפסוקים המקבילים… כגון:»), a question card (no number, as harvested); its
  «כגון:» points at the panel. Five narrations then walk her table's rows, each only quoting the
  paired fragments.
- [4] «ועוד ועוד ועוד...» not rendered (it closes her table).
- [5] Malbim from «והנה דיבור» (her label «מלבי"ם:» dropped; it is the card label). No `ref`:
  the harvest gives none, and I did not want to guess the Malbim segment.
- [6], [7] whole.
- §ב [11] Ibn Ezra from «אלה תולדות:»; [12] Ramban split at «למה ציוהו בתיבה.» / «ואף על פי»,
  whole item across two cards. Both are EXPANDED from the names in her header («ראב"ע - רמב"ן»),
  bare names, no stop. Ramban [12] carries «(הראב"ע, והרד"ק)», an edition's gloss; translated as
  "(Ibn Ezra and Radak)".
- [13] her Q1, whole, **no number**: the digitization dropped her «1.» and the scan's reading was
  not applied (gaps don't line up). Shown as harvested.
- [14] Ibn Ezra on 37:1 from «והטעם אלה תולדות» (her start point, triage `editorial`); her pointer
  lead-in is not shown. Label "Ibn Ezra, on Genesis 37:1"; lights «תולדת» in 6:9.
- [15], [16], [17] whole.
- §ג [19], [20] Rashi (digitizer's text for her pointer «1) ט ד"ה אלה תולדות נח»), [19] from
  «אלה תולדות נח:». [21] whole, pointer «(ועיין רש"י י"ח י"ח)» included. [22] Rashi from
  «בדורותיו:» (digitizer's text for «2) "בדורותיו"»).
- [23] Levush HaOrah from «מאי טעמא»: her lead-in «לבוש האורה (ר' מרדכי יפה) מקשה על סגנונו של
  רש"י:» is not shown; the label carries "Levush HaOrah (R. Mordechai Yaffe)". [24] whole.
- [25] Bereshit Rabbah from «"משל»: her lead-in «דברי רש"י אלה לקוחים מבראשית רבה:» is not shown
  (it refers to a Rashi on «את האלהים התהלך נח» that 1947 doesn't print). Ref Bereshit Rabbah 30:10.
- [26], [27] whole («א.», «ב.» kept, rendered "a.", "b.").

**Omitted questions:** none.

**Translation, second look:**
- Malbim: «שם אלוקים» as "the name Elohim" (his point is the name), «ה'» as "the Lord".
- [22] keeps the digitized «(סנהדרין ק"ט)» as "(Sanhedrin 109)"; the passage is at 108a. A
  digitizer's citation inside the digitizer's text; not corrected.
- "toledot" is transliterated throughout §ב–ג; the panel's JPS reads "This is the line of Noah".

---

## 1954 (תשי"ד) · sheet 161402 · `leaf_1954`, prefix `gn-1954`

**Sections rendered:** §א (panel 6:9–13), §ב (panel 6:11–13, 19), §ג (panel 6:13–14). All her
sections. No manuscript image (§7a).

**Slices:**
- §א [1] Cassuto from «מבנה הפרשה» (her lead-in «קאסוטו בספרו "מנח עד אברהם"… כותב:» is in the
  label, "Cassuto, From Noah to Abraham").
- [2] Q1 cut at «ואת שתי המערכות»: the rest is her blank table, which flattens into an unreadable
  run of numbers. The rows she filled in (1: 6:9–12; 2: 6:13–22; 3: from 7:1; set B, 7–12) are
  given by the narration `gn-1954-rows`, which lights the openings of 6:9 and 6:13. **Second look:**
  that narration renders her scaffold, not a source; cut it if it reads as answering.
- [3] whole, the scan's reading (triage `scan`: «המתארים דרגה אחר דרגה»), with its lettering «ב)».
  [4], [5] whole, numbered «3.», «4.» (triage kept the digitization). So §א shows «1.», «ב)», «3.»,
  «4.», exactly as harvested; her scan has א)–ד) throughout.
- §ב [8] Rashi from «כי השחית כל בשר:»; [9] Ramban from «כי השחית כל בשר את דרכו:»; [10] Ramban
  whole («ועל דרך הפשט…»). All EXPANDED from bare pointers. Order: Rashi, Q1, Ramban (a), Q2–Q4,
  Ramban (b), Q5. Sources and questions each keep her order; Q1 follows Rashi, Q5 follows the
  Ramban it quotes.
- [11]–[15] whole.
- §ג [19] Tanchuma from «בא וראה», [20] «נוסח אחר» from «עמד נח»; Q1–Q2 [22], [23] follow them;
  then Rashi [21] from «עשה לך תבת:», Q3–Q4 [24], [25].

**Omitted:** [16], her cross-reference to the 1948 gilayon («לכל שאלה ב עיין גליון נח תש"ח…»):
it points to another sheet, not a question.

**Source slips (not fixed; reported):**
- [20]: the digitized «ואמר לו לעשות תיבה» is, per the scan check, «ואמר לי» on her sheet (Noah is
  speaking). The Hebrew is quoted as harvested; the English reads "He told him [read: me] to make
  an ark". A candidate for `overrides.json` `replace`.
- [19]: the scan's «להצילך[?]» is doubtful; the digitized «להצילן» stands ("saved them").

**Translation, second look:** [19] «להצילן בדברו או להעלותן לשמים באמונתו» as "saved them by His
word, or raised them to heaven by His faithfulness"; «באמונתו» could equally be Noah's faith ("by his
faith"). «מערכה» as "set" (Cassuto's two series of six); «חמס» in Ramban
as "chamas" (the panel's "lawlessness").

---

## 1958 (תשי"ח) · sheet 161147 · `leaf_1958`, prefix `gn-1958`

**Sections rendered:** §א (panel 6:9), §ב–ד (panel 6:9), §ה–ז (panel 6:11–13). All seven.

**Slices:**
- §א Rashi [2] split at «דבר אחר»: (a) from «אלה תולדות נח נח איש צדיק:» through «לברכה".»;
  (b) from «דבר אחר». Radak [3] from «אלה תולדות נח:».
- Order: Rashi (a, b), Q1, Q2, Q4, Q5, Tanchuma [9], Radak [3], Q6, Q7. Q1–Q5 ask about Rashi and
  follow him; Q6–Q7 ask about Radak and follow him. On her sheet Radak stands right after Rashi,
  with all seven questions after both.
- [9] her parenthesis, sliced from «"תלדותיו» (the Tanchuma's words she quotes, «תנחומא נח ב'»),
  as a Tanchuma card.
- §ב [16] Tanchuma Buber from «מהו» (her label «תנחומא באבער נח ה':» → label and ref). [17] whole.
- §ג 'before 19' (the Rashi she printed, lost in the digitization) from «"בדורותיו":»; [19] Levush
  HaOrah from «ודע» (her lead-in «ופרש דבריו ר' מרדכי יפה בעל "לבוש האורה" על רש"י:» → label
  "Levush HaOrah, on Rashi"); [20], [21], [22] whole ([22] in her wording, restored by overrides).
- §ד 'before 24' (the Rashi she printed) from «ובאברהם»; Bereshit Rabbah [24] split at «ר' נחמיה
  אמר» (a: through «שהיה כוחו רע – "את האלוקים התהלך נח".»). [25]–[27] whole. [28] cut at «סימן
  הוא להוראה אחרת בנמשל.», dropping only «ועיין גיליון בראשית תשי"ח שאלה ג!)», a pointer to another
  gilayon. Her note («שים לב: …») stays, so the card ends with an unclosed parenthesis in both
  languages. **Second look.**
- §ה [31] from «חמס: גזל»; [32] from «גזל, שנאמר» (her lead-in «ויש ספרים שכתוב בהם ברש"י:» → label
  "Rashi, in some editions"); [33] whole.
- §ו Rashi [36] whole; [37], [39] whole.
- §ז Sanhedrin [43] whole; [44] cut at «דברי הגמרא האלה?» (triage: slice before her parenthesis,
  whose year differs between scan and digitization); «(עיין בשאלה ג')» stays, since it points to
  §ו Q3 in this leaf. [45] whole.

**Omitted for density (36 steps even so):**
- §א Q3 [6] («העתק את פסוקנו פעמים וסמנו בסמני פסוק…»): a copy-out exercise. The same exercise is
  inside 1947 [21], which is quoted whole.
- [10] «ולא נאמר שם "עיקר תולדותיו")»: her aside closing the Tanchuma parenthesis. It is not a
  question, and Q5 already sets the two wordings side by side.
- §ו Q2 [38] («מה הרעיון הכלול בדבריו?»): the most general of §ו's three questions.
- [40] «ענה לשאלתו.»: a one-line imperative after Q3 [39], which already asks.
- [11] is `publish: false` (NOT-IN-SCAN).

**Translation, second look:**
- [7] «לא נחה דעתו אף באחד מהם» as "he was not at ease with either one of them alone".
- [19] «שלא היה אדוק בצדקתו» as "he was not steadfast in his righteousness".
- [24] «עד שאתה…» as "Rather than…".
- The intro to §ה–ז names the word: "The word for lawlessness is chamas." The cards use "chamas"
  because Rashi's gloss and her question [33] are about the word.

---

## Blurbs

- **1947** God speaks to Noah twice, as Elohim and as the Lord; then “toledot,” and “in his age.”
- **1954** The story’s twelve paragraphs, “all flesh” for Rashi and Ramban, and the ark as a warning.
- **1958** “Righteous in his generations”: praise or blame, Noah beside Abraham, and the robbery that
  sealed the flood.

## Review fixes (Claude, 2026-10-12)

- **1954 [20]:** «ואמר לו לעשות תיבה» is now «ואמר לי» via `overrides.json` `replace` (Noah is
  speaking; read on the scan). The English reads "He told me", with no bracket.
- **1958 [28]:** Q4 now stops at «בין דעותיהם?». Her note in parentheses ends in a pointer to
  another gilayon, and any slice inside it left an unclosed parenthesis. The note («שים לב: שימוש
  בדימוי אחר…») is lost from the card and recorded here.
