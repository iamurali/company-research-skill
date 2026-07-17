# Sector lens: Agrochem & fertilizers

`lens_id`: `agrochem-fertilizers`

Load this file only when the router selects `agrochem-fertilizers`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Crop-protection and nutrient suppliers sell through seasonal channels; policy and monsoon matter.

**How it is valued:** P/E or EV/EBITDA with volume/realization and subsidy/channel health for fertilizers.

**Competitive intensity:** Global molecule competition in agrochem; fertilizers influenced by gas/RM and subsidies.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| RM / gas | Inputs |
| THE COMPANY | Formulation / manufacturing |
| Channel | Distributors / retailers |
| Farmers | End demand |

## Must-have metrics

- **Volumes** (`volumes`)
- **Realization** (`realization`)
- **Gross margin** (`gross_margin`)
- **Channel inventory** (`channel_inventory`)
- **Subsidy receivable** (`subsidy_receivable`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** P/E or EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: P/E, Margins, Growth, Mix
- Selection: Agrochem vs fertilizer separately; similar export vs domestic mix.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Volumes, channel & policy

Cover (bullets/tables, sourced):
- Volume vs realization bridge
- Channel inventory commentary
- Subsidy / receivables for fertilizers
- Molecule / nutrient mix

## Query keys for `query_source.py` / `build_facts.py`

```
monsoon
channel inventory
subsidy
urea
DAP
formulation
technical
```
