---
name: ba-mtw
description: Mission Thread Workshop - end-to-end scenario generation for mission threads
user_invocable: true
agent: business-analyst
---

# /ba-mtw - Mission Thread Workshop

> **Note:** Mission Thread Workshop is an extension beyond the ADD 3.0 book process.
> Recommended for systems-of-systems, mission-critical, or multi-organization contexts.

## What this skill does
Facilitates a Mission Thread Workshop (MTW) to generate end-to-end mission thread scenarios that cross multiple system components and quality attributes.

## Usage
- `/ba-mtw` - Start a new MTW session
- `/ba-mtw <thread-name>` - Create/update a specific mission thread

## What is a Mission Thread?
A mission thread is an end-to-end sequence of activities and interactions that achieves a specific operational goal, crossing multiple system boundaries and involving multiple stakeholders. Unlike individual use cases, mission threads capture the full operational context.

## Process

1. **Context Setting**:
   - Read existing use cases from `docs/requirements/use-cases/`
   - Read quality attributes from `docs/architecture/drivers/quality-attributes/`
   - Read existing mission threads from `docs/requirements/mission-threads/`
   - Summarize what's already documented

2. **Thread Identification**:
   - Ask: "Какую операционную цель хотите проследить от начала до конца?"
   - Identify participating actors and systems
   - Define the thread scope (start event → end state)

3. **Thread Elaboration**:
   - Map the step-by-step flow across system boundaries
   - For each step, identify:
     - Actor/system performing the action
     - Input/output data
     - Quality attribute scenarios triggered (performance, availability, security)
     - Failure modes and recovery paths
   - Identify cross-cutting concerns (logging, auth, monitoring)

4. **Thread Documentation**:
   - Save to `docs/requirements/mission-threads/MT-NNN-{name}.md`
   - Format:
     ```markdown
     # MT-NNN: {Thread Name}

     ## Operational Goal
     {description}

     ## Actors & Systems
     - {actor/system}: {role in thread}

     ## Thread Flow
     | Step | Actor/System | Action | QA Scenarios | Failure Modes |
     |------|-------------|--------|-------------|---------------|

     ## Quality Attribute Impact
     - QA-NNN: {how this thread exercises the QA}

     ## Related
     - Use Cases: UC-NNN, UC-NNN
     - ADRs: ADR-NNNN
     ```

5. **Next Steps**:
   - Suggest `/ba-qaw` for new QA scenarios discovered
   - Suggest `/sa-iterate` to address architectural implications
   - Suggest `/pm-issue` to create work items
