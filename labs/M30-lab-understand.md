# M30 Lab: Understand It — Knowledge Management

## Objective
Review a past postmortem and check whether it produced durable artifacts (alert, test, guardrail, runbook) or just a filed document; identify what would have prevented a recurrence.

## Prerequisites
- Completed module M30 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Hospital Morbidity & Mortality Conferences* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Blameless postmortems and the institutional memory they build
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "blameless postmortems and the institutional memory they build" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — From incident to durable artifact: runbook, test, guardrail
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "from incident to durable artifact: runbook, test, guardrail" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Decision records for prompts, models, and policy choices
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "decision records for prompts, models, and policy choices" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Blameful postmortems — people hide mistakes, the real causes never surface, and the same incident recurs.
  - Lessons that live in someone's head or a Slack thread — they vanish when that person leaves or the thread scrolls away.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. After a serious PA incident, the team holds a postmortem, writes a doc, and files it. Six months later a nearly identical incident recurs. What did knowledge management miss?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Hospital Morbidity & Mortality Conferences* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Convert every incident and decision into durable artifacts and searchable records through blameless postmortems — so the team's competence compounds and the same mistake can't recur after someone leaves.
