# ADD-AI: Architecture Decision Support Plugin

## Overview

Claude Code plugin providing 8 agents and 30 skills for architecture-driven development using ADD 3.0 methodology.

## Plugin Structure

```
.claude-plugin/plugin.json   # Plugin manifest
agents/                      # 8 role-based agents
skills/                      # 30 skills (slash commands)
reference/                   # Convention docs (not auto-loaded, for human/agent reference)
```

## Agents

- **Solution Architect** — ADD 3.0, ADRs (MADR v3), C4 diagrams (LikeC4), design kanban
- **Business Analyst** — Utility trees, QAW, use cases, requirements elicitation, mission threads
- **Project Manager** — Platform-adaptive issue management (GitHub/Bitbucket/GitLab), sprint planning, status reports
- **Backend Developer** — Backend scaffolding (hexagonal/DDD), feature implementation, framework-adaptive
- **Frontend Developer** — Frontend scaffolding, UI components, API layer, framework-adaptive
- **DevOps Engineer** — CI/CD pipelines, Docker, deployment, platform-adaptive
- **Tester** — Unit/integration/E2E/BDD tests, TDD, framework-adaptive
- **Code Reviewer** — Code review, PR review, standards audit (read-only)

## Skills (invoked as `/add-ai:<skill>`)

| Role | Skills |
|------|--------|
| SA | `sa-init`, `sa-iterate`, `sa-adr`, `sa-diagram`, `sa-review`, `sa-kanban`, `sa-resume` |
| BA | `ba-requirements`, `ba-qaw`, `ba-utility-tree`, `ba-usecase`, `ba-mtw` |
| PM | `pm-plan`, `pm-issue`, `pm-status` |
| Backend Dev | `dev-scaffold`, `dev-implement` |
| Frontend Dev | `fe-scaffold`, `fe-component`, `fe-api` |
| DevOps | `ops-pipeline`, `ops-docker`, `ops-deploy` |
| Tester | `test-unit`, `test-integration`, `test-e2e`, `test-bdd` |
| Code Reviewer | `review-code`, `review-pr`, `review-standards` |

## Reference Files

Convention docs in `reference/` (not auto-loaded by plugin, available for agents to read):
- `architecture-conventions.md` — ID formats, directory structure
- `adr-format.md` — MADR v3 template
- `likec4.md` — LikeC4 DSL conventions
- `git-workflow.md` — Git labels, branches, commits (platform-agnostic)
- `nestjs-patterns.md` — Hexagonal architecture patterns
- `gt-context.md` — Example target project context

## Development

```bash
# Test plugin locally
claude --plugin-dir .

# Validate plugin
claude plugin validate .
```
