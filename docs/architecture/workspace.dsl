workspace "add-ai" "Architecture documentation and C4 model." {

    model {
        user = person "User" "End user"
        main = softwareSystem "Main System" "Placeholder; refine in ADD iterations."
        user -> main "Uses" "Web Browser"
    }

    views {
        systemLandscape "SystemLandscape" "Default landscape view." {
            include *
            autoLayout
        }
        systemContext main "SystemContext" "System context for Main System." {
            include *
            autoLayout
        }
    }

    configuration {
        scope landscape
    }

    !docs "docs"
    !adrs "adrs" madr
}
