# Sector lens: Power & utilities

`lens_id`: `power-utilities`

Load this file only when the router selects `power-utilities`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Generators and utilities sell power under regulated or merchant arrangements; receivables and fuel are key.

**How it is valued:** P/B for regulated utilities; EV/EBITDA for merchant/generation with PLF context.

**Competitive intensity:** Regulated returns capped; merchant exposed to demand and fuel.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Fuel | Coal, gas, hydro inflows |
| THE UTILITY | Generation / T&D |
| Offtakers | Discoms, C&I, exchanges |
| End use | Power consumers |

## Must-have metrics

- **PLF %** (`plf`)
- **Availability** (`availability`)
- **Receivables** (`receivables`)
- **PPA mix %** (`ppa_mix`)
- **Net debt** (`net_debt`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B (regulated) or EV/EBITDA (merchant)

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, PLF, Receivables, Leverage
- Selection: Regulated vs merchant peers separately.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** PLF, offtake & receivables

Cover (bullets/tables, sourced):
- PLF / availability
- PPA vs merchant mix
- Receivables / discom exposure
- Regulated RoE framework if applicable

## Query keys for `query_source.py` / `build_facts.py`

```
PLF
PPA
merchant
receivables
discom
availability
RoE
```
