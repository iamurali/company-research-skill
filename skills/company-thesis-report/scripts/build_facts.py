#!/usr/bin/env python3
"""Merge query hits + lens schema into facts packs (skeleton writer).

This script does deterministic scaffolding; the agent fills narrative fields
from the returned snippets without reading whole source files.

Usage:
  python3 build_facts.py <slug> --lens banks \
      --hits hits.json \
      [--meta meta.json] \
      [--init-empty]

Writes/merges under ~/.company-research/<slug>/facts/.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
CACHE_ROOT = Path.home() / ".company-research"

UNIVERSAL = [
    "meta", "decision", "sources_completeness", "sector", "value_chain", "outlook",
    "customers", "milestones",
    "financials", "financials_quarterly", "earnings_bridge", "working_capital",
    "cash_flow", "kpi_scorecard", "segments", "demand", "operations",
    "capital_allocation", "valuation", "peers", "moats", "risks", "thesis",
    "management_scorecard", "governance", "technicals", "quotes", "sources_index",
    "sector_overlay",
]


def empty_pack(name: str) -> dict:
    defaults = {
        "meta": {},
        "decision": {
            "action": "",
            "confidence": "",
            "horizon": "",
            "entry_zone": "",
            "invalidation": "",
            "key_debate": "",
            "one_paragraph_why": "",
            "confirm_thesis": [],
            "kill_thesis": [],
            "alternative_thesis": {
                "side": "",
                "claim": "",
                "why_it_could_be_right": "",
                "why_we_reject_or_partial": "",
            },
            "position_framing": "",
            "next_checkpoint": "",
        },
        "sources_completeness": {
            "status": "fail",
            "latest_concall": "",
            "prior_concalls": [],
            "latest_deck": "",
            "deck_gap": "",
            "annual_report": "",
            "annual_report_gap": "",
            "latest_pr": "",
            "peers_n": 0,
            "missing": [
                "latest_concall",
                "prior_concalls (≥3)",
                "annual_report or annual_report_gap",
                "peers_n ≥3",
            ],
            "notes": [],
        },
        "sector": {"lens_id": "", "sector_value_chain_stages": [], "notes": []},
        "value_chain": {"stages": [], "backward_integration_note": "", "sources": []},
        "outlook": {"near": [], "medium": [], "long": [], "guidance_history": []},
        "customers": {"items": [], "concentration": {}, "customer_guidance_checks": []},
        "milestones": {"items": []},
        "financials": {
            "period_type": "annual",
            "rows": [],
            "cagr": {},
            "regime_notes": [],
            "balance_sheet_anomaly": {"found": False, "notes": []},
            "lens_metric_cards": [],
        },
        "financials_quarterly": {
            "rows": [],
            "min_quarters_expected": 8,
            "seasonality_note": "",
        },
        "earnings_bridge": {
            "latest_period": "",
            "vs": "both",
            "headline": "",
            "drivers": [],
            "narrative": "",
            "sources": [],
        },
        "working_capital": {
            "rows": [],
            "cfo_vs_pat": [],
            "commentary": "",
            "sources": [],
        },
        "cash_flow": {"rows": [], "quality_notes": [], "sources": []},
        "kpi_scorecard": {
            "period_columns": [],
            "rows": [],
            "min_kpis_expected": 6,
            "min_periods": 4,
            "gap": "",
        },
        "segments": {"tables": [], "gap": ""},
        "demand": {"material": False, "rows": [], "count_vs_size_note": "", "gap": ""},
        "operations": {"footprint": [], "raw_materials": {}, "capacity": {}, "tam": {}},
        "capital_allocation": {
            "dividends": [],
            "buybacks": [],
            "ma": [],
            "reinvestment_notes": "",
            "roic_or_roce_story": "",
            "grade": "unknown",
            "sources": [],
        },
        "valuation": {
            "method": "",
            "inputs": {},
            "implied_growth": {"label": "", "assumption": "", "note": ""},
            "scenarios": [],
            "notes": [],
            "sources": [],
        },
        "peers": {"columns": [], "rows": []},
        "moats": {"items": []},
        "risks": {"items": []},
        "thesis": {"items": []},
        "management_scorecard": {
            "guidance_delivery": [],
            "capital_allocation_grade": "",
            "key_person_risk": "",
            "governance_flags": [],
            "overall_note": "",
            "sources": [],
        },
        "governance": {
            "shareholding": [],
            "ratings": [],
            "litigation": [],
            "fund_raises": [],
            "leadership_changes": [],
        },
        "technicals": {"items": [], "gap": ""},
        "quotes": {"items": []},
        "sources_index": {"items": []},
        "sector_overlay": {
            "lens_id": "",
            "deep_dive_blocks": [],
            "metric_cards": [],
            "query_hits": {},
        },
    }
    return defaults.get(name, {})


def load_lens(lens_id: str) -> dict:
    path = SKILL_ROOT / "sectors" / lens_id / "metrics.schema.json"
    if not path.exists():
        raise SystemExit(f"unknown lens: {lens_id} ({path})")
    return json.loads(path.read_text(encoding="utf-8"))


def facts_dir(slug: str) -> Path:
    return CACHE_ROOT / slug / "facts"


def read_json(path: Path, default: dict) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug")
    ap.add_argument("--lens", required=True)
    ap.add_argument("--hits", type=Path, default=None, help="JSON map of query_key -> [snippets]")
    ap.add_argument("--meta", type=Path, default=None)
    ap.add_argument("--init-empty", action="store_true")
    args = ap.parse_args()

    lens = load_lens(args.lens)
    fdir = facts_dir(args.slug)
    fdir.mkdir(parents=True, exist_ok=True)

    if args.init_empty:
        for name in UNIVERSAL:
            p = fdir / f"{name}.json"
            if not p.exists():
                write_json(p, empty_pack(name))

    meta = read_json(fdir / "meta.json", empty_pack("meta"))
    if args.meta:
        meta.update(json.loads(args.meta.read_text(encoding="utf-8")))
    meta["sector_lens_id"] = args.lens
    meta["slug"] = args.slug
    write_json(fdir / "meta.json", meta)

    sector = read_json(fdir / "sector.json", empty_pack("sector"))
    sector["lens_id"] = args.lens
    sector["how_sector_is_valued"] = lens.get("valuation_method", "")
    sector["sector_value_chain_stages"] = lens.get("sector_value_chain_stages", [])
    sector["primer_used"] = True
    write_json(fdir / "sector.json", sector)

    overlay = read_json(fdir / "sector_overlay.json", empty_pack("sector_overlay"))
    overlay["lens_id"] = args.lens
    overlay["deep_dive_title"] = lens.get("deep_dive_title", "Sector Deep-Dive")
    overlay["valuation_method"] = lens.get("valuation_method", "")
    overlay["peer_columns"] = lens.get("peer_columns", [])
    overlay["metric_defs"] = lens.get("metrics", [])
    overlay["deep_dive_prompts"] = lens.get("deep_dive_prompts", [])
    if args.hits and args.hits.exists():
        overlay["query_hits"] = json.loads(args.hits.read_text(encoding="utf-8"))
    else:
        overlay.setdefault("query_hits", {})
        # seed empty keys so the agent knows what to query
        for k in lens.get("query_keys", []):
            overlay["query_hits"].setdefault(k, [])
    write_json(fdir / "sector_overlay.json", overlay)

    valuation = read_json(fdir / "valuation.json", empty_pack("valuation"))
    if not valuation.get("method"):
        valuation["method"] = lens.get("valuation_method", "")
        write_json(fdir / "valuation.json", valuation)

    peers = read_json(fdir / "peers.json", empty_pack("peers"))
    if not peers.get("columns"):
        peers["columns"] = lens.get("peer_columns", [])
        write_json(fdir / "peers.json", peers)

    print(json.dumps({
        "slug": args.slug,
        "lens": args.lens,
        "facts_dir": str(fdir),
        "deep_dive_title": overlay["deep_dive_title"],
        "query_keys": lens.get("query_keys", []),
        "packs": sorted(p.name for p in fdir.glob("*.json")),
    }, indent=2))


if __name__ == "__main__":
    main()
