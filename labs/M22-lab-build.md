# M22 Lab: Build It with AI — Multi-Model Strategies

## Objective
Implement a cascade router with confidence thresholds and stakes overrides, then tune the thresholds on the gold set to meet both a cost ceiling and a deny-recall floor.

## Prerequisites
- Completed the M22 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
def route_determination(req):
    if req.dollar_stakes > HIGH or req.service_type in ALWAYS_HUMAN:
        return human_queue(req)                       # stakes override

    cheap = gw.complete(prompt(req), model="fast-cheap", use_case="pa")
    if cheap.confidence >= 0.85 and cheap.schema_valid:
        return cheap                                  # bulk of traffic, low cost

    strong = gw.complete(prompt(req), model="claude-sonnet-4-6", use_case="pa")
    if strong.confidence >= 0.80:
        return strong                                 # escalate hard cases
    return human_queue(req)                           # low confidence -> human

# thresholds tuned on the gold set to hit a cost AND quality target
router_report = tune_thresholds(gold, cost_ceiling=0.012, min_deny_recall=0.90)
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Implement a cascade router with confidence thresholds and stakes overrides, then tune the thresholds on the gold set to meet both a cost ceiling and a deny-recall floor. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- One expensive model for every determination — you pay partner rates to review NDAs and blow the budget.
- Routing with no confidence signal — hard cases silently get the cheap model and quality craters on exactly the cases that matter.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **multi-model strategies** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M23: Model Deprecation & Sunset**, which builds on what you constructed here.
