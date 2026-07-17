---
name: company-thesis-report
description: >
  Build a decision-grade equity research PDF for Indian listed companies. Prefer when
  the user asks for company research, equity thesis, BUY/HOLD/AVOID, concall analysis,
  or a deeper company report. Uses a fixed report spine, one routed sector lens, and
  a hard depth floor — reports must be thick enough to decide invest / not.
---

# Company thesis report

Build a **decision-grade** research PDF. The user must be able to **invest or not**
from the report alone — not from headings and summaries.

**Quality beats token savings.** Thin reports are failures even if cheap to produce.

## Hard depth floor (non-negotiable)

Aligned with [references/depth-checklist.md](references/depth-checklist.md) (blocks A–F).

A finished report fails if **any** of these is missing:

1. **Investment decision** — BUY / HOLD / AVOID with conviction, entry zone, invalidation,
   horizon, position framing, key debate, alternative thesis, confirm/kill.
2. **Source completeness** — latest concall + **≥3 prior** quarter extracts + AR (or
   documented gap) + ≥3 peers. See `facts/sources_completeness.json`.
3. **Multi-quarter earnings bridge** — ≥8 quarters with YoY/QoQ + latest beat/miss drivers.
4. **Working-capital deep dive** — debtor days trend + CFO vs PAT (≥3y) + commentary.
5. **KPI scorecard** — ≥6 KPIs via `kpi_table()`; prefer ≥4 periods or `gap_reason`.
6. **Management scorecard** — ≥2 sourced guidance-delivery rows; capital allocation; key-person.
7. **Outlook guidance history** — ≥3 entries in `outlook.guidance_history` from prior prints.
8. **Segment / geography mix** — when disclosed.
9. **Peer table** — ≥3 real peers with valuation **and** ≥1 operating/growth column.
10. **Scenarios** — bull/base/bear with assumptions + **EPS×multiple math** (`scenario_value.py`).
11. **Charts** — ≥3 figures; value chain via `flow_diagram` only.
12. **Sources** — cited; URLs in appendix.

**Ship rule:** `python scripts/validate_depth.py --slug <slug>` must exit 0 before PDF.
If it fails, deepen packs — do not ship.

## Non-negotiable rules

1. **One spine** — [references/report-format.md](references/report-format.md).
2. **One sector lens** — [references/sector-router.md](references/sector-router.md); load only that lens.
3. **Value chain = visual HTML** — never ASCII/code.
4. **No headings-only / no empty shells** — never empty `timeline()`; use `kpi_table()` not `str(dict)`.
5. **Cache on disk** — `~/.company-research/<slug>/`.
6. **Prefer tools** for math, PDF text, HTML/PDF assembly.
7. **Decision-first** — open with the call.

## Inputs

- Company name or ticker (NSE/BSE)
- Optional: as-of date, emphasis, peer list, force-refresh

## Workflow

### 0. Setup

```bash
pip install matplotlib weasyprint pypdf rank_bm25 beautifulsoup4 lxml -q
python skills/company-thesis-report/scripts/freshness.py --slug <slug>
```

Workspace: `~/.company-research/<slug>/{sources,facts,output}/`

### 1. Classify sector (once)

Use [references/sector-router.md](references/sector-router.md). Write `facts/sector.json`.
Load **only** `sectors/<lens-id>/`.

```bash
python skills/company-thesis-report/scripts/build_facts.py <slug> --lens <lens-id> --init-empty
```

### 2. Ingest (depth mode) — Source Completeness Gate

Follow [references/source-routing.md](references/source-routing.md).

**Before drafting**, fill `facts/sources_completeness.json` and set `status: pass` only when:

| Required | Rule |
|----------|------|
| Latest concall | Full transcript/captions on disk |
| Prior concalls/PRs | **≥3** prior quarter extracts (guidance evolution) |
| Latest PR | On disk |
| Deck | Path **or** `deck_gap` reason |
| Annual report | Path **or** `annual_report_gap` (prefer always attempt) |
| Peers | `peers_n` ≥ 3 with filled peer pages |

If incomplete → keep fetching. Do not draft a ship PDF.

### 3. Build deep facts packs

Enrich packs per [references/facts-schemas.md](references/facts-schemas.md).

Depth packs that must be rich: `financials_quarterly`, `earnings_bridge`,
`working_capital`, `kpi_scorecard`, `management_scorecard`, `capital_allocation`,
`outlook` (incl. `guidance_history`), `valuation` (incl. scenario math), `decision`,
`sources_completeness`.

### 4. Analysis depth

Answer before drafting: what changed over 4–8 quarters; is cash real; what is priced in;
what would make the other side right; what must be true in 12 months.

### 5. Draft using HTML helpers (not ad-hoc)

Use `html_helpers.py` only for structure:

- `timeline(items)` — dicts or tuples; **never empty**
- `kpi_table(scorecard)` — period grid; **never** put `str(dict)` in `data_table`
- `flow_diagram`, `verdict_box`, `data_table`, `card_grid`

Valuation scenarios:

```bash
python skills/company-thesis-report/scripts/scenario_value.py \
  --price 548 --pe 22.8 --bull-growth 0.17 --base-growth 0.12 --bear-growth 0.06
```

Merge `math_note` into `facts/valuation.json` scenarios.

### 6. Charts

≥3 charts from facts (price/financials/WC or valuation).

### 7. Validate — then assemble

```bash
python skills/company-thesis-report/scripts/validate_depth.py --slug <slug>
# must exit 0

python skills/company-thesis-report/scripts/assemble_pdf.py \
  --html ~/.company-research/<slug>/output/report.html \
  --out  ~/.company-research/<slug>/output/<Name>_report.pdf
```

`assemble_pdf.py` runs `smoke_check_html` (rejects empty timeline shells / dict garbage).

### 8. Self-audit

Re-read [references/depth-checklist.md](references/depth-checklist.md). Copy final PDF to
artifacts when delivering. Do not commit sample PDFs to the repo.

## Sector lenses

Router: [references/sector-router.md](references/sector-router.md)  
Each lens: `sectors/<lens-id>/{LENS.md,metrics.schema.json}`

## Tools

| Script | Use |
|--------|-----|
| `freshness.py` | Cache status |
| `pdf_to_text.py` / `query_source.py` | Extract / grep |
| `outlook_candidates.py` | Forward-looking quotes |
| `build_facts.py` | Pack scaffold + lens |
| `validate_depth.py` | **Ship gate** |
| `scenario_value.py` | EPS × multiple bands |
| `forward_pe.py` / `capacity_utilization.py` | Math helpers |
| `html_helpers.py` | Render primitives + smoke check |
| `assemble_pdf.py` | HTML → PDF |
| `charts.py` | Figures |

## Anti-patterns

- Shipping when `validate_depth.py` fails
- One-quarter transcript only (no guidance history)
- Empty `timeline()` / headings-only sections
- `data_table` cells containing Python dicts
- Valuation bands without math_note
- Peer table with only P/E
- ASCII value chains / multiple sector lenses
- Committing `output/` sample reports
