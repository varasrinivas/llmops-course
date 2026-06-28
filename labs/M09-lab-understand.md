# M09 Lab: Understand It — Canary & Progressive Deployment

## Objective
Given a rollout that caused an incident, identify what canary stage and which guardrail metric would have caught it, and how many determinations the blast radius would have been reduced to.

## Prerequisites
- Completed module M09 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Testing a New Recipe on a Few Tables* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Why big-bang LLM releases are uniquely dangerous
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why big-bang llm releases are uniquely dangerous" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Canary cohorts and automated promotion criteria
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "canary cohorts and automated promotion criteria" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Shadow deployment: running the new version with no live impact
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "shadow deployment: running the new version with no live impact" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Big-bang 100% release of a prompt change — a regression hits every member simultaneously.
  - Canary with no automated halt — by the time a human notices, the bad version already served thousands of determinations.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. You're rolling out prompt v8 to a PA pipeline serving thousands of determinations per hour. Why is an automated guardrail-based halt essential, rather than watching a dashboard?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Testing a New Recipe on a Few Tables* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Release LLM changes progressively — shadow, then canary, then expand — with guardrail metrics that automatically halt and roll back, because at production volume humans react far too slowly.
