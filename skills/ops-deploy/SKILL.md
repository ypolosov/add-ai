---
name: ops-deploy
description: Deployment configuration - environment configs, K8s manifests, cloud deploy
user_invocable: true
agent: devops-engineer
---

# /ops-deploy - Deployment Configuration

## What this skill does
Generates deployment configurations for various platforms: Kubernetes, cloud services, or simple server deployment.

## Usage
- `/ops-deploy` - Interactive: detect deployment target and generate configs
- `/ops-deploy k8s` - Generate Kubernetes manifests
- `/ops-deploy <platform>` - Generate for specific platform (vercel, railway, fly, aws, etc.)

## Process

1. **Detect deployment context**:
   - Existing deployment configs: `k8s/`, `helm/`, `terraform/`, `vercel.json`, `fly.toml`, `railway.json`
   - Dockerfile presence
   - Framework-specific deployment (Next.js → Vercel, etc.)
   - If none found, ask the user
2. **Ask for details** (if not provided):
   - Target environments (staging, production)
   - Required resources (CPU, memory)
   - Scaling requirements (replicas, auto-scaling)
   - External dependencies (databases, APIs)
3. **Generate deployment configs**:
   - Environment-specific configuration files
   - Secret references (not values)
   - Health check endpoints
   - Resource limits and requests
   - Ingress/routing rules
4. **Present configs** and suggest:
   - `/ops-pipeline` for automated deployment
   - Secrets management setup

## Platform-Specific Output

### Kubernetes
```
k8s/
  base/
    deployment.yaml
    service.yaml
    configmap.yaml
  overlays/
    staging/
    production/
```

### Helm
```
helm/{app-name}/
  Chart.yaml
  values.yaml
  values-staging.yaml
  values-production.yaml
  templates/
```

### Cloud Platforms
- Vercel: `vercel.json`
- Fly.io: `fly.toml`
- Railway: `railway.json`
- AWS: CloudFormation/CDK templates
