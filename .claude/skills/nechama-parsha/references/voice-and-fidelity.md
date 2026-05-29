# Voice & fidelity — the editorial heart

This is the part that makes a Nechama parsha flow good rather than merely functional.
Three intertwined commitments: **voice**, **source density**, and **faithfulness to her
material**. They reinforce each other — faithful rendering at high density is what lets
the narrator's voice stay quiet.

---

## 1. Faithfulness to her material

The whole premise: this is **her** work, rendered — not a parsha sheet inspired by her.
Hold the line on every one of these:

- **Every commentary card is a source she actually chose.** Open her gilayon
  (`/api/sheets/<id>`), see which sources she cited under each lettered section, and use
  those. Don't substitute a commentator you find more convenient or famous. If her
  section ד quotes the Sifra and Ibn Ezra, the leaf quotes the Sifra and Ibn Ezra.
- **Her order is the leaf's order.** She sequenced the sources deliberately — usually
  problem → first reading → counter-reading → resolution. Preserve that arc.
- **Her questions are her questions.** The numbered questions at the bottom of each
  section are the gold. Translate them faithfully into the `question` cards (with
  `questionLabel: "Nechama asks"`). Don't smooth them into something blander, and don't
  invent questions she didn't pose.
- **Don't invent a "carry-forward."** The general close-read format likes to end with a
  Hasidic + modern voice. Many of her sheets have no such thing. If she didn't reach for
  Rav Kook or the Sefat Emet, don't graft them on. Let the leaf end where she ended —
  usually on a question.
- **Get attributions right.** This is where it's easiest to embarrass yourself. Hizkuni
  is a 13th-c. French Rishon, not a Hasidic master. The Akeidat Yitzhak is R. Yitzhak
  Arama (15th c. Spain). Ibn Kaspi is 14th-c. Provence. If you're not certain of a
  commentator's era/school, look it up before you label them in narration. A wrong
  attribution undermines the whole "faithful to the sources" promise.
- **`primaryText` = the verses her leaves actually anchor on, trimmed honestly.** A theme
  might span Num 6:1–21, but if the leaves only touch verses 2, 5, 7, 11, show only
  those — join the gaps with `…` and set `ref` to the true range (`Numbers 6:1-3, 5, 7,
  11`). Never pad the panel with verses no card references.
- **The research pack is the audit trail.** Before drafting a leaf, the pack should
  record: which gilayon (year + sheet ID), which lettered sections you're rendering, the
  sources in each, and her question. Every claim in the JSON traces back to a line in the
  pack. If you can't cite it, don't ship it.

When her material is genuinely thin for a theme, that's a finding — say so in the pack
and pick a denser theme, rather than inventing to fill space.

---

## 2. Source density — lean toward more of her

**The default failure mode is a thin sheet**: one commentary per leaf, the narrator
paraphrasing the move instead of letting the sources make it. The prototype Nasso
skeleton had exactly this problem. Correct *against* it.

- **3+ of her cruxes per leaf.** A gilayon typically has 3–11 lettered sections. Render
  at least 3. Pick the pedagogically rich ones (below), but don't reduce a leaf to a
  single idea — she didn't.
- **Prefer cruxes where she pits 2+ commentators against each other.** Her signature move
  is the mahloket — Rashi vs. Ramban, the Sifra vs. the plain sense, R. Yashia vs. R.
  Yonatan. A leaf that stages a real disagreement is doing her work; a leaf with one
  voice is doing less.
- **Use her full panel, not just the famous four.** She cited the Sifra, Sifrei, Bamidbar
  Rabbah, Rambam (both Mishneh Torah and the Moreh), Ibn Kaspi, Malbim, Akeidat Yitzhak,
  the Alshich, Hizkuni, Ha'amek Davar, R. Hirsch, and more. Bring them in. The breadth of
  her sourcing *is* the experience.
- **A short prooftext she cites lives inline** in the commentary card's text or
  annotation — not as its own `verse-change`. (See close-read-sheet/hard-rules.md.)

Which cruxes to render (when a sheet has more than 3):

- Prefer cruxes with a sharp question and a highlightable verse phrase.
- Prefer cruxes that *cohere* — three angles on one thread, not three scattered shots.
- Skip pure-grammar cruxes ("why hifil not piel") unless the grammar is the point.
- It's fine for different leaves in a theme to render different cruxes from the same
  passage — that's the across-the-decades contrast working.

---

## 3. Voice — the narrator names, then disappears

The narrator is a guide, not an interpreter. Its entire job is to make Nechama's
editorial choices legible and then step aside so the sources speak.

**What the narrator does:**
- Names the gilayon: the year, what's new about this sheet's angle. *"Gilayon תשי״ג /
  1953. Nine years on, the headline of her sheet has changed."*
- Names the puzzle, in her terms, pointing at the verse phrase that creates it.
- Names who speaks next, and what shifts between voices. *"Ramban accepts the question in
  its sharpest form — but he moves the moment of sin."*
- Frames the closing question.

**What the narrator never does:**
- **Never moralizes.** No life lessons, no "and so we learn that…". The reader draws the
  lesson; the text and the question set it up.
- **Never paraphrases what the commentary is about to say.** Don't pre-chew. Let the card
  land, then (in the `annotation`) name what shifted — that's where interpretation of the
  source belongs, tightly.
- **Never substitutes for a commentator.** If a move is interesting, find the source she
  used to make it and quote that. Narrator-as-pseudo-commentator is the thin-sheet trap.

**Mechanics of voice:**
- **One thought per card.** Let it breathe. This format is for noticing and sitting with;
  compressed multi-clause cards work against it. If a card carries two thoughts, split it.
- **English-only narration.** Hebrew lives in the pinned primary text and in direct
  commentary quotations. Bilingual narration overloads the eye.
- **Her questions get `questionLabel: "Nechama asks"`** (set once in the title block).
  This is what marks the difference between the narrator's framing and her actual query.
- **Cut the tying-the-bow cards.** Restating a question after a commentator already named
  it, or a card that just transitions, adds length without value. Trim them.
- **Bind narration to the verse.** When a card names a phrase that's in the primary text,
  give it a `highlight`. The reader's eye should move between the sidebar claim and the
  pinned phrase. Aim for the majority of cards carrying a highlight (the Nasso build runs
  ~two-thirds). Use `glow` for the crescendo card in a crux, `pulse` on the question.

---

## The test

Read a finished leaf and ask: *Could a knowledgeable reader tell which moves are
Nechama's and which are mine?* If the answer is "it's all hers, I just pointed" — the
leaf is right. If the narrator is doing interpretive work the sources should be doing,
go back and find the source she used.
