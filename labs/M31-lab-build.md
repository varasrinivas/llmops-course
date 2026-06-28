# M31 Lab: Build It with AI — Capstone — Operating the PA Pipeline

## Objective
Wire the full PA pipeline operating loop end-to-end (monitor → drift → flywheel → migration → incident → compliance), run the simulated week, and produce the operational evidence report demonstrating the pipeline is trustworthy.

## Prerequisites
- Completed the M31 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
def operate_pa_pipeline(day):
    # T4 monitor -> T5 feedback / T7 incident
    health = monitor.snapshot()
    if drift.check(health).firing:           # T4/T13
        diagnose_and_pin_snapshot()          # T6/M20
    if health.auto_deny_rate > THRESH:       # T7
        run_runbook("auto_deny_spike")       # -> rollback (M11) + remediate

    # T5 flywheel: verified overrides -> gold set -> gated improvement
    if day.weekly:
        candidate = flywheel_turn()          # M18
        if candidate and regression_gate(candidate).passed:   # T2/T3
            canary_rollout(candidate)        # M09

    # T6 lifecycle
    for notice in provider.deprecations():   # M23
        plan_and_stage_migration(notice)     # M21

    # T8 governance: always-on
    enforce_compliance_controls()            # M29
    return operational_evidence_report()     # dashboards+traces+evals+audit

```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Wire the full PA pipeline operating loop end-to-end (monitor → drift → flywheel → migration → incident → compliance), run the simulated week, and produce the operational evidence report demonstrating the pipeline is trustworthy. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Treating the tracks as separate checklists — under a real incident the seams between eval, rollback, and compliance are where things break.
- Optimizing one dimension (cost) until another (quality or compliance) silently fails — operations is balancing all of them at once.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **capstone — operating the pa pipeline** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This is the capstone — it ties together everything you built across the eight tracks.
