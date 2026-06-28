# M19 Lab: Understand It — Synthetic Data & Augmentation

## Objective
Identify the most under-represented case types in your PA gold set and assess the risk of leaving them untested.

## Prerequisites
- Completed module M19 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Flight Simulators* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — When synthetic data helps: rare classes, edge cases, privacy
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "when synthetic data helps: rare classes, edge cases, privacy" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Generating realistic PA cases without leaking real PHI
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "generating realistic pa cases without leaking real phi" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Validating synthetic data so it doesn't poison your eval
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "validating synthetic data so it doesn't poison your eval" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Mixing unvalidated synthetic cases into the gold set — you measure against fiction and trust a wrong number.
  - Generating synthetic data with the same model you're testing — it manufactures cases it already handles well.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. You generate 50 synthetic PA cases for a rare service type and want to use them. Which use is appropriate, and which would corrupt your evaluation?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Flight Simulators* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Use synthetic data to simulate the rare and dangerous cases logs lack — but validate it, tag its provenance, and keep it out of the human gold gate so you never grade the model against fiction.
