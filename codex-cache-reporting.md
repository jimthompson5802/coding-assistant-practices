# Codex conversation

## User

how can I find amount of input/cached/output tokens used by codex

## Assistant

I’ll check the local Codex setup and its documentation for where token usage is reported. I’m using the openai-docs skill.

## Activity

    $ cat /Users/jim/.codex/skills/.system/openai-docs/SKILL.md
    ---
    name: "openai-docs"
    description: "Use for Codex models/pricing, scheduled tasks, skills, settings, setup, troubleshooting, customization, automations, and self-knowledge—including 'you,' 'your,' 'this app,' or 'this coding agent' when they refer to Codex—and for OpenAI APIs/products and ChatGPT Work. Also use for model choice/migration, prompting, SDKs, Responses, Realtime, agents, evals, and Chat/Work/Codex comparisons. Do not use for generic app/software tasks that merely mention Codex."
    metadata:
      short-description: "Codex models/pricing, scheduled tasks, skills, settings, setup, troubleshooting, and self-knowledge; OpenAI APIs and ChatGPT Work. 'You'/'this app' means Codex only."
    ---
    
    # OpenAI Docs
    
    Provide current, cited OpenAI product, API, model, and Codex guidance. Read zero or one primary reference.
    
    **First substantive action:** Search the user's exact requested official OpenAI documentation topic and any explicitly named model using a concise, topic-specific query of 2-6 essential terms. When an already-available direct official documentation search and page-retrieval capability is present, use it first: search, then fetch or open the matching official page before general web search. Otherwise, immediately use official-domain web search, then actually open or fetch the relevant official page. Complete this source order before reading a reference, inspecting local or repository files, running a Codex manual or model resolver, drafting a plan, or answering from memory. Use the actual fetched page, not a search snippet or an unopened link. If one official search or page does not establish the answer, search another appropriate official domain and actually open or fetch the result. Preserve the exact requested model; never substitute a newer model.
    
    **Only exception:** An explicitly requested, genuinely broad, cross-topic Codex setup, orientation, or system-map synthesis may use the manual first when shell execution and an allowed temporary cache are available. A specific Codex feature, setting, command, error, model, or requested citation remains docs-first. Mixed Chat/Work/Codex comparisons are official documentation questions, not manual-first Codex requests.
    
    For generic software tasks, answer the software task directly. OpenAI implementation, debugging, SDK, API, prompting, agent, and eval requests are not generic.
    
    For a straightforward factual or citation-only request, follow the source order and do not read a route reference. This includes straightforward API facts, ChatGPT Work or mixed Chat/Work/Codex comparisons, model tiers, aliases, Pro mode, reasoning settings, factual migration baselines, and narrow Codex facts. Prioritize `learn.chatgpt.com` for ChatGPT Work.
    
    ## Choose one primary route
    
    Use the first matching route, and read its reference only when the requested task needs that specialized workflow:
    
    - **Explicitly requested local documentation integration:** Read [integration guidance](references/mcp-diagnostics.md) only when the user explicitly requests that local integration.
    - **Model migration, upgrades, or model-specific prompting:** Read [model-migration.md](references/model-migration.md) for actual migration planning, implementation, dynamic target resolution, or prompt changes. Preserve an explicitly requested target.
    - **Model selection and comparisons:** Read [model-selection.md](references/model-selection.md) only when nuanced current, latest, default, cost, latency, quality, or modality tradeoffs need more guidance. Do not run a migration resolver for selection alone.
    - **Product, API, ChatGPT Work, and mixed Chat/Work/Codex documentation:** Read [official-docs.md](references/official-docs.md) only when fetched official pages leave source selection, API schemas, or the requested implementation unresolved. This route is not manual-first.
    - **Explicitly broad Codex setup, orientation, or cross-topic synthesis:** Read [codex-self-knowledge.md](references/codex-self-knowledge.md) when the eligible Codex manual or deeper Codex procedures are needed.
    
    Read at most one primary reference. Do not open every route, bundled model guide, or helper script. Read a supporting reference or run a helper only when the chosen workflow demonstrably needs it.
    
    ## Source and execution boundaries
    
    - Search, open, fetch, and cite only `developers.openai.com`, `platform.openai.com`, and `learn.chatgpt.com`. Cite the page that supports the claim. State uncertainty when official sources do not establish pricing, availability, account access, limits, or behavior.
    - Preserve an explicitly requested model for selection, migration, and prompting. Resolve an unspecified latest or current migration target only after searching and fetching current official guidance.
    - Use `references/latest-model.md` only as a disclosed fallback after current official model guidance does not answer the question. Read `references/upgrading-to-gpt-6-astra.md` only for an actual, requested GPT-6 migration; read `references/prompting-guide.md` only for requested prompting work.
    - Before building, running, editing, debugging, or testing an API-backed app or tool, use `openai-platform-api-key` first when available. Documentation, conceptual examples, model selection, and read-only guidance do not require an API key.
    - Say "OpenAI Docs" or "official OpenAI documentation" in user-facing answers. Keep exact official citations and examples concise.
    ✓ • 0ms

## Activity

    $ command -v codex
    /Users/jim/.nvm/versions/node/v26.3.1/bin/codex
    ✓ • 0ms

## Activity

    Searched the web for site:developers.openai.com codex token usage cached input output json

## Activity

    Searched the web for site:developers.openai.com/codex "cached_input_tokens", site:developers.openai.com/codex "/status" tokens

## Activity

    $ codex --help
    WARNING: proceeding, even though we could not create PATH aliases: Operation not permitted (os error 1)
    Codex CLI
    
    If no subcommand is specified, options will be forwarded to the interactive CLI.
    
    Usage: codex [OPTIONS] [PROMPT]
           codex [OPTIONS] <COMMAND> [ARGS]
    
    Commands:
      agents            Browse all agent sessions on the shared local app-server daemon
      exec              Run Codex non-interactively [aliases: e]
      review            Run a code review non-interactively
      login             Manage login
      logout            Remove stored authentication credentials
      mcp               Manage external MCP servers for Codex
      plugin            Manage Codex plugins
      app-server        [experimental] Run the app server or related tooling
      remote-control    [experimental] Manage the app-server daemon with remote control enabled
      app               Launch the Desktop app (opens the app installer if missing)
      completion        Generate shell completion scripts
      update            Update Codex to the latest version
      doctor            Diagnose local Codex installation, config, auth, and runtime health
      sandbox           Run commands within a Codex-provided sandbox
      debug             Debugging tools
      apply             Apply the latest diff produced by Codex agent as a `git apply` to your local
                        working tree [aliases: a]
      resume            Resume a previous interactive session (picker by default; use --last to continue
                        the most recent)
      queue             Queue a message for an existing session
      archive           Archive a saved session by id or session name
      delete            Permanently delete a saved session by id or session name
      migrate-rollouts  Inspect or migrate legacy local sessions to paginated thread history
      unarchive         Unarchive a saved session by id or session name
      fork              Fork a previous interactive session (picker by default; use --last to fork the
                        most recent)
      cloud             [EXPERIMENTAL] Browse tasks from Codex Cloud and apply changes locally
      exec-server       [EXPERIMENTAL] Run the standalone exec-server service
      features          Inspect feature flags
      help              Print this message or the help of the given subcommand(s)
    
    Arguments:
      [PROMPT]
              Optional user prompt to start the session
    
    Options:
      -c, --config <key=value>
              Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
              Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
              as TOML. If it fails to parse as TOML, the raw string is used as a literal.
    
              Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
              shell_environment_policy.inherit=all`
    
          --enable <FEATURE>
              Enable a feature (repeatable). Equivalent to `-c features.<name>=true`
    
          --disable <FEATURE>
              Disable a feature (repeatable). Equivalent to `-c features.<name>=false`
    
          --remote <ADDR>
              Connect the TUI to a remote app server endpoint.
    
              Accepted forms: `ws://host:port`, `wss://host:port`, `unix://`, or `unix://PATH`.
    
          --remote-auth-token-env <ENV_VAR>
              Name of the environment variable containing the bearer token to send to a remote app
              server websocket
    
          --strict-config
              Error out when config.toml contains fields that are not recognized by this version of
              Codex
    
      -i, --image <FILE>...
              Optional image(s) to attach to the initial prompt
    
      -m, --model <MODEL>
              Model the agent should use
    
          --oss
              Use open-source provider
    
          --local-provider <OSS_PROVIDER>
              Specify which local provider to use (lmstudio or ollama). If not specified with --oss,
              will use config default or show selection
    
      -p, --profile <CONFIG_PROFILE_V2>
              Layer $CODEX_HOME/<name>.config.toml on top of the base user config
    
      -s, --sandbox <SANDBOX_MODE>
              Select the sandbox policy to use when executing model-generated shell commands
    
              [possible values: read-only, workspace-write, danger-full-access]
    
          --approve-for-me
              Route approval requests through automatic review using the workspace-write sandbox
    
          --dangerously-bypass-approvals-and-sandbox
              Skip all confirmation prompts and execute commands without sandboxing. EXTREMELY
              DANGEROUS. Intended solely for running in environments that are externally sandboxed
    
          --dangerously-bypass-hook-trust
              Run enabled hooks without requiring persisted hook trust for this invocation. DANGEROUS.
              Intended only for automation that already vets hook sources
    
      -C, --cd <DIR>
              Tell the agent to use the specified directory as its working root
    
          --worktree
              Run the session in a new managed Git worktree
    
          --add-dir <DIR>
              Additional directories that should be writable alongside the primary workspace
    
      -a, --ask-for-approval <APPROVAL_POLICY>
              Configure when the model requires human approval before executing a command
    
              Possible values:
              - on-request: The model decides when to ask the user for approval
              - never:      Never ask for user approval Execution failures are immediately returned to
                the model
    
          --search
              Enable live web search. When enabled, the native Responses `web_search` tool is available
              to the model (no per‑call approval)
    
          --no-alt-screen
              Disable alternate screen mode
    
              Runs the TUI in inline mode, preserving terminal scrollback history.
    
          --no-daemon
              Run without the shared background server, even if it is already running
    
      -h, --help
              Print help (see a summary with '-h')
    
      -V, --version
              Print version
    ✓ • 0ms

## Activity

    Opened https://learn.chatgpt.com/docs/slash-commands

## Activity

    $ python3 - <<'PY'
        from pathlib import Path
        import json
        root=Path.home()/'.codex/sessions'
        files=sorted(root.rglob('*.jsonl'), key=lambda p:p.stat().st_mtime, reverse=True)[:3]
        for p in files:
         last=None
         for line in p.open():
          try: x=json.loads(line)
          except ValueError: continue
          payload=x.get('payload',{})
          if payload.get('type')=='token_count': last=payload.get('info')
         print(p)
         print(json.dumps(last))
        PY
    /Users/jim/.codex/sessions/2026/10/18/rollout-2026-10-18T19-15-29-01a1514c-7b06-75b2-ac9d-0a6eab33b02d.jsonl
    {"total_token_usage": {"input_tokens": 69800, "cached_input_tokens": 54784, "cache_write_input_tokens": 0, "output_tokens": 290, "reasoning_output_tokens": 0, "total_tokens": 70090}, "last_token_usage": {"input_tokens": 26705, "cached_input_tokens": 22272, "cache_write_input_tokens": 0, "output_tokens": 101, "reasoning_output_tokens": 0, "total_tokens": 26806}, "model_context_window": 475000}
    /Users/jim/.codex/sessions/2026/10/18/rollout-2026-10-18T14-48-30-01a15058-0d4a-7751-b8d9-6123054e19a0.jsonl
    {"total_token_usage": {"input_tokens": 335304, "cached_input_tokens": 294144, "cache_write_input_tokens": 0, "output_tokens": 2887, "reasoning_output_tokens": 91, "total_tokens": 338191}, "last_token_usage": {"input_tokens": 51841, "cached_input_tokens": 50944, "cache_write_input_tokens": 0, "output_tokens": 60, "reasoning_output_tokens": 0, "total_tokens": 51901}, "model_context_window": 475000}
    /Users/jim/.codex/sessions/2026/10/18/rollout-2026-10-18T12-54-50-01a14fef-fbbe-7601-a232-cd649a76701c.jsonl
    {"total_token_usage": {"input_tokens": 18761995, "cached_input_tokens": 18362496, "cache_write_input_tokens": 0, "output_tokens": 64253, "reasoning_output_tokens": 31778, "total_tokens": 18826248}, "last_token_usage": {"input_tokens": 209065, "cached_input_tokens": 208896, "cache_write_input_tokens": 0, "output_tokens": 98, "reasoning_output_tokens": 0, "total_tokens": 209163}, "model_context_window": 475000}
    ✓ • 360ms

## Assistant

You can get the exact breakdown from **Codex’s local session logs**. I confirmed your logs contain these fields.

For an existing session, run:

```bash
jq -s '
  [.[] | select(.payload.type == "token_count")
   | .payload.info.total_token_usage | select(. != null)]
  | last
' ~/.codex/sessions/2026/10/18/rollout-2026-10-18T05-53-37-01a14e6e-5b08-7f33-8a30-196fcb1f6a5c.jsonl
```

This shows cumulative session totals:

| Field | Meaning |
|---|---|
| `input_tokens` | All input, including cached input |
| `cached_input_tokens` | Input reused from cache |
| `output_tokens` | Generated output, including reasoning |
| `reasoning_output_tokens` | Reasoning portion of output |

**Uncached input = `input_tokens - cached_input_tokens`.** Use the last cumulative record; adding all records would double-count usage.

For **new command-line runs**, capture usage directly:

```bash
codex exec --json "your task" \
  | jq 'select(.type == "turn.completed") | .usage'
```

The `turn.completed` event includes input, cached input, and output counts. See the [official OpenAI documentation](https://learn.chatgpt.com/docs/non-interactive-mode#make-output-machine-readable).
