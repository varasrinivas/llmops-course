# M04 Lab: Understand It — Evaluation Frameworks

## Objective
Take an existing 'eval' and audit it for coverage: which service types, determinations, and difficulty bands are missing? Estimate what production failures it cannot catch.

## Prerequisites
- Completed module M04 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Types of School Testing* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The four eval types: golden sets, reference-free, LLM-as-judge, human review
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the four eval types: golden sets, reference-free, llm-as-judge, human review" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Building a representative gold set for PA determinations
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "building a representative gold set for pa determinations" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Offline vs online evaluation
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "offline vs online evaluation" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - A gold set of 12 hand-picked easy cases — it certifies nothing about the real, messy case mix.
  - Optimizing a single average metric while the worst-case denials (the ones that get appealed) quietly get worse.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA model scores 94% overall agreement on the gold set, and the team wants to ship. What should you check BEFORE approving release?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Types of School Testing* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
A trustworthy eval program mixes golden sets, structural checks, judges, and human review — and always reads per-slice results, because the average hides the failures that matter most.
