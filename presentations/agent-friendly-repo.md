# Defining an Agent-Friendly Repository

Draft presentation outline

**Audience:** Developers, technical leads, and repository maintainers adopting AI coding assistants.

**Suggested length:** 25–30 minutes, including discussion.

**Presentation objective:** Define what makes a repository agent-friendly, connect those qualities to concrete repository artifacts, and give teams a practical way to assess readiness.

**Working definition:** An agent-friendly repository provides discoverable project knowledge, clear instructions and boundaries, executable verification, and persistent task state so a coding assistant can make reviewable changes with appropriate human oversight.

This outline synthesizes the repository's practical guides. The suggested repository layout and readiness checklist are proposed applications of those practices, rather than requirements for a particular assistant.

## 1. The repository is part of the agent's working environment

**Key message:** Effective agentic development depends on the environment around the model.

- An assistant needs to discover how the project works, identify relevant code, understand constraints, and evaluate its changes.
- Knowledge available only in a developer's memory or an old chat is difficult to recover reliably.
- Repository readiness means making that knowledge and feedback accessible during the work.
- Opening question for the audience: Could a new assistant find the correct implementation path and verification commands without a maintainer narrating every step?

**Suggested visual:** Task → repository context → change → executable feedback → review.

**Source:** [Planning practices, sections 1.2–1.3](../coding-assistant-planning-practices.md#12-understand-the-codebase-before-planning).

## 2. Define agent-friendly through observable capabilities

**Key message:** Readiness can be assessed through what an assistant can do.

| Capability | Question the repository should help answer | Evidence |
| --- | --- | --- |
| Discover | Where is the relevant code and project knowledge? | Entry documentation, module map, linked architecture and contracts |
| Understand | Which conventions and constraints apply here? | Concise instructions and documented decisions |
| Act within bounds | What is in scope, and when is human input required? | Acceptance criteria, permissions, review gates |
| Verify | How can I establish that the change works? | Runnable checks and clear completion criteria |
| Resume | What has been completed, verified, and left unresolved? | Current plan and checkpoint |

**Speaker emphasis:** These capabilities are the presentation's proposed synthesis of the guides and apply across coding assistants.

**Sources:** [Context management, sections 1.1–1.5](../context-window-management.md#1-common-best-practices-across-all-three-assistants); [closed-loop practices](../open-vs-closed-loop-practices.md).

## 3. Make project knowledge discoverable in layers

**Key message:** Give the assistant a short route from the task to the necessary evidence.

- Use an entry document to explain repository structure and point to relevant instructions, architecture, and verification commands.
- Keep architectural decisions, API contracts, and specifications in version-controlled files.
- Support progressive discovery: task → relevant module → dependencies and contracts → targeted code and tests.
- Keep detailed reference material behind links so every task does not require loading the entire repository.

**Suggested example:** Trace an authentication change from the repository map to the authentication module, API contract, and relevant tests.

**Source:** [Context management, sections 1.1–1.5](../context-window-management.md#11-keep-context-focused-on-the-current-task).

## 4. Keep persistent instructions concise and stable

**Key message:** Instruction files should capture reusable project guidance and direct the assistant to deeper material.

- Include essential commands, coding conventions, architectural constraints, and applicable execution boundaries.
- Put local guidance near the code it governs where the assistant supports hierarchical instructions.
- Keep temporary debugging notes, task progress, and long tutorials in separate documents.
- Avoid duplicated or conflicting guidance across instruction files.
- Use the instruction mechanism supported by the chosen assistant; the guides discuss `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md`.

**Suggested visual:** Short repository instructions → local guidance → detailed reference documents.

**Sources:** [Context management, section 1.3](../context-window-management.md#13-keep-persistent-instructions-concise) and [section 3.2](../context-window-management.md#32-keep-agentsmd-short-and-hierarchical); [cache guidance, section 1.2](../cache-token-guidance.md#12-keep-stable-instructions-consistent).

## 5. Make verification an executable repository capability

**Key message:** A reliable verification environment is the central enabler of closed-loop development.

- Document setup prerequisites and the exact commands needed to run applicable checks.
- Provide tests, builds, linting, and type checks appropriate to the project.
- Make targeted checks easy to find, with broader regression checks for wider changes.
- Define observable success criteria and preserve meaningful failure output.
- Distinguish checks that passed, checks that failed, and checks that could not run.

**Suggested demonstration:** Start from a small behavior change, run its targeted check, inspect a failure, correct the implementation, and rerun verification.

**Source:** [Closed-loop practices, section 2](../open-vs-closed-loop-practices.md#2-common-good-practices) and [key recommendation](../open-vs-closed-loop-practices.md#5-key-recommendation).

## 6. Define bounded autonomy and completion

**Key message:** The repository and task specification should make the limits of autonomous execution explicit.

- Specify expected behavior, scope, compatibility constraints, and acceptance criteria before implementation.
- Use open-loop exploration when appropriate; use execution feedback for changes requiring verification.
- Bound correction attempts and define when the assistant should escalate unresolved failures.
- Preserve verification integrity: do not weaken assertions or acceptance criteria merely to obtain a passing result.
- Document human review and approval requirements for consequential actions and significant decisions.
- For substantial phased work, the planning guide recommends developer validation before moving between phases.

**Suggested visual:** Implement → verify → evaluate → correct, with exits for completion and escalation and a developer validation gate at the phase boundary.

**Sources:** [Closed-loop practices, sections 1–2](../open-vs-closed-loop-practices.md#1-understand-the-two-workflows); [planning practices, sections 1.7–1.9](../coding-assistant-planning-practices.md#17-support-closed-loop-execution-at-task-and-phase-levels).

## 7. Make substantial work resumable

**Key message:** A fresh session should be able to reconstruct the current task from repository artifacts.

- Persist substantial plans with objectives, tasks, dependencies, acceptance criteria, verification, and review gates.
- Maintain checkpoints containing decisions, files changed, checks and results, unresolved issues, and next actions.
- Separate stable project knowledge from temporary task state.
- Keep the recorded state current; distinguish verified facts from assumptions and completed work from proposed work.
- Scale the process to the task: small edits need less planning than changes spanning modules or sessions.

**Suggested exercise:** Ask a fresh assistant to identify the next action from a checkpoint without reading the prior conversation.

**Sources:** [Planning practices, sections 1.10–1.11](../coding-assistant-planning-practices.md#110-maintain-the-plan-as-a-living-artifact); [context management, sections 1.4–1.5](../context-window-management.md#14-summarize-at-meaningful-milestones).

## 8. Support bounded delegation when it adds value

**Key message:** Clear scope and evidence make work easier to delegate and integrate.

- Define each assignment's objective, scope, constraints, deliverable, and completion criteria.
- Prefer independent investigations or changes with limited overlap.
- Isolate concurrent modifications in branches or worktrees where needed.
- Require concise findings with file references, evidence, verification results, and unresolved risks.
- Keep responsibility for integration and final validation with the primary agent.
- Use delegation selectively; concurrency adds coordination cost and can duplicate work.

**Repository implication:** Clear module responsibilities, contracts, and targeted checks help define bounded assignments.

**Source:** [Subagent practices, sections 1.1–1.9](../subagent-practices.md#1-common-best-practices-across-coding-assistants).

## 9. Treat efficiency as a measured outcome

**Key message:** Evaluate the cost of successfully verified work alongside quality.

- Reduce irrelevant context through targeted discovery and concise instructions.
- Keep reusable guidance stable; place changing task information elsewhere.
- Measure completion time, correction attempts, human intervention, and review rework.
- Evaluate model choices against representative tasks from the actual repository.
- Use cache metrics as supporting evidence: cache reuse does not expand the context window, and a high reuse percentage alone does not establish efficiency.

**Speaker emphasis:** Efficient context and model use support the repository's core capabilities; model choice alone does not establish readiness.

**Sources:** [Model selection, sections 1.2–1.3](../model-selection-guidance.md#12-use-a-tiered-escalation-strategy) and [section 1.8](../model-selection-guidance.md#18-evaluate-models-on-your-own-codebase); [cache guidance, sections 1.1–1.8](../cache-token-guidance.md#1-common-best-practices-across-all-three-assistants).

## 10. Show what the capabilities look like in a repository

**Key message:** A small set of maintained artifacts can make the workflow discoverable and repeatable.

Illustrative layout; adapt names and structure to the project and assistant:

```text
repository/
├── README.md                 # Entry point, module map, setup, links
├── AGENTS.md                 # Example assistant instruction entry point
├── CONTRIBUTING.md           # Development and verification workflow
├── docs/
│   ├── architecture.md       # Components, boundaries, dependencies
│   ├── decisions/            # Architectural decisions and rationale
│   └── plans/                # Substantial task plans and progress
├── src/                      # Implementation and applicable local guidance
├── tests/                    # Executable behavior checks
├── scripts/                  # Setup and verification entry points
└── CHECKPOINT.md             # Current handoff state when needed
```

- Explain how an assistant follows the links for one concrete task.
- Verify that documented commands work in the supported environment.
- Assign maintenance responsibility so documents continue to describe the code.
- Treat the layout as an example; assess the capabilities demonstrated by the contents.

**Sources:** [Context management, sections 1.3–1.5](../context-window-management.md#13-keep-persistent-instructions-concise); [planning practices, section 4](../coding-assistant-planning-practices.md#4-recommended-implementation-plan-structure).

## 11. Assess readiness with a representative task

**Key message:** Demonstrate readiness by observing an assistant complete and hand off real work.

Proposed checklist for a bounded change:

- Can the assistant find the relevant code, constraints, and contracts?
- Can it identify and run the documented verification commands?
- Are the acceptance criteria and human review boundaries clear?
- Can it use failure feedback to correct the change within agreed limits?
- Does the final report distinguish verified results from unresolved issues?
- Can a fresh session recover the current state and next actions?

Record evidence and friction for each item. Use the findings to prioritize repository improvements.

**Suggested audience activity:** Identify the first missing capability in a repository the team maintains.

**Sources:** [Model selection, section 1.8](../model-selection-guidance.md#18-evaluate-models-on-your-own-codebase); [closed-loop practices, section 2](../open-vs-closed-loop-practices.md#2-common-good-practices); [context management, section 1.4](../context-window-management.md#14-summarize-at-meaningful-milestones).

## 12. Turn the definition into a first improvement

**Key message:** Start with the gap that most often prevents a verified, reviewable result.

- Establish working setup and verification commands with clear completion criteria.
- Add concise entry instructions and links to essential project knowledge.
- Introduce persistent plans and checkpoints for substantial work.
- Clarify execution boundaries, escalation conditions, and developer validation gates.
- Repeat a representative task and compare evidence of quality, time, rework, and intervention.

**Closing discussion:** Which repository improvement would most help an assistant complete your team's next real task?

**Definition to leave on screen:** An agent-friendly repository makes project knowledge discoverable, changes bounded, results verifiable, and work resumable.

## Source guides

- [Open-loop vs. closed-loop practices](../open-vs-closed-loop-practices.md)
- [Planning practices](../coding-assistant-planning-practices.md)
- [Context window management](../context-window-management.md)
- [Subagent practices](../subagent-practices.md)
- [Model selection guidance](../model-selection-guidance.md)
- [Cache token guidance](../cache-token-guidance.md)
