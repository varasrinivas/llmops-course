# M14 Plan — Distributed Tracing for LLM Pipelines

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M14 | **Track:** 4 (Monitoring & Observability) | **Color:** #e3a52c maize
- **Title:** Distributed Tracing for LLM Pipelines
- **Subtitle:** Following one request through every hop so you can debug what actually happened
- **Icon:** 📦

## Everyday Analogy: Postal Package Tracking
When a package is late, the tracking history shows every scan — accepted, sorted, in transit, out for delivery — so you know exactly where it stalled. A trace does that for a PA request: each hop (retrieval, prompt build, model call, guardrail, write) leaves a timestamped scan, so when a determination is wrong or slow you can see precisely where, instead of guessing.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Trace, span, and context propagation across multi-step pipelines
2. Capturing prompts, retrieved criteria, tokens, and cost per span
3. Linking a determination to its exact inputs for audit and appeals
4. Sampling strategy: trace everything that matters, store affordably

## Sections Outline
- **content** — *Trace, Span, Context*: A trace is the full story of one PA request; each step is a span with a start, end, and attributes; a trace-id propagates through every hop so the spans stitch…
- **content** — *Tracing as Audit Evidence*: In a regulated PA workflow, the trace is not just for debugging — it's audit evidence. An appeal months later may require showing exactly what the model saw and…
- **code** (python) — *Stitched, Audit-Ready Traces*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A medical director disputes a specific denial from last month. What capability lets you answer 'exactly what did the model see and decide?' in minutes?
    - Correct: A stored trace for that request linking the retrieved policy snapshot, assembled prompt, model snapshot, and guardrail result
    - Explanation: Re-running on today's pipeline answers 'what would happen now', not 'what happened then' — the policy and model may have changed. A persisted trace tied to that request captures the exact inputs and d…
- **antipattern** — *What Goes Wrong*:
    - Outcome-only logging: a disputed denial can't be reconstructed because the retrieved criteria and prompt were never captured.
    - Naive full-fidelity tracing: storage costs balloon, so tracing gets cut entirely — right before the audit that needed it.

## SVG Diagram Plan
A `renderVisual("M14")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#e3a52c`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M28 Tracing
- `sdlc` → AI-SDLC — Audit

## Lab Briefs
- **Understand It:** Pull a trace for a wrong determination and use the spans to localize the fault to a specific layer; note what attribute was missing to fully explain it.
- **Build It with AI:** Instrument the PA pipeline with propagated traces capturing retrieval snapshot, prompt, model, tokens, cost, and guardrail result, plus a sampling policy that keeps 100% of denials/overrides.

## LLMOps Takeaway
Trace every PA request hop-by-hop and persist high-stakes traces — because a stored trace is simultaneously your fastest debugger and your audit evidence for an appeal.

## Anti-Patterns
- Logging only the final determination — when it's wrong you can't see which layer caused it.
- Tracing 100% of traffic at full fidelity — storage costs explode and you sample nothing intelligently.

## Continuity Notes
Builds on the prior track-4 / sequence module **M13**. Followed by **M15**, which carries these concepts forward.
