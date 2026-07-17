# Sector lens: Metals & mining

`lens_id`: `metals-mining`

Load this file only when the router selects `metals-mining`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Miners and metal producers earn on volumes times realizations/spreads through the commodity cycle.

**How it is valued:** EV/EBITDA through the cycle; net debt and cost curve position matter.

**Competitive intensity:** Global price takers; domestic cost and integration differentiate.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Ore / energy | Mining inputs |
| THE COMPANY | Mining + smelting/refining |
| Sales | Domestic / export |
| End use | Infra, auto, packaging |

## Must-have metrics

- **Volumes** (`volumes`)
- **Realization** (`realization`)
- **EBITDA/ton** (`ebitda_per_ton`)
- **Net debt** (`net_debt`)
- **C1 / cost** (`c1_cost`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA through cycle

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, EBITDA/ton, Net debt, Cost
- Selection: Same metal (steel flat vs long; aluminium; zinc, etc.).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Realizations, spreads & costs

Cover (bullets/tables, sourced):
- Volume and realization / spread trends
- Cost per ton and power/coal linkage
- Net debt and FCF
- Integration (mine to metal)

## Query keys for `query_source.py` / `build_facts.py`

```
realization
LME
spread
cost per ton
coking coal
volume
```
