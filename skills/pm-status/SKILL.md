---
name: pm-status
description: Status report generation - project progress based on issues (GitHub/Bitbucket/GitLab)
user_invocable: true
agent: project-manager
---

# /pm-status - Status Report

## What this skill does
Generates a project status report based on issue states. Auto-detects the git platform.

## Usage
- `/pm-status` - Full status report
- `/pm-status sprint` - Current sprint status
- `/pm-status role <role>` - Status by role (sa/ba/pm/dev/fe/ops/test/review)

## Process

1. **Detect Platform**
   - Run `git remote get-url origin` to detect GitHub/Bitbucket/GitLab
   - Use appropriate CLI/API to fetch issues

2. **Collect Data**
   - Fetch all issues with their state, labels, dates via platform CLI/API

3. **Analyze**
   - Count issues by state (open/closed)
   - Group by type (epic/story/task/bug)
   - Group by role (sa/ba/pm/dev/fe/ops/test/review)
   - Group by priority
   - Calculate completion percentage

4. **Generate Report**
   ```markdown
   # Status Report — {date}

   ## Summary
   - Total issues: N
   - Open: N | Closed: N
   - Completion: N%

   ## By Type
   | Type | Open | Closed | Total |
   |------|------|--------|-------|

   ## By Role
   | Role | Open | Closed | Total |
   |------|------|--------|-------|

   ## By Priority
   | Priority | Open | Closed | Total |
   |----------|------|--------|-------|

   ## Blockers & Risks
   - {blocker 1}

   ## Next Steps
   - {action item 1}
   ```

5. **Present and Ask**
   - Show the report
   - Ask if user wants to take action on any items
