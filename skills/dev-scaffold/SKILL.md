---
name: dev-scaffold
description: Backend module scaffolding with hexagonal architecture structure (framework-adaptive)
user_invocable: true
agent: backend-developer
---

# /dev-scaffold - Backend Module Scaffolding

## What this skill does
Generates a backend module following hexagonal architecture (ports & adapters) and DDD patterns. Auto-detects the project framework.

## Usage
- `/dev-scaffold <module-name>` - Scaffold a new module
- `/dev-scaffold` - Interactive: ask for module name and details

## Generated Structure

For a module named `{name}`:

```
{base-path}/
  core/domain/{name}/
    {name}.entity.ts              # Aggregate root entity
    {name}.value-objects.ts       # Value objects
    {name}.events.ts              # Domain events
    {name}.repository.port.ts     # Repository interface (outbound port)

  core/application/{name}/
    ports/
      inbound/
        {name}.use-cases.ts       # Use case interfaces (inbound port)
      outbound/
        {name}.repository.port.ts # Re-export or additional outbound ports
    services/
      {name}.service.ts           # Use case implementation
    dto/
      {name}.dto.ts               # Input/Output DTOs

  infrastructure/{name}/
    {name}.repository.ts          # Repository implementation (Drizzle)
    {name}.mapper.ts              # Entity <-> DB mapping
    {name}.schema.ts              # Drizzle schema definition

  interfaces/http/{name}/
    {name}.controller.ts          # REST controller
    {name}.request.ts             # Request validation (class-validator)
    {name}.response.ts            # Response DTOs

  modules/{name}/
    {name}.module.ts              # NestJS module definition
```

> `{base-path}` is the project's source root (e.g., `src/`, `packages/api/src/`). The skill auto-detects it by looking for `tsconfig.json`, `nest-cli.json`, or `package.json` with a NestJS dependency. If multiple candidates exist, the user is asked to choose.

## Process
1. **Detect project source root** - scan for NestJS project markers, ask user to confirm or specify the base path
2. Ask for module name (if not provided)
3. Ask for key entity properties
4. Ask for main use cases
5. Generate all files with proper imports and structure
6. Register module in `app.module.ts`
7. Suggest running `/test-unit` to generate tests
