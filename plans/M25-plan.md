# M25 Plan — SLOs & SLAs for LLM Applications

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M25 | **Track:** 7 (Incident & Reliability) | **Color:** #9486cf iris
- **Title:** SLOs & SLAs for LLM Applications
- **Subtitle:** Defining and defending reliability targets for quality, latency, and turnaround
- **Icon:** 🎯

## Everyday Analogy: A Delivery Service's Guarantees
A courier promises 'most packages by noon' (an internal target) and contractually guarantees 'by end of day or your money back' (a customer promise). It measures on-time rate to manage both. LLM reliability works the same: SLIs are what you measure, SLOs are your internal targets, and the SLA is the promise with consequences — and for PA, regulators set some of those promises for you.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. SLI vs SLO vs SLA, applied to LLM quality not just uptime
2. Choosing SLIs that capture determination quality and TAT
3. Error budgets that govern release pace
4. Regulatory turnaround as a hard SLA

## Sections Outline
- **content** — *From SLI to SLA, for Quality*: An SLI is a measurement (reviewer agreement, p95 latency, urgent-case TAT). An SLO is your internal target on it (agreement ≥ 90%, urgent TAT < 48h). An SLA is…
- **content** — *Error Budgets and Regulatory SLAs*: An error budget is the allowed shortfall (if the SLO is 90%, the budget is the 10%). Spend it wisely: when the budget is healthy you can ship faster (Track 3);…
- **code** (python) — *SLOs With an Error Budget Gate*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA service reports 99.95% uptime and the team declares its SLOs met. A regulator notes urgent determinations routinely exceed the mandated 72-hour window. What was the SLO design failure?
    - Correct: SLIs/SLOs were set on availability, not on the quality and turnaround that define the service's real obligation — including the regulatory TAT SLA
    - Explanation: Availability is necessary but not the job. The service's real obligations are determination quality and a regulatory turnaround SLA, and those needed their own SLIs and SLOs. Measuring only uptime let…
- **antipattern** — *What Goes Wrong*:
    - Uptime-only SLOs: the dashboard is green while agreement and turnaround quietly violate the service's real (and regulatory) obligations.
    - Unmeasurable SLA: a turnaround promise exists with no SLI behind it, so breaches are invisible until a regulator or lawsuit surfaces them.

## SVG Diagram Plan
A `renderVisual("M25")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#9486cf`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M29 SLOs
- `sdlc` → AI-SDLC — Ops

## Lab Briefs
- **Understand It:** Review a service's current SLOs and identify which real obligations (quality, TAT, compliance) have no SLI; flag any SLA you can't measure.
- **Build It with AI:** Define SLIs/SLOs for the PA pipeline covering agreement, turnaround, and schema validity, implement an error-budget calculation, and wire it to gate release pace.

## LLMOps Takeaway
Define SLOs on determination quality and turnaround — not just uptime — with error budgets that govern release pace and regulatory TAT as a hard SLA you can measure and defend.

## Anti-Patterns
- SLOs only on uptime — you meet 99.9% availability while determination quality and TAT silently fail.
- An SLA you can't measure — you've promised a turnaround you have no SLI to verify or defend.

## Continuity Notes
Builds on the prior track-7 / sequence module **M24**. Followed by **M26**, which carries these concepts forward.
