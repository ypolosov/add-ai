# ADD-AI Hello World: Полный пример использования всех 9 ролей

> Пошаговый туториал использования плагина **add-ai** на примере проекта **TaskFlow** — простого Todo API с веб-интерфейсом.
> Демонстрирует все **9 ролей** и **32 скилла** в реалистичном сценарии архитектурно-управляемой разработки.

## Содержание

- [Введение](#введение)
- [Фаза 0: Navigator — оценка состояния](#фаза-0-navigator--оценка-состояния)
- [Фаза 1: Project Manager — инициализация трекинга](#фаза-1-project-manager--инициализация-трекинга)
- [Фаза 2: Business Analyst](#фаза-2-business-analyst)
- [Фаза 3: Solution Architect](#фаза-3-solution-architect)
- [Фаза 4: Project Manager — спринт-планирование](#фаза-4-project-manager--спринт-планирование)
- [Фаза 5: Backend Developer](#фаза-5-backend-developer)
- [Фаза 6: Frontend Developer](#фаза-6-frontend-developer)
- [Фаза 7: DevOps Engineer](#фаза-7-devops-engineer)
- [Фаза 8: Tester](#фаза-8-tester)
- [Фаза 9: Code Reviewer](#фаза-9-code-reviewer)
- [Бонус: Navigator — статус и возобновление](#бонус-navigator--статус-и-возобновление)
- [Сводная таблица: все 32 скилла](#сводная-таблица-все-32-скилла)

---

## Введение

### Что такое add-ai?

**add-ai** — это плагин для [Claude Code](https://claude.com/claude-code), предоставляющий 9 ролевых агентов и 32 скилла для архитектурно-управляемой разработки по методологии ADD 3.0.

Плагин помогает на всех этапах жизненного цикла проекта — от выявления требований и проектирования архитектуры до генерации кода, тестирования и код-ревью.

### Установка

```bash
# Из marketplace (рекомендуется)
claude plugin install add-ai

# Или локально из клонированного репозитория
git clone https://github.com/ypolosov/add-ai.git
claude --plugin-dir ./add-ai
```

### Проект TaskFlow

В этом туториале мы используем проект **TaskFlow** как сквозной пример:

- **Суть**: REST API для управления задачами с веб-интерфейсом
- **Стек**: NestJS + React + PostgreSQL + Docker + GitHub Actions
- **Почему этот стек**: покрывает backend, frontend, базу данных, контейнеризацию и CI/CD — все 8 ролей задействованы

### Как читать туториал

Каждая фаза описывает:
1. **Какие скиллы** вызываются и в каком порядке
2. **Пример диалога** — как выглядит реальное взаимодействие
3. **Артефакты** — что создаётся в результате

Все скиллы вызываются командой `/add-ai:<skill>` в Claude Code.

---

## Фаза 1: Business Analyst

> 5 скиллов | Роль: выявление и документирование требований

Бизнес-аналитик — отправная точка проекта. Он выявляет требования, определяет атрибуты качества и документирует use case'ы.

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:ba-requirements` | Интерактивная сессия: выявляем требования к TaskFlow | Список UC, QA, CON, CRN |
| 2 | `/add-ai:ba-qaw` | Quality Attribute Workshop: определяем QA-сценарии | `docs/requirements/qaw-results.md` |
| 3 | `/add-ai:ba-utility-tree` | Приоритизируем QA: строим дерево утилитарности | `docs/requirements/utility-tree.md` |
| 4 | `/add-ai:ba-usecase` | Документируем ключевые use case'ы | `docs/requirements/use-cases/UC-001-create-task.md` |
| 5 | `/add-ai:ba-scenario` | Сценарий: сквозной flow жизненного цикла задачи | `docs/requirements/scenarios/SC-001-task-lifecycle.md` |

### 1.1 Выявление требований (`ba-requirements`)

Начинаем с интерактивной сессии, где BA задаёт вопросы и формирует первичный список требований.

```
User: /add-ai:ba-requirements

BA: Расскажите о вашем проекте. Что он делает? Кто основные пользователи?

User: Приложение для управления задачами. Пользователи создают, редактируют,
      удаляют и завершают задачи. Нужна фильтрация и поиск.

BA: Понял. Уточню несколько моментов:
    1. Нужна ли аутентификация или приложение однопользовательское?
    2. Какие статусы задачи: только "открыта/завершена" или более сложный workflow?
    3. Есть ли требования к производительности?

User: Однопользовательское пока. Статусы: todo, in-progress, done.
      По производительности — список до 1000 задач должен грузиться < 500ms.

BA: На основе анализа выделяю следующие артефакты:

    📋 Use Cases:
    • UC-001: Create Task
    • UC-002: Update Task Status
    • UC-003: Filter Tasks by Status
    • UC-004: Search Tasks by Title
    • UC-005: Delete Task

    🎯 Quality Attributes:
    • QA-001: Response time < 500ms for list of 1000 tasks (Performance)
    • QA-002: Data persists across server restarts (Reliability)
    • QA-003: API follows REST conventions (Interoperability)

    🔒 Constraints:
    • CON-001: Single-user, no authentication required
    • CON-002: PostgreSQL as persistence layer

    ⚠️ Concerns:
    • CRN-001: Future multi-user support
    • CRN-002: Mobile-friendly UI

    Варианты:
    1) Провести QAW для детализации QA-сценариев
    2) Документировать use case'ы
    3) Перейти к архитектуре
    4) Уточнить требования
    5) Построить дерево утилитарности
```

### 1.2 Quality Attribute Workshop (`ba-qaw`)

Структурированная сессия для детальной проработки QA-сценариев.

```
User: /add-ai:ba-qaw

BA: Запускаю Quality Attribute Workshop для TaskFlow.
    Начнём с QA-001 (Performance). Опишите сценарий:
    • Источник стимула: кто/что инициирует?
    • Стимул: что происходит?
    • Окружение: в каких условиях?
    • Артефакт: что затрагивается?
    • Ответ: как система реагирует?
    • Мера ответа: как измерить?

User: Пользователь открывает список задач при нормальной нагрузке.

BA: Формализую QA-001:

    QA-001: Performance — Task List Loading
    ┌─────────────────────────────────────────────┐
    │ Source:   User                               │
    │ Stimulus: Requests task list (up to 1000)    │
    │ Environment: Normal operation                │
    │ Artifact: Task API endpoint                  │
    │ Response: Returns paginated task list         │
    │ Measure:  Response time < 500ms (p95)        │
    └─────────────────────────────────────────────┘

    Переходим к QA-002...
```

**Результат**: `docs/requirements/qaw-results.md` с 5 формализованными QA-сценариями (QA-001..QA-005).

### 1.3 Дерево утилитарности (`ba-utility-tree`)

Приоритизация QA-сценариев по важности для бизнеса и сложности реализации.

```
User: /add-ai:ba-utility-tree

BA: Строю дерево утилитарности на основе QA-001..QA-005.

    Utility Tree: TaskFlow
    ├── Performance
    │   └── QA-001: Task list < 500ms .............. (H, M)
    ├── Reliability
    │   ├── QA-002: Data persistence ............... (H, L)
    │   └── QA-004: Graceful error handling ........ (M, L)
    ├── Interoperability
    │   └── QA-003: REST conventions ............... (M, L)
    └── Modifiability
        └── QA-005: Add new task fields ............ (M, M)

    Шкала: (Business importance, Technical difficulty)
    H = High, M = Medium, L = Low

    Рекомендация: фокус на QA-001 (единственный H,M) — индексация БД
    и пагинация на этапе архитектуры.
```

**Результат**: `docs/requirements/utility-tree.md`.

### 1.4 Документирование use case'ов (`ba-usecase`)

```
User: /add-ai:ba-usecase

BA: Какой use case документируем? Доступны: UC-001..UC-005.

User: UC-001

BA: Создаю спецификацию UC-001: Create Task.
```

**Результат**: `docs/requirements/use-cases/UC-001-create-task.md` — полная спецификация с предусловиями, основным сценарием, альтернативными путями и связями с QA.

### 1.5 Scenario Workshop (`ba-scenario`)

Сквозной сценарий (SC-NNN), прослеживающий путь через всю систему как цепочку UC-NNN шагов с QA-NNN чекпоинтами.

```
User: /add-ai:ba-scenario

BA: Определим сквозной сценарий для TaskFlow.
    Какую операционную цель хотите проследить от начала до конца?

User: Полный жизненный цикл задачи: создание → работа → завершение.

BA: Scenario: SC-001 — Task Lifecycle

    | Step | UC Ref  | Actor/System | Action                              | QA Checkpoints         |
    |------|---------|-------------|--------------------------------------|------------------------|
    | 1    | UC-001  | User        | Opens TaskFlow, creates task         | —                      |
    | 2    | UC-001  | Frontend    | POST /api/tasks                      | QA-001: <200ms         |
    | 3    | UC-001  | Backend     | Validate, persist to PostgreSQL      | QA-002: no data loss   |
    | 4    | UC-001  | Backend     | Return 201 Created                   | QA-003: REST contract  |
    | 5    | UC-002  | User        | Change status: todo → in-progress    | —                      |
    | 6    | UC-002  | Frontend    | PATCH /api/tasks/:id                 | QA-001: <200ms         |
    | 7    | UC-002  | Backend     | Update status, emit event            | QA-002: no data loss   |
    | 8    | UC-003  | User        | Complete task: in-progress → done    | —                      |

    Трассировка:
    • SC-001 → features/SC-001-task-lifecycle.feature (BDD)
    • SC-001 → e2e/SC-001-task-lifecycle.spec.ts (E2E)
```

**Результат**: `docs/requirements/scenarios/SC-001-task-lifecycle.md`.

---

## Фаза 2: Solution Architect

> 7 скиллов | Роль: проектирование архитектуры по ADD 3.0

Архитектор берёт требования от BA и проектирует систему итеративно — через ADD 3.0 итерации, ADR'ы и C4 диаграммы.

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:sa-init` | Инициализируем `docs/architecture/` | Полная структура каталогов |
| 2 | `/add-ai:sa-iterate` | 1-я итерация ADD: декомпозиция на контейнеры | `ITER-01.md`, C4, ADR-0001 |
| 3 | `/add-ai:sa-adr` | ADR: выбор NestJS + гексагональная архитектура | `adrs/0001-nestjs-hexagonal.md` |
| 4 | `/add-ai:sa-diagram` | C4 диаграммы: context, container, component | `c4/src/model.c4`, `views.c4` |
| 5 | `/add-ai:sa-iterate` | 2-я итерация: детализация Task модуля | `ITER-02.md`, ADR-0002 |
| 6 | `/add-ai:sa-kanban` | Обновляем kanban: QA → Addressed | `kanban.md` |
| 7 | `/add-ai:sa-review` | Ревью архитектуры: покрытие QA, конфликты тактик | Отчёт |

### 2.1 Инициализация архитектуры (`sa-init`)

```
User: /add-ai:sa-init
```

Создаётся полная структура каталогов:

```
docs/architecture/
├── README.md              # Обзор и ссылки на все разделы
├── kanban.md              # Design kanban board
├── utility-tree.md        # Ссылка на дерево утилитарности
├── c4/                    # LikeC4 проект
│   ├── package.json
│   └── src/
│       ├── specification.c4   # Виды элементов, стили
│       ├── model.c4           # Архитектурная модель
│       ├── views.c4           # Определения видов
│       └── deployment.c4      # Модель деплоя
├── adrs/                  # Architecture Decision Records
├── drivers/               # Архитектурные драйверы
│   ├── use-cases/         # UC-NNN файлы
│   ├── quality-attributes/# QA-NNN файлы
│   ├── constraints/       # CON-NNN файлы
│   └── concerns/          # CRN-NNN файлы
├── decisions/             # Design decisions (DD-NNN)
├── iterations/            # ADD iteration logs (ITER-NN)
└── views/                 # Архитектурные виды
```

### 2.2 Первая итерация ADD (`sa-iterate`)

ADD 3.0 итерация — 7-шаговый процесс декомпозиции:

```
User: /add-ai:sa-iterate

SA: Запускаю итерацию ITER-01.

    Step 1 — Review inputs:
    Drivers: UC-001..UC-005, QA-001..QA-005, CON-001..CON-002

    Step 2 — Establish iteration goal:
    Цель: Декомпозиция TaskFlow на контейнеры (Container level).
    Фокус: QA-001 (Performance), QA-002 (Reliability).

    Step 3 — Choose element to refine:
    Refinement target: TaskFlow System (top-level)

    Step 4 — Choose design concepts:
    • Layered architecture with hexagonal core
    • SPA + REST API separation
    • Relational DB for persistence

    Step 5 — Instantiate elements:
    ┌─────────────────────────────────────────────┐
    │           TaskFlow System                    │
    │                                              │
    │  ┌──────────┐  REST  ┌──────────┐           │
    │  │ React    │──────→│ NestJS   │           │
    │  │ SPA      │       │ API      │           │
    │  └──────────┘       └────┬─────┘           │
    │                          │ SQL              │
    │                     ┌────▼─────┐           │
    │                     │PostgreSQL│           │
    │                     │ DB       │           │
    │                     └──────────┘           │
    └─────────────────────────────────────────────┘

    Step 6 — Sketch views:
    → Создаю C4 container diagram

    Step 7 — Review:
    QA-001: Partially addressed (need pagination design)
    QA-002: Addressed (PostgreSQL persistence)
    QA-003: Addressed (REST API)

    Варианты:
    1) Создать ADR для выбора NestJS
    2) Запустить следующую итерацию (component level)
    3) Обновить C4 диаграммы
    4) Обновить kanban
```

**Результат**: `docs/architecture/iterations/ITER-01.md`.

### 2.3 Architecture Decision Record (`sa-adr`)

```
User: /add-ai:sa-adr

SA: Какое архитектурное решение документируем?

User: Выбор NestJS с гексагональной архитектурой для Backend API.

SA: Создаю ADR-0001 в формате MADR v3.
```

**Результат**: `docs/architecture/adrs/0001-nestjs-hexagonal.md` — полный ADR с контекстом, рассмотренными альтернативами (Express, Fastify), обоснованием выбора и связями с QA-001, QA-005.

### 2.4 C4 диаграммы (`sa-diagram`)

```
User: /add-ai:sa-diagram

SA: Какой уровень диаграммы создать или обновить?

User: Container diagram для TaskFlow.

SA: Обновляю docs/architecture/c4/src/model.c4 и views.c4.
```

Пример сгенерированной LikeC4 модели:

```likec4
// model.c4
model {
  user = person "User" {
    description "Пользователь TaskFlow"
  }

  taskflow = softwareSystem "TaskFlow" {
    description "Task management application"

    spa = container "Web SPA" {
      description "Single-page application"
      technology "React, TypeScript"
    }

    api = container "Backend API" {
      description "REST API server"
      technology "NestJS, TypeScript"
    }

    db = database "Database" {
      description "Task persistence"
      technology "PostgreSQL"
    }
  }

  user -> taskflow.spa "Uses" { style sync }
  taskflow.spa -> taskflow.api "REST API calls" { style sync }
  taskflow.api -> taskflow.db "Reads/Writes" { style sync }
}
```

```bash
# Запуск LikeC4 dev server
cd docs/architecture/c4 && npx likec4 serve
```

### 2.5 Вторая итерация (`sa-iterate`)

```
User: /add-ai:sa-iterate

SA: Запускаю итерацию ITER-02.
    Цель: детализация Backend API до component level.
    Фокус: QA-001 (пагинация), QA-005 (модифицируемость).

    Результат декомпозиции:
    Backend API →
    ├── Task Module (domain + application + infrastructure)
    ├── Health Module
    └── Shared (pagination, error handling)

    Архитектурные решения:
    → ADR-0002: Repository pattern для абстракции persistence
    → DD-001: Pagination strategy (cursor-based)
```

### 2.6 Design Kanban (`sa-kanban`)

```
User: /add-ai:sa-kanban

SA: Обновляю kanban доску.

    Design Kanban Board
    ┌──────────────┬──────────────────┬───────────────────┐
    │ Not Addressed│ Partially Addr.  │ Completely Addr.  │
    ├──────────────┼──────────────────┼───────────────────┤
    │              │ QA-001 Perf      │ QA-002 Reliability│
    │              │ QA-005 Modif     │ QA-003 Interop    │
    │              │                  │ QA-004 Error hand.│
    └──────────────┴──────────────────┴───────────────────┘

    QA-001: pagination designed (ITER-02), index needed → Partially
    QA-005: hexagonal + repository pattern → Partially
```

### 2.7 Ревью архитектуры (`sa-review`)

```
User: /add-ai:sa-review

SA: Провожу ревью архитектуры TaskFlow.

    ✅ Strengths:
    • Clear separation: SPA / API / DB
    • Hexagonal architecture supports QA-005 (modifiability)
    • Repository pattern enables testing and DB switching

    ⚠️ Risks:
    • QA-001: No caching strategy — may need Redis for large lists
    • QA-005: No event bus — adding async features later will be harder

    📊 QA Coverage: 3/5 fully addressed, 2/5 partially

    Рекомендации:
    1) Добавить DB индексы для QA-001 в ITER-03
    2) Рассмотреть in-memory cache для hot data
    3) Задокументировать решение о событийной модели в ADR-0003
```

---

## Фаза 3: Project Manager

> 3 скилла | Роль: планирование и трекинг задач

PM переводит архитектурные решения в рабочие задачи. Работает с GitHub, GitLab и Bitbucket (определяет платформу автоматически).

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:pm-plan` | Спринт-планирование: ADR → epic → stories → tasks | Epic + issues |
| 2 | `/add-ai:pm-issue` | Создаём конкретный issue для Task CRUD | Issue с лейблами |
| 3 | `/add-ai:pm-status` | Статус-отчёт: прогресс, блокеры, следующие шаги | Отчёт в консоли |

### 3.1 Спринт-планирование (`pm-plan`)

```
User: /add-ai:pm-plan

PM: Анализирую архитектурные артефакты...
    Обнаружены: 5 UC, 5 QA, 2 ADR, 2 ITER.

    Предлагаю структуру спринта:

    Epic: TaskFlow MVP
    ├── Story: Task CRUD API (role:dev, priority:high)
    │   ├── Task: Scaffold task module
    │   ├── Task: Implement create/read/update/delete
    │   └── Task: Add validation and error handling
    ├── Story: Task Web UI (role:fe, priority:high)
    │   ├── Task: Scaffold pages and routes
    │   ├── Task: Create TaskCard component
    │   └── Task: Integrate API layer
    ├── Story: Infrastructure (role:ops, priority:medium)
    │   ├── Task: Docker configuration
    │   └── Task: CI/CD pipeline
    └── Story: Testing (role:test, priority:high)
        ├── Task: Unit tests for domain
        └── Task: E2E tests for user flows

    Создать issues в GitHub?
    1) Да, все сразу
    2) Только Epic + Stories
    3) Скорректировать план
```

### 3.2 Управление issues (`pm-issue`)

```
User: /add-ai:pm-issue

PM: Что нужно сделать?

User: Создай story для Task CRUD API.

PM: Создаю issue в GitHub...

    ✅ Created: #1 "Task CRUD API"
    Labels: type:story, role:dev, priority:high
    Body:
      ## Description
      Implement CRUD operations for Task entity.
      Related: UC-001, UC-002, UC-005, ADR-0001

      ## Acceptance Criteria
      - [ ] POST /api/tasks creates a task
      - [ ] GET /api/tasks returns paginated list
      - [ ] GET /api/tasks/:id returns single task
      - [ ] PATCH /api/tasks/:id updates task
      - [ ] DELETE /api/tasks/:id deletes task
      - [ ] Input validation with error messages
```

### 3.3 Статус-отчёт (`pm-status`)

```
User: /add-ai:pm-status

PM: 📊 TaskFlow Status Report

    Sprint: MVP (Week 1)

    Progress:
    ████████░░░░░░░░ 30%

    By Status:
    • Done:        3/12 issues
    • In Progress: 2/12 issues
    • Backlog:     7/12 issues

    By Role:
    • dev:  2/5 done
    • fe:   0/3 done
    • ops:  1/2 done
    • test: 0/2 done

    🚧 Blockers:
    • None

    📌 Next Steps:
    1. Complete Task CRUD implementation (#1)
    2. Start frontend scaffold (#4)
    3. Set up CI pipeline (#8)
```

---

## Фаза 4: Backend Developer

> 2 скилла | Роль: реализация серверной части

Backend-разработчик создаёт модули с гексагональной архитектурой. Адаптируется к фреймворку проекта (NestJS, Express, Fastify и др.).

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:dev-scaffold` | Scaffold модуля Task с гексагональной архитектурой | Структура модуля |
| 2 | `/add-ai:dev-implement` | Реализация UC-001: создание задачи | Рабочий код |

### 4.1 Scaffold модуля (`dev-scaffold`)

```
User: /add-ai:dev-scaffold

Dev: Какой модуль создать? Обнаружен NestJS проект.

User: Task module согласно ADR-0001.

Dev: Создаю модуль с гексагональной структурой...
```

Результат:

```
src/
├── core/
│   ├── domain/
│   │   ├── entities/task.entity.ts
│   │   ├── value-objects/task-status.vo.ts
│   │   └── domain-events/task-created.event.ts
│   └── application/
│       ├── ports/
│       │   ├── inbound/create-task.port.ts
│       │   └── outbound/task-repository.port.ts
│       └── services/create-task.service.ts
├── infrastructure/
│   └── persistence/task.repository.ts
├── interfaces/
│   ├── http/task.controller.ts
│   └── dto/create-task.dto.ts
└── modules/task.module.ts
```

Каждый слой изолирован: domain не зависит ни от чего, application зависит только от domain, infrastructure реализует порты.

### 4.2 Реализация фичи (`dev-implement`)

```
User: /add-ai:dev-implement

Dev: Какой use case реализовать?

User: UC-001: Create Task.

Dev: Реализую по слоям: domain → application → infrastructure → interfaces.
```

Пример сгенерированного кода:

```typescript
// core/domain/entities/task.entity.ts
export class Task {
  constructor(
    public readonly id: string,
    public title: string,
    public description: string,
    public status: TaskStatus,
    public readonly createdAt: Date,
    public updatedAt: Date,
  ) {}

  static create(title: string, description: string): Task {
    return new Task(
      randomUUID(),
      title,
      description,
      TaskStatus.TODO,
      new Date(),
      new Date(),
    );
  }
}

// core/application/services/create-task.service.ts
@Injectable()
export class CreateTaskService implements CreateTaskPort {
  constructor(
    @Inject(TASK_REPOSITORY) private readonly taskRepo: TaskRepositoryPort,
  ) {}

  async execute(command: CreateTaskCommand): Promise<Task> {
    const task = Task.create(command.title, command.description);
    return this.taskRepo.save(task);
  }
}
```

---

## Фаза 5: Frontend Developer

> 3 скилла | Роль: реализация клиентской части

Frontend-разработчик создаёт страницы, компоненты и API-слой. Адаптируется к фреймворку (React, Vue, Angular, Svelte и др.).

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:fe-scaffold` | Scaffold страниц: TaskList, TaskDetail | Страницы, роуты, layouts |
| 2 | `/add-ai:fe-component` | Компонент TaskCard с типизацией и a11y | `TaskCard.tsx` + тест |
| 3 | `/add-ai:fe-api` | Типизированный API слой (TanStack Query + axios) | `api/tasks.ts`, `hooks/useTasks.ts` |

### 5.1 Scaffold страниц (`fe-scaffold`)

```
User: /add-ai:fe-scaffold

FE: Обнаружен React + React Router проект.
    Какие страницы создать?

User: TaskList (главная) и TaskDetail (просмотр/редактирование).

FE: Создаю scaffold...
```

Результат:

```
src/
├── pages/
│   ├── TaskListPage/
│   │   ├── TaskListPage.tsx
│   │   └── index.ts
│   └── TaskDetailPage/
│       ├── TaskDetailPage.tsx
│       └── index.ts
├── layouts/
│   └── MainLayout.tsx
└── routes.tsx           # Updated with new routes
```

### 5.2 UI компонент (`fe-component`)

```
User: /add-ai:fe-component

FE: Какой компонент создать?

User: TaskCard — карточка задачи с кнопками Complete и Delete.
```

Результат:

```tsx
// components/TaskCard/TaskCard.tsx
interface TaskCardProps {
  task: Task;
  onComplete: (id: string) => void;
  onDelete: (id: string) => void;
}

export const TaskCard: React.FC<TaskCardProps> = ({
  task,
  onComplete,
  onDelete,
}) => (
  <article role="article" aria-label={`Task: ${task.title}`}>
    <h3>{task.title}</h3>
    <p>{task.description}</p>
    <span className="badge" data-status={task.status}>
      {task.status}
    </span>
    <div role="group" aria-label="Task actions">
      <button
        onClick={() => onComplete(task.id)}
        aria-label="Complete task"
        disabled={task.status === 'done'}
      >
        Complete
      </button>
      <button
        onClick={() => onDelete(task.id)}
        aria-label="Delete task"
      >
        Delete
      </button>
    </div>
  </article>
);
```

### 5.3 Типизированный API слой (`fe-api`)

```
User: /add-ai:fe-api

FE: Обнаружен axios + TanStack Query. Для какой сущности создать API?

User: Tasks — все CRUD операции.
```

Результат:

```typescript
// api/tasks.ts
const TASKS_URL = '/api/tasks';

export const tasksApi = {
  getAll: (params?: TaskFilterParams) =>
    axios.get<PaginatedResponse<Task>>(TASKS_URL, { params }),
  getById: (id: string) =>
    axios.get<Task>(`${TASKS_URL}/${id}`),
  create: (data: CreateTaskDto) =>
    axios.post<Task>(TASKS_URL, data),
  update: (id: string, data: UpdateTaskDto) =>
    axios.patch<Task>(`${TASKS_URL}/${id}`, data),
  delete: (id: string) =>
    axios.delete(`${TASKS_URL}/${id}`),
};

// hooks/useTasks.ts
export function useTasks(params?: TaskFilterParams) {
  return useQuery({
    queryKey: ['tasks', params],
    queryFn: () => tasksApi.getAll(params).then(r => r.data),
  });
}

export function useCreateTask() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: tasksApi.create,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['tasks'] }),
  });
}
```

---

## Фаза 6: DevOps Engineer

> 3 скилла | Роль: инфраструктура и CI/CD

DevOps инженер настраивает контейнеризацию, CI/CD пайплайн и конфигурацию деплоя. Адаптируется к платформе (GitHub Actions, GitLab CI, Bitbucket Pipelines).

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:ops-docker` | Multi-stage Dockerfile + docker-compose | `Dockerfile`, `docker-compose.yml` |
| 2 | `/add-ai:ops-pipeline` | GitHub Actions: lint → test → build → deploy | `.github/workflows/ci.yml` |
| 3 | `/add-ai:ops-deploy` | Конфигурация деплоя | `deploy/` с манифестами |

### 6.1 Docker конфигурация (`ops-docker`)

```
User: /add-ai:ops-docker

Ops: Обнаружен NestJS проект. Создаю Docker конфигурацию...
```

Результат:

```dockerfile
# Dockerfile — Multi-stage build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
RUN addgroup -g 1001 -S app && adduser -S app -u 1001
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER app
HEALTHCHECK CMD wget -qO- http://localhost:3000/health || exit 1
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://taskflow:secret@db:5432/taskflow
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: taskflow
      POSTGRES_USER: taskflow
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U taskflow"]
      interval: 5s
      timeout: 3s
      retries: 5

volumes:
  pgdata:
```

### 6.2 CI/CD Pipeline (`ops-pipeline`)

```
User: /add-ai:ops-pipeline

Ops: Обнаружен GitHub. Создаю GitHub Actions pipeline...
```

Результат: `.github/workflows/ci.yml` с этапами:

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npm run lint

  test:
    needs: lint
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: taskflow_test
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready
          --health-interval 5s
          --health-timeout 3s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npm test
      - run: npm run test:e2e

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with:
          push: false
          tags: taskflow:${{ github.sha }}
```

### 6.3 Конфигурация деплоя (`ops-deploy`)

```
User: /add-ai:ops-deploy

Ops: Куда планируете деплоить?

User: Kubernetes.

Ops: Создаю K8s манифесты в deploy/...
```

Результат:

```
deploy/
├── namespace.yml
├── deployment.yml       # API deployment + readiness/liveness probes
├── service.yml          # ClusterIP service
├── ingress.yml          # Ingress with TLS
├── configmap.yml        # Non-secret config
├── secret.yml           # DB credentials (template)
└── postgres/
    ├── statefulset.yml  # PostgreSQL StatefulSet
    └── service.yml      # PostgreSQL service
```

---

## Фаза 7: Tester

> 4 скилла | Роль: тестирование на всех уровнях

Тестировщик создаёт тесты от юнитов до BDD-сценариев. Адаптируется к тестовому фреймворку проекта (Jest, Vitest, Mocha, Playwright, Cypress и др.).

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:test-unit` | Юнит-тесты: Task entity, CreateTaskService | `*.spec.ts` файлы |
| 2 | `/add-ai:test-integration` | Интеграционные тесты API (supertest + тестовая БД) | `test/integration/*.spec.ts` |
| 3 | `/add-ai:test-e2e` | E2E тесты из UC-001 (Playwright) | `e2e/tasks.spec.ts` |
| 4 | `/add-ai:test-bdd` | BDD сценарии (Gherkin + step definitions) | `features/*.feature` |

### 7.1 Юнит-тесты (`test-unit`)

```
User: /add-ai:test-unit

Test: Что тестируем?

User: Task entity и CreateTaskService.

Test: Создаю юнит-тесты с Jest (обнаружен в проекте)...
```

Результат:

```typescript
// core/domain/entities/task.entity.spec.ts
describe('Task', () => {
  describe('create', () => {
    it('should create task with TODO status', () => {
      const task = Task.create('Buy groceries', 'Milk, eggs, bread');

      expect(task.title).toBe('Buy groceries');
      expect(task.description).toBe('Milk, eggs, bread');
      expect(task.status).toBe(TaskStatus.TODO);
      expect(task.id).toBeDefined();
      expect(task.createdAt).toBeInstanceOf(Date);
    });
  });
});

// core/application/services/create-task.service.spec.ts
describe('CreateTaskService', () => {
  let service: CreateTaskService;
  let mockRepo: jest.Mocked<TaskRepositoryPort>;

  beforeEach(() => {
    mockRepo = { save: jest.fn(), findById: jest.fn(), findAll: jest.fn() };
    service = new CreateTaskService(mockRepo);
  });

  it('should create and persist a task', async () => {
    mockRepo.save.mockImplementation(async (task) => task);

    const result = await service.execute({
      title: 'Test task',
      description: 'Description',
    });

    expect(result.title).toBe('Test task');
    expect(result.status).toBe(TaskStatus.TODO);
    expect(mockRepo.save).toHaveBeenCalledTimes(1);
  });
});
```

### 7.2 Интеграционные тесты (`test-integration`)

```
User: /add-ai:test-integration

Test: Какой API эндпоинт тестируем?

User: Task CRUD — все эндпоинты.

Test: Создаю интеграционные тесты с supertest и тестовой БД...
```

Результат:

```typescript
// test/integration/task.e2e-spec.ts
describe('Task API (integration)', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const module = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = module.createNestApplication();
    await app.init();
  });

  afterAll(() => app.close());

  describe('POST /api/tasks', () => {
    it('should create a task and return 201', () => {
      return request(app.getHttpServer())
        .post('/api/tasks')
        .send({ title: 'Test', description: 'Integration test' })
        .expect(201)
        .expect((res) => {
          expect(res.body.id).toBeDefined();
          expect(res.body.status).toBe('todo');
        });
    });

    it('should return 400 for empty title', () => {
      return request(app.getHttpServer())
        .post('/api/tasks')
        .send({ title: '', description: '' })
        .expect(400);
    });
  });
});
```

### 7.3 E2E тесты (`test-e2e`)

```
User: /add-ai:test-e2e

Test: Какой use case покрываем E2E тестами?

User: UC-001: Create Task — через UI.

Test: Создаю E2E тесты с Playwright и Page Object Model...
```

Результат:

```typescript
// e2e/pages/TaskPage.ts
export class TaskPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/');
  }

  async createTask(title: string, description: string) {
    await this.page.getByRole('button', { name: 'New Task' }).click();
    await this.page.getByLabel('Title').fill(title);
    await this.page.getByLabel('Description').fill(description);
    await this.page.getByRole('button', { name: 'Save' }).click();
  }

  async getTaskTitles(): Promise<string[]> {
    return this.page.getByRole('article').getByRole('heading').allTextContents();
  }
}

// e2e/tasks.spec.ts
test.describe('Task Management', () => {
  test('should create a new task', async ({ page }) => {
    const taskPage = new TaskPage(page);
    await taskPage.goto();
    await taskPage.createTask('Buy groceries', 'Milk, eggs, bread');

    const titles = await taskPage.getTaskTitles();
    expect(titles).toContain('Buy groceries');
  });
});
```

### 7.4 BDD сценарии (`test-bdd`)

```
User: /add-ai:test-bdd

Test: Для какой функциональности создать BDD сценарии?

User: Task management — создание, завершение, удаление.
```

Результат:

```gherkin
# features/task-management.feature
Feature: Task Management
  As a user
  I want to manage my tasks
  So that I can track my work

  Scenario: Create a new task
    Given I am on the task list page
    When I click "New Task"
    And I fill in "Title" with "Buy groceries"
    And I fill in "Description" with "Milk, eggs, bread"
    And I click "Save"
    Then I should see "Buy groceries" in the task list
    And the task status should be "todo"

  Scenario: Complete a task
    Given a task "Buy groceries" exists with status "todo"
    When I click "Complete" on "Buy groceries"
    Then the task "Buy groceries" should have status "done"

  Scenario: Delete a task
    Given a task "Buy groceries" exists
    When I click "Delete" on "Buy groceries"
    And I confirm the deletion
    Then I should not see "Buy groceries" in the task list
```

---

## Фаза 8: Code Reviewer

> 3 скилла | Роль: ревью кода и стандартов (read-only)

Code Reviewer анализирует код, но никогда не изменяет его — только читает и выдаёт отчёты.

| # | Команда | Что делаем | Артефакт |
|---|---------|-----------|----------|
| 1 | `/add-ai:review-code` | Ревью незакоммиченных изменений vs ADR | Отчёт с issues |
| 2 | `/add-ai:review-standards` | Аудит структуры проекта и направления зависимостей | Отчёт с нарушениями |
| 3 | `/add-ai:review-pr` | Ревью Pull Request по чеклисту | Approve / Request Changes |

### 8.1 Ревью кода (`review-code`)

```
User: /add-ai:review-code

Reviewer: Анализирую незакоммиченные изменения...

    📝 Code Review Report

    🔴 Critical (1):
    • task.controller.ts:23 — Direct database access from controller
      bypasses application layer (violates ADR-0001: hexagonal arch)

    🟡 Warning (2):
    • create-task.dto.ts:5 — Missing validation decorators
      (@IsString, @IsNotEmpty) for title field
    • task.repository.ts:18 — Raw SQL query without parameterization
      (potential SQL injection)

    🔵 Info (1):
    • task.entity.ts:12 — Consider adding updatedAt auto-update
      in status change method

    Summary: 1 critical, 2 warnings, 1 info
    Recommendation: Fix critical issue before committing.
```

### 8.2 Аудит стандартов (`review-standards`)

```
User: /add-ai:review-standards

Reviewer: Аудит проекта по ADR-0001 и conventions...

    📋 Standards Audit Report

    ✅ Passing (4):
    • Hexagonal structure: domain → application → infrastructure ✓
    • DTOs separate from domain entities ✓
    • Repository pattern with ports ✓
    • Conventional commits in git log ✓

    ❌ Violations (2):
    • NAMING: TaskRepository class should be TaskTypeOrmRepository
      (implementation should indicate adapter type)
    • DEPENDENCY: infrastructure/persistence imports from interfaces/dto
      (should only import from core/)

    ⚠️ Suggestions (1):
    • Add index.ts barrel exports for each layer
```

### 8.3 Ревью Pull Request (`review-pr`)

```
User: /add-ai:review-pr

Reviewer: Номер PR?

User: #5

Reviewer: Загружаю PR #5 из GitHub...

    📝 PR Review: "Add Task CRUD API" (#5)

    Checklist:
    ✅ PR title follows convention
    ✅ References issue (#1)
    ✅ Tests included (12 tests, all passing)
    ❌ Missing: migration file for new table
    ⚠️ create-task.dto.ts: add @ApiProperty for Swagger docs

    Verdict: Request Changes
    Reason: Missing database migration will break deployment.
```

---

## Бонус: Navigator — статус и возобновление

Скилл `nav-resume` (Navigator) сканирует все артефакты всех ролей и определяет текущую SDLC-фазу:

```
User: /add-ai:nav-resume

Navigator: Сканирую артефакты проекта...

    Текущее состояние TaskFlow:
    ─────────────────────────────
    SDLC Phase: Development

    Requirements:
    • Use cases: 5 (UC-001..UC-005)
    • Scenarios: 1 (SC-001 task lifecycle)
    • QA scenarios: 5 (3 addressed, 2 partially)
    • Constraints: 2, Concerns: 2

    Architecture:
    • ADRs: 3 (all accepted)
    • Iterations: 2 completed
    • C4 diagrams: context, container, component

    Issues by Phase:
    • phase:requirements: 5/5 done
    • phase:architecture: 3/3 done
    • phase:development: 4/8 in progress
    • phase:testing: 0/4 not started

    Traceability Gaps:
    • SC-001 has no BDD feature file yet
    • QA-004 has no ADR

    Рекомендуемые следующие шаги:
    1) Завершить реализацию UC-003 (фильтрация задач)
    2) Создать BDD feature из SC-001 (/add-ai:test-bdd SC-001)
    3) Интегрировать API слой на фронтенде (/add-ai:fe-api)
    4) Провести sa-review для оценки покрытия QA-004
    5) Посмотреть полный статус (/add-ai:nav-status)
```

Для детального мета-статуса используйте `nav-status`:

```
User: /add-ai:nav-status

Navigator: Unified Project Status — 2026-03-09

    Progress: 65% (drivers: 3/5 addressed, issues: 8/12 closed)
    Design Kanban: 0 Not | 2 Partially | 3 Completely | 2 Implemented | 0 Verified
    Traceability: 1 gap (SC-001 → no BDD feature)
    Blockers: none

    Рекомендации:
    1) Закрыть оставшиеся dev issues
    2) Генерировать тесты из SC-001
    3) Запланировать review фазу
```

---

## Сводная таблица: все 32 скилла

| # | Роль | Скилл | Фаза | Что делает |
|---|------|-------|------|-----------|
| 1 | Nav | `nav-resume` | * | Возобновление сессии (сканирование всех артефактов) |
| 2 | Nav | `nav-status` | * | Мета-статус проекта (kanban + issues + traceability) |
| 3 | BA | `ba-requirements` | 2 | Выявление требований (интерактивная сессия) |
| 4 | BA | `ba-qaw` | 2 | Quality Attribute Workshop |
| 5 | BA | `ba-utility-tree` | 2 | Дерево утилитарности (приоритизация QA) |
| 6 | BA | `ba-usecase` | 2 | Документирование use case'ов (UC-NNN) |
| 7 | BA | `ba-scenario` | 2 | Scenario Workshop (SC-NNN из UC + QA) |
| 8 | SA | `sa-init` | 3 | Инициализация `docs/architecture/` |
| 9 | SA | `sa-iterate` | 3 | Итерация ADD 3.0 (7-step process) |
| 10 | SA | `sa-adr` | 3 | Architecture Decision Record (MADR v3) |
| 11 | SA | `sa-diagram` | 3 | C4 диаграммы (LikeC4 DSL) |
| 12 | SA | `sa-kanban` | 3 | Design kanban board |
| 13 | SA | `sa-review` | 3 | Ревью архитектуры vs QA |
| 14 | PM | `pm-init` | 1 | Инициализация трекинга (labels, milestone, stories) |
| 15 | PM | `pm-plan` | 4 | Спринт-планирование (ADR → issues) |
| 16 | PM | `pm-issue` | * | Управление issues (GitHub/GitLab/Bitbucket) |
| 17 | PM | `pm-status` | * | Статус-отчёт проекта |
| 18 | Dev | `dev-scaffold` | 5 | Scaffold бэкенд-модуля (hexagonal) |
| 19 | Dev | `dev-implement` | 5 | Реализация use case'а (+ TDD mode) |
| 20 | FE | `fe-scaffold` | 5 | Scaffold страниц и роутов |
| 21 | FE | `fe-component` | 5 | UI компонент (typed props, a11y, + TDD mode) |
| 22 | FE | `fe-api` | 5 | Типизированный API слой (+ TDD mode) |
| 23 | Ops | `ops-docker` | 5 | Docker конфигурация (multi-stage) |
| 24 | Ops | `ops-pipeline` | 5 | CI/CD pipeline (platform-adaptive) |
| 25 | Ops | `ops-deploy` | 5 | Конфигурация деплоя (K8s, Fly.io и др.) |
| 26 | Test | `test-unit` | 6 | Юнит-тесты (domain, services) |
| 27 | Test | `test-integration` | 6 | Интеграционные тесты (API + DB) |
| 28 | Test | `test-e2e` | 6 | E2E тесты из SC-NNN (Playwright, Page Objects) |
| 29 | Test | `test-bdd` | 6 | BDD сценарии из SC-NNN (Gherkin + steps) |
| 30 | Review | `review-code` | 7 | Ревью кода vs ADR и паттерны |
| 31 | Review | `review-standards` | 7 | Аудит стандартов проекта |
| 32 | Review | `review-pr` | 7 | Ревью Pull Request |

---

## Workflow: как фазы связаны между собой

```
  Фаза 1           Фаза 2            Фаза 3
┌──────────┐    ┌──────────────┐    ┌────────────┐
│    BA    │───→│     SA       │───→│     PM     │
│ требова- │    │ архитектура  │    │ planning & │
│ ния      │    │ ADD 3.0      │    │ tracking   │
└──────────┘    └──────────────┘    └─────┬──────┘
                                          │
              ┌───────────────────────────┬┴──────────────────┐
              ▼                           ▼                    ▼
        Фаза 4                      Фаза 5              Фаза 6
    ┌──────────────┐           ┌──────────────┐    ┌──────────────┐
    │  Backend Dev │           │ Frontend Dev │    │    DevOps    │
    │  scaffold +  │           │  scaffold +  │    │  docker +   │
    │  implement   │           │  components  │    │  CI/CD      │
    └──────┬───────┘           └──────┬───────┘    └──────┬───────┘
           │                          │                    │
           └──────────────┬───────────┘                    │
                          ▼                                │
                    Фаза 7                                 │
               ┌──────────────┐                            │
               │   Tester     │                            │
               │ unit → integ │                            │
               │ → e2e → bdd  │                            │
               └──────┬───────┘                            │
                      │                                    │
                      ▼                                    │
                Фаза 8                                     │
           ┌──────────────┐                                │
           │Code Reviewer │◄───────────────────────────────┘
           │ code, stds,  │
           │ PR review    │
           └──────────────┘
```

> **Примечание**: Dev/FE/Ops фазы могут выполняться параллельно. Тесты могут начинаться одновременно с реализацией (TDD mode в `dev-implement`/`fe-component`/`fe-api`). Скиллы `nav-resume` и `nav-status` можно вызвать на любом этапе.
