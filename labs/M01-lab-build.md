# M01 Lab: Build It with AI — LLMOps vs MLOps — What's Actually Different

## Objective
Build a 'deployment fingerprint' utility that hashes model snapshot + prompt version + policy snapshot, and a CI check that fails the build whenever the fingerprint changes without an accompanying eval run.

## Prerequisites
- Completed the M01 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
# In MLOps you version weights you trained.
# In LLMOps you must PIN the snapshot you consume,
# because the provider can change it under you.
PA_CONFIG = {
    "model": "claude-sonnet-4-6",   # pin the exact snapshot
    "temperature": 0.0,              # determinism where decisions are made
    "prompt_version": "pa-policy-v7",
    "policy_snapshot": "medpol-2026-06",  # retrieved criteria are versioned too
}

def determination_fingerprint(cfg):
    # If ANY of these change, treat it as a new deployment to re-evaluate.
    import hashlib, json
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:12]

print("deployment fingerprint:", determination_fingerprint(PA_CONFIG))
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Build a 'deployment fingerprint' utility that hashes model snapshot + prompt version + policy snapshot, and a CI check that fails the build whenever the fingerprint changes without an accompanying eval run. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Reusing an accuracy-only MLOps dashboard — it misses hallucination, refusal, injection, and cost-per-call entirely.
- Treating model version as static config — a silent provider snapshot update is a deployment you didn't make.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **llmops vs mlops — what's actually different** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M02: The LLM Application Stack**, which builds on what you constructed here.
