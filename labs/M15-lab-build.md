# M15 Lab: Build It with AI — User Experience Monitoring

## Objective
Instrument implicit UX signal capture in the PA tool and build a weekly job that clusters overrides and promotes recurring patterns into the gold eval set.

## Prerequisites
- Completed the M15 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.ux import signal

def on_reviewer_action(case, suggested, final_action):
    if final_action.decision != suggested.decision:
        signal("override", case=case, frm=suggested.decision,
               to=final_action.decision, slice=case.service_type)
    if final_action.rationale_edited:
        signal("rationale_edit", case=case, diff=final_action.edit_distance)
    if final_action.escalated:
        signal("escalation", case=case, to="medical_director")

# Weekly: turn recurring overrides into eval cases (close the loop)
clusters = mine_signals("override", window="7d", min_cluster=20)
for c in clusters.top(10):
    add_to_gold_set(c.representative_case, label=c.majority_final_decision,
                    tag=f"ux-mined:{c.service_type}")
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Instrument implicit UX signal capture in the PA tool and build a weekly job that clusters overrides and promotes recurring patterns into the gold eval set. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

- **Expected output:** the scaffold runs end-to-end against one sample PA request without errors.

### Step 2: Extend it to real PA cases
- Wire the scaffold to a small batch of determinations (pull 10–20 from the sandbox, spanning approve / deny / pend and at least two service types).
- Iterate with Claude on anything that breaks; ask it to explain each change.
- **Expected output:** the tool produces correct, structured results across the batch.

### Step 3: Test against the domain
- Add explicit checks tied to this module's goal (e.g., assertions, thresholds, or metrics) so a regression would fail loudly.
- Include at least one hard case (a borderline determination that drives appeals).
- **Expected output:** tests pass on good input and fail clearly on a deliberately broken case.

### Step 4: Refine for the failure modes
Harden against the anti-patterns this module calls out:
- Measuring only model outputs, never reviewer behavior — you miss that nurses silently override 30% of suggestions.
- Collecting UX signals but never feeding them back into the gold set — the same failures recur release after release.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **user experience monitoring** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M16: Human Feedback Collection**, which builds on what you constructed here.
