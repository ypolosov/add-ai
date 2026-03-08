---
name: sa-resume
description: Resume ADD 3.0 session - scan project artifacts, determine current phase, suggest next steps
user_invocable: true
agent: solution-architect
---

# /sa-resume - Resume ADD 3.0 Session

## What this skill does
Scans existing project artifacts to determine the current ADD 3.0 phase and recommends concrete next steps. Single entry point for resuming architecture work in a new session.

## Usage
- `/sa-resume` - Full analysis with artifact inventory and recommendations
- `/sa-resume brief` - One-line status + next action

## Process

1. **Scan Artifacts** - Check existence and contents of project artifacts per phase:

   | # | Phase | Completed When | Scan Paths | Next Skill |
   |---|-------|----------------|------------|------------|
   | 1 | Initialization | `README.md` + `kanban.md` + `c4/src/model.c4` exist | `docs/architecture/` | `/sa-init` |
   | 2 | Requirements Discovery | Files in `drivers/constraints/` or `drivers/concerns/` or `docs/requirements/` | `docs/requirements/`, `docs/architecture/drivers/` | `/ba-requirements` |
   | 3 | QAW | `qaw-results.md` + >=3 `QA-*.md` files | `docs/requirements/qaw-results.md`, `docs/architecture/drivers/quality-attributes/` | `/ba-qaw` |
   | 4 | Utility Tree | `utility-tree.md` contains H/M/L priorities | `docs/architecture/utility-tree.md`, `docs/requirements/utility-tree.md` | `/ba-utility-tree` |
   | 5 | Use Cases | >=1 `UC-*.md` in `requirements/use-cases/` + driver in `drivers/use-cases/` | `docs/requirements/use-cases/`, `docs/architecture/drivers/use-cases/` | `/ba-usecase` |
   | 6 | Mission Threads (Extension) | >=1 `MT-*.md` (optional phase, beyond ADD 3.0) | `docs/requirements/mission-threads/` | `/ba-mtw` |
   | 7 | ADD Iterations | >=1 `ITER-*.md` with full 7 steps | `docs/architecture/iterations/` | `/sa-iterate` |
   | 8 | Sprint Planning | Issues created on git platform | `gh issue list` / analogs | `/pm-plan` |
   | 9 | Implementation | Kanban items in "Implemented" | `docs/architecture/kanban.md` | `/dev-scaffold` |
   | 10 | Testing | Kanban items in "Verified" | `docs/architecture/kanban.md` | `/test-unit` |
   | 11 | Review | PRs with reviews | git platform | `/review-code` |

   Status per phase: **Not Started** / **In Progress** / **Completed**

2. **Determine Current Phase**
   - Evaluate each phase 1-11 independently
   - First phase with status "In Progress" = **current phase**
   - Previous completed = **last completed phase**
   - Next not-started = **recommended next step**
   - Phases are independent (non-linear ordering allowed)

3. **Handle Edge Cases**
   - **No `docs/` at all** -> "Project not initialized" + suggest `/sa-init`
   - **Partial initialization** -> Phase 1 = "In Progress" + suggest `/sa-init`
   - **Git platform unavailable** -> Skip phases 8-11, focus on 1-7
   - **Non-linear workflow** -> Show each phase independently, "current" = earliest In Progress

4. **Generate Output**

   Full mode:
   ```markdown
   # ADD 3.0 Project Status - {date}

   ## Current Position
   - **Last completed phase:** {name} (Phase {N})
   - **Current phase:** {name} (Phase {N})
   - **Status:** {what is done, what remains}

   ## Artifacts
   | Artifact | Count | Path |
   |----------|-------|------|
   | Quality Attributes (QA) | N | docs/architecture/drivers/quality-attributes/ |
   | Use Cases (UC) | N drivers, N specs | docs/requirements/use-cases/ |
   | ADRs | N (accepted: N, proposed: N) | docs/architecture/adrs/ |
   | ADD Iterations | N | docs/architecture/iterations/ |
   | Design Decisions (DD) | N | docs/architecture/decisions/ |
   | Constraints (CON) | N | docs/architecture/drivers/constraints/ |
   | Concerns (CRN) | N | docs/architecture/drivers/concerns/ |
   | Mission Threads (MT) | N | docs/requirements/mission-threads/ |

   ## Design Kanban
   | Not Addressed | Partially Addressed | Completely Addressed | Implemented | Verified |
   |---------------|---------------------|----------------------|-------------|----------|
   | N             | N                   | N                    | N           | N        |

   ## Recommended Next Steps
   1. {primary action - `/add-ai:<skill>`}
   2. {alternative}
   3. {another option}
   ```

   Brief mode — single line:
   ```
   Phase {N} ({name}) in progress. Next: `/add-ai:<skill>` - {description}
   ```
