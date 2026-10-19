#!/usr/bin/env python3
"""Sum recorded Copilot Chat/agent token usage from VS Code debug logs."""

import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory to search recursively")
    args = parser.parse_args()
    directory = args.directory.expanduser()
    if not directory.is_dir():
        parser.error(f"not a directory: {directory}")

    fields = {
        "input_tokens": "inputTokens",
        "cached_input_tokens": "cachedTokens",
        "output_tokens": "outputTokens",
    }
    totals = dict.fromkeys(fields, 0)
    missing = dict.fromkeys(fields, 0)
    path = directory
    try:
        for path in directory.rglob("*.jsonl"):
            if "debug-logs" not in path.parts[:-1]:
                continue
            with path.open(encoding="utf-8") as source:
                for line_number, line in enumerate(source, start=1):
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as error:
                        parser.exit(1, f"{path}:{line_number}: {error.msg}\n")
                    if not isinstance(record, dict) or record.get("type") != "llm_request":
                        continue
                    attrs = record.get("attrs")
                    if not isinstance(attrs, dict):
                        attrs = {}
                    for key, field in fields.items():
                        value = attrs.get(field)
                        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                            totals[key] += value
                        else:
                            missing[key] += 1
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"{path}: {error}\n")

    if any(missing.values()):
        counts = ", ".join(f"{key}={count:,}" for key, count in missing.items() if count)
        print(
            f"Warning: totals include available counters only; "
            f"requests with missing or invalid counters: {counts}",
            file=sys.stderr,
        )

    print("coding_assistant: GitHub Copilot (VS Code)")
    for key, value in totals.items():
        print(f"{key}: {value:,}")
    print("reasoning_output_tokens: unavailable")
    print(f"total_tokens: {totals['input_tokens'] + totals['output_tokens']:,}")
    percentage = (
        totals["cached_input_tokens"] / totals["input_tokens"] * 100
        if totals["input_tokens"]
        else 0
    )
    print(f"cached_input_percentage: {percentage:.2f}%")


if __name__ == "__main__":
    main()
