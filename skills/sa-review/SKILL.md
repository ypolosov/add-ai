---
name: sa-review
description: Architecture review - evaluate design against quality attribute scenarios
user_invocable: true
agent: solution-architect
---

# /sa-review - Architecture Review

## What this skill does
Evaluates the current architecture against quality attribute scenarios and identifies risks, including tactics conflicts.

## Process

1. **Gather Context**
   - Read `docs/architecture/README.md` for Design Purpose and System Context
   - Read `docs/architecture/utility-tree.md` for QA priorities
   - Read `docs/architecture/c4/src/model.c4` for current design
   - Read all ADRs from `docs/architecture/adrs/`
   - Read design decisions from `docs/architecture/decisions/`

2. **Analyze Coverage**
   - For each high-priority QA scenario, check if there's a design decision addressing it
   - Identify QAs without corresponding ADRs or design decisions
   - List unaddressed architecture drivers
   - Show kanban summary: Not Addressed / Partially Addressed / Completely Addressed

3. **Tactics Analysis**
   - List all tactics applied across ADRs and decisions
   - Check for conflicting tactics between QA categories:
     | Tactic A | QA | Tactic B | QA | Conflict | Resolution |
     |----------|-----|----------|-----|----------|------------|
   - Identify **Sensitivity Points** — where one tactic strongly affects a QA response
     (e.g., "Caching significantly affects response time but may impact data freshness")
   - Identify **Trade-off Points** — where two QA requirements pull design in opposite directions
     (e.g., "Encryption (security) vs. response time (performance)")
   - Flag unresolved trade-offs as risks

4. **Risk Assessment**
   - Identify potential single points of failure
   - Check for missing error handling strategies
   - Evaluate scalability bottlenecks
   - Review security boundaries
   - Assess deployment complexity

5. **Generate Review Report**
   Present findings in a table:
   | QA Scenario | Status | ADR | Tactics | Risk Level | Notes |
   |-------------|--------|-----|---------|------------|-------|

6. **Recommendations**
   - Suggest ADRs to create
   - Propose additional iterations
   - Highlight areas needing spike/prototyping
   - List unresolved trade-offs with suggested resolution approaches

7. **Next Steps** - present options:
   - Start ADD iteration to address gaps
   - Create specific ADRs
   - Update diagrams
   - Conduct deeper analysis on a specific area
