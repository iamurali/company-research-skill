# Sector lens: CDMO / API

`lens_id`: `cdmo-api`

Load this file only when the router selects `cdmo-api`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Contract development/manufacturing and API suppliers serve innovator and generic sponsors under quality systems.

**How it is valued:** EV/EBITDA with capacity, utilization, and customer/pipeline quality; PE alone understates pipeline optionality.

**Competitive intensity:** Global competition; sticky relationships once qualified; modality/tech capability matters.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Sponsors | Innovators / generic cos |
| THE COMPANY | Development + manufacturing |
| Tech / capacity | Reactives, fermentation, peptides, etc. |
| Patients / end drugs | Via sponsor labels |

## Must-have metrics

- **CDMO mix %** (`cdmo_mix`)
- **Capacity** (`capacity`)
- **Utilization** (`utilization`)
- **Top customer %** (`top_customer`)
- **Commercial projects** (`pipeline_commercial`)
- **Clinical projects** (`pipeline_clinical`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA with growth/capacity

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, EBITDA margin, Growth, Capacity
- Selection: Peers with similar service mix (pure CDMO vs API-heavy).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Service mix & pipeline

Cover (bullets/tables, sourced):
- CDMO vs API vs CRAMS mix if disclosed
- Pipeline / project counts by phase when disclosed
- Capacity by technology and utilization
- Customer concentration and qualifications

## Query keys for `query_source.py` / `build_facts.py`

```
CDMO
CRAMS
CRDMO
API
pipeline
Phase
capacity
utilization
peptide
fermentation
customer concentration
```
