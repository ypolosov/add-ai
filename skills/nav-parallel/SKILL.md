---
name: nav-parallel
description: Parallel workstream coordination — dependency analysis, wave planning, and coordination rules for concurrent work
user_invocable: true
agent: navigator
---

# Parallel Workstreams

Identifies parallelism in a task and builds a wave-based execution plan.

## What this skill does

Analyzes artifact dependencies to find independent workstreams that can proceed concurrently. Organizes work into waves where each wave's items are independent, and subsequent waves depend on prior ones.

## Usage

- `/nav-parallel {goal}` — analyze dependencies and build wave plan

## Process

1. **Accept** goal from user
2. **Map** required artifacts and their dependencies
3. **Build** dependency graph (which artifacts block which)
4. **Organize** into waves:
   - **Wave 1**: items with no dependencies (can run in parallel)
   - **Wave 2**: items depending only on Wave 1
   - **Wave N**: items depending on Wave N-1
5. **Present** wave plan with coordination rules

## Output Format

```
## Parallel Execution Plan — {goal}

### Dependency Graph
{artifact} → depends on → {artifact}

### Wave 1 (independent — can run in parallel)
| Stream | Skill | Deliverable |
|--------|-------|-------------|
| A | ba-qaw | Quality attributes |
| B | ba-usecase | Use cases |

### Wave 2 (depends on Wave 1)
| Stream | Skill | Deliverable | Depends On |
|--------|-------|-------------|------------|
| C | sa-iterate | ADD iteration | Wave 1A, 1B |

### Coordination Rules
- Commit between waves
- Checkpoint at wave boundaries
- If parallel sessions: use separate branches, merge at wave boundary
```

## Rules

- Navigator is read-only: presents the plan, user executes
- Each wave boundary = commit + checkpoint
- Parallel branches only if user explicitly requests multi-session work
- Single-session default: execute streams sequentially within each wave

## Difference from nav-phased

- `nav-phased` produces a linear sequence of phases
- `nav-parallel` identifies which phases can overlap and organizes them into waves
