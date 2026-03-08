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
3. **Plan implementation**:
   - List files to create/modify
   - Identify domain entities, ports, adapters involved
   - Map use case flow to code components
4. **Present implementation plan** to user for approval
5. **Implement** (after approval):
   - Domain logic (entities, value objects, domain services)
   - Application layer (use case service, DTOs)
   - Infrastructure (repository implementation, external adapters)
   - Interface layer (controller/handler, request/response DTOs)
   - Module registration
6. **Present completed code** and suggest:
   - `/test-unit` for unit tests
   - `/test-integration` for integration tests
   - `/review-code` for self-review

## Key Principles
- Follow existing architecture patterns (don't introduce new patterns without ADR)
- Implement one use case at a time
- Core domain has zero framework dependencies
- All external dependencies go through ports (interfaces)
- Reference ADR IDs in code comments for significant decisions
