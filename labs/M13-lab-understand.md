# M13 Lab: Understand It — Quality Drift Detection

## Objective
Given a window of PA traffic, compute input PSI and override-rate shift versus a baseline and decide whether drift is occurring and which type it is.

## Prerequisites
- Completed module M13 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Wheel Alignment* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The three drift types: input drift, model drift, policy/concept drift
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the three drift types: input drift, model drift, policy/concept drift" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Detecting drift without ground-truth labels in real time
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "detecting drift without ground-truth labels in real time" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Distribution tests, embedding shift, and proxy-quality signals
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "distribution tests, embedding shift, and proxy-quality signals" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Waiting for labeled outcomes to confirm drift — by then it's months old and expensive.
  - Drift alarms so twitchy they fire on every Monday-morning volume bump — the team mutes them and misses the real one.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. You want to catch PA quality drift early, but nurse-confirmed labels for a determination arrive 2-3 weeks later. What's the best detection strategy?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Wheel Alignment* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Detect quality drift with corroborating label-free signals — input shift plus proxy-quality — so you catch the slow misalignment in real time instead of waiting weeks for labels to confirm the blowout.
