# M25 Lab: Build It with AI — SLOs & SLAs for LLM Applications

## Objective
Define SLIs/SLOs for the PA pipeline covering agreement, turnaround, and schema validity, implement an error-budget calculation, and wire it to gate release pace.

## Prerequisites
- Completed the M25 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
SLOs = {
  "reviewer_agreement": {"target": 0.90, "window": "30d"},
  "tat_urgent_hours":   {"target_p95": 48, "window": "7d"},   # regulatory-anchored
  "schema_valid":       {"target": 0.995, "window": "7d"},
}

def error_budget_status(slo, sli_value):
    target = slo["target"]
    budget_used = max(0, target - sli_value) / (1 - target)
    return budget_used        # >1.0 means SLO breached

# Release pace governed by remaining budget
if error_budget_status(SLOs["reviewer_agreement"], current_agreement) > 0.75:
    freeze_risky_releases("agreement error budget nearly exhausted")
else:
    allow_canary_releases()
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Define SLIs/SLOs for the PA pipeline covering agreement, turnaround, and schema validity, implement an error-budget calculation, and wire it to gate release pace. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- SLOs only on uptime — you meet 99.9% availability while determination quality and TAT silently fail.
- An SLA you can't measure — you've promised a turnaround you have no SLI to verify or defend.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **slos & slas for llm applications** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M26: Runbooks & On-Call**, which builds on what you constructed here.
