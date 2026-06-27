# M07 Plan — Adversarial Testing & Red-Teaming

> Backfilled from the generator module data (`scripts/modules_*.py`) to match the
> shipped `course/index.html`. Domain anchor: **Prior Authorization (PA) Determination Pipeline**.

## Module Identity
- **ID:** M07 | **Track:** 2 (Eval & Testing) | **Color:** #ec8a6e salmon
- **Title:** Adversarial Testing & Red-Teaming
- **Subtitle:** Attacking your own LLM app before someone else does
- **Icon:** 🥷

## Everyday Analogy: Banks Hiring Burglars
Banks pay professional burglars to break into their own vaults, because the only way to trust a defense is to attack it on your own terms. Red-teaming an LLM app is the same: you deliberately craft malicious PA submissions — injected instructions hidden in a faxed note, coercion to auto-approve — so you find the holes before a bad actor (or a careless prompt) does in production.

*Mapping:* the analogy's elements map onto the PA pipeline concepts introduced in this module's topics and content sections.

## Key Topics (4)
1. Prompt injection via untrusted clinical documents
2. Jailbreaks that coerce inappropriate approvals or denials
3. PHI exfiltration and policy-bypass attacks
4. Building an automated adversarial suite that runs continuously

## Sections Outline
- **content** — *The PA Threat Model*: The PA pipeline ingests untrusted text: faxed clinical notes, provider portal free-text, attached PDFs. That is an injection surface. An attacker (or a careless…
- **content** — *Automate It, Run It Forever*: A launch-day red-team rots immediately: new jailbreak families appear and model updates change susceptibility. Convert findings into an automated adversarial su…
- **code** (python) — *An Adversarial Suite*: operational tooling snippet in the PA domain.
- **quiz** (WHY/WHEN) — Q: Your PA pipeline reads clinical notes faxed by provider offices and feeds them into the model's context. What is the core security mistake to avoid?
    - Correct: Treating the untrusted document text as trusted instructions the model may obey, enabling prompt injection that alters determinations
    - Explanation: The faxed note is untrusted input, but if it's concatenated into the prompt without isolation, an injected instruction can hijack the determination. Treating document content as data-to-analyze (never…
- **antipattern** — *What Goes Wrong*:
    - Untrusted-as-trusted: injected text in a fax flips determinations or exfiltrates PHI, surfacing as a HIPAA incident rather than a bug ticket.
    - Static one-time red-team: the suite isn't re-run, a model update reopens a jailbreak family, and the regression is invisible until exploited.

## SVG Diagram Plan
A `renderVisual("M07")` case renders a dark-theme diagram (surface `#1c1f26`, track color `#ec8a6e`) reinforcing the analogy and the module's core flow. Labels in JetBrains Mono, titles in Fraunces.

## Cross-Links
- `ce` → CE M20 Guardrails
- `platform` → Platform M12 Safety

## Lab Briefs
- **Understand It:** Take a working PA prompt and attempt three injection attacks via the clinical-note field; document which succeed and why the prompt structure allowed it.
- **Build It with AI:** Build an adversarial test suite (injection, jailbreak, PHI-exfil) with expected safe behaviors and an attack-success-rate metric, and wire it into CI next to the gold set.

## LLMOps Takeaway
Treat every document the PA pipeline ingests as hostile and run an automated adversarial suite continuously — because injection and PHI-exfiltration are compliance incidents, not edge cases.

## Anti-Patterns
- Treating uploaded clinical documents as trusted text the model can obey — an injected line flips a denial to an approval.
- One-time red-team at launch, never re-run — new attacks and model updates reopen old holes.

## Continuity Notes
Builds on the prior track-2 / sequence module **M06**. Followed by **M08**, which carries these concepts forward.
