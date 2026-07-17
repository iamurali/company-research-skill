#!/usr/bin/env python3
"""Deterministic bull/base/bear value bands from PAT/EPS × multiple.

Usage:
  python3 scenario_value.py --pat 314 --shares 14.1 --scenarios scenarios.json
  python3 scenario_value.py --eps 22.06 --price 548 --pe 22.8 \\
      --bull-growth 0.16 --base-growth 0.12 --bear-growth 0.06

Prints JSON with math_note on each scenario for valuation.json.
"""

from __future__ import annotations

import argparse
import json
import sys


def band(eps: float, lo_mult: float, hi_mult: float) -> dict:
    lo = round(eps * lo_mult, 1)
    hi = round(eps * hi_mult, 1)
    return {
        "eps": round(eps, 2),
        "multiple_lo": lo_mult,
        "multiple_hi": hi_mult,
        "value_lo": lo,
        "value_hi": hi,
        "value": f"~Rs {lo:.0f}–{hi:.0f}",
        "math_note": f"EPS {eps:.2f} × {lo_mult}–{hi_mult}x = Rs {lo:.0f}–{hi:.0f}",
    }


def forward_eps(ttm_eps: float, growth: float, years: float = 1.0) -> float:
    return ttm_eps * ((1.0 + growth) ** years)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--eps", type=float, help="TTM EPS (Rs)")
    ap.add_argument("--pat", type=float, help="TTM PAT (Rs Cr)")
    ap.add_argument("--shares", type=float, help="Shares (Cr) for PAT→EPS")
    ap.add_argument("--price", type=float, default=None)
    ap.add_argument("--pe", type=float, default=None)
    ap.add_argument("--bull-growth", type=float, default=0.17)
    ap.add_argument("--base-growth", type=float, default=0.12)
    ap.add_argument("--bear-growth", type=float, default=0.06)
    ap.add_argument("--bull-pe", type=float, nargs=2, default=[26.0, 28.0])
    ap.add_argument("--base-pe", type=float, nargs=2, default=[20.0, 23.0])
    ap.add_argument("--bear-pe", type=float, nargs=2, default=[14.0, 17.0])
    ap.add_argument("--horizon-years", type=float, default=1.0)
    args = ap.parse_args()

    if args.eps is not None:
        ttm_eps = args.eps
    elif args.pat is not None and args.shares:
        ttm_eps = args.pat / args.shares
    elif args.price and args.pe:
        ttm_eps = args.price / args.pe
    else:
        raise SystemExit("need --eps, or --pat + --shares, or --price + --pe")

    scenarios = []
    for name, g, pe in [
        ("bull", args.bull_growth, args.bull_pe),
        ("base", args.base_growth, args.base_pe),
        ("bear", args.bear_growth, args.bear_pe),
    ]:
        feps = forward_eps(ttm_eps, g, args.horizon_years)
        b = band(feps, pe[0], pe[1])
        scenarios.append({
            "name": name,
            "growth": f"{g*100:.0f}% EPS growth over {args.horizon_years:g}y",
            "multiple": f"{pe[0]}–{pe[1]}x",
            "eps_or_pat": f"fwd EPS {b['eps']}",
            "value": b["value"],
            "math_note": (
                f"TTM EPS {ttm_eps:.2f} × (1+{g:.0%})^{args.horizon_years:g} "
                f"= {feps:.2f}; × {pe[0]}–{pe[1]}x → {b['value']}"
            ),
            "assumptions": f"growth={g:.0%}, multiples={pe[0]}–{pe[1]}x",
        })

    out = {
        "ttm_eps": round(ttm_eps, 2),
        "spot": {"price": args.price, "pe": args.pe},
        "scenarios": scenarios,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
