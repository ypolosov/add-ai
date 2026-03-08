---
name: review-code
description: Code review - uncommitted changes, files, or branches vs ADRs and patterns
user_invocable: true
agent: code-reviewer
---

# /review-code - Code Review

## What this skill does
Reviews code against architecture decisions (ADRs), project patterns, and coding standards. Read-only — reports issues, suggests fixes.

## Usage
- `/review-code` - Review all uncommitted changes
- `/review-code <file-or-dir>` - Review specific file or directory
- `/review-code branch <branch-name>` - Review changes on a branch vs main

## Process

1. **Collect code to review**:
   - Uncommitted: `git diff` + `git diff --staged`
   - File/dir: read specified paths
   - Branch: `git diff main...<branch>`
2. **Read project context**:
   - ADRs from `docs/architecture/adrs/`
   - Architecture patterns from project docs
   - Existing code conventions (inferred from codebase)
3. **Review against checklist**:
   - Architecture compliance (dependency direction, layer boundaries)
   - ADR compliance (implementation matches decisions)
   - Code quality (no logic in wrong layers, proper error handling)
   - Security (no secrets, input validation at boundaries)
   - Testing (tests exist for changes)
4. **Generate review report**:
   ```
   ## Review Summary
   - Files reviewed: N
   - Issues found: N (critical: N, warning: N, info: N)

   ## Issues
   ### [CRITICAL] {file}:{line} — {title}
   {description}
   Suggested fix: {code snippet}
   Related: {ADR-NNNN}

   ### [WARNING] {file}:{line} — {title}
   ...
   ```
5. **Present report** and suggest options:
   - Create issues for critical findings
   - Pass to developer for fixes
   - Re-review after fixes
