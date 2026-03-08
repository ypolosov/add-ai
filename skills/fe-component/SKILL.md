---
name: fe-component
description: Generate UI components with typed props, accessibility, and project styling
user_invocable: true
agent: frontend-developer
---

# /fe-component - UI Component Generation

## What this skill does
Generates UI components with typed props, accessibility attributes, and styling matching the project's conventions.

## Usage
- `/fe-component <component-name>` - Generate a named component
- `/fe-component` - Interactive: ask for component details

## Process

1. **Detect project conventions**:
   - Framework (React, Vue, Angular, Svelte)
   - Styling approach (Tailwind, CSS Modules, styled-components, SCSS)
   - Component directory (`src/components/`, `src/shared/`, `components/`)
   - Existing component patterns (naming, file structure, export style)
2. **Ask for details** (if not provided):
   - Component name
   - Props (key data inputs)
   - Variants/states (if applicable)
   - Interactive elements (buttons, inputs, etc.)
3. **Generate component** with:
   - TypeScript interface for props
   - Semantic HTML structure
   - ARIA attributes for accessibility
   - Keyboard navigation (for interactive components)
   - Styling matching project conventions
   - Default export matching project patterns
4. **Present the component** and suggest:
   - `/test-unit` for component tests
   - Additional sub-components if needed

## Accessibility Checklist
- Semantic HTML elements (`<button>`, `<nav>`, `<main>`, etc.)
- ARIA labels for non-text elements
- Keyboard navigation for interactive elements
- Focus management for modals/dropdowns
- Color contrast considerations (noted in comments)
- Screen reader-friendly text alternatives
