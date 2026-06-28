# M21 Lab: Understand It — Model Migration

## Objective
Compare two models on the same PA gold set and prompt; quantify per-slice disagreement and identify where the 'better' model actually regresses.

## Prerequisites
- Completed module M21 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Upgrading a City Bus Fleet* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Why a 'better' model can be worse for your specific task
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why a 'better' model can be worse for your specific task" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Behavioral diffing: shadow the new model against the old
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "behavioral diffing: shadow the new model against the old" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Re-tuning prompts for the new model's quirks
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "re-tuning prompts for the new model's quirks" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Swapping models because the new one tops a public benchmark — your task isn't the benchmark, and it regresses on denials.
  - Migrating without re-tuning prompts — the old prompt was shaped to the old model's quirks and now underperforms.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A new model scores higher on public reasoning benchmarks, so a teammate wants to swap it into the PA pipeline this week. What's the disciplined path?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Upgrading a City Bus Fleet* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Migrate models as a staged, gated release — shadow, diff, re-tune the prompt, canary — because 'better in general' routinely means 'worse for your specific task' until proven otherwise on your gold set.
