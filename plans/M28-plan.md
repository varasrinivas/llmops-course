# M28 Plan — Cost Optimization at Scale

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M28 | **Track:** 8 (Governance & Optimization) | **Color:** #3f95a8 teal
- **Title:** Cost Optimization at Scale
- **Subtitle:** Cutting cost per determination without quietly cutting quality
- **Icon:** 💰

## Everyday Analogy: Factory Efficiency Engineering
A factory cuts unit cost by trimming waste — shorter material paths, less scrap, reused heat — not by using cheaper steel that cracks. LLM cost optimization is the same discipline: cache repeated work, compress bloated prompts, and route by complexity to trim the waste, while watching quality so you never 'save' money by shipping determinations that get appealed and cost far more downstream.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The cost drivers: tokens, model tier, retries, and traffic shape
2. Caching, prompt compression, and routing as cost levers
3. Attributing cost per determination, team, and service line
4. Cost guardrails that don't sacrifice quality

## Sections Outline
- **content** — *Know Where the Money Goes*: You can't optimize what you can't attribute. Tag every call's cost by determination, prompt version, service line, and team (via the gateway seam, M03). This re…
- **content** — *Levers That Preserve Quality*: Three levers cut cost without cutting corners. Caching: identical or near-identical PA requests (or stable policy-criteria retrievals) reuse prior results. Prom…
- **code** (python) — *Cost Attribution and Guarded Optimization*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: To hit a budget, a proposal truncates clinical notes to half length and downgrades all PA calls to the cheapest model. Why is this the wrong kind of cost cut?
    - Correct: It cuts quality, not waste: truncation and blanket downgrades lower determination accuracy, and the resulting wrong denials cost far more in appeals and care delays than the tokens saved
    - Explanation: This saves on steel by using steel that cracks. Token and tier cuts that degrade accuracy trade a small, visible saving for large, downstream costs — appeals, re-adjudication, regulatory exposure, and…
- **antipattern** — *What Goes Wrong*:
    - Quality-blind cuts: truncating context and downgrading models lowers accuracy, and the appeal/re-adjudication costs exceed the token savings many times over.
    - Unattributed spend: with no per-determination cost tagging, the team optimizes the wrong thing while one verbose template or retry storm quietly drives the bill.

## SVG Diagram Plan
A `renderVisual("M28")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#3f95a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M16-M19 Cost
- `sdlc` → AI-SDLC — FinOps

## Lab Briefs
- **Understand It:** Attribute a month of PA spend by service line and prompt version; identify the top cost driver and whether it's waste or genuine workload.
- **Build It with AI:** Implement cost attribution at the gateway, apply caching/compression/routing levers, and gate each change through a regression run with a deny-recall floor before keeping it.

## LLMOps Takeaway
Cut cost by trimming waste — caching, compression, routing — under a quality guardrail, because a 'cheap' wrong denial costs far more in appeals and harm than the tokens it saved.

## Anti-Patterns
- Cutting cost by truncating context or downgrading every call — quality drops and appeal costs dwarf the savings.
- No per-determination cost attribution — you can't tell which service line or prompt is burning the budget.

## Continuity Notes
Builds on the prior track-8 / sequence module **M27**. Followed by **M29**, which carries these concepts forward.
