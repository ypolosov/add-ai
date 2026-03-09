# Scenario Template

```markdown
# SC-NNN: {Scenario Name}

## Operational Goal
{What end-to-end objective does this scenario achieve}

## Actors & Systems
- **{Actor/System}**: {role in this scenario}

## Scenario Flow

| Step | UC Ref | Actor/System | Action | QA Checkpoints | Failure Modes |
|------|--------|-------------|--------|----------------|---------------|
| 1    | UC-NNN | {actor}     | {action} | QA-NNN: {threshold} | {failure + recovery} |
| 2    | UC-NNN | {system}    | {action} | — | {failure + recovery} |
| 3    | NEW    | {actor}     | {action} | QA-NNN: {threshold} | {failure + recovery} |

## Quality Attribute Checkpoints
- **QA-NNN**: {how this scenario exercises the QA, expected measure}
- **QA-NNN**: {another QA checkpoint}

## Cross-Cutting Concerns
- Authentication: {how auth is handled across steps}
- Logging: {what is logged}
- Monitoring: {alerts and thresholds}

## Related
- Use Cases: UC-NNN, UC-NNN, UC-NNN
- Quality Attributes: QA-NNN, QA-NNN
- ADRs: ADR-NNNN (if applicable)

## Test Mapping
- BDD: `features/SC-NNN-{name}.feature`
- E2E: `e2e/SC-NNN-{name}.spec.ts`
```

## Scenario vs Use Case

| Aspect | UC-NNN (Use Case) | SC-NNN (Scenario) |
|--------|-------------------|-------------------|
| Scope | Single interaction | End-to-end flow |
| Granularity | Atomic, reusable | Composite |
| Steps | Own actions | References to UC-NNN |
| QA | Lists related QAs | Embeds QA checkpoints with thresholds |
| Testing | Unit/Integration | BDD features + E2E tests |
