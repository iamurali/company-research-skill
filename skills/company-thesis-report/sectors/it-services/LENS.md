# Sector lens: IT services

`lens_id`: `it-services`

Load this file only when the router selects `it-services`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** IT services firms sell digital/engineering/outsourcing to global enterprises on T&M or fixed-price models.

**How it is valued:** P/E vs growth and margins; deal TCV and attrition are leading indicators.

**Competitive intensity:** Global scale players + niche digital engineers; pricing and talent are the constraints.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Clients | Global enterprises by vertical |
| THE COMPANY | Delivery centres + onsite |
| Services | ADM, cloud, engineering, BPO |
| Talent | Hiring, utilization, attrition |

## Must-have metrics

- **CC growth** (`growth_cc`)
- **EBIT margin** (`ebit_margin`)
- **Attrition** (`attrition`)
- **Utilization** (`utilization`)
- **Deal TCV** (`tcv`)
- **Top client %** (`top_client`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E vs growth/margins

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, CC growth, EBIT margin, Attrition
- Selection: Similar size tier and digital vs traditional mix.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Growth quality & talent

Cover (bullets/tables, sourced):
- Revenue by vertical and geography
- Large deal TCV / wins
- Attrition and utilization
- Margin bridge commentary

## Query keys for `query_source.py` / `build_facts.py`

```
constant currency
attrition
utilization
TCV
deal win
vertical
geography
headcount
```
