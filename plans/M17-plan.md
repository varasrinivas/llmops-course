# M17 Plan — Data Curation & Annotation

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M17 | **Track:** 5 (Data & Feedback Loops) | **Color:** #8fc7a8 sage
- **Title:** Data Curation & Annotation
- **Subtitle:** Turning raw production logs into a trustworthy labeled dataset
- **Icon:** 🗂️

## Everyday Analogy: A Museum's Acquisition Process
A museum doesn't hang every donated painting. A committee appraises provenance, authenticates, conserves, and catalogs each piece before it enters the collection. Data curation is the same discipline: production logs are donations, and only the authenticated, well-labeled, properly cataloged cases earn a place in your gold and training sets. Curation is selection plus verification, not hoarding.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Curation as selection: what to keep, drop, and prioritize
2. Annotation guidelines and inter-annotator agreement
3. Adjudicating disagreement with expert review
4. Dataset versioning, lineage, and PHI handling

## Sections Outline
- **content** — *Curation Is Selection*: The instinct to 'use all the data' is a trap. Most production PA logs are routine approvals that teach a model nothing; the value concentrates in the hard, cont…
- **content** — *Annotation Quality: Guidelines and Agreement*: A label is only as trustworthy as the process that produced it. You need written annotation guidelines (how to decide approve/deny/pend, how to pick the control…
- **code** (python) — *Curate, Annotate, Version*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A teammate proposes building the new gold set by exporting all 80,000 of last quarter's PA logs and using the original model suggestions as labels. What's wrong?
    - Correct: Using the model's own suggestions as labels bakes in its errors, and unfiltered logs are mostly easy duplicates — you need stratified selection plus independent human annotation
    - Explanation: Labeling with the model's own outputs is circular — it canonizes the model's mistakes as 'truth'. And raw logs over-represent easy approvals. Real curation selects a stratified, deduplicated sample an…
- **antipattern** — *What Goes Wrong*:
    - Unfiltered dump: the dataset is 90% trivial approvals and a few mislabeled records, so eval scores look great and predict nothing.
    - Single-annotator, no guideline: labels reflect one reviewer's idiosyncrasies, agreement is unmeasured, and the gold set can't be defended.

## SVG Diagram Plan
A `renderVisual("M17")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#8fc7a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE — Dataset Design
- `sdlc` → AI-SDLC — Data Governance

## Lab Briefs
- **Understand It:** Audit an existing dataset for selection bias, label provenance, and PHI handling; identify what makes it untrustworthy as a gold set.
- **Build It with AI:** Build a curation pipeline that stratified-samples production logs, runs a two-annotator flow with adjudication, computes inter-annotator agreement, and publishes a versioned, lineage-tagged dataset.

## LLMOps Takeaway
Curate by selecting a stratified sample and annotating it with guideline-driven, multi-annotator, expert-adjudicated review — because a small trustworthy dataset beats a large noisy one for both eval and tuning.

## Anti-Patterns
- Dumping all production logs into 'the dataset' unfiltered — you train and evaluate on noise and mislabels.
- One annotator, no guidelines — labels are inconsistent and no one can trust the gold set.

## Continuity Notes
Builds on the prior track-5 / sequence module **M16**. Followed by **M18**, which carries these concepts forward.
