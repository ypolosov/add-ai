---
name: ops-pipeline
description: Generate CI/CD pipelines (GitHub Actions, GitLab CI, Bitbucket Pipelines, etc.)
user_invocable: true
agent: devops-engineer
---

# /ops-pipeline - CI/CD Pipeline Generation

## What this skill does
Generates CI/CD pipeline configurations adapted to the project's platform and tools.

## Usage
- `/ops-pipeline` - Detect platform and generate/update pipeline
- `/ops-pipeline <platform>` - Generate for specific platform (github, gitlab, bitbucket)

## Process

1. **Detect CI/CD platform**:
   - Check existing configs: `.github/workflows/`, `.gitlab-ci.yml`, `bitbucket-pipelines.yml`
   - Check git remote URL for platform hints
   - If none found, ask the user
2. **Analyze project**:
   - Package manager (npm, yarn, pnpm, bun)
   - Build tool (Vite, Webpack, tsc, etc.)
   - Test framework (Jest, Vitest, Playwright, etc.)
   - Linting/formatting (ESLint, Prettier, etc.)
   - Docker presence
3. **Ask for pipeline stages** (suggest defaults):
   - Install dependencies
   - Lint & format check
   - Type check
   - Unit tests
   - Integration tests
   - Build
   - Deploy (optional)
4. **Generate pipeline config** with:
   - Dependency caching
   - Parallel jobs where possible
   - Environment-specific deployments
   - Secret references (not values)
5. **Present config** and suggest:
   - `/ops-docker` for containerization
   - `/ops-deploy` for deployment config

## Platform-Specific Output

### GitHub Actions
```yaml
# .github/workflows/ci.yml
```

### GitLab CI
```yaml
# .gitlab-ci.yml
```

### Bitbucket Pipelines
```yaml
# bitbucket-pipelines.yml
```
