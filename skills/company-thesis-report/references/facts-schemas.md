# Facts pack schemas

Working state lives under `~/.company-research/<company_slug>/`:

```
sources/          # raw PDF/txt — never load whole files into model context
facts/            # small typed JSON packs — what the agent drafts from
index/            # optional BM25 / line maps
output/           # report.md + PDF
```

Draft **only** from facts packs (+ tiny grepped snippets). Empty field → honest gap.

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
  "one_paragraph_why": "",
  "confirm_thesis": [{"watch": "", "why_it_matters": ""}],
  "kill_thesis": [{"watch": "", "why_it_matters": ""}],
  "next_checkpoint": "e.g. Q2 FY27 results"
}
```


### `facts/sector.json`

Sector Context inputs (primer may be copied from the lens; market facts are sparse).

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

Company-specific stages for `flow_diagram()`.

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
  "guidance_history": []
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

```json
{
  "period_type": "annual|quarterly",
  "rows": [
    {"period": "", "revenue": null, "yoy_pct": null, "gross_margin_pct": null, "ebitda_margin_pct": null, "pbt": null, "pat": null, "pat_margin_pct": null}
  ],
  "cagr": {"revenue_3y": null, "revenue_5y": null, "pat_3y": null, "pat_5y": null},
  "balance_sheet_anomaly": {"found": false, "notes": []},
  "lens_metric_cards": [{"label": "", "value": "", "tone": ""}]
}
```

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

Commercial backlog / demand indicators (order book, AUM, subscribers, etc.).

```json
{
  "material": false,
  "metric_name": "",
  "rows": [{"as_of": "", "value": "", "basis": "", "composition": "", "source": ""}],
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

### `facts/valuation.json`

```json
{
  "method": "",
  "as_of_price": "",
  "as_of_date": "",
  "inputs": {},
  "result": "",
  "historical_median": "",
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

### `facts/governance.json`

```json
{
  "shareholding": [{"period": "", "promoter": null, "fii": null, "dii": null, "public": null}],
  "guidance_reliability": "",
  "ratings": [{"agency": "", "rating": "", "outlook": "", "date": "", "source": ""}],
  "litigation": [{"matter": "", "status": "", "source": ""}],
  "fund_raises": [{"date": "", "type": "", "amount": "", "investors": "", "source": ""}]
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

Curated quotes that made the report (traceability for Sources).

```json
{
  "items": [{"id": "", "quote": "", "doc": "", "date": "", "section": ""}]
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
