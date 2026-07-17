# Sector lens: Renewables

`lens_id`: `renewables`

Load this file only when the router selects `renewables`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Renewable IPPs and developers build and operate solar/wind/hybrid assets under bid tariffs or C&I contracts.

**How it is valued:** P/B or EV/EBITDA with pipeline MW and bid tariff; execution and ALM matter.

**Competitive intensity:** Bid tariffs competitive; module/equipment costs and grid curtailment are swing factors.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Equipment | Modules, turbines, BOS |
| THE DEVELOPER | Open capacity + operating assets |
| Offtake | SECI/discom/C&I PPAs |
| Grid | Transmission / curtailment |

## Must-have metrics

- **Operating MW** (`operating_mw`)
- **Pipeline MW** (`pipeline_mw`)
- **CUF** (`cuf`)
- **Avg tariff** (`tariff`)
- **Net debt** (`net_debt`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B or EV/EBITDA per MW

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, MW growth, CUF, Leverage
- Selection: Similar tech mix (solar vs wind vs hybrid) and offtake type.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Pipeline & tariffs

Cover (bullets/tables, sourced):
- Operating vs under-construction MW
- Bid / PPA tariffs
- CUF / generation
- Balance sheet and bid pipeline risk

## Query keys for `query_source.py` / `build_facts.py`

```
MW
CUF
PPA
bid tariff
module
hybrid
BESS
```
