# M03 Plan — The LLMOps Toolchain

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M03 | **Track:** 1 (Foundations) | **Color:** #4caf82 pine
- **Title:** The LLMOps Toolchain
- **Subtitle:** The categories of tools you need — and how to choose without lock-in
- **Icon:** 🛠️

## Everyday Analogy: A Mechanic's Specialized Garage
A home toolbox has a hammer and a screwdriver. A working garage has a lift, a diagnostic scanner, a torque wrench, and a parts inventory — each specialized, each chosen deliberately. The LLMOps toolchain is the garage: an eval harness, an observability platform, a model gateway, a flagging system, and a feedback store. You don't need the most expensive lift; you need the right tools wired together so a car (a release) moves through safely.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The five tool categories: eval, observability, gateway, feature flags, feedback
2. Buy vs build vs open-source for each category
3. Avoiding lock-in with thin abstraction seams
4. A reference toolchain for the PA pipeline

## Sections Outline
- **content** — *Five Categories, Not One Platform*: The toolchain divides into five jobs. Evaluation (run gold sets, judges, regression). Observability/tracing (per-call logs, spans, cost). Model gateway (one sea…
- **content** — *The Abstraction Seam That Prevents Lock-In*: The single most valuable architectural move is a thin gateway seam: never call the provider SDK directly from business logic. Route every determination through…
- **code** (python) — *The Gateway Seam*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A vendor demos one platform that bundles eval, tracing, flags, and a gateway. What is the strongest reason to be cautious before standardizing the whole PA stack on it?
    - Correct: Bundling every category behind one vendor maximizes lock-in and couples your release path to their roadmap and outages
    - Explanation: Convenience is real, but standardizing all five categories on one vendor couples your eval, observability, and release flow to a single roadmap, price, and failure domain. Keeping a thin gateway seam…
- **antipattern** — *What Goes Wrong*:
    - All-in on one suite: when the vendor deprecates a feature or hikes pricing, your entire PA release pipeline is held hostage.
    - No gateway seam: the SDK is imported in 200 files, so adding retries or a fallback provider becomes a multi-sprint migration instead of a one-file change.

## SVG Diagram Plan
A `renderVisual("M03")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#4caf82`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M05 Gateway
- `sdlc` → AI-SDLC — Tooling

## Lab Briefs
- **Understand It:** Inventory your current LLM tooling against the five categories; flag the categories that are missing and the call sites that bypass any gateway seam.
- **Build It with AI:** Implement a minimal ModelGateway that adds tracing, cost tagging, and a flag-driven model variant, and refactor the PA pipeline to call only the gateway.

## LLMOps Takeaway
Choose LLMOps tooling per category behind a thin gateway seam — so any single tool can be swapped without rewriting the application.

## Anti-Patterns
- Buying a single 'LLMOps platform' that does everything poorly and locks every layer to one vendor.
- Calling the model SDK directly everywhere — swapping providers later means touching hundreds of call sites.

## Continuity Notes
Builds on the prior track-1 / sequence module **M02**. Followed by **M04**, which carries these concepts forward.
