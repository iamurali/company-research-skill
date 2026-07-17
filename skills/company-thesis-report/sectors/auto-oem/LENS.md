# Sector lens: Auto OEMs

`lens_id`: `auto-oem`

Load this file only when the router selects `auto-oem`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Vehicle OEMs design, manufacture, and distribute vehicles; volumes and mix drive earnings.

**How it is valued:** P/E or EV/EBITDA through the cycle; volume outlook and mix (UV/EV) matter.

**Competitive intensity:** Brand and distribution heavy; cyclical with rates, fuel, and rural demand.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Suppliers | Auto ancillaries |
| THE OEM | Manufacturing + R&D |
| Dealers | Domestic network / exports |
| Buyers | Retail and fleet |

## Must-have metrics

- **Volumes** (`volumes`)
- **Market share** (`market_share`)
- **ASP** (`asp`)
- **EBITDA margin** (`ebitda_margin`)
- **Export mix** (`export_mix`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA through cycle

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, Volume growth, EBITDA margin, Mix
- Selection: Same vehicle category (PV vs 2W vs CV).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Volumes, mix & ASP

Cover (bullets/tables, sourced):
- Wholesale/retail volumes and market share
- Segment mix (UV, PV, CV, 2W)
- ASP and realization trends
- EV / alternate fuel roadmap if material

## Query keys for `query_source.py` / `build_facts.py`

```
wholesale
retail
market share
ASP
UV mix
EV
inventory
```
