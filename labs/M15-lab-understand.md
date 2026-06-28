# M15 Lab: Understand It — User Experience Monitoring

## Objective
Analyze a week of reviewer actions to compute override/edit/escalation rates by slice and identify the slice where the tool is least trusted.

## Prerequisites
- Completed module M15 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Watching How Customers Move Through a Store* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Behavioral signals: override, edit, escalation, and abandonment
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "behavioral signals: override, edit, escalation, and abandonment" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Implicit feedback as a free, high-volume quality proxy
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "implicit feedback as a free, high-volume quality proxy" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Turnaround time and the member-facing experience
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "turnaround time and the member-facing experience" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Measuring only model outputs, never reviewer behavior — you miss that nurses silently override 30% of suggestions.
  - Collecting UX signals but never feeding them back into the gold set — the same failures recur release after release.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA model's offline eval looks healthy, but nurses override its suggested determination on 28% of orthopedic cases. What does this signal, and what should you do with it?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Watching How Customers Move Through a Store* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Reviewer and member behavior — overrides, edits, escalations, turnaround — is your highest-volume honest quality signal, and its value is realized only when you feed it back into the gold set.
