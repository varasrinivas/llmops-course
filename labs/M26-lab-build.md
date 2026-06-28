# M26 Lab: Build It with AI — Runbooks & On-Call

## Objective
Author executable runbooks for the top LLM failure families (auto-deny spike, schema-invalid surge, injection detection) with escalation paths, and link each to its taxonomy entry.

## Prerequisites
- Completed the M26 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
RUNBOOK_auto_deny_spike = Runbook(
  trigger="alert:auto_deny_rate > baseline + 0.05",
  severity="SEV1",
  steps=[
    Step("detect",  check="confirm spike on dashboards/pa, not a data artifact"),
    Step("decide",  rule="if sustained >10m -> rollback; else investigate"),
    Step("act",     run=lambda: emergency_rollback("auto-deny spike")),  # M11
    Step("verify",  check="auto_deny_rate back to baseline within 10m"),
    Step("remediate", run=lambda: reexamine_since(incident_start)),       # state
    Step("communicate", notify=["medical_director","compliance","status_page"]),
  ],
  escalation=["oncall_eng","senior_eng","medical_director"],
)
register(RUNBOOK_auto_deny_spike)   # linked from the M24 taxonomy
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Author executable runbooks for the top LLM failure families (auto-deny spike, schema-invalid surge, injection detection) with escalation paths, and link each to its taxonomy entry. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- No runbooks, so every incident depends on whoever happens to be awake remembering the right steps.
- Runbooks written once and never rehearsed — they reference a dashboard that moved and a flag that was renamed.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **runbooks & on-call** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M27: Chaos Engineering for AI**, which builds on what you constructed here.
