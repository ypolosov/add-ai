# LikeC4 Conventions

## File Structure
- `specification.c4` - Element kinds, relationship kinds, deployment node kinds, styles
- `model.c4` - Architecture model (elements, relationships)
- `deployment.c4` - Deployment model (environments, zones, instances)
- `views.c4` - View definitions (static, dynamic, deployment views)

## Naming
- Element identifiers: camelCase (e.g., `gtPlatform`, `paymentService`)
- Element titles: human-readable with spaces (e.g., "GT Platform", "Payment Service")
- All elements must have a `description`
- Technology should be specified where applicable

## Element Hierarchy
```
person → (external actors)
softwareSystem → container → component
database, queue → (specialized containers)
```

## Relationships
- Always specify direction: `source -> target "label"`
- Use relationship kinds: `sync`, `async`
- Keep labels concise: "Reads/Writes", "Publishes events", "Authenticates"

## Views
- One view per level of abstraction minimum
- System context view is mandatory
- Container view for each software system
- Component views only for complex containers

## Dynamic Views
- Use `dynamic view` for interaction/sequence flows between elements
- Two display variants: `diagram` (default) and `sequence`
- Element identifiers must match model elements
- Supports: forward (`->`), reverse (`<-`), self-calls (`api -> api`)
- Continuous steps: chain with `->` for sequential flows
- Use `include` for non-participating elements as context

## Deployment Model & Views
- Define `deploymentNode` kinds in specification (environment, zone, kubernetes, vm)
- Use `deployment {}` block for deployment model (separate from logical `model {}`)
- `instanceOf` deploys logical elements onto deployment nodes
- Instances inherit properties from logical model, can override title/technology/style
- Deployment relationships: `vm2.db -> vm1.db 'replicates'`
- Deployment views: `deployment view` with `include prod.**` predicates
- Store deployment model in `deployment.c4`, views in `views.c4`

## Commands
```bash
npx likec4 serve          # Start dev server with hot reload
npx likec4 build          # Build static site
npx likec4 export png     # Export views as PNG
```
