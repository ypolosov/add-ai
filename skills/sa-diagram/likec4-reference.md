# LikeC4 DSL Quick Reference

## Specification (element, relation & deployment node kinds)

```likec4
specification {
  element person {
    style {
      shape person
      color amber
    }
  }
  element softwareSystem {
    style {
      shape rectangle
      color blue
    }
  }
  element container {
    style {
      shape rectangle
      color green
    }
  }
  element component {
    style {
      shape rectangle
      color slate
    }
  }
  element database {
    style {
      shape storage
      color red
    }
  }
  element queue {
    style {
      shape queue
      color purple
    }
  }

  relationship async {
    style {
      line dashed
      color gray
    }
  }
  relationship sync {
    style {
      line solid
      color blue
    }
  }

  deploymentNode environment
  deploymentNode zone
  deploymentNode kubernetes {
    style {
      color blue
      icon tech:kubernetes
    }
  }
  deploymentNode vm {
    notation 'Virtual Machine'
    technology 'VMware'
  }
}
```

## Model

```likec4
model {
  customer = person "Customer" {
    description "End user of the platform"
  }

  gtPlatform = softwareSystem "GT Platform" {
    description "Online gambling platform"

    webApp = container "Web Application" {
      description "SPA frontend"
      technology "React"
    }

    apiGateway = container "API Gateway" {
      description "API entry point"
      technology "NestJS"
    }

    database = database "Database" {
      description "Primary data store"
      technology "PostgreSQL"
    }

    // Relationships inside the system
    webApp -> apiGateway "Uses" { style sync }
    apiGateway -> database "Reads/Writes" { style sync }
  }

  // External relationships
  customer -> gtPlatform.webApp "Uses" { style sync }
}
```

## Views

```likec4
views {
  view systemContext of gtPlatform {
    title "GT Platform - System Context"
    include *
  }

  view containers of gtPlatform {
    title "GT Platform - Containers"
    include *
    include customer
  }

  view components of gtPlatform.apiGateway {
    title "API Gateway - Components"
    include *
  }
}
```

## Deployment Model

```likec4
deployment {
  environment prod 'Production' {
    zone eu 'EU Region' {
      zone zone1 {
        instanceOf gtPlatform.webApp
        instanceOf gtPlatform.apiGateway
      }
      zone zone2 {
        web = instanceOf gtPlatform.webApp
        api1 = instanceOf gtPlatform.apiGateway
        api2 = instanceOf gtPlatform.apiGateway
      }
      db = instanceOf gtPlatform.database
    }

    // Deployment relationships
    vm vm1 {
      db = instanceOf gtPlatform.database 'Primary DB'
    }
    vm vm2 {
      db = instanceOf gtPlatform.database 'Standby DB'
    }
    vm2.db -> vm1.db 'replicates'
  }
}
```

## Deployment Views

```likec4
deployment view prodDeployment {
  title 'Production Deployment'
  include prod.**
  include * -> *
}
```

## Dynamic Views

```likec4
dynamic view userLogin {
  title 'User Login Flow'

  customer -> web 'opens in browser'
  web -> auth 'updates bearer token if needed'
  web -> api 'POST request'
  api -> auth  // title derived from model
  api -> api 'process request'  // self-call
  web <- api 'returns JSON'  // reverse direction

  // Include non-participating elements for context
  include cloud, ui, backend

  style cloud {
    color muted
    opacity 0%
  }
}

// Continuous steps syntax (chaining)
dynamic view shortForm {
  customer
    -> web
    -> api  // same as web -> api
    -> web  // same as web <- api
}
```

## Style Options
- **shape**: rectangle, person, storage, queue, cylinder, browser, mobile
- **color**: amber, blue, green, red, purple, slate, gray, indigo, sky, emerald
- **line**: solid, dashed, dotted
- **opacity**: 0-100
