# M22 Plan — Multi-Model Strategies

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M22 | **Track:** 6 (Model Lifecycle) | **Color:** #cf6f5f brick
- **Title:** Multi-Model Strategies
- **Subtitle:** Routing each determination to the right model for its complexity and stakes
- **Icon:** 🔀

## Everyday Analogy: A Law Firm Staffing by Complexity
A law firm doesn't put a senior partner on a routine NDA — paralegals handle simple matters and partners take the bet-the-company cases. Multi-model routing staffs your PA determinations the same way: a fast cheap model clears the obvious approvals, while complex, high-cost, or low-confidence cases escalate to a stronger (pricier) model or a human. You match the resource to the stakes.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Routing by complexity, stakes, and confidence
2. Cascade/fallback patterns: cheap-first, escalate on low confidence
3. Cost-quality trade-offs and the routing budget
4. Operating multiple models without operational sprawl

## Sections Outline
- **content** — *Route by Complexity, Stakes, and Confidence*: Not every PA request needs your strongest model. A routine in-network imaging approval is a paralegal task; a rare gene therapy denial is bet-the-company. A rou…
- **content** — *Cascades and the Routing Budget*: A common pattern is the cascade: try the cheap model first; if its confidence is below threshold (or stakes are high), escalate to a stronger model, then to a h…
- **code** (python) — *A Cost-Aware Cascade Router*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: To cut cost, a team routes every PA determination through one premium model. What's the smarter design, and what makes it safe?
    - Correct: A cascade: cheap model for the obvious bulk, escalate low-confidence/high-stakes cases to a stronger model or human — safe only if the confidence signal is validated and thresholds are tuned on the gold set
    - Explanation: Premium-everything overpays on routine approvals. A confidence-based cascade reserves the expensive model and humans for cases that warrant them, cutting cost while protecting quality — but it only wo…
- **antipattern** — *What Goes Wrong*:
    - Premium-everything: budget is exhausted paying partner rates for paralegal work, and finance kills the project before it scales.
    - Untuned routing: an unvalidated confidence signal sends genuinely hard denials to the cheap model, so quality collapses precisely on the high-stakes cases.

## SVG Diagram Plan
A `renderVisual("M22")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#cf6f5f`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M05 Routing
- `platform` → Platform M16 Cost

## Lab Briefs
- **Understand It:** Analyze a single-model pipeline's cost and per-slice quality; estimate the savings and risks of introducing a cheap-first cascade.
- **Build It with AI:** Implement a cascade router with confidence thresholds and stakes overrides, then tune the thresholds on the gold set to meet both a cost ceiling and a deny-recall floor.

## LLMOps Takeaway
Route each determination to the right model by complexity, stakes, and validated confidence — a cascade that staffs cheap models on routine cases and reserves strong models and humans for where the stakes justify the cost.

## Anti-Patterns
- One expensive model for every determination — you pay partner rates to review NDAs and blow the budget.
- Routing with no confidence signal — hard cases silently get the cheap model and quality craters on exactly the cases that matter.

## Continuity Notes
Builds on the prior track-6 / sequence module **M21**. Followed by **M23**, which carries these concepts forward.
