# M12 Plan — LLM-Specific Metrics

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M12 | **Track:** 4 (Monitoring & Observability) | **Color:** #e3a52c maize
- **Title:** LLM-Specific Metrics
- **Subtitle:** The vital signs of a production LLM app — quality, cost, latency, and safety
- **Icon:** 🩺

## Everyday Analogy: A Hospital Vital-Signs Panel
A bedside monitor doesn't show one number; it tracks heart rate, blood pressure, O2, and temperature together, because a patient can have a perfect pulse and be crashing on oxygen. An LLM app needs the same panel: quality, cost, latency, and safety side by side — because your PA pipeline can have 100% uptime while its determination quality is silently bleeding out.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The four metric families: quality, cost, latency, safety/compliance
2. Leading vs lagging indicators of quality
3. Why request count and uptime are necessary but nowhere near sufficient
4. Designing the PA determination metrics panel

## Sections Outline
- **content** — *Four Families of Vital Signs*: A complete panel tracks four families. Quality: reviewer agreement, per-class recall, override rate, appeal-overturn rate. Cost: cost per determination, tokens…
- **content** — *Leading Beats Lagging*: The cruelest quality metric is appeal-overturn rate: by the time it moves, the bad determinations are weeks old and already harmed members. Pair every lagging m…
- **code** (python) — *Defining the Metrics Panel*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA service shows 99.98% uptime and healthy QPS, and leadership calls monitoring 'solved.' Why is this dangerously incomplete?
    - Correct: Infra metrics say the service responds, not that its determinations are correct, affordable, or compliant — quality can collapse while uptime stays green
    - Explanation: Uptime and QPS are the floor: they confirm the service answers, not that it answers well. A PA pipeline can be 100% available while override and appeal-overturn rates climb. You need the full vital-si…
- **antipattern** — *What Goes Wrong*:
    - Infra-only monitoring: dashboards are green, the service is 'up', and determination quality quietly degrades for weeks.
    - Lagging-only quality: the first signal is an appeals spike, by which point thousands of wrong determinations are already in members' records.

## SVG Diagram Plan
A `renderVisual("M12")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#e3a52c`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M28 Observability
- `sdlc` → AI-SDLC — Ops

## Lab Briefs
- **Understand It:** Audit a current LLM dashboard and classify every metric as infra/quality/cost/safety and leading/lagging; identify the missing quadrants.
- **Build It with AI:** Define a full PA metrics panel with the four families, mark leading vs lagging metrics, and configure alert thresholds tied to regulatory TAT and quality floors.

## LLMOps Takeaway
Monitor an LLM app like a patient on a vital-signs panel — quality, cost, latency, and safety together, with leading indicators — because uptime tells you the service responds, not that it's right.

## Anti-Patterns
- Monitoring only infra (uptime, QPS) — the service is 'up' while determination quality collapses unseen.
- Tracking only lagging quality (appeals overturned) — you learn about a regression weeks after it shipped.

## Continuity Notes
Builds on the prior track-4 / sequence module **M11**. Followed by **M13**, which carries these concepts forward.
