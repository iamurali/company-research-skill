# Facts pack schemas

Working state lives under `~/.company-research/<company_slug>/`:

```
sources/          # raw PDF/txt — never load whole files into model context
facts/            # small typed JSON packs — what the agent drafts from
index/            # optional BM25 / line maps
output/           # report.md + PDF
```

Draft **only** from facts packs (+ tiny grepped snippets). Empty field → honest gap.

**Depth rule:** packs below marked *(depth)* are required for a shippable report.
Thin `financials` without quarterly bridge / WC / KPI scorecard = fail the depth floor.

## Universal packs

### `facts/meta.json`

```json
{
  "company_name": "",
  "slug": "",
  "tickers": {"nse": "", "bse": ""},
  "exchanges": [],
  "sector_lens_id": "",
  "screener_industry": "",
  "situation": "",
  "badge_kind": "neutral",
  "report_date": "",
  "latest_results_date": "",
  "market_cap": "",
  "price": "",
  "fifty_two_week": "",
  "about": ""
}
```

### `facts/decision.json` *(required before draft)*

```json
{
  "action": "BUY|HOLD|AVOID|SELECTIVE_ACCUMULATE",
  "confidence": "high|medium|low",
  "horizon": "e.g. 12 months / next 2–3 quarters",
  "entry_zone": "",
  "invalidation": "",
  "key_debate": "",
  "one_paragraph_why": "",
  "confirm_thesis": [{"watch": "", "why_it_matters": ""}],
  "kill_thesis": [{"watch": "", "why_it_matters": ""}],
  "alternative_thesis": {
    "side": "bear|bull",
    "claim": "",
    "why_it_could_be_right": "",
    "why_we_reject_or_partial": ""
  },
  "position_framing": "core|satellite|wait|trim",
  "next_checkpoint": "e.g. Q2 FY27 results"
}
```

### `facts/sources_completeness.json` *(ship gate — block A)*

Set `status` to `pass` only when required fields are filled. `validate_depth.py` fails otherwise.

```json
{
  "status": "fail|pass",
  "latest_concall": "sources/q1fy27_transcript.txt",
  "prior_concalls": [
    "sources/q4fy26_transcript.txt",
    "sources/q3fy26_pr.txt",
    "sources/q2fy26_pr.txt"
  ],
  "latest_pr": "sources/q1fy27_pr.txt",
  "latest_deck": "sources/q1fy27_deck.pdf",
  "deck_gap": "",
  "annual_report": "sources/ar_fy26.pdf",
  "annual_report_gap": "",
  "peers_n": 3,
  "missing": [],
  "notes": []
}
```

Rules:

- `prior_concalls` length **≥3** (transcripts or PRs that support guidance history)
- Either `latest_deck` **or** non-empty `deck_gap`
- Either `annual_report` **or** non-empty `annual_report_gap`
- `peers_n` ≥ 3

### `facts/sector.json`

```json
{
  "lens_id": "",
  "primer_used": true,
  "how_sector_operates": "",
  "how_sector_is_valued": "",
  "competitive_intensity": "",
  "sector_value_chain_stages": [
    {"label": "Upstream", "detail": ""},
    {"label": "Industry core", "detail": ""},
    {"label": "Downstream", "detail": ""},
    {"label": "End market", "detail": ""}
  ],
  "notes": []
}
```

### `facts/value_chain.json`

```json
{
  "stages": [
    {"label": "Upstream", "detail": ""},
    {"label": "THE COMPANY", "detail": ""},
    {"label": "Downstream", "detail": ""},
    {"label": "End market", "detail": ""}
  ],
  "backward_integration_note": "",
  "sources": []
}
```

### `facts/outlook.json`

```json
{
  "near": [{"headline": "", "status": "Pending", "claim": "", "quote": "", "source": ""}],
  "medium": [],
  "long": [],
  "guidance_history": [
    {"period": "", "what_management_said": "", "what_happened": "", "source": ""}
  ]
}
```

Status values: `Pending` | `On Track` | `Delivered` | `Delayed` | `Missed`.

### `facts/customers.json`

```json
{
  "items": [{"name": "", "note": "", "source": ""}],
  "concentration": {"top_n": null, "pct": null, "source": ""},
  "customer_guidance_checks": []
}
```

### `facts/milestones.json`

```json
{
  "items": [
    {"date": "", "milestone": "", "status": "achieved|on-track|delayed|pending", "amount": "", "source": ""}
  ]
}
```

### `facts/financials.json`

Prefer splitting deep history into the dedicated packs below when large; this pack
remains the annual + summary home.

```json
{
  "period_type": "annual",
  "rows": [
    {"period": "", "revenue": null, "yoy_pct": null, "gross_margin_pct": null, "ebitda_margin_pct": null, "pbt": null, "pat": null, "pat_margin_pct": null}
  ],
  "cagr": {"revenue_3y": null, "revenue_5y": null, "pat_3y": null, "pat_5y": null},
  "regime_notes": [],
  "balance_sheet_anomaly": {"found": false, "notes": []},
  "lens_metric_cards": [{"label": "", "value": "", "tone": ""}]
}
```

### `facts/financials_quarterly.json` *(depth)*

```json
{
  "rows": [
    {
      "period": "Q1 FY27",
      "revenue": null,
      "yoy_pct": null,
      "qoq_pct": null,
      "ebitda_margin_pct": null,
      "pat": null,
      "pat_margin_pct": null,
      "note": ""
    }
  ],
  "min_quarters_expected": 8,
  "seasonality_note": ""
}
```

### `facts/earnings_bridge.json` *(depth)*

```json
{
  "latest_period": "",
  "vs": "YoY|QoQ|both",
  "headline": "beat|miss|inline",
  "drivers": [
    {"factor": "mix|volume|price|geo|one_off|other_income|opex|tax", "impact": "", "direction": "up|down", "source": ""}
  ],
  "narrative": "",
  "sources": []
}
```

### `facts/working_capital.json` *(depth)*

```json
{
  "rows": [
    {"period": "", "debtor_days": null, "inventory_days": null, "creditor_days": null, "ccc_days": null}
  ],
  "cfo_vs_pat": [
    {"period": "", "pat": null, "cfo": null, "note": ""}
  ],
  "commentary": "",
  "sources": []
}
```

### `facts/cash_flow.json` *(depth)*

```json
{
  "rows": [
    {"period": "", "cfo": null, "cfi": null, "cff": null, "fcf": null, "capex": null}
  ],
  "quality_notes": [],
  "sources": []
}
```

### `facts/kpi_scorecard.json` *(depth)*

Render with **`kpi_table(scorecard)`** only — never stringify dicts into `data_table` cells.

```json
{
  "period_columns": ["Jun25", "Sep25", "Dec25", "Mar26", "Jun26"],
  "rows": [
    {
      "metric": "Annuity (Cr)",
      "periods": {"Jun25": 220, "Sep25": 240, "Dec25": 245, "Mar26": 260, "Jun26": 254},
      "trend": "up|down|flat|volatile|seasonal",
      "implication": "",
      "gap_reason": "",
      "source": ""
    }
  ],
  "min_kpis_expected": 6,
  "min_periods": 4,
  "gap": ""
}
```

If a KPI has &lt;4 periods, set `gap_reason` (e.g. "only disclosed from Q1 FY27").

### `facts/segments.json`

```json
{
  "tables": [
    {"basis": "", "as_of": "", "rows": [{"segment": "", "revenue": "", "yoy": "", "margin": ""}]}
  ],
  "gap": ""
}
```

### `facts/demand.json`

```json
{
  "material": false,
  "metric_name": "",
  "rows": [{"as_of": "", "value": "", "basis": "", "composition": "", "source": ""}],
  "count_vs_size_note": "",
  "gap": ""
}
```

### `facts/operations.json`

```json
{
  "footprint": [{"location": "", "owned_leased": "", "detail": "", "source": ""}],
  "raw_materials": {"domestic_pct": null, "import_pct": null, "by_country": [], "source": ""},
  "capacity": {"unit": "", "installed": null, "utilized_pct": null, "notes": "", "source": ""},
  "tam": {"figure": "", "as_of": "", "source": "", "gap": ""}
}
```

### `facts/capital_allocation.json` *(depth)*

```json
{
  "dividends": [],
  "buybacks": [],
  "ma": [],
  "reinvestment_notes": "",
  "roic_or_roce_story": "",
  "grade": "A|B|C|D|unknown",
  "sources": []
}
```

### `facts/valuation.json`

Build scenario arithmetic with `scripts/scenario_value.py` and copy `math_note` / `eps_or_pat`.

```json
{
  "method": "",
  "as_of_price": "",
  "as_of_date": "",
  "inputs": {},
  "result": "",
  "historical_median": "",
  "implied_growth": {
    "label": "what market appears to price in",
    "assumption": "",
    "note": "back-of-envelope; labeled judgment"
  },
  "scenarios": [
    {
      "name": "bull|base|bear",
      "probability": null,
      "growth": "",
      "margin": "",
      "multiple": "",
      "eps_or_pat": "",
      "value": "",
      "math_note": "TTM EPS × (1+g) × multiple band = …",
      "assumptions": ""
    }
  ],
  "notes": [],
  "sources": []
}
```

### `facts/peers.json`

```json
{
  "columns": [],
  "rows": [{"name": "", "is_subject": false, "values": {}}]
}
```

### `facts/moats.json` / `facts/risks.json` / `facts/thesis.json`

```json
{"items": [{"text": "", "source": ""}]}
```

### `facts/management_scorecard.json` *(depth)*

```json
{
  "guidance_delivery": [
    {"period": "", "said": "", "delivered": "", "grade": "met|missed|mixed", "source": ""}
  ],
  "capital_allocation_grade": "",
  "key_person_risk": "",
  "governance_flags": [],
  "overall_note": "",
  "sources": []
}
```

### `facts/governance.json`

```json
{
  "shareholding": [{"period": "", "promoter": null, "fii": null, "dii": null, "public": null}],
  "guidance_reliability": "",
  "ratings": [{"agency": "", "rating": "", "outlook": "", "date": "", "source": ""}],
  "litigation": [{"matter": "", "status": "", "source": ""}],
  "fund_raises": [{"date": "", "type": "", "amount": "", "investors": "", "source": ""}],
  "leadership_changes": [{"date": "", "change": "", "source": ""}]
}
```

### `facts/technicals.json`

```json
{
  "as_of": "",
  "items": [{"label": "", "value": ""}],
  "gap": ""
}
```

### `facts/quotes.json`

```json
{
  "items": [{"id": "", "quote": "", "doc": "", "date": "", "section": ""}]
}
```

### `facts/sources_index.json`

```json
{
  "items": [
    {"id": 1, "title": "", "url": "", "supports": "", "retrieved": ""}
  ]
}
```

### `facts/sector_overlay.json`

Shape defined by the loaded lens `metrics.schema.json`. Always include:

```json
{
  "lens_id": "",
  "deep_dive_title": "",
  "deep_dive_blocks": [],
  "metric_cards": [],
  "valuation_method": "",
  "peer_columns": [],
  "query_hits": {}
}
```

## Freshness state

`facts/freshness.json` (also written by `scripts/freshness.py`):

```json
{
  "status": "no_state|up_to_date|new_quarter|force_full",
  "latest_seen": "",
  "last_processed": "",
  "price_at_last_run": ""
}
```
