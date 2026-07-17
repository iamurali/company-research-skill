# Sector lens: Telecom

`lens_id`: `telecom`

Load this file only when the router selects `telecom`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Telecom operators monetize connectivity via ARPU and subscribers; capex and spectrum are structural.

**How it is valued:** EV/EBITDA with ARPU, subs, and leverage; FCF after capex is critical.

**Competitive intensity:** Oligopoly in India mobile; competition on price vs quality cycles.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Spectrum / network | Licences, towers, fibre |
| THE OPERATOR | Retail + enterprise connectivity |
| Distribution | Recharge / enterprise sales |
| Subscribers | Consumer and enterprise |

## Must-have metrics

- **Subscribers** (`subs`)
- **ARPU** (`arpu`)
- **EBITDA margin** (`ebitda_margin`)
- **Capex** (`capex`)
- **Net debt/EBITDA** (`net_debt_ebitda`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA with FCF lens

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, ARPU, Subs growth, Leverage
- Selection: Other listed Indian telcos; equipment makers use capital-goods lens instead.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** ARPU, subs & capex

Cover (bullets/tables, sourced):
- Subscriber base and net adds
- ARPU trends
- Capex intensity and spectrum payments
- Leverage / net debt to EBITDA

## Query keys for `query_source.py` / `build_facts.py`

```
ARPU
subscribers
net adds
MOU
capex
spectrum
churn
```
