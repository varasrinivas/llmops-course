# M23 Lab: Understand It — Model Deprecation & Sunset

## Objective
Given a deprecation notice, build the full inventory of where a model is referenced (code, live stamps, batch jobs, fallbacks) and assess what would break on EOL day.

## Prerequisites
- Completed module M23 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Building Elevator's End-of-Life* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Reading provider deprecation notices and EOL timelines
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "reading provider deprecation notices and eol timelines" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Inventory: every place a deprecated model is used
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "inventory: every place a deprecated model is used" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — The forced-migration fire drill vs the planned sunset
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the forced-migration fire drill vs the planned sunset" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Ignoring deprecation notices until the model returns errors in production — now it's a 2am forced migration with no eval.
  - No inventory of where a model is used — you migrate the obvious service and miss the batch job still calling the dead snapshot.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A provider announces your pinned PA model reaches end-of-life in 90 days, after which calls redirect to a successor. What's the right response?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Building Elevator's End-of-Life* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Treat every provider EOL date as a deadline you plan around — inventory all usages and migrate deliberately — because the alternative is an unevaluated forced migration at the worst possible moment.
