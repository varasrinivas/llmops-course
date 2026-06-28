# M27 Lab: Build It with AI — Chaos Engineering for AI

## Objective
Design and run a blast-radius-limited chaos experiment that injects a provider outage and degraded retrieval, observes guardrails and runbook behavior, and files fixes for every gap found.

## Prerequisites
- Completed the M27 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
experiment = ChaosExperiment(
  hypothesis="primary provider outage -> failover < 30s, no member impact",
  blast_radius={"env":"prod","cohort":"0.5%","kill_switch":True},
  inject=Fault("provider_500", target="primary", duration="5m"),
  observe=["failover_time_s","schema_invalid_rate","tat_breaches","override_rate"],
  abort_if="member_impact > 0 or override_rate > baseline + 0.05",
)
result = experiment.run()
for gap in result.gaps:
    file_followup(gap)        # -> harden guardrail / fix runbook / add alert
assert result.hypothesis_held, result.summary
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Design and run a blast-radius-limited chaos experiment that injects a provider outage and degraded retrieval, observes guardrails and runbook behavior, and files fixes for every gap found. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Assuming the fallback provider works because it's configured — it was never exercised and fails on first real use.
- Running chaos in production with no blast-radius limit — your drill becomes the incident.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **chaos engineering for ai** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M28: Cost Optimization at Scale**, which builds on what you constructed here.
