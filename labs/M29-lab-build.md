# M29 Lab: Build It with AI — Compliance Automation

## Objective
Implement a set of compliance controls (denial citation, no-PHI-in-logs, TAT window, reproducibility) that run on every determination, block or alert on failure, and write continuous audit evidence.

## Prerequisites
- Completed the M29 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
COMPLIANCE_CONTROLS = [
  Control("denial_cites_policy",
          test=lambda d: d.decision != "deny" or d.cites_policy_section,
          on_fail="block"),                       # guardrail, every call
  Control("no_phi_in_logs",
          test=lambda d: not phi_scan(d.log_payload), on_fail="redact+alert"),
  Control("urgent_within_window",
          test=lambda d: not d.urgent or d.tat_hours <= 72, on_fail="alert"),
  Control("reproducible",
          test=lambda d: d.bundle_fingerprint and d.trace_id, on_fail="block"),
]

def enforce(determination):
    for c in COMPLIANCE_CONTROLS:
        if not c.test(determination):
            handle(c.on_fail, determination, control=c.name)  # block/redact/alert
    audit_store.write_evidence(determination)   # continuous, queryable evidence
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Implement a set of compliance controls (denial citation, no-PHI-in-logs, TAT window, reproducibility) that run on every determination, block or alert on failure, and write continuous audit evidence. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Compliance as a once-a-year manual audit — between audits, violations accumulate undetected.
- Determinations that can't be reproduced — when a regulator asks 'why was this denied,' you have no defensible answer.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **compliance automation** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M30: Knowledge Management**, which builds on what you constructed here.
