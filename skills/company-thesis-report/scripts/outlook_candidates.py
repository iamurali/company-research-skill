#!/usr/bin/env python3
"""Pull forward-looking candidate quotes from an extracted transcript/deck text.

Writes a small JSON file the agent can curate into facts/outlook.json.
Never a substitute for reading the whole transcript into the model.

Usage:
  python3 outlook_candidates.py transcript.txt out.json [--max-per-bucket 40]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

NEAR = re.compile(
    r"\b(this quarter|next quarter|coming quarter|near term|current year|FY\s?\d{2}|guidance|"
    r"order book|expected to|we expect|we guide|run.?rate)\b",
    re.I,
)
MEDIUM = re.compile(
    r"\b(next\s+(6|nine|9|12)\s+months|medium term|by\s+FY|H[12]\s*FY|capex|"
    r"commission(?:ing)?|expansion|ramp[- ]?up|pipeline)\b",
    re.I,
)
LONG = re.compile(
    r"\b(long term|multi[- ]year|over the next\s+\d+\s+years|vision|structural|"
    r"by 20\d{2}|target of|aspir(?:e|ation))\b",
    re.I,
)
QUOTEISH = re.compile(r"\b(will|expect|target|aim|plan|guidance|should|outlook)\b", re.I)


def bucket_line(line: str) -> str | None:
    if not QUOTEISH.search(line) and not NEAR.search(line):
        return None
    if len(line.strip()) < 40:
        return None
    if LONG.search(line):
        return "long"
    if MEDIUM.search(line):
        return "medium"
    if NEAR.search(line):
        return "near"
    return "near"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--max-per-bucket", type=int, default=40)
    args = ap.parse_args()

    lines = args.source.read_text(encoding="utf-8", errors="replace").splitlines()
    out = {"near": [], "medium": [], "long": [], "source": str(args.source)}
    seen = {k: set() for k in out if k != "source"}

    for i, line in enumerate(lines, 1):
        b = bucket_line(line)
        if not b:
            continue
        text = " ".join(line.split())
        if text in seen[b] or len(out[b]) >= args.max_per_bucket:
            continue
        seen[b].add(text)
        out[b].append({"line": i, "text": text[:500]})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(
        f"wrote {args.output} "
        f"near={len(out['near'])} medium={len(out['medium'])} long={len(out['long'])}"
    )


if __name__ == "__main__":
    main()
