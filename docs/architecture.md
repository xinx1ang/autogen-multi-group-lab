# Architecture

## Goal

Build a directly runnable repository that demonstrates a 4-group multi-agent workflow inspired by AutoGen:

- Requirement Team
- Implementation Team
- QA Team
- UserProxy Team

## Team design

### Requirement Team
- Leader: assigns analysis work and merges the result into a structured spec
- Worker 1: clarifies user intent and constraints
- Worker 2: decomposes the task into concrete subtasks

### Implementation Team
- Leader: assigns implementation work and merges it into a delivery plan
- Worker 1: proposes core implementation
- Worker 2: proposes supporting code, refactor, edge-case handling, and docs

### QA Team
- Leader: defines acceptance judgment and decides pass/fail
- Worker 1: creates test cases
- Worker 2: performs review and risk inspection

### UserProxy Team
- UserProxy: receives the original task, invokes teams, and returns the final result

## Pipeline

1. UserProxy receives task
2. Requirement Team returns structured task specification
3. Implementation Team returns implementation plan and code draft
4. QA Team returns pass/fail decision
5. UserProxy returns final summary

## MVP simplification

To make the repository immediately runnable, the first version uses deterministic Python role logic instead of remote LLM calls.
This preserves the organizational design while making the project easy to run locally.

The LLM-backed AutoGen implementation can be added in later iterations behind the same team interfaces.
