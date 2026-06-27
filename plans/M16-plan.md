# M16 Plan — Human Feedback Collection

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M16 | **Track:** 5 (Data & Feedback Loops) | **Color:** #8fc7a8 sage
- **Title:** Human Feedback Collection
- **Subtitle:** Designing capture so the corrections you need actually get recorded
- **Icon:** 📝

## Everyday Analogy: Hotel Comment Cards
A blank comment card gets ignored; a card that asks 'How was the room? The breakfast? The check-in?' gets filled in. The structure is what produces useful feedback. For the PA tool, a bare 'wrong' button yields noise; a capture flow that records the corrected determination, the controlling criterion, and a one-line reason yields training-grade data. Design the card and you design the data.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Explicit vs implicit feedback, and why explicit is rare
2. Capturing the structured correction, not just a thumbs-down
3. Reducing reviewer friction so feedback gets given
4. Provenance: who corrected what, when, and why

## Sections Outline
- **content** — *Why Explicit Feedback Is Rare — and How to Get It*: People rarely volunteer feedback unless it's nearly free to give. A standalone 'rate this' widget on the PA tool will be ignored under reviewer workload. The tr…
- **content** — *Capture the Correction, With Provenance*: A thumbs-down tells you something was wrong; it doesn't tell you the right answer. Useful feedback is structured: the corrected determination, the controlling p…
- **code** (python) — *A Structured Feedback Schema*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: You add a thumbs-up/down to the PA tool and get few responses; the data that arrives is just 'down'. What's the more effective design?
    - Correct: Capture the correction inline from the reviewer's existing workflow — the changed decision, the controlling criterion, and a reason — with full provenance
    - Explanation: Bare thumbs-down is high-friction and low-information. Capturing the correction as a byproduct of the work the reviewer already does — the before/after decision, the criterion, the reason, and who mad…
- **antipattern** — *What Goes Wrong*:
    - Binary-only feedback: you learn that 12% of suggestions were 'wrong' but have no corrected labels to learn from.
    - High-friction capture: a clunky feedback modal is dismissed, so you record a tiny, biased fraction of the corrections actually occurring.

## SVG Diagram Plan
A `renderVisual("M16")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#8fc7a8`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `agent` → Agent M15 HITL
- `platform` → Platform M10 Feedback

## Lab Briefs
- **Understand It:** Evaluate an existing feedback mechanism for friction and information content; estimate what fraction of real corrections it actually captures and why.
- **Build It with AI:** Design and implement an inline structured-correction capture for the PA tool recording corrected decision, controlling criterion, reason code, and reviewer provenance.

## LLMOps Takeaway
Collect feedback as a structured, provenance-tagged byproduct of the reviewer's existing workflow — because a thumbs-down isn't a label, and a chore won't get done.

## Anti-Patterns
- Capturing only a binary thumbs-down — you know something was wrong but not what the right answer was.
- A feedback flow so clunky reviewers skip it — you collect 2% of the corrections happening in reality.

## Continuity Notes
Builds on the prior track-5 / sequence module **M15**. Followed by **M17**, which carries these concepts forward.
