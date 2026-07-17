#!/usr/bin/env python3
"""Capacity utilization helper.

Usage:
  python3 capacity_utilization.py --installed 100 --produced 72 --unit "fiber-km"
  python3 capacity_utilization.py --installed 100 --util-pct 72 --post-capex-installed 150
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--installed", type=float, required=True)
    ap.add_argument("--produced", type=float, default=None)
    ap.add_argument("--util-pct", type=float, default=None)
    ap.add_argument("--unit", default="")
    ap.add_argument("--post-capex-installed", type=float, default=None)
    args = ap.parse_args()

    if args.util_pct is not None:
        util = args.util_pct
        produced = args.installed * util / 100.0
    elif args.produced is not None:
        produced = args.produced
        util = (produced / args.installed * 100.0) if args.installed else None
    else:
        raise SystemExit("provide --produced or --util-pct")

    headroom = args.installed - produced if produced is not None else None
    post = None
    if args.post_capex_installed:
        post = {
            "installed": args.post_capex_installed,
            "implied_util_at_same_output_pct": round(produced / args.post_capex_installed * 100.0, 2)
            if produced is not None else None,
        }

    print(json.dumps({
        "unit": args.unit,
        "installed": args.installed,
        "produced": round(produced, 4) if produced is not None else None,
        "utilization_pct": round(util, 2) if util is not None else None,
        "headroom": round(headroom, 4) if headroom is not None else None,
        "post_capex": post,
    }, indent=2))


if __name__ == "__main__":
    main()
