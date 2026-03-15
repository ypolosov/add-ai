---
name: nav-phased
description: Phased execution planning — decompose large tasks into committable phases with session continuity
user_invocable: true
agent: navigator
---

# Phased Execution

Breaks a large task into committable phases, each with a clear deliverable and commit point.

## What this skill does

Takes a task description, identifies required skills and artifacts, and decomposes the work into phases. Each phase is scoped to produce a meaningful commit within a single focused session.

## Usage

- `/nav-phased {task description}` — generate phased execution plan

## Process

1. **Accept** task description from user
2. **Identify** skills and artifacts needed (map to SDLC workflow)
3. **Decompose** into phases:
   - Each phase: 5-15 min of focused work
   - Each phase: one commit with independent value
   - Each phase: uses 1-2 skills maximum
4. **Present** execution plan as a table
5. **After each phase**: user commits + `/nav-checkpoint save`
6. **On interruption**: `/nav-checkpoint restore` in next session

## Output Format

```
## Execution Plan — {task summary}

| Phase | Skill(s) | Deliverable | Commit Message |
|-------|----------|-------------|----------------|
| 1 | sa-init | Architecture skeleton | docs: initialize architecture structure |
| 2 | ba-qaw | Quality attributes | docs: add quality attribute scenarios |
| 3 | sa-iterate | ADD iteration 1 | docs: complete ADD iteration 1 |
| ... | ... | ... | ... |

**Total phases:** N
**Estimated commits:** N
**Checkpoint strategy:** save after each phase
```

## Rules

- Navigator is read-only: presents the plan, user invokes skills
- Each phase must be independently valuable (no "setup only" phases)
- Commit messages follow project's git conventions
- If a phase fails or takes longer than expected, adjust remaining phases

## Difference from nav-resume

- `nav-resume` answers: "Where are we?" (current state)
- `nav-phased` answers: "How do we get there?" (execution roadmap)
