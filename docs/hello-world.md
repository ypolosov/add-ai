# Hello World: полный SDLC-цикл с ADD-AI

Пошаговый tutorial, в котором мы проведём простое fullstack-приложение через весь цикл architecture-driven development — от первой оценки состояния до финального статус-отчёта.

**Что строим:** NestJS backend (`GET /api/hello`) + Next.js frontend (отображает приветствие)
**Зачем:** показать как 20 из 32 скиллов ADD-AI работают вместе в реальном SDLC-процессе
**Формат:** каждый шаг = команда → диалог с агентом → созданные артефакты

## Содержание

1. [Оценка состояния — `nav-resume`](#шаг-1-оценка-состояния)
2. [Трекинг проекта — `pm-init`](#шаг-2-трекинг-проекта)
3. [Инициализация архитектуры — `sa-init`](#шаг-3-инициализация-архитектуры)
4. [Выявление требований — `ba-requirements`](#шаг-4-выявление-требований)
5. [Use case — `ba-usecase`](#шаг-5-use-case)
6. [Атрибуты качества — `ba-qaw` + `ba-utility-tree`](#шаг-6-атрибуты-качества)
7. [Итерация архитектуры — `sa-iterate`](#шаг-7-итерация-архитектуры)
8. [Спринт-планирование — `pm-plan`](#шаг-8-спринт-планирование)
9. [Backend — `dev-scaffold` + `dev-implement`](#шаг-9-backend)
10. [Frontend — `fe-scaffold` + `fe-component` + `fe-api`](#шаг-10-frontend)
11. [Инфраструктура — `ops-docker` + `ops-pipeline`](#шаг-11-инфраструктура)
12. [Тестирование — `test-unit` + `test-integration`](#шаг-12-тестирование)
13. [Код-ревью — `review-code` + `review-standards`](#шаг-13-код-ревью)
14. [Финальный статус — `nav-status`](#шаг-14-финальный-статус)

---

## Prerequisites

- Claude Code установлен, add-ai плагин подключён (`claude --plugin-dir .` или через settings)
- GitHub-репозиторий `hello-world` инициализирован, `gh` CLI авторизован
- Node.js 20+

Создайте пустой проект:

```bash
mkdir hello-world && cd hello-world
git init && gh repo create hello-world --public --source=. --push
```

---

## Шаг 1: Оценка состояния

Навигатор сканирует все артефакты проекта, определяет текущую SDLC-фазу и предлагает следующие шаги. Точка входа в любую сессию.

**Команда:** `/add-ai:nav-resume`

### Диалог

```
🤖 Navigator:

# Project Status — 2026-03-12

## Current Position
- **SDLC Phase:** Not started
- **Last completed phase:** — (none)
- **Current phase:** — (none)
- **Status:** Project not initialized. No docs/ directory found.

## Artifacts
| Artifact | Count | Path |
|----------|-------|------|
| Quality Attributes (QA) | 0 | — |
| Use Cases (UC) | 0 | — |
| ADRs | 0 | — |
| ADD Iterations | 0 | — |

## Recommended Next Steps
1. `/add-ai:pm-init` — инициализировать трекинг проекта (labels, milestone)
2. `/add-ai:sa-init` — создать docs/architecture/ со всей структурой
3. `/add-ai:ba-requirements` — начать сбор требований
```

### Что создано
Ничего — навигатор работает в read-only режиме. Он только анализирует и рекомендует.

---

## Шаг 2: Трекинг проекта

PM-агент создаёт labels, milestone и начальные stories на GitHub. Это фундамент для дальнейшего планирования спринтов.

**Команда:** `/add-ai:pm-init`

### Диалог

```
🤖 Project Manager:

Обнаружена платформа: GitHub (gh CLI доступен)
Репозиторий: hello-world

Проверяю существующее состояние...
- Labels: 0 (создам 26)
- Milestones: 0 (создам 1)
- Issues: 0 (предложу 4 начальных stories)

Создать инфраструктуру трекинга?

1. Полная инициализация (labels + milestone + stories)
2. Только labels
3. Проверить что есть, показать пробелы
```

```
👤 User: 1
```

```
🤖 Project Manager:

## Project Tracking Initialized

### Labels Created (26)
- Type: type:epic, type:story, type:task, type:bug, type:spike (5)
- Role: role:sa, role:ba, role:pm, role:dev, role:fe, role:ops, role:test,
  role:review, role:nav (9)
- Phase: phase:requirements, phase:architecture, phase:development,
  phase:testing, phase:review (5)
- Priority: priority:high, priority:medium, priority:low (3)
- Status: status:backlog, status:in-progress, status:review, status:done (4)

### Milestone
- "Project Inception" created

### Initial Stories
- #1: Gather requirements (role:ba, phase:requirements)
- #2: Define architecture (role:sa, phase:architecture)
- #3: Set up CI/CD (role:ops, phase:development)
- #4: Set up project infrastructure (role:ops, phase:development)

Что дальше?
1. `/add-ai:sa-init` — инициализировать архитектурную документацию
2. `/add-ai:ba-requirements` — начать сбор требований
3. `/add-ai:nav-resume` — проверить обновлённый статус
```

### Что создано
- 26 labels на GitHub (type/role/phase/priority/status)
- Milestone "Project Inception"
- 4 issues (#1–#4) с labels

---

## Шаг 3: Инициализация архитектуры

SA-агент создаёт полную структуру `docs/architecture/` с файлами-заглушками для ADD 3.0 процесса, включая LikeC4 проект для C4-диаграмм.

**Команда:** `/add-ai:sa-init`

### Диалог

```
🤖 Solution Architect:

Перед созданием артефактов нужно установить контекст.

Какова цель дизайна?
A) Estimation — грубая оценка для предложения/бюджета
B) Exploratory prototype — spike для снижения неопределённости
C) Production development — полная архитектура для реализации
```

```
👤 User: C
```

```
🤖 Solution Architect:

Каков контекст системы?
A) Greenfield (mature domain) — есть reference architectures и стандарты
B) Greenfield (novel domain) — высокая неопределённость
C) Brownfield — расширение существующей системы
D) Legacy replacement — замена legacy
```

```
👤 User: A
```

```
🤖 Solution Architect:

## Architecture Initialized

Created docs/architecture/ with:

docs/architecture/
  README.md                      # Design Purpose: development, Context: greenfield-mature
  utility-tree.md                # Empty tree structure
  kanban.md                      # Not Addressed | Partially | Completely | Implemented | Verified
  c4/
    package.json                 # likec4 dependency
    src/
      specification.c4           # C4 element kinds
      model.c4                   # System context stub
      views.c4                   # Initial view definitions
      deployment.c4              # Empty deployment block
  adrs/
    0000-template.md             # MADR v3 template
  drivers/
    use-cases/
    quality-attributes/
    constraints/
    concerns/
  decisions/
    DD-000-template.md           # Design Decision template
  views/
  iterations/

Что дальше?
1. `/add-ai:ba-requirements` — начать сбор требований
2. `/add-ai:ba-qaw` — качественные атрибуты через QAW
3. `/add-ai:ba-utility-tree` — приоритизация атрибутов качества
```

### Что создано

```
docs/architecture/
├── README.md
├── utility-tree.md
├── kanban.md
├── c4/
│   ├── package.json
│   └── src/
│       ├── specification.c4
│       ├── model.c4
│       ├── views.c4
│       └── deployment.c4
├── adrs/
│   └── 0000-template.md
├── drivers/
│   ├── use-cases/
│   ├── quality-attributes/
│   ├── constraints/
│   └── concerns/
├── decisions/
│   └── DD-000-template.md
├── views/
└── iterations/
```

---

## Шаг 4: Выявление требований

BA-агент проводит интерактивную сессию для обнаружения функциональных и нефункциональных требований: use cases, quality attributes, constraints и concerns.

**Команда:** `/add-ai:ba-requirements`

### Диалог

```
🤖 Business Analyst:

Проверяю существующие требования...
- docs/requirements/ — не существует
- docs/architecture/drivers/ — пусто

Какую область хотите исследовать?
1. Функциональные требования (что система делает)
2. Нефункциональные требования (как система работает)
3. Ограничения и concerns
4. Всё сразу (комплексная сессия)
```

```
👤 User: 4
```

```
🤖 Business Analyst:

Отлично, проведём комплексную сессию.

Опишите основную функциональность системы — что она должна делать
для пользователя?
```

```
👤 User: Простое fullstack приложение. Backend на NestJS отдаёт GET /api/hello
с JSON { message: "Hello, World!" }. Frontend на Next.js вызывает этот endpoint
и отображает приветствие на странице. В будущем хотим добавить персонализацию
(имя пользователя), но сейчас это не в скоупе.
```

```
🤖 Business Analyst:

Понял. Уточняющие вопросы:

1. Кто является пользователем системы?
   — Любой посетитель (без аутентификации)?

2. Какие ограничения существуют?
   — Конкретный стек (NestJS + Next.js)?
   — Hosting requirements?

3. Есть ли требования к производительности?
   — Время ответа API, кол-во пользователей?
```

```
👤 User:
1. Да, любой посетитель, аутентификации нет
2. Стек: NestJS backend + Next.js frontend. Деплоим в Docker
3. Время ответа API < 200ms. Нагрузка минимальная — это tutorial-проект
```

```
🤖 Business Analyst:

Формализую обнаруженные требования:

## Функциональные требования
- **UC-001: Display Greeting** — пользователь открывает страницу, система
  отображает приветствие "Hello, World!" полученное от backend API

## Качественные атрибуты
- **QA-001: API Response Latency** — GET /api/hello отвечает за < 200ms
  при нормальной нагрузке (6-part scenario будет оформлен через /ba-qaw)

## Ограничения
- **CON-001: NestJS Backend** — backend реализуется на NestJS (technical)
- **CON-002: Next.js Frontend** — frontend реализуется на Next.js (technical)

## Concerns
- **CRN-001: Future Personalization** — в будущем нужна персонализация
  приветствия по имени пользователя. Сейчас не в скоупе, но архитектура
  должна позволять расширение.

Всё верно? Сохраняю артефакты?

1. Да, сохранить всё
2. Добавить ещё требования
3. Скорректировать существующие
```

```
👤 User: 1
```

```
🤖 Business Analyst:

## Артефакты сохранены

### Drivers (docs/architecture/drivers/)
- drivers/use-cases/UC-001.md — Display Greeting (summary)
- drivers/quality-attributes/QA-001.md — API Response Latency
- drivers/constraints/CON-001.md — NestJS Backend
- drivers/constraints/CON-002.md — Next.js Frontend
- drivers/concerns/CRN-001.md — Future Personalization

### Requirements (docs/requirements/)
- docs/requirements/ — directory created

Что дальше?
1. `/add-ai:ba-usecase` — детализировать UC-001 (полный use case spec)
2. `/add-ai:ba-qaw` — провести QAW для систематического выявления QA
3. `/add-ai:ba-utility-tree` — приоритизировать атрибуты качества
```

### Что создано

```
docs/architecture/drivers/
├── use-cases/
│   └── UC-001.md          # Display Greeting (summary)
├── quality-attributes/
│   └── QA-001.md          # API Response Latency
├── constraints/
│   ├── CON-001.md         # NestJS Backend
│   └── CON-002.md         # Next.js Frontend
└── concerns/
    └── CRN-001.md         # Future Personalization

docs/requirements/         # directory created
```

---

## Шаг 5: Use case

BA-агент создаёт детальную спецификацию use case: actors, preconditions, main success scenario, alternative/error flows, postconditions.

**Команда:** `/add-ai:ba-usecase create`

### Диалог

```
🤖 Business Analyst:

Найден driver: UC-001 — Display Greeting. Создаю полную спецификацию.

Опишите основной сценарий: что делает пользователь и как реагирует система?
```

```
👤 User: Пользователь открывает главную страницу. Frontend запрашивает
GET /api/hello. Backend возвращает { message: "Hello, World!" }.
Frontend отображает сообщение.
```

```
🤖 Business Analyst:

## UC-001: Display Greeting

### Summary
User visits the home page and sees a greeting message fetched from the backend API.

### Actors
- **Primary**: Anonymous User (browser)
- **System**: Hello World Application (frontend + backend)

### Preconditions
1. Backend service is running and accessible
2. Frontend is loaded in user's browser

### Trigger
User navigates to the home page (/)

### Main Success Scenario
1. User opens the home page in browser
2. Frontend sends GET /api/hello to backend
3. Backend returns { message: "Hello, World!" } with status 200
4. Frontend displays the greeting message on the page

### Alternative Flows

#### AF-1: Slow Network
- **At step:** 2
- **Condition:** Network latency > 1s
- **Steps:**
  1. Frontend shows loading indicator
  2. Returns to step 3 when response arrives

### Error Flows

#### EF-1: Backend Unavailable
- **At step:** 2
- **Condition:** Backend returns 5xx or connection refused
- **Steps:**
  1. Frontend displays error message: "Service unavailable"
  2. User can retry by refreshing the page

### Postconditions
#### Success
- Greeting message is visible on the page

#### Failure
- Error message is displayed instead of greeting

### Architectural Significance
- **Architecturally Significant:** Yes
- **Reason:** Drives QA-001 (latency), establishes frontend-backend contract

### Quality Attributes
- Related: QA-001

Сохраняю?

1. Да, сохранить
2. Добавить flows
3. Скорректировать
```

```
👤 User: 1
```

### Что создано

```
docs/requirements/use-cases/
└── UC-001-display-greeting.md    # Full use case specification

docs/architecture/drivers/use-cases/
└── UC-001.md                     # Updated summary with link
```

---

## Шаг 6: Атрибуты качества

Два скилла работают в паре: `ba-qaw` формализует QA-сценарии в 6-part формат, `ba-utility-tree` приоритизирует их для архитектурных итераций.

### 6a: Quality Attribute Workshop

**Команда:** `/add-ai:ba-qaw`

```
🤖 Business Analyst:

Начинаем Quality Attribute Workshop.

## Part 1: QAW Overview
QAW помогает систематически выявить и формализовать качественные атрибуты
через 6-part сценарии (source → stimulus → artifact → environment →
response → measure).

Готовы начать?

1. Да, начнём
2. Объясните подробнее формат 6-part scenario
```

```
👤 User: 1
```

```
🤖 Business Analyst:

## Part 2: Business Context
Из ba-requirements известно:
- Простое fullstack приложение (NestJS + Next.js)
- Один endpoint: GET /api/hello
- Нет аутентификации
- Будущая персонализация (CRN-001)

## Part 4: Architecture Drivers
Предварительно идентифицирован QA-001: API Response Latency.

Давайте формализуем его в 6-part scenario и проверим, есть ли другие QA.

Для QA-001 — какое поведение вы ожидаете?
```

```
👤 User: API должен отвечать меньше чем за 200ms при нормальной нагрузке.
Для tutorial-проекта это единственный значимый QA.
```

```
🤖 Business Analyst:

## QA-001: API Response Latency

| Part | Description |
|------|-------------|
| **Source** | Anonymous user (browser) |
| **Stimulus** | Sends GET /api/hello request |
| **Artifact** | Hello API endpoint |
| **Environment** | Normal operation (single user) |
| **Response** | Return JSON greeting |
| **Measure** | Response time < 200ms (p95) |

Priority: Business — **M**, Technical Difficulty — **L**

## Part 6: Consolidation

Один QA-сценарий для tutorial-проекта. Сохраняю результаты?

1. Да, сохранить QAW-результаты
2. Добавить ещё QA-сценарии
3. Изменить приоритеты
```

```
👤 User: 1
```

### 6b: Utility Tree

**Команда:** `/add-ai:ba-utility-tree build`

```
🤖 Business Analyst:

Читаю QAW-результаты...
Найден QA-001: API Response Latency (M, L)

## Utility Tree: Hello World

### Performance
#### Latency
- QA-001: API response < 200ms (p95) — Priority: M, Difficulty: L

### Modifiability
#### Extensibility
- (linked to CRN-001: Future Personalization) — Priority: M, Difficulty: L

Всего: 1 формализованный QA + 1 неформализованный concern.
Нет (H,H) драйверов — проект с низким архитектурным риском.

Сохраняю utility tree?

1. Да
2. Повысить приоритеты
3. Добавить QA-сценарии
```

```
👤 User: 1
```

### Что создано

```
docs/requirements/
├── qaw-results.md                # QAW session log
└── utility-tree.md               # Prioritized quality attributes

docs/architecture/
├── utility-tree.md               # Synced copy for SA
└── drivers/quality-attributes/
    └── QA-001.md                 # Updated with 6-part scenario
```

---

## Шаг 7: Итерация архитектуры

SA-агент проводит полную ADD 3.0 итерацию (7 шагов): review inputs → establish goal → choose element → design concepts → instantiate → sketch views → review & assess.

**Команда:** `/add-ai:sa-iterate`

### Диалог

```
🤖 Solution Architect:

## Step 1: Review Inputs

- **Design Purpose:** Production development
- **System Context:** Greenfield (mature domain)
- **Utility Tree:**
  - QA-001: API latency < 200ms — (M, L)
- **Drivers:**
  - UC-001: Display Greeting
  - CON-001: NestJS Backend
  - CON-002: Next.js Frontend
  - CRN-001: Future Personalization
- **Kanban:** Not Addressed: 3 | Partially: 0 | Completely: 0

Есть ли новые stakeholder concerns, не отражённые в драйверах?
```

```
👤 User: Нет, всё учтено.
```

```
🤖 Solution Architect:

## Step 2: Iteration Goal

Наиболее приоритетные unaddressed drivers:
1. UC-001: Display Greeting — основной use case
2. QA-001: API latency — единственный QA
3. CRN-001: Future Personalization — concern (влияет на структуру)

Рекомендую все три в одну итерацию (проект простой).

Сформулируйте цель итерации:
Template: "Итерация ITER-01 решает [что] путём [как]"
```

```
👤 User: Итерация ITER-01 решает отображение приветствия (UC-001) с гарантией
латентности (QA-001) путём разделения на frontend/backend с hexagonal
architecture на backend.
```

```
🤖 Solution Architect:

## Step 3: Choose Element to Refine

Текущая C4-модель содержит один элемент: HelloWorldSystem (system context).

Тип уточнения:
A) **Decompose** — разбить HelloWorldSystem на компоненты
B) Improve — улучшить внутреннюю структуру
C) Add — добавить новый элемент

Рекомендация: **A) Decompose** — разбить систему на Backend (NestJS)
и Frontend (Next.js) с API-контрактом между ними.

1. Согласен — Decompose
2. Другой вариант
```

```
👤 User: 1
```

```
🤖 Solution Architect:

## Step 4: Design Concepts

Для UC-001 + QA-001 + CON-001/002:

| Alternative | Effort | Quality Impact | Risk | Trade-offs |
|-------------|--------|----------------|------|------------|
| Monorepo (Nx/Turborepo) | M | Good separation, shared types | L | Build complexity |
| Separate repos | L | Full isolation | L | No shared types |
| Monolith (Next.js API routes) | S | Simplest | L | No hexagonal, hard to extend |

Рекомендация: **Separate repos** (два отдельных приложения) —
простейший вариант для tutorial, чёткое разделение.

Для CRN-001 (modifiability): hexagonal architecture на backend
обеспечивает расширяемость через порты и адаптеры.

1. Согласен — separate apps + hexagonal backend
2. Monorepo
3. Monolith
```

```
👤 User: 1
```

```
🤖 Solution Architect:

## Step 5: Instantiate Elements

Тип структуры: **C&C structure** (runtime элементы)

| Element | Responsibilities | Provided Interfaces | Required Interfaces |
|---------|-----------------|---------------------|---------------------|
| HelloBackend (NestJS) | Serve greeting API | GET /api/hello → JSON | — |
| HelloFrontend (Next.js) | Display greeting UI | HTML page at / | GET /api/hello |
| HelloService | Business logic (greeting message) | getGreeting(): string | — |
| HelloController | HTTP adapter (REST) | GET /api/hello | HelloService |

Архитектурная схема:

```
User → [Next.js Frontend] → GET /api/hello → [NestJS Backend]
                                                ├── HelloController (interface)
                                                ├── HelloService (application)
                                                └── (core domain — trivial)
```

Подтверждаете?

1. Да, сохранить и перейти к views
2. Добавить элементы
3. Скорректировать
```

```
👤 User: 1
```

```
🤖 Solution Architect:

## Step 6: Sketch Views & Record Decisions

### ADR-0001: Separate Frontend and Backend Applications

**Status:** Accepted
**Date:** 2026-03-12

**Context:** Hello World — fullstack приложение с NestJS backend и Next.js
frontend. Нужно определить как организовать код и runtime-архитектуру.

**Decision Drivers:**
- UC-001: Display Greeting
- QA-001: API Response Latency
- CON-001: NestJS Backend
- CON-002: Next.js Frontend
- CRN-001: Future Personalization

**Considered Options:**
1. Separate applications (NestJS + Next.js)
2. Monorepo with shared types
3. Monolith (Next.js API routes only)

**Decision Outcome:** Option 1 — Separate applications.
Hexagonal architecture on backend for extensibility (CRN-001).

### DD-001: Hexagonal Architecture for Backend

- **Iteration:** ITER-01
- **Drivers:** QA-001, UC-001, CRN-001
- **Decision:** Backend follows hexagonal architecture (ports & adapters)
- **Rationale:** CRN-001 requires easy extension. Hex arch isolates
  business logic from framework, making future personalization a new
  adapter/port addition.

### C4 Model Updated
- model.c4 — decomposed into HelloBackend + HelloFrontend
- views.c4 — container view + component view for backend

### Kanban Updated

1. Да, всё верно, перейти к review
2. Скорректировать ADR
3. Добавить ещё решения
```

```
👤 User: 1
```

```
🤖 Solution Architect:

## Step 7: Review & Assess

### Tactics Conflict Check
| Tactic A | QA | Tactic B | QA | Conflict | Resolution |
|----------|-----|----------|-----|----------|------------|
| Hexagonal layers | Modifiability | Direct calls | Performance | Minimal overhead | Acceptable — in-process call |

Конфликтов нет — overhead hexagonal architecture пренебрежимо мал
для in-process вызовов.

### Kanban Update
| Not Addressed | Partially | Completely | Implemented | Verified |
|---------------|-----------|------------|-------------|----------|
| 0             | 0         | 3          | 0           | 0        |

UC-001, QA-001, CRN-001 → **Completely Addressed**

### Stopping Criteria
- [x] All (H,H) drivers addressed (нет (H,H) — все M/L)
- [x] Residual risk acceptable
- [x] Design stabilized

Рекомендация: **Stop** — дизайн достаточен для текущего Design Purpose.

1. Stop — перейти к Sprint Planning
2. Continue — начать ITER-02
3. Refine — уточнить текущие решения
4. Switch — переключиться на BA/PM/Dev
```

```
👤 User: 1
```

### Что создано

```
docs/architecture/
├── adrs/
│   └── 0001-separate-frontend-backend.md    # ADR-0001 (MADR v3)
├── decisions/
│   └── DD-001-hexagonal-backend.md          # Design Decision
├── iterations/
│   └── ITER-01.md                           # Full 7-step iteration log
├── kanban.md                                # Updated: 3 Completely Addressed
├── views/
│   └── hello-backend-ert.md                 # Element Responsibility Table
└── c4/src/
    ├── model.c4                             # Updated: HelloBackend + HelloFrontend
    └── views.c4                             # Updated: container + component views
```

---

## Шаг 8: Спринт-планирование

PM-агент превращает архитектурные решения в actionable issues на GitHub: stories и tasks с labels, связанные с ADR и требованиями.

**Команда:** `/add-ai:pm-plan`

### Диалог

```
🤖 Project Manager:

## Sprint Planning

Читаю контекст...
- Kanban: 3 items в "Completely Addressed" (UC-001, QA-001, CRN-001)
- ADR: ADR-0001 accepted (Separate Frontend and Backend)
- DD: DD-001 (Hexagonal Architecture)

Предлагаю Sprint 1 — "Hello World MVP":

| # | Title | Type | Role | Priority | Size |
|---|-------|------|------|----------|------|
| 1 | Backend: scaffold hello module | story | role:dev | high | S |
| 2 | Backend: implement GET /api/hello | task | role:dev | high | S |
| 3 | Frontend: scaffold Next.js app | story | role:fe | high | S |
| 4 | Frontend: greeting component | task | role:fe | high | S |
| 5 | Frontend: API layer for /api/hello | task | role:fe | medium | S |
| 6 | Docker setup (backend + frontend) | story | role:ops | medium | S |
| 7 | CI pipeline (lint + test + build) | story | role:ops | medium | S |
| 8 | Unit tests | story | role:test | medium | S |
| 9 | Integration tests | story | role:test | medium | S |

Все issues будут привязаны к milestone "Project Inception"
и содержать ссылки на ADR-0001, UC-001.

1. Создать все 9 issues
2. Выбрать подмножество
3. Скорректировать
```

```
👤 User: 1
```

```
🤖 Project Manager:

## Sprint 1 Created

Issues created on GitHub:
- #5: Backend: scaffold hello module (role:dev, phase:development, priority:high)
- #6: Backend: implement GET /api/hello (role:dev, phase:development, priority:high)
- #7: Frontend: scaffold Next.js app (role:fe, phase:development, priority:high)
- #8: Frontend: greeting component (role:fe, phase:development, priority:high)
- #9: Frontend: API layer (role:fe, phase:development, priority:medium)
- #10: Docker setup (role:ops, phase:development, priority:medium)
- #11: CI pipeline (role:ops, phase:development, priority:medium)
- #12: Unit tests (role:test, phase:testing, priority:medium)
- #13: Integration tests (role:test, phase:testing, priority:medium)

All linked to milestone "Project Inception".

Что дальше?
1. `/add-ai:dev-scaffold` — начать с backend scaffolding (#5)
2. `/add-ai:fe-scaffold` — начать с frontend scaffolding (#7)
3. `/add-ai:nav-resume` — проверить полный статус
```

### Что создано
- 9 issues на GitHub (#5–#13) с labels (type, role, phase, priority)
- Issues привязаны к milestone "Project Inception"
- Каждый issue содержит ссылки на ADR-0001, UC-001, DD-001

---

## Шаг 9: Backend

Два скилла: `dev-scaffold` создаёт структуру модуля (hexagonal architecture), `dev-implement` реализует use case.

### 9a: Scaffold

**Команда:** `/add-ai:dev-scaffold hello`

```
🤖 Backend Developer:

Определяю проект...
- Framework: NestJS (из CON-001 + package.json)
- Source root: src/
- Architecture: hexagonal (из ADR-0001, DD-001)

Scaffold модуля "hello":

```
src/
  core/domain/hello/
    hello.entity.ts                # Greeting entity
    hello.repository.port.ts       # Repository interface

  core/application/hello/
    ports/inbound/
      hello.use-cases.ts           # GetGreeting use case interface
    services/
      hello.service.ts             # Use case implementation
    dto/
      hello.dto.ts                 # GreetingResponseDto

  interfaces/http/hello/
    hello.controller.ts            # GET /api/hello
    hello.response.ts              # Response DTO

  modules/hello/
    hello.module.ts                # NestJS module wiring
```

Infrastructure layer пропущен — для простого greeting не нужен
persistence. HelloService возвращает значение напрямую.

1. Создать все файлы
2. Добавить infrastructure layer
3. Скорректировать структуру
```

```
👤 User: 1
```

### 9b: Implement

**Команда:** `/add-ai:dev-implement UC-001`

```
🤖 Backend Developer:

Читаю UC-001: Display Greeting...
- Main Success Scenario step 3: Backend returns { message: "Hello, World!" }
- Related: ADR-0001, DD-001, QA-001

Подход к реализации:
1. Implementation First — реализация → тесты (по умолчанию)
2. TDD — тесты → реализация → рефакторинг
```

```
👤 User: 1
```

```
🤖 Backend Developer:

## Implementation Plan

1. `hello.entity.ts` — Greeting entity с message property
2. `hello.use-cases.ts` — GetGreetingUseCase interface
3. `hello.service.ts` — реализация: returns "Hello, World!"
4. `hello.dto.ts` — GreetingResponseDto { message: string }
5. `hello.controller.ts` — GET /api/hello → HelloService → DTO
6. `hello.module.ts` — wiring
7. `app.module.ts` — register HelloModule

Подтверждаете?

1. Да, реализовать
2. Скорректировать план
```

```
👤 User: 1
```

```
🤖 Backend Developer:

## Implementation Complete

### Key files:

**hello.service.ts** (core/application)
```typescript
@Injectable()
export class HelloService implements GetGreetingUseCase {
  execute(): GreetingResponseDto {
    return { message: 'Hello, World!' };
  }
}
```

**hello.controller.ts** (interfaces/http)
```typescript
@Controller('api')
export class HelloController {
  constructor(
    @Inject('GetGreetingUseCase')
    private readonly getGreeting: GetGreetingUseCase,
  ) {}

  @Get('hello')
  getHello(): GreetingResponseDto {
    return this.getGreeting.execute();
  }
}
```

**hello.module.ts** (modules)
```typescript
@Module({
  providers: [
    { provide: 'GetGreetingUseCase', useClass: HelloService },
  ],
  controllers: [HelloController],
})
export class HelloModule {}
```

// ADR-0001: Separate frontend/backend
// DD-001: Hexagonal architecture — core has no framework deps

Что дальше?
1. `/add-ai:test-unit` — unit-тесты для HelloService
2. `/add-ai:test-integration` — интеграционные тесты для API
3. `/add-ai:review-code` — проверить код vs ADR
```

### Что создано

```
src/
├── core/
│   ├── domain/hello/
│   │   ├── hello.entity.ts
│   │   └── hello.repository.port.ts
│   └── application/hello/
│       ├── ports/inbound/
│       │   └── hello.use-cases.ts
│       ├── services/
│       │   └── hello.service.ts
│       └── dto/
│           └── hello.dto.ts
├── interfaces/http/hello/
│   ├── hello.controller.ts
│   └── hello.response.ts
└── modules/hello/
    └── hello.module.ts
```

---

## Шаг 10: Frontend

Три скилла: `fe-scaffold` создаёт страницу, `fe-component` — UI-компонент, `fe-api` — типизированный API-слой.

### 10a: Scaffold

**Команда:** `/add-ai:fe-scaffold hello`

```
🤖 Frontend Developer:

Определяю проект...
- Framework: Next.js (App Router) — из CON-002 + package.json
- Styling: Tailwind CSS (из tailwind.config.js)

Scaffold страницы "hello":

```
app/
  page.tsx           # Home page — displays greeting
  loading.tsx        # Loading state
  error.tsx          # Error boundary
```

1. Создать файлы
2. Добавить layout.tsx
3. Скорректировать
```

```
👤 User: 1
```

### 10b: Component

**Команда:** `/add-ai:fe-component Greeting`

```
🤖 Frontend Developer:

Определяю конвенции...
- Framework: React (Next.js)
- Styling: Tailwind CSS
- Component dir: src/components/

Подход к реализации:
1. Implementation First — компонент → тесты (по умолчанию)
2. TDD — тесты → компонент → рефакторинг
```

```
👤 User: 1
```

```
🤖 Frontend Developer:

## Greeting Component

**src/components/greeting/Greeting.tsx**
```tsx
interface GreetingProps {
  message: string;
}

export function Greeting({ message }: GreetingProps) {
  return (
    <main role="main" className="flex min-h-screen items-center justify-center">
      <h1 className="text-4xl font-bold">{message}</h1>
    </main>
  );
}
```

TypeScript props, semantic HTML, ARIA role, Tailwind styling.

1. Сохранить
2. Добавить варианты (loading/error states)
3. Скорректировать
```

```
👤 User: 1
```

### 10c: API Layer

**Команда:** `/add-ai:fe-api hello`

```
🤖 Frontend Developer:

Определяю паттерны...
- Data fetching: fetch (Next.js built-in)
- API style: REST
- Existing API layer: нет

Подход к реализации:
1. Implementation First — API layer → тесты (по умолчанию)
2. TDD — тесты → API layer → рефакторинг
```

```
👤 User: 1
```

```
🤖 Frontend Developer:

## API Layer Generated

**src/api/hello.ts** — API client
```typescript
export interface GreetingResponse {
  message: string;
}

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:3001';

export async function fetchGreeting(): Promise<GreetingResponse> {
  const res = await fetch(`${API_BASE}/api/hello`);
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}
```

**app/page.tsx** — updated to use API
```tsx
import { fetchGreeting } from '@/api/hello';
import { Greeting } from '@/components/greeting/Greeting';

export default async function HomePage() {
  const data = await fetchGreeting();
  return <Greeting message={data.message} />;
}
```

Что дальше?
1. `/add-ai:test-unit` — тесты для Greeting компонента
2. `/add-ai:ops-docker` — Docker configuration
3. `/add-ai:review-code` — проверить код
```

### Что создано

```
app/
├── page.tsx              # Home page (uses API + Greeting)
├── loading.tsx           # Loading state
└── error.tsx             # Error boundary

src/
├── components/greeting/
│   └── Greeting.tsx      # Greeting component
├── api/
│   └── hello.ts          # API client (fetchGreeting)
└── types/
    └── hello.types.ts    # GreetingResponse type
```

---

## Шаг 11: Инфраструктура

`ops-docker` генерирует Dockerfile и docker-compose, `ops-pipeline` — CI/CD workflow для GitHub Actions.

### 11a: Docker

**Команда:** `/add-ai:ops-docker`

```
🤖 DevOps Engineer:

Анализирую проект...
- Backend: Node.js (NestJS) — порт 3001
- Frontend: Node.js (Next.js) — порт 3000
- Package manager: npm (lock file detected)

Target environment?
1. Development (hot reload, volumes)
2. Production (multi-stage, optimized)
3. Both (development + production configs)
```

```
👤 User: 3
```

```
🤖 DevOps Engineer:

## Docker Configuration

### Dockerfile.backend (multi-stage)
- Stage 1: build (npm ci + npm run build)
- Stage 2: production (node:20-alpine, non-root user, health check)

### Dockerfile.frontend (multi-stage)
- Stage 1: build (npm ci + npm run build)
- Stage 2: production (node:20-alpine, Next.js standalone)

### docker-compose.yml
```yaml
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports: ["3001:3001"]
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:3001/api/hello"]

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports: ["3000:3000"]
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:3001
    depends_on:
      backend:
        condition: service_healthy
```

### docker-compose.dev.yml
- Volume mounts for hot reload
- Node debug ports

### .dockerignore
- node_modules, .git, dist, .next, *.md

Что дальше?
1. `/add-ai:ops-pipeline` — CI/CD pipeline
2. `/add-ai:ops-deploy` — deployment configuration
3. Скорректировать Docker config
```

```
👤 User: 1
```

### 11b: CI Pipeline

**Команда:** `/add-ai:ops-pipeline`

```
🤖 DevOps Engineer:

Определяю платформу...
- CI/CD: GitHub Actions (из git remote)
- Test runner: Jest (из package.json)
- Linter: ESLint

Предлагаю pipeline stages:

1. Install → 2. Lint → 3. Type Check → 4. Unit Tests →
5. Build → 6. Integration Tests

1. Создать pipeline с этими stages
2. Добавить deploy stage
3. Скорректировать stages
```

```
👤 User: 1
```

```
🤖 DevOps Engineer:

## CI Pipeline Created

**.github/workflows/ci.yml**
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm test
      - run: npm run build
      - run: npm run test:integration
```

Что дальше?
1. `/add-ai:test-unit` — написать тесты до первого CI run
2. `/add-ai:ops-deploy` — deployment config
3. `/add-ai:review-code` — проверить инфраструктуру
```

### Что создано

```
Dockerfile.backend             # Multi-stage NestJS build
Dockerfile.frontend            # Multi-stage Next.js build
docker-compose.yml             # Production compose
docker-compose.dev.yml         # Development compose (hot reload)
.dockerignore                  # Exclude node_modules, .git, etc.
.github/workflows/ci.yml      # GitHub Actions CI pipeline
```

---

## Шаг 12: Тестирование

`test-unit` генерирует unit-тесты (AAA pattern), `test-integration` — интеграционные тесты для API endpoints.

### 12a: Unit Tests

**Команда:** `/add-ai:test-unit hello`

```
🤖 Tester:

Определяю test framework...
- Runner: Jest (из package.json)
- Pattern: *.spec.ts (co-located)

Анализирую модуль hello...

Идентифицированные тест-кейсы:
1. HelloService.execute() — returns greeting message
2. HelloService.execute() — returns correct DTO shape
3. HelloController — calls use case and returns result
4. HelloController — endpoint responds with 200

Генерирую unit-тесты (AAA pattern)?

1. Да, все 4 кейса
2. Выбрать подмножество
3. Добавить edge cases
```

```
👤 User: 1
```

```
🤖 Tester:

## Unit Tests Generated

**src/core/application/hello/services/hello.service.spec.ts**
```typescript
describe('HelloService', () => {
  let service: HelloService;

  beforeEach(() => {
    service = new HelloService();
  });

  it('should return greeting message', () => {
    // Arrange — service created in beforeEach
    // Act
    const result = service.execute();
    // Assert
    expect(result.message).toBe('Hello, World!');
  });

  it('should return GreetingResponseDto shape', () => {
    // Arrange & Act
    const result = service.execute();
    // Assert
    expect(result).toHaveProperty('message');
    expect(typeof result.message).toBe('string');
  });
});
```

**src/interfaces/http/hello/hello.controller.spec.ts**
```typescript
describe('HelloController', () => {
  let controller: HelloController;
  let mockUseCase: GetGreetingUseCase;

  beforeEach(() => {
    // Arrange
    mockUseCase = { execute: jest.fn().mockReturnValue({ message: 'Hello, World!' }) };
    controller = new HelloController(mockUseCase);
  });

  it('should return greeting from use case', () => {
    // Act
    const result = controller.getHello();
    // Assert
    expect(result).toEqual({ message: 'Hello, World!' });
    expect(mockUseCase.execute).toHaveBeenCalled();
  });
});
```

// UC-001: Display Greeting — main success scenario steps 3-4

Что дальше?
1. `/add-ai:test-integration` — интеграционные тесты для API
2. Запустить тесты (`npm test`)
3. Добавить тесты для frontend компонентов
```

```
👤 User: 1
```

### 12b: Integration Tests

**Команда:** `/add-ai:test-integration hello`

```
🤖 Tester:

Определяю инструменты...
- HTTP testing: supertest (из package.json)
- Test runner: Jest

Анализирую API endpoints...
- GET /api/hello — returns { message: "Hello, World!" }

Генерирую интеграционные тесты?

1. Да
2. Добавить custom scenarios
```

```
👤 User: 1
```

```
🤖 Tester:

## Integration Tests Generated

**test/integration/hello/hello.api.spec.ts**
```typescript
describe('GET /api/hello', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = moduleFixture.createNestApplication();
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  it('should return 200 with greeting message', async () => {
    // Act
    const response = await request(app.getHttpServer())
      .get('/api/hello')
      .expect(200);

    // Assert
    expect(response.body).toEqual({ message: 'Hello, World!' });
  });

  it('should respond within 200ms (QA-001)', async () => {
    // Arrange
    const start = Date.now();
    // Act
    await request(app.getHttpServer()).get('/api/hello');
    // Assert
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(200);
  });

  it('should return correct content-type', async () => {
    // Act & Assert
    await request(app.getHttpServer())
      .get('/api/hello')
      .expect('Content-Type', /json/);
  });
});
```

// QA-001: API Response Latency < 200ms — verified in test

Что дальше?
1. `/add-ai:review-code` — проверить весь код vs ADR
2. `/add-ai:review-standards` — audit структуры проекта
3. Запустить все тесты
```

### Что создано

```
src/core/application/hello/services/
└── hello.service.spec.ts              # Unit tests (AAA pattern)

src/interfaces/http/hello/
└── hello.controller.spec.ts           # Controller unit tests

test/integration/hello/
└── hello.api.spec.ts                  # API integration tests (supertest)
```

---

## Шаг 13: Код-ревью

`review-code` проверяет код против ADR и паттернов, `review-standards` проводит аудит структуры проекта.

### 13a: Code Review

**Команда:** `/add-ai:review-code`

```
🤖 Code Reviewer:

Собираю код для ревью...
- git diff: all uncommitted changes
- ADRs: ADR-0001 (Separate Frontend/Backend)
- Patterns: hexagonal architecture (DD-001)

## Review Summary
- Files reviewed: 15
- Issues found: 2 (critical: 0, warning: 1, info: 1)

## Issues

### [WARNING] src/api/hello.ts:5 — Hardcoded fallback URL
API_BASE fallback `http://localhost:3001` is hardcoded.
Consider documenting required env var NEXT_PUBLIC_API_URL.
Related: ADR-0001

### [INFO] src/core/application/hello/services/hello.service.ts:4 — Static greeting
Greeting message is hardcoded in service. When CRN-001
(Future Personalization) is addressed, this will need to
accept parameters.
Related: CRN-001

## Architecture Compliance
✅ Dependency direction: correct (interfaces → core ← infrastructure)
✅ ADR-0001: frontend and backend are properly separated
✅ DD-001: hexagonal layers respected, core has no NestJS imports
✅ No secrets in code

Что дальше?
1. Создать issues для findings
2. Исправить warnings
3. Перейти к standards audit
```

```
👤 User: 3
```

### 13b: Standards Audit

**Команда:** `/add-ai:review-standards`

```
🤖 Code Reviewer:

Читаю стандарты проекта...
- ADRs: docs/architecture/adrs/
- Architecture: docs/architecture/
- Linter: .eslintrc.js

## Standards Audit Report

### Summary
- Areas audited: 4
- Compliant: 4 | Violations: 0

### Directory Structure ✅
- Hexagonal layers properly organized (core/domain, core/application,
  interfaces/http, modules)
- docs/architecture/ follows conventions
- tests in correct locations

### Naming Conventions ✅
- Files: kebab-case (.ts)
- Classes: PascalCase
- Artifact IDs: UC-001, QA-001, ADR-0001, DD-001 — consistent

### Dependency Direction ✅
- core/ has no imports from interfaces/ or infrastructure/
- Proper port/adapter pattern via DI

### Configuration ✅
- Environment variables documented
- No hardcoded secrets

### Recommendations
- Consider adding .env.example with NEXT_PUBLIC_API_URL
- Consider adding README.md with setup instructions

Что дальше?
1. Создать .env.example
2. Создать issues для рекомендаций
3. `/add-ai:nav-status` — финальный статус
```

```
👤 User: 3
```

### Что создано
Ничего — Code Reviewer работает в read-only режиме. Генерирует отчёты, но не изменяет код.

---

## Шаг 14: Финальный статус

Навигатор собирает cross-role метрики: kanban progress, issue statistics, artifact coverage, traceability gaps.

**Команда:** `/add-ai:nav-status`

### Диалог

```
🤖 Navigator:

# Unified Project Status — 2026-03-12

## SDLC Phase
**Development/Testing** — backend and frontend implemented, tests written,
infrastructure configured.

## Progress Summary
| Metric | Value |
|--------|-------|
| Drivers addressed | 3/3 (100%) |
| ADRs accepted | 1 |
| Issues completed | 0/13 (0% — code written, issues not closed yet) |
| Test coverage (scenarios) | 1/1 UC covered |

## Design Kanban
| Not Addressed | Partially | Completely | Implemented | Verified |
|---------------|-----------|------------|-------------|----------|
| 0             | 0         | 0          | 3           | 0        |

## Issues by Phase
| Phase | Open | In Progress | Done | Total |
|-------|------|-------------|------|-------|
| phase:requirements | 0 | 0 | 0 | 1 |
| phase:architecture | 0 | 0 | 0 | 1 |
| phase:development | 7 | 0 | 0 | 7 |
| phase:testing | 2 | 0 | 0 | 2 |
| phase:review | 0 | 0 | 0 | 2 |

## Traceability
UC-001 → QA-001 → ADR-0001 → DD-001 → code → tests ✅
Complete traceability chain from requirement to verification.

## Traceability Gaps
- Issues not yet closed (code exists but issues are open)
- No E2E tests (SC-NNN not created — optional for this project)
- Kanban items in "Implemented" but not "Verified" (need test run)

## Recommendations
1. Run `npm test` and `npm run test:integration` to verify all tests pass
2. Close completed issues on GitHub
3. Move kanban items to "Verified" after successful test run
4. Consider `/add-ai:ba-scenario` for SC-001 if E2E testing needed
```

### Что создано
Ничего — навигатор работает в read-only режиме.

---

## Итоги

### Полное дерево созданных файлов

```
hello-world/
├── docs/
│   ├── architecture/
│   │   ├── README.md                                # Project context
│   │   ├── utility-tree.md                          # QA priorities
│   │   ├── kanban.md                                # Design progress
│   │   ├── c4/
│   │   │   ├── package.json
│   │   │   └── src/
│   │   │       ├── specification.c4
│   │   │       ├── model.c4                         # HelloBackend + HelloFrontend
│   │   │       ├── views.c4                         # Container + component views
│   │   │       └── deployment.c4
│   │   ├── adrs/
│   │   │   ├── 0000-template.md
│   │   │   └── 0001-separate-frontend-backend.md    # ADR-0001
│   │   ├── drivers/
│   │   │   ├── use-cases/
│   │   │   │   └── UC-001.md
│   │   │   ├── quality-attributes/
│   │   │   │   └── QA-001.md
│   │   │   ├── constraints/
│   │   │   │   ├── CON-001.md                       # NestJS Backend
│   │   │   │   └── CON-002.md                       # Next.js Frontend
│   │   │   └── concerns/
│   │   │       └── CRN-001.md                       # Future Personalization
│   │   ├── decisions/
│   │   │   ├── DD-000-template.md
│   │   │   └── DD-001-hexagonal-backend.md
│   │   ├── views/
│   │   │   └── hello-backend-ert.md                 # Element Responsibility Table
│   │   └── iterations/
│   │       └── ITER-01.md                           # ADD 3.0 iteration log
│   └── requirements/
│       ├── qaw-results.md
│       ├── utility-tree.md
│       └── use-cases/
│           └── UC-001-display-greeting.md
│
├── src/
│   ├── core/
│   │   ├── domain/hello/
│   │   │   ├── hello.entity.ts
│   │   │   └── hello.repository.port.ts
│   │   └── application/hello/
│   │       ├── ports/inbound/
│   │       │   └── hello.use-cases.ts
│   │       ├── services/
│   │       │   ├── hello.service.ts
│   │       │   └── hello.service.spec.ts
│   │       └── dto/
│   │           └── hello.dto.ts
│   ├── interfaces/http/hello/
│   │   ├── hello.controller.ts
│   │   ├── hello.controller.spec.ts
│   │   └── hello.response.ts
│   └── modules/hello/
│       └── hello.module.ts
│
├── app/                                              # Next.js (App Router)
│   ├── page.tsx
│   ├── loading.tsx
│   └── error.tsx
│
├── src/                                              # Frontend src
│   ├── components/greeting/
│   │   └── Greeting.tsx
│   ├── api/
│   │   └── hello.ts
│   └── types/
│       └── hello.types.ts
│
├── test/integration/hello/
│   └── hello.api.spec.ts
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── docker-compose.dev.yml
├── .dockerignore
└── .github/workflows/
    └── ci.yml
```

### Трассировка артефактов

| Requirement | Architecture | Code | Tests |
|------------|--------------|------|-------|
| UC-001: Display Greeting | ADR-0001, DD-001 | HelloService, HelloController, Greeting.tsx | hello.service.spec.ts, hello.controller.spec.ts, hello.api.spec.ts |
| QA-001: API Latency < 200ms | ADR-0001 | HelloController (GET /api/hello) | hello.api.spec.ts (latency assertion) |
| CON-001: NestJS Backend | ADR-0001 | src/ (hexagonal structure) | — |
| CON-002: Next.js Frontend | ADR-0001 | app/, src/components/ | — |
| CRN-001: Future Personalization | DD-001 (hexagonal) | Port/adapter separation | — (deferred) |

### Использованные скиллы (20 из 32)

| # | Скилл | Агент | Шаг |
|---|-------|-------|-----|
| 1 | `nav-resume` | Navigator | 1 |
| 2 | `pm-init` | Project Manager | 2 |
| 3 | `sa-init` | Solution Architect | 3 |
| 4 | `ba-requirements` | Business Analyst | 4 |
| 5 | `ba-usecase` | Business Analyst | 5 |
| 6 | `ba-qaw` | Business Analyst | 6 |
| 7 | `ba-utility-tree` | Business Analyst | 6 |
| 8 | `sa-iterate` | Solution Architect | 7 |
| 9 | `sa-adr` | Solution Architect | 7 (internally) |
| 10 | `sa-diagram` | Solution Architect | 7 (internally) |
| 11 | `sa-kanban` | Solution Architect | 7 (internally) |
| 12 | `pm-plan` | Project Manager | 8 |
| 13 | `dev-scaffold` | Backend Developer | 9 |
| 14 | `dev-implement` | Backend Developer | 9 |
| 15 | `fe-scaffold` | Frontend Developer | 10 |
| 16 | `fe-component` | Frontend Developer | 10 |
| 17 | `fe-api` | Frontend Developer | 10 |
| 18 | `ops-docker` | DevOps Engineer | 11 |
| 19 | `ops-pipeline` | DevOps Engineer | 11 |
| 20 | `test-unit` | Tester | 12 |
| 21 | `test-integration` | Tester | 12 |
| 22 | `review-code` | Code Reviewer | 13 |
| 23 | `review-standards` | Code Reviewer | 13 |
| 24 | `nav-status` | Navigator | 14 |

---

## Советы и следующие шаги

### Ежедневная работа

- **Начинайте сессию с** `/add-ai:nav-resume` — навигатор покажет где вы остановились и что делать дальше
- **TDD mode** доступен в `dev-implement`, `fe-component`, `fe-api` — выбирайте вариант 2 при старте реализации
- **`pm-status`** — быстрая сводка по issues без полного analysis навигатора
- **`sa-kanban`** — управление design kanban board отдельно от итераций

### Скиллы не покрытые в tutorial

| Скилл | Когда нужен |
|-------|-------------|
| `ba-scenario` | Composite flows (SC-NNN) — когда UC недостаточно и нужны cross-cutting сценарии |
| `sa-review` | Архитектурный review vs QA-сценарии — проверить что архитектура отвечает всем QA |
| `sa-adr` | Standalone ADR management — создание/обновление ADR вне итерации |
| `sa-diagram` | Standalone diagram management — LikeC4 dynamic и deployment views |
| `test-e2e` | E2E тесты (Playwright/Cypress) — из SC-NNN сценариев |
| `test-bdd` | BDD сценарии (Gherkin) — из SC-NNN в .feature файлы |
| `review-pr` | PR review — полный checklist для pull request |
| `ops-deploy` | Deployment config — Kubernetes, cloud platforms |
| `pm-issue` | CRUD для отдельных issues — создание/обновление вне sprint planning |
| `pm-status` | Status report — лёгкая альтернатива nav-status |

### Расширение проекта

Хотите продолжить? Вот идеи для следующей итерации:

1. **CRN-001 → ITER-02**: персонализированные приветствия — новый use case UC-002, параметр `name` в API, input field на frontend
2. **SC-001**: composite scenario "User opens page → sees greeting → enters name → gets personalized greeting" — для E2E и BDD тестов
3. **ops-deploy**: deployment на cloud platform (Vercel + Fly.io / Railway)

Для каждого расширения процесс тот же: `ba-requirements` → `sa-iterate` → `pm-plan` → `dev/fe/ops` → `test` → `review`.
