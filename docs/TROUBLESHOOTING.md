# Troubleshooting

## `just` commands fail with "recipe not found"

Make sure you're running `just` from the repo root — recipes are defined relative to `tools/`.

## Python module can't find dependencies

Run `uv sync --group dev` inside `python/`, and confirm `.python-version` matches an interpreter `uv` can find.

## TypeScript build fails on a fresh clone

Delete `typescript/node_modules` and re-run `npm ci` (not `npm install`) to get the exact locked versions.

## C++ module fails to configure with CMake

Confirm CMake ≥ 3.20 and a C++17-capable compiler are on `PATH`. If using vcpkg/Pixi, make sure the toolchain file is passed via `-DCMAKE_TOOLCHAIN_FILE`.

## Docker Compose stack won't start

Check `.env` exists (`cp .env.example .env`) and that the ports in `infra/docker/docker-compose.yml` aren't already bound by another local service.

## Pre-commit hook fails on a hook I don't have installed locally

Most hooks run via `language: system` and expect the module's toolchain (e.g. `cargo`, `./gradlew`) to already be on `PATH` — install the missing toolchain rather than skipping the hook.

---

Still stuck? Open an issue using the [bug report template](../.github/ISSUE_TEMPLATE/bug_report.yml).
