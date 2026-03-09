---
name: nav-status
description: Unified project status - kanban progress, issue stats, artifact coverage, SDLC metrics
user_invocable: true
agent: navigator
---

# /nav-status - Unified Project Status

## What this skill does
Generates a comprehensive cross-role project status combining design kanban progress, issue statistics, artifact coverage metrics, and SDLC phase completion. Meta-view of the entire project.

## Usage
- `/nav-status` - Full unified status report
- `/nav-status kanban` - Design kanban progress only
- `/nav-status coverage` - Artifact traceability coverage
- `/nav-status blockers` - Open blockers and cross-role dependencies

## Process

1. **Collect Design Kanban Data**
   - Read `docs/architecture/kanban.md`
   - Count drivers by state: Not Addressed → Partially → Completely → Implemented → Verified
   - Calculate progress percentage

2. **Collect Issue Statistics** (if git platform available)
   - Detect platform and fetch issues via CLI/API
   - Group by `phase:*` labels
   - Group by `role:*` labels
   - Group by `status:*` labels
   - Calculate completion percentage per phase

3. **Analyze Artifact Coverage**
   - **Requirements → Architecture traceability:**
     - Are all (H,H) QA scenarios addressed in ADRs?
     - Do all primary UC have corresponding design decisions?
   - **Architecture → Implementation traceability:**
     - Do ADRs have corresponding issues?
     - Are kanban "Completely Addressed" items planned in sprints?
   - **Requirements → Testing traceability:**
     - Do SC-NNN scenarios have corresponding BDD features?
     - Do UC-NNN have corresponding E2E tests?
   - Show gaps as actionable items

4. **Determine SDLC Phase**
   - Based on artifact presence and completion, classify the project into:
     - **Requirements** — BA artifacts being created
     - **Architecture** — SA iterations in progress
     - **Development** — Code being written
     - **Testing** — Tests being created/run
     - **Review** — PRs under review

5. **Identify Blockers**
   - Unaddressed (H,H) drivers
   - Issues blocked by other issues
   - Missing traceability links
   - Stale issues (no updates for >7 days)

6. **Generate Report**
   ```markdown
   # Unified Project Status — {date}

   ## SDLC Phase
   **{Current Phase}** — {description of what's happening}

   ## Progress Summary
   | Metric | Value |
   |--------|-------|
   | Drivers addressed | N/M (N%) |
   | ADRs accepted | N |
   | Issues completed | N/M (N%) |
   | Test coverage (scenarios) | N/M UC covered |

   ## Design Kanban
   | Not Addressed | Partially | Completely | Implemented | Verified |
   |---------------|-----------|------------|-------------|----------|
   | N             | N         | N          | N           | N        |

   ## Issues by Phase
   | Phase | Open | In Progress | Review | Done | Total |
   |-------|------|-------------|--------|------|-------|

   ## Traceability Gaps
   - {gap 1: e.g., "QA-003 (H,H) has no ADR"}
   - {gap 2: e.g., "ADR-0005 has no implementation issue"}
   - {gap 3: e.g., "SC-001 has no BDD feature file"}

   ## Blockers
   - {blocker 1}

   ## Recommendations
   1. {action 1}
   2. {action 2}
   3. {action 3}
   ```
