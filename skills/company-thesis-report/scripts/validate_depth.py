#!/usr/bin/env python3
"""Validate depth floor + source completeness before shipping a PDF.

Usage:
  python3 validate_depth.py --slug newgen
  python3 validate_depth.py --slug newgen --html ~/.company-research/newgen/output/report.html

Exit 0 = ship-eligible (warnings allowed).
Exit 1 = hard failures — do not assemble PDF.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

CACHE_ROOT = Path.home() / ".company-research"


def load(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def nonempty(x: Any) -> bool:
    if x is None:
        return False
    if isinstance(x, (str, list, dict)):
        return bool(x)
    return True


def count_period_keys(row: dict) -> int:
    periods = row.get("periods")
    if periods is None:
        periods = row.get("values")
    if isinstance(periods, dict):
        return sum(1 for v in periods.values() if v not in (None, "", "—", "-"))
    return 0


def validate_slug(slug: str, html_path: Path | None = None) -> tuple[list[str], list[str]]:
    """Return (failures, warnings)."""
    fdir = CACHE_ROOT / slug / "facts"
    failures: list[str] = []
    warnings: list[str] = []

    if not fdir.exists():
        return [f"facts dir missing: {fdir}"], []

    def need(name: str) -> dict | None:
        data = load(fdir / f"{name}.json")
        if data is None:
            failures.append(f"missing pack: {name}.json")
        return data

    # --- A. Source completeness ---
    sc = need("sources_completeness")
    if sc is not None:
        status = (sc.get("status") or "").lower()
        if status != "pass":
            missing = sc.get("missing") or []
            failures.append(
                "sources_completeness.status != pass"
                + (f" missing={missing}" if missing else f" status={status!r}")
            )
        if not sc.get("latest_concall"):
            failures.append("A: latest_concall required")
        prior = sc.get("prior_concalls") or []
        if len(prior) < 3:
            failures.append(
                f"A: prior_concalls need ≥3 extracts for guidance evolution (have {len(prior)})"
            )
        if not sc.get("annual_report") and not sc.get("annual_report_gap"):
            failures.append("A: annual_report path or annual_report_gap required")
        peers_n = sc.get("peers_n")
        if peers_n is not None and int(peers_n) < 3:
            failures.append(f"A: peers_n={peers_n} < 3")
        if not sc.get("latest_deck") and not sc.get("deck_gap"):
            warnings.append("A: no latest_deck / deck_gap noted")

    # --- B. Decision ---
    dec = need("decision")
    if dec is not None:
        for k in ("action", "confidence", "horizon", "one_paragraph_why",
                  "key_debate", "position_framing", "next_checkpoint"):
            if not nonempty(dec.get(k)):
                failures.append(f"B: decision.{k} empty")
        if len(dec.get("confirm_thesis") or []) < 3:
            failures.append("B: confirm_thesis needs ≥3 items")
        if len(dec.get("kill_thesis") or []) < 3:
            failures.append("B: kill_thesis needs ≥3 items")
        alt = dec.get("alternative_thesis") or {}
        if not nonempty(alt.get("claim")) or not nonempty(alt.get("why_it_could_be_right")):
            failures.append("B: alternative_thesis incomplete")

    # --- C. Financial depth ---
    fq = need("financials_quarterly")
    if fq is not None:
        nrows = len(fq.get("rows") or [])
        if nrows < 8:
            failures.append(f"C: financials_quarterly rows={nrows} < 8")
        if not fq.get("seasonality_note"):
            warnings.append("C: seasonality_note empty")

    eb = need("earnings_bridge")
    if eb is not None:
        if not nonempty(eb.get("narrative")) or len(eb.get("drivers") or []) < 2:
            failures.append("C: earnings_bridge needs narrative + ≥2 drivers")

    wc = need("working_capital")
    if wc is not None:
        if len(wc.get("rows") or []) < 3:
            failures.append("C: working_capital.rows need ≥3 periods")
        if len(wc.get("cfo_vs_pat") or []) < 3:
            failures.append("C: working_capital.cfo_vs_pat need ≥3 years")
        if not nonempty(wc.get("commentary")):
            failures.append("C: working_capital.commentary empty")

    fin = load(fdir / "financials.json")
    if fin is not None and len(fin.get("regime_notes") or []) < 1:
        warnings.append("C: financials.regime_notes empty")

    ca = load(fdir / "capital_allocation.json")
    if ca is not None and not nonempty(ca.get("roic_or_roce_story")) and ca.get("grade") in (None, "", "unknown"):
        warnings.append("C: capital_allocation thin")

    # --- D. KPI / ops / management ---
    kpi = need("kpi_scorecard")
    if kpi is not None:
        rows = kpi.get("rows") or []
        if len(rows) < 6:
            failures.append(f"D: kpi_scorecard rows={len(rows)} < 6")
        sparse = 0
        dict_as_string = 0
        for r in rows:
            n = count_period_keys(r)
            if n < 4 and not r.get("gap_reason"):
                sparse += 1
            # detect anti-pattern: values stored as a stringified dict
            vals = r.get("values")
            if isinstance(vals, str) and ("{" in vals or "&#x27;" in vals):
                dict_as_string += 1
            if isinstance(vals, dict) and r.get("periods") is None:
                # legacy ok if dict — but prefer periods; warn if <4
                pass
        if sparse > max(2, len(rows) // 2):
            failures.append(
                f"D: kpi_scorecard: {sparse}/{len(rows)} rows have <4 periods "
                "without gap_reason"
            )
        if dict_as_string:
            failures.append("D: kpi_scorecard has stringified dict values")

    mgmt = need("management_scorecard")
    if mgmt is not None:
        gd = mgmt.get("guidance_delivery") or []
        if len(gd) < 2:
            failures.append("D: management_scorecard.guidance_delivery need ≥2")
        unsourced = [g for g in gd if not g.get("source")]
        if unsourced:
            warnings.append(f"D: {len(unsourced)} guidance_delivery rows lack source")

    outlook = load(fdir / "outlook.json")
    if outlook is not None:
        gh = outlook.get("guidance_history") or []
        if len(gh) < 3:
            failures.append(
                f"D: outlook.guidance_history need ≥3 (have {len(gh)}) "
                "— mine prior quarters"
            )

    # --- E. Peers / valuation ---
    peers = need("peers")
    if peers is not None:
        rows = [r for r in (peers.get("rows") or []) if not _is_placeholder_peer(r)]
        if len(rows) < 3:
            failures.append(f"E: peers need ≥3 real rows (have {len(rows)})")
        cols = [c.lower() for c in (peers.get("columns") or [])]
        if cols and not any(
            any(tok in c for tok in ("growth", "roe", "roce", "margin", "opm", "sales", "debtor", "attrition"))
            for c in cols
        ):
            failures.append("E: peers.columns need ≥1 operating/growth metric (not PE-only)")

    val = need("valuation")
    if val is not None:
        ig = val.get("implied_growth") or {}
        if not nonempty(ig.get("assumption")):
            failures.append("E: valuation.implied_growth.assumption empty")
        scenarios = val.get("scenarios") or []
        if len(scenarios) < 3:
            failures.append(f"E: valuation.scenarios need ≥3 (have {len(scenarios)})")
        for s in scenarios:
            if not s.get("assumptions") and not s.get("growth"):
                failures.append(f"E: scenario {s.get('name')} missing assumptions/growth")
            if not s.get("math_note") and not (s.get("eps_or_pat") and s.get("multiple")):
                warnings.append(
                    f"E: scenario {s.get('name')} lacks math_note / eps×multiple bridge"
                )

    # --- HTML smoke (optional) ---
    if html_path is None:
        cand = CACHE_ROOT / slug / "output"
        for name in ("report.html", f"{slug}_report.html"):
            p = cand / name
            if p.exists():
                html_path = p
                break
        # common Newgen name
        for p in sorted(cand.glob("*.html")) if cand.exists() else []:
            html_path = p
            break

    if html_path and html_path.exists():
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from html_helpers import smoke_check_html
        import re
        html = html_path.read_text(encoding="utf-8", errors="replace")
        for problem in smoke_check_html(html):
            failures.append(f"F/production: HTML smoke — {problem}")

        # --- Prose / research-memo gates (writing-quality.md) ---
        text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
        text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
        plain = re.sub(r"<[^>]+>", " ", text)
        words = len(plain.split())
        paras = re.findall(r"<p[^>]*>(.*?)</p>", html, flags=re.I | re.S)
        lis = len(re.findall(r"<li\b", html, flags=re.I))
        n_p = len(paras)
        para_words = []
        for p in paras:
            pw = re.sub(r"<[^>]+>", " ", p)
            pw = re.sub(r"\s+", " ", pw).strip()
            if pw:
                para_words.append(len(pw.split()))
        avg_p = sum(para_words) / max(len(para_words), 1)
        li_ratio = lis / max(n_p, 1)

        if words < 3500:
            failures.append(
                f"F/prose: body ~{words} words < 3500 — tip-sheet density, not research memo"
            )
        if avg_p < 35:
            failures.append(
                f"F/prose: avg paragraph ~{avg_p:.0f} words < 35 — expand analytical read-throughs"
            )
        if li_ratio > 2.5:
            failures.append(
                f"F/prose: li/p ratio {li_ratio:.1f} > 2.5 — too bullet-linear / tip-like"
            )

        tip_patterns = [
            r"accumulate on dips",
            r"avoid chasing",
            r"satellite\s*/\s*wait",
            r"trim above",
            r"position framing",
            r"buy the dip",
        ]
        low = plain.lower()
        tip_hits = [p for p in tip_patterns if re.search(p, low)]
        if tip_hits:
            failures.append(
                "F/prose: tip-speak banned in research voice — " + ", ".join(tip_hits)
            )

        # Heuristic: financial section should have a substantial paragraph near tables
        if "Financial Performance" in html or "11. Financial" in html:
            long_after = [w for w in para_words if w >= 60]
            if len(long_after) < 2:
                failures.append(
                    "F/prose: need ≥2 analytical paragraphs (≥60 words) — "
                    "post-table financial read-through missing"
                )

    return failures, warnings


def _is_placeholder_peer(row: dict) -> bool:
    if row.get("is_subject"):
        return False
    vals = row.get("values") or {}
    blob = " ".join(str(v) for v in vals.values()).lower()
    return "n/a" in blob and "this run" in blob


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--html", type=Path, default=None)
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    args = ap.parse_args()

    failures, warnings = validate_slug(args.slug, args.html)
    result = {
        "slug": args.slug,
        "pass": len(failures) == 0,
        "failures": failures,
        "warnings": warnings,
        "n_failures": len(failures),
        "n_warnings": len(warnings),
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"validate_depth: {args.slug}")
        if failures:
            print(f"FAIL ({len(failures)}):")
            for f in failures:
                print(f"  ✗ {f}")
        else:
            print("PASS — ship-eligible on pack checks")
        if warnings:
            print(f"WARNINGS ({len(warnings)}):")
            for w in warnings:
                print(f"  ! {w}")

    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
