# Sector router

Classify the company once, then load **only** `sectors/<lens-id>/`.
Never load multiple lenses. Never put lens names into the report format spine.

## How to classify

1. Read screener.in industry / sector labels and the About blurb (already in `facts/meta.json`).  
2. Match against the table below (first strong match wins).  
3. If two lenses fit a conglomerate, pick the **primary revenue** segment; note secondary in Segment-wise + Risks.  
4. If unclear after one pass, ask the user once or use `generic` and state that in Sector Context.

## Mapping table (screener / description cues → lens id)

| Lens id | Match cues (industry keywords, business words) |
|---------|--------------------------------------------------|
| `banks` | Bank, Private Sector Bank, Public Sector Bank, banking, deposits, CASA |
| `nbfc-hfc` | NBFC, Housing Finance, HFC, microfinance, AUM, gold loan, vehicle finance (non-bank) |
| `insurance` | Life Insurance, General Insurance, VNB, APE, solvency |
| `capital-markets` | Exchange, Broker, Depository, Asset Management, AMC, mutual fund house |
| `pharma-formulations` | Pharmaceuticals, formulations, branded generics, US generics (finished dose) |
| `cdmo-api` | CDMO, CRAMS, CRDMO, API manufacturer, contract manufacturing pharma, intermediates |
| `hospitals-diagnostics` | Hospital, Diagnostics, healthcare services, ARPOB, occupancy |
| `it-services` | IT - Software, IT Services, consulting, BPO/KPO with IT services mix |
| `internet-saas` | Internet, e-commerce platform, SaaS product, online marketplace (non-retail pure) |
| `telecom` | Telecom - Services, Telecom - Equipment with carrier services, ARPU |
| `capital-goods-epc` | Capital Goods, Industrial Products, heavy electrical, EPC, engineering project |
| `aerospace-defence` | Aerospace & Defense, defence, defence electronics, offset, LCA/programme |
| `auto-oem` | Passenger Cars, 2/3 Wheelers, Commercial Vehicles, tractor OEM |
| `auto-ancillary` | Auto Components, Tyres, auto parts supplier |
| `specialty-chemicals` | Specialty Chemicals, dyes, pigments, fine chemicals (non-commodity) |
| `agrochem-fertilizers` | Fertilizers, Pesticides, agrochemicals |
| `cement-building-materials` | Cement, Building Products, construction materials |
| `metals-mining` | Ferrous, Non-Ferrous, Mining, steel, aluminium, zinc, copper |
| `commodities-petrochem` | Commodity Chemicals, Petrochemicals, polymers bulk |
| `oil-gas` | Oil Exploration, Refineries, Gas Transmission, oil marketing |
| `power-utilities` | Power Generation, Transmission, Distribution, integrated power |
| `renewables` | Renewable, solar, wind, green energy IPP |
| `fmcg-staples` | FMCG, Packaged Foods, Personal Care, staples |
| `consumer-discretionary` | Consumer Durables, Retail, Apparel, Footwear, jewellery retail |
| `realty` | Realty, residential/commercial developer, pre-sales |
| `transport-logistics` | Logistics, Shipping, Ports, Airlines, Airports, road transport |
| `media-hotels-leisure` | Media, Hotels, Restaurants, Leisure, gaming, film |
| `generic` | Diversified with no clear primary, or no match |

## Load rules

```text
1. Write sector_lens_id into facts/meta.json
2. Read sectors/<lens-id>/LENS.md and metrics.schema.json only
3. Run build_facts with that schema → facts/sector_overlay.json
4. Draft Sector Context + Sector Deep-Dive + metric/valuation/peer overlays from that pack
```

## Adding a new lens

1. Create `sectors/<new-id>/LENS.md` + `metrics.schema.json`  
2. Add a row to this router table  
3. No changes to `report-format.md` spine required  
