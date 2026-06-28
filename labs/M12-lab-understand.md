# M12 Lab: Understand It — LLM-Specific Metrics

## Objective
Audit a current LLM dashboard and classify every metric as infra/quality/cost/safety and leading/lagging; identify the missing quadrants.

## Prerequisites
- Completed module M12 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Hospital Vital-Signs Panel* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The four metric families: quality, cost, latency, safety/compliance
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the four metric families: quality, cost, latency, safety/compliance" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Leading vs lagging indicators of quality
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "leading vs lagging indicators of quality" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Why request count and uptime are necessary but nowhere near sufficient
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why request count and uptime are necessary but nowhere near sufficient" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Monitoring only infra (uptime, QPS) — the service is 'up' while determination quality collapses unseen.
  - Tracking only lagging quality (appeals overturned) — you learn about a regression weeks after it shipped.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA service shows 99.98% uptime and healthy QPS, and leadership calls monitoring 'solved.' Why is this dangerously incomplete?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Hospital Vital-Signs Panel* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Monitor an LLM app like a patient on a vital-signs panel — quality, cost, latency, and safety together, with leading indicators — because uptime tells you the service responds, not that it's right.
