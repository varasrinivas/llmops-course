# M00 Plan — Course Orientation & The LLMOps Manifesto

## Module Identity
- **ID:** M00 | **Track:** 1 (Foundations) | **Color:** #2d6a4f (pine)
- **Title:** Course Orientation & The LLMOps Manifesto
- **Subtitle:** Why "it works on my laptop" is the beginning, not the end
- **Icon:** 🏭

## Everyday Analogy: Launching a Restaurant vs Cooking at Home
Cooking at home = prototype. Running a restaurant = production. The restaurant needs health inspections (eval), consistent recipes (prompt versioning), food safety logs (monitoring), feedback cards (feedback loops), supplier management (model lifecycle), and a plan for when the chef is sick (reliability).

## Key Topics (4)
1. **The Day 2 Problem** — Most AI education stops at "build it." LLMOps starts where they stop. Quality degrades, costs creep, models change.
2. **LLMOps vs MLOps vs DevOps** — LLMs are pre-trained (no training loop), non-deterministic, and behavior changes via prompts not code.
3. **The 6-Stage Lifecycle** — Build → Evaluate → Deploy → Monitor → Feedback → Upgrade (continuous loop).
4. **UCC LLMOps Sandbox** — Setting up eval suite, tracing, and feedback collection on the UCC extraction pipeline.

## SVG Diagram: The LLM Application Lifecycle (circular)
6 nodes in a circle (Build, Evaluate, Deploy, Monitor, Feedback, Upgrade) with "CONTINUOUS LOOP" in the center. T7 Reliability and T8 Governance shown as cross-cutting bars below.

## Cross-Links: None (M00)

## Labs
- **Understand It:** Map a real LLM app's lifecycle stages — identify tooling gaps
- **Build It with AI:** Set up UCC sandbox with eval suite, Langfuse tracing, feedback endpoint

## LLMOps Takeaway
LLMOps is the operational discipline that keeps LLM applications reliable, improving, and cost-effective in production — it's the difference between a successful demo and a successful product.

## Continuity: Builds on nothing (M00). Referenced by all subsequent modules. M01 expands on LLMOps vs MLOps. M04 starts building the eval infrastructure.
