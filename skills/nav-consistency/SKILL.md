---
name: nav-consistency
description: Cross-cutting consistency review — C4 element refs, artifact IDs, hardcoded tools, version strings, skill index
user_invocable: true
agent: navigator
---

# Consistency Review

Checks project artifacts for internal consistency across 5 categories.

## What this skill does

Scans the target project for broken references, stale IDs, hardcoded tool names, version drift, and index mismatches. Produces a categorized report with findings and fix suggestions.

## Usage

- `/nav-consistency` — full report (all 5 categories)
- `/nav-consistency element-refs` — C4 element references only
- `/nav-consistency artifact-refs` — artifact ID references only
- `/nav-consistency tools` — hardcoded diagramming tools only
- `/nav-consistency index` — skill index vs directories only
- `/nav-consistency auto-fix` — full report with fix suggestions table

## Process

### 1. C4 Element References

- Scan all markdown files for C4 element names (containers, components, relationships)
- Cross-check against definitions in `docs/architecture/c4/src/model.c4` (or all `.c4` files)
- Report any references to undefined elements

### 2. Artifact ID References

- Scan for artifact IDs: UC-NNN, QA-NNN, SC-NNN, CON-NNN, CRN-NNN, DD-NNN, ADR-NNNN
- Verify each ID resolves to an existing file (per `reference/architecture-conventions.md` naming)
- Report orphaned references and unreferenced artifacts

### 3. Hardcoded Tools

- Scan non-reference files for Mermaid (` ```mermaid `), PlantUML (`@startuml`), D2 (` ```d2 `) syntax
- Files in `reference/` are exempt (convention docs may name tools)
- Report violations with file and line number

### 4. Version Strings

- Compare version in `plugin.json` vs `package.json` (if both exist)
- Flag drift between declared versions

### 5. Plugin Skill Index

- Compare CLAUDE.md skill table entries against actual `skills/` subdirectories
- Report skills listed but missing, or present but unlisted

## Output Format

```
## Consistency Report — {project} ({timestamp})

### C4 Element References
| Status | Reference | File | Expected In |
|--------|-----------|------|-------------|
| pass/fail | element_name | file:line | model.c4 |

### Artifact ID References
| Status | ID | Referenced In | Expected File |
|--------|----|---------------|---------------|
| pass/fail | UC-001 | file:line | path/to/file |

### Hardcoded Tools
| File | Line | Tool | Context |
|------|------|------|---------|
| file | N | Mermaid | code block |

### Version Strings
| Source | Version | Match |
|--------|---------|-------|
| plugin.json | x.y.z | pass/fail |

### Skill Index
| Status | Skill | In Table | In Directory |
|--------|-------|----------|--------------|
| pass/fail | name | yes/no | yes/no |
```

When using `auto-fix` mode, append a Fix Suggestions table:

```
### Fix Suggestions
| # | Category | Action | Details |
|---|----------|--------|---------|
| 1 | element-refs | Create element | Add `container_name` to model.c4 |
```

Navigator is read-only — suggestions are presented for the user to approve and execute via the appropriate skill.

## Difference from nav-resume

- `nav-resume` answers: "Where are we in the SDLC?"
- `nav-consistency` answers: "Is everything internally coherent?"
