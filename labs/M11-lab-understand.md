# M11 Lab: Understand It — Rollback & Recovery

## Objective
Take a past incident and measure how long rollback actually took; identify what (versioning, flags, runbook) would have cut it to seconds and whether state was remediated.

## Prerequisites
- Completed module M11 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *An Airplane Go-Around* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Why 'roll forward' is often the wrong instinct under fire
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why 'roll forward' is often the wrong instinct under fire" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Versioned bundles make rollback a config flip, not a redeploy
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "versioned bundles make rollback a config flip, not a redeploy" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Recovering corrupted state: re-adjudicating bad determinations
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "recovering corrupted state: re-adjudicating bad determinations" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Trying to 'roll forward' a hotfix during an active incident — you ship a second, unevaluated change on top of the first.
  - No plan for the bad determinations already issued — you roll back the code but leave wrong denials in members' records.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Prompt v8 is wrongly denying valid PA requests in production. What is the correct FIRST action, and what must recovery also address?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *An Airplane Go-Around* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Recovery means reverting to a known-good bundle in seconds and then re-adjudicating the bad determinations it left behind — because rolling back the code doesn't roll back the harm.
