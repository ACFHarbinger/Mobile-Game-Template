# Research Methodology & Guidelines

Guidelines and protocols for conducting technical research, architectural spikes, and mobile game loop assessments across Android and iOS.

## Overview

In this project, research is a collaborative effort to explore new mobile rendering techniques, evaluate Kotlin (Android) and Swift (iOS) framework decisions, and prototype cross-platform asset/state-machine capabilities before they are formally adopted into the core modules (`android/`, `ios/`, `core/`). This document outlines our standard research methodology to ensure that findings are structured, reproducible, and aligned with our system design principles.

---

## 1. Initiating Research

Research is typically initiated via an issue labeled with `type/research` or `type/spike`. Before starting:
1. Create a dedicated feature branch named `research/<issue-number>-<short-description>`.
2. Define clear boundaries to avoid "scope creep". A research spike should have a fixed duration (usually 2-5 days).

## 2. Research Steps

### Phase 1: Literature & Ecosystem Review
Explore existing mobile game graphics performance guides (SurfaceView, SpriteKit, Metal) and state-machine sharing design patterns. Document options in the research note.

### Phase 2: Prototyping (Spikes)
Build a minimalist proof-of-concept. Experimental code should:
- Live in the relevant client module (`android/` or `ios/`) but be clearly isolated (e.g. in a `spike/` or `experimental/` package).
- Avoid changing existing production code interfaces unless necessary.
- Include a simple driver or view harness to demonstrate functionality.

### Phase 3: Evaluation
Benchmark frame rates, memory overhead, battery consumption, and assess developer experience on target Android and iOS test devices/emulators.

## 3. Documenting Findings

Upon completion, the researcher must compile findings into a research note under `docs/moon/research/` utilizing the `TEMPLATE.md` structure. The research note must be committed to the branch, and a Pull Request opened for review.
Once the PR is approved and merged, the decisions made should be codified in an [Architectural Decision Record (ADR)](../adr/0001-record-architecture-decisions.md) if they alter the project's long-term structure or technologies.
