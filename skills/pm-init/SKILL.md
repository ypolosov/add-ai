---
name: pm-init
description: Initialize project tracking - labels, milestones, initial stories (GitHub/Bitbucket/GitLab)
user_invocable: true
agent: project-manager
---

# /pm-init - Initialize Project Tracking

## What this skill does
Sets up project tracking infrastructure on the detected git platform: creates labels, milestones/epics, and initial stories. Should be one of the first skills invoked in a new project.

## Usage
- `/pm-init` - Full initialization (detect platform, create labels, milestone, stories)
- `/pm-init labels` - Create only labels
- `/pm-init check` - Check what already exists, report gaps

## Process

1. **Detect Platform**
   - Run `git remote get-url origin` to detect GitHub/Bitbucket/GitLab
   - Verify CLI tool availability (`which gh` / `which glab` / `curl`)
   - If platform cannot be determined, ask the user

2. **Check Existing State**
   - List existing labels, milestones, issues
   - Report what already exists to avoid duplicates

3. **Create Labels** (if not existing)

   **Type Labels** (required on every issue):
   - `type:epic` - Large feature spanning multiple stories
   - `type:story` - User-facing story with acceptance criteria
   - `type:task` - Technical task, part of a story
   - `type:bug` - Defect fix
   - `type:spike` - Time-boxed research/investigation

   **Role Labels** (required on every issue):
   - `role:sa` - Solution Architect
   - `role:ba` - Business Analyst
   - `role:pm` - Project Manager
   - `role:dev` - Backend Developer
   - `role:fe` - Frontend Developer
   - `role:ops` - DevOps Engineer
   - `role:test` - Tester
   - `role:review` - Code Reviewer
   - `role:nav` - Navigator

   **Phase Labels** (SDLC phase tracking):
   - `phase:requirements` - Requirements gathering and analysis
   - `phase:architecture` - Architecture design and decisions
   - `phase:development` - Implementation (backend, frontend, infrastructure)
   - `phase:testing` - Testing (unit, integration, E2E, BDD)
   - `phase:review` - Code review and quality assurance

   **Priority Labels**:
   - `priority:high` - Must do, blocking
   - `priority:medium` - Important, not blocking
   - `priority:low` - Nice to have

   **Status Labels**:
   - `status:backlog` - Not started
   - `status:in-progress` - Work in progress
   - `status:review` - Awaiting review
   - `status:done` - Completed

4. **Create Milestone/Epic** - "Project Inception"
   - GitHub: `gh api repos/{owner}/{repo}/milestones -f title="Project Inception"`
   - GitLab: `glab api projects/:id/milestones -f title="Project Inception"`
   - Bitbucket: create epic issue

5. **Create Initial Stories** (ask user to confirm before creating)
   - "Gather requirements" (`role:ba`, `phase:requirements`)
   - "Define architecture" (`role:sa`, `phase:architecture`)
   - "Set up CI/CD" (`role:ops`, `phase:development`)
   - "Set up project infrastructure" (`role:ops`, `phase:development`)

6. **Optionally: Create GitHub Projects Board** (GitHub only)
   - Ask if user wants a Projects board
   - If yes, create board with columns matching phases

7. **Present Summary**
   ```markdown
   ## Project Tracking Initialized

   ### Labels Created
   - Type: 5, Role: 9, Phase: 5, Priority: 3, Status: 4

   ### Milestone
   - "Project Inception" created

   ### Initial Stories
   - #N: Gather requirements (role:ba, phase:requirements)
   - #N: Define architecture (role:sa, phase:architecture)
   - #N: Set up CI/CD (role:ops, phase:development)
   ```

8. **Next Steps**
   - Suggest `/ba-requirements` to start gathering requirements
   - Suggest `/sa-init` to initialize architecture structure
   - Suggest `/nav-resume` to check overall project status
