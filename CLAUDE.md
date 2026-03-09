# ADD-AI: Architecture Decision Support Plugin

## Overview

Claude Code plugin providing 9 agents and 32 skills for architecture-driven development using ADD 3.0 methodology.

## Plugin Structure

```
.claude-plugin/plugin.json   # Plugin manifest
agents/                      # 9 role-based agents
skills/                      # 32 skills (slash commands)
reference/                   # Convention docs (not auto-loaded, for human/agent reference)
reference/templates/         # Artifact templates (ADR, DD, QAW, UC, SC, etc.)
```

## Agents

- **Navigator** — Cross-role orchestration, SDLC phase tracking, project status analysis (read-only)
- **Solution Architect** — ADD 3.0, ADRs (MADR v3), C4 diagrams (LikeC4), design kanban
- **Business Analyst** — Utility trees, QAW, use cases, requirements elicitation, scenarios
- **Project Manager** — Platform-adaptive project tracking and issue management (GitHub/Bitbucket/GitLab), sprint planning, status reports
- **Backend Developer** — Backend scaffolding (hexagonal/DDD), feature implementation (with TDD mode), framework-adaptive
- **Frontend Developer** — Frontend scaffolding, UI components (with TDD mode), API layer (with TDD mode), framework-adaptive
- **DevOps Engineer** — CI/CD pipelines, Docker, deployment, platform-adaptive
- **Tester** — Unit/integration/E2E/BDD tests, TDD, framework-adaptive
- **Code Reviewer** — Code review, PR review, standards audit (read-only)

## Skills (invoked as `/add-ai:<skill>`)

| Role | Skills |
|------|--------|
| Navigator | `nav-resume`, `nav-status` |
| SA | `sa-init`, `sa-iterate`, `sa-adr`, `sa-diagram`, `sa-review`, `sa-kanban` |
| BA | `ba-requirements`, `ba-qaw`, `ba-utility-tree`, `ba-usecase`, `ba-scenario` |
| PM | `pm-init`, `pm-plan`, `pm-issue`, `pm-status` |
| Backend Dev | `dev-scaffold`, `dev-implement` |
| Frontend Dev | `fe-scaffold`, `fe-component`, `fe-api` |
| DevOps | `ops-pipeline`, `ops-docker`, `ops-deploy` |
| Tester | `test-unit`, `test-integration`, `test-e2e`, `test-bdd` |
| Code Reviewer | `review-code`, `review-pr`, `review-standards` |

## SDLC Workflow

```
1. nav-resume     → Assess project state (or first run)
2. pm-init        → Initialize tracking (boards, labels, milestone)
3. sa-init        → Initialize architecture
4. ba-*           → Gather requirements (UC, QA, CON, CRN, SC)
5. sa-iterate     → ADD 3.0 iterations (ADR, DD, C4)
6. pm-plan        → Sprint planning (stories → issues)
7. dev/fe/ops-*   → Implementation (with optional TDD)
8. test-*         → Testing (unit, integration, E2E from SC, BDD from SC)
9. review-*       → Code review and PR review
10. nav-status    → Metrics and progress
```

## Unified Artifact Model

```
UC-NNN  — Use Case (atomic, reusable)
QA-NNN  — Quality Attribute (6-part scenario)
SC-NNN  — Scenario (composite: UC steps + QA checkpoints)
CON-NNN — Constraint
CRN-NNN — Concern
DD-NNN  — Design Decision
ADR-NNNN — Architecture Decision Record
ITER-NN — Iteration log
```

## Reference Files

Convention docs in `reference/` (not auto-loaded by plugin, available for agents to read):
- `architecture-conventions.md` — ID formats, directory structure
- `adr-format.md` — MADR v3 template
- `likec4.md` — LikeC4 DSL conventions
- `git-workflow.md` — Git labels (incl. phase labels), branches, commits (platform-agnostic)
- `nestjs-patterns.md` — Hexagonal architecture patterns
- `tactics-catalog.md` — ADD 3.0 reference architectures, patterns, and tactics
- `gt-context.md` — Example target project context

Templates in `reference/templates/`:
- `adr-template.md`, `dd-template.md`, `qaw-template.md`, `utility-tree-template.md`, `usecase-template.md`, `scenario-template.md`, `iteration-template.md`, `issue-template.md`, `constraint-template.md`, `concern-template.md`

## Creation Chain (optional)

add-ai can serve as a methodology layer in a creation chain — a sequence of
creating systems where each creates value for the next.
Agents may benefit from complementary capabilities (first-principles thinking,
project knowledge retrieval) if available in the session.
See `reference/creation-chain.md` for capability needs. Chain awareness is additive.

## Development

```bash
# Test plugin locally
claude --plugin-dir .

# Validate plugin
claude plugin validate .
```
