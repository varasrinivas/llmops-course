# M10 Lab: Build It with AI — Feature Flags & Experimentation

## Objective
Add a flag layer to the PA pipeline that supports per-cohort model/prompt selection, a kill switch, and an experiment harness enforcing a pre-committed sample size.

## Prerequisites
- Completed the M10 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
exp = Experiment(
    name="retrieval-strategy-v8",
    arms={"control":"bm25-policy", "treatment":"hybrid-policy"},
    primary="reviewer_agreement",
    guardrails=["override_rate","cost_per_call"],
    min_n=4000,                 # fixed in advance; no peeking before this
    alpha=0.05,
)

def determine(req):
    arm = exp.assign(req.member_id)          # stable hashing per member
    strat = exp.arms[arm]
    return run_with_retrieval(req, strategy=strat)

result = exp.analyze()        # only valid at/after min_n
if result.significant and result.guardrails_ok:
    flags.set("retrieval-strategy", "hybrid-policy")   # promote
else:
    flags.kill("retrieval-strategy-v8")                # instant rollback
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Add a flag layer to the PA pipeline that supports per-cohort model/prompt selection, a kill switch, and an experiment harness enforcing a pre-committed sample size. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- A/B test stopped the moment it 'looks significant' (peeking) — you ship noise as a win.
- No kill switch, so disabling a misbehaving variant requires a full redeploy during an incident.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **feature flags & experimentation** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M11: Rollback & Recovery**, which builds on what you constructed here.
