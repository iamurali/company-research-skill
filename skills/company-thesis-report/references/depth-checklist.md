# Depth checklist — research-grade (ship gate)

Human checklist + machine gate. Run:

```bash
python skills/company-thesis-report/scripts/validate_depth.py --slug <slug>
```

If more than two **human** items fail, or the script exits non-zero, **do not ship**.

## A. Evidence depth (lookback) — `sources_completeness`

- [ ] **Latest quarter fully mined:** results PR + investor deck (or `deck_gap`) + **full concall**
- [ ] **Trailing lookback:** last **4–6** quarters of concalls/PRs (≥3 prior extracts on disk)
- [ ] **Annual depth:** latest AR queried **or** `annual_report_gap` with reason; required when segment/WC/governance gaps remain
- [ ] **Primary over aggregator:** material numbers from screener tables, filings, transcript/deck
- [ ] **`facts/sources_completeness.json` → `status: pass`**

## B. Decision depth — `decision.json`

- [ ] Action + confidence + **time horizon**
- [ ] **Key debate** in one sentence
- [ ] Confirm / kill lists **numeric or observable** (next 1–2 prints)
- [ ] **Position framing** (core / satellite / wait / trim)
- [ ] **Alternative thesis** (other side + why reject/partial)

## C. Financial depth

- [ ] 5–10y annual history **with regime_notes**
- [ ] Last **≥8** quarters + **seasonality_note**
- [ ] **earnings_bridge** with ≥2 drivers + narrative
- [ ] **working_capital:** debtor days + CFO vs PAT ≥3y + commentary
- [ ] **capital_allocation** grade / ROCE story
- [ ] Lens must-have metrics present or explicit gaps

## D. Operating / KPI depth

- [ ] **kpi_scorecard** ≥6 rows; ≥4 periods where disclosed (else `gap_reason`)
- [ ] Render only via **`kpi_table()`** — never `str(dict)` in cells
- [ ] Mix: geo **and** product/vertical/stream when both exist
- [ ] Demand: named wins + count vs size
- [ ] **outlook.guidance_history ≥3** sourced rows
- [ ] **management_scorecard.guidance_delivery ≥2** with sources

## E. Market / relative depth

- [ ] ≥3 real peers; columns include valuation **and** operating/growth metric
- [ ] **implied_growth.assumption** filled
- [ ] Bull/base/bear with assumptions + **math_note** (use `scenario_value.py`)

## F. Intellectual honesty + production

- [ ] Thesis-breaking risks (not only generic macro)
- [ ] Moats: real vs marketing
- [ ] Gaps stated (no silent omit)
- [ ] HTML smoke clean: no empty timeline shell, no `{&#x27;` dict garbage
- [ ] Skeptical PM test: enough to allocate? If no → deepen

## Machine gate mapping

| Checklist | Pack / check |
|-----------|----------------|
| A | `sources_completeness` |
| B | `decision` |
| C | `financials_quarterly`, `earnings_bridge`, `working_capital` |
| D | `kpi_scorecard`, `outlook.guidance_history`, `management_scorecard` |
| E | `peers`, `valuation` |
| F | `smoke_check_html` via `validate_depth.py --html` / `assemble_pdf.py` |
