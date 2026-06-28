# M14 Lab: Build It with AI — Distributed Tracing for LLM Pipelines

## Objective
Instrument the PA pipeline with propagated traces capturing retrieval snapshot, prompt, model, tokens, cost, and guardrail result, plus a sampling policy that keeps 100% of denials/overrides.

## Prerequisites
- Completed the M14 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.trace import start_trace, span

def determine(req):
    with start_trace("pa-determination", member=req.member_hash) as tr:
        tr.set(cpt=req.cpt, dx=req.dx, urgent=req.urgent)
        with span("retrieval") as s:
            crit = policy_index.search(req.cpt, req.dx)
            s.set(policy_snapshot=policy_index.version, n=len(crit))
        with span("model") as s:
            out = gw.complete(build_prompt(req, crit), use_case="pa")
            s.set(model=out.model, tokens=out.tokens, cost=out.cost)
        with span("guardrail") as s:
            d = validate(out); s.set(valid=d.ok, cited=d.has_citation)
        # sampling policy: always keep high-stakes outcomes
        tr.keep(full=d.decision in ("deny",) or d.overridden, else_sample=0.1)
        return d
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Instrument the PA pipeline with propagated traces capturing retrieval snapshot, prompt, model, tokens, cost, and guardrail result, plus a sampling policy that keeps 100% of denials/overrides. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Logging only the final determination — when it's wrong you can't see which layer caused it.
- Tracing 100% of traffic at full fidelity — storage costs explode and you sample nothing intelligently.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **distributed tracing for llm pipelines** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M15: User Experience Monitoring**, which builds on what you constructed here.
