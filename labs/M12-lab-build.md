# M12 Lab: Build It with AI — LLM-Specific Metrics

## Objective
Define a full PA metrics panel with the four families, mark leading vs lagging metrics, and configure alert thresholds tied to regulatory TAT and quality floors.

## Prerequisites
- Completed the M12 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
from llmops.metrics import Panel, Metric

panel = Panel("pa-determination")
# Quality
panel.add(Metric("reviewer_agreement", kind="quality", window="1h", alert="<0.88"))
panel.add(Metric("override_rate",       kind="quality", window="1h", alert=">0.12"))   # leading
panel.add(Metric("appeal_overturn",     kind="quality", window="7d"))                  # lagging
# Cost
panel.add(Metric("cost_per_call_usd",   kind="cost",    window="1h", alert=">0.012"))
# Latency / turnaround
panel.add(Metric("tat_hours_urgent",    kind="latency", window="1h", alert=">48"))     # regulatory
panel.add(Metric("p95_latency_ms",      kind="latency", window="5m", alert=">4000"))
# Safety / compliance
panel.add(Metric("schema_invalid_rate", kind="safety",  window="5m", alert=">0.005"))
panel.add(Metric("citation_present",    kind="safety",  window="1h", alert="<0.99"))
panel.emit_to("dashboards/pa")
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Define a full PA metrics panel with the four families, mark leading vs lagging metrics, and configure alert thresholds tied to regulatory TAT and quality floors. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Monitoring only infra (uptime, QPS) — the service is 'up' while determination quality collapses unseen.
- Tracking only lagging quality (appeals overturned) — you learn about a regression weeks after it shipped.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **llm-specific metrics** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M13: Quality Drift Detection**, which builds on what you constructed here.
