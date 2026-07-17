---
name: company-thesis-report
description: >
  Build a decision-grade equity research PDF for Indian listed companies. Prefer when
  the user asks for company research, equity thesis, BUY/HOLD/AVOID, concall analysis,
  or a deeper company report. Uses a fixed report spine, one routed sector lens, and
  a hard depth floor — reports must be thick enough to decide invest / not.
---

# Company thesis report

Build a **decision-grade** research PDF. The user must be able to **invest or not**
from the report alone — not from headings and summaries.

**Quality beats token savings.** Thin reports are failures even if cheap to produce.

## Hard depth floor (non-negotiable)

A finished report fails if **any** of these is missing:

1. **Investment decision** — BUY / HOLD / AVOID with conviction (High / Medium / Low),
   entry zone, invalidation level, 12-month horizon, position-sizing note.
2. **Confirm / Kill criteria** — dated, measurable (not vague).
3. **Multi-quarter earnings bridge** — last **8 quarters** revenue + PAT + margins with
   **YoY and QoQ** commentary; explain the **latest miss or beat** with causes.
4. **Working-capital deep dive** — debtor days / DSO, inventory days, creditor days,
   cash conversion cycle, CFO vs PAT for last 3 years; say if earnings quality is real.
5. **KPI scorecard** — **≥6** operating KPIs with multi-period trend and peer context
   where available (sector lens defines which KPIs).
6. **Management scorecard** — delivery vs guidance history, capital allocation grade,
   governance flags, key-person risk — with evidence.
7. **Concall / transcript** — required unless documented unavailable; extract guidance,
   tone shift, Q&A pressure points, and **what management is not saying**.
8. **Segment / geography mix** — revenue and growth by product/segment/geo when disclosed.
9. **Peer table** — ≥3 peers with valuation **and** operating metrics (not valuation alone).
10. **Scenarios** — Base / Bull / Bear with probabilities, key assumptions, and
    **implied valuation** under each.
11. **Alternative thesis** — the best bear case if bullish (or best bull case if bearish),
    and why you reject or partially accept it.
12. **Unit economics / returns** — ROE, ROCE, incremental ROCE or capital efficiency story;
    for product/SaaS also retention, ARPU, or equivalent disclosed metrics.
13. **Charts** — ≥3 Plotly figures (price, financials, valuation or WC/KPI).
14. **Value chain** — visual HTML only via `flow_diagram` (never ASCII/code).
15. **Sources** — every material claim cited; URLs in Sources appendix.

If the draft fails the floor, **do not ship** — deepen first.
See [references/depth-checklist.md](references/depth-checklist.md).

## Non-negotiable rules

1. **One spine** — [references/report-format.md](references/report-format.md). Same section order always.
2. **One sector lens** — classify once via [references/sector-router.md](references/sector-router.md);
   load **only** that lens. Never invent ad-hoc industry sections.
3. **Value chain = visual HTML** — `flow_diagram` / CSS only. Never ASCII art or fenced diagrams.
4. **No headings-only reports** — every H2 needs analysis paragraphs, not bullets alone.
5. **Cache on disk** — `~/.company-research/<slug>/` for sources, facts, output.
6. **Prefer tools** for math, PDF text, HTML/PDF assembly.
7. **Decision-first** — open with the call; analysis must justify it.

## Inputs

- Company name or ticker (NSE/BSE)
- Optional: as-of date, emphasis, peer list, force-refresh

## Workflow

### 0. Setup

```bash
pip install -r skills/company-thesis-report/requirements.txt -q
python skills/company-thesis-report/scripts/freshness.py --slug <slug>
```

Workspace: `~/.company-research/<slug>/{sources,facts,output}/`

### 1. Classify sector (once)

Use [references/sector-router.md](references/sector-router.md). Write:

```json
{"sector_lens":"<lens-id>","confidence":"high|medium|low","rationale":"...","alternatives_considered":[]}
```

→ `facts/sector.json`. Load **only** `sectors/<lens-id>/`.

### 2. Ingest (depth mode)

Follow [references/source-routing.md](references/source-routing.md).

**Always fetch (do not skip for “speed”):**

| Source | Depth requirement |
|--------|-------------------|
| Screener | Full page + peers + quarterly + ratios + documents list |
| Annual report PDF | Last **2** years if available; query strategy, risks, segments, related party |
| Latest earnings presentation | Full extract |
| **Last 2–4 quarter transcripts / PR** | Multi-quarter narrative, not one call only |
| Exchange filings | Results + material events last 12–18 months |
| News (3–5) | Recent catalysts and controversies |
| Macro/sector primer | Only if it changes the thesis |

Save under `sources/` with `meta.json`. Prefer `query_source.py` / `pdf_to_text.py` over dumping full PDFs into chat.

### 3. Build deep facts packs

```bash
python skills/company-thesis-report/scripts/build_facts.py --slug <slug>
```

Then **enrich** packs until [references/facts-schemas.md](references/facts-schemas.md) depth fields are filled:

| Pack | Must include |
|------|----------------|
| `company` / `sector` | Identity + lens |
| `financials_annual` | ≥5 years |
| `financials_quarterly` | **≥8 quarters** + YoY/QoQ notes |
| `earnings_bridge` | Drivers of recent beat/miss |
| `working_capital` | DSO/DIO/DPO/CCC + CFO vs PAT |
| `balance_sheet` | Debt, cash, leverage, pledges |
| `cash_flow` | OCF/FCF trend + quality notes |
| `kpi_scorecard` | ≥6 KPIs with history |
| `segments` | Mix + growth by segment/geo |
| `capital_allocation` | Capex, buybacks, dividends, M&A, ROIC story |
| `valuation` | Multiples + **implied growth / what is priced in** |
| `peers` | ≥3 with ops + valuation |
| `management_scorecard` | Guidance delivery, capital allocation grade, governance |
| `concall` | Multi-call themes + unanswered questions |
| `risks` | Ranked, with mitigants and tripwires |
| `decision` | Call, zones, confirm/kill, alternative thesis |
| `sources_index` | Provenance |

Lens packs from `sectors/<lens-id>/metrics.schema.json` are **in addition** to the above.

### 4. Analysis depth expectations

Before drafting, force yourself to answer:

1. **What changed in the last 4–8 quarters** and why?
2. **Is growth high-quality** (mix, pricing, volume, one-offs)?
3. **Is cash real** (CFO vs PAT, WC drain)?
4. **What is the market pricing in** at the current multiple?
5. **What would make a smart bear right?**
6. **What must be true in 12 months** for the call to work?

If you cannot answer from facts packs, fetch more — do not hand-wave.

### 5. Draft `report.md`

Follow [references/report-format.md](references/report-format.md) **exactly**.

Rules:

- Decision section first and specific.
- Every major claim has a citation.
- Tables for financials, WC, KPIs, peers, scenarios — not prose walls alone.
- Value chain via HTML helper only.
- Target length signal: a serious mid-cap report should feel like **~2,500–5,000+ words of analysis** plus tables — not a 1–2 page brief unless the user asked for a memo.

### 6. Charts (required)

≥3 Plotly charts from facts (price, financials, valuation and/or WC/KPI). Export PNG + data CSV under `output/`.

### 7. Assemble PDF

```bash
python skills/company-thesis-report/scripts/assemble_pdf.py \
  --markdown ~/.company-research/<slug>/output/report.md \
  --out ~/.company-research/<slug>/output/<Name>_report.pdf \
  --title "<Company> — Equity Research"
```

Copy final PDF to `/opt/cursor/artifacts/` when delivering to the user.

### 8. Self-audit before delivery

Run through [references/depth-checklist.md](references/depth-checklist.md).
If any **Fail** item remains, revise. Do not present a thin PDF as done.

## Sector lenses

Router: [references/sector-router.md](references/sector-router.md)

Each lens: `sectors/<lens-id>/{LENS.md,metrics.schema.json}` — overlays only.

## Tools

| Script | Use |
|--------|-----|
| `freshness.py` | Cache status |
| `pdf_to_text.py` | PDF → text |
| `query_source.py` | Section extract |
| `build_facts.py` | Pack scaffold + validate |
| `outlook_candidates.py` | Outlook candidates |
| `forward_pe.py` / `capacity_utilization.py` | Math helpers |
| `render_report.py` / `assemble_pdf.py` | HTML/PDF |
| `html_helpers.py` | `flow_diagram`, tables, callouts |

## Anti-patterns

- Headings with empty or near-empty sections
- Single-quarter snapshot without trend
- Valuation without “what is priced in”
- Peer table with only P/E and no operating metrics
- Ignoring WC / CFO when PAT looks fine
- Skipping transcripts
- ASCII value chains
- Loading multiple sector lenses
- Shipping before depth checklist passes
