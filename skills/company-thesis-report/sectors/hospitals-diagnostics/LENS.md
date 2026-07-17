# Sector lens: Hospitals & diagnostics

`lens_id`: `hospitals-diagnostics`

Load this file only when the router selects `hospitals-diagnostics`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Healthcare providers earn on patient volumes, case mix, and payer mix across owned/managed networks.

**How it is valued:** EV/EBITDA with ARPOB, occupancy, and bed/network growth.

**Competitive intensity:** Regional clusters; brand and doctor engagement matter; diagnostics is more volume/price competitive.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Patients / payers | Cash, insurance, government |
| THE PROVIDER | Hospitals / labs network |
| Clinical delivery | Specialties, diagnostics |
| Outcomes | Care delivered |

## Must-have metrics

- **ARPOB** (`arpob`)
- **Occupancy %** (`occupancy`)
- **Beds / centres** (`beds`)
- **Insurance mix %** (`payer_mix_insurance`)
- **EBITDA margin** (`ebitda_margin`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, ARPOB, Occupancy, Growth
- Selection: Same format (hospitals vs pure diagnostics); similar city tier mix.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Network operating metrics

Cover (bullets/tables, sourced):
- ARPOB / ALOS and occupancy
- Bed count / centre count and additions
- Payer mix
- Specialty or test mix if disclosed

## Query keys for `query_source.py` / `build_facts.py`

```
ARPOB
occupancy
ALOS
beds
payer mix
footfall
tests
```
