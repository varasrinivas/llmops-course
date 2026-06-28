# M22 Lab: Understand It — Multi-Model Strategies

## Objective
Analyze a single-model pipeline's cost and per-slice quality; estimate the savings and risks of introducing a cheap-first cascade.

## Prerequisites
- Completed module M22 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Law Firm Staffing by Complexity* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Routing by complexity, stakes, and confidence
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "routing by complexity, stakes, and confidence" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Cascade/fallback patterns: cheap-first, escalate on low confidence
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "cascade/fallback patterns: cheap-first, escalate on low confidence" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Cost-quality trade-offs and the routing budget
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "cost-quality trade-offs and the routing budget" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - One expensive model for every determination — you pay partner rates to review NDAs and blow the budget.
  - Routing with no confidence signal — hard cases silently get the cheap model and quality craters on exactly the cases that matter.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. To cut cost, a team routes every PA determination through one premium model. What's the smarter design, and what makes it safe?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Law Firm Staffing by Complexity* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Route each determination to the right model by complexity, stakes, and validated confidence — a cascade that staffs cheap models on routine cases and reserves strong models and humans for where the stakes justify the cost.
