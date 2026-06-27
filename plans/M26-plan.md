# M26 Plan — Runbooks & On-Call

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M26 | **Track:** 7 (Incident & Reliability) | **Color:** #9486cf iris
- **Title:** Runbooks & On-Call
- **Subtitle:** Turning incident response from improvisation into practiced procedure
- **Icon:** 📕

## Everyday Analogy: Fire Department Protocols
Firefighters don't debate tactics inside a burning building — they execute drilled protocols where every role and step is predefined, so they act fast under stress. A runbook is that protocol for an LLM incident: when the auto-deny rate spikes at 2am, the on-call engineer follows a checklist (detect, decide, act, verify, communicate) instead of improvising while members are harmed.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Anatomy of a good runbook: detect, decide, act, verify, communicate
2. On-call rotation, escalation paths, and severity-based response
3. Runbooks for the LLM failure families
4. Keeping runbooks alive: rehearse and update

## Sections Outline
- **content** — *Anatomy of a Runbook*: A good runbook is a checklist for one failure mode with five beats: Detect (which alert, what it means), Decide (severity, rollback-or-mitigate criteria), Act (…
- **content** — *On-Call and Living Runbooks*: Runbooks need an on-call rotation with clear escalation (engineer → senior → medical director for clinical-impact calls) and severity-based response (Sev-1 page…
- **code** (python) — *A Runbook as Executable Checklist*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: It's 2am and the PA auto-deny rate has doubled. Your team has dashboards but no runbooks. What's the core operational gap, and the fix?
    - Correct: Without a runbook, response depends on the awake engineer improvising under stress; codify detect/decide/act/verify/communicate per failure mode and rehearse it
    - Explanation: Dashboards show the fire; they don't tell you how to fight it. A runbook turns response into a drilled checklist — confirm, decide severity, revert, verify recovery, remediate state, communicate — so…
- **antipattern** — *What Goes Wrong*:
    - Improvised response: with no runbook, recovery time and correctness depend entirely on who's awake, and member harm scales with their hesitation.
    - Stale runbook: it points to a renamed flag and a deleted dashboard, so following it during a Sev-1 wastes the minutes that matter most.

## SVG Diagram Plan
A `renderVisual("M26")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#9486cf`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M29 On-Call
- `sdlc` → AI-SDLC — Incident

## Lab Briefs
- **Understand It:** Take a past incident's timeline and write the runbook that would have shortened it; identify which step was improvised and cost the most time.
- **Build It with AI:** Author executable runbooks for the top LLM failure families (auto-deny spike, schema-invalid surge, injection detection) with escalation paths, and link each to its taxonomy entry.

## LLMOps Takeaway
Codify incident response as rehearsed, executable runbooks — detect, decide, act, verify, communicate — so a 2am responder follows a drilled protocol instead of improvising while members are harmed.

## Anti-Patterns
- No runbooks, so every incident depends on whoever happens to be awake remembering the right steps.
- Runbooks written once and never rehearsed — they reference a dashboard that moved and a flag that was renamed.

## Continuity Notes
Builds on the prior track-7 / sequence module **M25**. Followed by **M27**, which carries these concepts forward.
