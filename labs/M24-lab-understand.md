# M24 Lab: Understand It — LLM Failure Modes Taxonomy

## Objective
Classify a set of past PA incidents into failure families and severities; identify which family recurs most and lacks a detector.

## Prerequisites
- Completed module M24 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Hospital Medical-Error Categories* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The failure families: hallucination, refusal, drift, injection, format, latency/cost
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the failure families: hallucination, refusal, drift, injection, format, latency/cost" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Severity classification by member and compliance impact
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "severity classification by member and compliance impact" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Mapping failure modes to detectors and owners
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "mapping failure modes to detectors and owners" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Treating every incident as a novel mystery — no taxonomy means no pattern, no prevention, slow response.
  - Classifying by symptom not cause — 'the model is wrong' lumps hallucination, drift, and injection into one useless bucket.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. During an incident, on-call reports 'the PA model is giving wrong answers.' Why is a failure taxonomy worth adopting before the next incident?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Hospital Medical-Error Categories* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Adopt a shared failure taxonomy classified by cause and severity — so every incident maps instantly to a detector, an owner, and a runbook instead of being re-diagnosed from scratch.
