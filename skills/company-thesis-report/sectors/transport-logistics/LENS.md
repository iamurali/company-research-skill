# Sector lens: Transport & logistics

`lens_id`: `transport-logistics`

Load this file only when the router selects `transport-logistics`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Logistics, shipping, ports, and aviation move goods/people; volumes and realizations drive earnings.

**How it is valued:** EV/EBITDA with volume growth and realization; asset-heavy names also use P/B.

**Competitive intensity:** Fragmented road logistics; ports/airports more concession-driven.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Shippers / travellers | Demand |
| THE OPERATOR | Network / fleet / terminal |
| Infrastructure | Ports, airports, warehouses |
| Delivery | End destination |

## Must-have metrics

- **Volumes** (`volumes`)
- **Realization / yield** (`realization`)
- **EBITDA margin** (`ebitda_margin`)
- **Utilization** (`utilization`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA (or P/B for concessions)

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, Volume growth, Margins
- Selection: Same mode (road, ocean, port, aviation).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Volumes & realizations

Cover (bullets/tables, sourced):
- Volume trends (TEU, tonnage, Pax, GMT)
- Realization / yield
- Network or capacity adds
- Fuel / cost pass-through

## Query keys for `query_source.py` / `build_facts.py`

```
TEU
tonnage
Pax
yield
realization
fleet
concession
```
