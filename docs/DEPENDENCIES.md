# Dependencies

| Module | Manifest | Manager |
| --- | --- | --- |
| `python/` | `pyproject.toml` | [uv](https://github.com/astral-sh/uv) |
| `typescript/` | `package.json` | npm |
| `kotlin/` | `build.gradle.kts` | Gradle |
| `java/` | `pom.xml` | Maven |
| `rust/` | `Cargo.toml` | Cargo |
| `go/` | `go.mod` | Go modules |
| `cpp/` | `CMakeLists.txt` | CMake (+ vcpkg/Conan as needed) |

Dependency updates are automated via [Dependabot](../.github/dependabot.yml) on a per-ecosystem weekly schedule. Environment-level dependencies (system packages, CUDA, etc.) are documented in [`env/`](../env/).

See [`DEPENDENCY_POLICY.md`](DEPENDENCY_POLICY.md) for the policy on adding, pinning, and upgrading dependencies.
