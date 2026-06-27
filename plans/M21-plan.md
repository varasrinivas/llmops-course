# M21 Plan — Model Migration

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M21 | **Track:** 6 (Model Lifecycle) | **Color:** #cf6f5f brick
- **Title:** Model Migration
- **Subtitle:** Moving to a new model without breaking the behavior you depend on
- **Icon:** 🚌

## Everyday Analogy: Upgrading a City Bus Fleet
A city doesn't scrap every old bus the day new ones arrive. It runs new buses on a few routes, checks they fit the depots and the drivers adapt, fixes the surprises, then expands. Model migration is the same staged swap: the new model may be 'better' in general yet stumble on your PA prompts and policy format, so you shadow it, re-tune, pilot a route, and only then roll out the fleet.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Why a 'better' model can be worse for your specific task
2. Behavioral diffing: shadow the new model against the old
3. Re-tuning prompts for the new model's quirks
4. A staged migration playbook with rollback

## Sections Outline
- **content** — *'Better' Is Task-Relative*: A new model topping a public leaderboard tells you little about your PA task. It may reason better in general yet be worse at following your structured determin…
- **content** — *Diff, Re-Tune, Stage*: Run the new model in shadow against the current one on live traffic and compute a behavioral diff: where do determinations disagree, and on which slices? Expect…
- **code** (python) — *Behavioral Diff in Shadow*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A new model scores higher on public reasoning benchmarks, so a teammate wants to swap it into the PA pipeline this week. What's the disciplined path?
    - Correct: Shadow it against the current model, diff determinations by slice, re-tune the prompt for it, then canary with rollback — gated on your own gold set
    - Explanation: Public benchmarks aren't your task. The new model may regress on your schema or skew denials despite a better leaderboard score. Shadowing reveals the behavioral delta, prompt re-tuning adapts to its…
- **antipattern** — *What Goes Wrong*:
    - Benchmark-driven swap: the 'smarter' model quietly over-approves a high-cost service line, and the win on paper is a loss in claims.
    - No prompt re-tuning: the old prompt's quirk-specific scaffolding misfires on the new model, so a genuinely better model underperforms in your pipeline.

## SVG Diagram Plan
A `renderVisual("M21")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#cf6f5f`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M05 Multi-Provider
- `sdlc` → AI-SDLC — Change Mgmt

## Lab Briefs
- **Understand It:** Compare two models on the same PA gold set and prompt; quantify per-slice disagreement and identify where the 'better' model actually regresses.
- **Build It with AI:** Build a shadow-diff harness that runs a candidate model on live traffic, reports behavioral deltas by slice, and gates migration on a re-tuned-prompt regression run plus canary.

## LLMOps Takeaway
Migrate models as a staged, gated release — shadow, diff, re-tune the prompt, canary — because 'better in general' routinely means 'worse for your specific task' until proven otherwise on your gold set.

## Anti-Patterns
- Swapping models because the new one tops a public benchmark — your task isn't the benchmark, and it regresses on denials.
- Migrating without re-tuning prompts — the old prompt was shaped to the old model's quirks and now underperforms.

## Continuity Notes
Builds on the prior track-6 / sequence module **M20**. Followed by **M22**, which carries these concepts forward.
