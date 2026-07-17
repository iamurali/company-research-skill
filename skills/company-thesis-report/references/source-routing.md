# Source routing — cheapest adequate source wins

Never load a full concall, investor deck, or annual report into model context.
Extract to disk once, then query. Prefer structured pages over PDFs when they
already answer the question.

## Trust hierarchy

1. **Primary** — exchange filings, filed presentations, rating rationales, company concall transcripts/PRs as filed  
2. **Structured financials** — screener.in (or equivalent) for P&L, BS, ratios, shareholding  
3. **Discovery-only** — news aggregators; verify before citing numbers  
4. **Broker research** — only if the user uploads it; fold facts inline, never as the pipeline’s own finding  

## Per-section routing

| Section / need | Prefer | Query keys (examples) | Avoid |
|----------------|--------|------------------------|-------|
| Company Summary, price, ratios | screener consolidated page | About, market cap, P/E | Re-reading AR cover |
| Sector Context primer | loaded lens `LENS.md` | — | Re-deriving sector 101 every run |
| Company value chain | investor deck business-model slide; AR overview | value chain, backward integrat, customer, raw material | Guessing tiers |
| Outlook Near/Med/Long | concall extract → `outlook_candidates.py` | guidance, outlook, expect, order book, capex | Full transcript Read |
| Customers | deck + concall | customer, client, marquee, concentration, top 10 | Logo inference |
| Capex / milestones / certs | deck awards/capex slides; concall | capex, commission, certification, AS9100, USFDA, ISO | — |
| Sector Deep-Dive | lens query keys + targeted chunks | **from lens `metrics.schema.json`** | Generic PE-only scrape |
| Financials | screener tables | quarterly, annual, TTM | Re-fetch every section |
| Segments | AR Ind AS 108 note; screener; concall | segment, geography, export, domestic | Invented SKU splits |
| Demand / backlog | concall + deck | order book, backlog, AUM, booking, subscriber | Blending stock and flow |
| Footprint / RM | AR + deck | plant, facility, manufacturing, import, raw material | Registered office ≠ plant |
| Capacity | concall ops / deck | capacity, utilisation, utilization, occupancy, PLF | Bare % without unit |
| TAM | deck / concall only if figure stated | TAM, addressable market, market size | Growth rate as TAM |
| Valuation | lens method + screener price | — | Wrong method for the lens |
| Peers | lens peer rules + screener comps | — | Random large-caps |
| Moats / risks / thesis | packs already built + sparse primary | — | Marketing adjectives |
| Governance | screener shareholding; rating PDFs; AR litigation note | promoter, pledge, rating, litigation, preferential | — |
| Technicals | screener / secondary aggregator summary | 52 week, RSI, DMA | Hand-rolled OHLC in sandbox |
| YouTube-only concall (REC) | captions/transcript → same extract path | — | NotebookLM as hard dependency |

## Concall path

1. Screener Documents/Concalls tab → prefer PDF transcript  
2. If REC/YouTube only → fetch captions/transcript to `sources/`  
3. `pdf_to_text.py` (if PDF) → `outlook_candidates.py` + `query_source.py`  
4. Write `facts/outlook.json` / merge into other packs  
5. Draft outlook from the pack only  

## Annual report / deck path

1. Save PDF under `sources/`  
2. Full-doc `pdf_to_text.py` once (use `--expect-name` when URL was search-derived)  
3. `query_source.py` with section/lens keys → snippets only  
4. `build_facts.py` merges into packs  

## Incremental runs

- `up_to_date` — reuse packs/report; optional price refresh in valuation  
- `new_quarter` — new concall/results + last 1–2 screener columns; refresh outlook/financials/governance deltas; **carry forward** sector primer, value chain, footprint, peer set unless evidence changes  
- `force_full` — refetch and rebuild everything except append-only histories  

## Parallelism

Batch independent fetches (screener + concall PDF + rating rationale). One retry max on a stuck source, then fall back (BSE/NSE filing, deck restatement, secondary quote for price only).
