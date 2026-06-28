# M11 Lab: Build It with AI — Rollback & Recovery

## Objective
Write and rehearse a rollback runbook that flips to the last known-good bundle and runs a remediation job to re-adjudicate determinations issued by the bad version.

## Prerequisites
- Completed the M11 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
def emergency_rollback(reason):
    last_good = registry.last_known_good("pa-bundle")
    flags.set("pa-bundle", last_good.fingerprint)      # seconds, no redeploy
    alert(f"ROLLBACK to {last_good.fingerprint}: {reason}")
    wait_for_metrics_recovery(timeout="10m")

    # Remediate state created by the bad version
    bad = audit_log.determinations(bundle="pa-bundle-v8",
                                   since=v8_release_time)
    for d in bad:
        redo = determine(d.request, bundle=last_good.fingerprint)
        if redo.decision != d.decision:
            reopen_case(d, corrected=redo, notify=True)   # re-adjudicate
    return {"rolled_back_to": last_good.fingerprint,
            "reexamined": len(bad)}
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Write and rehearse a rollback runbook that flips to the last known-good bundle and runs a remediation job to re-adjudicate determinations issued by the bad version. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Trying to 'roll forward' a hotfix during an active incident — you ship a second, unevaluated change on top of the first.
- No plan for the bad determinations already issued — you roll back the code but leave wrong denials in members' records.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **rollback & recovery** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M12: LLM-Specific Metrics**, which builds on what you constructed here.
