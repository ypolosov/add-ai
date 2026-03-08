---
name: sa-kanban
description: Architecture design kanban board management — tracks architectural drivers through ADD 3.0
user_invocable: true
agent: solution-architect
---

# /sa-kanban - Design Kanban

## What this skill does
Manages the architecture design kanban board at `docs/architecture/kanban.md`. Tracks **architectural drivers** (QA scenarios, use cases, constraints, concerns) through their resolution lifecycle per ADD 3.0.

## Usage
- `/sa-kanban` - Show current board with driver counts by state
- `/sa-kanban add <driver-id>` - Add a driver to the board (e.g., QA-001, UC-003)
- `/sa-kanban move <driver-id> <column>` - Move driver between columns
- `/sa-kanban update` - Sync board with current state of ADRs, decisions, and iterations

## Columns (ADD 3.0 + Extensions)

### Book-aligned (Cervantes & Kazman, 2nd ed.)
1. **Not Addressed** — Driver identified but not yet considered in any iteration
2. **Partially Addressed** — Driver considered in an iteration, but not fully resolved (e.g., only one aspect addressed)
3. **Completely Addressed** — All aspects of the driver resolved through design decisions and ADRs

### Extensions (beyond ADD 3.0)
4. **Implemented** — Code reflects the design decisions
5. **Verified** — Tested and validated against the driver's scenario

## Board Format in kanban.md

```markdown
# Architecture Design Kanban

## Not Addressed
- [ ] QA-005: System recovers from database failure within 30s
- [ ] UC-004: Admin manages user roles
- [ ] CON-002: Must comply with GDPR

## Partially Addressed
- [ ] QA-002: 99.9% availability (ITER-01, ADR-0001 — caching addressed, failover not yet)
- [ ] UC-003: User authentication flow (ITER-01 — login done, MFA not yet)

## Completely Addressed
- [x] QA-003: JWT-based authentication < 100ms (ADR-0002, DD-001, DD-003)
- [x] UC-001: User registration (ADR-0003, DD-002)
- [x] CON-001: Must use PostgreSQL (ADR-0001)

## Implemented
- [x] QA-001: API response < 200ms (ADR-0001, PR #15)
- [x] UC-002: Product search (ADR-0004, PR #18)

## Verified
- [x] CRN-001: Monitoring strategy (ADR-0005, tested in ITER-03)
```

## Key Principles
- **Primary items are drivers** (QA-NNN, UC-NNN, CON-NNN, CRN-NNN), not design decisions
- **DD-NNN and ADR-NNNN are cross-references** — they appear as "addressed by" annotations
- **Iteration references** (ITER-NN) show when a driver was worked on
- A driver moves to "Partially Addressed" when at least one aspect is resolved but others remain
- A driver moves to "Completely Addressed" when its full scenario/requirement is satisfied

## Sync Logic
When running `/sa-kanban update`:
1. Read all drivers from `docs/architecture/drivers/` — ensure all are on the board
2. Read all ADRs from `docs/architecture/adrs/` — check which drivers they reference
3. Read all iterations from `docs/architecture/iterations/` — check which drivers were worked on
4. For each driver on the board:
   - If referenced in an ADR but scenario not fully covered → "Partially Addressed"
   - If all aspects of the driver's scenario are covered by ADRs/DDs → "Completely Addressed"
   - If related PRs are merged → "Implemented"
5. Report summary:
   ```
   Not Addressed: N | Partially Addressed: N | Completely Addressed: N | Implemented: N | Verified: N
   ```
6. Highlight any (H,H) drivers still in "Not Addressed"
