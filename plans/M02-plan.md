# M02 Plan — The LLM Application Stack

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M02 | **Track:** 1 (Foundations) | **Color:** #4caf82 pine
- **Title:** The LLM Application Stack
- **Subtitle:** The layers between a user request and a model response — and where each can fail
- **Icon:** 🧱

## Everyday Analogy: A Car's Systems, Not Just Its Engine
Drivers blame 'the engine' when the car runs badly, but the fault is usually fuel delivery, sensors, or transmission. An LLM app is the same: people blame 'the model,' but poor results usually come from stale retrieval (bad fuel), a sloppy prompt (mis-tuned timing), or a missing guardrail (no brakes). To operate the system you must see every layer, not just the engine.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The seven layers: interface → orchestration → retrieval → prompt → model → guardrails → storage
2. Where latency, cost, and quality are actually decided
3. Why most 'model problems' are really stack problems
4. Mapping the PA pipeline onto the stack

## Sections Outline
- **content** — *Seven Layers, Seven Failure Modes*: A production LLM request passes through layers, each with its own failure mode. Interface (the PA intake portal/fax parser) can mangle input. Orchestration sequ…
- **content** — *Most 'Model Problems' Are Stack Problems*: When a PA determination is wrong, the instinct is to swap the model. But in practice the index returned last quarter's policy, or the prompt truncated the clini…
- **code** (python) — *Layer-Attributed Tracing*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A medical director reports the PA assistant 'keeps citing a policy rule that was retired last year.' Where should you look FIRST?
    - Correct: The retrieval layer and its index version — it is almost certainly serving stale criteria
    - Explanation: A retired-but-cited rule is a classic stale-retrieval symptom: the model is faithfully reasoning over outdated criteria the retrieval layer handed it. Re-indexing the current medical policy fixes it;…
- **antipattern** — *What Goes Wrong*:
    - Treating the stack as a black box: a wrong determination triggers a model swap when the real cause was a six-month-old policy index.
    - No per-layer cost/latency attribution: a 5s p95 can't be traced, so the team optimizes the model while retrieval quietly eats 4 of those seconds.

## SVG Diagram Plan
A `renderVisual("M02")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#4caf82`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M03 App Stack
- `ce` → CE — Context Assembly

## Lab Briefs
- **Understand It:** Diagram the PA pipeline's seven layers and, for each, write the one failure mode most likely to cause a wrong determination and how you'd detect it.
- **Build It with AI:** Instrument the pipeline with per-layer spans (retrieval, prompt, model, guardrail) capturing version, tokens, cost, and latency; produce a waterfall view for a single request.

## LLMOps Takeaway
An LLM application is a multi-layer system, and operating it means observing every layer — because most 'model problems' are really retrieval, prompt, or guardrail problems.

## Anti-Patterns
- Blaming the model for what is actually a stale retrieval index — you swap models for weeks and nothing improves.
- No layer-level tracing, so a 4-second response can't be attributed to retrieval vs generation.

## Continuity Notes
Builds on the prior track-1 / sequence module **M01**. Followed by **M03**, which carries these concepts forward.
