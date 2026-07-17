# Sector lens: Specialty chemicals

`lens_id`: `specialty-chemicals`

Load this file only when the router selects `specialty-chemicals`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Differentiated chemical producers sell application-specific molecules with technical qualification cycles.

**How it is valued:** EV/EBITDA or P/E with RM pass-through and specialty mix.

**Competitive intensity:** China+1 and qualification barriers help; commodity overhang when mix dilutes.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Feedstock | RM / intermediates |
| THE COMPANY | Process chemistry + plants |
| Customers | Pharma, agro, industrial OEMs |
| Applications | End uses |

## Must-have metrics

- **Gross margin** (`gross_margin`)
- **EBITDA margin** (`ebitda_margin`)
- **Export %** (`export_mix`)
- **Capacity** (`capacity`)
- **Top products %** (`top_products`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA or P/E

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, EBITDA margin, Export mix, Growth
- Selection: Similar chemistry/application peers, not bulk commodity names.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Mix, RM & capacity

Cover (bullets/tables, sourced):
- Product / application mix
- RM linkage and gross margin bridge
- Capacity and new molecule pipeline
- Customer quals / stickiness

## Query keys for `query_source.py` / `build_facts.py`

```
specialty
gross margin
raw material
capacity
China
qualification
molecule
```
