# M19 Plan — Synthetic Data & Augmentation

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M19 | **Track:** 5 (Data & Feedback Loops) | **Color:** #8fc7a8 sage
- **Title:** Synthetic Data & Augmentation
- **Subtitle:** Generating the rare and dangerous cases your production logs lack
- **Icon:** 🧬

## Everyday Analogy: Flight Simulators
Pilots can't practice an engine fire on a real flight, so simulators generate the rare, dangerous scenarios safely and repeatedly. Synthetic data is the simulator for your PA model: you manufacture the rare service types, the adversarial notes, and the tricky edge cases that almost never appear in logs — so the model is tested on the emergencies before it meets one for real, and without exposing real patient data.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. When synthetic data helps: rare classes, edge cases, privacy
2. Generating realistic PA cases without leaking real PHI
3. Validating synthetic data so it doesn't poison your eval
4. Augmentation vs fabrication — keeping the distribution honest

## Sections Outline
- **content** — *When Synthetic Data Earns Its Place*: Production logs under-represent exactly the cases that matter most: a rare oncology regimen, a service type seen twice a year, an adversarial fax. Synthetic dat…
- **content** — *Validate, Tag, and Don't Fool Yourself*: Synthetic data is dangerous if it leaks into eval unchecked: you'd measure the model against scenarios that don't reflect reality, or worse, against cases gener…
- **code** (python) — *Generate and Guard Synthetic Cases*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: You generate 50 synthetic PA cases for a rare service type and want to use them. Which use is appropriate, and which would corrupt your evaluation?
    - Correct: Use validated, tagged synthetic cases to augment the few-shot/training pool, but keep them out of the human-labeled held-out gold gate
    - Explanation: Synthetic cases are great for augmenting training/few-shot coverage of rare classes, but if they enter the held-out human gold set you're grading the model against fiction (and against cases a sibling…
- **antipattern** — *What Goes Wrong*:
    - Synthetic leakage into the gold gate: release decisions ride on made-up cases, and real-world quality diverges from the green dashboard.
    - Self-generated tests: cases authored by the model under test flatter it, hiding the very weaknesses you generated data to expose.

## SVG Diagram Plan
A `renderVisual("M19")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#8fc7a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE — Data Augmentation
- `platform` → Platform M12 Safety

## Lab Briefs
- **Understand It:** Identify the most under-represented case types in your PA gold set and assess the risk of leaving them untested.
- **Build It with AI:** Generate and validate a batch of synthetic rare-class and adversarial PA cases (using a different model than the system under test), tag provenance, and add them only to the few-shot pool.

## LLMOps Takeaway
Use synthetic data to simulate the rare and dangerous cases logs lack — but validate it, tag its provenance, and keep it out of the human gold gate so you never grade the model against fiction.

## Anti-Patterns
- Mixing unvalidated synthetic cases into the gold set — you measure against fiction and trust a wrong number.
- Generating synthetic data with the same model you're testing — it manufactures cases it already handles well.

## Continuity Notes
Builds on the prior track-5 / sequence module **M18**. Followed by **M20**, which carries these concepts forward.
