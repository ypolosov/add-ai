# ADD 3.0 Design Concepts Reference

## Reference Architectures

### Application Types
- **Web/API Application** — 3-tier: presentation, business logic, data access
- **Mobile Application** — thin client + API backend, offline-first considerations
- **Rich Client** — desktop app with local storage and server sync
- **Service-Oriented / Event-Driven** — distributed services with message bus
- **Data-Intensive** — ETL pipelines, data lakes, analytics platforms
- **Embedded / Real-Time** — constrained resources, timing guarantees

### Deployment Patterns
- **Single Node** — all components on one server
- **Load-Balanced Cluster** — N replicas behind load balancer
- **Primary-Secondary** — one primary, N secondaries for reads/failover
- **Active-Active** — all nodes handle traffic, shared state
- **Blue/Green** — two identical environments, traffic switch
- **Canary** — gradual rollout to subset of users

## Architecture Patterns

### Structural Patterns
- **Layered** - Separation into presentation, business, data layers
- **Hexagonal (Ports & Adapters)** - Core domain isolated from infrastructure
- **Modular Monolith** - Modules with clear boundaries, deployable as one unit
- **Microservices** - Independent deployable services
- **CQRS** - Separate read and write models
- **Event Sourcing** - Store state changes as sequence of events

### Communication Patterns
- **Request/Response** - Synchronous HTTP/gRPC calls
- **Event-Driven** - Async communication via events/messages
- **Saga** - Distributed transaction management
- **API Gateway** - Single entry point for clients
- **BFF (Backend for Frontend)** - Dedicated backend per frontend type

### Data Patterns
- **Database per Service** - Each service owns its data
- **Shared Database** - Single database, multiple services
- **CQRS** - Separate read/write stores
- **Event Store** - Append-only event log

## Availability Tactics
- **Detect**: Heartbeat, Ping/Echo, Monitor, Timestamp, Voting
- **Recover**: Active Redundancy, Passive Redundancy, Spare, Rollback, Retry, Ignore, Degradation, Reconfiguration
- **Prevent**: Removal from Service, Transactions, Predictive Model

## Performance Tactics
- **Control Resource Demand**: Manage Work Requests, Limit Event Response, Prioritize Events, Reduce Overhead, Bound Execution Times, Increase Resource Efficiency
- **Manage Resources**: Increase Resources, Introduce Concurrency, Maintain Multiple Copies, Schedule Resources

## Security Tactics
- **Detect**: Detect Intrusion, Detect Service Denial, Verify Message Integrity, Detect Message Delay
- **Resist**: Authenticate Actors, Authorize Actors, Maintain Data Confidentiality, Maintain Integrity, Limit Exposure, Encrypt Data
- **React**: Revoke Access, Lock Computer, Inform Actors
- **Recover**: Audit Trail, Restore

## Modifiability Tactics
- **Reduce Size of Module**: Split Module, Increase Cohesion
- **Increase Cohesion**: Encapsulate, Use Intermediary, Restrict Dependencies, Abstract Common Services
- **Defer Binding**: Runtime Registration, Configuration Files, Polymorphism, Component Replacement, Adherence to Protocols

## Scalability Tactics
- **Horizontal Scaling**: Load Balancer, Stateless Services, Sharding
- **Vertical Scaling**: Resource Upgrade
- **Caching**: In-Memory Cache, Distributed Cache, CDN
- **Async Processing**: Message Queue, Background Workers

## Testability Tactics
- **Controllability**: Specialized Testing Interfaces, Record/Playback, Abstract Data Sources, Sandbox
- **Observability**: Record/Log, Localize State Storage, Specialized Monitoring, Executable Assertions
- **Limit Complexity**: Limit Structural Complexity, Limit Nondeterminism

## Deployability Tactics
- **Manage Deployment Pipeline**: Script Deployment Commands, Rollback, Manage Versioning
- **Manage Deployed System**: Blue/Green Deployment, Canary Release, Feature Toggles, A/B Testing, Proportional Shedding

## Integrability Tactics
- **Limit Dependencies**: Encapsulate, Use Intermediary, Restrict Communication Paths, Adhere to Standards, Abstract Common Services
- **Adapt**: Discover Services, Tailor Interface, Configure Behavior, Transform Representation

## Usability Tactics
- **Support User Initiative**: Cancel, Undo, Pause/Resume, Aggregate Commands
- **Support System Initiative**: Maintain Task Model, Maintain User Model, Maintain System Model

## Interoperability Tactics
- **Locate**: Discover Service, Use Known Interface
- **Manage Interfaces**: Orchestrate, Tailor Interface, Transform Representation

## Energy Efficiency Tactics
- **Monitor Resources**: Metering, Static Classification, Dynamic Classification
- **Allocate Resources**: Schedule Resources, Reduce Usage, Discovery
- **Reduce Resource Demand**: Reduce Workload, Manage Sampling Rate, Prioritize Resources
