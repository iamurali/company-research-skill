# Sector lens: FMCG staples

`lens_id`: `fmcg-staples`

Load this file only when the router selects `fmcg-staples`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Branded staples companies distribute high-velocity consumer products through GT/MT channels.

**How it is valued:** P/E with volume growth and margin stability; brand strength supports premium multiples.

**Competitive intensity:** Intense brand and distribution competition; rural/urban mix matters.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| RM / packing | Inputs |
| THE COMPANY | Brand + manufacturing |
| Distribution | GT, MT, e-comm |
| Consumers | Households |

## Must-have metrics

- **Volume growth** (`volume_growth`)
- **Value growth** (`value_growth`)
- **Gross margin** (`gross_margin`)
- **A&P %** (`ap_spend`)
- **EBITDA margin** (`ebitda_margin`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, Volume growth, EBITDA margin, A&P
- Selection: Similar category (personal care, foods, etc.).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Volume, value & distribution

Cover (bullets/tables, sourced):
- Volume vs value growth
- Gross margin and A&P spends
- Distribution reach / outlet adds
- Category growth and market share if disclosed

## Query keys for `query_source.py` / `build_facts.py`

```
volume growth
value growth
A&P
distribution
rural
gross margin
market share
```
