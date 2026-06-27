# M27 Plan — Chaos Engineering for AI

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M27 | **Track:** 7 (Incident & Reliability) | **Color:** #9486cf iris
- **Title:** Chaos Engineering for AI
- **Subtitle:** Deliberately injecting failure to prove your defenses work
- **Icon:** 🌀

## Everyday Analogy: Earthquake Preparedness Drills
A city doesn't wait for the real earthquake to discover its evacuation plan has gaps — it runs drills that simulate the disaster so weaknesses surface while everyone is safe. Chaos engineering is the earthquake drill for your PA pipeline: you deliberately trigger a provider outage or a quality drop in a controlled way, and find out whether your fallbacks, guardrails, and runbooks actually hold before a real failure tests them for you.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Why untested resilience is assumed, not proven
2. AI-specific chaos: provider outages, latency spikes, degraded quality, bad retrieval
3. Game days and blast-radius control
4. From chaos findings to runbook and guardrail improvements

## Sections Outline
- **content** — *Untested Resilience Is a Hope, Not a Property*: You configured a fallback provider, a schema guardrail, and a rollback flag. Do they actually work? Until exercised, they're assumptions. Chaos engineering repl…
- **content** — *Game Days With a Blast Radius*: Chaos is run as a game day: a hypothesis ('if the provider 500s, we fail over within 30s with no member impact'), a controlled injection, and observation of whe…
- **code** (python) — *A Controlled Chaos Experiment*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA pipeline has a configured fallback provider that has never actually been triggered. Why run a chaos game day before you trust it?
    - Correct: A configured-but-unexercised fallback is an assumption; injecting a controlled provider outage proves whether failover, guardrails, and the runbook actually work — before a real outage tests them
    - Explanation: Configuration isn't validation. The first time a fallback runs shouldn't be during a real outage at 2am. A controlled game day — with a limited blast radius and a kill switch — turns 'we think it work…
- **antipattern** — *What Goes Wrong*:
    - Untested fallback: it's invoked for the first time during a real provider outage and fails, turning a degraded state into a full outage.
    - Uncontrolled chaos: an injection with no blast-radius limit or kill switch escapes its cohort and becomes the very incident it was meant to prevent.

## SVG Diagram Plan
A `renderVisual("M27")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#9486cf`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M07 Resilience
- `platform` → Platform M29 Reliability

## Lab Briefs
- **Understand It:** Inventory your pipeline's resilience assumptions (fallbacks, guardrails, rollback) and rate each by whether it has ever actually been exercised.
- **Build It with AI:** Design and run a blast-radius-limited chaos experiment that injects a provider outage and degraded retrieval, observes guardrails and runbook behavior, and files fixes for every gap found.

## LLMOps Takeaway
Prove resilience with controlled chaos game days — inject provider outages, latency, and degraded retrieval within a limited blast radius — because an unexercised fallback or guardrail is a hope, not a property.

## Anti-Patterns
- Assuming the fallback provider works because it's configured — it was never exercised and fails on first real use.
- Running chaos in production with no blast-radius limit — your drill becomes the incident.

## Continuity Notes
Builds on the prior track-7 / sequence module **M26**. Followed by **M28**, which carries these concepts forward.
