# Sector lens: Capital goods / EPC

`lens_id`: `capital-goods-epc`

Load this file only when the router selects `capital-goods-epc`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Engineered equipment and project firms convert orders into revenue over multi-quarter execution cycles.

**How it is valued:** P/E or EV/EBITDA with order book / book-to-bill; execution risk adjusts the multiple.

**Competitive intensity:** Bidding competition; qualification and reference plants matter for complex equipment.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Customers | Utilities, industry, infra |
| THE COMPANY | Engineering + manufacturing / EPC |
| Execution | Projects, working capital |
| Installed base | Aftermarket / spares |

## Must-have metrics

- **Order book** (`order_book`)
- **Book-to-bill** (`book_to_bill`)
- **Order inflow** (`inflow`)
- **EBITDA margin** (`ebitda_margin`)
- **WC days** (`wc_days`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA with order-book context

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, Order book / sales, EBITDA margin, Growth
- Selection: Peers in same product/EPC niche and similar domestic/export mix.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Order book & execution

Cover (bullets/tables, sourced):
- Order book size, composition, book-to-bill
- Inflow vs execution commentary
- Segment margins
- Working-capital / retention money

## Query keys for `query_source.py` / `build_facts.py`

```
order book
order inflow
book to bill
execution
retention
L1
bid
```
