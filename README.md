# ADD-AI: Architecture Decision Support Toolkit for Claude Code

A universal, project-agnostic toolkit that adds structured architecture and development workflows to any project via [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code).

## What It Does

Provides four specialized agents with 16 skills covering the full software delivery lifecycle:

- **Solution Architect** — ADD 3.0 iterations, ADRs (MADR v3), C4 diagrams (LikeC4)
- **Business Analyst** — Requirements elicitation, utility trees, QAW, use cases
- **Project Manager** — GitHub Issues management, sprint planning, status reports
- **Backend Developer** — NestJS module scaffolding (hexagonal/DDD), TDD test generation, code review

## Quick Start

1. Copy the `.claude/` directory into your target project root.
2. Run `/sa-init` to create the architecture documentation scaffold.
3. Customize `.claude/rules/gt-context.md` with your project's context.
4. Run `claude` in your project and use slash commands like `/sa-init`, `/ba-requirements`, `/pm-plan`, `/dev-scaffold`.

## Key Conventions

- **Human-in-the-loop**: The agent proposes, you decide. Every response ends with options.
- **Language**: Interaction in Russian, code artifacts in English.
- **IDs**: `UC-NNN`, `QA-NNN`, `ADR-NNNN`, `CON-NNN`, `CRN-NNN`, `ITER-NN`

See [CLAUDE.md](CLAUDE.md) for full project instructions and command reference.
