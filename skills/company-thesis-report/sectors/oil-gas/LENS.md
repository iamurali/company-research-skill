# Sector lens: Oil & gas

`lens_id`: `oil-gas`

Load this file only when the router selects `oil-gas`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Upstream, refining, and marketing companies earn on production, GRMs, and marketing margins.

**How it is valued:** P/B or EV/EBITDA with GRM/production outlook; marketing is volume × margin.

**Competitive intensity:** Policy and global oil prices dominate; refining cycles are sharp.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Upstream | Crude / gas production |
| Refining | GRM / complexity |
| Marketing | Fuels retail / bulk |
| Consumers | Transport, industry |

## Must-have metrics

- **Production** (`production`)
- **GRM** (`grm`)
- **Throughput** (`throughput`)
- **Marketing margin** (`marketing_margin`)
- **Net debt** (`net_debt`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/B or EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/B, GRM, Production growth, Net debt
- Selection: Same segment (E&P vs refining vs integrated).
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Production, GRM & marketing

Cover (bullets/tables, sourced):
- Production volumes (upstream)
- GRM and throughput (refining)
- Marketing volumes and margins
- Debt and working capital

## Query keys for `query_source.py` / `build_facts.py`

```
GRM
production
throughput
marketing margin
ATF
diesel
under-recovery
```
