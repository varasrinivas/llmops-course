# M07 Lab: Understand It — Adversarial Testing & Red-Teaming

## Objective
Take a working PA prompt and attempt three injection attacks via the clinical-note field; document which succeed and why the prompt structure allowed it.

## Prerequisites
- Completed module M07 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Banks Hiring Burglars* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Prompt injection via untrusted clinical documents
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "prompt injection via untrusted clinical documents" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Jailbreaks that coerce inappropriate approvals or denials
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "jailbreaks that coerce inappropriate approvals or denials" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — PHI exfiltration and policy-bypass attacks
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "phi exfiltration and policy-bypass attacks" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Treating uploaded clinical documents as trusted text the model can obey — an injected line flips a denial to an approval.
  - One-time red-team at launch, never re-run — new attacks and model updates reopen old holes.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA pipeline reads clinical notes faxed by provider offices and feeds them into the model's context. What is the core security mistake to avoid?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Banks Hiring Burglars* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Treat every document the PA pipeline ingests as hostile and run an automated adversarial suite continuously — because injection and PHI-exfiltration are compliance incidents, not edge cases.
