---
name: review-standards
description: Standards audit - project structure, naming, dependency direction compliance
user_invocable: true
agent: code-reviewer
---

# /review-standards - Standards Audit

## What this skill does
Audits the entire project (or specific area) for compliance with declared standards, conventions, and architecture patterns.

## Usage
- `/review-standards` - Full project audit
- `/review-standards structure` - Audit directory structure
- `/review-standards naming` - Audit naming conventions
- `/review-standards dependencies` - Audit dependency direction

## Process

1. **Read project standards**:
   - ADRs from `docs/architecture/adrs/`
   - Architecture docs from `docs/architecture/`
   - Reference conventions (if `reference/` exists)
   - `CLAUDE.md`, `package.json`, linter configs
2. **Audit categories**:

   ### Directory Structure
   - Files are in correct directories per architecture pattern
   - No mixed concerns (e.g., domain code in infrastructure dir)
   - Consistent module/feature organization

   ### Naming Conventions
   - File names follow project convention (kebab-case, PascalCase, etc.)
   - Class/function names are consistent
   - ID formats match declared patterns (UC-NNN, ADR-NNNN, etc.)

   ### Dependency Direction
   - Core/domain does not import from infrastructure
   - Interfaces/adapters depend on core, not vice versa
   - No circular dependencies between modules

   ### Configuration
   - No hardcoded values that should be configurable
   - Environment variables are documented
   - Secrets are not in version control

3. **Generate audit report**:
   ```
   ## Standards Audit Report

   ### Summary
   - Areas audited: N
   - Compliant: N | Violations: N

   ### Violations
   | # | Category | Location | Description | Severity |
   |---|----------|----------|-------------|----------|

   ### Recommendations
   - {recommendation 1}
   ```
4. **Present report** and suggest:
   - Create ADR for undocumented patterns
   - Create issues for violations
   - Schedule fix sprints for systematic issues
