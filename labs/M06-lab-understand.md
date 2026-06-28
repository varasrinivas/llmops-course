# M06 Lab: Understand It — Regression Testing for LLM Apps

## Objective
Take a prompt change and run the full gold set before and after; identify any slice that regressed even though the targeted case improved.

## Prerequisites
- Completed module M06 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Bridge Load Testing* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Why prompt and model changes silently regress unrelated cases
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why prompt and model changes silently regress unrelated cases" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Snapshot/golden-output testing under non-determinism
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "snapshot/golden-output testing under non-determinism" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Tolerance bands and semantic equivalence instead of exact match
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "tolerance bands and semantic equivalence instead of exact match" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Only testing the case you just fixed — the fix silently breaks ten others you never re-ran.
  - Exact-string assertions on non-deterministic output — the suite is so flaky everyone disables it.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A developer fixes one mis-handled oncology case by editing the shared system prompt and re-tests only that case (now passing). Why is this dangerous in the PA pipeline?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Bridge Load Testing* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Treat every prompt or model change as a global change: re-run the full gold set with semantic tolerance bands so a fix in one slice can't silently regress another.
