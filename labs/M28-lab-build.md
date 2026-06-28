# M28 Lab: Build It with AI — Cost Optimization at Scale

## Objective
Implement cost attribution at the gateway, apply caching/compression/routing levers, and gate each change through a regression run with a deny-recall floor before keeping it.

## Prerequisites
- Completed the M28 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
# Attribute every determination's cost (via the gateway seam)
cost_report = cost_sink.group_by(["service_line","prompt_version"], window="30d")
print(cost_report.top_spenders(10))

# Apply a lever, but gate on quality before keeping it
candidate = current_bundle().with_changes(
    cache="policy_retrieval",          # cache stable criteria lookups
    prompt="compressed-v9",            # trim redundant instructions
    routing="cheap_first_cascade",     # M22
)
q = regression_gate(candidate, baseline=current_bundle())   # M06
c = cost_estimate(candidate)
if q.passed and q.deny_recall >= 0.90 and c.per_call <= 0.012:
    promote(candidate)
else:
    reject("cost win not worth quality/regression risk", q, c)
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Implement cost attribution at the gateway, apply caching/compression/routing levers, and gate each change through a regression run with a deny-recall floor before keeping it. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Cutting cost by truncating context or downgrading every call — quality drops and appeal costs dwarf the savings.
- No per-determination cost attribution — you can't tell which service line or prompt is burning the budget.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **cost optimization at scale** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M29: Compliance Automation**, which builds on what you constructed here.
