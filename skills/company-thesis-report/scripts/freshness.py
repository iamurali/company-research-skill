#!/usr/bin/env python3
"""Freshness state for ~/.company-research/<slug>/.

Usage:
  python3 freshness.py <slug> --latest-seen YYYY-MM-DD [--force]
  python3 freshness.py <slug> --mark-processed YYYY-MM-DD [--price X]
  python3 freshness.py <slug> --status
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path.home() / ".company-research"


def cache_dir(slug: str) -> Path:
    return ROOT / slug


def facts_path(slug: str) -> Path:
    return cache_dir(slug) / "facts" / "freshness.json"


def load(slug: str) -> dict:
    p = facts_path(slug)
    if not p.exists():
        return {"status": "no_state", "latest_seen": "", "last_processed": "", "price_at_last_run": ""}
    return json.loads(p.read_text(encoding="utf-8"))


def save(slug: str, data: dict) -> None:
    p = facts_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def decide(slug: str, latest_seen: str, force: bool) -> dict:
    state = load(slug)
    if force:
        state["status"] = "force_full"
        state["latest_seen"] = latest_seen
        save(slug, state)
        return state
    if not state.get("last_processed"):
        state["status"] = "no_state"
        state["latest_seen"] = latest_seen
        save(slug, state)
        return state
    if latest_seen and latest_seen == state.get("last_processed"):
        state["status"] = "up_to_date"
        state["latest_seen"] = latest_seen
        save(slug, state)
        return state
    state["status"] = "new_quarter"
    state["latest_seen"] = latest_seen
    save(slug, state)
    return state


def mark(slug: str, processed: str, price: str) -> dict:
    state = load(slug)
    state["last_processed"] = processed
    state["latest_seen"] = processed
    if price:
        state["price_at_last_run"] = price
    state["status"] = "up_to_date"
    state["marked_on"] = date.today().isoformat()
    save(slug, state)
    return state


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug")
    ap.add_argument("--latest-seen", default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--mark-processed", default=None)
    ap.add_argument("--price", default="")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    if args.status:
        print(json.dumps(load(args.slug), indent=2))
        return
    if args.mark_processed:
        print(json.dumps(mark(args.slug, args.mark_processed, args.price), indent=2))
        return
    if not args.latest_seen and not args.force:
        raise SystemExit("provide --latest-seen YYYY-MM-DD (or --status / --mark-processed)")
    print(json.dumps(decide(args.slug, args.latest_seen or "", args.force), indent=2))


if __name__ == "__main__":
    main()
