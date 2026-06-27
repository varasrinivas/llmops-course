# M15 Plan — User Experience Monitoring

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M15 | **Track:** 4 (Monitoring & Observability) | **Color:** #e3a52c maize
- **Title:** User Experience Monitoring
- **Subtitle:** Measuring what reviewers and members actually experience, not just what the model emits
- **Icon:** 👥

## Everyday Analogy: Watching How Customers Move Through a Store
A store doesn't only count sales; it watches where shoppers pause, what they pick up and put back, and where they abandon their carts. Those behaviors reveal problems no survey captures. UX monitoring for the PA tool is the same: how often a nurse overrides the suggested determination, edits the rationale, or escalates — these behaviors are a continuous, honest read on quality that no offline eval gives you.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Behavioral signals: override, edit, escalation, and abandonment
2. Implicit feedback as a free, high-volume quality proxy
3. Turnaround time and the member-facing experience
4. Closing the loop from UX signals to eval cases

## Sections Outline
- **content** — *Behavior Is the Best Free Signal*: Explicit feedback (a thumbs-down) is rare and biased. Implicit behavioral signals are abundant and honest. When a nurse reviewer overrides the suggested determi…
- **content** — *Member Experience and the Closed Loop*: Beyond reviewers, the member experiences the determination as turnaround time and outcome. TAT against regulatory deadlines is a UX metric, not just an SLO. The…
- **code** (python) — *Capturing Implicit Signals*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA model's offline eval looks healthy, but nurses override its suggested determination on 28% of orthopedic cases. What does this signal, and what should you do with it?
    - Correct: A real quality gap the offline set doesn't cover; mine those overrides and add the patterns to the gold set so future releases are measured on them
    - Explanation: A 28% override rate is production telling you the offline eval doesn't represent orthopedic reality. The override behavior is a free, honest quality signal; the right move is to mine those cases and f…
- **antipattern** — *What Goes Wrong*:
    - Output-only view: a high silent override rate goes unmeasured, so leadership believes quality is fine while reviewers route around the tool.
    - Open loop: UX signals are dashboarded but never converted into eval cases, so the same failure patterns survive every release.

## SVG Diagram Plan
A `renderVisual("M15")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#e3a52c`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `agent` → Agent M15 HITL
- `platform` → Platform M28 UX Metrics

## Lab Briefs
- **Understand It:** Analyze a week of reviewer actions to compute override/edit/escalation rates by slice and identify the slice where the tool is least trusted.
- **Build It with AI:** Instrument implicit UX signal capture in the PA tool and build a weekly job that clusters overrides and promotes recurring patterns into the gold eval set.

## LLMOps Takeaway
Reviewer and member behavior — overrides, edits, escalations, turnaround — is your highest-volume honest quality signal, and its value is realized only when you feed it back into the gold set.

## Anti-Patterns
- Measuring only model outputs, never reviewer behavior — you miss that nurses silently override 30% of suggestions.
- Collecting UX signals but never feeding them back into the gold set — the same failures recur release after release.

## Continuity Notes
Builds on the prior track-4 / sequence module **M14**. Followed by **M16**, which carries these concepts forward.
