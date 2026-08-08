/*
 * Mobile-Game-Template — Structurizr DSL workspace (C4 model)
 *
 * See docs/structurizr/README.md for rendering instructions.
 *
 * TODO: Replace the placeholder model below with the real system once this
 * template is used to seed a product repository.
 */

workspace "Mobile-Game-Template" "Placeholder C4 model for a repository generated from this template." {

    model {
        user = person "User" "Interacts with the system."

        system = softwareSystem "System" "The application generated from this template." {
            api = container "API" "Serves requests." "Python"
            webapp = container "Web App" "User-facing interface." "TypeScript"
            core = container "Core Engine" "Performance-critical logic." "Rust / C++"
            database = container "Database" "Stores application state." "PostgreSQL"
        }

        user -> webapp "Uses"
        webapp -> api "Calls" "HTTPS/JSON"
        api -> core "Delegates to"
        api -> database "Reads/writes"
    }

    views {
        systemContext system "SystemContext" {
            include *
            autoLayout
        }

        container system "Containers" {
            include *
            autoLayout
        }

        theme default
    }
}
