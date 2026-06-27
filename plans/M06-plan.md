# M06 Plan — Regression Testing for LLM Apps

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M06 | **Track:** 2 (Eval & Testing) | **Color:** #ec8a6e salmon
- **Title:** Regression Testing for LLM Apps
- **Subtitle:** Catching the change that quietly breaks yesterday's good behavior
- **Icon:** 🌀

## Everyday Analogy: Bridge Load Testing
Before reopening a repaired bridge, engineers don't just check the patched span — they re-run the full load test, because a fix in one place can stress another. LLM regression testing is the same: a prompt tweak to improve oncology approvals can quietly break cardiology denials. You re-run the whole load test (the gold set) on every change, every time.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Why prompt and model changes silently regress unrelated cases
2. Snapshot/golden-output testing under non-determinism
3. Tolerance bands and semantic equivalence instead of exact match
4. Wiring regression gates into CI

## Sections Outline
- **content** — *The Silent Regression*: You edit the prompt so oncology pre-auths approve correctly. Ship it. Two weeks later appeals spike on cardiology denials — your edit shifted how the model weig…
- **content** — *Testing Under Non-Determinism*: Exact-match snapshot tests break instantly when temperature > 0 or the model updates. Instead: pin temperature to 0 for the decision field and assert exact matc…
- **code** (python) — *A Regression Gate*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: A developer fixes one mis-handled oncology case by editing the shared system prompt and re-tests only that case (now passing). Why is this dangerous in the PA pipeline?
    - Correct: A shared-prompt change has global effects; without re-running the full gold set, regressions in other specialties ship undetected
    - Explanation: The system prompt is shared across every specialty, so a fix is a global change. Testing only the fixed case is like load-testing only the repaired bridge span. The full gold set must re-run so a card…
- **antipattern** — *What Goes Wrong*:
    - Spot-fix testing: only the touched case is re-run, so the global side effects of a shared-prompt edit reach production unseen.
    - Brittle exact-match suite: it fails on harmless wording changes, the team marks it 'flaky' and disables it, and real regressions sail through.

## SVG Diagram Plan
A `renderVisual("M06")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#ec8a6e`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `sdlc` → AI-SDLC — CI/CD
- `platform` → Platform M11 Release

## Lab Briefs
- **Understand It:** Take a prompt change and run the full gold set before and after; identify any slice that regressed even though the targeted case improved.
- **Build It with AI:** Build a CI regression gate that diffs against a versioned baseline using exact-match on decisions and semantic match on rationales, with configurable tolerance bands.

## LLMOps Takeaway
Treat every prompt or model change as a global change: re-run the full gold set with semantic tolerance bands so a fix in one slice can't silently regress another.

## Anti-Patterns
- Only testing the case you just fixed — the fix silently breaks ten others you never re-ran.
- Exact-string assertions on non-deterministic output — the suite is so flaky everyone disables it.

## Continuity Notes
Builds on the prior track-2 / sequence module **M05**. Followed by **M07**, which carries these concepts forward.
