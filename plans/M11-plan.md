# M11 Plan — Rollback & Recovery

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M11 | **Track:** 3 (Deployment & Release) | **Color:** #6f93c9 denim
- **Title:** Rollback & Recovery
- **Subtitle:** Getting back to known-good in seconds when a release goes wrong
- **Icon:** ↩️

## Everyday Analogy: An Airplane Go-Around
When a landing looks unsafe, pilots don't improvise a fix on final approach — they execute a practiced go-around: full power, climb, circle, try again. Rollback is the LLM app's go-around: the moment a release misbehaves, you don't debug in production, you revert to the last known-good bundle instantly, stabilize, then diagnose on the ground.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Why 'roll forward' is often the wrong instinct under fire
2. Versioned bundles make rollback a config flip, not a redeploy
3. Recovering corrupted state: re-adjudicating bad determinations
4. The rollback runbook and its rehearsal

## Sections Outline
- **content** — *Revert First, Diagnose Later*: Under fire, the instinct to 'just push a quick fix' is usually wrong: you'd be deploying a second unevaluated change while the first is still hurting members. T…
- **content** — *The Part Everyone Forgets: Corrupted State*: Rolling back the code doesn't undo what the bad version did. If prompt v8 wrongly denied 800 PA requests before halt, those denials sit in members' records and…
- **code** (python) — *Rollback With Remediation*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Prompt v8 is wrongly denying valid PA requests in production. What is the correct FIRST action, and what must recovery also address?
    - Correct: Instantly revert to the last known-good bundle, then re-adjudicate the wrong determinations v8 already issued
    - Explanation: Member harm is bounded by recovery time, so you revert immediately to the known-good bundle rather than debugging live. But code rollback doesn't undo the wrong denials already made — recovery must al…
- **antipattern** — *What Goes Wrong*:
    - Roll-forward under fire: a rushed 'fix' stacks a second unevaluated change on a live incident and often makes it worse.
    - Code-only rollback: the version is reverted but 800 wrong denials remain in members' records, surfacing later as appeals and regulatory findings.

## SVG Diagram Plan
A `renderVisual("M11")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#6f93c9`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M29 Reliability
- `sdlc` → AI-SDLC — Incident

## Lab Briefs
- **Understand It:** Take a past incident and measure how long rollback actually took; identify what (versioning, flags, runbook) would have cut it to seconds and whether state was remediated.
- **Build It with AI:** Write and rehearse a rollback runbook that flips to the last known-good bundle and runs a remediation job to re-adjudicate determinations issued by the bad version.

## LLMOps Takeaway
Recovery means reverting to a known-good bundle in seconds and then re-adjudicating the bad determinations it left behind — because rolling back the code doesn't roll back the harm.

## Anti-Patterns
- Trying to 'roll forward' a hotfix during an active incident — you ship a second, unevaluated change on top of the first.
- No plan for the bad determinations already issued — you roll back the code but leave wrong denials in members' records.

## Continuity Notes
Builds on the prior track-3 / sequence module **M10**. Followed by **M12**, which carries these concepts forward.
