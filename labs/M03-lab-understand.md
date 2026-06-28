# M03 Lab: Understand It — The LLMOps Toolchain

## Objective
Inventory your current LLM tooling against the five categories; flag the categories that are missing and the call sites that bypass any gateway seam.

## Prerequisites
- Completed module M03 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Mechanic's Specialized Garage* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The five tool categories: eval, observability, gateway, feature flags, feedback
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the five tool categories: eval, observability, gateway, feature flags, feedback" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Buy vs build vs open-source for each category
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "buy vs build vs open-source for each category" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Avoiding lock-in with thin abstraction seams
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "avoiding lock-in with thin abstraction seams" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Buying a single 'LLMOps platform' that does everything poorly and locks every layer to one vendor.
  - Calling the model SDK directly everywhere — swapping providers later means touching hundreds of call sites.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A vendor demos one platform that bundles eval, tracing, flags, and a gateway. What is the strongest reason to be cautious before standardizing the whole PA stack on it?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Mechanic's Specialized Garage* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Choose LLMOps tooling per category behind a thin gateway seam — so any single tool can be swapped without rewriting the application.
