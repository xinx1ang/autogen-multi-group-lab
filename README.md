# AutoGen Multi-Group Lab

A runnable multi-agent software-factory demo inspired by AutoGen.

This project models four collaborating groups:

- **Group A — Requirement Team**: 1 leader + 2 workers
- **Group B — Implementation Team**: 1 leader + 2 workers
- **Group C — QA Team**: 1 leader + 2 workers
- **Group D — UserProxy Team**: 1 user proxy agent

The goal is not only to show multiple agents talking, but to show **organized collaboration**:

- leaders assign work
- workers produce artifacts
- downstream teams consume structured outputs
- QA can reject implementation and request another pass

## Current status

Runnable MVP with a backend abstraction.

## Features in the MVP

- local, dependency-light Python implementation
- four-group collaboration flow
- leader / worker role separation
- structured handoff artifacts between groups
- built-in demo task
- simple console logs for observability
- **backend switch**: heuristic by default, AutoGen-style adapter path available

## Quick start

Heuristic backend:

```bash
python3 -m src.autogen_multi_group_lab.main --demo --backend heuristic
```

AutoGen path with graceful fallback:

```bash
python3 -m src.autogen_multi_group_lab.main --demo --backend autogen
```

If `autogen-agentchat` / `autogen-core` are not installed or `OPENAI_API_KEY` is not set,
the program will automatically fall back to the heuristic backend and print that status.

Or run with a custom task:

```bash
python3 -m src.autogen_multi_group_lab.main --task "Build a Python function that adds two numbers and provide tests" --backend heuristic
```

## What “接入 AutoGen” means here

This repository now includes an AutoGen-ready backend abstraction:

- `heuristic` backend: always runnable locally
- `autogen` backend: selected by CLI/env and routed through an adapter
- graceful fallback when AutoGen dependencies are unavailable

This is a practical integration step that preserves the same team interfaces,
so real AutoGen conversational logic can be dropped into the adapter without rewriting the team pipeline.

## Repository structure

```text
docs/                       design docs
examples/                   example tasks
src/autogen_multi_group_lab/
  agents/                   role definitions
  backends/                 heuristic + autogen adapter
  groups/                   team logic
  runtime/                  shared schemas and backend manager
```

## Planned next steps

- replace placeholder adapter calls with real AutoGen agent conversations
- support tool-using execution and test running
- add persistent run artifacts
- add web UI / visualization if needed
