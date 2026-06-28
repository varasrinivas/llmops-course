# M28 Lab: Understand It — Cost Optimization at Scale

## Objective
Attribute a month of PA spend by service line and prompt version; identify the top cost driver and whether it's waste or genuine workload.

## Prerequisites
- Completed module M28 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Factory Efficiency Engineering* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — The cost drivers: tokens, model tier, retries, and traffic shape
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "the cost drivers: tokens, model tier, retries, and traffic shape" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Caching, prompt compression, and routing as cost levers
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "caching, prompt compression, and routing as cost levers" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Attributing cost per determination, team, and service line
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "attributing cost per determination, team, and service line" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Cutting cost by truncating context or downgrading every call — quality drops and appeal costs dwarf the savings.
  - No per-determination cost attribution — you can't tell which service line or prompt is burning the budget.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. To hit a budget, a proposal truncates clinical notes to half length and downgrades all PA calls to the cheapest model. Why is this the wrong kind of cost cut?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Factory Efficiency Engineering* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Cut cost by trimming waste — caching, compression, routing — under a quality guardrail, because a 'cheap' wrong denial costs far more in appeals and harm than the tokens it saved.
