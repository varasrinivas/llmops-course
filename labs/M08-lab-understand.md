# M08 Lab: Understand It — CI/CD for LLM Applications

## Objective
Trace how a prompt change currently reaches production and list every step with no gate or no version record; rate the audit risk of each.

## Prerequisites
- Completed module M08 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Pharmaceutical Production Lines* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — What 'the artifact' is when there's no compiled binary
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "what 'the artifact' is when there's no compiled binary" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Eval gates, red-team gates, and cost gates in the pipeline
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "eval gates, red-team gates, and cost gates in the pipeline" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Promoting prompt+model+policy as one versioned bundle
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "promoting prompt+model+policy as one versioned bundle" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Editing the production prompt in a console with no version, no eval, no rollback — a 'hotfix' nobody can reproduce.
  - Eval results that are advisory, not blocking — so a failing gate gets waved through under deadline.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. During an appeal, a regulator asks you to reproduce exactly how a denial was reached 5 months ago. Your CI/CD design should have ensured what?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Pharmaceutical Production Lines* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
LLM CI/CD promotes prompt+model+policy as one fingerprinted bundle through blocking eval, red-team, and cost gates — so every production determination is both quality-gated and reproducible.
