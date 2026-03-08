---
name: pm-issue
description: Issue management - create, read, update, close issues (GitHub/Bitbucket/GitLab)
user_invocable: true
agent: project-manager
---

# /pm-issue - Issue Management

## What this skill does
CRUD operations for issues across git platforms (GitHub, Bitbucket, GitLab). Auto-detects the platform from git remote URL.

## Usage
- `/pm-issue` - List open issues
- `/pm-issue create <type> <title>` - Create a new issue (type: epic/story/task/bug/spike)
- `/pm-issue view <number>` - View issue details
- `/pm-issue update <number>` - Update an issue
- `/pm-issue close <number>` - Close an issue
- `/pm-issue label <number> <labels>` - Add/remove labels

## Platform Detection

1. Run `git remote get-url origin` to detect the platform
2. Use the appropriate CLI/API:
   - **GitHub** → `gh issue ...`
   - **Bitbucket** → Bitbucket REST API via `curl`
   - **GitLab** → `glab issue ...` or GitLab REST API via `curl`
3. If platform cannot be determined, ask the user

## Issue Creation Flow

1. Ask for (if not provided):
   - Type (epic/story/task/bug/spike)
   - Title
   - Description
   - Role label (sa/ba/pm/dev/fe/ops/test/review)
   - Priority (high/medium/low)
   - Related ADRs or requirements

2. Generate issue body:
   ```markdown
   ## Description
   {description}

   ## Related
   - ADR: {ADR-NNNN}
   - Requirement: {UC-NNN / QA-NNN}

   ## Acceptance Criteria
   - [ ] {criterion 1}
   - [ ] {criterion 2}

   ## Notes
   {additional context}
   ```

3. Create via detected platform CLI/API

4. Report created issue number and URL
