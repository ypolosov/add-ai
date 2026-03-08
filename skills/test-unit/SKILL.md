---
name: test-unit
description: Unit test generation - TDD, AAA pattern, domain/services/utilities
user_invocable: true
agent: tester
---

# /test-unit - Unit Test Generation

## What this skill does
Generates unit tests following TDD principles for domain logic, services, and utilities.

## Usage
- `/test-unit <file-path>` - Generate unit tests for a specific file
- `/test-unit <module-name>` - Generate unit tests for a module
- `/test-unit` - Interactive: ask what to test

## Process

1. **Detect test framework** - Jest, Vitest, Mocha, pytest, JUnit, etc.
2. **Read the target code** - Analyze exports, classes, functions
3. **Identify test cases**:
   - Happy path for each public function/method
   - Edge cases (empty inputs, boundaries, nulls)
   - Error cases (invalid inputs, expected failures)
   - State transitions (for stateful objects)
4. **Generate test file** following AAA pattern:
   - **Arrange** - Set up test data and mocks
   - **Act** - Call the function/method under test
   - **Assert** - Verify the result
5. **Present tests** and ask:
   - Run tests? (to verify they fail — TDD red phase)
   - Adjust test cases?
   - Generate implementation? (TDD green phase)

## Test Conventions
- Test file location matches project convention (co-located `*.spec.ts` or separate `test/` dir)
- `describe` blocks group by class/function
- `it` blocks describe behavior: `it('should calculate total with discount applied')`
- Mock boundaries (ports, external services), not internals
- One concept per test (multiple related asserts are OK)
- Reference requirement IDs where applicable: `// UC-001: user registration`
