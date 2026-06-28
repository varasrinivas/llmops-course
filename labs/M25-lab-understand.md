# M25 Lab: Understand It — SLOs & SLAs for LLM Applications

## Objective
Review a service's current SLOs and identify which real obligations (quality, TAT, compliance) have no SLI; flag any SLA you can't measure.

## Prerequisites
- Completed module M25 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Delivery Service's Guarantees* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — SLI vs SLO vs SLA, applied to LLM quality not just uptime
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "sli vs slo vs sla, applied to llm quality not just uptime" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Choosing SLIs that capture determination quality and TAT
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "choosing slis that capture determination quality and tat" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Error budgets that govern release pace
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "error budgets that govern release pace" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - SLOs only on uptime — you meet 99.9% availability while determination quality and TAT silently fail.
  - An SLA you can't measure — you've promised a turnaround you have no SLI to verify or defend.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. Your PA service reports 99.95% uptime and the team declares its SLOs met. A regulator notes urgent determinations routinely exceed the mandated 72-hour window. What was the SLO design failure?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Delivery Service's Guarantees* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Define SLOs on determination quality and turnaround — not just uptime — with error budgets that govern release pace and regulatory TAT as a hard SLA you can measure and defend.
