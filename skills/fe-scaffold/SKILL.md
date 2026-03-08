---
name: fe-scaffold
description: Scaffold frontend modules, pages, and routes (framework-adaptive)
user_invocable: true
agent: frontend-developer
---

# /fe-scaffold - Frontend Module Scaffolding

## What this skill does
Generates frontend pages, routes, and feature modules matching the project's framework and structure.

## Usage
- `/fe-scaffold <module-name>` - Scaffold a new frontend module/page
- `/fe-scaffold` - Interactive: detect framework and ask for details

## Process

1. **Detect framework** - Read `package.json`, check for framework configs (React/Next.js, Vue/Nuxt, Angular, Svelte, etc.)
2. **Analyze project structure** - Scan existing pages/routes/features to match conventions
3. **Ask for details** (if not provided):
   - Module/page name
   - Route path
   - Key features (data fetching, forms, lists, etc.)
4. **Generate files** based on detected framework:
   - Page/route component
   - Layout (if needed)
   - Sub-components
   - Types/interfaces
   - Route registration
5. **Present generated structure** and suggest next steps:
   - `/fe-component` for additional UI components
   - `/fe-api` for API integration
   - `/test-unit` for component tests

## Framework-Specific Output

### Next.js (App Router)
```
app/{name}/
  page.tsx
  layout.tsx (if needed)
  loading.tsx
  error.tsx
```

### React (Vite/CRA)
```
src/pages/{name}/
  {Name}Page.tsx
  {Name}Page.module.css
src/routes.tsx (update)
```

### Vue/Nuxt
```
pages/{name}/
  index.vue
  [id].vue (if needed)
```

### Angular
```
src/app/{name}/
  {name}.component.ts
  {name}.component.html
  {name}.component.scss
  {name}.module.ts
  {name}-routing.module.ts
```
