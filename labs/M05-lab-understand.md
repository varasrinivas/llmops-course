# M05 Lab: Understand It — LLM-as-Judge

## Objective
Take 30 PA rationales scored by a naive judge and by a human; measure agreement, then identify whether verbosity or position bias explains the disagreements.

## Prerequisites
- Completed module M05 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Restaurant Critics and the Michelin Guide* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — When a judge model beats string matching
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "when a judge model beats string matching" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Writing rubrics that produce consistent scores
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "writing rubrics that produce consistent scores" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Known biases: position, verbosity, self-preference — and how to control them
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "known biases: position, verbosity, self-preference" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Trusting judge scores that were never validated against human labels — you scale a bias instead of catching it.
  - Judging with the same model that generated the answer — self-preference inflates the grade.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. You want to use an LLM judge to grade PA rationales at scale. What must you do BEFORE relying on its scores in your release gate?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Restaurant Critics and the Michelin Guide* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
An LLM judge scales semantic grading only after you've controlled its biases and validated it against human labels — an uncalibrated judge automates bias, not quality.
