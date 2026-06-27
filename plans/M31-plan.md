# M31 Plan — Capstone — Operating the PA Pipeline

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M31 | **Track:** 8 (Governance & Optimization) | **Color:** #3f95a8 teal
- **Title:** Capstone — Operating the PA Pipeline
- **Subtitle:** Run the full LLMOps lifecycle on the prior-authorization pipeline for a week
- **Icon:** 🏁

## Everyday Analogy: Running the Restaurant for a Week
You've learned to cook, inspect, plate, and manage suppliers separately. The capstone is opening the doors and running the whole restaurant for a week: the lunch rush (load), a bad-ingredient scare (drift), a walk-in health inspector (audit), a supplier going out of business (model deprecation), and a kitchen fire (incident) — all while every plate still has to be good, on time, and within budget. This is LLMOps as a single operating discipline.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Wiring all eight tracks into one operating system
2. Handling a simulated week: a drift event, an incident, a migration, an audit
3. Balancing quality, cost, reliability, and compliance under pressure
4. Producing the operational evidence that the pipeline is trustworthy

## Sections Outline
- **content** — *From Eight Tracks to One Operating System*: Each track gave you a capability; the capstone makes them one living system around the prior-authorization pipeline. The CI/CD gates (T3) run the eval suite (T2…
- **content** — *The Simulated Week*: The capstone runs a compressed week against the PA pipeline. Monday: a prompt improvement ships through canary. Tuesday: a provider repoints a snapshot and drif…
- **code** (python) — *The Operating Loop, Wired End-to-End*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Mid-capstone, an auto-deny spike hits during an active model migration, and a compliance audit request lands the same hour. What does this scenario test that single-track practice does not?
    - Correct: Your ability to operate the seams between tracks under pressure — rolling back without derailing the migration, remediating state, and still producing reproducible audit evidence — balancing quality, reliability, and compliance at once
    - Explanation: Real operations is concurrent and interconnected. The capstone's value is in the seams: an incident response (T7) that respects an in-flight migration (T6), preserves the audit trail (T8), and re-adju…
- **antipattern** — *What Goes Wrong*:
    - Siloed operation: the tracks are run as independent checklists, and the first multi-track incident exposes the unhandled seams between rollback, migration, and audit.
    - Single-axis optimization: cost is squeezed until quality or compliance quietly breaches, proving the operator never internalized that LLMOps is balancing all dimensions at once.

## SVG Diagram Plan
A `renderVisual("M31")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#3f95a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE Capstone
- `agent` → Agent Capstone
- `platform` → Platform Capstone
- `sdlc` → AI-SDLC Capstone

## Lab Briefs
- **Understand It:** Walk through the simulated week and, at each event, identify which tracks interact and where the seams between them create risk; produce an operating-readiness assessment.
- **Build It with AI:** Wire the full PA pipeline operating loop end-to-end (monitor → drift → flywheel → migration → incident → compliance), run the simulated week, and produce the operational evidence report demonstrating the pipeline is trustworthy.

## LLMOps Takeaway
LLMOps mastery is operating all eight tracks as one system under real pressure — balancing quality, cost, reliability, and compliance simultaneously — so the pipeline stays trustworthy through drift, incidents, migrations, and audits alike.

## Anti-Patterns
- Treating the tracks as separate checklists — under a real incident the seams between eval, rollback, and compliance are where things break.
- Optimizing one dimension (cost) until another (quality or compliance) silently fails — operations is balancing all of them at once.

## Continuity Notes
Builds on the prior track-8 / sequence module **M30**. Final module — synthesizes everything before it.
