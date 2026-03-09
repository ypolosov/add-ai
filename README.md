# ADD-AI: Architecture Decision Support Plugin for Claude Code

A Claude Code plugin that adds structured architecture and development workflows to any project. Implements ADD 3.0 (Attribute-Driven Design) methodology with 9 specialized agents and 32 skills.

## Features

- **Navigator** — Cross-role orchestration, SDLC phase tracking, project status analysis (read-only entry point)
- **Solution Architect** — ADD 3.0 iterations, ADRs (MADR v3), C4 diagrams (LikeC4), design kanban
- **Business Analyst** — Requirements elicitation, utility trees, QAW, use cases, scenarios
- **Project Manager** — Platform-adaptive project tracking and issue management (GitHub/Bitbucket/GitLab), sprint planning, status reports
- **Backend Developer** — Backend module scaffolding (hexagonal/DDD), feature implementation (with TDD mode)
- **Frontend Developer** — Frontend scaffolding, UI components, typed API layer (framework-adaptive, with TDD mode)
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
# Navigator
/add-ai:nav-resume       # Assess project state, recommend next steps
/add-ai:nav-status       # Project metrics and progress

# Solution Architect
/add-ai:sa-init          # Initialize architecture docs
/add-ai:sa-iterate       # Run ADD 3.0 iteration
/add-ai:sa-adr           # Create/update ADRs (MADR v3)
/add-ai:sa-diagram       # Create/update C4 diagrams (LikeC4)
/add-ai:sa-review        # Architecture review
/add-ai:sa-kanban        # Design kanban management

# Business Analyst
/add-ai:ba-requirements  # Requirements elicitation
/add-ai:ba-qaw           # Quality Attribute Workshop
/add-ai:ba-utility-tree  # Utility tree with priorities
/add-ai:ba-usecase       # Use case specification
/add-ai:ba-scenario      # Cross-cutting scenarios (SC-NNN)

# Project Manager
/add-ai:pm-init          # Initialize project tracking
/add-ai:pm-plan          # Sprint planning
/add-ai:pm-issue         # Issue management (GitHub/Bitbucket/GitLab)
/add-ai:pm-status        # Status report generation

# Backend Developer
/add-ai:dev-scaffold     # Backend module scaffolding
/add-ai:dev-implement    # Feature implementation

# Frontend Developer
/add-ai:fe-scaffold      # Frontend module scaffolding
/add-ai:fe-component     # UI component generation
/add-ai:fe-api           # Typed API layer generation

# DevOps Engineer
/add-ai:ops-pipeline     # CI/CD pipeline generation
/add-ai:ops-docker       # Docker configuration
/add-ai:ops-deploy       # Deployment configuration

# Tester
/add-ai:test-unit        # Unit test generation (TDD)
/add-ai:test-integration # Integration test generation
/add-ai:test-e2e         # E2E test generation
/add-ai:test-bdd         # BDD scenarios (Gherkin)

# Code Reviewer
/add-ai:review-code      # Code review
/add-ai:review-pr        # PR review
/add-ai:review-standards # Standards audit
```

## Conventions

- **Human-in-the-loop**: Agent proposes, you decide. Every response ends with options.
- **Language**: Interaction in Russian, code artifacts in English.
- **Framework-adaptive**: Agents auto-detect project technologies from configs.
- **Platform-adaptive**: PM and DevOps work across GitHub, Bitbucket, GitLab.

See [CLAUDE.md](CLAUDE.md) for full reference.
