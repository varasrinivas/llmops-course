# -*- coding: utf-8 -*-
"""Modules for Tracks 5-8 (M16-M31). Domain: Prior Authorization Determination Pipeline."""
from modules_t1_4 import svg_flow, svg_stack, svg_compare, svg_cycle, svg_gauge, svg_quadrant

SAGE="#8fc7a8"; BRICK="#cf6f5f"; IRIS="#9486cf"; TEAL="#3f95a8"
MODS=[]; SVGS={}

# ════════════════════════════════════════════════════════════════════
#  TRACK 5 — DATA & FEEDBACK LOOPS
# ════════════════════════════════════════════════════════════════════

MODS.append({
 "id":"M16","track":5,"title":"Human Feedback Collection",
 "subtitle":"Designing capture so the corrections you need actually get recorded",
 "icon":"\U0001F4DD","color":SAGE,
 "topics":[
   "Explicit vs implicit feedback, and why explicit is rare",
   "Capturing the structured correction, not just a thumbs-down",
   "Reducing reviewer friction so feedback gets given",
   "Provenance: who corrected what, when, and why"],
 "analogy":{"title":"Hotel Comment Cards","text":"A blank comment card gets ignored; a card that asks 'How was the room? The breakfast? The check-in?' gets filled in. The structure is what produces useful feedback. For the PA tool, a bare 'wrong' button yields noise; a capture flow that records the corrected determination, the controlling criterion, and a one-line reason yields training-grade data. Design the card and you design the data."},
 "antiPatterns":[
   "Capturing only a binary thumbs-down — you know something was wrong but not what the right answer was.",
   "A feedback flow so clunky reviewers skip it — you collect 2% of the corrections happening in reality."]})
SVGS["M16"]=svg_flow("Structured Feedback Capture",["Suggestion|model determination","Reviewer correction|decision+criterion","Reason|one line","Provenance|who/when","Store|training-grade"],SAGE,"a structured card beats a thumbs-down")
MODS[-1].update({
 "crosslinks":[{"type":"agent","label":"Agent M15 HITL"},{"type":"platform","label":"Platform M10 Feedback"}],
 "sections":[
  {"type":"content","title":"Why Explicit Feedback Is Rare — and How to Get It","body":"<p>People rarely volunteer feedback unless it's nearly free to give. A standalone 'rate this' widget on the PA tool will be ignored under reviewer workload. The trick is to capture feedback <strong>inside the work the reviewer already does</strong>: when a nurse changes the suggested decision before submitting, that action <em>is</em> the feedback — capture the before/after, the criterion they relied on, and an optional one-line reason. You get correction data as a byproduct of the job, not an extra chore.</p>"},
  {"type":"content","title":"Capture the Correction, With Provenance","body":"<p>A thumbs-down tells you something was wrong; it doesn't tell you the right answer. Useful feedback is <strong>structured</strong>: the corrected determination, the controlling policy criterion, and the reason category. Equally important is <strong>provenance</strong> — which reviewer, what role (nurse vs medical director), at what time, against which bundle. In a regulated workflow provenance is both a data-quality signal (a medical director's correction outweighs a trainee's) and an audit requirement.</p>"},
  {"type":"code","title":"A Structured Feedback Schema","language":"python","code":"from dataclasses import dataclass\nfrom datetime import datetime\n\n@dataclass\nclass Correction:\n    case_id: str\n    bundle_fingerprint: str        # which prompt+model+policy produced it\n    suggested_decision: str        # approve/deny/pend\n    corrected_decision: str\n    controlling_criterion: str     # the policy section that actually applied\n    reason_code: str               # e.g. 'missing-clinical-doc','wrong-criterion'\n    reviewer_id: str\n    reviewer_role: str             # 'nurse' | 'medical_director'\n    ts: datetime\n\ndef on_submit(case, suggested, final, reviewer):\n    if final.decision != suggested.decision or final.rationale_edited:\n        store(Correction(case.id, suggested.bundle, suggested.decision,\n              final.decision, final.criterion, final.reason_code,\n              reviewer.id, reviewer.role, datetime.utcnow()))"},
  {"type":"quiz","question":"You add a thumbs-up/down to the PA tool and get few responses; the data that arrives is just 'down'. What's the more effective design?",
   "options":["Make rating mandatory before submit","Capture the correction inline from the reviewer's existing workflow — the changed decision, the controlling criterion, and a reason — with full provenance","Email reviewers a weekly survey","Remove feedback entirely and rely on offline eval"],
   "correct":1,
   "explanation":"Bare thumbs-down is high-friction and low-information. Capturing the correction as a byproduct of the work the reviewer already does — the before/after decision, the criterion, the reason, and who made it — yields training-grade, auditable data without adding a chore. Structure the card and you get the data."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Binary-only feedback: you learn that 12% of suggestions were 'wrong' but have no corrected labels to learn from.",
   "High-friction capture: a clunky feedback modal is dismissed, so you record a tiny, biased fraction of the corrections actually occurring."]}],
 "takeaway":"Collect feedback as a structured, provenance-tagged byproduct of the reviewer's existing workflow — because a thumbs-down isn't a label, and a chore won't get done.",
 "labUnderstand":"Evaluate an existing feedback mechanism for friction and information content; estimate what fraction of real corrections it actually captures and why.",
 "labBuild":"Design and implement an inline structured-correction capture for the PA tool recording corrected decision, controlling criterion, reason code, and reviewer provenance."})

MODS.append({
 "id":"M17","track":5,"title":"Data Curation & Annotation",
 "subtitle":"Turning raw production logs into a trustworthy labeled dataset",
 "icon":"\U0001F5C2️","color":SAGE,
 "topics":[
   "Curation as selection: what to keep, drop, and prioritize",
   "Annotation guidelines and inter-annotator agreement",
   "Adjudicating disagreement with expert review",
   "Dataset versioning, lineage, and PHI handling"],
 "analogy":{"title":"A Museum's Acquisition Process","text":"A museum doesn't hang every donated painting. A committee appraises provenance, authenticates, conserves, and catalogs each piece before it enters the collection. Data curation is the same discipline: production logs are donations, and only the authenticated, well-labeled, properly cataloged cases earn a place in your gold and training sets. Curation is selection plus verification, not hoarding."},
 "antiPatterns":[
   "Dumping all production logs into 'the dataset' unfiltered — you train and evaluate on noise and mislabels.",
   "One annotator, no guidelines — labels are inconsistent and no one can trust the gold set."]})
SVGS["M17"]=svg_flow("Curation Pipeline",["Collect|prod logs","Select|stratified sample","Annotate|guideline + 2 raters","Adjudicate|expert on disagreement","Version|lineage + PHI policy"],SAGE,"selection + verification, not hoarding")
MODS[-1].update({
 "crosslinks":[{"type":"ce","label":"CE — Dataset Design"},{"type":"sdlc","label":"AI-SDLC — Data Governance"}],
 "sections":[
  {"type":"content","title":"Curation Is Selection","body":"<p>The instinct to 'use all the data' is a trap. Most production PA logs are routine approvals that teach a model nothing; the value concentrates in the hard, contested, and rare cases. Curation means <strong>deliberately selecting</strong> a stratified, balanced sample — across service types, determinations, and difficulty — and discarding duplicates and corrupt records. A curated 500-case set outperforms 50,000 unfiltered logs for both eval and any future tuning.</p>"},
  {"type":"content","title":"Annotation Quality: Guidelines and Agreement","body":"<p>A label is only as trustworthy as the process that produced it. You need written <strong>annotation guidelines</strong> (how to decide approve/deny/pend, how to pick the controlling criterion), at least <strong>two independent annotators</strong> per contested case, and a measured <strong>inter-annotator agreement</strong>. Where annotators disagree, an expert (medical director) <strong>adjudicates</strong>. Every dataset is versioned with lineage (which logs, which guidelines version) and handled under PHI policy — de-identified or access-controlled. Without this, your 'ground truth' is one person's opinion.</p>"},
  {"type":"code","title":"Curate, Annotate, Version","language":"python","code":"from llmops.data import Curator, Dataset\n\ncur = Curator(source=\"prod-logs\", pii_policy=\"deidentify\")\nsample = cur.select(\n    stratify_by=[\"service_type\",\"decision\",\"difficulty\"],\n    target_per_cell=20, drop_duplicates=True, drop_corrupt=True,\n)\n\nann = sample.annotate(\n    guideline=\"guidelines/pa-labeling-v3.md\",\n    annotators=2, adjudicator_role=\"medical_director\",\n)\nprint(\"inter-annotator kappa:\", ann.kappa)        # trust check\nassert ann.kappa > 0.7, \"guidelines too ambiguous — revise before using\"\n\nds = Dataset.publish(ann, name=\"pa-gold\", version=\"v8\",\n    lineage={\"logs\":\"2026-05\",\"guideline\":\"v3\"}, access=\"phi-restricted\")"},
  {"type":"quiz","question":"A teammate proposes building the new gold set by exporting all 80,000 of last quarter's PA logs and using the original model suggestions as labels. What's wrong?",
   "options":["80,000 is too few cases","Using the model's own suggestions as labels bakes in its errors, and unfiltered logs are mostly easy duplicates — you need stratified selection plus independent human annotation","Logs can never be used as data","The set should use 800,000 cases instead"],
   "correct":1,
   "explanation":"Labeling with the model's own outputs is circular — it canonizes the model's mistakes as 'truth'. And raw logs over-represent easy approvals. Real curation selects a stratified, deduplicated sample and labels it with guideline-driven, multi-annotator human review (adjudicated on disagreement). Selection plus verification, like a museum acquisition."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Unfiltered dump: the dataset is 90% trivial approvals and a few mislabeled records, so eval scores look great and predict nothing.",
   "Single-annotator, no guideline: labels reflect one reviewer's idiosyncrasies, agreement is unmeasured, and the gold set can't be defended."]}],
 "takeaway":"Curate by selecting a stratified sample and annotating it with guideline-driven, multi-annotator, expert-adjudicated review — because a small trustworthy dataset beats a large noisy one for both eval and tuning.",
 "labUnderstand":"Audit an existing dataset for selection bias, label provenance, and PHI handling; identify what makes it untrustworthy as a gold set.",
 "labBuild":"Build a curation pipeline that stratified-samples production logs, runs a two-annotator flow with adjudication, computes inter-annotator agreement, and publishes a versioned, lineage-tagged dataset."})

MODS.append({
 "id":"M18","track":5,"title":"The Data Flywheel",
 "subtitle":"Turning production feedback into compounding quality improvement",
 "icon":"\U0001F501","color":SAGE,
 "topics":[
   "The flywheel: serve → capture → curate → improve → serve",
   "What 'improve' means without retraining: prompts, retrieval, few-shots, routing",
   "Measuring flywheel velocity and avoiding feedback-loop bias",
   "Guarding against drift-amplifying loops"],
 "analogy":{"title":"Amazon's Virtuous Cycle","text":"More customers bring more sellers, which brings more selection and lower prices, which brings more customers — a flywheel where each turn makes the next easier. A well-run LLM app builds the same momentum: every determination produces feedback, feedback improves the system, a better system earns more usage and more feedback. The danger is spinning the wheel backwards — amplifying your own errors."},
 "antiPatterns":[
   "A feedback loop that only sees its own outputs — the model trains on its mistakes and confidently entrenches them.",
   "Capturing feedback that never reaches 'improve' — a flywheel with no axle, spinning effort with no momentum."]})
SVGS["M18"]=svg_cycle("The Data Flywheel",["Serve","Capture","Curate","Improve","Validate"],SAGE,"compounding|quality")
MODS[-1].update({
 "crosslinks":[{"type":"agent","label":"Agent M15 HITL"},{"type":"platform","label":"Platform M10 Eval"}],
 "sections":[
  {"type":"content","title":"The Loop That Compounds","body":"<p>The flywheel is: <strong>serve</strong> determinations → <strong>capture</strong> reviewer corrections (M16) → <strong>curate</strong> them into datasets (M17) → <strong>improve</strong> the system → serve better, capturing more. Each turn should make the next turn easier. For the PA pipeline 'improve' rarely means retraining a foundation model — it means promoting mined failures into the gold set, refining retrieval of policy criteria, adding targeted few-shot examples, and routing hard slices to stronger models (M22).</p>"},
  {"type":"content","title":"Don't Spin It Backwards","body":"<p>The flywheel can amplify errors. If you 'improve' using the model's own unreviewed outputs as truth, you create a <strong>feedback-loop bias</strong> that entrenches mistakes with rising confidence. The safeguards: only human-corrected (M16) and adjudicated (M17) data feeds 'improve'; every improvement passes the regression gate (M06) before release; and you measure <strong>flywheel velocity</strong> — how fast a mined failure becomes a fixed-and-validated release — as a first-class metric.</p>"},
  {"type":"code","title":"One Turn of the Flywheel","language":"python","code":"def flywheel_turn(window=\"30d\"):\n    # capture -> curate: only reviewer-verified PA determination overrides\n    corrections = load_corrections(window, verified=True,\n                                   kinds=[\"decision_override\",\"rationale_edit\"])\n    new_cases   = curate(corrections, stratify=[\"service_type\",\"decision\"])  # M17\n    gold.extend(new_cases, version=\"auto\")                  # grow PA gold set\n\n    # improve WITHOUT retraining: retrieval + few-shot + routing\n    candidate = build_bundle(\n        few_shots = select_hard_examples(new_cases, k=8),\n        retrieval = tune_policy_retrieval(corrections),\n        routing   = route_low_confidence_to(\"stronger-model\"),\n    )\n    # validate before serving -> never spin backwards\n    report = regression_gate(candidate, baseline=current_bundle())\n    if report.passed:\n        promote(candidate)\n    return {\"new_gold\": len(new_cases), \"velocity_days\": report.cycle_days}"},
  {"type":"quiz","question":"To accelerate improvement, an engineer proposes auto-adding every determination the model made with high confidence to the training/few-shot pool. Why is this risky?",
   "options":["High-confidence outputs are always correct","It creates a self-reinforcing loop: the model's own (possibly wrong) outputs become 'truth', entrenching errors with growing confidence","Few-shot pools can't be updated automatically","Confidence scores aren't computable"],
   "correct":1,
   "explanation":"Feeding the model its own unverified outputs spins the flywheel backwards — confident mistakes get canonized and compound. Only human-corrected, adjudicated data should drive 'improve', and every change must clear the regression gate before serving. Otherwise you build momentum in the wrong direction."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Self-training loop: unverified model outputs feed back as labels, errors entrench, and confidence rises as accuracy falls.",
   "Dead flywheel: feedback is captured and curated but never wired to 'improve' or release, so quality stays flat despite mounting data."]}],
 "takeaway":"A data flywheel compounds quality only when human-verified feedback drives improvement that clears the regression gate — feed it the model's own guesses and it compounds your errors instead.",
 "labUnderstand":"Map your current serve→capture→curate→improve loop and find the broken link (usually capture-with-no-improve or improve-with-no-validation); estimate flywheel velocity.",
 "labBuild":"Implement a flywheel job that promotes verified corrections into the gold set, builds an improved bundle via retrieval/few-shot/routing (no retraining), and gates it through regression before release."})

MODS.append({
 "id":"M19","track":5,"title":"Synthetic Data & Augmentation",
 "subtitle":"Generating the rare and dangerous cases your production logs lack",
 "icon":"\U0001F9EC","color":SAGE,
 "topics":[
   "When synthetic data helps: rare classes, edge cases, privacy",
   "Generating realistic PA cases without leaking real PHI",
   "Validating synthetic data so it doesn't poison your eval",
   "Augmentation vs fabrication — keeping the distribution honest"],
 "analogy":{"title":"Flight Simulators","text":"Pilots can't practice an engine fire on a real flight, so simulators generate the rare, dangerous scenarios safely and repeatedly. Synthetic data is the simulator for your PA model: you manufacture the rare service types, the adversarial notes, and the tricky edge cases that almost never appear in logs — so the model is tested on the emergencies before it meets one for real, and without exposing real patient data."},
 "antiPatterns":[
   "Mixing unvalidated synthetic cases into the gold set — you measure against fiction and trust a wrong number.",
   "Generating synthetic data with the same model you're testing — it manufactures cases it already handles well."]})
SVGS["M19"]=svg_flow("Synthetic Case Generation",["Identify gap|rare/edge class","Generate|templated + LLM","Validate|expert + realism check","Tag|synthetic provenance","Use|test set / few-shot"],SAGE,"simulate emergencies, no real PHI")
MODS[-1].update({
 "crosslinks":[{"type":"ce","label":"CE — Data Augmentation"},{"type":"platform","label":"Platform M12 Safety"}],
 "sections":[
  {"type":"content","title":"When Synthetic Data Earns Its Place","body":"<p>Production logs under-represent exactly the cases that matter most: a rare oncology regimen, a service type seen twice a year, an adversarial fax. Synthetic data fills these gaps. It also sidesteps <strong>privacy</strong>: a realistic-but-fake PA case carries no real PHI, so it's safe to share across teams and store loosely. The three best uses are rare-class coverage, edge/adversarial cases (M07), and privacy-safe shareable fixtures.</p>"},
  {"type":"content","title":"Validate, Tag, and Don't Fool Yourself","body":"<p>Synthetic data is dangerous if it leaks into eval unchecked: you'd measure the model against scenarios that don't reflect reality, or worse, against cases generated by the very model under test (which knows how to solve them). Rules: have a clinician <strong>validate</strong> realism, run a <strong>distribution check</strong> against real cases so augmentation doesn't distort the mix, <strong>tag</strong> every synthetic record's provenance, and keep synthetic data out of the held-out human gold set used for the release gate.</p>"},
  {"type":"code","title":"Generate and Guard Synthetic Cases","language":"python","code":"from llmops.synth import generate, validate\n\n# fill a known gap: rare service type with too few real cases\ncases = generate(\n    spec=\"PA request: rare gene therapy, must require failed step-therapy\",\n    n=50, generator_model=\"different-from-system-under-test\",\n    seed_realism=load_real_examples(\"rare-therapy\", k=5),\n)\n\nreport = validate(cases,\n    clinician_review=True,                 # realism\n    distribution_ref=\"pa-gold\",            # don't distort the mix\n    pii_scan=True,                         # no accidental real PHI\n)\nfor c in cases:\n    c.provenance = \"synthetic\"             # always tag\n\n# allowed: augment TRAINING/few-shot pool; NOT the held-out human gold gate\nfew_shot_pool.extend([c for c in cases if report.ok])"},
  {"type":"quiz","question":"You generate 50 synthetic PA cases for a rare service type and want to use them. Which use is appropriate, and which would corrupt your evaluation?",
   "options":["Add them straight into the held-out human gold set used for the release gate","Use validated, tagged synthetic cases to augment the few-shot/training pool, but keep them out of the human-labeled held-out gold gate","Synthetic data can't be used for anything","Generate them with the model under test for consistency"],
   "correct":1,
   "explanation":"Synthetic cases are great for augmenting training/few-shot coverage of rare classes, but if they enter the held-out human gold set you're grading the model against fiction (and against cases a sibling model invented). Validate realism, tag provenance, and protect the human gold gate. The simulator trains the pilot; the checkride is still real."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Synthetic leakage into the gold gate: release decisions ride on made-up cases, and real-world quality diverges from the green dashboard.",
   "Self-generated tests: cases authored by the model under test flatter it, hiding the very weaknesses you generated data to expose."]}],
 "takeaway":"Use synthetic data to simulate the rare and dangerous cases logs lack — but validate it, tag its provenance, and keep it out of the human gold gate so you never grade the model against fiction.",
 "labUnderstand":"Identify the most under-represented case types in your PA gold set and assess the risk of leaving them untested.",
 "labBuild":"Generate and validate a batch of synthetic rare-class and adversarial PA cases (using a different model than the system under test), tag provenance, and add them only to the few-shot pool."})

# ════════════════════════════════════════════════════════════════════
#  TRACK 6 — MODEL LIFECYCLE
# ════════════════════════════════════════════════════════════════════

MODS.append({
 "id":"M20","track":6,"title":"Model Versioning & Pinning",
 "subtitle":"Controlling exactly which model snapshot serves each determination",
 "icon":"\U0001F4CC","color":BRICK,
 "topics":[
   "Pinned snapshots vs floating aliases ('latest')",
   "Why a silent provider update is an unreviewed deployment",
   "Tying every determination to its exact model version",
   "Coordinated, evaluated version bumps"],
 "analogy":{"title":"Pharmaceutical Lot Numbers","text":"Every batch of medicine carries a lot number, so if a problem appears the manufacturer can trace exactly which batch, made when, with which inputs. Model pinning is the lot number for your determinations: pin the exact snapshot, record it on every decision, and you can trace, reproduce, and recall. Run on 'latest' and you're dispensing unlabeled pills."},
 "antiPatterns":[
   "Pointing at a floating alias like 'latest' — the provider updates it and your behavior shifts with no PR and no rollback.",
   "Not recording the model snapshot per determination — during an appeal you can't say which model decided."]})
SVGS["M20"]=svg_compare("Pinned vs Floating Model","Floating ('latest')",["Provider updates silently","Behavior shifts unbidden","No review, no rollback","Can't reproduce decisions"],"Pinned snapshot",["You choose when to move","Bumps are evaluated","Recorded per determination","Reproducible for appeals"],BRICK)
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M05 Multi-Provider"},{"type":"sdlc","label":"AI-SDLC — Model Governance"}],
 "sections":[
  {"type":"content","title":"Pin the Snapshot, Always","body":"<p>Foundation-model aliases like 'latest' float: the provider can repoint them to a new snapshot whenever they ship. If your PA pipeline targets a floating alias, a provider update becomes a <strong>deployment you never made</strong> — behavior shifts overnight with no PR, no eval, no rollback path. The rule is absolute for a regulated workflow: pin the exact snapshot, and treat any move to a new one as a reviewed, evaluated release.</p>"},
  {"type":"content","title":"Record the Lot Number on Every Decision","body":"<p>Pinning controls input; <strong>recording</strong> enables accountability. Stamp every determination with its model snapshot (plus prompt and policy versions — the M01 fingerprint). When a denial is appealed months later, you can state exactly which model, prompt, and policy produced it and reproduce it. Without the lot number, a quality problem can't be scoped: you can't tell which determinations a bad snapshot touched, so you can't recall them.</p>"},
  {"type":"code","title":"Pin and Stamp","language":"python","code":"# Pin the exact snapshot; never target a floating alias in production.\nPINNED = \"claude-sonnet-4-6\"   # exact snapshot id, reviewed & evaluated\n\ndef determine(req):\n    out = client.complete(build_prompt(req), model=PINNED, temperature=0.0)\n    record_determination(\n        case_id=req.id,\n        decision=out.decision,\n        model_snapshot=PINNED,           # the 'lot number'\n        prompt_version=PROMPT_VERSION,\n        policy_snapshot=POLICY_VERSION,\n    )\n    return out\n\n# A version bump is a release, not a config tweak:\ndef bump_model(new_snapshot):\n    report = regression_gate(new_snapshot, baseline=PINNED)   # M06\n    assert report.passed, report.summary\n    return canary_rollout(new_snapshot)                       # M09"},
  {"type":"quiz","question":"Your PA pipeline targets the model alias 'latest' to always get improvements. One morning determinations shift noticeably with no change on your side. What happened, and what's the fix?",
   "options":["A bug in your code; add logging","The provider repointed 'latest' to a new snapshot — an unreviewed deployment; pin an exact snapshot and treat version bumps as evaluated releases","The eval set changed itself","Temperature drifted; set it to 1.0"],
   "correct":1,
   "explanation":"A floating alias let the provider deploy a new model into your production path without your review. In a regulated determination workflow that's unacceptable: pin the exact snapshot, stamp it on every decision (the lot number), and move to a new snapshot only through the regression gate and a canary. Control when you change, and be able to reproduce what you decided."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "'latest' in production: a silent provider snapshot bump shifts determinations overnight with no rollback path and no audit trail.",
   "Unstamped decisions: a bad snapshot is identified, but you can't tell which determinations it touched, so you can't scope a recall or defend an appeal."]}],
 "takeaway":"Pin the exact model snapshot and stamp it on every determination — so a provider update is a decision you make and evaluate, not one that happens to you, and every decision is reproducible.",
 "labUnderstand":"Inspect a pipeline's model configuration for floating aliases and check whether determinations record their snapshot; rate the audit and rollback risk.",
 "labBuild":"Refactor the PA pipeline to pin an exact snapshot, stamp model+prompt+policy versions on every determination, and gate any version bump through regression + canary."})

MODS.append({
 "id":"M21","track":6,"title":"Model Migration",
 "subtitle":"Moving to a new model without breaking the behavior you depend on",
 "icon":"\U0001F68C","color":BRICK,
 "topics":[
   "Why a 'better' model can be worse for your specific task",
   "Behavioral diffing: shadow the new model against the old",
   "Re-tuning prompts for the new model's quirks",
   "A staged migration playbook with rollback"],
 "analogy":{"title":"Upgrading a City Bus Fleet","text":"A city doesn't scrap every old bus the day new ones arrive. It runs new buses on a few routes, checks they fit the depots and the drivers adapt, fixes the surprises, then expands. Model migration is the same staged swap: the new model may be 'better' in general yet stumble on your PA prompts and policy format, so you shadow it, re-tune, pilot a route, and only then roll out the fleet."},
 "antiPatterns":[
   "Swapping models because the new one tops a public benchmark — your task isn't the benchmark, and it regresses on denials.",
   "Migrating without re-tuning prompts — the old prompt was shaped to the old model's quirks and now underperforms."]})
SVGS["M21"]=svg_flow("Staged Model Migration",["Shadow|new vs old","Diff|behavioral delta","Re-tune|prompts for new","Canary|one route","Expand|full fleet"],BRICK,"general 'better' ≠ better for your task")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M05 Multi-Provider"},{"type":"sdlc","label":"AI-SDLC — Change Mgmt"}],
 "sections":[
  {"type":"content","title":"'Better' Is Task-Relative","body":"<p>A new model topping a public leaderboard tells you little about your PA task. It may reason better in general yet be <em>worse</em> at following your structured determination schema, more prone to over-approve, or differently susceptible to injection. The only benchmark that matters is your gold set on your prompts. Treat every migration as a hypothesis to test, not an upgrade to assume.</p>"},
  {"type":"content","title":"Diff, Re-Tune, Stage","body":"<p>Run the new model in <strong>shadow</strong> against the current one on live traffic and compute a <strong>behavioral diff</strong>: where do determinations disagree, and on which slices? Expect to <strong>re-tune the prompt</strong> — the existing one was shaped around the old model's quirks (formatting, refusal tendencies, few-shot needs). Then migrate in <strong>stages</strong> with canary and rollback (M09/M11). A migration is a release pipeline, not a config swap.</p>"},
  {"type":"code","title":"Behavioral Diff in Shadow","language":"python","code":"def shadow_diff(new_model, window=\"7d\"):\n    rows=[]\n    for req in live_requests(window):\n        old = determine(req, model=CURRENT)\n        new = determine(req, model=new_model)   # shadow: not served\n        if old.decision != new.decision:\n            rows.append((req.service_type, old.decision, new.decision, req.id))\n    diff = summarize(rows, by=\"service_type\")\n    # which way does disagreement skew? more denials? more approvals?\n    print(diff.table())\n    return diff\n\ndiff = shadow_diff(\"candidate-model-y\")\n# gate migration on gold-set performance AFTER re-tuning the prompt\nretuned = retune_prompt_for(\"candidate-model-y\")\nassert regression_gate(\"candidate-model-y\", prompt=retuned).passed"},
  {"type":"quiz","question":"A new model scores higher on public reasoning benchmarks, so a teammate wants to swap it into the PA pipeline this week. What's the disciplined path?",
   "options":["Swap immediately — higher benchmark means higher quality","Shadow it against the current model, diff determinations by slice, re-tune the prompt for it, then canary with rollback — gated on your own gold set","Only migrate during a quarterly freeze","Run both models forever and average their outputs"],
   "correct":1,
   "explanation":"Public benchmarks aren't your task. The new model may regress on your schema or skew denials despite a better leaderboard score. Shadowing reveals the behavioral delta, prompt re-tuning adapts to its quirks, and a canary bounds risk — all gated on your gold set. Upgrade the fleet route by route, not all at once."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Benchmark-driven swap: the 'smarter' model quietly over-approves a high-cost service line, and the win on paper is a loss in claims.",
   "No prompt re-tuning: the old prompt's quirk-specific scaffolding misfires on the new model, so a genuinely better model underperforms in your pipeline."]}],
 "takeaway":"Migrate models as a staged, gated release — shadow, diff, re-tune the prompt, canary — because 'better in general' routinely means 'worse for your specific task' until proven otherwise on your gold set.",
 "labUnderstand":"Compare two models on the same PA gold set and prompt; quantify per-slice disagreement and identify where the 'better' model actually regresses.",
 "labBuild":"Build a shadow-diff harness that runs a candidate model on live traffic, reports behavioral deltas by slice, and gates migration on a re-tuned-prompt regression run plus canary."})

MODS.append({
 "id":"M22","track":6,"title":"Multi-Model Strategies",
 "subtitle":"Routing each determination to the right model for its complexity and stakes",
 "icon":"\U0001F500","color":BRICK,
 "topics":[
   "Routing by complexity, stakes, and confidence",
   "Cascade/fallback patterns: cheap-first, escalate on low confidence",
   "Cost-quality trade-offs and the routing budget",
   "Operating multiple models without operational sprawl"],
 "analogy":{"title":"A Law Firm Staffing by Complexity","text":"A law firm doesn't put a senior partner on a routine NDA — paralegals handle simple matters and partners take the bet-the-company cases. Multi-model routing staffs your PA determinations the same way: a fast cheap model clears the obvious approvals, while complex, high-cost, or low-confidence cases escalate to a stronger (pricier) model or a human. You match the resource to the stakes."},
 "antiPatterns":[
   "One expensive model for every determination — you pay partner rates to review NDAs and blow the budget.",
   "Routing with no confidence signal — hard cases silently get the cheap model and quality craters on exactly the cases that matter."]})
SVGS["M22"]=svg_flow("Confidence-Based Cascade",["Triage|complexity/stakes","Cheap model|clears obvious","Confidence check|threshold","Escalate|stronger model","Human|low-confidence/high-stakes"],BRICK,"match the resource to the stakes")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M05 Routing"},{"type":"platform","label":"Platform M16 Cost"}],
 "sections":[
  {"type":"content","title":"Route by Complexity, Stakes, and Confidence","body":"<p>Not every PA request needs your strongest model. A routine in-network imaging approval is a paralegal task; a rare gene therapy denial is bet-the-company. A <strong>router</strong> sends each case to the appropriate model based on signals: service complexity, dollar stakes, and the model's own <strong>confidence</strong>. The cheap model handles the bulk; the expensive model and human reviewers are reserved for where their cost is justified.</p>"},
  {"type":"content","title":"Cascades and the Routing Budget","body":"<p>A common pattern is the <strong>cascade</strong>: try the cheap model first; if its confidence is below threshold (or stakes are high), escalate to a stronger model, then to a human. This dramatically cuts cost while protecting quality on hard cases — but only if your confidence signal is trustworthy and your thresholds are tuned against the gold set. Operating multiple models adds complexity (more snapshots to pin, monitor, and migrate), so the gateway seam (M03) is what keeps the sprawl manageable.</p>"},
  {"type":"code","title":"A Cost-Aware Cascade Router","language":"python","code":"def route_determination(req):\n    if req.dollar_stakes > HIGH or req.service_type in ALWAYS_HUMAN:\n        return human_queue(req)                       # stakes override\n\n    cheap = gw.complete(prompt(req), model=\"fast-cheap\", use_case=\"pa\")\n    if cheap.confidence >= 0.85 and cheap.schema_valid:\n        return cheap                                  # bulk of traffic, low cost\n\n    strong = gw.complete(prompt(req), model=\"claude-sonnet-4-6\", use_case=\"pa\")\n    if strong.confidence >= 0.80:\n        return strong                                 # escalate hard cases\n    return human_queue(req)                           # low confidence -> human\n\n# thresholds tuned on the gold set to hit a cost AND quality target\nrouter_report = tune_thresholds(gold, cost_ceiling=0.012, min_deny_recall=0.90)"},
  {"type":"quiz","question":"To cut cost, a team routes every PA determination through one premium model. What's the smarter design, and what makes it safe?",
   "options":["Premium-everything is already optimal","A cascade: cheap model for the obvious bulk, escalate low-confidence/high-stakes cases to a stronger model or human — safe only if the confidence signal is validated and thresholds are tuned on the gold set","Always use the cheapest model","Pick the model randomly per request"],
   "correct":1,
   "explanation":"Premium-everything overpays on routine approvals. A confidence-based cascade reserves the expensive model and humans for cases that warrant them, cutting cost while protecting quality — but it only works if confidence is trustworthy and thresholds are tuned against the gold set, otherwise hard cases slip through on the cheap path. Staff by stakes, like a law firm."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Premium-everything: budget is exhausted paying partner rates for paralegal work, and finance kills the project before it scales.",
   "Untuned routing: an unvalidated confidence signal sends genuinely hard denials to the cheap model, so quality collapses precisely on the high-stakes cases."]}],
 "takeaway":"Route each determination to the right model by complexity, stakes, and validated confidence — a cascade that staffs cheap models on routine cases and reserves strong models and humans for where the stakes justify the cost.",
 "labUnderstand":"Analyze a single-model pipeline's cost and per-slice quality; estimate the savings and risks of introducing a cheap-first cascade.",
 "labBuild":"Implement a cascade router with confidence thresholds and stakes overrides, then tune the thresholds on the gold set to meet both a cost ceiling and a deny-recall floor."})

MODS.append({
 "id":"M23","track":6,"title":"Model Deprecation & Sunset",
 "subtitle":"Retiring a model on your schedule, before the provider forces yours",
 "icon":"\U0001F305","color":BRICK,
 "topics":[
   "Reading provider deprecation notices and EOL timelines",
   "Inventory: every place a deprecated model is used",
   "The forced-migration fire drill vs the planned sunset",
   "Sunsetting your own prompt/bundle versions"],
 "analogy":{"title":"A Building Elevator's End-of-Life","text":"A building manager who ignores an elevator's end-of-life notice ends up with it failing inspection and shut down with no replacement ordered — tenants stuck on the stairs. Reading the notice early means scheduling the modernization, keeping the old car running during the swap, and a smooth cutover. Model deprecation is identical: the provider's EOL date is coming whether you plan for it or not."},
 "antiPatterns":[
   "Ignoring deprecation notices until the model returns errors in production — now it's a 2am forced migration with no eval.",
   "No inventory of where a model is used — you migrate the obvious service and miss the batch job still calling the dead snapshot."]})
SVGS["M23"]=svg_flow("Planned Sunset",["Notice|EOL date","Inventory|all usages","Migrate|staged + gated","Verify|nothing left on old","Decommission|on your schedule"],BRICK,"plan the sunset before it's forced")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M05 Lifecycle"},{"type":"sdlc","label":"AI-SDLC — EOL"}],
 "sections":[
  {"type":"content","title":"The EOL Date Is Coming Either Way","body":"<p>Every model snapshot gets deprecated. Providers publish <strong>end-of-life timelines</strong>, after which the snapshot returns errors or auto-redirects to a successor (a silent migration you didn't evaluate). You either plan the sunset on your schedule — or the provider schedules a fire drill on theirs, typically at the worst time. Monitoring deprecation notices is an operational duty, not an afterthought.</p>"},
  {"type":"content","title":"You Can't Sunset What You Can't Find","body":"<p>The first step of any sunset is an <strong>inventory</strong>: every code path, batch job, eval harness, and fallback that references the deprecated snapshot. The classic failure is migrating the obvious online path while a nightly re-adjudication job keeps calling the dead model — and breaks on EOL day. Because every determination is stamped with its snapshot (M20), the inventory is queryable. The same discipline applies to <strong>your own</strong> bundle versions: retire old prompt/policy versions deliberately so they can't be accidentally re-pinned.</p>"},
  {"type":"code","title":"Find Every Usage Before Sunset","language":"python","code":"def sunset_plan(deprecated_snapshot, eol_date):\n    # 1. find every place it's used (code + live stamps + jobs)\n    usages = {\n      \"code_refs\":   grep_repo(deprecated_snapshot),\n      \"live_stamps\": audit_log.count(model_snapshot=deprecated_snapshot, window=\"30d\"),\n      \"batch_jobs\":  scheduler.jobs_using(deprecated_snapshot),\n      \"fallbacks\":   gateway.fallbacks_referencing(deprecated_snapshot),\n    }\n    # 2. migrate each via the staged playbook (M21), gated (M06), canaried (M09)\n    # 3. verify zero remaining usage BEFORE the EOL date\n    remaining = audit_log.count(model_snapshot=deprecated_snapshot, window=\"24h\")\n    assert remaining == 0, f\"{remaining} determinations still on dead model!\"\n    return {\"eol\": eol_date, \"usages\": usages, \"clear\": remaining == 0}"},
  {"type":"quiz","question":"A provider announces your pinned PA model reaches end-of-life in 90 days, after which calls redirect to a successor. What's the right response?",
   "options":["Ignore it — 90 days is far away","Do nothing; the auto-redirect to the successor handles it","Inventory every usage now, migrate to a chosen successor via the staged gated playbook, and verify zero usage of the old snapshot before EOL","Switch everything to 'latest' so it never expires"],
   "correct":2,
   "explanation":"The auto-redirect IS the danger — it's an unevaluated forced migration to a model you didn't test on your gold set. Plan the sunset: inventory all usages (including batch jobs and fallbacks), migrate deliberately through the gated playbook, and confirm nothing still calls the dead snapshot before the EOL date. Schedule your own modernization before the elevator fails inspection."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Notice ignored: the model starts erroring on EOL day and the team scrambles a 2am migration with no eval, shipping an unvetted successor.",
   "Incomplete inventory: the online path is migrated but a nightly re-adjudication job still calls the dead snapshot and silently fails for days."]}],
 "takeaway":"Treat every provider EOL date as a deadline you plan around — inventory all usages and migrate deliberately — because the alternative is an unevaluated forced migration at the worst possible moment.",
 "labUnderstand":"Given a deprecation notice, build the full inventory of where a model is referenced (code, live stamps, batch jobs, fallbacks) and assess what would break on EOL day.",
 "labBuild":"Write a sunset playbook and tooling that inventories all usages of a snapshot, drives staged migration, and asserts zero remaining usage before the EOL date."})

# ════════════════════════════════════════════════════════════════════
#  TRACK 7 — INCIDENT & RELIABILITY
# ════════════════════════════════════════════════════════════════════

MODS.append({
 "id":"M24","track":7,"title":"LLM Failure Modes Taxonomy",
 "subtitle":"A shared vocabulary for how LLM apps actually break",
 "icon":"\U0001F4CB","color":IRIS,
 "topics":[
   "The failure families: hallucination, refusal, drift, injection, format, latency/cost",
   "Severity classification by member and compliance impact",
   "Mapping failure modes to detectors and owners",
   "Why a shared taxonomy speeds every incident response"],
 "analogy":{"title":"Hospital Medical-Error Categories","text":"Hospitals classify errors — medication, surgical, diagnostic, documentation — because a shared taxonomy lets staff report, analyze, and prevent them systematically instead of treating each as a unique surprise. An LLM failure taxonomy does the same: when on-call can say 'this is a hallucinated-criterion incident, severity 1,' everyone knows the detector, the runbook, and the owner. Naming the failure is the first step to managing it."},
 "antiPatterns":[
   "Treating every incident as a novel mystery — no taxonomy means no pattern, no prevention, slow response.",
   "Classifying by symptom not cause — 'the model is wrong' lumps hallucination, drift, and injection into one useless bucket."]})
SVGS["M24"]=svg_stack("LLM Failure Taxonomy (PA)",[("Hallucination","invents a policy criterion"),("Refusal","declines a valid request"),("Drift","quality decays over time"),("Injection","note hijacks the decision"),("Format","invalid/unparseable output"),("Latency/Cost","breaches TAT or budget")],IRIS)
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M29 Reliability"},{"type":"sdlc","label":"AI-SDLC — Incident"}],
 "sections":[
  {"type":"content","title":"Six Failure Families","body":"<p>LLM apps break in recognizable ways. <strong>Hallucination</strong>: the model invents a policy criterion that doesn't exist. <strong>Refusal</strong>: it declines a legitimate PA request as 'medical advice.' <strong>Drift</strong>: quality decays over time (M13). <strong>Injection</strong>: untrusted note text hijacks the decision (M07). <strong>Format</strong>: output isn't valid against the determination schema. <strong>Latency/cost</strong>: the call breaches turnaround time or budget. A named family points straight to a detector and a response.</p>"},
  {"type":"content","title":"Classify by Cause and Severity","body":"<p>Two axes make the taxonomy operational. <strong>Cause</strong> (which family) routes to the right fix — hallucination needs grounding, injection needs input isolation; lumping them as 'model wrong' wastes the incident. <strong>Severity</strong> ranks by member and compliance impact — a hallucinated criterion that wrongly denies urgent care is Sev-1; a formatting blip that auto-retries is Sev-4. Every family maps to a detector, an owner, and a runbook (M26), so response is reflexive, not improvised.</p>"},
  {"type":"code","title":"A Failure Classifier","language":"python","code":"FAILURE_FAMILIES = {\n  \"hallucination\": lambda o: o.cited_criterion not in valid_criteria(o.case),\n  \"refusal\":       lambda o: o.is_refusal and o.case.is_legitimate,\n  \"format\":        lambda o: not o.schema_valid,\n  \"injection\":     lambda o: injection_markers(o.case.clinical_note),\n  \"latency\":       lambda o: o.latency_ms > SLA_MS,\n}\n\ndef classify(outcome):\n    hits = [name for name, test in FAILURE_FAMILIES.items() if test(outcome)]\n    sev  = severity(hits, member_impact=outcome.case.urgent,\n                          compliance=outcome.decision == \"deny\")\n    return {\"families\": hits, \"severity\": sev,\n            \"owner\": OWNERS[hits[0]] if hits else None,\n            \"runbook\": RUNBOOKS.get(hits[0] if hits else None)}"},
  {"type":"quiz","question":"During an incident, on-call reports 'the PA model is giving wrong answers.' Why is a failure taxonomy worth adopting before the next incident?",
   "options":["It makes nicer reports","A named family (e.g., 'hallucinated criterion, Sev-1') maps directly to a detector, owner, and runbook, so response is fast and the cause-specific fix is obvious","Taxonomies prevent all failures","It replaces the need for monitoring"],
   "correct":1,
   "explanation":"'Wrong answers' is a symptom that hides very different causes — hallucination, drift, and injection need opposite fixes. A shared taxonomy classifies by cause and severity, instantly pointing to the detector, owner, and runbook. Like hospital error categories, naming the failure is what makes systematic, fast response possible."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Mystery-per-incident: with no taxonomy, every outage is re-diagnosed from scratch and recurring failures are never prevented.",
   "Symptom-based buckets: 'model wrong' conflates injection and drift, so the team applies the wrong fix and the real cause persists."]}],
 "takeaway":"Adopt a shared failure taxonomy classified by cause and severity — so every incident maps instantly to a detector, an owner, and a runbook instead of being re-diagnosed from scratch.",
 "labUnderstand":"Classify a set of past PA incidents into failure families and severities; identify which family recurs most and lacks a detector.",
 "labBuild":"Implement a failure classifier that tags each production outcome with its families and severity and routes it to the right owner and runbook."})

MODS.append({
 "id":"M25","track":7,"title":"SLOs & SLAs for LLM Applications",
 "subtitle":"Defining and defending reliability targets for quality, latency, and turnaround",
 "icon":"\U0001F3AF","color":IRIS,
 "topics":[
   "SLI vs SLO vs SLA, applied to LLM quality not just uptime",
   "Choosing SLIs that capture determination quality and TAT",
   "Error budgets that govern release pace",
   "Regulatory turnaround as a hard SLA"],
 "analogy":{"title":"A Delivery Service's Guarantees","text":"A courier promises 'most packages by noon' (an internal target) and contractually guarantees 'by end of day or your money back' (a customer promise). It measures on-time rate to manage both. LLM reliability works the same: SLIs are what you measure, SLOs are your internal targets, and the SLA is the promise with consequences — and for PA, regulators set some of those promises for you."},
 "antiPatterns":[
   "SLOs only on uptime — you meet 99.9% availability while determination quality and TAT silently fail.",
   "An SLA you can't measure — you've promised a turnaround you have no SLI to verify or defend."]})
SVGS["M25"]=svg_stack("SLI → SLO → SLA",[("SLI (measure)","agreement, p95 latency, TAT hours"),("SLO (internal target)","agreement >=90%, TAT urgent <48h"),("Error budget","governs release pace"),("SLA (promise)","regulatory TAT, consequences")],IRIS)
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M29 SLOs"},{"type":"sdlc","label":"AI-SDLC — Ops"}],
 "sections":[
  {"type":"content","title":"From SLI to SLA, for Quality","body":"<p>An <strong>SLI</strong> is a measurement (reviewer agreement, p95 latency, urgent-case TAT). An <strong>SLO</strong> is your internal target on it (agreement ≥ 90%, urgent TAT &lt; 48h). An <strong>SLA</strong> is an external promise with consequences. The LLM-specific move is to set these on <em>quality</em>, not just uptime — a PA pipeline that's 99.99% available but agrees with reviewers only 80% is failing its real job. Pick SLIs that capture the determination's correctness and timeliness.</p>"},
  {"type":"content","title":"Error Budgets and Regulatory SLAs","body":"<p>An <strong>error budget</strong> is the allowed shortfall (if the SLO is 90%, the budget is the 10%). Spend it wisely: when the budget is healthy you can ship faster (Track 3); when it's exhausted you freeze risky releases and stabilize. This makes reliability a shared, quantitative lever instead of an argument. For PA, some targets aren't yours to choose: <strong>regulatory turnaround</strong> (e.g., decisions on urgent requests within a mandated window) is a hard SLA with legal consequences — it anchors your latency and TAT SLOs.</p>"},
  {"type":"code","title":"SLOs With an Error Budget Gate","language":"python","code":"SLOs = {\n  \"reviewer_agreement\": {\"target\": 0.90, \"window\": \"30d\"},\n  \"tat_urgent_hours\":   {\"target_p95\": 48, \"window\": \"7d\"},   # regulatory-anchored\n  \"schema_valid\":       {\"target\": 0.995, \"window\": \"7d\"},\n}\n\ndef error_budget_status(slo, sli_value):\n    target = slo[\"target\"]\n    budget_used = max(0, target - sli_value) / (1 - target)\n    return budget_used        # >1.0 means SLO breached\n\n# Release pace governed by remaining budget\nif error_budget_status(SLOs[\"reviewer_agreement\"], current_agreement) > 0.75:\n    freeze_risky_releases(\"agreement error budget nearly exhausted\")\nelse:\n    allow_canary_releases()"},
  {"type":"quiz","question":"Your PA service reports 99.95% uptime and the team declares its SLOs met. A regulator notes urgent determinations routinely exceed the mandated 72-hour window. What was the SLO design failure?",
   "options":["Uptime should have been 99.99%","SLIs/SLOs were set on availability, not on the quality and turnaround that define the service's real obligation — including the regulatory TAT SLA","SLAs don't apply to AI systems","The error budget was too large"],
   "correct":1,
   "explanation":"Availability is necessary but not the job. The service's real obligations are determination quality and a regulatory turnaround SLA, and those needed their own SLIs and SLOs. Measuring only uptime let a legally-significant TAT breach hide behind a green dashboard. Set reliability targets on what the service actually promises."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Uptime-only SLOs: the dashboard is green while agreement and turnaround quietly violate the service's real (and regulatory) obligations.",
   "Unmeasurable SLA: a turnaround promise exists with no SLI behind it, so breaches are invisible until a regulator or lawsuit surfaces them."]}],
 "takeaway":"Define SLOs on determination quality and turnaround — not just uptime — with error budgets that govern release pace and regulatory TAT as a hard SLA you can measure and defend.",
 "labUnderstand":"Review a service's current SLOs and identify which real obligations (quality, TAT, compliance) have no SLI; flag any SLA you can't measure.",
 "labBuild":"Define SLIs/SLOs for the PA pipeline covering agreement, turnaround, and schema validity, implement an error-budget calculation, and wire it to gate release pace."})

MODS.append({
 "id":"M26","track":7,"title":"Runbooks & On-Call",
 "subtitle":"Turning incident response from improvisation into practiced procedure",
 "icon":"\U0001F4D5","color":IRIS,
 "topics":[
   "Anatomy of a good runbook: detect, decide, act, verify, communicate",
   "On-call rotation, escalation paths, and severity-based response",
   "Runbooks for the LLM failure families",
   "Keeping runbooks alive: rehearse and update"],
 "analogy":{"title":"Fire Department Protocols","text":"Firefighters don't debate tactics inside a burning building — they execute drilled protocols where every role and step is predefined, so they act fast under stress. A runbook is that protocol for an LLM incident: when the auto-deny rate spikes at 2am, the on-call engineer follows a checklist (detect, decide, act, verify, communicate) instead of improvising while members are harmed."},
 "antiPatterns":[
   "No runbooks, so every incident depends on whoever happens to be awake remembering the right steps.",
   "Runbooks written once and never rehearsed — they reference a dashboard that moved and a flag that was renamed."]})
SVGS["M26"]=svg_flow("Incident Runbook",["Detect|alert fires","Decide|severity + rollback?","Act|revert/mitigate","Verify|metrics recover","Communicate|stakeholders"],IRIS,"drill it before you need it")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M29 On-Call"},{"type":"sdlc","label":"AI-SDLC — Incident"}],
 "sections":[
  {"type":"content","title":"Anatomy of a Runbook","body":"<p>A good runbook is a checklist for one failure mode with five beats: <strong>Detect</strong> (which alert, what it means), <strong>Decide</strong> (severity, rollback-or-mitigate criteria), <strong>Act</strong> (the exact commands — flip the bundle flag, halt the canary), <strong>Verify</strong> (which metric must recover), and <strong>Communicate</strong> (who to notify, what to tell members and compliance). For a PA auto-deny spike, that means: detect via the override/deny-rate alert, decide Sev-1, revert to last-good bundle (M11), verify deny-rate normalizes, notify the medical director and compliance.</p>"},
  {"type":"content","title":"On-Call and Living Runbooks","body":"<p>Runbooks need an <strong>on-call rotation</strong> with clear <strong>escalation</strong> (engineer → senior → medical director for clinical-impact calls) and <strong>severity-based response</strong> (Sev-1 pages immediately; Sev-3 waits for business hours). The fatal mistake is letting them rot: a runbook that cites a renamed flag or a moved dashboard fails exactly when needed. Keep them alive by <strong>rehearsing</strong> — game days (M27) and updating the runbook after every real incident's postmortem (M30).</p>"},
  {"type":"code","title":"A Runbook as Executable Checklist","language":"python","code":"RUNBOOK_auto_deny_spike = Runbook(\n  trigger=\"alert:auto_deny_rate > baseline + 0.05\",\n  severity=\"SEV1\",\n  steps=[\n    Step(\"detect\",  check=\"confirm spike on dashboards/pa, not a data artifact\"),\n    Step(\"decide\",  rule=\"if sustained >10m -> rollback; else investigate\"),\n    Step(\"act\",     run=lambda: emergency_rollback(\"auto-deny spike\")),  # M11\n    Step(\"verify\",  check=\"auto_deny_rate back to baseline within 10m\"),\n    Step(\"remediate\", run=lambda: reexamine_since(incident_start)),       # state\n    Step(\"communicate\", notify=[\"medical_director\",\"compliance\",\"status_page\"]),\n  ],\n  escalation=[\"oncall_eng\",\"senior_eng\",\"medical_director\"],\n)\nregister(RUNBOOK_auto_deny_spike)   # linked from the M24 taxonomy"},
  {"type":"quiz","question":"It's 2am and the PA auto-deny rate has doubled. Your team has dashboards but no runbooks. What's the core operational gap, and the fix?",
   "options":["Need a bigger on-call team","Without a runbook, response depends on the awake engineer improvising under stress; codify detect/decide/act/verify/communicate per failure mode and rehearse it","Just disable alerts at night","Wait until morning to respond"],
   "correct":1,
   "explanation":"Dashboards show the fire; they don't tell you how to fight it. A runbook turns response into a drilled checklist — confirm, decide severity, revert, verify recovery, remediate state, communicate — so a tired on-call engineer acts correctly and fast. And it must be rehearsed and updated, or it'll reference the flag you renamed last quarter."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Improvised response: with no runbook, recovery time and correctness depend entirely on who's awake, and member harm scales with their hesitation.",
   "Stale runbook: it points to a renamed flag and a deleted dashboard, so following it during a Sev-1 wastes the minutes that matter most."]}],
 "takeaway":"Codify incident response as rehearsed, executable runbooks — detect, decide, act, verify, communicate — so a 2am responder follows a drilled protocol instead of improvising while members are harmed.",
 "labUnderstand":"Take a past incident's timeline and write the runbook that would have shortened it; identify which step was improvised and cost the most time.",
 "labBuild":"Author executable runbooks for the top LLM failure families (auto-deny spike, schema-invalid surge, injection detection) with escalation paths, and link each to its taxonomy entry."})

MODS.append({
 "id":"M27","track":7,"title":"Chaos Engineering for AI",
 "subtitle":"Deliberately injecting failure to prove your defenses work",
 "icon":"\U0001F300","color":IRIS,
 "topics":[
   "Why untested resilience is assumed, not proven",
   "AI-specific chaos: provider outages, latency spikes, degraded quality, bad retrieval",
   "Game days and blast-radius control",
   "From chaos findings to runbook and guardrail improvements"],
 "analogy":{"title":"Earthquake Preparedness Drills","text":"A city doesn't wait for the real earthquake to discover its evacuation plan has gaps — it runs drills that simulate the disaster so weaknesses surface while everyone is safe. Chaos engineering is the earthquake drill for your PA pipeline: you deliberately trigger a provider outage or a quality drop in a controlled way, and find out whether your fallbacks, guardrails, and runbooks actually hold before a real failure tests them for you."},
 "antiPatterns":[
   "Assuming the fallback provider works because it's configured — it was never exercised and fails on first real use.",
   "Running chaos in production with no blast-radius limit — your drill becomes the incident."]})
SVGS["M27"]=svg_flow("Game Day Chaos",["Hypothesis|'fallback holds'","Inject|outage/latency/bad retrieval","Observe|guardrails+runbook","Limit|blast radius","Fix|guardrail/runbook gap"],IRIS,"prove resilience, don't assume it")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M07 Resilience"},{"type":"platform","label":"Platform M29 Reliability"}],
 "sections":[
  {"type":"content","title":"Untested Resilience Is a Hope, Not a Property","body":"<p>You configured a fallback provider, a schema guardrail, and a rollback flag. Do they actually work? Until exercised, they're assumptions. Chaos engineering replaces assumption with evidence by injecting controlled failure: kill the primary provider and confirm the PA pipeline fails over; inject 10s latency and confirm TAT alerts fire; feed the model deliberately <strong>degraded retrieval</strong> (stale policy criteria) and confirm the citation guardrail catches the resulting hallucination. You learn your real resilience before a real outage does.</p>"},
  {"type":"content","title":"Game Days With a Blast Radius","body":"<p>Chaos is run as a <strong>game day</strong>: a hypothesis ('if the provider 500s, we fail over within 30s with no member impact'), a controlled injection, and observation of whether guardrails and runbooks hold. Crucially, control the <strong>blast radius</strong> — start in staging, then a small production cohort with a kill switch — so the drill never becomes the incident. Every gap found becomes a fix: a hardened guardrail, a corrected runbook step, a new alert. Chaos findings feed directly back into Tracks 4 and 7.</p>"},
  {"type":"code","title":"A Controlled Chaos Experiment","language":"python","code":"experiment = ChaosExperiment(\n  hypothesis=\"primary provider outage -> failover < 30s, no member impact\",\n  blast_radius={\"env\":\"prod\",\"cohort\":\"0.5%\",\"kill_switch\":True},\n  inject=Fault(\"provider_500\", target=\"primary\", duration=\"5m\"),\n  observe=[\"failover_time_s\",\"schema_invalid_rate\",\"tat_breaches\",\"override_rate\"],\n  abort_if=\"member_impact > 0 or override_rate > baseline + 0.05\",\n)\nresult = experiment.run()\nfor gap in result.gaps:\n    file_followup(gap)        # -> harden guardrail / fix runbook / add alert\nassert result.hypothesis_held, result.summary"},
  {"type":"quiz","question":"Your PA pipeline has a configured fallback provider that has never actually been triggered. Why run a chaos game day before you trust it?",
   "options":["Game days are a compliance checkbox","A configured-but-unexercised fallback is an assumption; injecting a controlled provider outage proves whether failover, guardrails, and the runbook actually work — before a real outage tests them","Chaos testing replaces monitoring","Fallbacks never need testing"],
   "correct":1,
   "explanation":"Configuration isn't validation. The first time a fallback runs shouldn't be during a real outage at 2am. A controlled game day — with a limited blast radius and a kill switch — turns 'we think it works' into evidence, and every gap found hardens a guardrail or runbook. Drill the earthquake before it comes."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Untested fallback: it's invoked for the first time during a real provider outage and fails, turning a degraded state into a full outage.",
   "Uncontrolled chaos: an injection with no blast-radius limit or kill switch escapes its cohort and becomes the very incident it was meant to prevent."]}],
 "takeaway":"Prove resilience with controlled chaos game days — inject provider outages, latency, and degraded retrieval within a limited blast radius — because an unexercised fallback or guardrail is a hope, not a property.",
 "labUnderstand":"Inventory your pipeline's resilience assumptions (fallbacks, guardrails, rollback) and rate each by whether it has ever actually been exercised.",
 "labBuild":"Design and run a blast-radius-limited chaos experiment that injects a provider outage and degraded retrieval, observes guardrails and runbook behavior, and files fixes for every gap found."})

# ════════════════════════════════════════════════════════════════════
#  TRACK 8 — GOVERNANCE & OPTIMIZATION
# ════════════════════════════════════════════════════════════════════

MODS.append({
 "id":"M28","track":8,"title":"Cost Optimization at Scale",
 "subtitle":"Cutting cost per determination without quietly cutting quality",
 "icon":"\U0001F4B0","color":TEAL,
 "topics":[
   "The cost drivers: tokens, model tier, retries, and traffic shape",
   "Caching, prompt compression, and routing as cost levers",
   "Attributing cost per determination, team, and service line",
   "Cost guardrails that don't sacrifice quality"],
 "analogy":{"title":"Factory Efficiency Engineering","text":"A factory cuts unit cost by trimming waste — shorter material paths, less scrap, reused heat — not by using cheaper steel that cracks. LLM cost optimization is the same discipline: cache repeated work, compress bloated prompts, and route by complexity to trim the waste, while watching quality so you never 'save' money by shipping determinations that get appealed and cost far more downstream."},
 "antiPatterns":[
   "Cutting cost by truncating context or downgrading every call — quality drops and appeal costs dwarf the savings.",
   "No per-determination cost attribution — you can't tell which service line or prompt is burning the budget."]})
SVGS["M28"]=svg_flow("Cost Levers (quality-guarded)",["Attribute|$/determination","Cache|repeated work","Compress|prompt bloat","Route|cheap-first cascade","Guardrail|quality floor"],TEAL,"trim waste, not quality")
MODS[-1].update({
 "crosslinks":[{"type":"platform","label":"Platform M16-M19 Cost"},{"type":"sdlc","label":"AI-SDLC — FinOps"}],
 "sections":[
  {"type":"content","title":"Know Where the Money Goes","body":"<p>You can't optimize what you can't attribute. Tag every call's cost by determination, prompt version, service line, and team (via the gateway seam, M03). This reveals the real drivers: maybe one verbose prompt template, a retry storm on a flaky service, or oncology cases dominating spend. The biggest lever is usually <strong>tokens</strong> — bloated system prompts and over-retrieved policy text — followed by <strong>model tier</strong> and <strong>retries</strong>.</p>"},
  {"type":"content","title":"Levers That Preserve Quality","body":"<p>Three levers cut cost without cutting corners. <strong>Caching</strong>: identical or near-identical PA requests (or stable policy-criteria retrievals) reuse prior results. <strong>Prompt compression</strong>: trim redundant instructions and retrieve only the relevant policy sections, not the whole manual. <strong>Routing</strong>: the cheap-first cascade (M22). The non-negotiable is a <strong>quality guardrail</strong> on every cost change — an optimization that drops deny-recall below the floor is rejected, because a wrong denial's appeal and care-delay costs dwarf the token savings.</p>"},
  {"type":"code","title":"Cost Attribution and Guarded Optimization","language":"python","code":"# Attribute every determination's cost (via the gateway seam)\ncost_report = cost_sink.group_by([\"service_line\",\"prompt_version\"], window=\"30d\")\nprint(cost_report.top_spenders(10))\n\n# Apply a lever, but gate on quality before keeping it\ncandidate = current_bundle().with_changes(\n    cache=\"policy_retrieval\",          # cache stable criteria lookups\n    prompt=\"compressed-v9\",            # trim redundant instructions\n    routing=\"cheap_first_cascade\",     # M22\n)\nq = regression_gate(candidate, baseline=current_bundle())   # M06\nc = cost_estimate(candidate)\nif q.passed and q.deny_recall >= 0.90 and c.per_call <= 0.012:\n    promote(candidate)\nelse:\n    reject(\"cost win not worth quality/regression risk\", q, c)"},
  {"type":"quiz","question":"To hit a budget, a proposal truncates clinical notes to half length and downgrades all PA calls to the cheapest model. Why is this the wrong kind of cost cut?",
   "options":["Cheaper models are never acceptable","It cuts quality, not waste: truncation and blanket downgrades lower determination accuracy, and the resulting wrong denials cost far more in appeals and care delays than the tokens saved","Truncation is a security risk only","Budgets should never constrain AI spend"],
   "correct":1,
   "explanation":"This saves on steel by using steel that cracks. Token and tier cuts that degrade accuracy trade a small, visible saving for large, downstream costs — appeals, re-adjudication, regulatory exposure, and member harm. Real optimization trims waste (caching, compression, routing) under a quality guardrail that rejects any change breaching the deny-recall floor."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Quality-blind cuts: truncating context and downgrading models lowers accuracy, and the appeal/re-adjudication costs exceed the token savings many times over.",
   "Unattributed spend: with no per-determination cost tagging, the team optimizes the wrong thing while one verbose template or retry storm quietly drives the bill."]}],
 "takeaway":"Cut cost by trimming waste — caching, compression, routing — under a quality guardrail, because a 'cheap' wrong denial costs far more in appeals and harm than the tokens it saved.",
 "labUnderstand":"Attribute a month of PA spend by service line and prompt version; identify the top cost driver and whether it's waste or genuine workload.",
 "labBuild":"Implement cost attribution at the gateway, apply caching/compression/routing levers, and gate each change through a regression run with a deny-recall floor before keeping it."})

MODS.append({
 "id":"M29","track":8,"title":"Compliance Automation",
 "subtitle":"Making regulatory and policy requirements automatic and auditable",
 "icon":"\2696️","color":TEAL,
 "topics":[
   "Encoding policy as automated, testable controls",
   "Audit trails: reproducing any determination on demand",
   "PHI handling, access control, and data retention",
   "Continuous compliance checks vs point-in-time audits"],
 "analogy":{"title":"Modern Car Safety Systems","text":"Early cars relied on the driver to remember every safe behavior; modern cars build safety in — seatbelt chimes, automatic braking, lane keeping — so compliance with safe practice is continuous and automatic, not a manual checklist. Compliance automation does this for the PA pipeline: instead of trusting people to follow the rules each time, you encode the rules as controls the system enforces and records on every determination."},
 "antiPatterns":[
   "Compliance as a once-a-year manual audit — between audits, violations accumulate undetected.",
   "Determinations that can't be reproduced — when a regulator asks 'why was this denied,' you have no defensible answer."]})
SVGS["M29"]=svg_stack("Compliance as Code",[("Policy controls","encoded + testable"),("Audit trail","reproduce any decision"),("PHI handling","access control + retention"),("Continuous checks","not point-in-time"),("Evidence","auto-generated for audit")],TEAL)
MODS[-1].update({
 "crosslinks":[{"type":"sdlc","label":"AI-SDLC — Compliance"},{"type":"platform","label":"Platform M19 Governance"}],
 "sections":[
  {"type":"content","title":"Encode the Rules as Controls","body":"<p>Manual compliance is hope dressed as process. The durable approach is <strong>compliance as code</strong>: every requirement becomes an automated, testable control. 'Every denial must cite a specific policy section' is a guardrail that blocks uncited denials. 'No PHI in logs' is an automated scan. 'Urgent decisions within the regulatory window' is a monitored SLO (M25). The controls run on every determination, not once a year, so violations are prevented or caught immediately.</p>"},
  {"type":"content","title":"Audit Trails and Continuous Evidence","body":"<p>For a regulated PA workflow, the defining requirement is <strong>defensibility</strong>: for any determination, you must reproduce exactly what the model saw and why it decided. That's the fingerprinted bundle (M08) plus the persisted trace (M14) plus the recorded snapshot (M20). Pair this with <strong>PHI controls</strong> (access control, de-identification, retention limits) and <strong>continuous compliance checks</strong> that generate audit evidence automatically. When the regulator arrives, you produce evidence on demand instead of scrambling to reconstruct it.</p>"},
  {"type":"code","title":"Compliance Controls That Run Every Time","language":"python","code":"COMPLIANCE_CONTROLS = [\n  Control(\"denial_cites_policy\",\n          test=lambda d: d.decision != \"deny\" or d.cites_policy_section,\n          on_fail=\"block\"),                       # guardrail, every call\n  Control(\"no_phi_in_logs\",\n          test=lambda d: not phi_scan(d.log_payload), on_fail=\"redact+alert\"),\n  Control(\"urgent_within_window\",\n          test=lambda d: not d.urgent or d.tat_hours <= 72, on_fail=\"alert\"),\n  Control(\"reproducible\",\n          test=lambda d: d.bundle_fingerprint and d.trace_id, on_fail=\"block\"),\n]\n\ndef enforce(determination):\n    for c in COMPLIANCE_CONTROLS:\n        if not c.test(determination):\n            handle(c.on_fail, determination, control=c.name)  # block/redact/alert\n    audit_store.write_evidence(determination)   # continuous, queryable evidence"},
  {"type":"quiz","question":"A regulator audits a denial from 8 months ago and asks you to show exactly how it was decided. Compliance automation should have ensured what?",
   "options":["A signed PDF policy document exists","Every determination is reproducible (fingerprinted bundle + persisted trace + recorded snapshot) and its controls (citation, PHI, TAT) ran and were logged at decision time","The newest model was used","A human reviewed every single case"],
   "correct":1,
   "explanation":"Defensibility requires reproducing the exact decision and proving the controls were satisfied when it was made. That means the fingerprinted bundle, the persisted trace, the recorded snapshot, and logged control results — generated continuously, not reconstructed for the audit. Like modern car safety, compliance is built in and always on, not a once-a-year checklist."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Point-in-time compliance: between annual audits, uncited denials and PHI-in-logs accumulate, surfacing all at once as findings and penalties.",
   "Irreproducible decisions: a denial can't be reconstructed because the bundle and trace weren't recorded, leaving no defensible answer to a regulator or appeal."]}],
 "takeaway":"Encode regulatory requirements as automated controls that run on every determination and persist reproducible audit evidence continuously — so compliance is built-in and always-on, not an annual scramble.",
 "labUnderstand":"Take three real PA compliance requirements and assess whether each is enforced automatically per determination or relies on manual process; rate the exposure.",
 "labBuild":"Implement a set of compliance controls (denial citation, no-PHI-in-logs, TAT window, reproducibility) that run on every determination, block or alert on failure, and write continuous audit evidence."})

MODS.append({
 "id":"M30","track":8,"title":"Knowledge Management",
 "subtitle":"Capturing operational learning so the team improves instead of repeating mistakes",
 "icon":"\U0001F4DA","color":TEAL,
 "topics":[
   "Blameless postmortems and the institutional memory they build",
   "From incident to durable artifact: runbook, test, guardrail",
   "Decision records for prompts, models, and policy choices",
   "Onboarding and the cost of tribal knowledge"],
 "analogy":{"title":"Hospital Morbidity & Mortality Conferences","text":"Hospitals hold regular M&M conferences where clinicians review adverse outcomes openly and blamelessly, extracting lessons that become protocol changes — so the same mistake doesn't recur ward after ward. Knowledge management is the M&M for your LLM operation: every incident, override pattern, and migration becomes a durable, shared lesson, so the team's competence compounds instead of resetting with each departure."},
 "antiPatterns":[
   "Blameful postmortems — people hide mistakes, the real causes never surface, and the same incident recurs.",
   "Lessons that live in someone's head or a Slack thread — they vanish when that person leaves or the thread scrolls away."]})
SVGS["M30"]=svg_flow("Incident → Durable Knowledge",["Postmortem|blameless","Root cause|systemic","Artifact|runbook/test/guardrail","Decision record|why we chose","Onboarding|shared memory"],TEAL,"compound competence, don't reset it")
MODS[-1].update({
 "crosslinks":[{"type":"sdlc","label":"AI-SDLC — Knowledge"},{"type":"platform","label":"Platform M29 Postmortems"}],
 "sections":[
  {"type":"content","title":"Blameless Postmortems Build Memory","body":"<p>When a PA incident happens, the goal isn't to find who to blame — it's to find what in the <em>system</em> allowed it and fix that. <strong>Blameless postmortems</strong> make this safe: people surface the real causes (a missing guardrail, an ambiguous runbook, an untested fallback) instead of hiding them. The output isn't a document that's filed and forgotten; it's a set of <strong>durable artifacts</strong> — a new runbook (M26), a regression test (M06), a hardened guardrail (M07/M29) — so the lesson is encoded into the system, not just remembered.</p>"},
  {"type":"content","title":"Decision Records and Defeating Tribal Knowledge","body":"<p>The other half of knowledge management is capturing <em>why</em>, not just what. <strong>Decision records</strong> document why you chose this prompt structure, pinned that model, or set this routing threshold — so a future engineer doesn't undo a hard-won choice they don't understand. The enemy is <strong>tribal knowledge</strong>: critical context living only in one person's head or a buried Slack thread. When they leave, the team's competence drops. Written, searchable records and good onboarding turn individual experience into institutional capability.</p>"},
  {"type":"code","title":"From Postmortem to Artifacts","language":"python","code":"@postmortem\nclass AutoDenySpike_2026_06:\n    severity = \"SEV1\"\n    summary  = \"Policy index served stale criteria after a failed re-index;\"\\\n               \" model 'correctly' denied against outdated rules.\"\n    root_cause = \"No alert on index staleness; no citation-freshness guardrail.\"\n    # Lessons become DURABLE artifacts, not just prose:\n    artifacts = [\n        new_alert(\"policy_index_age > 24h\"),                 # detection (M13)\n        new_guardrail(\"cited_criterion_must_be_current\"),    # prevention (M29)\n        new_regression_case(\"stale-index-denial\"),           # eval (M06)\n        update_runbook(\"auto_deny_spike\", add_step=\"check index age first\"),\n    ]\n    decision_record = \"DR-042: pin policy_snapshot per determination (M20)\"\n# Searchable, linked from onboarding -> no tribal knowledge"},
  {"type":"quiz","question":"After a serious PA incident, the team holds a postmortem, writes a doc, and files it. Six months later a nearly identical incident recurs. What did knowledge management miss?",
   "options":["The postmortem should have named who was at fault","Lessons weren't converted into durable artifacts (alert, guardrail, regression test, runbook update) and decision records — a filed doc isn't a system change","Postmortems are useless","They should have switched models"],
   "correct":1,
   "explanation":"A document that's read once and filed doesn't change the system. The recurrence shows the lesson never became an alert, a guardrail, a regression test, or a runbook step — the artifacts that actually prevent repetition. And blame-seeking would have driven the real causes into hiding. Like hospital M&M, the point is protocol change, not paperwork."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Postmortem theater: a doc is written and filed but no alert, test, or guardrail changes, so the same incident recurs months later.",
   "Tribal knowledge: the reasoning behind a model pin or routing threshold lives in one engineer's head; they leave, a successor reverts it, and a solved problem returns."]}],
 "takeaway":"Convert every incident and decision into durable artifacts and searchable records through blameless postmortems — so the team's competence compounds and the same mistake can't recur after someone leaves.",
 "labUnderstand":"Review a past postmortem and check whether it produced durable artifacts (alert, test, guardrail, runbook) or just a filed document; identify what would have prevented a recurrence.",
 "labBuild":"Establish a postmortem template that mandates durable artifacts and a decision record, then run it on a real (or simulated) incident and produce the linked alert, regression test, and runbook update."})

MODS.append({
 "id":"M31","track":8,"title":"Capstone — Operating the PA Pipeline",
 "subtitle":"Run the full LLMOps lifecycle on the prior-authorization pipeline for a week",
 "icon":"\U0001F3C1","color":TEAL,
 "topics":[
   "Wiring all eight tracks into one operating system",
   "Handling a simulated week: a drift event, an incident, a migration, an audit",
   "Balancing quality, cost, reliability, and compliance under pressure",
   "Producing the operational evidence that the pipeline is trustworthy"],
 "analogy":{"title":"Running the Restaurant for a Week","text":"You've learned to cook, inspect, plate, and manage suppliers separately. The capstone is opening the doors and running the whole restaurant for a week: the lunch rush (load), a bad-ingredient scare (drift), a walk-in health inspector (audit), a supplier going out of business (model deprecation), and a kitchen fire (incident) — all while every plate still has to be good, on time, and within budget. This is LLMOps as a single operating discipline."},
 "antiPatterns":[
   "Treating the tracks as separate checklists — under a real incident the seams between eval, rollback, and compliance are where things break.",
   "Optimizing one dimension (cost) until another (quality or compliance) silently fails — operations is balancing all of them at once."]})
SVGS["M31"]=svg_cycle("LLMOps Operating System",["Evaluate","Deploy","Monitor","Feedback","Upgrade","Govern"],TEAL,"all 8|tracks live")
MODS[-1].update({
 "crosslinks":[{"type":"ce","label":"CE Capstone"},{"type":"agent","label":"Agent Capstone"},{"type":"platform","label":"Platform Capstone"},{"type":"sdlc","label":"AI-SDLC Capstone"}],
 "sections":[
  {"type":"content","title":"From Eight Tracks to One Operating System","body":"<p>Each track gave you a capability; the capstone makes them one living system around the prior-authorization pipeline. The CI/CD gates (T3) run the eval suite (T2) on every change; the monitors (T4) feed drift detection that triggers a flywheel turn (T5); a model deprecation notice (T6) kicks off a staged migration through the same gates; an incident (T7) fires a runbook that rolls back a bundle and remediates state; and compliance controls (T8) record reproducible evidence through all of it. The skill is operating the <em>seams</em>, not the pieces.</p>"},
  {"type":"content","title":"The Simulated Week","body":"<p>The capstone runs a compressed week against the PA pipeline. <strong>Monday</strong>: a prompt improvement ships through canary. <strong>Tuesday</strong>: a provider repoints a snapshot and drift detectors fire — you diagnose and pin (M20). <strong>Wednesday</strong>: an auto-deny spike incident — you execute the runbook, roll back, and re-adjudicate (M11/M26). <strong>Thursday</strong>: a deprecation notice forces a planned migration (M21/M23). <strong>Friday</strong>: a compliance audit asks you to reproduce three determinations (M14/M29). Throughout, quality, TAT, cost, and the error budget must all stay within bounds. You finish by producing the <strong>operational evidence</strong> that the pipeline is trustworthy — the dashboards, traces, eval history, and audit trail that let a skeptic conclude the AI is safe to rely on.</p>"},
  {"type":"code","title":"The Operating Loop, Wired End-to-End","language":"python","code":"def operate_pa_pipeline(day):\n    # T4 monitor -> T5 feedback / T7 incident\n    health = monitor.snapshot()\n    if drift.check(health).firing:           # T4/T13\n        diagnose_and_pin_snapshot()          # T6/M20\n    if health.auto_deny_rate > THRESH:       # T7\n        run_runbook(\"auto_deny_spike\")       # -> rollback (M11) + remediate\n\n    # T5 flywheel: verified overrides -> gold set -> gated improvement\n    if day.weekly:\n        candidate = flywheel_turn()          # M18\n        if candidate and regression_gate(candidate).passed:   # T2/T3\n            canary_rollout(candidate)        # M09\n\n    # T6 lifecycle\n    for notice in provider.deprecations():   # M23\n        plan_and_stage_migration(notice)     # M21\n\n    # T8 governance: always-on\n    enforce_compliance_controls()            # M29\n    return operational_evidence_report()     # dashboards+traces+evals+audit\n"},
  {"type":"quiz","question":"Mid-capstone, an auto-deny spike hits during an active model migration, and a compliance audit request lands the same hour. What does this scenario test that single-track practice does not?",
   "options":["Raw model quality only","Your ability to operate the seams between tracks under pressure — rolling back without derailing the migration, remediating state, and still producing reproducible audit evidence — balancing quality, reliability, and compliance at once","Whether the newest model is in use","How fast you can write a new prompt"],
   "correct":1,
   "explanation":"Real operations is concurrent and interconnected. The capstone's value is in the seams: an incident response (T7) that respects an in-flight migration (T6), preserves the audit trail (T8), and re-adjudicates state (T5) — all while quality, TAT, cost, and error budget stay in bounds. Mastery is balancing every dimension simultaneously, the way you run a restaurant during a rush, an inspection, and a small fire."},
  {"type":"antipattern","title":"What Goes Wrong","items":[
   "Siloed operation: the tracks are run as independent checklists, and the first multi-track incident exposes the unhandled seams between rollback, migration, and audit.",
   "Single-axis optimization: cost is squeezed until quality or compliance quietly breaches, proving the operator never internalized that LLMOps is balancing all dimensions at once."]}],
 "takeaway":"LLMOps mastery is operating all eight tracks as one system under real pressure — balancing quality, cost, reliability, and compliance simultaneously — so the pipeline stays trustworthy through drift, incidents, migrations, and audits alike.",
 "labUnderstand":"Walk through the simulated week and, at each event, identify which tracks interact and where the seams between them create risk; produce an operating-readiness assessment.",
 "labBuild":"Wire the full PA pipeline operating loop end-to-end (monitor → drift → flywheel → migration → incident → compliance), run the simulated week, and produce the operational evidence report demonstrating the pipeline is trustworthy."})
