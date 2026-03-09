---
name: nav-resume
description: Resume project session - scan all artifacts, determine SDLC phase, suggest next steps
user_invocable: true
agent: navigator
---

# /nav-resume - Resume Project Session

## What this skill does
Scans all project artifacts across all roles and SDLC phases to determine the current project state and recommend concrete next steps. Single entry point for resuming work in a new session.

## Usage
- `/nav-resume` - Full analysis with artifact inventory and recommendations
- `/nav-resume brief` - One-line status + next action

## Process

0. **Check Complementary Capabilities** (silent — no output unless detected)
   - Check if project knowledge retrieval MCP tools are available in this session
   - Note any first-principles analysis capabilities if present
   - Store results for use in Step 5 recommendations
   - Do NOT add extra sections if nothing complementary is detected

1. **Scan Artifacts** - Check existence and contents of project artifacts per SDLC phase:

   | # | Phase | Completed When | Scan Paths | Next Skill |
   |---|-------|----------------|------------|------------|
   | 1 | Project Tracking | Labels + milestone exist on git platform | `gh label list` / analogs | `/pm-init` |
   | 2 | Initialization | `README.md` + `kanban.md` + `c4/src/model.c4` exist | `docs/architecture/` | `/sa-init` |
   | 3 | Requirements Discovery | Files in `drivers/constraints/` or `drivers/concerns/` or `docs/requirements/` | `docs/requirements/`, `docs/architecture/drivers/` | `/ba-requirements` |
   | 4 | QAW | `qaw-results.md` + >=3 `QA-*.md` files | `docs/requirements/qaw-results.md`, `docs/architecture/drivers/quality-attributes/` | `/ba-qaw` |
   | 5 | Utility Tree | `utility-tree.md` contains H/M/L priorities | `docs/architecture/utility-tree.md`, `docs/requirements/utility-tree.md` | `/ba-utility-tree` |
   | 6 | Use Cases | >=1 `UC-*.md` in `requirements/use-cases/` + driver in `drivers/use-cases/` | `docs/requirements/use-cases/`, `docs/architecture/drivers/use-cases/` | `/ba-usecase` |
   | 7 | Scenarios (optional) | >=1 `SC-*.md` (optional phase, for cross-cutting flows) | `docs/requirements/scenarios/` | `/ba-scenario` |
   | 8 | ADD Iterations | >=1 `ITER-*.md` with full 7 steps | `docs/architecture/iterations/` | `/sa-iterate` |
   | 9 | Sprint Planning | Issues created on git platform | `gh issue list` / analogs | `/pm-plan` |
   | 10 | Implementation | Kanban items in "Implemented" | `docs/architecture/kanban.md` | `/dev-scaffold` |
   | 11 | Testing | Kanban items in "Verified" | `docs/architecture/kanban.md` | `/test-unit` |
   | 12 | Review | PRs with reviews | git platform | `/review-code` |

   Status per phase: **Not Started** / **In Progress** / **Completed**

2. **Determine Current Phase**
   - Evaluate each phase 1-12 independently
   - First phase with status "In Progress" = **current phase**
   - Previous completed = **last completed phase**
   - Next not-started = **recommended next step**
   - Phases are independent (non-linear ordering allowed)

3. **Check Phase Labels on Issues** (if git platform available)
   - Count issues by `phase:*` labels
   - Show cross-role dependencies (e.g., SA work blocking Dev)

4. **Handle Edge Cases**
   - **No `docs/` at all** -> "Project not initialized" + suggest `/pm-init` then `/sa-init`
   - **Partial initialization** -> Phase 2 = "In Progress" + suggest `/sa-init`
   - **Git platform unavailable** -> Skip phases 1, 9-12, focus on 2-8
   - **Non-linear workflow** -> Show each phase independently, "current" = earliest In Progress

5. **Generate Output**

   Full mode:
   ```markdown
   # Project Status — {date}

   ## Current Position
   - **SDLC Phase:** {Requirements / Architecture / Development / Testing / Review}
   - **Last completed phase:** {name} (Phase {N})
   - **Current phase:** {name} (Phase {N})
   - **Status:** {what is done, what remains}

   ## Artifacts
   | Artifact | Count | Path |
   |----------|-------|------|
   | Quality Attributes (QA) | N | docs/architecture/drivers/quality-attributes/ |
   | Use Cases (UC) | N drivers, N specs | docs/requirements/use-cases/ |
   | Scenarios (SC) | N | docs/requirements/scenarios/ |
   | ADRs | N (accepted: N, proposed: N) | docs/architecture/adrs/ |
   | ADD Iterations | N | docs/architecture/iterations/ |
   | Design Decisions (DD) | N | docs/architecture/decisions/ |
   | Constraints (CON) | N | docs/architecture/drivers/constraints/ |
   | Concerns (CRN) | N | docs/architecture/drivers/concerns/ |

   ## Design Kanban
   | Not Addressed | Partially Addressed | Completely Addressed | Implemented | Verified |
   |---------------|---------------------|----------------------|-------------|----------|
   | N             | N                   | N                    | N           | N        |

   ## Issue Tracking
   | Phase | Open | Closed | Total |
   |-------|------|--------|-------|
   | phase:requirements | N | N | N |
   | phase:architecture | N | N | N |
   | phase:development | N | N | N |
   | phase:testing | N | N | N |
   | phase:review | N | N | N |

   ## Recommended Next Steps
   1. {primary action - `/add-ai:<skill>`}
   2. {alternative}
   3. {another option}
   ```

   If complementary capabilities were detected in Step 0, include them
   as additional options in Recommended Next Steps (e.g., "deeper boundary
   analysis available", "project knowledge retrieval available").

   Brief mode — single line:
   ```
   Phase {N} ({name}) in progress. Next: `/add-ai:<skill>` - {description}
   ```
