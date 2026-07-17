# Source routing — depth mode (quality over skim)

Never load a full concall, investor deck, or annual report into model context as
one blob. Extract to disk once, then query. Prefer structured pages over PDFs
when they already answer the question.

**Quality override:** screener + press release alone is **not** enough. Always
ingest the latest **earnings call transcript** (or captions) **and** enough prior
quarters to see guidance evolution. If token savings and report depth conflict,
**fetch and query more**.

## Depth ingest minimum (every full report)

| Source | Minimum |
|--------|---------|
| Screener consolidated | Full financials, ratios, peers, documents list |
| Latest results PR + deck | Full extract to `sources/` (or `deck_gap`) |
| Latest concall transcript | Required; mine guidance, mix, Q&A, tone |
| Prior 3–5 quarter PRs/transcripts | **≥3 prior** on disk; fill `outlook.guidance_history` |
| Annual report (latest; prior if gaps) | Segments, related party, contingent liabilities, auditor notes — or `annual_report_gap` |
| Exchange filings (12–18m) | Material events, results |
| News (3–5) | Catalysts / controversies — verify numbers |
| Peer screener pages | ≥3 peers, ops + valuation columns |

## Source Completeness Gate (before draft)

Write `facts/sources_completeness.json` (see facts-schemas). Drafting a ship PDF is
**blocked** until `status: pass`.

```bash
python skills/company-thesis-report/scripts/validate_depth.py --slug <slug>
```

Typical fail mode from thin runs: only latest PR+concall → `prior_concalls` &lt; 3 and
no AR. Fix by fetching prior quarter docs and AR, then re-validate.

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
| Outlook Near/Med/Long | **multi-quarter** concall extracts → `outlook_candidates.py` | guidance, outlook, expect, order book, capex | Single-call only |
| Guidance history | last 4–6 PRs/transcripts | guidance, expect, next quarter, FY | Ignoring prior misses |
| Customers | deck + concall | customer, client, marquee, concentration, top 10 | Logo inference |
| Capex / milestones / certs | deck awards/capex slides; concall | capex, commission, certification | — |
| Sector Deep-Dive | lens query keys + targeted chunks | **from lens `metrics.schema.json`** | Generic PE-only scrape |
| Financials annual | screener tables | annual, TTM | Re-fetch every section |
| Quarterly bridge | screener quarterly + concall | YoY, QoQ, one-off, other income | Snapshot without trend |
| Working capital | screener ratios + BS notes + concall | debtor, receivable, DSO, collection, cash flow | Skipping when PAT looks fine |
| KPI scorecard | deck + concall + lens metrics | annuity, SaaS, logo, attrition, utilisation, GNPA, … | Valuation-only KPIs |
| Segments | AR Ind AS 108; screener; concall | segment, geography, export, domestic | Invented SKU splits |
| Demand / backlog | concall + deck | order book, backlog, AUM, booking, subscriber, logo | Blending stock and flow |
| Capital allocation | AR + concall + cash flow | dividend, buyback, acquisition, capex | Ignoring cash use |
| Management scorecard | multi-quarter guidance vs delivery | guidance, expect, transition, CEO, succession | Single glowing quote |
| Footprint / RM | AR + deck | plant, facility, manufacturing, import, raw material | Registered office ≠ plant |
| Capacity | concall ops / deck | capacity, utilisation, utilization, occupancy, PLF | Bare % without unit |
| TAM | deck / concall only if figure stated | TAM, addressable market, market size | Growth rate as TAM |
| Valuation / implied growth | lens method + screener price + growth history | — | Multiple without “priced in” |
| Peers | lens peer rules + screener comps | — | Random large-caps; valuation-only rows |
| Moats / risks / thesis | packs already built + sparse primary | — | Marketing adjectives |
| Governance | screener shareholding; rating PDFs; AR litigation note | promoter, pledge, rating, litigation, preferential | — |
| Technicals | screener / secondary aggregator summary | 52 week, RSI, DMA | Hand-rolled OHLC in sandbox |
| YouTube-only concall (REC) | captions/transcript → same extract path | — | NotebookLM as hard dependency |

## Concall path (multi-quarter)

1. Screener Documents/Concalls → prefer PDF transcripts for **latest + prior 3–5 quarters**  
2. If REC/YouTube only → fetch captions/transcript to `sources/`  
3. `pdf_to_text.py` → `outlook_candidates.py` + `query_source.py`  
4. Fill `outlook.json`, `earnings_bridge.json`, `management_scorecard.json`, `kpi_scorecard.json`  
5. Draft from packs only  

## Annual report / deck path

1. Save PDF under `sources/`  
2. Full-doc `pdf_to_text.py` once (use `--expect-name` when URL was search-derived)  
3. `query_source.py` with section/lens keys → snippets only  
4. Merge into packs via `build_facts.py` + agent enrichment  

## Incremental runs

- `up_to_date` — reuse packs/report; optional price refresh in valuation  
- `new_quarter` — new concall/results + last 1–2 screener columns; refresh outlook/financials/governance/WC/KPI deltas; **carry forward** sector primer, value chain, footprint, peer set unless evidence changes  
- `force_full` — refetch and rebuild everything except append-only histories  

## Parallelism

Batch independent fetches (screener + concall PDFs + peer pages + rating rationale).
One retry max on a stuck source, then fall back (BSE/NSE filing, deck restatement,
secondary quote for price only). **Do not** declare a gap on concall until transcript
**and** captions paths were attempted.
