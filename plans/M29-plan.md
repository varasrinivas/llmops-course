# M29 Plan — Compliance Automation

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M29 | **Track:** 8 (Governance & Optimization) | **Color:** #3f95a8 teal
- **Title:** Compliance Automation
- **Subtitle:** Making regulatory and policy requirements automatic and auditable
- **Icon:** 96️

## Everyday Analogy: Modern Car Safety Systems
Early cars relied on the driver to remember every safe behavior; modern cars build safety in — seatbelt chimes, automatic braking, lane keeping — so compliance with safe practice is continuous and automatic, not a manual checklist. Compliance automation does this for the PA pipeline: instead of trusting people to follow the rules each time, you encode the rules as controls the system enforces and records on every determination.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Encoding policy as automated, testable controls
2. Audit trails: reproducing any determination on demand
3. PHI handling, access control, and data retention
4. Continuous compliance checks vs point-in-time audits

## Sections Outline
- **content** — *Encode the Rules as Controls*: Manual compliance is hope dressed as process. The durable approach is compliance as code: every requirement becomes an automated, testable control. 'Every denia…
- **content** — *Audit Trails and Continuous Evidence*: For a regulated PA workflow, the defining requirement is defensibility: for any determination, you must reproduce exactly what the model saw and why it decided.…
- **code** (python) — *Compliance Controls That Run Every Time*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A regulator audits a denial from 8 months ago and asks you to show exactly how it was decided. Compliance automation should have ensured what?
    - Correct: Every determination is reproducible (fingerprinted bundle + persisted trace + recorded snapshot) and its controls (citation, PHI, TAT) ran and were logged at decision time
    - Explanation: Defensibility requires reproducing the exact decision and proving the controls were satisfied when it was made. That means the fingerprinted bundle, the persisted trace, the recorded snapshot, and log…
- **antipattern** — *What Goes Wrong*:
    - Point-in-time compliance: between annual audits, uncited denials and PHI-in-logs accumulate, surfacing all at once as findings and penalties.
    - Irreproducible decisions: a denial can't be reconstructed because the bundle and trace weren't recorded, leaving no defensible answer to a regulator or appeal.

## SVG Diagram Plan
A `renderVisual("M29")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#3f95a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `sdlc` → AI-SDLC — Compliance
- `platform` → Platform M19 Governance

## Lab Briefs
- **Understand It:** Take three real PA compliance requirements and assess whether each is enforced automatically per determination or relies on manual process; rate the exposure.
- **Build It with AI:** Implement a set of compliance controls (denial citation, no-PHI-in-logs, TAT window, reproducibility) that run on every determination, block or alert on failure, and write continuous audit evidence.

## LLMOps Takeaway
Encode regulatory requirements as automated controls that run on every determination and persist reproducible audit evidence continuously — so compliance is built-in and always-on, not an annual scramble.

## Anti-Patterns
- Compliance as a once-a-year manual audit — between audits, violations accumulate undetected.
- Determinations that can't be reproduced — when a regulator asks 'why was this denied,' you have no defensible answer.

## Continuity Notes
Builds on the prior track-8 / sequence module **M28**. Followed by **M30**, which carries these concepts forward.
