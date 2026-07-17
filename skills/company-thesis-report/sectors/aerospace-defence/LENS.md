# Sector lens: Aerospace & defence

`lens_id`: `aerospace-defence`

Load this file only when the router selects `aerospace-defence`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Defence and aerospace suppliers execute long-cycle programmes under government and OEM contracts.

**How it is valued:** P/E or EV/EBITDA with order book visibility; programme concentration is a key risk adjuster.

**Competitive intensity:** Qualification barriers high; offset and indigenisation policies shape demand.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Budget / OEMs | MoD, DPSUs, global OEMs |
| THE COMPANY | Platforms, electronics, components |
| Programmes | Named platforms / contracts |
| End use | Air, land, naval, space |

## Must-have metrics

- **Order book** (`order_book`)
- **Top programme %** (`top_programme`)
- **Defence mix %** (`defence_mix`)
- **Export %** (`exports`)
- **EBITDA margin** (`ebitda_margin`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA with programme visibility

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, Order book, Margins, Growth
- Selection: Defence electronics vs platforms vs components — pick same tier.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Programmes & indigenisation

Cover (bullets/tables, sourced):
- Order book by programme / customer
- Indigenisation / offset exposure
- Execution milestones and LD risk
- Export vs domestic mix

## Query keys for `query_source.py` / `build_facts.py`

```
order book
programme
indigenisation
offset
MoD
HAL
export order
LD
```
