# M05 Lab: Build It with AI — LLM-as-Judge

## Objective
Write a rubric-based judge for PA rationales, add order randomization and a cross-family judge model, and build a calibration harness that blocks use until kappa exceeds a threshold.

## Prerequisites
- Completed the M05 "Understand It" lab
- Claude API access (or Claude.ai) and Python 3.10+
- The PA LLMOps sandbox from M00 (eval suite + tracing + feedback store)

## The Build (35–45 min)

### Step 1: Scaffold from the module's reference
Start from the operational-tooling pattern introduced in the module:

```python
JUDGE_RUBRIC = '''Score the PA rationale 1-5 on EACH dimension. Return JSON.
- criterion_correct: cites the right medical-policy criterion for this CPT/dx
- no_fabrication: invents no policy rule that isn't in the provided criteria
- clinical_soundness: reasoning matches the documented clinical facts
Return: {"criterion_correct":n,"no_fabrication":n,"clinical_soundness":n}'''

def judge(case, rationale, criteria):
    msg = f"CRITERIA:\n{criteria}\n\nCASE:\n{case}\n\nRATIONALE:\n{rationale}"
    # different family than the generator to avoid self-preference
    return judge_client.complete(JUDGE_RUBRIC + msg, model="judge-model-x").json()

# VALIDATE the judge before trusting it:
human = load_human_scores("evals/judge-calibration-80.json")
agreement = correlate(human, [judge(*c) for c in human.cases])
assert agreement.kappa > 0.7, "Judge not calibrated to humans — do not deploy"
```

Use Claude to adapt it to your environment:
> "Generate a starter implementation for a prior-authorization (PA) determination pipeline that accomplishes: Write a rubric-based judge for PA rationales, add order randomization and a cross-family judge model, and build a calibration harness that blocks use until kappa exceeds a threshold. Use Python, the PA domain (member, CPT/HCPCS, ICD-10, clinical notes, approve/deny/pend, reviewer overrides), pin model 'claude-sonnet-4-6', and return runnable, commented code."

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
- Trusting judge scores that were never validated against human labels — you scale a bias instead of catching it.
- Judging with the same model that generated the answer — self-preference inflates the grade.
- Ask Claude: *"Review this for the failure modes above and suggest the smallest changes that close them."*
- **Expected output:** a short note listing each failure mode and how your build now guards against it.

## Deliverable
A runnable artifact (script or module) that implements **llm-as-judge** for the PA pipeline, with tests/checks and a one-paragraph README describing how it guards against the module's anti-patterns.

## Stretch Goals
- Wire the artifact into the PA CI/CD gates (M08) so it runs on every change.
- Emit its key signal to the monitoring panel (M12) and alert on a threshold breach.

## Connection to Next Module
This prepares you for **M06: Regression Testing for LLM Apps**, which builds on what you constructed here.
