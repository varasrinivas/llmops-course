# M17 Lab: Understand It — Data Curation & Annotation

## Objective
Audit an existing dataset for selection bias, label provenance, and PHI handling; identify what makes it untrustworthy as a gold set.

## Prerequisites
- Completed module M17 content
- Access to a Prior Authorization (PA) determination pipeline and its logs/dashboards — or use the course PA sandbox from M00 as the worked example
- No code required for this lab; you are auditing and reasoning

## Setup (5 min)
1. Open the PA sandbox (or your pipeline) and confirm you can see recent determinations with their inputs (member, CPT/HCPCS, ICD-10, clinical notes) and outputs (approve / deny / pend).
2. Have the module's analogy in mind — *A Museum's Acquisition Process* — you will map your findings back to it.

## Exercise (25 min)

### Step 1: Observe — Curation as selection: what to keep, drop, and prioritize
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "curation as selection: what to keep, drop, and prioritize" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 2: Analyze — Annotation guidelines and inter-annotator agreement
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "annotation guidelines and inter-annotator agreement" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.
### Step 3: Quantify — Adjudicating disagreement with expert review
- **What to do:** In the PA sandbox (or your own pipeline), find where this shows up for real auth requests, and pull a representative sample.
- **What to observe:** how "adjudicating disagreement with expert review" actually behaves on production determinations (approve / deny / pend) across a few service types.
- **Expected output:** a short table or note capturing what you saw — and at least one case where it is weaker than you assumed.

### Step 4: Hunt for the anti-patterns
Look specifically for the failure signatures this module warns about:
  - Dumping all production logs into 'the dataset' unfiltered — you train and evaluate on noise and mislabels.
  - One annotator, no guidelines — labels are inconsistent and no one can trust the gold set.
- **Expected output:** a yes/no for each, with one concrete example or the reason it is not happening.

## Reflection Questions
1. A teammate proposes building the new gold set by exporting all 80,000 of last quarter's PA logs and using the original model suggestions as labels. What's wrong?
2. What would change in your findings if the case mix (service types, urgency, or volume) shifted next quarter?
3. How does what you observed map onto the *A Museum's Acquisition Process* analogy — which part of that everyday system is strong, and which is missing?

## Key Insight
Curate by selecting a stratified sample and annotating it with guideline-driven, multi-annotator, expert-adjudicated review — because a small trustworthy dataset beats a large noisy one for both eval and tuning.
