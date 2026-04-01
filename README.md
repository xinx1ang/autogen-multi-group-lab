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

Runnable MVP with a backend abstraction and a real-model-ready AutoGen path.

## Features in the MVP

- local, dependency-light Python implementation
- four-group collaboration flow
- leader / worker role separation
- structured handoff artifacts between groups
- built-in demo task
- simple console logs for observability
- **backend switch**: heuristic by default, AutoGen-style adapter path available
- **real model call path** in `autogen_adapter.py` once dependencies and API key are present

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
the program will automatically fall back to the heuristic backend and print the exact reason.

## Environment status in this workspace

Current progress in this machine:

- `uv` has been installed locally for Python package management
- project virtualenv `.venv` has been created
- AutoGen/OpenAI package installation was started via `uv pip`
- runtime fallback and reason display are already wired

If package installation finishes and `OPENAI_API_KEY` is set,
`--backend autogen` will use a real model request path.

## What “接入 AutoGen” means here now

This repository now includes both:

1. **environment preparation work**
   - local `uv` installation
   - project `.venv`
   - package install attempt for AutoGen dependencies

2. **code-side real integration skeleton**
   - `heuristic` backend: always runnable locally
   - `autogen` backend: selected by CLI/env and routed through an adapter
   - graceful fallback when AutoGen dependencies are unavailable
   - fallback reason surfaced in runtime output
   - real `OpenAI` model call path implemented in `autogen_adapter.py`

This means the project is no longer only "conceptually ready".
The remaining runtime dependency is environment completion plus API key availability.

## To enable real AutoGen execution

Once the environment has the required packages and an API key:

```bash
export OPENAI_API_KEY=...your_key...
. .venv/bin/activate
python3 -m src.autogen_multi_group_lab.main --demo --backend autogen
```

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

- replace one-shot backend calls with richer AutoGen multi-turn conversations
- support tool-using execution and test running
- add persistent run artifacts
- add web UI / visualization if needed
