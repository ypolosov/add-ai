# QAW Scenario Template

## 6-Part Quality Attribute Scenario

```markdown
# QA-NNN: {Short Title}

## Quality Attribute
{e.g., Performance, Availability, Security, Scalability, Modifiability, Integrability}

## Scenario

| Part | Description |
|------|-------------|
| **Source** | {Who or what generates the stimulus} |
| **Stimulus** | {What condition or event occurs} |
| **Artifact** | {What part of the system is affected} |
| **Environment** | {Under what conditions (normal, peak, failure)} |
| **Response** | {What the system should do} |
| **Measure** | {Quantitative measure of the response} |

## Example

| Part | Description |
|------|-------------|
| **Source** | 10,000 concurrent users |
| **Stimulus** | Submit orders during a flash sale event |
| **Artifact** | Order Processing API |
| **Environment** | Peak load (promotional campaign) |
| **Response** | Process order and confirm |
| **Measure** | 95th percentile latency < 200ms |

## Priority
- Business Priority: {H/M/L}
- Technical Difficulty: {H/M/L}

## Notes
{Additional context, related scenarios, trade-offs}
```

## Common Quality Attribute Categories

1. **Performance** — Latency, throughput, resource utilization
2. **Availability** — Uptime, MTTR, fault tolerance
3. **Security** — Authentication, authorization, data protection
4. **Scalability** — Horizontal scaling, elastic capacity
5. **Modifiability** — Time to add features, deploy changes
6. **Integrability** — Third-party service/API integration
7. **Testability** — Test coverage, test automation
8. **Deployability** — CI/CD, rollback capability
9. **Observability** — Monitoring, logging, tracing
