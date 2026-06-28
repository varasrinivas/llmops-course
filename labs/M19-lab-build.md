# M19 Lab: Build It with AI — Synthetic Data & Augmentation

## Objective
Generate and validate a batch of synthetic rare-class and adversarial PA cases (using a different model than the system under test), tag provenance, and add them only to the few-shot pool.

## Prerequisites
- Completed the M19 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.synth import generate, validate

# fill a known gap: rare service type with too few real cases
cases = generate(
    spec="PA request: rare gene therapy, must require failed step-therapy",
    n=50, generator_model="different-from-system-under-test",
    seed_realism=load_real_examples("rare-therapy", k=5),
)

report = validate(cases,
    clinician_review=True,                 # realism
    distribution_ref="pa-gold",            # don't distort the mix
    pii_scan=True,                         # no accidental real PHI
)
for c in cases:
    c.provenance = "synthetic"             # always tag

# allowed: augment TRAINING/few-shot pool; NOT the held-out human gold gate
few_shot_pool.extend([c for c in cases if report.ok])
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Generate and validate a batch of synthetic rare-class and adversarial PA cases (using a different model than the system under test), tag provenance, and add them only to the few-shot pool. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Mixing unvalidated synthetic cases into the gold set — you measure against fiction and trust a wrong number.
- Generating synthetic data with the same model you're testing — it manufactures cases it already handles well.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **synthetic data & augmentation** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M20: Model Versioning & Pinning**, which builds on what you constructed here.
