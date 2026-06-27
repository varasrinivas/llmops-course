# M09 Plan — Canary & Progressive Deployment

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M09 | **Track:** 3 (Deployment & Release) | **Color:** #6f93c9 denim
- **Title:** Canary & Progressive Deployment
- **Subtitle:** Releasing to 1% before 100% — and knowing when to stop
- **Icon:** 🐤

## Everyday Analogy: Testing a New Recipe on a Few Tables
A smart restaurant doesn't change the signature dish for every table at once. It sends the new version to a few tables, watches the plates come back, and only rolls it out kitchen-wide if the reactions are good. Canary deployment is that: prompt v8 goes to 1% of PA traffic, you watch the determinations and overrides, and you expand only if the signal holds.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Why big-bang LLM releases are uniquely dangerous
2. Canary cohorts and automated promotion criteria
3. Shadow deployment: running the new version with no live impact
4. Guardrail metrics that auto-halt a rollout

## Sections Outline
- **content** — *Shadow First, Then Canary*: Before a single member is affected, run the new bundle in shadow: it processes real PA requests in parallel with production, its outputs logged but not acted on…
- **content** — *Guardrail Metrics That Halt Automatically*: A canary is only safe if it can stop itself. Define guardrail metrics with thresholds that trigger an automatic rollback: auto-deny rate rises above baseline +…
- **code** (python) — *Canary With Auto-Halt*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: You're rolling out prompt v8 to a PA pipeline serving thousands of determinations per hour. Why is an automated guardrail-based halt essential, rather than watching a dashboard?
    - Correct: At that volume a regression affects thousands before a human reacts; only an automated threshold can halt fast enough to limit harm
    - Explanation: Throughput is the enemy of manual response. A wrong-denial regression compounds every minute, and human reaction time is measured in minutes-to-hours. Guardrail metrics with automatic rollback bound t…
- **antipattern** — *What Goes Wrong*:
    - Big-bang release: prompt v8 ships to 100%, a deny-recall regression hits every member at once, and rollback is a fire drill.
    - Manual canary watch: the guardrail breach is noticed an hour later; thousands of wrong determinations already issued and now need re-adjudication.

## SVG Diagram Plan
A `renderVisual("M09")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#6f93c9`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M11 Rollout
- `sdlc` → AI-SDLC — Release Mgmt

## Lab Briefs
- **Understand It:** Given a rollout that caused an incident, identify what canary stage and which guardrail metric would have caught it, and how many determinations the blast radius would have been reduced to.
- **Build It with AI:** Implement a progressive rollout controller with shadow/canary/expand/full stages and automated guardrail thresholds that trigger rollback on breach.

## LLMOps Takeaway
Release LLM changes progressively — shadow, then canary, then expand — with guardrail metrics that automatically halt and roll back, because at production volume humans react far too slowly.

## Anti-Patterns
- Big-bang 100% release of a prompt change — a regression hits every member simultaneously.
- Canary with no automated halt — by the time a human notices, the bad version already served thousands of determinations.

## Continuity Notes
Builds on the prior track-3 / sequence module **M08**. Followed by **M10**, which carries these concepts forward.
