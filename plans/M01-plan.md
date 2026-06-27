# M01 Plan — LLMOps vs MLOps — What's Actually Different

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M01 | **Track:** 1 (Foundations) | **Color:** #4caf82 pine
- **Title:** LLMOps vs MLOps — What's Actually Different
- **Subtitle:** Why your MLOps playbook only half-applies to LLM applications
- **Icon:** 🏭

## Everyday Analogy: Manufacturing Your Own Parts vs Running a Consultancy
Classic MLOps is like a factory that manufactures its own parts: you own the machine (training), so you version the blueprint and re-tool the line. LLMOps is like running a consulting firm staffed by brilliant contractors you don't employ — you can't retrain them, you brief them (prompts), check their work (evals), and they may answer the same question slightly differently each time. Your job shifts from building the worker to directing and verifying one.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. No training loop: you operate a model you did not train
2. Non-determinism: the same input can yield different outputs
3. Behavior changes through prompts and context, not just code or weights
4. New failure surface: hallucination, refusal, prompt injection, drift-on-update

## Sections Outline
- **content** — *Three Inversions From MLOps*: MLOps assumes you train a model: you own data pipelines, training runs, and weight versioning. With foundation models, three things invert. (1) No training loop…
- **content** — *A Bigger, Stranger Failure Surface*: A fraud classifier fails by being wrong. An LLM PA assistant can be wrong in qualitatively new ways: hallucinate a policy criterion that doesn't exist, refuse a…
- **code** (python) — *Pinning the Model Is Now a First-Class Concern*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your team copies its mature MLOps stack to launch the PA assistant: weight registry, training CI, an accuracy dashboard. Which gap is MOST likely to cause a production incident first?
    - Correct: No detection for hallucinated policy criteria, refusals, or a silent snapshot change
    - Explanation: You aren't training, so the training-centric machinery is mostly irrelevant. The real exposure is the LLM-specific failure surface — hallucinated criteria, refusals, and provider snapshot drift — whic…
- **antipattern** — *What Goes Wrong*:
    - Porting MLOps metrics 1:1 and declaring victory — the dashboard is green while the model invents a coverage rule that denies a valid claim.
    - Leaving the model name unpinned ('latest') — a provider snapshot ships overnight and your determinations shift with no PR, no review, no rollback path.

## SVG Diagram Plan
A `renderVisual("M01")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#4caf82`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `sdlc` → AI-SDLC — Model Governance
- `platform` → Platform M05 Multi-Provider

## Lab Briefs
- **Understand It:** Audit an existing MLOps pipeline and classify each component as 'still applies', 'needs adaptation', or 'irrelevant' for an LLM app. Identify the three biggest unmonitored LLM-specific risks.
- **Build It with AI:** Build a 'deployment fingerprint' utility that hashes model snapshot + prompt version + policy snapshot, and a CI check that fails the build whenever the fingerprint changes without an accompanying eval run.

## LLMOps Takeaway
LLMOps inherits MLOps discipline but re-centers it on prompts, non-determinism, and a provider you don't control — the operational risk moves from training the model to directing and verifying one.

## Anti-Patterns
- Reusing an accuracy-only MLOps dashboard — it misses hallucination, refusal, injection, and cost-per-call entirely.
- Treating model version as static config — a silent provider snapshot update is a deployment you didn't make.

## Continuity Notes
Builds on the prior track-1 / sequence module **M00**. Followed by **M02**, which carries these concepts forward.
