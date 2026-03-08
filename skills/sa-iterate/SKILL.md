---
name: sa-iterate
description: Run an ADD 3.0 iteration - interactive 7-step architecture design process
user_invocable: true
agent: solution-architect
---

# /sa-iterate - ADD 3.0 Iteration

## What this skill does
Guides the user through one complete ADD 3.0 iteration interactively, following the 7-step process from "Designing Software Architectures" (Cervantes & Kazman, 2nd ed.).

## Prerequisites
- `docs/architecture/` must be initialized (run `/sa-init` if not)
- Architecture drivers should exist in `docs/architecture/drivers/`
- Utility tree should have priorities (`docs/architecture/utility-tree.md`)

## Process (7 Steps)

### Step 1: Review Inputs
1. Read `docs/architecture/README.md` for Design Purpose and System Context
2. Read `docs/architecture/utility-tree.md` for prioritized quality attributes
3. Read `docs/architecture/drivers/` for use cases, constraints, concerns
4. Read previous iterations from `docs/architecture/iterations/`
5. Read `docs/architecture/kanban.md` — show driver counts by state:
   ```
   Not Addressed: N | Partially Addressed: N | Completely Addressed: N
   ```
6. Summarize current state for the user
7. Ask: "Есть ли новые stakeholder concerns, не отражённые в драйверах?"
8. Ask: "Готовы начать итерацию? Какие драйверы в фокусе?"

### Step 2: Establish Iteration Goal
1. Present the highest-priority unaddressed drivers (only architecturally significant ones — high-priority QAs + primary UCs)
2. Ask user to select 2-4 drivers for this iteration
3. Ask: "Сформулируйте цель итерации одним предложением:"
   - Template: "Итерация ITER-NN решает [что] путём [как]"
4. Write this goal as the header of `docs/architecture/iterations/ITER-NN.md`:
   ```markdown
   # ITER-NN: {iteration goal statement}
   ## Drivers
   - QA-NNN: ...
   - UC-NNN: ...
   ```

### Step 3: Choose Element to Refine
1. Show current C4 model elements (read `docs/architecture/c4/src/model.c4`)
2. Present three refinement types:
   - A) **Decompose** — разбить элемент на под-элементы
   - B) **Improve** — улучшить внутреннюю структуру существующего элемента
   - C) **Add** — добавить новый элемент для удовлетворения драйвера
3. Suggest which element to refine and why
4. Ask user to confirm or choose another element
5. Record rationale in ITER-NN.md: "Выбран {element} потому что {reason}"

### Step 4: Choose Design Concepts
1. For each selected driver, propose applicable:
   - Reference architectures (see `templates.md` → Reference Architectures)
   - Architecture patterns (e.g., CQRS, Event Sourcing, Saga)
   - Tactics (e.g., load balancing, caching, circuit breaker)
   - Technologies (e.g., Redis, Kafka, PostgreSQL)
2. Reference `sa-iterate/templates.md` for pattern/tactics catalog
3. Ask: "Достаточно ли информации для решения, или нужен spike/prototype?"
   - If spike needed → create `type:spike` issue via `/pm-issue`, defer driver to next iteration
4. Present pros/cons table for each alternative:
   | Alternative | Effort | Quality Impact | Risk | Trade-offs |
   |-------------|--------|----------------|------|------------|
5. Ask user to choose or suggest alternatives

### Step 5: Instantiate Elements
1. Ask: "Какой тип структуры проектируем?"
   - A) **Module structure** — организация кода, зависимости модулей, layers/packages
   - B) **C&C structure** — runtime элементы, коннекторы, протоколы, порты
   - C) **Allocation structure** — маппинг на инфраструктуру, команды, файловую систему
2. Define new elements, their responsibilities, and interfaces
3. Map elements to design concepts from Step 4
4. Create **Element Responsibility Table (ERT)** for each new/modified element:
   ```markdown
   | Element | Responsibilities | Provided Interfaces | Required Interfaces |
   |---------|-----------------|---------------------|---------------------|
   ```
   Save to `docs/architecture/views/{element}-ert.md`
5. Show how elements address selected drivers
6. Note: Provided/Required Interfaces from ERT will be detailed via LikeC4 dynamic views in Step 6
7. Ask user to confirm the design

### Step 6: Sketch Views & Record Decisions
1. Update LikeC4 diagrams (`docs/architecture/c4/src/`)
2. Create ADRs for significant decisions (using `/sa-adr` internally)
3. Create design decision records in `docs/architecture/decisions/` using DD template (see `skills/sa-iterate/dd-template.md` for format, `sa-init` creates `decisions/DD-000-template.md`)
4. Create LikeC4 dynamic views for key interactions (using `/sa-diagram dynamic` if needed)
5. Show user the updated views

### Step 7: Review & Assess
1. Review how well the iteration addressed its goals
2. **Tactics conflict check:**
   - List all tactics applied in this iteration
   - Check for conflicting tactics between QA categories
   - Present Sensitivity Points (where one tactic strongly affects a QA response)
   - Present Trade-off Points (where two QA requirements pull design in opposite directions)
   - Example: "Caching (performance) vs. real-time consistency (correctness)"
   ```markdown
   | Tactic A | QA | Tactic B | QA | Conflict | Resolution |
   |----------|-----|----------|-----|----------|------------|
   ```
3. Identify any new drivers or concerns discovered
4. Update the kanban board (`docs/architecture/kanban.md`)
5. Write iteration log to `docs/architecture/iterations/ITER-NN.md`
6. **Stopping criteria checklist:**
   - How many drivers in "Not Addressed"? (list (H,H) ones explicitly)
   - Residual risk: acceptable for the Design Purpose?
   - Are there (H,H) QA scenarios still in "Not Addressed"?
   - Has the design stabilized (few new concerns discovered)?
7. Present options:
   - A) **Continue** — start next iteration (if (H,H) drivers remain unaddressed)
   - B) **Plan next round** — defer remaining drivers, plan next design session
   - C) **Stop** — design is complete for current Design Purpose
   - D) Refine current decisions
   - E) Switch to another activity (BA, PM, Dev)
