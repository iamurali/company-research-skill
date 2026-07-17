# Sector lens: Media, hotels & leisure

`lens_id`: `media-hotels-leisure`

Load this file only when the router selects `media-hotels-leisure`. Do not load other lenses.

## Sector primer (for Sector Context)

**How it operates:** Media monetizes ads/subscriptions; hotels/leisure monetize occupancy and ADR / ticketed demand.

**How it is valued:** EV/EBITDA with occupancy/ADR or ad/subscription growth.

**Competitive intensity:** Cyclical advertising and travel; content and location differentiate.

### Sector value-chain stages (for visual `flow_diagram()`)

| Stage | Detail |
|-------|--------|
| Content / property | Assets |
| THE OPERATOR | Network / hotels / parks |
| Distribution | Screens, OTT, OTAs |
| Audiences / guests | End demand |

## Must-have metrics

- **Occupancy** (`occupancy`)
- **ADR** (`adr`)
- **RevPAR** (`revpar`)
- **Ad revenue** (`ad_revenue`)
- **Subscription revenue** (`subscription`)

Pull these into `facts/sector_overlay.json` and Financial Performance metric cards when disclosed. If missing, state the gap — do not invent.

## Valuation method

**Primary:** EV/EBITDA

Write method + inputs into `facts/valuation.json`. Do not default to an unrelated multiple.

## Peer rules

- Columns: EV/EBITDA, Occupancy/ADR or ad growth, Margins
- Selection: Hotels vs media vs parks separately.
- Always include the subject company as its own row.

## Sector Deep-Dive template

**Suggested title:** Occupancy, ADR or ads

Cover (bullets/tables, sourced):
- Occupancy and ADR (hotels) or ad/subscription mix (media)
- RevPAR or ARPU analogues
- Capacity / room / screen adds
- Cost inflation commentary

## Query keys for `query_source.py` / `build_facts.py`

```
occupancy
ADR
RevPAR
ad revenue
subscription
TRP
footfall
```
