# M13 Plan — Quality Drift Detection

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M13 | **Track:** 4 (Monitoring & Observability) | **Color:** #e3a52c maize
- **Title:** Quality Drift Detection
- **Subtitle:** Catching the slow, silent decline before it becomes an incident
- **Icon:** 📉

## Everyday Analogy: Wheel Alignment
A car with slightly misaligned wheels drives fine today, but the tires wear unevenly and months later you're replacing them early. Quality drift is that misalignment: no single determination looks broken, but the distribution slowly pulls off-center until appeals spike. Drift detection is the alignment check you run continuously, not the blowout you wait for.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The three drift types: input drift, model drift, policy/concept drift
2. Detecting drift without ground-truth labels in real time
3. Distribution tests, embedding shift, and proxy-quality signals
4. Setting drift alarms that fire early but don't cry wolf

## Sections Outline
- **content** — *Three Kinds of Drift*: Input drift: the incoming PA requests change — a new provider group submits differently formatted notes, or a seasonal surge in a service type. Model drift: the…
- **content** — *Detecting Drift Without Labels*: Ground-truth labels (nurse-confirmed determinations) arrive slowly, so you can't wait for them. Use label-free signals: distribution tests on inputs (PSI, KL di…
- **code** (python) — *A Label-Free Drift Detector*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: You want to catch PA quality drift early, but nurse-confirmed labels for a determination arrive 2-3 weeks later. What's the best detection strategy?
    - Correct: Combine label-free signals — input/embedding distribution shifts plus proxy-quality like override rate and a live judge score — and alarm when several corroborate
    - Explanation: Label latency means waiting for ground truth detects drift weeks late. Label-free signals — distribution shift on inputs/embeddings and proxy-quality metrics — move in near real time, and requiring se…
- **antipattern** — *What Goes Wrong*:
    - Label-only detection: drift is 'confirmed' only after appeals overturn spikes, three weeks and thousands of determinations too late.
    - Hair-trigger alarms: every volume bump pages on-call, the team mutes drift alerts, and the real concept-drift event goes unnoticed.

## SVG Diagram Plan
A `renderVisual("M13")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#e3a52c`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE M14 Context Decay
- `platform` → Platform M28 Observability

## Lab Briefs
- **Understand It:** Given a window of PA traffic, compute input PSI and override-rate shift versus a baseline and decide whether drift is occurring and which type it is.
- **Build It with AI:** Build a drift detector combining input distribution tests, embedding shift, and proxy-quality signals, with a corroboration-and-sustained rule to suppress false alarms.

## LLMOps Takeaway
Detect quality drift with corroborating label-free signals — input shift plus proxy-quality — so you catch the slow misalignment in real time instead of waiting weeks for labels to confirm the blowout.

## Anti-Patterns
- Waiting for labeled outcomes to confirm drift — by then it's months old and expensive.
- Drift alarms so twitchy they fire on every Monday-morning volume bump — the team mutes them and misses the real one.

## Continuity Notes
Builds on the prior track-4 / sequence module **M12**. Followed by **M14**, which carries these concepts forward.
