# ADD-AI: Architecture Decision Support Plugin for Claude Code

A Claude Code plugin that adds structured architecture and development workflows to any project. Implements ADD 3.0 (Attribute-Driven Design) methodology with 8 specialized agents and 29 skills.

## Features

- **Solution Architect** — ADD 3.0 iterations, ADRs (MADR v3), C4 diagrams (LikeC4)
- **Business Analyst** — Requirements elicitation, utility trees, QAW, use cases, mission threads
- **Project Manager** — Platform-adaptive issue management (GitHub/Bitbucket/GitLab), sprint planning, status reports
- **Backend Developer** — Backend module scaffolding (hexagonal/DDD), feature implementation
- **Frontend Developer** — Frontend scaffolding, UI components, typed API layer (framework-adaptive)
- **DevOps Engineer** — CI/CD pipelines, Docker configuration, deployment (platform-adaptive)
- **Tester** — Unit, integration, E2E, BDD test generation (TDD, framework-adaptive)
- **Code Reviewer** — Code review, PR review, standards audit (read-only)

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
/add-ai:ba-mtw           # Mission Thread Workshop
/add-ai:pm-plan          # Sprint planning
/add-ai:pm-issue         # Issue management (GitHub/Bitbucket/GitLab)
/add-ai:dev-scaffold     # Backend module scaffolding
/add-ai:dev-implement    # Feature implementation
/add-ai:fe-scaffold      # Frontend module scaffolding
/add-ai:fe-component     # UI component generation
/add-ai:ops-pipeline     # CI/CD pipeline generation
/add-ai:ops-docker       # Docker configuration
/add-ai:test-unit        # Unit test generation (TDD)
/add-ai:test-e2e         # E2E test generation
/add-ai:review-code      # Code review
/add-ai:review-pr        # PR review
```

## Conventions

- **Human-in-the-loop**: Agent proposes, you decide. Every response ends with options.
- **Language**: Interaction in Russian, code artifacts in English.
- **Framework-adaptive**: Agents auto-detect project technologies from configs.
- **Platform-adaptive**: PM and DevOps work across GitHub, Bitbucket, GitLab.

See [CLAUDE.md](CLAUDE.md) for full reference.
