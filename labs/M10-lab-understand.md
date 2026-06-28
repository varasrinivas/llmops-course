# M10 Lab: Understand It — Feature Flags & Experimentation

## Objective
Review an experiment write-up and identify whether peeking, missing guardrails, or insufficient sample size threatens its conclusion.

## Prerequisites
- Completed module M10 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A TV Network's Pilot Season* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Flags as the control plane for prompts, models, and routing
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "flags as the control plane for prompts, models, and routing" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — A/B and online experiments on live determinations
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "a/b and online experiments on live determinations" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Kill switches for instant, deploy-free disablement
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "kill switches for instant, deploy-free disablement" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - A/B test stopped the moment it 'looks significant' (peeking) — you ship noise as a win.
  - No kill switch, so disabling a misbehaving variant requires a full redeploy during an incident.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. An A/B test of two PA prompts hits p<0.05 in favor of treatment after one day; the team wants to ship immediately. Why hold off?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A TV Network's Pilot Season* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Feature flags decouple deploy from release — giving you kill switches and live experiments — but only disciplined, pre-committed statistics keep those experiments from shipping noise as wins.
