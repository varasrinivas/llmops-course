# M10 Plan — Feature Flags & Experimentation

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M10 | **Track:** 3 (Deployment & Release) | **Color:** #6f93c9 denim
- **Title:** Feature Flags & Experimentation
- **Subtitle:** Decoupling 'deployed' from 'released' so you can experiment safely
- **Icon:** 🏳️

## Everyday Analogy: A TV Network's Pilot Season
A network shoots many pilots, airs a few to test audiences, and greenlights only what performs — without re-building the whole studio each time. Feature flags give the PA team the same control room: route 5% of traffic to prompt v8, A/B two retrieval strategies, and kill any variant instantly, all without a redeploy. Deployment ships the code; the flag decides what's actually released.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Flags as the control plane for prompts, models, and routing
2. A/B and online experiments on live determinations
3. Kill switches for instant, deploy-free disablement
4. Statistical rigor: sample size, guardrails, and not peeking

## Sections Outline
- **content** — *Flags Are the Control Plane*: A feature flag decouples deployed (the code is live) from released (the behavior is active). For the PA pipeline, flags select the prompt version, the model, or…
- **content** — *Experiment Without Fooling Yourself*: Flags enable real online experiments — but statistics still apply. Fix the sample size in advance, define the primary metric (e.g., reviewer agreement) and guar…
- **code** (python) — *Flagged Experiment With Guarded Stopping*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: An A/B test of two PA prompts hits p<0.05 in favor of treatment after one day; the team wants to ship immediately. Why hold off?
    - Correct: Stopping early because it 'looks significant' (peeking) inflates false positives; you may be shipping noise without the pre-committed sample size
    - Explanation: Repeatedly checking and stopping at the first significant moment dramatically inflates the false-positive rate. Without the pre-committed sample size and guardrail check, you risk institutionalizing a…
- **antipattern** — *What Goes Wrong*:
    - Peeking: the experiment is stopped at the first lucky p-value, a worse prompt is promoted, and override rates quietly rise.
    - No kill switch: a bad variant requires a redeploy to disable, turning a 30-second mitigation into a 30-minute incident.

## SVG Diagram Plan
A `renderVisual("M10")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#6f93c9`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE M29 A/B Testing
- `platform` → Platform M11 Release

## Lab Briefs
- **Understand It:** Review an experiment write-up and identify whether peeking, missing guardrails, or insufficient sample size threatens its conclusion.
- **Build It with AI:** Add a flag layer to the PA pipeline that supports per-cohort model/prompt selection, a kill switch, and an experiment harness enforcing a pre-committed sample size.

## LLMOps Takeaway
Feature flags decouple deploy from release — giving you kill switches and live experiments — but only disciplined, pre-committed statistics keep those experiments from shipping noise as wins.

## Anti-Patterns
- A/B test stopped the moment it 'looks significant' (peeking) — you ship noise as a win.
- No kill switch, so disabling a misbehaving variant requires a full redeploy during an incident.

## Continuity Notes
Builds on the prior track-3 / sequence module **M09**. Followed by **M11**, which carries these concepts forward.
