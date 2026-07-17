# Sector lens: Pharma formulations

`lens_id`: `pharma-formulations`

Load this file only when the router selects `pharma-formulations`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Finished-dose manufacturers sell branded/generic medicines in India and/or regulated export markets.

**How it is valued:** P/E or EV/EBITDA with US/India mix, FDA status, and pricing pressure context.

**Competitive intensity:** Highly competitive generics; differentiation via complex generics, specialty, and India brands.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| API / inputs | Own or bought API |
| THE COMPANY | Formulation manufacturing & filings |
| Channels | US wholesalers, India trade, other markets |
| Patients | Therapy areas |

## Must-have metrics

- **US revenue %** (`us_mix`)
- **India revenue %** (`india_mix`)
- **Gross margin** (`gross_margin`)
- **R&D % sales** (`r_and_d`)
- **Filings / launches** (`anda_pipeline`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA with mix adjustment

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, US mix, EBITDA margin, Growth
- Selection: Peers with similar US/India mix and therapy focus.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Market mix & regulatory

Cover (bullets/tables, sourced):
- US vs India vs RoW revenue mix
- Key launches / limited competition products
- FDA / regulatory status of plants
- Pricing / erosion commentary

## Query keys for `query_source.py` / `build_facts.py`

```
US generics
India branded
FDA
warning letter
ANDA
price erosion
complex generics
```
