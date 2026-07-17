# Sector lens: Internet / SaaS

`lens_id`: `internet-saas`

Load this file only when the router selects `internet-saas`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Platforms and software products monetize subscriptions, take-rates, or ads with high fixed-cost leverage.

**How it is valued:** EV/Sales or EV/EBITDA with growth and retention; profitability path matters for listed India internet.

**Competitive intensity:** Winner-take-most dynamics in many categories; CAC and retention decide durability.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Users / customers | Acquisition funnel |
| THE PLATFORM | Product + marketplace |
| Monetization | Subs, take-rate, ads |
| Partners | Supply-side / developers |

## Must-have metrics

- **Revenue growth** (`rev_growth`)
- **Contribution margin** (`contribution_margin`)
- **Active users** (`active_users`)
- **Take-rate / ARPU** (`take_rate`)
- **Adj. EBITDA** (`adjusted_ebitda`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/Sales or EV/EBITDA with growth

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/Sales, Growth, Margins
- Selection: Same business model (marketplace vs SaaS vs classifieds).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Growth & retention

Cover (bullets/tables, sourced):
- Revenue growth and contribution margins
- Active users / customers and retention if disclosed
- Take-rate or ARPU trends
- Path to profitability / cash burn

## Query keys for `query_source.py` / `build_facts.py`

```
GMV
take rate
ARPU
retention
contribution margin
adjusted EBITDA
active users
```
