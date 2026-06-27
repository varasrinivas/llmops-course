# M00 Lab: Understand It — LLM Application Lifecycle Audit

## Objective
Map a real LLM application's lifecycle stages, identify which have proper tooling, and quantify the operational risk of gaps.

## Prerequisites
- Completed M00 module content
- Access to an LLM application in production (or use the UCC extraction pipeline as the example)

## Exercise (25 min)

### Step 1: Map the 6 Lifecycle Stages
Create a table for your application:

| Stage | Tooling Status | Automation Level | Risk if Missing |
|-------|---------------|-----------------|-----------------|
| Build | ✅ Claude API + prompts | Manual | Low (already done) |
| Evaluate | ❓ | ? | ? |
| Deploy | ❓ | ? | ? |
| Monitor | ❓ | ? | ? |
| Feedback | ❓ | ? | ? |
| Upgrade | ❓ | ? | ? |

### Step 2: Score Each Stage
Rate each 0-3: 0=missing, 1=manual, 2=partially automated, 3=fully automated.

**Expected finding:** Most teams score 2-3 on Build but 0-1 on Monitor, Feedback, and Upgrade.

### Step 3: Calculate Operational Risk
For each gap, estimate: What's the worst thing that happens if this stage stays at its current maturity for 6 months?

## Reflection Questions
1. Which lifecycle stage has the biggest gap between current state and where it needs to be?
2. If you could only invest in one stage, which would reduce the most risk?
3. How does this map to the restaurant analogy — which restaurant function is missing?

## Key Insight
The stages you're weakest at are the ones that will cause production incidents. Build is the easy part — Evaluate, Monitor, and Feedback are where production AI succeeds or fails.
