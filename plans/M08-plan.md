# M08 Plan — CI/CD for LLM Applications

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M08 | **Track:** 3 (Deployment & Release) | **Color:** #6f93c9 denim
- **Title:** CI/CD for LLM Applications
- **Subtitle:** An automated pipeline that won't let an unevaluated prompt reach production
- **Icon:** 🔁

## Everyday Analogy: Pharmaceutical Production Lines
A drug isn't shipped because someone 'feels good' about the batch — it passes assay gates, contamination checks, and potency tests, each automated, each able to halt the line. LLM CI/CD is the same line: a prompt change passes the eval gate, the red-team gate, and the cost gate before it can reach patients. No green checks, no release.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. What 'the artifact' is when there's no compiled binary
2. Eval gates, red-team gates, and cost gates in the pipeline
3. Promoting prompt+model+policy as one versioned bundle
4. Reproducible deployments via the determination fingerprint

## Sections Outline
- **content** — *What Are You Even Deploying?*: There's no compiled binary. The deployable artifact is a bundle: the prompt version, the pinned model snapshot, the retrieved policy snapshot, and config (tempe…
- **content** — *Gates That Can Halt the Line*: The pipeline enforces three blocking gates: the eval gate (agreement and per-class recall meet thresholds, M04/M06), the red-team gate (attack-success-rate is z…
- **code** (yaml) — *A Pipeline Definition*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: During an appeal, a regulator asks you to reproduce exactly how a denial was reached 5 months ago. Your CI/CD design should have ensured what?
    - Correct: Every determination is tied to a versioned bundle (prompt + pinned model snapshot + policy snapshot) that can be re-run identically
    - Explanation: Defensibility requires reproducibility. If each determination records the exact fingerprinted bundle, you can replay the decision under audit. Console hotfixes and 'latest' models make this impossible…
- **antipattern** — *What Goes Wrong*:
    - Console hotfix: an un-versioned prompt edit fixes today's complaint and becomes an unreproducible determination you can't defend on appeal.
    - Advisory gates: a failing eval is overridden to hit a date; the regression reaches members and the gate's existence provided false comfort.

## SVG Diagram Plan
A `renderVisual("M08")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#6f93c9`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `sdlc` → AI-SDLC — CI/CD
- `platform` → Platform M11 Release

## Lab Briefs
- **Understand It:** Trace how a prompt change currently reaches production and list every step with no gate or no version record; rate the audit risk of each.
- **Build It with AI:** Author a CI pipeline that runs eval, red-team, and cost gates as blocking checks and promotes a fingerprinted prompt+model+policy bundle as the deployable artifact.

## LLMOps Takeaway
LLM CI/CD promotes prompt+model+policy as one fingerprinted bundle through blocking eval, red-team, and cost gates — so every production determination is both quality-gated and reproducible.

## Anti-Patterns
- Editing the production prompt in a console with no version, no eval, no rollback — a 'hotfix' nobody can reproduce.
- Eval results that are advisory, not blocking — so a failing gate gets waved through under deadline.

## Continuity Notes
Builds on the prior track-3 / sequence module **M07**. Followed by **M09**, which carries these concepts forward.
