# M20 Lab: Build It with AI — Model Versioning & Pinning

## Objective
Refactor the PA pipeline to pin an exact snapshot, stamp model+prompt+policy versions on every determination, and gate any version bump through regression + canary.

## Prerequisites
- Completed the M20 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
# Pin the exact snapshot; never target a floating alias in production.
PINNED = "claude-sonnet-4-6"   # exact snapshot id, reviewed & evaluated

def determine(req):
    out = client.complete(build_prompt(req), model=PINNED, temperature=0.0)
    record_determination(
        case_id=req.id,
        decision=out.decision,
        model_snapshot=PINNED,           # the 'lot number'
        prompt_version=PROMPT_VERSION,
        policy_snapshot=POLICY_VERSION,
    )
    return out

# A version bump is a release, not a config tweak:
def bump_model(new_snapshot):
    report = regression_gate(new_snapshot, baseline=PINNED)   # M06
    assert report.passed, report.summary
    return canary_rollout(new_snapshot)                       # M09
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Refactor the PA pipeline to pin an exact snapshot, stamp model+prompt+policy versions on every determination, and gate any version bump through regression + canary. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Pointing at a floating alias like 'latest' — the provider updates it and your behavior shifts with no PR and no rollback.
- Not recording the model snapshot per determination — during an appeal you can't say which model decided.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **model versioning & pinning** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M21: Model Migration**, which builds on what you constructed here.
