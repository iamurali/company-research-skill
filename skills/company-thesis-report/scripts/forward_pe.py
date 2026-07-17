#!/usr/bin/env python3
"""Deterministic forward-PE helper (only when the loaded lens asks for PE-style valuation).

Usage:
  python3 forward_pe.py --price 120 --shares-cr 10 --revenue-cr 500 \
      --pat-margin-pct 12 --pe-multiple 25
"""

from __future__ import annotations

import argparse
import json


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--shares-cr", type=float, required=True, help="Shares outstanding in crore")
    ap.add_argument("--revenue-cr", type=float, required=True, help="Forward revenue INR cr")
    ap.add_argument("--pat-margin-pct", type=float, required=True)
    ap.add_argument("--pe-multiple", type=float, default=None)
    args = ap.parse_args()

    market_cap = args.price * args.shares_cr
    pat = args.revenue_cr * (args.pat_margin_pct / 100.0)
    eps = pat / args.shares_cr if args.shares_cr else None
    fwd_pe = (args.price / eps) if eps else None
    implied_price = (eps * args.pe_multiple) if (eps and args.pe_multiple) else None

    print(json.dumps({
        "market_cap_cr": round(market_cap, 2),
        "forward_pat_cr": round(pat, 2),
        "forward_eps": round(eps, 2) if eps else None,
        "forward_pe": round(fwd_pe, 2) if fwd_pe else None,
        "implied_price_at_multiple": round(implied_price, 2) if implied_price else None,
    }, indent=2))


if __name__ == "__main__":
    main()
