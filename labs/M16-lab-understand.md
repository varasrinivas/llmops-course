# M16 Lab: Understand It — Human Feedback Collection

## Objective
Evaluate an existing feedback mechanism for friction and information content; estimate what fraction of real corrections it actually captures and why.

## Prerequisites
- Completed module M16 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Hotel Comment Cards* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Explicit vs implicit feedback, and why explicit is rare
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "explicit vs implicit feedback, and why explicit is rare" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Capturing the structured correction, not just a thumbs-down
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "capturing the structured correction, not just a thumbs-down" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Reducing reviewer friction so feedback gets given
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "reducing reviewer friction so feedback gets given" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Capturing only a binary thumbs-down — you know something was wrong but not what the right answer was.
  - A feedback flow so clunky reviewers skip it — you collect 2% of the corrections happening in reality.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. You add a thumbs-up/down to the PA tool and get few responses; the data that arrives is just 'down'. What's the more effective design?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Hotel Comment Cards* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Collect feedback as a structured, provenance-tagged byproduct of the reviewer's existing workflow — because a thumbs-down isn't a label, and a chore won't get done.
