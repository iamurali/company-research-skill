# Sector lens: Cement & building materials

`lens_id`: `cement-building-materials`

Load this file only when the router selects `cement-building-materials`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Cement and building-material producers are regional volume/price businesses with high fixed costs.

**How it is valued:** EV/EBITDA with utilization and realization; replacement cost sometimes used.

**Competitive intensity:** Regional oligopolies; pricing power fluctuates with demand and fuel costs.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Limestone / fuel | Inputs |
| THE COMPANY | Clinker / cement plants |
| Trade | Dealers / projects |
| Construction | End demand |

## Must-have metrics

- **Volumes** (`volumes`)
- **Utilization** (`utilization`)
- **Realization** (`realization`)
- **EBITDA/ton** (`ebitda_per_ton`)
- **Fuel cost** (`fuel_cost`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, EBITDA/ton, Utilization, Growth
- Selection: Overlapping geographies preferred.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Utilization & realizations

Cover (bullets/tables, sourced):
- Volume and capacity utilization
- Realization / premium mix
- Fuel cost and power mix
- Regional demand commentary

## Query keys for `query_source.py` / `build_facts.py`

```
realization
utilization
clinker
trade vs non-trade
pet coke
power
```
