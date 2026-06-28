# M29 Lab: Understand It — Compliance Automation

## Objective
Take three real PA compliance requirements and assess whether each is enforced automatically per determination or relies on manual process; rate the exposure.

## Prerequisites
- Completed module M29 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Modern Car Safety Systems* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Encoding policy as automated, testable controls
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "encoding policy as automated, testable controls" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Audit trails: reproducing any determination on demand
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "audit trails: reproducing any determination on demand" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — PHI handling, access control, and data retention
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "phi handling, access control, and data retention" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Compliance as a once-a-year manual audit — between audits, violations accumulate undetected.
  - Determinations that can't be reproduced — when a regulator asks 'why was this denied,' you have no defensible answer.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A regulator audits a denial from 8 months ago and asks you to show exactly how it was decided. Compliance automation should have ensured what?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Modern Car Safety Systems* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Encode regulatory requirements as automated controls that run on every determination and persist reproducible audit evidence continuously — so compliance is built-in and always-on, not an annual scramble.
