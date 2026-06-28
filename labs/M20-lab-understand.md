# M20 Lab: Understand It — Model Versioning & Pinning

## Objective
Inspect a pipeline's model configuration for floating aliases and check whether determinations record their snapshot; rate the audit and rollback risk.

## Prerequisites
- Completed module M20 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Pharmaceutical Lot Numbers* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Pinned snapshots vs floating aliases ('latest')
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "pinned snapshots vs floating aliases ('latest')" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Why a silent provider update is an unreviewed deployment
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "why a silent provider update is an unreviewed deployment" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Tying every determination to its exact model version
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "tying every determination to its exact model version" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Pointing at a floating alias like 'latest' — the provider updates it and your behavior shifts with no PR and no rollback.
  - Not recording the model snapshot per determination — during an appeal you can't say which model decided.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA pipeline targets the model alias 'latest' to always get improvements. One morning determinations shift noticeably with no change on your side. What happened, and what's the fix?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Pharmaceutical Lot Numbers* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Pin the exact model snapshot and stamp it on every determination — so a provider update is a decision you make and evaluate, not one that happens to you, and every decision is reproducible.
