# Sector lens: Commodity chemicals / petrochem

`lens_id`: `commodities-petrochem`

Load this file only when the router selects `commodities-petrochem`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Bulk chemical and petrochemical producers run cracker/process plants earning on spreads over feedstock.

**How it is valued:** EV/EBITDA with spread cycle; integration and utilization adjust multiples.

**Competitive intensity:** Global commodity pricing; domestic demand and import parity set local realizations.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Feedstock | Naphtha, gas, other |
| THE COMPANY | Crackers / plants |
| Polymers / chem | Product slate |
| Converters | Downstream users |

## Must-have metrics

- **Utilization** (`utilization`)
- **Key spread** (`spread`)
- **EBITDA margin** (`ebitda_margin`)
- **Net debt** (`net_debt`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA through cycle

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, Spreads, Utilization
- Selection: Similar product slate and feedstock base.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Spreads & utilization

Cover (bullets/tables, sourced):
- Key spreads / cracks vs history
- Utilization and turnaround schedule
- Product slate mix
- Integration benefits

## Query keys for `query_source.py` / `build_facts.py`

```
spread
crack
utilization
naphtha
polymer
PVC
PE
PP
```
