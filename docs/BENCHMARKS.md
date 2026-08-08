# Benchmarks

> **TODO:** Fill in with real benchmark results once the project has measurable workloads.

| Module | Tool | Location |
| --- | --- | --- |
| `python/` | pytest-benchmark | `python/benchmark/` |
| `rust/` | criterion | `rust/benches/` |
| `cpp/` | Google Benchmark | `cpp/benchmark/` |
| `go/` | `testing.B` | `go/*_test.go` |

Run the full suite with `just bench`, or a single module's benchmarks as shown above. CI runs benchmarks on pushes to `main` that touch a `benchmark/`/`benches/` directory — see [`.github/workflows/benchmark.yml`](../.github/workflows/benchmark.yml).
