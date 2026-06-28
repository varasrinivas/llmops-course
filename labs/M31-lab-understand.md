# M31 Lab: Understand It — Capstone — Operating the PA Pipeline

## Objective
Walk through the simulated week and, at each event, identify which tracks interact and where the seams between them create risk; produce an operating-readiness assessment.

## Prerequisites
- Completed module M31 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *Running the Restaurant for a Week* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Wiring all eight tracks into one operating system
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "wiring all eight tracks into one operating system" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Handling a simulated week: a drift event, an incident, a migration, an audit
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "handling a simulated week: a drift event, an incident, a migration, an audit" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Balancing quality, cost, reliability, and compliance under pressure
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "balancing quality, cost, reliability, and compliance under pressure" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Treating the tracks as separate checklists — under a real incident the seams between eval, rollback, and compliance are where things break.
  - Optimizing one dimension (cost) until another (quality or compliance) silently fails — operations is balancing all of them at once.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Mid-capstone, an auto-deny spike hits during an active model migration, and a compliance audit request lands the same hour. What does this scenario test that single-track practice does not?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *Running the Restaurant for a Week* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
LLMOps mastery is operating all eight tracks as one system under real pressure — balancing quality, cost, reliability, and compliance simultaneously — so the pipeline stays trustworthy through drift, incidents, migrations, and audits alike.
