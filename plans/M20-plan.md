# M20 Plan — Model Versioning & Pinning

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M20 | **Track:** 6 (Model Lifecycle) | **Color:** #cf6f5f brick
- **Title:** Model Versioning & Pinning
- **Subtitle:** Controlling exactly which model snapshot serves each determination
- **Icon:** 📌

## Everyday Analogy: Pharmaceutical Lot Numbers
Every batch of medicine carries a lot number, so if a problem appears the manufacturer can trace exactly which batch, made when, with which inputs. Model pinning is the lot number for your determinations: pin the exact snapshot, record it on every decision, and you can trace, reproduce, and recall. Run on 'latest' and you're dispensing unlabeled pills.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Pinned snapshots vs floating aliases ('latest')
2. Why a silent provider update is an unreviewed deployment
3. Tying every determination to its exact model version
4. Coordinated, evaluated version bumps

## Sections Outline
- **content** — *Pin the Snapshot, Always*: Foundation-model aliases like 'latest' float: the provider can repoint them to a new snapshot whenever they ship. If your PA pipeline targets a floating alias,…
- **content** — *Record the Lot Number on Every Decision*: Pinning controls input; recording enables accountability. Stamp every determination with its model snapshot (plus prompt and policy versions — the M01 fingerpri…
- **code** (python) — *Pin and Stamp*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA pipeline targets the model alias 'latest' to always get improvements. One morning determinations shift noticeably with no change on your side. What happened, and what's the fix?
    - Correct: The provider repointed 'latest' to a new snapshot — an unreviewed deployment; pin an exact snapshot and treat version bumps as evaluated releases
    - Explanation: A floating alias let the provider deploy a new model into your production path without your review. In a regulated determination workflow that's unacceptable: pin the exact snapshot, stamp it on every…
- **antipattern** — *What Goes Wrong*:
    - 'latest' in production: a silent provider snapshot bump shifts determinations overnight with no rollback path and no audit trail.
    - Unstamped decisions: a bad snapshot is identified, but you can't tell which determinations it touched, so you can't scope a recall or defend an appeal.

## SVG Diagram Plan
A `renderVisual("M20")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#cf6f5f`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `platform` → Platform M05 Multi-Provider
- `sdlc` → AI-SDLC — Model Governance

## Lab Briefs
- **Understand It:** Inspect a pipeline's model configuration for floating aliases and check whether determinations record their snapshot; rate the audit and rollback risk.
- **Build It with AI:** Refactor the PA pipeline to pin an exact snapshot, stamp model+prompt+policy versions on every determination, and gate any version bump through regression + canary.

## LLMOps Takeaway
Pin the exact model snapshot and stamp it on every determination — so a provider update is a decision you make and evaluate, not one that happens to you, and every decision is reproducible.

## Anti-Patterns
- Pointing at a floating alias like 'latest' — the provider updates it and your behavior shifts with no PR and no rollback.
- Not recording the model snapshot per determination — during an appeal you can't say which model decided.

## Continuity Notes
Builds on the prior track-6 / sequence module **M19**. Followed by **M21**, which carries these concepts forward.
