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

Runnable MVP.

## Features in the MVP

- local, dependency-light Python implementation
- four-group collaboration flow
- leader / worker role separation
- structured handoff artifacts between groups
- built-in demo task
- simple console logs for observability

## Why this exists

Many multi-agent demos stop at “several agents chatting.”
This project tries to model a more realistic software-delivery pipeline:

1. requirements analysis and task breakdown
2. implementation planning and code drafting
3. testing and acceptance decision
4. final user-facing summary through a user proxy

## Quick start

```bash
python3 -m src.autogen_multi_group_lab.main --demo
```

Or run with a custom task:

```bash
python3 -m src.autogen_multi_group_lab.main --task "Build a Python function that adds two numbers and provide tests"
```

## Repository structure

```text
docs/                       design docs
examples/                   example tasks
src/autogen_multi_group_lab/
  agents/                   role definitions
  groups/                   team logic
  runtime/                  shared schemas and orchestration
```

## Planned next steps

- replace heuristic workers with real LLM-backed AutoGen agents
- support tool-using execution and test running
- add persistent run artifacts
- add web UI / visualization if needed
