# Sector lens: Consumer discretionary

`lens_id`: `consumer-discretionary`

Load this file only when the router selects `consumer-discretionary`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Durables, apparel, jewellery, and retail sell discretionary goods via stores and online.

**How it is valued:** P/E or EV/EBITDA with SSSG / volume and store expansion.

**Competitive intensity:** Brand + design cycles; rate-sensitive demand.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Sourcing | Manufacturing / imports |
| THE BRAND | Design + brand |
| Channels | Stores / online |
| Consumers | Discretionary demand |

## Must-have metrics

- **SSSG / LFL** (`sssg`)
- **Stores** (`store_count`)
- **ASP** (`asp`)
- **Gross margin** (`gross_margin`)
- **Inventory days** (`inventory_days`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, SSSG, Margins, Store growth
- Selection: Same category (durables, apparel, jewellery, specialty retail).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** SSSG, stores & mix

Cover (bullets/tables, sourced):
- Same-store / volume growth
- Store or outlet footprint adds
- ASP / mix commentary
- Inventory health

## Query keys for `query_source.py` / `build_facts.py`

```
SSSG
same store
store addition
ASP
inventory
online mix
```
