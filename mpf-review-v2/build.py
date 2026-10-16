#!/usr/bin/env python3
"""Rebuild the review surface's level content from the specification.

Regenerates the `<template data-section="unified">` block of index.html (every
tier, level, skill and their comment boxes) and the "Generated from …" footer.
Everything else in index.html (welcome, questions, styles, script) is
hand-written and left alone.

Source: the parsed specification dataset the Krāv PWA generates from this
repo's spec (`lib/progression.generated.ts` in krav-pwa, produced by
`npm run gen:progression`). Re-vendor the spec there first, then run:

    python3 build.py [path/to/progression.generated.ts]

Comment fields keep the page's existing naming so saved answers line up:
note-<SKILL-ID>, note-priv-<Level>, note-restr-<Level>, note-level-<Level>,
where <Level> is the spec level name without spaces (Lead 1 -> Lead1).
"""

import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.html")
DEFAULT_DATASET = os.path.expanduser("~/Developer/krav-pwa/lib/progression.generated.ts")

TIERS = [
    ("flyer", "Flyer Tier", "Managing yourself and your place in a group"),
    ("leader", "Leader Tier", "Leading other flyers, from one follower to the whole jump"),
    ("ee", "Evaluator &amp; Examiner Tier", "Evaluating others and protecting the standards"),
]


def load_dataset(path):
    src = open(path, encoding="utf-8").read()
    marker = "export const LEVELS: Level[] = "
    start = src.index(marker) + len(marker)
    end = src.index("\n];", start) + 2
    levels = json.loads(src[start:end])
    version = re.search(r'export const SPEC_VERSION = "([^"]+)"', src).group(1)
    return levels, version


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def prose(text):
    """Small Markdown subset: paragraphs, bullet and numbered lists, tables."""
    if not text:
        return ""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.rstrip() for l in block.split("\n") if l.strip()]
        if all(re.match(r"^\s*[-*]\s+", l) for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', l))}</li>" for l in lines) + "</ul>")
        elif all(re.match(r"^\s*\d+\.\s+", l) for l in lines):
            out.append("<ol>" + "".join(f"<li>{inline(re.sub(r'^\s*\d+\.\s+', '', l))}</li>" for l in lines) + "</ol>")
        elif all(l.lstrip().startswith("|") for l in lines):
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
            head, body = rows[0], rows[1:]
            out.append(
                "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
                + "</tbody></table>"
            )
        else:
            out.append(f"<p>{inline(' '.join(l.strip() for l in lines))}</p>")
    return "\n".join(out)


def ul(items):
    return "<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>" if items else ""


def groups_html(groups):
    parts = []
    for g in groups:
        if g["heading"]:
            parts.append(f"<p><strong>{inline(g['heading'])}</strong></p>")
        parts.append(ul(g["items"]))
    return "\n".join(parts)


def fb(field, placeholder, prompt=None):
    p = f'<p class="fb-prompt">{prompt}</p>' if prompt else ""
    return (
        f'<div class="fb">{p}<textarea data-field="{field}" rows="2" placeholder="{placeholder}"></textarea>'
        f'<span class="save-state" data-state-for="{field}"></span></div>'
    )


def level_html(level):
    key = level["specName"].replace(" ", "")
    name = level["specName"]
    theme = level["developmentTheme"].split("\n")[0].strip()

    pre = level["prerequisites"]
    note = pre.get("note") or ""
    # A lead-in that only introduces a list ("The following … :") is already
    # carried by that list's subheading.
    note_html = "" if note.strip().endswith(":") else prose(note)
    future = ""
    if pre.get("futureConsiderations"):
        future = "<p><strong>Future consideration (not yet ratified)</strong></p>" + ul(pre["futureConsiderations"])
    overview = (
        "<h4>Intent</h4>" + prose(level["intentStatement"])
        + "<h4>Responsibility</h4>" + prose(level["responsibility"])
        + "<h4>Prerequisites</h4>" + groups_html(pre["groups"]) + note_html + future
        + "<h4>Knowledge</h4><p>The candidate must understand:</p>" + groups_html(level["knowledge"])
    )

    skills = [f'<p class="part-hint">Each skill expands to show what the student is told and what the evaluator assesses. Comment on any of them.</p>']
    current = None
    for s in level["skills"]:
        if s["categoryHeading"] and s["categoryHeading"] != current:
            skills.append(f'<h5 class="cat">{inline(s["categoryHeading"])}</h5>')
        current = s["categoryHeading"]
        skills.append(
            f'<details class="skill-x"><summary class="skill-sum"><span class="skill-sum-req">{inline(s["requirement"])}</span></summary>'
            f'<div class="skill-body"><code class="sid">{s["id"]}</code>'
            f'<div class="layer"><span class="layer-label">Student explanation</span>{prose(s["studentExplanation"])}</div>'
            f'<div class="layer"><span class="layer-label">Evaluator guidance</span>{prose(s["evaluatorGuidance"])}</div>'
            + fb(f'note-{s["id"]}', "A note on this skill…")
            + "</div></details>"
        )

    restr = ul(level["restrictions"]) if level["restrictions"] else prose(level.get("restrictionsNote") or "")

    return (
        f'<details class="lvl-x" data-level="{key}"><summary class="lvl-sum"><span class="lvl-name">{inline(name)}</span>'
        f'<span class="lvl-theme">{inline(theme)}</span></summary><div class="lvl-body">'
        f'<details class="lvl-part part-overview"><summary class="lvl-part-sum">Overview: intent, responsibility, prerequisites, knowledge</summary>'
        f'<div class="lvl-part-body">{overview}</div></details>'
        f'<details class="lvl-part part-skills"><summary class="lvl-part-sum">Skill sign-offs ({len(level["skills"])})</summary>'
        f'<div class="lvl-part-body">{"".join(skills)}</div></details>'
        f'<details class="lvl-part part-priv"><summary class="lvl-part-sum lvl-part-priv">Privileges: the flyer can</summary>'
        f'<div class="lvl-part-body">{ul(level["privileges"])}'
        + fb(f"note-priv-{key}", "A note on these privileges…", "Are these the right privileges to unlock at this level? Too much, too little, missing one?")
        + "</div></details>"
        f'<details class="lvl-part part-restr"><summary class="lvl-part-sum lvl-part-restr">Restrictions: the flyer can not</summary>'
        f'<div class="lvl-part-body">{restr}'
        + fb(f"note-restr-{key}", "A note on these restrictions…", "Are these restrictions right? Any you would remove, or any missing that should be here?")
        + "</div></details>"
        f'<div class="lvl-overall-fb"><h5 class="cat">Your feedback on {inline(name)}</h5>'
        + fb(
            f"note-level-{key}",
            f"Your take on {inline(name)} as a whole…",
            f"Feedback on {inline(name)} overall: is this level right? Wrong responsibility, missing something, out of place? Anything about the level goes here.",
        )
        + "</div></div></details>"
    )


def unified_html(levels):
    tiers = []
    for tier, title, sub in TIERS:
        body = "".join(level_html(l) for l in levels if l["tier"] == tier)
        tiers.append(
            f'<details class="tier-x" data-tier="{tier}"><summary class="tier-sum"><span class="tier-name">{title}</span>'
            f'<span class="tier-subm">{sub}</span></summary><div class="tier-body">{body}'
            f'<div class="tier-questions" data-tierq="{tier}"></div></div></details>'
        )
    return (
        '<template data-section="unified"><section id="unified-wrap"><div class="unified">'
        + "".join(tiers)
        + "</div></section></template>"
    )


def main():
    dataset = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DATASET
    levels, version = load_dataset(dataset)
    page = open(INDEX, encoding="utf-8").read()

    start = page.index('<template data-section="unified">')
    end = page.index("</template>", start) + len("</template>")
    page = page[:start] + unified_html(levels) + page[end:]

    page, n = re.subn(
        r"Generated from Movement Progression Program Specification v[\d.]+\.",
        f"Generated from Movement Progression Program Specification v{version}.",
        page,
    )
    if n != 1:
        sys.exit("build.py: version footer not found")

    open(INDEX, "w", encoding="utf-8").write(page)
    skills = sum(len(l["skills"]) for l in levels)
    print(f"index.html: {len(levels)} levels, {skills} skills, spec v{version}")


if __name__ == "__main__":
    main()
