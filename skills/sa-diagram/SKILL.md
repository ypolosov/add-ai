---
name: sa-diagram
description: Create and update LikeC4 C4 model diagrams, dynamic views, and deployment views
user_invocable: true
agent: solution-architect
---

# /sa-diagram - Diagram Management

## What this skill does
Creates and updates C4 architecture diagrams, dynamic views (interaction/sequence flows), and deployment views (allocation structures) using LikeC4 DSL.

## Usage
- `/sa-diagram` - Interactive: show current diagrams, ask what to update
- `/sa-diagram context` - Update system context diagram
- `/sa-diagram container` - Update container diagram
- `/sa-diagram component <container>` - Update component diagram for a container
- `/sa-diagram deployment` - Update deployment diagram
- `/sa-diagram dynamic <interaction-name>` - Create LikeC4 dynamic view for an interaction flow

## Process (C4 Diagrams)

1. Read current diagram files:
   - `docs/architecture/c4/src/specification.c4` - Element/relation/deployment node kinds
   - `docs/architecture/c4/src/model.c4` - Model definition
   - `docs/architecture/c4/src/views.c4` - View definitions
   - `docs/architecture/c4/src/deployment.c4` - Deployment model

2. Ask user what to add/change:
   - New system/container/component?
   - New relationship?
   - Update existing element?

3. Apply changes following LikeC4 DSL syntax (see `reference/likec4.md`)

4. Suggest running `npx likec4 serve` to preview

## Dynamic Views (for defining interfaces — ADD Step 5)

Use when defining interfaces between elements during instantiation (Step 5) or when documenting interaction patterns. Dynamic views support two display variants: `diagram` (default) and `sequence`.

1. Ask user which interaction to document:
   - Which elements participate?
   - What is the trigger/entry point?
   - What are the key messages exchanged?

2. Generate LikeC4 dynamic view:
   ```likec4
   dynamic view userLogin {
     title 'User Login Flow'
     customer -> cloud.frontend 'enters credentials'
     cloud.frontend -> cloud.backend.api 'POST /login'
     cloud.backend.api -> auth0 'validate credentials'
     auth0 -> cloud.backend.api 'return token'
     cloud.backend.api -> cloud.db.users 'fetch user profile'
     cloud.db.users -> cloud.backend.api 'user data'
     cloud.backend.api -> cloud.frontend 'authentication response'
   }
   ```

3. Save to `docs/architecture/c4/src/views.c4` (alongside other view definitions)

4. Include in the dynamic view:
   - Element identifiers matching the C4 model
   - Step labels with parameters and return values
   - Forward (`->`) and reverse (`<-`) directions
   - Self-calls for internal processing (`api -> api 'process'`)
   - `include` for non-participating elements as context
   - References to related drivers (QA-NNN, UC-NNN) in comments

5. Reference the dynamic view in:
   - Related ITER-NN.md
   - Related ADRs
   - Element Responsibility Tables (ERTs)

## Deployment Views (for allocation structures — ADD Step 5)

Use when defining allocation structures — mapping logical elements to infrastructure (environments, zones, VMs, containers).

1. Ask user which deployment environment to document:
   - What environments exist? (prod, staging, dev)
   - What infrastructure topology? (zones, clusters, VMs)
   - Which logical elements are deployed where?

2. Ensure deployment node kinds are defined in `specification.c4`:
   ```likec4
   specification {
     deploymentNode environment
     deploymentNode zone
     deploymentNode kubernetes {
       style {
         color blue
         icon tech:kubernetes
       }
     }
     deploymentNode vm
   }
   ```

3. Generate deployment model in `docs/architecture/c4/src/deployment.c4`:
   ```likec4
   deployment {
     environment prod 'Production' {
       zone eu 'EU Region' {
         instanceOf gtPlatform.webApp
         instanceOf gtPlatform.apiGateway
       }
       db = instanceOf gtPlatform.database {
         title 'Primary DB'
         technology 'PostgreSQL with replication'
       }
     }
   }
   ```

4. Add deployment view in `docs/architecture/c4/src/views.c4`:
   ```likec4
   deployment view prodDeployment {
     title 'Production Deployment'
     include prod.**
   }
   ```

5. Reference the deployment diagram in:
   - Related ITER-NN.md
   - Related ADRs
   - Infrastructure documentation

## File Organization
- `specification.c4` - Element kinds, relationship kinds, and deployment node kinds
- `model.c4` - The actual model with elements and relationships
- `deployment.c4` - Deployment model (environments, zones, instances)
- `views.c4` - View definitions (static views, dynamic views, and deployment views)

## Guidelines
- Keep model.c4 as the single source of truth for the architecture model
- Use meaningful identifiers in camelCase (e.g., `gtPlatform`, `paymentGateway`)
- Add descriptions to all elements
- Reference ADRs in element descriptions where relevant
- Use dynamic views to define interfaces between elements (not just static structure)
- Use deployment views to map logical elements onto infrastructure nodes
