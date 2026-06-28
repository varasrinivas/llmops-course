# Production LLMOps: AI Application Lifecycle

A self-contained, interactive course that teaches ML engineers, SREs, and engineering
managers how to **evaluate, deploy, monitor, upgrade, and govern LLM applications in
production** — the "day 2" discipline that begins where most AI tutorials stop.

The whole course ships as a single dark-theme HTML player (`course/index.html`) with no
build step required to view it. Every concept is taught with an everyday analogy first,
then grounded in one running domain: the **Prior Authorization (PA) Determination
Pipeline** — a health-plan LLM application that reads incoming auth requests (member,
requested CPT/HCPCS, diagnosis ICD-10, clinical notes), matches them against payer
medical-policy criteria, and recommends **approve / deny / pend** with nurse and
medical-director review.

Part of the five-pillar curriculum published at **ai.varasrinivas.com**:
Context Engineering · Building AI Agents with Claude · AI Platform Engineering ·
**Production LLMOps** (this course) · AI-SDLC Series.

---

## Quick start

```powershell
# View the course — just open the file, no build needed
Start-Process "course\index.html"
```

```bash
# Regenerate the course after editing module data
python scripts/generate_course.py

# Backfill plan files from the module data
python scripts/generate_plans.py
```

---

## Course structure

**32 modules across 8 tracks.** Each module includes: an everyday analogy, 4–6 key
topics, content sections, an operational-tooling code sample, a WHY/WHEN quiz,
production anti-patterns, cross-links to sibling courses, a one-sentence takeaway, two
labs ("Understand It" + "Build It with AI"), and an inline SVG diagram.

| Track | Theme | Modules |
|---|---|---|
| 1 | Foundations | M00–M03 |
| 2 | Eval & Testing | M04–M07 |
| 3 | Deployment & Release | M08–M11 |
| 4 | Monitoring & Observability | M12–M15 |
| 5 | Data & Feedback Loops | M16–M19 |
| 6 | Model Lifecycle | M20–M23 |
| 7 | Incident & Reliability | M24–M27 |
| 8 | Governance & Optimization | M28–M31 |

Code examples focus on **operational tooling** — eval scripts, CI/CD gates, monitoring
panels, drift detectors, runbooks, routing, cost attribution, compliance controls — not
model training or prompt engineering.

---

## Repository layout

```
llmops-kit/
├── course/index.html        # The single-file dark-theme course player (generated)
├── scripts/
│   ├── generate_course.py   # Builds course/index.html (dark theme shell + JS engine)
│   ├── modules_t1_4.py      # Module data M00–M15 + shared SVG helpers
│   ├── modules_t5_8.py      # Module data M16–M31
│   ├── generate_plans.py    # Backfills plans/MXX-plan.md from module data
│   └── validate-*.ps1       # PowerShell validation helpers
├── plans/                   # One MXX-plan.md per module
├── labs/                    # Dual-path lab files (M00 seeded)
├── docs/curriculum-map.md   # 32-module blueprint
├── templates/               # module-schema.json
├── .claude/commands/        # Slash commands (plan/build/validate/lab)
└── CLAUDE.md                # Master context for the course generator
```

## Editing a module

The course is generated, so edit the source data rather than the HTML:

1. Edit the module's dict in `scripts/modules_t1_4.py` or `scripts/modules_t5_8.py`.
2. Run `python scripts/generate_course.py` to rebuild `course/index.html`.
3. Run `python scripts/generate_plans.py` to keep the plan files in sync.

Module objects follow `templates/module-schema.json`. The design system, content rules,
and the 20-point quality checklist live in `CLAUDE.md`.

## Slash commands (Claude Code)

| Command | Description |
|---|---|
| `/plan-module MXX` | Create a plan at `plans/MXX-plan.md` |
| `/build-module MXX` | Build a module into the course player |
| `/validate-module MXX` | Run the 20-point quality checklist |
| `/build-lab MXX` | Generate the module's lab files |

---

## Design system

Dark theme (`#14161b` background, `#1c1f26` surfaces, `#e9e5dc` text) with eight
track accent colors. Fonts: Fraunces (display), Inter (body), JetBrains Mono (code),
loaded from Google Fonts CDN. All CSS, JS, and SVG diagrams are inline — the player is
fully self-contained.
