# M18 Plan — The Data Flywheel

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M18 | **Track:** 5 (Data & Feedback Loops) | **Color:** #8fc7a8 sage
- **Title:** The Data Flywheel
- **Subtitle:** Turning production feedback into compounding quality improvement
- **Icon:** 🔁

## Everyday Analogy: Amazon's Virtuous Cycle
More customers bring more sellers, which brings more selection and lower prices, which brings more customers — a flywheel where each turn makes the next easier. A well-run LLM app builds the same momentum: every determination produces feedback, feedback improves the system, a better system earns more usage and more feedback. The danger is spinning the wheel backwards — amplifying your own errors.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The flywheel: serve → capture → curate → improve → serve
2. What 'improve' means without retraining: prompts, retrieval, few-shots, routing
3. Measuring flywheel velocity and avoiding feedback-loop bias
4. Guarding against drift-amplifying loops

## Sections Outline
- **content** — *The Loop That Compounds*: The flywheel is: serve determinations → capture reviewer corrections (M16) → curate them into datasets (M17) → improve the system → serve better, capturing more…
- **content** — *Don't Spin It Backwards*: The flywheel can amplify errors. If you 'improve' using the model's own unreviewed outputs as truth, you create a feedback-loop bias that entrenches mistakes wi…
- **code** (python) — *One Turn of the Flywheel*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: To accelerate improvement, an engineer proposes auto-adding every determination the model made with high confidence to the training/few-shot pool. Why is this risky?
    - Correct: It creates a self-reinforcing loop: the model's own (possibly wrong) outputs become 'truth', entrenching errors with growing confidence
    - Explanation: Feeding the model its own unverified outputs spins the flywheel backwards — confident mistakes get canonized and compound. Only human-corrected, adjudicated data should drive 'improve', and every chan…
- **antipattern** — *What Goes Wrong*:
    - Self-training loop: unverified model outputs feed back as labels, errors entrench, and confidence rises as accuracy falls.
    - Dead flywheel: feedback is captured and curated but never wired to 'improve' or release, so quality stays flat despite mounting data.

## SVG Diagram Plan
A `renderVisual("M18")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#8fc7a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `agent` → Agent M15 HITL
- `platform` → Platform M10 Eval

## Lab Briefs
- **Understand It:** Map your current serve→capture→curate→improve loop and find the broken link (usually capture-with-no-improve or improve-with-no-validation); estimate flywheel velocity.
- **Build It with AI:** Implement a flywheel job that promotes verified corrections into the gold set, builds an improved bundle via retrieval/few-shot/routing (no retraining), and gates it through regression before release.

## LLMOps Takeaway
A data flywheel compounds quality only when human-verified feedback drives improvement that clears the regression gate — feed it the model's own guesses and it compounds your errors instead.

## Anti-Patterns
- A feedback loop that only sees its own outputs — the model trains on its mistakes and confidently entrenches them.
- Capturing feedback that never reaches 'improve' — a flywheel with no axle, spinning effort with no momentum.

## Continuity Notes
Builds on the prior track-5 / sequence module **M17**. Followed by **M19**, which carries these concepts forward.
