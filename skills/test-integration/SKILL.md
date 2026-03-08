---
name: test-integration
description: Integration test generation - API endpoints, database, module wiring
user_invocable: true
agent: tester
---

# /test-integration - Integration Test Generation

## What this skill does
Generates integration tests for API endpoints, database interactions, and module wiring.

## Usage
- `/test-integration <module-name>` - Generate integration tests for a module
- `/test-integration api <endpoint>` - Generate API endpoint tests
- `/test-integration` - Interactive: ask what to test

## Process

1. **Detect test framework and tools**:
   - Test runner: Jest, Vitest, Mocha, pytest
   - HTTP testing: supertest, axios, httpx
   - DB testing: test containers, in-memory DB, fixtures
2. **Analyze the target module**:
   - API endpoints (routes, controllers)
   - Database operations (repositories, queries)
   - Module dependencies and wiring
3. **Generate integration tests**:
   - API tests: request → response validation (status, body, headers)
   - DB tests: CRUD operations against test database
   - Module tests: dependency injection, wiring correctness
4. **Include setup/teardown**:
   - Test database setup (migrations, seeds)
   - Test server bootstrap
   - Cleanup after each test
5. **Present tests** and suggest:
   - `/ops-docker` for test database containers
   - `/test-e2e` for end-to-end scenarios

## Test Structure
```
test/integration/
  {module}/
    {module}.api.spec.ts       # API endpoint tests
    {module}.repository.spec.ts # DB operation tests
    {module}.module.spec.ts     # Module wiring tests
  setup/
    test-app.ts                # Test application bootstrap
    test-db.ts                 # Test database setup
```

## Key Principles
- Use real database (test instance), not mocks
- Test full request-response cycle for APIs
- Verify side effects (DB state, events emitted)
- Isolate tests: each test starts with clean state
- Keep tests deterministic (no timing dependencies)
