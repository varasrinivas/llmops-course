# M14 Lab: Understand It — Distributed Tracing for LLM Pipelines

## Objective
Pull a trace for a wrong determination and use the spans to localize the fault to a specific layer; note what attribute was missing to fully explain it.

## Prerequisites
- Completed module M14 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Postal Package Tracking* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Trace, span, and context propagation across multi-step pipelines
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "trace, span, and context propagation across multi-step pipelines" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Capturing prompts, retrieved criteria, tokens, and cost per span
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "capturing prompts, retrieved criteria, tokens, and cost per span" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Linking a determination to its exact inputs for audit and appeals
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "linking a determination to its exact inputs for audit and appeals" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Logging only the final determination — when it's wrong you can't see which layer caused it.
  - Tracing 100% of traffic at full fidelity — storage costs explode and you sample nothing intelligently.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A medical director disputes a specific denial from last month. What capability lets you answer 'exactly what did the model see and decide?' in minutes?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Postal Package Tracking* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Trace every PA request hop-by-hop and persist high-stakes traces — because a stored trace is simultaneously your fastest debugger and your audit evidence for an appeal.
