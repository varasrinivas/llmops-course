# M26 Lab: Understand It — Runbooks & On-Call

## Objective
Take a past incident's timeline and write the runbook that would have shortened it; identify which step was improvised and cost the most time.

## Prerequisites
- Completed module M26 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Fire Department Protocols* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Anatomy of a good runbook: detect, decide, act, verify, communicate
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "anatomy of a good runbook: detect, decide, act, verify, communicate" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — On-call rotation, escalation paths, and severity-based response
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "on-call rotation, escalation paths, and severity-based response" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Runbooks for the LLM failure families
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "runbooks for the llm failure families" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - No runbooks, so every incident depends on whoever happens to be awake remembering the right steps.
  - Runbooks written once and never rehearsed — they reference a dashboard that moved and a flag that was renamed.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. It's 2am and the PA auto-deny rate has doubled. Your team has dashboards but no runbooks. What's the core operational gap, and the fix?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Fire Department Protocols* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Codify incident response as rehearsed, executable runbooks — detect, decide, act, verify, communicate — so a 2am responder follows a drilled protocol instead of improvising while members are harmed.
