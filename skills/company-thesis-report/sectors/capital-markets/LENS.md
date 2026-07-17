# Sector lens: Capital markets

`lens_id`: `capital-markets`

Load this file only when the router selects `capital-markets`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Exchanges, brokers, depositories, and AMCs earn on volumes, flows, and AUM-linked fees.

**How it is valued:** P/E or EV/EBITDA vs volume/AUM growth; operating leverage to market activity is central.

**Competitive intensity:** Oligopolistic exchanges; broking and AMC highly competitive on pricing and distribution.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Issuers / AMCs | Products and listings |
| Market infrastructure | Exchange, clearing, depository |
| Intermediaries | Brokers, distributors |
| Investors | Retail and institutional |

## Must-have metrics

- **ADTO / volumes** (`adto`)
- **AUM** (`aum`)
- **Net flows** (`net_flows`)
- **Yield / take-rate** (`yield`)
- **Cost ratio** (`opex_ratio`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA vs growth

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, AUM/ADTO growth, Yield, Margins
- Selection: Same business line (exchange vs broker vs AMC).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Volumes, flows & mix

Cover (bullets/tables, sourced):
- Cash/F&O ADTO or equivalent volumes
- Net flows / AUM for AMCs
- Yield / take-rate trends
- Operating leverage and cost ratios

## Query keys for `query_source.py` / `build_facts.py`

```
ADTO
turnover
AUM
net flows
yield
market share
active clients
```
