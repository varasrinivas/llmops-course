# M18 Lab: Understand It — The Data Flywheel

## Objective
Map your current serve→capture→curate→improve loop and find the broken link (usually capture-with-no-improve or improve-with-no-validation); estimate flywheel velocity.

## Prerequisites
- Completed module M18 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Amazon's Virtuous Cycle* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The flywheel: serve → capture → curate → improve → serve
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the flywheel: serve → capture → curate → improve → serve" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — What 'improve' means without retraining: prompts, retrieval, few-shots, routing
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "what 'improve' means without retraining: prompts, retrieval, few-shots, routing" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Measuring flywheel velocity and avoiding feedback-loop bias
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "measuring flywheel velocity and avoiding feedback-loop bias" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - A feedback loop that only sees its own outputs — the model trains on its mistakes and confidently entrenches them.
  - Capturing feedback that never reaches 'improve' — a flywheel with no axle, spinning effort with no momentum.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. To accelerate improvement, an engineer proposes auto-adding every determination the model made with high confidence to the training/few-shot pool. Why is this risky?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Amazon's Virtuous Cycle* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
A data flywheel compounds quality only when human-verified feedback drives improvement that clears the regression gate — feed it the model's own guesses and it compounds your errors instead.
