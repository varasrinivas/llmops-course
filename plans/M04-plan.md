# M04 Plan — Evaluation Frameworks

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M04 | **Track:** 2 (Eval & Testing) | **Color:** #ec8a6e salmon
- **Title:** Evaluation Frameworks
- **Subtitle:** How to measure LLM quality systematically instead of by gut feel
- **Icon:** 📏

## Everyday Analogy: Types of School Testing
Schools don't use one test. Multiple-choice exams (golden sets with known answers) scale cheaply. Essays need a rubric and a grader (LLM-as-judge). Oral exams need a human (expert review). Pop quizzes catch drift (online eval). Using only one type fails you: a model can ace multiple choice and still write an incoherent essay. A real eval program mixes types deliberately.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The four eval types: golden sets, reference-free, LLM-as-judge, human review
2. Building a representative gold set for PA determinations
3. Offline vs online evaluation
4. Choosing metrics that match the decision's stakes

## Sections Outline
- **content** — *Four Eval Types, Different Jobs*: Golden sets: inputs with known-correct outputs — for PA, requests with nurse-confirmed determinations. Cheap, repeatable, the backbone of regression testing. Re…
- **content** — *A Gold Set That Actually Represents Production*: A gold set is only as good as its coverage. Sample real PA traffic stratified by service type, by determination (approve/deny/pend), and crucially by difficulty…
- **code** (python) — *A Multi-Metric Eval Run*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA model scores 94% overall agreement on the gold set, and the team wants to ship. What should you check BEFORE approving release?
    - Correct: Per-slice and per-class results — a high average can hide that 'deny' recall on complex cases collapsed to 70%
    - Explanation: A single average is the most dangerous number in eval. The costly errors — wrongly approving or, worse, wrongly denying complex cases — hide inside slices. Always read per-class recall and per-slice t…
- **antipattern** — *What Goes Wrong*:
    - Vanity gold set: all easy approvals, so it reports 99% and certifies nothing about the appeals-driving edge cases.
    - Single-number worship: chasing one average lets the rare, expensive failure mode (wrong denials) degrade invisibly.

## SVG Diagram Plan
A `renderVisual("M04")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#ec8a6e`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE M29 A/B Testing
- `platform` → Platform M10 Prompt Eval

## Lab Briefs
- **Understand It:** Take an existing 'eval' and audit it for coverage: which service types, determinations, and difficulty bands are missing? Estimate what production failures it cannot catch.
- **Build It with AI:** Construct a 50-case stratified PA gold set with clinician-style labels, then build a multi-metric eval run that asserts per-class recall and slices results by service type and difficulty.

## LLMOps Takeaway
A trustworthy eval program mixes golden sets, structural checks, judges, and human review — and always reads per-slice results, because the average hides the failures that matter most.

## Anti-Patterns
- A gold set of 12 hand-picked easy cases — it certifies nothing about the real, messy case mix.
- Optimizing a single average metric while the worst-case denials (the ones that get appealed) quietly get worse.

## Continuity Notes
Builds on the prior track-2 / sequence module **M03**. Followed by **M05**, which carries these concepts forward.
