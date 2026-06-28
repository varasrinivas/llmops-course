# M18 Lab: Build It with AI — The Data Flywheel

## Objective
Implement a flywheel job that promotes verified corrections into the gold set, builds an improved bundle via retrieval/few-shot/routing (no retraining), and gates it through regression before release.

## Prerequisites
- Completed the M18 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
def flywheel_turn(window="30d"):
    # capture -> curate: only reviewer-verified PA determination overrides
    corrections = load_corrections(window, verified=True,
                                   kinds=["decision_override","rationale_edit"])
    new_cases   = curate(corrections, stratify=["service_type","decision"])  # M17
    gold.extend(new_cases, version="auto")                  # grow PA gold set

    # improve WITHOUT retraining: retrieval + few-shot + routing
    candidate = build_bundle(
        few_shots = select_hard_examples(new_cases, k=8),
        retrieval = tune_policy_retrieval(corrections),
        routing   = route_low_confidence_to("stronger-model"),
    )
    # validate before serving -> never spin backwards
    report = regression_gate(candidate, baseline=current_bundle())
    if report.passed:
        promote(candidate)
    return {"new_gold": len(new_cases), "velocity_days": report.cycle_days}
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Implement a flywheel job that promotes verified corrections into the gold set, builds an improved bundle via retrieval/few-shot/routing (no retraining), and gates it through regression before release. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- A feedback loop that only sees its own outputs — the model trains on its mistakes and confidently entrenches them.
- Capturing feedback that never reaches 'improve' — a flywheel with no axle, spinning effort with no momentum.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **the data flywheel** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M19: Synthetic Data & Augmentation**, which builds on what you constructed here.
