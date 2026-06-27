# M05 Plan — LLM-as-Judge

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M05 | **Track:** 2 (Eval & Testing) | **Color:** #ec8a6e salmon
- **Title:** LLM-as-Judge
- **Subtitle:** Using a model to grade model output — reliably, at scale, without fooling yourself
- **Icon:** 🧑‍⚖️

## Everyday Analogy: Restaurant Critics and the Michelin Guide
You can't taste every dish in every restaurant, so a guide trains critics against a shared rubric and cross-checks them so one critic's quirks don't define a star. LLM-as-judge is the same: a model critic scales grading you could never do by hand, but only if it follows a sharp rubric and is calibrated against human graders — otherwise you've automated a biased palate.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. When a judge model beats string matching
2. Writing rubrics that produce consistent scores
3. Known biases: position, verbosity, self-preference — and how to control them
4. Validating the judge against human labels before trusting it

## Sections Outline
- **content** — *Why and When to Use a Judge*: For a PA determination, the decision (approve/deny/pend) can be exact-matched against gold. But the rationale — 'does this justification correctly apply the ste…
- **content** — *Control the Biases, Then Validate*: Judges have known failure modes: position bias (favoring the first option in a pairwise compare), verbosity bias (longer = better), and self-preference (a model…
- **code** (python) — *A Rubric Judge With Validation*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: You want to use an LLM judge to grade PA rationales at scale. What must you do BEFORE relying on its scores in your release gate?
    - Correct: Validate the judge against a human-labeled sample and confirm acceptable agreement (e.g., Cohen's kappa)
    - Explanation: A judge is itself a model that can be wrong or biased. Before it gates releases you must show it agrees with human experts on a calibration sample. Skipping validation means you've scaled an unmeasure…
- **antipattern** — *What Goes Wrong*:
    - Unvalidated judge in the release gate: it quietly rewards verbose, confident rationales and your real quality slips while scores stay green.
    - Self-judging: the generator grades its own work, agreement looks great in testing, and production quality is worse than the numbers claim.

## SVG Diagram Plan
A `renderVisual("M05")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#ec8a6e`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M10 Prompt Eval
- `ce` → CE — Rubric Design

## Lab Briefs
- **Understand It:** Take 30 PA rationales scored by a naive judge and by a human; measure agreement, then identify whether verbosity or position bias explains the disagreements.
- **Build It with AI:** Write a rubric-based judge for PA rationales, add order randomization and a cross-family judge model, and build a calibration harness that blocks use until kappa exceeds a threshold.

## LLMOps Takeaway
An LLM judge scales semantic grading only after you've controlled its biases and validated it against human labels — an uncalibrated judge automates bias, not quality.

## Anti-Patterns
- Trusting judge scores that were never validated against human labels — you scale a bias instead of catching it.
- Judging with the same model that generated the answer — self-preference inflates the grade.

## Continuity Notes
Builds on the prior track-2 / sequence module **M04**. Followed by **M06**, which carries these concepts forward.
