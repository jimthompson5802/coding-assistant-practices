# Token counters

Two Python programs report token usage from local Codex and GitHub Copilot logs.
Both require Python 3 and use only the standard library; no packages need to be
installed. Run the commands below from this repository's directory.

## Codex

```bash
python3 count_codex_tokens.py ~/.codex/sessions
```

The program recursively searches for `.jsonl` files at any directory depth. For
each file, it takes the last non-null `total_token_usage` from a `token_count`
record, then sums those cumulative counts across files.

To count a smaller directory, such as one day's sessions:

```bash
python3 count_codex_tokens.py ~/.codex/sessions/2026/10/18
```

## GitHub Copilot in VS Code

On macOS, run:

```bash
python3 count_copilot_tokens.py \
  "$HOME/Library/Application Support/Code/User/workspaceStorage"
```

Copilot debug logs are nested beneath this directory:

```text
<workspace-id>/GitHub.copilot-chat/debug-logs/<session-id>/*.jsonl
```

The program recursively searches the supplied directory and processes JSONL files
only beneath a directory named `debug-logs`. It sums individual `llm_request`
records, including those in main, subagent, and title-generation logs. You can
also pass a specific workspace or `debug-logs` directory to narrow the report.
Keep paths containing spaces in quotes.

Only usage present in the debug logs is counted. This report covers recorded
chat/agent requests; it does not establish coverage for inline code completions.
If no matching logs exist, the program reports zeros.

## Understanding the output

Both programs identify the coding assistant, then print comma-separated counts
and a percentage to two decimal places. For example, Copilot output looks like:

```text
coding_assistant: GitHub Copilot (VS Code)
input_tokens: 100,000
cached_input_tokens: 80,000
output_tokens: 2,000
reasoning_output_tokens: unavailable
total_tokens: 102,000
cached_input_percentage: 80.00%
```

The Codex program starts with `coding_assistant: Codex`.

| Field | Meaning |
| --- | --- |
| `input_tokens` | Reported input tokens, including cached input |
| `cached_input_tokens` | Reported input tokens reused from cache |
| `output_tokens` | Reported output tokens |
| `reasoning_output_tokens` | Recorded reasoning count for Codex; `unavailable` for Copilot |
| `total_tokens` | Recorded total for Codex; input + output for Copilot |
| `cached_input_percentage` | Cached input ÷ input × 100, using the reported totals |

Cached input is already included in input tokens, so do not add it again when
calculating total usage. Both programs display `0.00%` when input totals are zero.

If Copilot requests have missing or invalid counters, the program sums the
available values and prints a warning to stderr with the number of affected
requests for each counter. The percentage still uses the available totals and
may be incomplete. Missing reasoning data is shown as `unavailable`, not zero.

## Help and errors

```bash
python3 count_codex_tokens.py --help
python3 count_copilot_tokens.py --help
```

Each program requires an existing directory. Unreadable files and malformed JSON
cause an unsuccessful exit without printing partial totals. JSON errors include
the file path and line number.
