# Best practices for using subagents in AI coding assistants

Subagents are specialized AI agents that a primary coding assistant can delegate work to. They can independently investigate problems, review code, implement features, or run tests, then report their results to the primary agent.

The three coding assistants—GitHub Copilot, OpenAI Codex, and Claude Code—support agent-oriented workflows, but differ in how subagents are defined, invoked, isolated, and coordinated.

The most important principle is:

Use subagents to divide work by responsibility and context, not simply to maximize parallelism.

## 1. Common best practices across coding assistants

These practices apply regardless of which coding assistant you use.

### 1.1 Delegate well-defined, bounded tasks

A subagent should have a specific responsibility, clear scope, and measurable outcome.

| Poor delegation      | Better delegation                                                  |
| -------------------- | ------------------------------------------------------------------ |
| Improve the codebase | Review authentication code for security vulnerabilities            |
| Fix the tests        | Identify and fix failing unit tests in the validation module       |
| Review my changes    | Review the diff for correctness, regressions, and missing tests    |
| Improve performance  | Profile the JSON parser and identify the three largest bottlenecks |

A useful delegation prompt specifies:

- Objective: What the subagent must accomplish.
- Scope: Files, modules, or functionality it should examine.
- Constraints: What it must not modify or assume.
- Deliverable: Findings, code changes, tests, or recommendations.
- Completion criteria: How to determine success.

### 1.2 Use subagents for independent work

Subagents are most effective when tasks have few dependencies and limited overlap.

Example: Parallel code investigation

Primary coding agent

Coordinates the investigation and integrates findings

Agent 1

Inspect implementation

Agent 2

Review test coverage

Agent 3

Analyze security

Primary coding agent

Reconciles results, implements changes, and validates

Good candidates for parallel delegation include codebase exploration, independent design reviews, security audits, and test coverage analysis.

Avoid assigning multiple agents overlapping edits to the same files unless their work is isolated in separate worktrees or branches.

### 1.3 Separate implementation from review

A useful pattern is to assign different responsibilities to different agents:

1. Implementation agent: Writes the code.
2. Review agent: Independently evaluates correctness, maintainability, and risks.
3. Testing agent: Verifies expected behavior and identifies missing tests.
4. Primary agent: Resolves findings and makes the final integration decision.

This separation can reduce confirmation bias, although independent review is not a substitute for human review.

### 1.4 Keep the primary agent responsible for integration

Subagents should not independently make conflicting architectural decisions.

The primary agent should own the overall plan, assign tasks, reconcile conflicting findings, review changes, and run final validation.

A subagent completing its assignment does not mean the overall task is complete.

### 1.5 Manage context deliberately

One major benefit of subagents is context isolation.

A subagent can examine large amounts of source code, logs, and documentation without filling the primary agent's conversation with all the intermediate details.

Ask subagents to return concise, structured results:

```
Return:
1. Summary of findings
2. Files examined or modified
3. Evidence supporting each finding
4. Tests executed and results
5. Remaining risks or open questions
```

This makes the subagent's output easier to integrate and reduces unnecessary context consumption.

### 1.6 Limit subagent concurrency

More agents do not necessarily mean faster execution.

Parallel execution can increase token consumption, duplicate work, create conflicting changes, and make coordination harder.

Start with two or three independent subagents. Increase concurrency only when tasks are genuinely independent and the improvement justifies the cost.

### 1.7 Define permissions and boundaries

Apply least-privilege principles:

- Give read-only investigation agents read-only tools where supported.
- Restrict implementation agents to relevant modules.
- Avoid granting unrestricted shell execution unless necessary.
- Require approval for destructive operations or external side effects.
- Use isolated branches or worktrees for concurrent modifications.

### 1.8 Require evidence and validation

A subagent's conclusion should be verifiable.

For example, a code review finding should identify the file, relevant lines, explanation, and potential failure scenario.

For implementation tasks, request test results and explicitly distinguish tests that passed from tests that were not run.

### 1.9 Avoid unnecessary delegation

Not every task warrants a subagent.

| Task                                     | Recommended approach                 |
| ---------------------------------------- | ------------------------------------ |
| Rename a variable                        | Primary agent                        |
| Fix a straightforward syntax error       | Primary agent                        |
| Investigate a complex bug across modules | Subagent                             |
| Independent code review                  | Subagent                             |
| Analyze multiple alternative designs     | Parallel subagents                   |
| Implement independent modules            | Parallel subagents with isolation    |
| Make final architectural decisions       | Primary agent, informed by subagents |

Rule of thumb: Delegate when specialization, independent verification, or context isolation provides more value than the coordination overhead.

## 2. GitHub Copilot-specific practices

GitHub Copilot supports subagents in VS Code and Copilot CLI, but the invocation and orchestration mechanisms differ.

### 2.1 VS Code: Enable and explicitly invoke subagents

In VS Code, enable the `runSubagent` tool in Copilot Chat. You can then ask Copilot to delegate a task or explicitly reference `#runSubagent`.

Example:

```
Use #runSubagent to independently examine the
authentication module for security vulnerabilities.

Do not modify files.

Report findings with file references and suggested
remediation steps.
```

For complex tasks, consider using Plan mode first, then delegate independent investigations.

### 2.2 Copilot CLI: Use built-in specialized agents

Copilot CLI provides built-in agents for common development activities, including:

| Agent             | Recommended use                                 |
| ----------------- | ----------------------------------------------- |
| `explore`         | Read-only codebase investigation                |
| `task`            | Execute builds, tests, and development commands |
| `code-review`     | Review code changes for significant defects     |
| `security-review` | Identify exploitable security vulnerabilities   |
| `research`        | Conduct deeper technical investigations         |
| `rubber-duck`     | Obtain a second opinion on plans and code       |
| `general-purpose` | Perform broader delegated tasks                 |

Use these before creating custom agents that duplicate their functionality.

### 2.3 Use `/fleet` for parallel orchestration in Copilot CLI

GitHub documents `/fleet` as a mechanism for delegating work to multiple agents. For more complex assignments, use `/plan` to establish the task breakdown before using `/fleet`.

Example:

```
/fleet Investigate the validation subsystem.

Delegate independent tasks to:
1. Examine validation logic for correctness.
2. Identify missing test coverage.
3. Review error handling and diagnostics.

Do not modify files.
Consolidate findings into a prioritized report.
```

The orchestrator determines how to delegate and parallelize the work; the prompt does not guarantee exactly three subagents.

### 2.4 Define reusable custom agents

For repository-level custom agents, use `.github/agents/` with Markdown agent definitions.

A useful practice is to define custom agents around recurring responsibilities, such as schema validation, API compatibility, or architectural conformance.

Make agent descriptions specific so Copilot can select the appropriate agent.

Copilot recommendation: Use `#runSubagent` for isolated investigations in VS Code, `/fleet` for parallel tasks in Copilot CLI, and custom agents for recurring specialized work.

## 3. OpenAI Codex-specific practices

For Codex CLI, I recommend using the primary agent as an orchestrator and explicitly requesting subagents for independent work.

### 3.1 Prompt Codex to delegate selectively

Rather than telling Codex to always use subagents, establish delegation criteria.

Example:

```
Use subagents when tasks are independent,
can execute in parallel, or benefit from
separate context.

Before delegating:
- Identify independent workstreams.
- Assign each subagent a bounded objective.
- Avoid overlapping file modifications.
- Keep simple tasks in the primary agent.

The primary agent owns integration,
final validation, and the summary.
```

This approach aligns with OpenAI's documented multi-agent guidance.

### 3.2 Use AGENTS.md for persistent guidance

Codex recognizes `AGENTS.md` as repository guidance. It is useful for instructions that should apply consistently across development sessions.

For example, you could add the delegation policy above to `AGENTS.md`, alongside your coding conventions, test requirements, and architectural constraints.

However, `AGENTS.md` is an instruction file, not itself a subagent definition or a mechanism that enables multi-agent support.

### 3.3 Distinguish CLI capabilities from API orchestration

OpenAI also documents multi-agent orchestration through its Agents API, where `multi_agent.enabled` enables delegation and `max_concurrent_subagents` limits concurrency.

That API configuration should not be confused with Codex CLI configuration. They are different interfaces, even though they share the Codex harness architecture.

### 3.4 Prefer read-only parallel exploration before implementation

A particularly effective Codex workflow is:

1. Ask independent subagents to investigate implementation, tests, and architecture.
2. Have the primary agent consolidate their findings.
3. Agree on the implementation plan.
4. Delegate isolated implementation tasks where appropriate.
5. Run independent review and final tests.

Codex recommendation: Establish a reusable delegation policy in `AGENTS.md`, explicitly request independent subagent investigations, and keep code integration centralized.

## 4. Claude Code-specific practices

Claude Code provides explicit support for custom subagents, including agent-specific prompts, tools, permissions, and model selection.

### 4.1 Define specialized agents in Markdown

Claude Code supports project-specific subagents under `.claude/agents/` and personal subagents under `~/.claude/agents/`.

For example, a reusable code review subagent:

```
---
name: code-reviewer
description: Reviews code for correctness,
  regressions, and maintainability.
tools: Read, Grep, Glob
model: sonnet
---

You are an independent code reviewer.

Examine the assigned code changes.
Do not modify files.

Report:
- Significant defects
- File and line references
- Supporting evidence
- Recommended corrections

Avoid speculative findings.
```

This gives the reviewer a dedicated role and restricts it to read-oriented tools.

### 4.2 Use model selection to balance cost and capability

Claude Code lets custom subagents use different models.

A practical strategy is to use a faster, less expensive model for routine exploration, a stronger model for complex design or implementation, and an appropriate model for independent review.

The `model` field in a custom subagent definition supports this configuration.

### 4.3 Prefer subagents for context-heavy investigations

Claude Code's subagent design is particularly useful for keeping verbose operations out of the main conversation.

For example:

```
Use three subagents in parallel to investigate:

1. Authentication implementation
2. Test coverage
3. Error handling

Each subagent must return a concise report
with supporting file references.

Do not modify code.
```

For implementation work requiring independent, long-running collaboration, consider Claude Code's separate agent-team capabilities rather than treating ordinary subagents as fully independent development sessions.

### 4.4 Distinguish subagents from skills

In Claude Code, a skill provides reusable instructions or a workflow, while a subagent provides a separate execution context with its own behavior and tools.

Use a skill to teach Claude how to perform a procedure. Use a subagent when the procedure should be delegated to an isolated worker.

These mechanisms can complement each other.

Claude Code recommendation: Define a small set of reusable specialists, use model selection and tool restrictions deliberately, and delegate context-heavy research and independent reviews.

## 5. Comparison across coding assistants

| Capability                         | GitHub Copilot                    | Codex                           | Claude Code               |
| ---------------------------------- | --------------------------------- | ------------------------------- | ------------------------- |
| Delegate in natural language       | Yes                               | Yes                             | Yes                       |
| Isolated subagent context          | Yes                               | Yes                             | Yes                       |
| Parallel delegation                | Yes                               | Yes                             | Yes                       |
| Persistent repository instructions | `AGENTS.md`, Copilot instructions | `AGENTS.md`                     | `CLAUDE.md`               |
| Specialized agent definitions      | `.github/agents/`                 | Runtime/configuration dependent | `.claude/agents/`         |
| Built-in specialized agents        | Yes                               | Runtime dependent               | Yes                       |
| Tool restrictions per specialist   | Supported                         | Configuration dependent         | Supported                 |
| Explicit parallel orchestration    | `/fleet` in CLI                   | Multi-agent orchestration       | Subagents and agent teams |

Features and configuration details vary by product surface and installed version.

## 6. A reusable prompting pattern

The following is the prompt I would recommend starting with across all three coding assistants.

## Subagent delegation policy

Use subagents selectively to improve development efficiency, code quality, and context management.

**Delegation criteria**

- Delegate independent, well-defined tasks that can run concurrently.
- Use subagents for codebase exploration, research, code review, security analysis, and test assessment.
- Keep simple or tightly dependent tasks in the primary agent.
- Avoid unnecessary delegation overhead.

**Execution**

- Identify workstreams and dependencies before delegation.
- Give each subagent a clear objective, scope, constraints, and expected deliverable.
- Prefer read-only access for investigative tasks.
- Avoid concurrent modifications to the same files.
- Use isolated worktrees or branches for parallel implementation when appropriate.
- Start with at most three concurrent subagents unless additional concurrency is justified.

**Coordination**

- The primary agent owns planning, integration, and final validation.
- Require subagents to provide concise, evidence-based results.
- Independently review implementation changes.
- Run relevant tests after integrating changes.
- Report unresolved issues and tests not executed.

**Reporting**\
Summarize which tasks were delegated, the findings, changes made, tests performed, and remaining risks.

For repeated use, put this policy in the repository's agent instructions and adapt it to the assistant's supported features.

## 7. My recommended starting approach

Start with three responsibilities: exploration, implementation, and review. Keep the primary agent responsible for orchestration and integration.

Use parallel subagents for exploration and independent analysis, but normally keep implementation sequential until module boundaries and file ownership are clear. After implementation, use an independent review subagent and have the primary agent verify the result.

This gives you the main benefits of subagents—context isolation, parallel investigation, and independent verification—without immediately introducing a complicated multi-agent development process.

### References

- [GitHub Copilot: Using subagents in your IDE](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-subagents?tool=vscode\&utm_source=chatgpt.com)
- [GitHub Copilot: Delegating and parallelizing work](https://docs.github.com/en/copilot/concepts/agent-capabilities/choosing-and-delegating-agent-work/delegating-and-parallelizing-work-with-agents?utm_source=chatgpt.com)
- [OpenAI: Multi-agent orchestration](https://developers.openai.com/api/docs/guides/agents-api/multi-agent?utm_source=chatgpt.com)
- [OpenAI: Codex development workflows](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex?utm_source=chatgpt.com)
- [Claude Code: Create custom subagents](https://code.claude.com/docs/en/sub-agents?utm_source=chatgpt.com)
- [Anthropic: How and when to use subagents](https://claude.com/blog/subagents-in-claude-code?utm_source=chatgpt.com)
