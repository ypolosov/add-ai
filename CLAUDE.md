# ADD-AI: Architecture Decision Support Plugin

## Overview

Claude Code plugin providing 9 agents and 36 skills for architecture-driven development using ADD 3.0 methodology.

## Plugin Structure

```
.claude-plugin/plugin.json   # Plugin manifest
agents/                      # 9 role-based agents
skills/                      # 36 skills (slash commands)
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
| Navigator | `nav-resume`, `nav-status`, `nav-consistency`, `nav-checkpoint`, `nav-phased`, `nav-parallel` |
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

### Cross-cutting Skills (any phase)

```
nav-consistency → Consistency review (C4 refs, artifact IDs, tool usage)
nav-checkpoint  → Session checkpoint management
nav-phased      → Phased execution planning
nav-parallel    → Parallel workstream coordination
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

Templates in `reference/templates/`:
- `adr-template.md`, `dd-template.md`, `qaw-template.md`, `utility-tree-template.md`, `usecase-template.md`, `scenario-template.md`, `iteration-template.md`, `issue-template.md`, `constraint-template.md`, `concern-template.md`

## Creation Chain (optional)

add-ai can serve as a methodology layer in a creation chain — a sequence of
creating systems where each creates value for the next.
Agents may benefit from complementary capabilities (first-principles thinking,
project knowledge retrieval) if available in the session. Chain awareness is additive.

## Diagramming Policy

- Never hardcode Mermaid, PlantUML, or D2 syntax in any artifact
- Determine the diagramming tool from `docs/architecture/c4/package.json` in the target project (current standard: LikeC4)
- If `c4/` directory does not exist — ask the user which tool to use
- Exception: `reference/likec4.md` may reference the tool by name (it is a convention doc)

## Project Ecosystem

- add-ai is a universal methodology toolkit (plugin), not specific to any target project
- add-ai knows about fpf-ai (creation chain) but does NOT know about specific target projects
- Never mention other specific target projects by name in CLAUDE.md or plugin code

## Artifact Validation Rules

- Before referencing a C4 element — verify it exists in `model.c4` (or relevant `.c4` files)
- Before cross-referencing an artifact (UC-NNN, QA-NNN, ADR-NNNN, etc.) — verify the file exists
- If the element/artifact does not exist — mark as "to be created" and ask the user

## Self-Review Protocol

Before delivering any artifact, perform a silent self-review:
1. All cross-references point to existing artifacts
2. All C4 elements exist in model.c4
3. No hardcoded diagramming tools (Mermaid, PlantUML, D2)
4. Russian for narrative, English for identifiers
5. Artifact follows the template from `reference/templates/`

## Development

```bash
# Test plugin locally
claude --plugin-dir .

# Validate plugin
claude plugin validate .
```
