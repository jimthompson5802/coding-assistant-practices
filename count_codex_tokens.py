#!/usr/bin/env python3
"""Sum the final cumulative token usage from each JSONL file in a directory."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory to search recursively")
    args = parser.parse_args()
    directory = args.directory.expanduser()
    if not directory.is_dir():
        parser.error(f"not a directory: {directory}")

    totals = dict.fromkeys(
        (
            "input_tokens",
            "cached_input_tokens",
            "output_tokens",
            "reasoning_output_tokens",
            "total_tokens",
        ),
        0,
    )
    path = directory
    try:
        for path in directory.rglob("*.jsonl"):
            last_usage = None
            with path.open(encoding="utf-8") as source:
                for line_number, line in enumerate(source, start=1):
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as error:
                        parser.exit(1, f"{path}:{line_number}: {error.msg}\n")
                    payload = record.get("payload") or {}
                    if payload.get("type") == "token_count":
                        info = payload.get("info") or {}
                        usage = info.get("total_token_usage")
                        if usage is not None:
                            last_usage = usage
            if last_usage is not None:
                for key in totals:
                    totals[key] += last_usage.get(key, 0)
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"{path}: {error}\n")

    print("coding_assistant: Codex")
    for key, value in totals.items():
        print(f"{key}: {value:,}")
    cached_percentage = (
        totals["cached_input_tokens"] / totals["input_tokens"] * 100
        if totals["input_tokens"]
        else 0
    )
    print(f"cached_input_percentage: {cached_percentage:.2f}%")


if __name__ == "__main__":
    main()
