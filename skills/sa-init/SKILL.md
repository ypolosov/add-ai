---
name: sa-init
description: Initialize docs/architecture/ structure with all required files and LikeC4 project
user_invocable: true
agent: solution-architect
---

# /sa-init - Initialize Architecture Documentation

## What this skill does
Creates the complete `docs/architecture/` structure with starter files for the ADD 3.0 process.

## Steps

### Step 0: Establish Context (ADD 3.0 Prerequisites)

Before creating any artifacts, establish design context:

1. Ask: "Какова цель дизайна?"
   - A) **Estimation** — грубая оценка для предложения/бюджета (high-level decisions only)
   - B) **Exploratory prototype** — spike для снижения неопределённости (focus on risky areas)
   - C) **Production development** — полная архитектура для реализации (comprehensive design)

2. Ask: "Каков контекст системы?"
   - A) **Greenfield (mature domain)** — есть reference architectures и стандарты, moderate risk
   - B) **Greenfield (novel domain)** — высокая неопределённость, нужны прототипы, high risk
   - C) **Brownfield** — расширение существующей системы, existing constraints dominate
   - D) **Legacy replacement** — замена legacy через Strangler Fig или parallel run

Record answers in `docs/architecture/README.md` (see Step 3).

### Step 1: Check Existing State

1. Check if `docs/architecture/` already exists and has content
   - If yes, ask user whether to skip, merge, or overwrite

### Step 2: Create Directory Structure
   ```
   docs/architecture/
     README.md
     utility-tree.md
     kanban.md
     c4/
       package.json
       src/
         specification.c4
         model.c4
         views.c4
         deployment.c4
     adrs/
       0000-template.md
     drivers/
       use-cases/
       quality-attributes/
       constraints/
       concerns/
     decisions/
     views/
     iterations/
   ```

### Step 3: Initialize README.md

Initialize `docs/architecture/README.md` with:
   - Project name and description
   - **Project Context** section with Design Purpose and System Context from Step 0
   - Links to all sections
   - Architecture principles placeholder

```markdown
## Project Context
- **Design Purpose:** {estimation | prototype | development}
- **System Context:** {greenfield-mature | greenfield-novel | brownfield | legacy-replacement}
- **Date:** {YYYY-MM-DD}
```

### Step 4: Initialize Kanban Board

Initialize `docs/architecture/kanban.md` with columns:
   - Not Addressed | Partially Addressed | Completely Addressed | Implemented | Verified

### Step 5: Initialize Utility Tree

Initialize `docs/architecture/utility-tree.md` with empty tree structure

### Step 6: Initialize LikeC4 Project
   - `c4/package.json` with likec4 dependency
   - `c4/src/specification.c4` with basic C4 element kinds
   - `c4/src/model.c4` with system context stub
   - `c4/src/views.c4` with initial view definitions
   - `c4/src/deployment.c4` with empty deployment block

### Step 7: Create Templates
   - ADR template at `adrs/0000-template.md` (MADR v3)
   - DD template at `decisions/DD-000-template.md`

### Step 8: Report & Next Steps

Report what was created and suggest next steps based on Design Purpose:

- **Estimation**: suggest `/ba-requirements` → `/ba-utility-tree` → `/sa-iterate` (1-2 iterations)
- **Prototype**: suggest `/ba-qaw` → `/sa-iterate` focusing on high-risk areas
- **Development**: suggest `/ba-requirements` → `/ba-qaw` → `/ba-utility-tree` → `/sa-iterate`
