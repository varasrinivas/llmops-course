# M04 Lab: Build It with AI — Evaluation Frameworks

## Objective
Construct a 50-case stratified PA gold set with clinician-style labels, then build a multi-metric eval run that asserts per-class recall and slices results by service type and difficulty.

## Prerequisites
- Completed the M04 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops import EvalSuite, metrics

suite = EvalSuite.load("evals/pa-gold-set.json")  # 200 nurse-labeled cases

report = suite.run(
    model="claude-sonnet-4-6",
    metrics=[
        metrics.Agreement(label="decision"),          # vs nurse determination
        metrics.PerClassRecall(classes=["approve","deny","pend"]),
        metrics.StructuralValid(schema="determination.json"),
        metrics.CitationPresent(),                     # every deny cites policy
    ],
    slice_by=["service_type","difficulty"],
)
report.assert_min("deny.recall", 0.90)   # missed denials are the costly error
report.assert_min("agreement", 0.90)
print(report.table(worst_slices=5))
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Construct a 50-case stratified PA gold set with clinician-style labels, then build a multi-metric eval run that asserts per-class recall and slices results by service type and difficulty. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- A gold set of 12 hand-picked easy cases — it certifies nothing about the real, messy case mix.
- Optimizing a single average metric while the worst-case denials (the ones that get appealed) quietly get worse.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **evaluation frameworks** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M05: LLM-as-Judge**, which builds on what you constructed here.
