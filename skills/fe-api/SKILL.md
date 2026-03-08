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
2. **Ask for details** (if not provided):
   - Resource name (e.g., `user`, `order`, `product`)
   - Endpoints/operations (CRUD or custom)
   - Base URL or API prefix
3. **Generate files**:
   - TypeScript types for request/response
   - API client functions (fetch/axios calls)
   - Data fetching hooks (if using react-query/SWR/Apollo)
   - Error handling utilities
4. **Present generated code** and suggest:
   - Integration with existing pages
   - `/test-unit` for API hook tests
   - `/test-integration` for API integration tests

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
