# -*- coding: utf-8 -*-
"""
generate_plans.py — Backfill plans/MXX-plan.md from the module data.
Follows the structure defined in .claude/commands/plan-module.md.
Skips M00 (hand-authored plan already exists). Run:
  python scripts/generate_plans.py
"""
import os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules_t1_4 import MODS as M1
from modules_t5_8 import MODS as M2
MODS = M1 + M2

TRACKS = {
 1:("Foundations","#4caf82 pine"), 2:("Eval & Testing","#ec8a6e salmon"),
 3:("Deployment & Release","#6f93c9 denim"), 4:("Monitoring & Observability","#e3a52c maize"),
 5:("Data & Feedback Loops","#8fc7a8 sage"), 6:("Model Lifecycle","#cf6f5f brick"),
 7:("Incident & Reliability","#9486cf iris"), 8:("Governance & Optimization","#3f95a8 teal"),
}

def strip_html(s):
    import re
    s = re.sub(r"<[^>]+>", "", s)
    return s.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")

def section_line(sec):
    t = sec["type"]
    if t == "content":
        return f"- **content** — *{sec['title']}*: {strip_html(sec['body'])[:160].strip()}…"
    if t == "code":
        return f"- **code** ({sec.get('language','')}) — *{sec['title']}*: operational tooling snippet in the PA domain."
    if t == "quiz":
        correct = sec["options"][sec["correct"]]
        return (f"- **quiz** (WHY/WHEN) — Q: {sec['question']}\n"
                f"    - Correct: {correct}\n"
                f"    - Explanation: {sec['explanation'][:200].strip()}…")
    if t == "antipattern":
        items = "\n".join(f"    - {strip_html(i)}" for i in sec["items"])
        return f"- **antipattern** — *{sec['title']}*:\n{items}"
    if t == "analogy":
        return f"- **analogy** — *{sec['title']}*: {strip_html(sec['body'])[:160]}…"
    return f"- **{t}**"

def crosslink_block(m):
    if not m.get("crosslinks"):
        return "- None"
    return "\n".join(f"- `{c['type']}` → {c['label']}" for c in m["crosslinks"])

def build_plan(m, idx):
    tname, tcolor = TRACKS[m["track"]]
    prev = MODS[idx-1]["id"] if idx > 0 else None
    nxt  = MODS[idx+1]["id"] if idx < len(MODS)-1 else None
    topics = "\n".join(f"{i+1}. {t}" for i, t in enumerate(m["topics"]))
    sections = "\n".join(section_line(s) for s in m["sections"])
    aps = "\n".join(f"- {strip_html(a)}" for a in m.get("antiPatterns", []))
    cont = []
    if prev: cont.append(f"Builds on the prior track-{m['track']} / sequence module **{prev}**.")
    else:    cont.append("Opens its track.")
    if nxt:  cont.append(f"Followed by **{nxt}**, which carries these concepts forward.")
    else:    cont.append("Final module — synthesizes everything before it.")
    return f"""# {m['id']} Plan — {m['title']}

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** {m['id']} | **Track:** {m['track']} ({tname}) | **Color:** {tcolor}
- **Title:** {m['title']}
- **Subtitle:** {m['subtitle']}
- **Icon:** {m['icon']}

## Everyday Analogy: {m['analogy']['title']}
{m['analogy']['text']}

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics ({len(m['topics'])})
{topics}

## Sections Outline
{sections}

## SVG Diagram Plan
A `renderVisual("{m['id']}")` case renders a dark-theme diagram (surface `#1c1f26`, track color `{tcolor.split()[0]}`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
{crosslink_block(m)}

## Lab Briefs
- **Understand It:** {m['labUnderstand']}
- **Build It with AI:** {m['labBuild']}

## LLMOps Takeaway
{m['takeaway']}

## Anti-Patterns
{aps}

## Continuity Notes
{' '.join(cont)}
"""

def main():
    written = 0
    for idx, m in enumerate(MODS):
        path = os.path.join(HERE, "plans", f"{m['id']}-plan.md")
        if m["id"] == "M00" and os.path.exists(path):
            continue  # keep the hand-authored M00 plan
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_plan(m, idx))
        written += 1
    print(f"Wrote {written} plan files to plans/")

if __name__ == "__main__":
    main()
