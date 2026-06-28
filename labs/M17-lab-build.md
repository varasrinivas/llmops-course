# M17 Lab: Build It with AI — Data Curation & Annotation

## Objective
Build a curation pipeline that stratified-samples production logs, runs a two-annotator flow with adjudication, computes inter-annotator agreement, and publishes a versioned, lineage-tagged dataset.

## Prerequisites
- Completed the M17 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.data import Curator, Dataset

cur = Curator(source="prod-logs", pii_policy="deidentify")
sample = cur.select(
    stratify_by=["service_type","decision","difficulty"],
    target_per_cell=20, drop_duplicates=True, drop_corrupt=True,
)

ann = sample.annotate(
    guideline="guidelines/pa-labeling-v3.md",
    annotators=2, adjudicator_role="medical_director",
)
print("inter-annotator kappa:", ann.kappa)        # trust check
assert ann.kappa > 0.7, "guidelines too ambiguous — revise before using"

ds = Dataset.publish(ann, name="pa-gold", version="v8",
    lineage={"logs":"2026-05","guideline":"v3"}, access="phi-restricted")
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Build a curation pipeline that stratified-samples production logs, runs a two-annotator flow with adjudication, computes inter-annotator agreement, and publishes a versioned, lineage-tagged dataset. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Dumping all production logs into 'the dataset' unfiltered — you train and evaluate on noise and mislabels.
- One annotator, no guidelines — labels are inconsistent and no one can trust the gold set.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **data curation & annotation** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M18: The Data Flywheel**, which builds on what you constructed here.
