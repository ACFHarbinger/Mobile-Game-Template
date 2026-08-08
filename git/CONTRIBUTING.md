# Contributing to Mobile-Game-Template

[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Rust](https://img.shields.io/badge/Rust-1.80%2B-000000?logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/ACFHarbinger/Mobile-Game-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/ACFHarbinger/Mobile-Game-Template/actions/workflows/ci.yml)

> **Version**: 1.0
> **Last Updated**: 2026-07-30

Thank you for your interest in contributing! This document covers setup, style, and the PR process for repositories generated from this template.

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Development Setup](#2-development-setup)
3. [Code Style Guidelines](#3-code-style-guidelines)
4. [Git Workflow](#4-git-workflow)
5. [Pull Request Process](#5-pull-request-process)
6. [Testing Requirements](#6-testing-requirements)
7. [Issue Reporting](#7-issue-reporting)

---

## 1. Getting Started

### 1.1 Prerequisites

- Git, and the toolchain(s) for whichever language module(s) you're touching: `uv` (Python), `npm` (TypeScript), Gradle/JDK 21 (Kotlin), `cargo` (Rust), Go 1.22+ (Go), CMake + a C++17 compiler (C++).
- [`just`](https://github.com/casey/just) as the command runner.
- `pre-commit` (`pip install pre-commit && pre-commit install`).

### 1.2 Clone and bootstrap

```bash
git clone https://github.com/<org>/<repo>.git
cd <repo>
cp .env.example .env
just --list
```

## 2. Development Setup

Each language module is self-contained under its own top-level directory (`python/`, `typescript/`, `kotlin/`, `rust/`, `go/`, `cpp/`) with its own dependency manifest, `src/`, `test/`, `benchmark/`, and `config/`. See `.devcontainer/devcontainer.json` for a one-click containerized setup.

## 3. Code Style Guidelines

Follow the per-language rules in [`.agent/rules/`](../.agent/rules/). All modules are linted/formatted automatically via `.pre-commit-config.yaml` — run `pre-commit run --all-files` before pushing.

## 4. Git Workflow

- Branch from `main`: `feature/<short-description>` or `fix/<short-description>`.
- Keep commits focused; write commit messages that explain *why*, not just *what*.
- Rebase onto `main` before opening a PR.

## 5. Pull Request Process

1. Fill out the [PR template](../.github/PULL_REQUEST_TEMPLATE.md) in full.
2. Ensure CI is green (`just lint && just test`).
3. Request review; address feedback with new commits (don't force-push during review).
4. Squash-merge once approved.

## 6. Testing Requirements

Every new public function/class needs a test. See [`.agent/rules/test_writing.md`](../.agent/rules/test_writing.md).

## 7. Issue Reporting

Use the [issue templates](../.github/ISSUE_TEMPLATE/) — they help both humans and coding agents triage faster.
