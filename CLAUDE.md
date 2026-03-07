# ADD-AI: Architecture Decision Support Plugin

## Overview

Claude Code plugin providing 4 agents and 16 skills for architecture-driven development using ADD 3.0 methodology.

## Plugin Structure

```
.claude-plugin/plugin.json   # Plugin manifest
agents/                      # 4 role-based agents
skills/                      # 16 skills (slash commands)
reference/                   # Convention docs (not auto-loaded, for human/agent reference)
```

## Agents

- **Solution Architect** — ADD 3.0, ADRs (MADR v3), C4 diagrams (LikeC4), design kanban
- **Business Analyst** — Utility trees, QAW, use cases, requirements elicitation
- **Project Manager** — GitHub Issues, sprint planning, status reports
- **Backend Developer** — NestJS scaffolding (hexagonal/DDD), TDD, code review

## Skills (invoked as `/add-ai:<skill>`)

| Role | Skills |
|------|--------|
| SA | `sa-init`, `sa-iterate`, `sa-adr`, `sa-diagram`, `sa-review`, `sa-kanban` |
| BA | `ba-utility-tree`, `ba-qaw`, `ba-usecase`, `ba-requirements` |
| PM | `pm-plan`, `pm-issue`, `pm-status` |
| Dev | `dev-scaffold`, `dev-test`, `dev-review` |

## Reference Files

Convention docs in `reference/` (not auto-loaded by plugin, available for agents to read):
- `architecture-conventions.md` — ID formats, directory structure
- `adr-format.md` — MADR v3 template
- `likec4.md` — LikeC4 DSL conventions
- `github-workflow.md` — GitHub labels, branches, commits
- `nestjs-patterns.md` — Hexagonal architecture patterns
- `gt-context.md` — Example target project context

## Development

```bash
# Test plugin locally
claude --plugin-dir .

# Validate plugin
claude plugin validate .
```
