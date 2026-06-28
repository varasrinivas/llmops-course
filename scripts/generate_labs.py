# -*- coding: utf-8 -*-
"""
generate_labs.py — Backfill labs/MXX-lab-understand.md and labs/MXX-lab-build.md
from the module data, following .claude/commands/build-lab.md.
Domain anchor: Prior Authorization (PA) Determination Pipeline.
Skips M00 (hand-authored labs already exist). Run:
  python scripts/generate_labs.py
"""
import os, sys, re
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules_t1_4 import MODS as M1
from modules_t5_8 import MODS as M2
MODS = M1 + M2

def strip_html(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return s.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&").strip()

def first(m, t):
    return next((s for s in m["sections"] if s["type"] == t), None)

def understand(m, nxt):
    topics = m["topics"]
    analogy = m["analogy"]
    quiz = first(m, "quiz")
    aps = m.get("antiPatterns", [])
    # build up to 3 observation/analysis steps from the topics
    verbs = ["Observe", "Analyze", "Quantify", "Map", "Compare"]
    steps = []
    for i, tp in enumerate(topics[:3]):
        v = verbs[i % len(verbs)]
        steps.append(
f"""### Step {i+1}: {v} — {tp}
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "{tp.split(' — ')[0].lower()}" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.""")
    watch = ("\n".join(f"  - {strip_html(a)}" for a in aps[:2])) or "  - (see the module's anti-patterns)"
    refq1 = strip_html(quiz["question"]) if quiz else "Why does the failure mode in this module stay invisible until it is expensive?"
    return f"""# {m['id']} Lab: Understand It — {m['title']}

## Objective
{strip_html(m['labUnderstand'])}

## Prerequisites
- Completed module {m['id']} content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *{analogy['title']}* — you will map your findings back to it.

## Exercise (25 min)

{chr(10).join(steps)}

### Step {len(steps)+1}: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
{watch}
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. {refq1}
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *{analogy['title']}* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
{strip_html(m['takeaway'])}
"""

def build(m, nxt):
    code = first(m, "code")
    lang = code.get("language", "python") if code else "python"
    starter = code["code"] if code else "# (no reference snippet for this module)"
    aps = m.get("antiPatterns", [])
    edge = ("\n".join(f"- {strip_html(a)}" for a in aps[:2])) or "- Handle the failure modes from the module's anti-patterns."
    nxt_line = (f"This prepares you for **{nxt['id']}: {nxt['title']}**, which builds on what you constructed here."
                if nxt else "This is the capstone — it ties together everything you built across the eight tracks.")
    obj = strip_html(m['labBuild'])
    scaffold_prompt = (f"Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: "
                       f"{obj} Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), "
                       f"pin model 'claude-sonnet-4-6', and return runnable, commented code.")
    return f"""# {m['id']} Lab: Build It with AI — {m['title']}

## Objective
{obj}

## Prerequisites
- Completed the {m['id']} "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```{lang}
{starter}
```

Use Claude to adapt it to your environment:
> "{scaffold_prompt}"

- **Expected output:** the scaffold runs end-to-end against one sample PA request without errors.

### Step 2: Extend it to real PA cases
- Wire the scaffold to a small batch of determinations (pull 10–20 from the sandbox, spanning approve / deny / pend and at least two service types).
- Iterate with Claude on anything that breaks; ask it to explain each change.
- **Expected output:** the tool produces correct, structured results across the batch.

### Step 3: Test against the domain
- Add explicit checks tied to this module's goal (e.g., assertions, thresholds, or metrics) so a regression would fail loudly.
- Include at least one hard case (a borderline determination that drives appeals).
- **Expected output:** tests pass on good input and fail clearly on a deliberately broken case.

### Step 4: Refine for the failure modes
Harden against the anti-patterns this module calls out:
{edge}
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **{m['title'].lower()}** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
{nxt_line}
"""

def main():
    written = 0
    for i, m in enumerate(MODS):
        if m["id"] == "M00":
            continue  # keep hand-authored M00 labs
        nxt = MODS[i+1] if i < len(MODS)-1 else None
        with open(os.path.join(HERE, "labs", f"{m['id']}-lab-understand.md"), "w", encoding="utf-8") as f:
            f.write(understand(m, nxt))
        with open(os.path.join(HERE, "labs", f"{m['id']}-lab-build.md"), "w", encoding="utf-8") as f:
            f.write(build(m, nxt))
        written += 2
    print(f"Wrote {written} lab files to labs/")

if __name__ == "__main__":
    main()
