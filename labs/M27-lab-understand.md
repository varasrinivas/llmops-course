# M27 Lab: Understand It — Chaos Engineering for AI

## Objective
Inventory your pipeline's resilience assumptions (fallbacks, guardrails, rollback) and rate each by whether it has ever actually been exercised.

## Prerequisites
- Completed module M27 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Earthquake Preparedness Drills* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Why untested resilience is assumed, not proven
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why untested resilience is assumed, not proven" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — AI-specific chaos: provider outages, latency spikes, degraded quality, bad retrieval
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "ai-specific chaos: provider outages, latency spikes, degraded quality, bad retrieval" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Game days and blast-radius control
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "game days and blast-radius control" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Assuming the fallback provider works because it's configured — it was never exercised and fails on first real use.
  - Running chaos in production with no blast-radius limit — your drill becomes the incident.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA pipeline has a configured fallback provider that has never actually been triggered. Why run a chaos game day before you trust it?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Earthquake Preparedness Drills* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Prove resilience with controlled chaos game days — inject provider outages, latency, and degraded retrieval within a limited blast radius — because an unexercised fallback or guardrail is a hope, not a property.
