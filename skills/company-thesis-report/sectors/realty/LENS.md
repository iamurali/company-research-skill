# Sector lens: Realty

`lens_id`: `realty`

Load this file only when the router selects `realty`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Developers monetize land banks via launches, pre-sales, and collections across residential/commercial projects.

**How it is valued:** P/B or NAV-based; pre-sales and collections are operating KPIs.

**Competitive intensity:** City-level competition; brand and execution on delivery timelines matter.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Land bank | Land / JDA |
| THE DEVELOPER | Projects under execution |
| Sales | Pre-sales / bookings |
| Customers | Homebuyers / tenants |

## Must-have metrics

- **Pre-sales** (`presales`)
- **Collections** (`collections`)
- **Net debt** (`net_debt`)
- **Land bank** (`land_bank`)
- **Unsold inventory** (`unsold`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B or NAV

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, Pre-sales growth, Net debt, Collections
- Selection: Overlapping cities and residential vs commercial focus.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Pre-sales & balance sheet

Cover (bullets/tables, sourced):
- Pre-sales and collections
- Launch pipeline and unsold inventory
- Net debt / cash flow
- City and segment mix

## Query keys for `query_source.py` / `build_facts.py`

```
pre-sales
collections
launch
land bank
unsold
JDA
RERA
```
