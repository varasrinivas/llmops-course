# M16 Lab: Build It with AI — Human Feedback Collection

## Objective
Design and implement an inline structured-correction capture for the PA tool recording corrected decision, controlling criterion, reason code, and reviewer provenance.

## Prerequisites
- Completed the M16 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Correction:
    case_id: str
    bundle_fingerprint: str        # which prompt+model+policy produced it
    suggested_decision: str        # approve/deny/pend
    corrected_decision: str
    controlling_criterion: str     # the policy section that actually applied
    reason_code: str               # e.g. 'missing-clinical-doc','wrong-criterion'
    reviewer_id: str
    reviewer_role: str             # 'nurse' | 'medical_director'
    ts: datetime

def on_submit(case, suggested, final, reviewer):
    if final.decision != suggested.decision or final.rationale_edited:
        store(Correction(case.id, suggested.bundle, suggested.decision,
              final.decision, final.criterion, final.reason_code,
              reviewer.id, reviewer.role, datetime.utcnow()))
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Design and implement an inline structured-correction capture for the PA tool recording corrected decision, controlling criterion, reason code, and reviewer provenance. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Capturing only a binary thumbs-down — you know something was wrong but not what the right answer was.
- A feedback flow so clunky reviewers skip it — you collect 2% of the corrections happening in reality.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **human feedback collection** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M17: Data Curation & Annotation**, which builds on what you constructed here.
