# M13 Lab: Build It with AI — Quality Drift Detection

## Objective
Build a drift detector combining input distribution tests, embedding shift, and proxy-quality signals, with a corroboration-and-sustained rule to suppress false alarms.

## Prerequisites
- Completed the M13 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.drift import PSI, EmbeddingShift, ProxyQuality

baseline = load_baseline("drift/pa-baseline.json")   # frozen reference window

def check_drift(window):
    signals = {
      "input_psi":   PSI(baseline.features, window.features),       # input drift
      "emb_shift":   EmbeddingShift(baseline.note_emb, window.note_emb),
      "override":    ProxyQuality(window.override_rate, baseline.override_rate),
      "judge_drop":  ProxyQuality(window.judge_score, baseline.judge_score),
    }
    # require >=2 corroborating signals + sustained over N windows -> low noise
    firing = [k for k,v in signals.items() if v.exceeds_threshold()]
    if len(firing) >= 2 and sustained(firing, n=3):
        alert_drift(firing, signals)
    return signals
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Build a drift detector combining input distribution tests, embedding shift, and proxy-quality signals, with a corroboration-and-sustained rule to suppress false alarms. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Waiting for labeled outcomes to confirm drift — by then it's months old and expensive.
- Drift alarms so twitchy they fire on every Monday-morning volume bump — the team mutes them and misses the real one.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **quality drift detection** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M14: Distributed Tracing for LLM Pipelines**, which builds on what you constructed here.
