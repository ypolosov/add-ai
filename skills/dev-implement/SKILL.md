---
name: dev-implement
description: Feature implementation - implement use cases following ADRs and architecture patterns
user_invocable: true
agent: backend-developer
---

# /dev-implement - Feature Implementation

## What this skill does
Implements backend features (use cases) following architecture decisions and project patterns.

## Usage
- `/dev-implement <use-case-id>` - Implement a use case (e.g., UC-001)
- `/dev-implement <issue-number>` - Implement from a GitHub/GitLab/Bitbucket issue
- `/dev-implement` - Interactive: ask what to implement

## Process

1. **Read requirements**:
   - Use case from `docs/requirements/use-cases/` (if UC-ID)
   - Issue details from git platform (if issue number)
   - Related ADRs and design decisions
2. **Detect project framework**:
   - NestJS, Express, Fastify, Django, Spring, etc.
   - ORM: Drizzle, Prisma, TypeORM, SQLAlchemy, etc.
   - Check existing code patterns and structure
3. **Choose implementation approach**:
   - Ask user:
     ```
     Подход к реализации:
     1. Implementation First — реализация → тесты (по умолчанию)
     2. TDD — тесты → реализация → рефакторинг
     ```
4. **Plan implementation**:
   - List files to create/modify
   - Identify domain entities, ports, adapters involved
   - Map use case flow to code components
5. **Present implementation plan** to user for approval

### Implementation First (default)
6. **Implement** (after approval):
   - Domain logic (entities, value objects, domain services)
   - Application layer (use case service, DTOs)
   - Infrastructure (repository implementation, external adapters)
   - Interface layer (controller/handler, request/response DTOs)
   - Module registration
7. **Present completed code** and suggest:
   - `/test-unit` for unit tests
   - `/test-integration` for integration tests
   - `/review-code` for self-review

### TDD Mode
6. **Red phase** — Generate test files first:
   - Unit tests for domain logic (entities, value objects)
   - Unit tests for use case service (with mocked ports)
   - Run tests — verify they FAIL (all red)
7. **Green phase** — Implement minimal code to pass tests:
   - Domain logic, application layer, infrastructure, interface layer
   - Run tests — verify they PASS (all green)
8. **Refactor phase** — Propose improvements:
   - Ask: "Хотите провести рефакторинг? Вот что можно улучшить:"
   - Apply refactoring if approved
   - Run tests — verify they still PASS
9. **Present completed code** and suggest:
   - `/test-integration` for integration tests
   - `/review-code` for self-review

## Key Principles
- Follow existing architecture patterns (don't introduce new patterns without ADR)
- Implement one use case at a time
- Core domain has zero framework dependencies
- All external dependencies go through ports (interfaces)
- Reference ADR IDs in code comments for significant decisions
