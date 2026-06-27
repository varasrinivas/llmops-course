# M23 Plan — Model Deprecation & Sunset

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M23 | **Track:** 6 (Model Lifecycle) | **Color:** #cf6f5f brick
- **Title:** Model Deprecation & Sunset
- **Subtitle:** Retiring a model on your schedule, before the provider forces yours
- **Icon:** 🌅

## Everyday Analogy: A Building Elevator's End-of-Life
A building manager who ignores an elevator's end-of-life notice ends up with it failing inspection and shut down with no replacement ordered — tenants stuck on the stairs. Reading the notice early means scheduling the modernization, keeping the old car running during the swap, and a smooth cutover. Model deprecation is identical: the provider's EOL date is coming whether you plan for it or not.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Reading provider deprecation notices and EOL timelines
2. Inventory: every place a deprecated model is used
3. The forced-migration fire drill vs the planned sunset
4. Sunsetting your own prompt/bundle versions

## Sections Outline
- **content** — *The EOL Date Is Coming Either Way*: Every model snapshot gets deprecated. Providers publish end-of-life timelines, after which the snapshot returns errors or auto-redirects to a successor (a silen…
- **content** — *You Can't Sunset What You Can't Find*: The first step of any sunset is an inventory: every code path, batch job, eval harness, and fallback that references the deprecated snapshot. The classic failur…
- **code** (python) — *Find Every Usage Before Sunset*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A provider announces your pinned PA model reaches end-of-life in 90 days, after which calls redirect to a successor. What's the right response?
    - Correct: Inventory every usage now, migrate to a chosen successor via the staged gated playbook, and verify zero usage of the old snapshot before EOL
    - Explanation: The auto-redirect IS the danger — it's an unevaluated forced migration to a model you didn't test on your gold set. Plan the sunset: inventory all usages (including batch jobs and fallbacks), migrate…
- **antipattern** — *What Goes Wrong*:
    - Notice ignored: the model starts erroring on EOL day and the team scrambles a 2am migration with no eval, shipping an unvetted successor.
    - Incomplete inventory: the online path is migrated but a nightly re-adjudication job still calls the dead snapshot and silently fails for days.

## SVG Diagram Plan
A `renderVisual("M23")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#cf6f5f`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M05 Lifecycle
- `sdlc` → AI-SDLC — EOL

## Lab Briefs
- **Understand It:** Given a deprecation notice, build the full inventory of where a model is referenced (code, live stamps, batch jobs, fallbacks) and assess what would break on EOL day.
- **Build It with AI:** Write a sunset playbook and tooling that inventories all usages of a snapshot, drives staged migration, and asserts zero remaining usage before the EOL date.

## LLMOps Takeaway
Treat every provider EOL date as a deadline you plan around — inventory all usages and migrate deliberately — because the alternative is an unevaluated forced migration at the worst possible moment.

## Anti-Patterns
- Ignoring deprecation notices until the model returns errors in production — now it's a 2am forced migration with no eval.
- No inventory of where a model is used — you migrate the obvious service and miss the batch job still calling the dead snapshot.

## Continuity Notes
Builds on the prior track-6 / sequence module **M22**. Followed by **M24**, which carries these concepts forward.
