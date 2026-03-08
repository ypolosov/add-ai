---
name: test-bdd
description: BDD scenarios in Gherkin - feature files and step definitions
user_invocable: true
agent: tester
---

# /test-bdd - BDD Scenario Generation

## What this skill does
Generates BDD scenarios in Gherkin format (Given/When/Then) and corresponding step definitions.

## Usage
- `/test-bdd <use-case-id>` - Generate BDD scenarios from a use case (e.g., UC-001)
- `/test-bdd <feature-name>` - Generate BDD scenarios for a named feature
- `/test-bdd` - Interactive: ask for feature details

## Process

1. **Detect BDD framework**:
   - **Cucumber.js** — `cucumber.js`, `@cucumber/cucumber` in deps
   - **jest-cucumber** — `jest-cucumber` in deps
   - **Behave** (Python) — `behave` in deps, `features/` dir
   - **SpecFlow** (.NET) — `.feature` files with SpecFlow references
   - If none found, suggest based on project stack and ask
2. **Read use case** from `docs/requirements/use-cases/` (if UC-ID provided)
3. **Generate feature file** in Gherkin:
   ```gherkin
   Feature: {feature name}
     As a {role}
     I want {action}
     So that {benefit}

     Scenario: {happy path}
       Given {precondition}
       When {action}
       Then {expected outcome}

     Scenario: {alternative/error flow}
       Given {precondition}
       When {action}
       Then {expected outcome}
   ```
4. **Generate step definitions** matching the framework
5. **Present scenarios** and suggest:
   - Review with stakeholders
   - `/test-e2e` for automation of these scenarios
   - Additional scenarios for edge cases

## File Structure
```
features/
  {feature-name}.feature       # Gherkin scenarios
  step-definitions/
    {feature-name}.steps.ts    # Step implementations
  support/
    world.ts                   # Shared context
```

## Key Principles
- Write scenarios in business language, not technical details
- Each scenario tests one behavior
- Use Background for shared preconditions
- Use Scenario Outline for data-driven scenarios
- Step definitions should be reusable across features
- Reference requirement IDs: `# UC-001`
