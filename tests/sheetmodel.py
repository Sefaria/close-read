"""Python mirror of the engine's structural rules (js/engine.js).

Both test layers use this so that "what the engine should render" is computed
once, from the data, with the same rules the engine applies:

- groupSections / primaryKey / mergedPrimaryText (shared sticky panels)
- buildBranchTree / pathToVisibleSet / normalizePath (branching)
- activateStep's backwards search for the active verse

If you change one of those engine functions, change its mirror here.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load_index():
    return json.loads((DATA / "index.json").read_text())


def sheet_slugs():
    """Sheets under test. examples/ holds reference prototypes, not shipped content."""
    return [e["slug"] for e in load_index() if not e["slug"].startswith("examples/")]


def load_sheet(slug):
    return json.loads((DATA / f"{slug}.json").read_text())


# ─── Grouping (engine.groupSections) ───

def primary_key(pt):
    if pt.get("mode") == "image":
        return f"image:{pt['ref']}|{pt['src']}"
    if pt.get("mode") == "comparison":
        return f"cmp:{pt['left']['ref']}|{pt['right']['ref']}|{pt['left']['he']}|{pt['right']['he']}"
    return f"single:{pt['ref']}|{pt['he']}"


def merged_words(pt_list):
    words = {}
    for pt in pt_list:
        words.update(pt.get("words") or {})
    return words


def is_image(verse):
    return verse.get("mode") == "image"


def targets(verse):
    """What a step's `highlight` ids resolve against: word groups, or an image's regions."""
    return (verse.get("regions") if is_image(verse) else verse.get("words")) or {}


@dataclass
class Group:
    dom_id: str                 # id of the .cr-section element (first sub-section)
    sections: list
    is_decision: bool = False

    @property
    def primary(self):
        base = self.sections[0]["primaryText"]
        if is_image(base):
            regions = {}
            for s in self.sections:
                regions.update(s["primaryText"].get("regions") or {})
            return {**base, "regions": regions}
        return {**base, "words": merged_words(s["primaryText"] for s in self.sections)}


@dataclass
class Tree:
    decisions: dict = field(default_factory=dict)        # id -> section
    targets: dict = field(default_factory=dict)          # section id -> (decision id, level, branch id)
    by_level: dict = field(default_factory=dict)         # level -> [decision ids]

    @property
    def branching(self):
        return bool(self.decisions)


def build_tree(sheet):
    tree = Tree()
    for s in sheet["sections"]:
        if s.get("type") != "decision":
            continue
        tree.decisions[s["id"]] = s
        tree.by_level.setdefault(s["level"], []).append(s["id"])
        for b in s["branches"]:
            tree.targets[b["target"]] = (s["id"], s["level"], b["id"])
    return tree


def group_sections(sheet, tree=None):
    tree = tree or build_tree(sheet)
    groups, current = [], None
    for s in sheet["sections"]:
        if s.get("type") == "decision":
            groups.append(Group(s["id"], [s], is_decision=True))
            current = None
            continue
        key = primary_key(s["primaryText"])
        if s["id"] not in tree.targets and current is not None and current[0] == key:
            current[1].sections.append(s)
        else:
            g = Group(s["id"], [s])
            current = (key, g)
            groups.append(g)
    return groups


def group_of(sheet, section_id, groups=None):
    for g in groups or group_sections(sheet):
        if any(s["id"] == section_id for s in g.sections):
            return g
    raise KeyError(section_id)


# ─── Branching (engine.pathToVisibleSet / normalizePath) ───

def visible_set(sheet, tree, path):
    visible, prev = [], True
    for s in sheet["sections"]:
        if s.get("type") == "decision" or s.get("titleCard") is False:
            show = prev   # decisions and continuations follow the section before them
        else:
            t = tree.targets.get(s["id"])
            if t is None:
                show = True
            else:
                dec_id, level, branch_id = t
                seg = path[level] if level < len(path) else None
                show = dec_id in visible and seg == branch_id
        if show:
            visible.append(s["id"])
        prev = show
    return visible


def open_decision(sheet, tree, path):
    """The decision the reader faces at depth len(path), or None at a leaf."""
    vis = set(visible_set(sheet, tree, path))
    for dec_id in tree.by_level.get(len(path), []):
        if dec_id in vis:
            return tree.decisions[dec_id]
    return None


def leaf_paths(sheet, tree=None):
    """Every root-to-leaf path. Linear sheets have exactly one: []."""
    tree = tree or build_tree(sheet)
    out = []

    def walk(path):
        dec = open_decision(sheet, tree, path)
        if dec is None:
            out.append(path)
            return
        for b in dec["branches"]:
            walk(path + [b["id"]])

    walk([])
    return out


# ─── Step expectations (engine.activateStep) ───

def active_verse(group, section, step_index):
    """The verse the panel must show while step `step_index` of `section` is active."""
    for st in reversed(section["steps"][:step_index]):
        if st["type"] == "verse-change" and st.get("newVerse"):
            return st["newVerse"]
    return group.primary


def card_expectations(sheet, groups=None):
    """Yield one dict per rendered card, in document order, with what must be true
    while that card is active."""
    groups = groups or group_sections(sheet)
    title = sheet["title"]
    for g in groups:
        if g.is_decision:
            continue
        for section in g.sections:
            for i, st in enumerate(section["steps"]):
                if st["type"] == "verse-change":
                    continue
                verse = active_verse(g, section, i)
                yield {
                    "group": g.dom_id,
                    "section": section["id"],
                    "step": st["id"],
                    "type": st["type"],
                    "highlight": st.get("highlight") or [],
                    "effect": st.get("effect"),
                    "verse_ref": verse["ref"],
                    "verse_words": targets(verse),
                    "verse_mode": verse.get("mode") or "single",
                    "question_label": st.get("questionLabel") or title.get("questionLabel"),
                }


def verses_of_group(group):
    """Every verse pre-rendered into a group's sticky panel."""
    yield group.primary
    for s in group.sections:
        for st in s["steps"]:
            if st["type"] == "verse-change" and st.get("newVerse"):
                yield st["newVerse"]


def verse_sides(verse):
    """(label, he, en, words) for each side of a verse (comparison has two).
    Images have no text sides."""
    if is_image(verse):
        return []
    if verse.get("mode") == "comparison":
        words = verse.get("words") or {}
        left = {k: w for k, w in words.items() if w.get("side", "left") == "left"}
        right = {k: w for k, w in words.items() if w.get("side") == "right"}
        return [
            ("left", verse["left"]["he"], verse["left"]["en"], left),
            ("right", verse["right"]["he"], verse["right"]["en"], right),
        ]
    return [("", verse["he"], verse["en"], verse.get("words") or {})]
