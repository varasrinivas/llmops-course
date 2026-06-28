# M24 Lab: Build It with AI — LLM Failure Modes Taxonomy

## Objective
Implement a failure classifier that tags each production outcome with its families and severity and routes it to the right owner and runbook.

## Prerequisites
- Completed the M24 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
FAILURE_FAMILIES = {
  "hallucination": lambda o: o.cited_criterion not in valid_criteria(o.case),
  "refusal":       lambda o: o.is_refusal and o.case.is_legitimate,
  "format":        lambda o: not o.schema_valid,
  "injection":     lambda o: injection_markers(o.case.clinical_note),
  "latency":       lambda o: o.latency_ms > SLA_MS,
}

def classify(outcome):
    hits = [name for name, test in FAILURE_FAMILIES.items() if test(outcome)]
    sev  = severity(hits, member_impact=outcome.case.urgent,
                          compliance=outcome.decision == "deny")
    return {"families": hits, "severity": sev,
            "owner": OWNERS[hits[0]] if hits else None,
            "runbook": RUNBOOKS.get(hits[0] if hits else None)}
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Implement a failure classifier that tags each production outcome with its families and severity and routes it to the right owner and runbook. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Treating every incident as a novel mystery — no taxonomy means no pattern, no prevention, slow response.
- Classifying by symptom not cause — 'the model is wrong' lumps hallucination, drift, and injection into one useless bucket.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **llm failure modes taxonomy** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M25: SLOs & SLAs for LLM Applications**, which builds on what you constructed here.
