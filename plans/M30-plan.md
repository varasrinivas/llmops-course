# M30 Plan — Knowledge Management

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M30 | **Track:** 8 (Governance & Optimization) | **Color:** #3f95a8 teal
- **Title:** Knowledge Management
- **Subtitle:** Capturing operational learning so the team improves instead of repeating mistakes
- **Icon:** 📚

## Everyday Analogy: Hospital Morbidity & Mortality Conferences
Hospitals hold regular M&M conferences where clinicians review adverse outcomes openly and blamelessly, extracting lessons that become protocol changes — so the same mistake doesn't recur ward after ward. Knowledge management is the M&M for your LLM operation: every incident, override pattern, and migration becomes a durable, shared lesson, so the team's competence compounds instead of resetting with each departure.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Blameless postmortems and the institutional memory they build
2. From incident to durable artifact: runbook, test, guardrail
3. Decision records for prompts, models, and policy choices
4. Onboarding and the cost of tribal knowledge

## Sections Outline
- **content** — *Blameless Postmortems Build Memory*: When a PA incident happens, the goal isn't to find who to blame — it's to find what in the system allowed it and fix that. Blameless postmortems make this safe:…
- **content** — *Decision Records and Defeating Tribal Knowledge*: The other half of knowledge management is capturing why, not just what. Decision records document why you chose this prompt structure, pinned that model, or set…
- **code** (python) — *From Postmortem to Artifacts*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: After a serious PA incident, the team holds a postmortem, writes a doc, and files it. Six months later a nearly identical incident recurs. What did knowledge management miss?
    - Correct: Lessons weren't converted into durable artifacts (alert, guardrail, regression test, runbook update) and decision records — a filed doc isn't a system change
    - Explanation: A document that's read once and filed doesn't change the system. The recurrence shows the lesson never became an alert, a guardrail, a regression test, or a runbook step — the artifacts that actually…
- **antipattern** — *What Goes Wrong*:
    - Postmortem theater: a doc is written and filed but no alert, test, or guardrail changes, so the same incident recurs months later.
    - Tribal knowledge: the reasoning behind a model pin or routing threshold lives in one engineer's head; they leave, a successor reverts it, and a solved problem returns.

## SVG Diagram Plan
A `renderVisual("M30")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#3f95a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `sdlc` → AI-SDLC — Knowledge
- `platform` → Platform M29 Postmortems

## Lab Briefs
- **Understand It:** Review a past postmortem and check whether it produced durable artifacts (alert, test, guardrail, runbook) or just a filed document; identify what would have prevented a recurrence.
- **Build It with AI:** Establish a postmortem template that mandates durable artifacts and a decision record, then run it on a real (or simulated) incident and produce the linked alert, regression test, and runbook update.

## LLMOps Takeaway
Convert every incident and decision into durable artifacts and searchable records through blameless postmortems — so the team's competence compounds and the same mistake can't recur after someone leaves.

## Anti-Patterns
- Blameful postmortems — people hide mistakes, the real causes never surface, and the same incident recurs.
- Lessons that live in someone's head or a Slack thread — they vanish when that person leaves or the thread scrolls away.

## Continuity Notes
Builds on the prior track-8 / sequence module **M29**. Followed by **M31**, which carries these concepts forward.
