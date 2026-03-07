# ADD-AI: Architecture Decision Support Plugin for Claude Code

A Claude Code plugin that adds structured architecture and development workflows to any project. Implements ADD 3.0 (Attribute-Driven Design) methodology with 4 specialized agents and 16 skills.

## Features

- **Solution Architect** — ADD 3.0 iterations, ADRs (MADR v3), C4 diagrams (LikeC4)
- **Business Analyst** — Requirements elicitation, utility trees, QAW, use cases
- **Project Manager** — GitHub Issues management, sprint planning, status reports
- **Backend Developer** — NestJS module scaffolding (hexagonal/DDD), TDD, code review

## Installation

### From GitHub (marketplace)

```bash
claude plugin marketplace add ypolosov/add-ai
claude plugin install add-ai
```

### Local development

```bash
claude --plugin-dir /path/to/add-ai
```

## Usage

After installation, skills are available as `/add-ai:<skill>`:

```
/add-ai:sa-init          # Initialize architecture docs
/add-ai:sa-iterate       # Run ADD 3.0 iteration
/add-ai:ba-requirements  # Requirements elicitation
/add-ai:pm-plan          # Sprint planning
/add-ai:dev-scaffold     # NestJS module scaffolding
```

## Conventions

- **Human-in-the-loop**: Agent proposes, you decide. Every response ends with options.
- **Language**: Interaction in Russian, code artifacts in English.

See [CLAUDE.md](CLAUDE.md) for full reference.
