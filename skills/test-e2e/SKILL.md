---
name: test-e2e
description: E2E test generation - user flows from use cases, Page Object Model
user_invocable: true
agent: tester
---

# /test-e2e - E2E Test Generation

## What this skill does
Generates end-to-end tests derived from use cases, using Page Object Model for maintainability.

## Usage
- `/test-e2e <use-case-id>` - Generate E2E test from a use case (e.g., UC-001)
- `/test-e2e <flow-name>` - Generate E2E test for a named user flow
- `/test-e2e` - Interactive: list use cases and ask which to test

## Process

1. **Detect E2E framework**:
   - Playwright (`playwright.config.*`)
   - Cypress (`cypress.config.*`, `cypress/`)
   - Selenium/WebDriver
   - If none found, suggest Playwright and ask
2. **Read use case** from `docs/requirements/use-cases/` (if UC-ID provided)
3. **Design test scenarios**:
   - Happy path (main flow)
   - Alternative flows
   - Error/edge cases from use case
4. **Generate Page Objects** (if not existing):
   - One page object per page/view
   - Encapsulate selectors and actions
   - Use data-testid attributes for selectors
5. **Generate test file**:
   - Structured by scenario
   - Uses page objects for interactions
   - Assertions on visible outcomes
   - Screenshots on failure (config)
6. **Present tests** and suggest:
   - Add `data-testid` attributes to components
   - `/ops-pipeline` for CI integration
   - Additional test scenarios

## Test Structure

### Playwright
```
e2e/
  pages/
    {page-name}.page.ts     # Page Object
  tests/
    {flow-name}.spec.ts     # Test scenarios
  fixtures/
    test-data.ts            # Shared test data
```

### Cypress
```
cypress/
  pages/
    {page-name}.page.ts     # Page Object
  e2e/
    {flow-name}.cy.ts       # Test scenarios
  fixtures/
    test-data.json           # Shared test data
```
