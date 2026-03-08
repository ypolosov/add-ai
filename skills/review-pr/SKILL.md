---
name: review-pr
description: Pull request review - structured checklist via git platform CLI
user_invocable: true
agent: code-reviewer
---

# /review-pr - Pull Request Review

## What this skill does
Reviews a pull request with a structured checklist. Uses git platform CLI to read PR details and diff.

## Usage
- `/review-pr <number>` - Review PR by number
- `/review-pr <url>` - Review PR by URL
- `/review-pr` - List open PRs and ask which to review

## Process

1. **Detect git platform**:
   - GitHub (`github.com` in remote) → `gh pr view`, `gh pr diff`
   - Bitbucket (`bitbucket.org` in remote) → `curl` Bitbucket REST API
   - GitLab (`gitlab.com` in remote) → `glab mr view` or REST API
   - If ambiguous, ask the user
2. **Read PR details**:
   - Title, description, author
   - Changed files and diff
   - Linked issues
   - CI status
3. **Review against checklist**:

   ### PR Meta
   - [ ] Title is descriptive
   - [ ] Description explains the "why"
   - [ ] Linked to issue(s)
   - [ ] CI passes

   ### Code Quality
   - [ ] Architecture compliance
   - [ ] ADR compliance
   - [ ] No logic in wrong layers
   - [ ] Error handling is consistent
   - [ ] No hardcoded configs or secrets

   ### Testing
   - [ ] Tests cover the changes
   - [ ] Tests pass

   ### Security
   - [ ] No secrets in code
   - [ ] Input validation at boundaries

4. **Generate review report** with checklist results
5. **Present report** and suggest:
   - Approve / Request changes
   - Specific comments to leave on PR
   - Issues to create for follow-up
