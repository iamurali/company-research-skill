# Sector lens: NBFC / HFC

`lens_id`: `nbfc-hfc`

Load this file only when the router selects `nbfc-hfc`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Non-bank lenders fund via markets/banks and originate retail or wholesale credit without a full deposit franchise (HFCs focus on housing).

**How it is valued:** P/B vs RoA; AUM growth, spreads, and credit cost dominate.

**Competitive intensity:** Fragmented by product (vehicle, gold, MSME, housing); funding access and ALM are key differentiators.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Funding | Banks, bonds, CPs, securitisation |
| THE LENDER | Origination, underwriting, collections |
| Portfolio | AUM by product / geography |
| Borrowers | Retail / MSME / homebuyers |

## Must-have metrics

- **AUM** (`aum`)
- **AUM growth** (`aum_growth`)
- **Stage-3 %** (`stage3`)
- **Credit cost** (`credit_cost`)
- **NIM / spread** (`nim_spread`)
- **Leverage** (`leverage`)
- **Cost of funds** (`cof`)
- **RoA** (`roa`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B with RoA and growth

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, RoA, AUM growth, Stage-3, NIM
- Selection: Peers in the same product niche (HFC vs vehicle vs gold vs diversified).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** AUM quality & funding

Cover (bullets/tables, sourced):
- AUM growth and product mix
- Stage-3 / GNPA analogue and credit cost
- Leverage and liability mix / CoF
- Disbursement trends and collection efficiency

## Query keys for `query_source.py` / `build_facts.py`

```
AUM
disbursement
Stage 3
GNPA
credit cost
cost of funds
borrowing mix
securitisation
```
