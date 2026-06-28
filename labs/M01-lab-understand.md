# M01 Lab: Understand It — LLMOps vs MLOps — What's Actually Different

## Objective
Audit an existing MLOps pipeline and classify each component as 'still applies', 'needs adaptation', or 'irrelevant' for an LLM app. Identify the three biggest unmonitored LLM-specific risks.

## Prerequisites
- Completed module M01 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Manufacturing Your Own Parts vs Running a Consultancy* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — No training loop: you operate a model you did not train
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "no training loop: you operate a model you did not train" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Non-determinism: the same input can yield different outputs
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "non-determinism: the same input can yield different outputs" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Behavior changes through prompts and context, not just code or weights
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "behavior changes through prompts and context, not just code or weights" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Reusing an accuracy-only MLOps dashboard — it misses hallucination, refusal, injection, and cost-per-call entirely.
  - Treating model version as static config — a silent provider snapshot update is a deployment you didn't make.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your team copies its mature MLOps stack to launch the PA assistant: weight registry, training CI, an accuracy dashboard. Which gap is MOST likely to cause a production incident first?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Manufacturing Your Own Parts vs Running a Consultancy* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
LLMOps inherits MLOps discipline but re-centers it on prompts, non-determinism, and a provider you don't control — the operational risk moves from training the model to directing and verifying one.
