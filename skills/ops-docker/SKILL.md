---
name: ops-docker
description: Docker configuration - Dockerfile, docker-compose, multi-stage builds
user_invocable: true
agent: devops-engineer
---

# /ops-docker - Docker Configuration

## What this skill does
Generates Docker configuration files with best practices: multi-stage builds, security, and optimization.

## Usage
- `/ops-docker` - Detect project type and generate Docker config
- `/ops-docker compose` - Generate/update docker-compose configuration
- `/ops-docker <service-name>` - Generate Dockerfile for a specific service

## Process

1. **Analyze project**:
   - Runtime: Node.js, Python, Go, Java, etc.
   - Package manager and lock file
   - Build output directory
   - Required system dependencies
   - Existing Docker files
2. **Ask for details** (if not provided):
   - Target environment (development, production, both)
   - Required services (database, cache, message queue, etc.)
   - Port mappings
3. **Generate Dockerfile** with:
   - Multi-stage build (build → production)
   - Non-root user
   - Minimal base image (alpine/distroless where possible)
   - Layer caching optimization (copy lock file first)
   - Health check instruction
   - `.dockerignore` file
4. **Generate docker-compose** (if applicable) with:
   - Application service
   - Database service (PostgreSQL, MongoDB, etc.)
   - Cache service (Redis, etc.)
   - Volume mounts for persistence
   - Network configuration
   - Environment variables (with `.env.example`)
5. **Present config** and suggest:
   - `/ops-pipeline` for CI/CD integration
   - `/ops-deploy` for deployment

## Best Practices Applied
- Pin base image versions
- Copy dependency manifest before source code (layer caching)
- Run as non-root user
- Use `.dockerignore` to exclude unnecessary files
- Multi-stage builds to minimize image size
- No secrets in Dockerfile (use build args or runtime env)
