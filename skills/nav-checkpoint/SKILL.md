---
name: nav-checkpoint
description: Session checkpoint management — save, restore, and clear uncommitted session state for continuity across sessions
user_invocable: true
agent: navigator
---

# Session Checkpoint

Manages `.claude-checkpoint.md` for session continuity across interrupted sessions.

## What this skill does

Captures the current session state (active task, pending changes, decisions made, next steps) into a checkpoint file that can be restored in a future session. This is session metadata, not an architectural artifact.

## Usage

- `/nav-checkpoint save` — scan git status and context, generate checkpoint file
- `/nav-checkpoint restore` — read checkpoint, show state, suggest skill to continue
- `/nav-checkpoint clear` — suggest removing checkpoint after successful commit

## Checkpoint File Format

File: `.claude-checkpoint.md` (project root, gitignored)

```markdown
# Session Checkpoint — {YYYY-MM-DD HH:MM}

## Active Task
- **Skill:** /add-ai:{skill-name}
- **Step:** {N of M}
- **Context:** {what was being done}

## Pending Changes
- [ ] {file} — {planned change}
- [x] {file} — {done, uncommitted}

## Decisions Made
- {decision description} (for {artifact ID})

## Next Steps
1. {continue from step N}
2. {then do X}
```

## Process

### save

1. Run `git status` to identify modified/untracked files
2. Analyze current conversation context (active skill, progress)
3. Record decisions made during the session
4. Write checkpoint file via Bash (exception for session metadata — Navigator normally read-only)
5. Confirm save to user

### restore

1. Read `.claude-checkpoint.md`
2. Verify referenced files still exist
3. Present session state summary
4. Recommend skill invocation to continue work
5. Offer options: continue, modify plan, or discard checkpoint

### clear

1. Check if pending changes have been committed
2. If yes — suggest deleting checkpoint
3. If uncommitted changes remain — warn user

## Difference from nav-resume

- `nav-resume` reads committed artifacts (backward-looking): "What has been built?"
- `nav-checkpoint` manages uncommitted session state (forward-looking): "What was I doing?"
