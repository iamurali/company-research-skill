# Sector lens: Insurance

`lens_id`: `insurance`

Load this file only when the router selects `insurance`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Life/general insurers collect premiums, invest float, and manage claims/persistency under solvency regulation.

**How it is valued:** Life: VNB / EV multiples; General: combined ratio and growth. PE alone is a weak primary lens.

**Competitive intensity:** Large bank-affiliated and standalone players; distribution (agency/bancassurance) is the battleground.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Distribution | Agency, banca, digital |
| THE INSURER | Underwriting, product design |
| Investments | Float / shareholder funds |
| Policyholders | Protection, savings, health, motor |

## Must-have metrics

- **APE** (`ape`)
- **VNB margin** (`vnb_margin`)
- **Persistency 13M** (`persistency_13m`)
- **Solvency** (`solvency`)
- **Combined ratio** (`combined_ratio`)
- **Embedded value** (`ev`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** VNB / EV multiple (life) or P/B with combined ratio (general)

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: VNB margin, APE growth, Persistency, Solvency
- Selection: Same line (life vs general/health); similar distribution mix preferred.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** New business & quality

Cover (bullets/tables, sourced):
- APE / NBP growth and mix (protection vs savings)
- VNB margin and embedded value if disclosed
- Persistency (13M/61M)
- Solvency ratio

## Query keys for `query_source.py` / `build_facts.py`

```
APE
VNB
embedded value
persistency
solvency
combined ratio
NBP
protection mix
```
