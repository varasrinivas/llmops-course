# M23 Lab: Build It with AI — Model Deprecation & Sunset

## Objective
Write a sunset playbook and tooling that inventories all usages of a snapshot, drives staged migration, and asserts zero remaining usage before the EOL date.

## Prerequisites
- Completed the M23 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
def sunset_plan(deprecated_snapshot, eol_date):
    # 1. find every place it's used (code + live stamps + jobs)
    usages = {
      "code_refs":   grep_repo(deprecated_snapshot),
      "live_stamps": audit_log.count(model_snapshot=deprecated_snapshot, window="30d"),
      "batch_jobs":  scheduler.jobs_using(deprecated_snapshot),
      "fallbacks":   gateway.fallbacks_referencing(deprecated_snapshot),
    }
    # 2. migrate each via the staged playbook (M21), gated (M06), canaried (M09)
    # 3. verify zero remaining usage BEFORE the EOL date
    remaining = audit_log.count(model_snapshot=deprecated_snapshot, window="24h")
    assert remaining == 0, f"{remaining} determinations still on dead model!"
    return {"eol": eol_date, "usages": usages, "clear": remaining == 0}
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Write a sunset playbook and tooling that inventories all usages of a snapshot, drives staged migration, and asserts zero remaining usage before the EOL date. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Ignoring deprecation notices until the model returns errors in production — now it's a 2am forced migration with no eval.
- No inventory of where a model is used — you migrate the obvious service and miss the batch job still calling the dead snapshot.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **model deprecation & sunset** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M24: LLM Failure Modes Taxonomy**, which builds on what you constructed here.
