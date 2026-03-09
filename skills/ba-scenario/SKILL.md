---
name: ba-scenario
description: Scenario Workshop - compose cross-cutting scenarios (SC-NNN) from use cases and quality attributes
user_invocable: true
agent: business-analyst
---

# /ba-scenario - Scenario Workshop

> **Note:** Scenario Workshop builds on Mission Thread Workshop (MTW) concepts.
> Recommended for systems-of-systems, mission-critical, or multi-component contexts.
> Uses the same method but outputs unified SC-NNN artifacts instead of MT-NNN.

## What this skill does
Facilitates a Scenario Workshop to generate cross-cutting scenarios (SC-NNN) that compose multiple use cases (UC-NNN) into end-to-end flows with quality attribute checkpoints (QA-NNN).

## Usage
- `/ba-scenario` - Start a new scenario workshop session
- `/ba-scenario <scenario-name>` - Create/update a specific scenario

## What is a Scenario (SC-NNN)?
A scenario is a composite, end-to-end sequence of activities that achieves a specific operational goal by chaining multiple use cases (UC-NNN steps) and verifying quality attributes (QA-NNN checkpoints) along the way. Unlike individual use cases, scenarios capture the full operational context across system boundaries.

**Key difference from UC-NNN:** A use case is atomic and reusable. A scenario composes multiple use cases into a flow and adds QA verification points.

## Traceability
- SC-NNN → `features/SC-NNN-name.feature` (BDD via `/test-bdd`)
- SC-NNN → `e2e/SC-NNN-name.spec.ts` (E2E via `/test-e2e`)
- SC-NNN steps reference UC-NNN (atomic use cases)
- SC-NNN checkpoints reference QA-NNN (quality attributes)

## Process

1. **Context Setting**:
   - Read existing use cases from `docs/requirements/use-cases/`
   - Read quality attributes from `docs/architecture/drivers/quality-attributes/`
   - Read existing scenarios from `docs/requirements/scenarios/`
   - Summarize what's already documented

2. **Scenario Identification**:
   - Ask: "Какую операционную цель хотите проследить от начала до конца?"
   - Identify participating actors and systems
   - Define the scenario scope (start event → end state)
   - Map to existing UC-NNN steps where possible

3. **Scenario Elaboration**:
   - Map the step-by-step flow as a chain of UC-NNN references
   - For each step, identify:
     - UC-NNN being executed (or new UC if gap found)
     - Actor/system performing the action
     - Input/output data
     - QA-NNN checkpoints (performance, availability, security thresholds)
     - Failure modes and recovery paths
   - Identify cross-cutting concerns (logging, auth, monitoring)
   - **Gap detection:** If a step doesn't map to an existing UC, propose creating a new UC-NNN

4. **Scenario Documentation**:
   - Save to `docs/requirements/scenarios/SC-NNN-{name}.md`
   - Use template from `reference/templates/scenario-template.md`

5. **Next Steps**:
   - Suggest `/ba-usecase` for new use cases discovered during elaboration
   - Suggest `/ba-qaw` for new QA scenarios discovered
   - Suggest `/sa-iterate` to address architectural implications
   - Suggest `/test-bdd SC-NNN` to generate BDD feature from this scenario
   - Suggest `/test-e2e SC-NNN` to generate E2E test from this scenario
   - Suggest `/pm-issue` to create work items
