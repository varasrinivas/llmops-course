# M24 Plan — LLM Failure Modes Taxonomy

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M24 | **Track:** 7 (Incident & Reliability) | **Color:** #9486cf iris
- **Title:** LLM Failure Modes Taxonomy
- **Subtitle:** A shared vocabulary for how LLM apps actually break
- **Icon:** 📋

## Everyday Analogy: Hospital Medical-Error Categories
Hospitals classify errors — medication, surgical, diagnostic, documentation — because a shared taxonomy lets staff report, analyze, and prevent them systematically instead of treating each as a unique surprise. An LLM failure taxonomy does the same: when on-call can say 'this is a hallucinated-criterion incident, severity 1,' everyone knows the detector, the runbook, and the owner. Naming the failure is the first step to managing it.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. The failure families: hallucination, refusal, drift, injection, format, latency/cost
2. Severity classification by member and compliance impact
3. Mapping failure modes to detectors and owners
4. Why a shared taxonomy speeds every incident response

## Sections Outline
- **content** — *Six Failure Families*: LLM apps break in recognizable ways. Hallucination: the model invents a policy criterion that doesn't exist. Refusal: it declines a legitimate PA request as 'me…
- **content** — *Classify by Cause and Severity*: Two axes make the taxonomy operational. Cause (which family) routes to the right fix — hallucination needs grounding, injection needs input isolation; lumping t…
- **code** (python) — *A Failure Classifier*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: During an incident, on-call reports 'the PA model is giving wrong answers.' Why is a failure taxonomy worth adopting before the next incident?
    - Correct: A named family (e.g., 'hallucinated criterion, Sev-1') maps directly to a detector, owner, and runbook, so response is fast and the cause-specific fix is obvious
    - Explanation: 'Wrong answers' is a symptom that hides very different causes — hallucination, drift, and injection need opposite fixes. A shared taxonomy classifies by cause and severity, instantly pointing to the d…
- **antipattern** — *What Goes Wrong*:
    - Mystery-per-incident: with no taxonomy, every outage is re-diagnosed from scratch and recurring failures are never prevented.
    - Symptom-based buckets: 'model wrong' conflates injection and drift, so the team applies the wrong fix and the real cause persists.

## SVG Diagram Plan
A `renderVisual("M24")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#9486cf`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M29 Reliability
- `sdlc` → AI-SDLC — Incident

## Lab Briefs
- **Understand It:** Classify a set of past PA incidents into failure families and severities; identify which family recurs most and lacks a detector.
- **Build It with AI:** Implement a failure classifier that tags each production outcome with its families and severity and routes it to the right owner and runbook.

## LLMOps Takeaway
Adopt a shared failure taxonomy classified by cause and severity — so every incident maps instantly to a detector, an owner, and a runbook instead of being re-diagnosed from scratch.

## Anti-Patterns
- Treating every incident as a novel mystery — no taxonomy means no pattern, no prevention, slow response.
- Classifying by symptom not cause — 'the model is wrong' lumps hallucination, drift, and injection into one useless bucket.

## Continuity Notes
Builds on the prior track-7 / sequence module **M23**. Followed by **M25**, which carries these concepts forward.
