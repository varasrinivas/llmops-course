# M06 Lab: Build It with AI — Regression Testing for LLM Apps

## Objective
Build a CI regression gate that diffs against a versioned baseline using exact-match on decisions and semantic match on rationales, with configurable tolerance bands.

## Prerequisites
- Completed the M06 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
# Run in CI on every prompt/model/policy change.
baseline = load_baseline("evals/baseline-v7.json")
current  = suite.run(model="claude-sonnet-4-6", prompt="pa-policy-v8")

diff = compare(baseline, current,
    decision_match="exact",           # structured decision must match
    rationale_match="semantic",       # embedding sim > 0.85 OR judge-equiv
)

# Tolerance bands -> deterministic pass/fail for the merge gate
assert diff.overall_drop <= 0.01, f"agreement dropped {diff.overall_drop:.1%}"
assert diff.worst_slice_drop <= 0.03, f"slice regressed: {diff.worst_slice}"
assert not diff.newly_broken, f"these cases newly fail: {diff.newly_broken}"

# Domain-explicit guard: the oncology prompt fix must NOT regress
# deny-recall on other specialties (the silent cross-specialty regression).
for specialty in ["cardiology", "oncology", "behavioral_health"]:
    assert diff.slice_metric(specialty, "deny_recall") >= baseline.slice_metric(
        specialty, "deny_recall"), f"deny-recall regressed on {specialty}"
print("Regression gate PASSED", diff.summary())
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Build a CI regression gate that diffs against a versioned baseline using exact-match on decisions and semantic match on rationales, with configurable tolerance bands. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Only testing the case you just fixed — the fix silently breaks ten others you never re-ran.
- Exact-string assertions on non-deterministic output — the suite is so flaky everyone disables it.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **regression testing for llm apps** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M07: Adversarial Testing & Red-Teaming**, which builds on what you constructed here.
