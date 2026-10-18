# Effective AI Coding Assistants

## Context, caching, model selection, and subagents

**A practical workflow for reliable results at a sensible cost**

GitHub Copilot · OpenAI Codex · Claude Code

<!--
Deck guide: Each horizontal rule starts a new slide. HTML comments contain
speaker notes and source mappings, not on-slide content. Slides 1–21 form the
main presentation; slides 22–25 are optional reference material.
Audience: Developers and engineering leads using agentic coding assistants.
Suggested duration: 25–35 minutes, excluding optional reference slides.
Provenance: Consolidated from the four local documents listed on slide 24.
Product details reflect those documents and have not been independently
revalidated. Check installed versions and official documentation before
presenting specific controls. Numerical examples are explicitly illustrative.
-->

---

## 2. Optimize the completed task

- Define success through acceptance criteria and verification.
- Evaluate total cost, elapsed time, rework, and human intervention.
- Choose context, models, and delegation together.
- Prefer the fastest, least expensive approach that reliably meets the quality bar.

**A cheap request can become an expensive task if it requires repeated repair.**

<!-- Speaker notes: Cost per successfully completed and verified task is the
shared organizing principle. No isolated metric captures quality and efficiency.
Sources: model-selection-guidance.md §§1.2–1.3, 6;
cache-token-guidance.md §§1.8, 7; subagent-practices.md §§1.4, 1.9. -->

---

## 3. Four controls, four different jobs

| Control | Primary purpose | Important limit |
| --- | --- | --- |
| Context management | Keep relevant information available | Summaries can lose detail |
| Prompt caching | Reuse processing of unchanged input | Does not enlarge the context window |
| Model selection | Match capability and effort to the task | Stronger models still need clear context |
| Subagents | Isolate work and investigate independently | Add tokens and coordination overhead |

<!-- Speaker notes: These controls complement one another. A larger window,
cache hit, or additional agent does not by itself establish better results.
Sources: all four documents, common-practices sections. -->

---

## 4. Use one coordinated workflow

**Define → Discover → Decide → Implement → Verify → Checkpoint**

- Define requirements, constraints, and acceptance criteria.
- Discover relevant files; delegate independent investigations when useful.
- Select model capability and reasoning effort for the work ahead.
- Integrate changes, validate results, and save the state needed to continue.

<!-- Speaker notes: This workflow synthesizes the four documents. The primary
agent owns the complete outcome even when individual phases are delegated.
Sources: context-window-management.md §7; model-selection-guidance.md §1.4;
subagent-practices.md §§1.4, 7. -->

---

## 5. Treat context as working memory

- Start with the objective, constraints, and acceptance criteria.
- Discover files and dependencies before loading large amounts of content.
- Read the relevant code and specifications as questions arise.
- Keep tool output focused; save full logs as files when needed.

**Example:** Inspect the authentication module and its dependencies before expanding to the rest of the repository.

<!-- Speaker notes: Progressive, just-in-time retrieval keeps the ratio of useful
information high. Large context capacity does not guarantee effective reasoning
over irrelevant or contradictory input.
Sources: context-window-management.md §§1.1–1.2, 1.7;
model-selection-guidance.md §1.6. -->

---

## 6. Give information a durable home

| Information | Preferred home |
| --- | --- |
| Coding standards and essential test commands | Concise repository instructions |
| Architecture and interface contracts | ADRs, specifications, and schemas |
| Objective, decisions, progress, and next steps | Task plan or checkpoint |
| Implementation and complete logs | Source files and saved artifacts |
| Temporary exploration | Current agent context |

**Keep stable guidance separate from changing task state.**

<!-- Speaker notes: Common instruction files include AGENTS.md, CLAUDE.md, and
.github/copilot-instructions.md. Use scoped instructions where supported and
avoid duplicated rules. Stable, concise instructions support both context quality
and cache reuse. Sources: context-window-management.md §§1.3–1.5;
cache-token-guidance.md §§1.2, 3.2, 4.3. -->

---

## 7. Continue, compact, or start fresh?

| Situation | Action |
| --- | --- |
| Same task; relevant history remains manageable | Continue the session |
| Same task; exploration and logs crowd useful context | Save a checkpoint, then compact |
| Unrelated task or counterproductive history | Save any needed state, then start fresh |
| Resuming after a context transition | Read saved state and revalidate key assumptions |

**Compaction helps continuity; durable files preserve important detail.**

<!-- Speaker notes: Compact at coherent milestones when context pressure
justifies it. Compaction changes the reusable prefix and may reduce cache reuse;
context quality takes priority. Neither a summary nor a new session guarantees
recovery of every earlier detail.
Sources: context-window-management.md §§1.4, 1.8, 6–7;
cache-token-guidance.md §§1.5–1.6, 2.3, 3.4. -->

---

## 8. Prompt caching reuses an unchanged prefix

```text
Stable instructions → Stable project context → Existing history → New request
|--------- unchanged prefix: eligible for reuse ---------|       new input
```

- Keep reusable instructions and tool configuration stable when practical.
- Append changing information after stable material when you control the prompt.
- Early changes can reduce reuse of the content that follows.
- Managed assistants usually control prompt construction internally.

<!-- Speaker notes: This is a conceptual ordering, not a promise about a product's
exact prompt layout or cache eligibility. Avoid timestamps and changing status
inside stable instructions. Editing document order does not necessarily change
the assistant's underlying prompt order.
Source: cache-token-guidance.md §§1.1–1.4, 3.1–3.3. -->

---

## 9. Preserve useful reuse

- Continue related work in the same session when its context remains useful.
- Avoid unnecessary model and runtime changes.
- Account for cache expiration and any cache-write charges.
- Compact or reset when irrelevant history outweighs continuity.

**Do not assume different models or separate agents share a cache.**

<!-- Speaker notes: Useful phase-specific model changes remain justified when
quality or total task cost improves. Cache compatibility and retention depend
on provider, model, and runtime. CLI controls and API cache controls differ.
Sources: cache-token-guidance.md §§1.5–1.7, 5, 7;
model-selection-guidance.md §1.4. -->

---

## 10. Illustrative caching economics

**20,000 stable tokens reused across 10 requests**

| Scenario | Cost in uncached-input-token equivalents |
| --- | ---: |
| No caching: 10 × 20,000 | 200,000 |
| First write: 20,000 × 1.25 | 25,000 |
| Nine reads: 9 × 20,000 × 0.10 | 18,000 |
| Total with caching | **43,000** |

**78.5% lower processing cost for this stable input alone.**

*Assumes one cache write and nine valid reads at the stated multipliers. Excludes dynamic input, output, and other charges.*

<!-- Speaker notes: This reproduces the source's arithmetic, not a current
cross-provider price quote. Expiration, rewritten prefixes, and different pricing
change the result. A high hit rate on unnecessary input is still wasteful.
Source: cache-token-guidance.md §§4.1, 6. -->

---

## 11. Match model capability to the work

| Work | Starting capability |
| --- | --- |
| File discovery, simple edits, boilerplate | Fast and economical |
| Routine features, tests, ordinary refactoring | Balanced |
| Difficult bugs, architecture, cross-module changes | Advanced reasoning |
| Security-sensitive or high-risk changes | Strong capability plus independent review |

**Use repository results to refine these starting points.**

<!-- Speaker notes: These are qualitative tiers rather than fixed model rankings.
Task risk, clarity, repository familiarity, and acceptance criteria matter.
Sources: model-selection-guidance.md §§1.1, 1.8, 6. -->

---

## 12. Escalate for a reason

1. Check requirements, relevant context, and the observed failure.
2. Increase reasoning effort where supported and useful.
3. Escalate model capability for persistent failures or harder reasoning.
4. Validate the result against the original acceptance criteria.

**Triggers:** repeated incorrect changes, failed tests, missed dependencies, or unresolved design trade-offs.

<!-- Speaker notes: Model selection and reasoning effort are separate controls.
Higher effort can increase latency and consumption. Start difficult work with
appropriate capability rather than requiring failure on a smaller model first.
Sources: model-selection-guidance.md §§1.2, 1.7, 3.3, 6. -->

---

## 13. Delegate when the boundary adds value

| Good candidates | Keep with the primary agent |
| --- | --- |
| Independent implementation, test, or security investigations | Small, straightforward edits |
| Context-heavy exploration | Tightly dependent next steps |
| Independent review or alternative designs | Final architecture and integration decisions |
| Independent modules with clear file ownership | Shared-file changes without isolation |

**Delegate by responsibility and context, rather than by agent count.**

<!-- Speaker notes: Context isolation protects the primary conversation but does
not necessarily lower total token use. Parallel work helps only where dependency
and integration costs permit it.
Sources: subagent-practices.md §§1.1–1.3, 1.9;
context-window-management.md §1.6. -->

---

## 14. Make every delegation a clear contract

```text
Objective: Review authentication changes for correctness and security.
Scope: Current diff and relevant authentication dependencies.
Constraints: Read-only; do not modify files.
Deliverable: Prioritized findings with file references and failure scenarios.
Completion: Report evidence, checks performed, and unresolved questions.
```

- Specify the expected result before the investigation begins.
- Request concise findings; keep exploratory output in the worker's context.

<!-- Speaker notes: For implementation, add file ownership, acceptance criteria,
and required validation. Ask agents to distinguish tests passed from tests not
run. A bounded contract improves both execution and the usefulness of the return.
Sources: subagent-practices.md §§1.1, 1.5, 1.8. -->

---

## 15. Coordinate parallel work deliberately

- Start with two or three independent workers when useful.
- Prefer read-only investigation before dividing implementation.
- Establish file ownership; use isolated worktrees or branches where appropriate.
- Give each worker only the tools and access its role needs.
- Keep reconciliation, integration, and final validation with the primary agent.

<!-- Speaker notes: Two or three is a starting heuristic, not a universal limit.
Increase concurrency only when measured benefit justifies the overhead.
Isolation reduces edit conflicts; it does not eliminate integration work.
Sources: subagent-practices.md §§1.2, 1.4, 1.6–1.7, 7. -->

---

## 16. Separate implementation from verification

**Implement → Independent review → Resolve findings → Validate integration**

- Require concrete defects, evidence, and plausible failure scenarios.
- Check claims against code, requirements, and relevant tests.
- Different model families may add perspective; agreement is not proof.
- A finished subagent assignment does not establish a finished task.

<!-- Speaker notes: Review should consider correctness, regressions,
maintainability, security, and missing tests as appropriate to the change.
Independent agent review does not replace human review requirements.
Sources: subagent-practices.md §§1.3–1.4, 1.8;
model-selection-guidance.md §1.5. -->

---

## 17. GitHub Copilot: distinguish IDE and CLI workflows

- **Model choice:** Use an appropriate Auto option or an explicit model for predictable behavior and comparison.
- **VS Code context:** Inspect the context indicator; compact or open a new chat as needed.
- **Delegation:** The sources describe `#runSubagent` in VS Code and `/fleet` in Copilot CLI.
- **Reusable guidance:** Keep Copilot instructions concise; define recurring specialists under `.github/agents/` where supported.

<!-- Speaker notes: The source recommends Auto—Balance for everyday work where
that tier is available. Chat and inline-completion model choices are separate.
Do not assume Auto routing preserves a single model's cache. Interface, plan, and
installed-version differences matter; confirm exact commands before demonstration.
Sources: model-selection-guidance.md §2; context-window-management.md §2;
cache-token-guidance.md §2; subagent-practices.md §2. -->

---

## 18. Codex: preserve guidance and centralize integration

- **Model choice:** Begin with the recommended coding model and an appropriate reasoning level.
- **Context:** Keep hierarchical `AGENTS.md` files concise; save progress at phase boundaries.
- **Session controls:** The sources describe `/status` and `/compact` in Codex CLI.
- **Delegation:** Assign bounded investigations; keep integration and validation centralized.

<!-- Speaker notes: The source proposes medium effort for routine coding and
higher effort for difficult tasks where supported. AGENTS.md provides guidance;
it does not itself enable subagents. Codex CLI and custom API/SDK orchestration
have different configuration surfaces. Confirm installed runtime capabilities.
Sources: model-selection-guidance.md §3; context-window-management.md §3;
cache-token-guidance.md §3; subagent-practices.md §3. -->

---

## 19. Claude Code: use focused instructions and specialists

- **Model choice:** The sources suggest Haiku for lightweight work, Sonnet for routine coding, and Opus for harder reasoning.
- **Context:** Keep `CLAUDE.md` focused; save durable progress before a reset.
- **Session controls:** The sources describe `/context`, `/compact`, `/clear`, `/model`, and `/cost`.
- **Delegation:** Define specialists in `.claude/agents/` with appropriate models and tool restrictions.

<!-- Speaker notes: Available versions, aliases, usage reporting, and model
settings depend on account and runtime. A skill provides reusable procedure;
a subagent supplies a separate execution context. Ordinary subagents and agent
teams are distinct capabilities. Consider cache-duration settings only when the
supported billing arrangement and reuse pattern justify them.
Sources: model-selection-guidance.md §4; context-window-management.md §4;
cache-token-guidance.md §4; subagent-practices.md §4. -->

---

## 20. Example: investigate a cross-module bug

1. **Define:** Capture the failure, reproduction steps, and acceptance criteria.
2. **Discover:** Give bounded, read-only implementation and test investigations to separate agents.
3. **Decide:** Reconcile evidence; correct missing context and select suitable reasoning capability.
4. **Implement and verify:** Apply a focused fix, obtain independent review, and run relevant tests.
5. **Checkpoint:** Save decisions and results; compact if continuing, or start fresh for unrelated work.

<!-- Speaker notes: This is a synthesized workflow example, not an empirical
case study. Keep the stable instruction prefix consistent where practical, but
accept cache disruption when a model change or compaction serves the task.
Use cheaper workers only when they can reliably perform the assigned work.
Sources: all four documents, reusable policies and recommended approaches. -->

---

## 21. Measure outcomes and refine the policy

| Measure | What it helps assess |
| --- | --- |
| Acceptance criteria, test results, review defects | Correctness and completeness |
| Total usage cost, iterations, and rework | Cost per verified task |
| Elapsed time and human intervention | Practical productivity |
| Cached reads, writes, uncached input, and output | Sources of processing cost |
| Duplicate work and integration conflicts | Delegation overhead |

**Compare approaches on representative repository tasks with the same acceptance criteria.**

<!-- Speaker notes: Cache hit rate = cached input tokens / total input tokens.
Use the accounting definitions exposed by the provider. High hit rate, low token
price, or many reviewer findings are diagnostic signals, not success criteria.
Periodically reevaluate model and delegation choices as capabilities change.
Sources: cache-token-guidance.md §§1.8, 7;
model-selection-guidance.md §§1.3, 1.8, 6;
subagent-practices.md §§1.6, 1.8. -->

---

## 22. Optional reference: checkpoint template

```markdown
# Task checkpoint
- Objective and acceptance criteria:
- Decisions and rationale:
- Relevant files and changes:
- Tests and checks: passed / failed / not run
- Known issues and unresolved questions:
- Next actions:
```

**Write the checkpoint before compaction, handoff, or a session reset.**

<!-- Speaker notes: Include enough evidence and artifact references for the next
session to reconstruct state. Revalidate assumptions against the repository.
Source: context-window-management.md §§1.4–1.5, 6. -->

---

## 23. Optional reference: compact subagent return

```markdown
# Delegated result
- Summary and completion status:
- Files examined or modified:
- Findings: priority, evidence, file references, failure scenario
- Tests and checks: passed / failed / not run
- Remaining risks and open questions:
- Recommended next action:
```

**The primary agent verifies the report and reconciles it with the other work.**

<!-- Speaker notes: Return useful evidence rather than raw search output or
entire logs. Preserve detailed artifacts separately when they are needed.
Source: subagent-practices.md §§1.4–1.5, 1.8, 6. -->

---

## 24. Optional reference: source documents

| Local source | Material consolidated |
| --- | --- |
| [Cached-token guidance](cache-token-guidance.md) | Stable prefixes, cache trade-offs, illustrative economics |
| [Context-window management](context-window-management.md) | Progressive retrieval, checkpoints, compaction, durable state |
| [Model-selection guidance](model-selection-guidance.md) | Capability tiers, effort, escalation, evaluation |
| [Subagent practices](subagent-practices.md) | Delegation contracts, isolation, concurrency, integration |

*This deck synthesizes the supplied documents. Product commands, model availability, pricing, and configuration depend on the installed version, plan, and runtime.*

<!-- Speaker notes: Source mappings throughout the deck refer to section numbers
in these documents. Product recommendations are source-derived guidance rather
than a newly verified compatibility matrix. -->

---

## 25. Optional reference: official documentation

**Links carried forward from the source documents**

- **GitHub / VS Code:** [AI usage and caching](https://docs.github.com/en/copilot/tutorials/optimize-ai-usage), [agent context](https://code.visualstudio.com/docs/agents/concepts/context), [model selection](https://docs.github.com/en/copilot/concepts/models/auto-model-selection).
- **OpenAI:** [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching), [reasoning effort](https://developers.openai.com/api/docs/guides/reasoning), [Codex development workflows](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex).
- **Claude Code:** [Costs and usage](https://code.claude.com/docs/en/costs), [memory and instructions](https://code.claude.com/docs/en/memory), [custom subagents](https://code.claude.com/docs/en/sub-agents).

<!-- Speaker notes: These links preserve the original documents' reference trail;
they were not independently opened or checked during consolidation. -->
