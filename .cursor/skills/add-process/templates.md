# Строгие шаблоны и канонические примеры

## Схема перекрёстных ссылок

- driver → `decision_ids`, `view_refs`
- decision → `driver_id`, `view_ref`
- view → секция Links (driver_id, decision_ids)

При любой правке — синхронизировать обратные ссылки.

---

## design-backlog.yaml

**Корень:** `drivers`. Каждый драйвер — объект.

**Поля драйвера:**

| Поле | Тип | Допустимые значения |
|------|-----|---------------------|
| id | string | уникальный идентификатор |
| type | enum | use_case, qa_scenario, constraint, concern |
| title | string | краткое название |
| priority | enum | high, medium, low |
| status | enum | not_yet_addressed, partially_addressed, completely_addressed, discarded |
| decision_ids | list of string | id решений по этому драйверу |
| view_refs | list of string | пути к view-файлам, напр. views/scenario-UC1.md |

**Канонический пример:**

```yaml
drivers:
  - id: UC-1
    type: use_case
    title: Пользователь авторизуется по логину и паролю
    priority: high
    status: partially_addressed
    decision_ids: [DD-001, DD-002]
    view_refs: [views/scenario-UC1.md]
  - id: QA-1
    type: qa_scenario
    title: Время отклика главной страницы < 2 с
    priority: high
    status: not_yet_addressed
    decision_ids: []
    view_refs: []
```

---

## design-decisions.yaml

**Корень:** `decisions`. Каждая запись — объект.

**Поля решения:**

| Поле | Тип | Обязательность |
|------|-----|----------------|
| id | string | да |
| decision | string | да |
| location | string | да (элемент/вид) |
| rationale | string | да |
| assumptions | list of string | да |
| driver_id | string | опц. |
| view_ref | string | опц. (путь к view) |

**Канонический пример:**

```yaml
decisions:
  - id: DD-001
    decision: Использовать JWT для аутентификации API
    location: API Gateway
    rationale: Без состояния, масштабируемо, стандарт для мобильных клиентов.
    assumptions:
      - Токены хранятся на клиенте; refresh не чаще 1/мин.
    driver_id: UC-1
    view_ref: views/scenario-UC1.md
  - id: DD-002
    decision: Отдельный сервис Auth Service за API Gateway
    location: Auth Service
    rationale: Единая точка проверки учётных данных и выдачи токенов.
    assumptions: []
    driver_id: UC-1
    view_ref: views/scenario-UC1.md
```

---

## views/ — строгий Markdown

**Имя файла:** `view-<name>.md` или `scenario-<id>.md`.

**Порядок секций:**

1. Заголовок H1
2. Блок кода Mermaid (диаграмма)
3. Таблица Element | Responsibility (Markdown table)
4. Секция **Links** — driver_id, decision_ids (для перекрёстных ссылок)

**Канонический пример (views/scenario-UC1.md):**

Структура файла — секции по порядку:

- H1: название сценария/вида.
- Блок Mermaid (отдельная кодовая секция с языком mermaid), например flowchart LR с элементами Client, API Gateway, Auth Service, User DB.
- Таблица в формате Markdown: колонки Element, Responsibility.
- Секция **## Links** с полями driver_id и decision_ids (например driver_id: UC-1, decision_ids: DD-001, DD-002).

Пример содержимого таблицы и Links:

| Element     | Responsibility                                      |
|-------------|-----------------------------------------------------|
| API Gateway | Проверка JWT, маршрутизация на Auth Service при /auth/* |
| Auth Service| Валидация логин/пароль, выдача JWT                 |
| User DB     | Хранение учётных записей                            |

Links: driver_id: UC-1; decision_ids: DD-001, DD-002.

---

## Правило актуализации при изменении

- **Добавили решение:** в decision указать `driver_id`; в design-backlog.yaml у этого драйвера добавить id решения в `decision_ids`.
- **Привязали решение к виду:** в decision указать `view_ref`; в view в Links добавить этот decision_id; в драйвере добавить путь вида в `view_refs` (если ещё нет).
- **Создали/изменили вид:** в view заполнить Links (driver_id, decision_ids); в драйвере обновить `view_refs`; в затронутых решениях обновить `view_ref`.
- **Изменили драйвер (id/удалили):** пройти по всем decision_ids и view_refs, обновить или удалить ссылки в decisions и views.
