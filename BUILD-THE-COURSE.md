# BUILD-THE-COURSE.md — Production LLMOps: AI Application Lifecycle

## Quick Start
```powershell
cd llmops-kit
claude                              # reads CLAUDE.md automatically
Start-Process "course\index.html"   # preview M00
```

## Pipeline: `/plan-module` → `/build-module` → `/validate-module` → `/build-lab` → `/clear`

## Build Order
1. **Calibration:** M01 (foundations), then M24 (incident management — very different content)
2. **Track-by-track:** T1→T2→T3→T4→T5→T6→T7→T8
3. **Capstone last:** M31 references all tracks

## Key Differentiator
Code examples focus on **operational tooling**: eval scripts, CI/CD configs, monitoring dashboards, runbooks, drift detectors, feedback pipelines, migration playbooks. NOT model training, NOT prompt engineering (that's CE), NOT platform infrastructure (that's AI Platform).

## File Layout
```
llmops-kit/
├── CLAUDE.md                    ← Master context
├── .claude/commands/            ← 4 slash commands
├── course/index.html            ← Player (M00 seeded)
├── docs/curriculum-map.md       ← 32-module blueprint
├── labs/M00-lab-*.md            ← Reference labs
├── plans/M00-plan.md            ← Reference plan
├── templates/module-schema.json
└── scripts/validate-*.ps1
```

## Quality Standards
- ✅ Analogy BEFORE technical explanation (restaurants, hospitals, factories, airlines)
- ✅ UCC Lien domain example in every module
- ✅ WHY/WHEN quiz questions with production scenarios
- ✅ Anti-patterns with real production failure consequences
- ✅ Code focused on ops tooling (eval, CI/CD, monitoring, runbooks)
- ✅ One-sentence LLMOps Takeaway per module
- ✅ Cross-links to CE, Agent, Platform, and SDLC courses
