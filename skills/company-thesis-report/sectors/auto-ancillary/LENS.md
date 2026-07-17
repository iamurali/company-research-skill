# Sector lens: Auto ancillary

`lens_id`: `auto-ancillary`

Load this file only when the router selects `auto-ancillary`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Component suppliers sell into OEM programmes and aftermarket; content per vehicle is the growth lever.

**How it is valued:** P/E or EV/EBITDA with OEM concentration and content-growth story.

**Competitive intensity:** Programme-win competition; sticky once tooled; EV content shift is structural.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Raw materials | Steel, plastics, electronics |
| THE SUPPLIER | Components / systems |
| OEM / aftermarket | Programme supply |
| Vehicles | End vehicles |

## Must-have metrics

- **OEM mix %** (`oem_mix`)
- **Top customer %** (`top_customer`)
- **Export %** (`export_mix`)
- **EBITDA margin** (`ebitda_margin`)
- **EV-related %** (`ev_mix`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, EBITDA margin, Growth, Export mix
- Selection: Similar product family (tyres, forging, electronics, interiors).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Content growth & customers

Cover (bullets/tables, sourced):
- OEM vs aftermarket mix
- Customer concentration
- Content/vehicle or new programme wins
- EV-exposed revenue if disclosed

## Query keys for `query_source.py` / `build_facts.py`

```
OEM
aftermarket
content per vehicle
programme win
EV
customer concentration
```
