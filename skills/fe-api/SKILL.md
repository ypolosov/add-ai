---
name: fe-api
description: Generate typed API layer - hooks, services, REST/GraphQL clients
user_invocable: true
agent: frontend-developer
---

# /fe-api - API Layer Generation

## What this skill does
Generates typed API clients, hooks, and services for frontend-backend communication.

## Usage
- `/fe-api <resource-name>` - Generate API layer for a resource
- `/fe-api` - Interactive: detect API patterns and ask for details

## Process

1. **Detect API patterns**:
   - Data fetching library: react-query/TanStack Query, SWR, Apollo, axios, fetch
   - API style: REST, GraphQL, tRPC
   - Existing API layer: `src/api/`, `src/services/`, `src/hooks/`
   - Backend types: shared types, OpenAPI spec, GraphQL schema
   - Test framework (Jest, Vitest, MSW for mocking)
2. **Ask for details** (if not provided):
   - Resource name (e.g., `user`, `order`, `product`)
   - Endpoints/operations (CRUD or custom)
   - Base URL or API prefix
3. **Choose implementation approach**:
   - Ask user:
     ```
     Подход к реализации:
     1. Implementation First — API layer → тесты (по умолчанию)
     2. TDD — тесты → API layer → рефакторинг
     ```

### Implementation First (default)
4. **Generate files**:
   - TypeScript types for request/response
   - API client functions (fetch/axios calls)
   - Data fetching hooks (if using react-query/SWR/Apollo)
   - Error handling utilities
5. **Present generated code** and suggest:
   - Integration with existing pages
   - `/test-unit` for API hook tests
   - `/test-integration` for API integration tests

### TDD Mode
4. **Red phase** — Generate test files first:
   - Tests for API client functions (mocked HTTP with MSW or jest.mock)
   - Tests for hooks (renderHook with mocked responses)
   - Tests for error handling (network errors, 4xx/5xx responses)
   - Run tests — verify they FAIL
5. **Green phase** — Generate minimal API layer to pass tests:
   - Types, client functions, hooks
   - Run tests — verify they PASS
6. **Refactor phase** — Propose improvements:
   - Type safety improvements, error handling refinements, caching strategies
   - Run tests — verify they still PASS
7. **Present completed API layer + tests**

## Generated Patterns

### TanStack Query (React)
```typescript
// api/{resource}.ts - API functions
// hooks/use-{resource}.ts - Query/Mutation hooks
// types/{resource}.types.ts - TypeScript types
```

### SWR (React)
```typescript
// api/{resource}.ts - Fetcher functions
// hooks/use-{resource}.ts - SWR hooks
// types/{resource}.types.ts - TypeScript types
```

### Apollo (GraphQL)
```typescript
// graphql/{resource}.graphql - Queries/Mutations
// hooks/use-{resource}.ts - Generated hooks
// types/{resource}.types.ts - Generated types
```

### Vanilla (fetch/axios)
```typescript
// services/{resource}.service.ts - Service class/functions
// types/{resource}.types.ts - TypeScript types
```
