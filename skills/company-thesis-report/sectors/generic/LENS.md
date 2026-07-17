# Sector lens: Generic (no specialist lens)

`lens_id`: `generic`

Load this file only when the router selects `generic`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** No specialist sector lens matched. Use universal report spine only and label Sector Context accordingly.

**How it is valued:** Default to methods supported by disclosures (often P/E or EV/EBITDA) without forcing a sector framework.

**Competitive intensity:** State competitive context from company sources only; do not invent industry structure.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Upstream | As disclosed |
| THE COMPANY | Core activities as disclosed |
| Downstream | Customers as disclosed |
| End market | As disclosed |

## Must-have metrics

- **Revenue growth** (`revenue_growth`)
- **EBITDA margin** (`ebitda_margin`)
- **RoE** (`roe`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** Disclosure-led (often P/E or EV/EBITDA)

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, EBITDA margin, Growth
- Selection: Closest listed comps by business description; keep peer set small and justified.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Company-specific operating points

Cover (bullets/tables, sourced):
- Summarize the 3–5 operating KPIs management actually discloses
- Note explicitly that no specialist sector lens was applied
- Avoid importing metrics from an unmatched industry

## Query keys for `query_source.py` / `build_facts.py`

```
guidance
outlook
margin
capacity
order
customer
```
