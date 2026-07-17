# Sector lens: Banks

`lens_id`: `banks`

Load this file only when the router selects `banks`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Banks intermediate deposits into loans and investments, earn net interest margin, and are supervised for capital adequacy and asset quality.

**How it is valued:** Primarily P/B vs RoA/RoE; credit growth and asset-quality trajectory matter more than headline PE.

**Competitive intensity:** Concentrated large private + PSU banks; niche small-finance and regional players compete on liability franchise and underwriting.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Funding / liabilities | Deposits, CASA, borrowings |
| THE BANK | Underwriting, ALM, distribution |
| Credit / assets | Retail, wholesale, agri, investments |
| End users | Households, SMEs, corporates |

## Must-have metrics

- **GNPA %** (`gnpa`)
- **NNPA %** (`nnpa`)
- **PCR %** (`pcr`)
- **NIM %** (`nim`)
- **CASA %** (`casa`)
- **Credit growth YoY** (`credit_growth`)
- **RoA %** (`roa`)
- **RoE %** (`roe`)
- **CRAR %** (`crar`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B with RoA/RoE context

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, RoA, GNPA, NIM, Credit growth
- Selection: 3–5 listed banks with similar book mix (private vs PSU; retail-heavy vs wholesale).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Asset quality & franchise

Cover (bullets/tables, sourced):
- GNPA / NNPA / PCR trend with as-of dates
- NIM, CASA ratio, credit growth YoY
- Capital ratios (CET1/CRAR) if disclosed
- Liability franchise quality and granularity

## Query keys for `query_source.py` / `build_facts.py`

```
GNPA
NNPA
PCR
NIM
CASA
credit growth
CET1
CRAR
slippages
restructured
```
