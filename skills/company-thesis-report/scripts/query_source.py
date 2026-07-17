#!/usr/bin/env python3
"""Query an extracted source .txt without loading the whole file into the agent context.

Usage:
  python3 query_source.py SOURCE.txt KEYWORD [KEYWORD...] [--context 3] [--max-hits 20]
  python3 query_source.py SOURCE.txt --bm25 "order book guidance" --top-k 5

Prints line ranges + snippets only.
"""

from __future__ import annotations

import argparse
import pickle
import re
import sys
from pathlib import Path


def grep_hits(lines: list[str], keywords: list[str], context: int, max_hits: int) -> list[dict]:
    pats = [re.compile(re.escape(k), re.I) for k in keywords]
    hits = []
    for i, line in enumerate(lines):
        if any(p.search(line) for p in pats):
            lo = max(0, i - context)
            hi = min(len(lines), i + context + 1)
            hits.append({
                "line": i + 1,
                "start": lo + 1,
                "end": hi,
                "snippet": "".join(lines[lo:hi]).rstrip(),
            })
            if len(hits) >= max_hits:
                break
    return hits


def bm25_hits(path: Path, query: str, top_k: int) -> list[dict]:
    try:
        from rank_bm25 import BM25Okapi
    except ImportError as exc:
        raise SystemExit(
            "rank_bm25 required for --bm25: pip install rank_bm25 --break-system-packages"
        ) from exc

    cache = path.with_suffix(path.suffix + ".bm25.pkl")
    text = path.read_text(encoding="utf-8", errors="replace")
    # chunk ~40 lines
    raw_lines = text.splitlines(keepends=True)
    chunks = []
    meta = []
    size = 40
    for i in range(0, max(1, len(raw_lines)), size):
        piece = raw_lines[i:i + size]
        chunks.append("".join(piece))
        meta.append((i + 1, min(len(raw_lines), i + size)))

    if cache.exists() and cache.stat().st_mtime >= path.stat().st_mtime:
        tokenized = pickle.loads(cache.read_bytes())
    else:
        tokenized = [re.findall(r"[a-z0-9%]+", c.lower()) for c in chunks]
        cache.write_bytes(pickle.dumps(tokenized))

    bm25 = BM25Okapi(tokenized)
    scores = bm25.get_scores(re.findall(r"[a-z0-9%]+", query.lower()))
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    out = []
    for i in ranked:
        if scores[i] <= 0:
            continue
        start, end = meta[i]
        out.append({
            "line": start,
            "start": start,
            "end": end,
            "score": round(float(scores[i]), 3),
            "snippet": chunks[i][:1200].rstrip(),
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path)
    ap.add_argument("keywords", nargs="*", help="Literal keywords for grep mode")
    ap.add_argument("--context", type=int, default=3)
    ap.add_argument("--max-hits", type=int, default=20)
    ap.add_argument("--bm25", default=None, help="BM25 query string")
    ap.add_argument("--top-k", type=int, default=5)
    args = ap.parse_args()

    if not args.source.exists():
        raise SystemExit(f"missing source: {args.source}")

    if args.bm25:
        hits = bm25_hits(args.source, args.bm25, args.top_k)
    else:
        if not args.keywords:
            raise SystemExit("provide KEYWORDs or --bm25")
        lines = args.source.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        hits = grep_hits(lines, args.keywords, args.context, args.max_hits)

    if not hits:
        print("NO_HITS")
        return

    for h in hits:
        score = f" score={h['score']}" if "score" in h else ""
        print(f"--- lines {h['start']}-{h['end']} (match~{h['line']}){score} ---")
        print(h["snippet"])
        print()


if __name__ == "__main__":
    main()
