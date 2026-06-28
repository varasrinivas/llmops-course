# M02 Lab: Understand It — The LLM Application Stack

## Objective
Diagram the PA pipeline's seven layers and, for each, write the one failure mode most likely to cause a wrong determination and how you'd detect it.

## Prerequisites
- Completed module M02 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Car's Systems, Not Just Its Engine* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The seven layers: interface → orchestration → retrieval → prompt → model → guardrails → storage
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the seven layers: interface → orchestration → retrieval → prompt → model → guardrails → storage" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Where latency, cost, and quality are actually decided
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "where latency, cost, and quality are actually decided" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Why most 'model problems' are really stack problems
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why most 'model problems' are really stack problems" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Blaming the model for what is actually a stale retrieval index — you swap models for weeks and nothing improves.
  - No layer-level tracing, so a 4-second response can't be attributed to retrieval vs generation.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A medical director reports the PA assistant 'keeps citing a policy rule that was retired last year.' Where should you look FIRST?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Car's Systems, Not Just Its Engine* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
An LLM application is a multi-layer system, and operating it means observing every layer — because most 'model problems' are really retrieval, prompt, or guardrail problems.
