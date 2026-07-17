---
name: company-thesis-report
description: "Generates a decision-grade investment research PDF for a listed company — clear BUY/HOLD/AVOID (or equivalent), dense sourced analysis, sector lens, charts/tables, confirm/kill criteria. Use when the user asks to research a company, build a thesis, deep-dive a stock, or decide whether to invest — even for a bare ticker. Prefer report quality over token savings when they conflict."
---

# Company thesis report (decision-grade)

## Why this exists

The deliverable is a document someone can use to **decide whether to invest** — not a table of contents with thin bullets. Every run must answer:

1. **What should I do?** (BUY / HOLD / AVOID / selective accumulate — with confidence)
2. **Why?** (falsifiable, numbered evidence)
3. **What would change my mind?** (confirm thesis vs kill thesis)

A claim without a source and a date is marketing, not evidence. A section that is only a heading plus two vague lines is a **failed report** — rewrite it.

## Quality bar (non-negotiable — ship nothing thinner)

Before delivering the PDF, the report **must** include all of the following. If any item is missing, keep researching or state the gap inside that section — do not ship a headings-only PDF.

| Requirement | Minimum bar |
|-------------|-------------|
| **Decision first** | Opening section after cover: recommendation + 1 short paragraph why + confirm-list + kill-list |
| **Substance density** | Each major section has real analysis (interpretation), not only labels/numbers |
| **Latest concall** | Latest earnings call transcript (or captions) ingested to disk and mined — **PR alone is not enough** |
| **Financials** | Multi-year table + YoY read-through + BS/cash anomaly note; chart when time series helps |
| **Mix deep-dive** | Geo and/or segment/vertical/product mix with decision read-through (what carried growth) |
| **Peers** | ≥3 real comps with PE/ROE/growth (or lens metrics) — subject as own row; no empty peer placeholder |
| **Valuation** | Method from lens + what is priced in at current price + bull/base/bear bands (judgmental OK if labeled) |
| **Thesis** | 3–5 **falsifiable** claims (evidence + how to falsify) |
| **Risks** | Mandatory, specific, sourced — not generic boilerplate |
| **Verdict** | Restates action, confidence, and what to watch next |

### Anti-patterns (automatic fail)

- Cover + section titles + metric cards with almost no prose
- “Watchlist / moderate” with no confirm/kill criteria
- Skipping the concall because a press release existed
- Peer table with “n/a this run” for every peer
- Outlook bullets without verbatim quotes from a primary transcript/deck
- Shipping because “token discipline” said not to fetch more — **quality wins that conflict**

## Token rules (efficiency for ingest — not an excuse for thin output)

Use facts packs and disk extracts so you do **not** dump entire 300-page ARs into context. That is still required.

But:

- **Quality > tokens** when the alternative is a headings-only report.
- Pull the latest **concall + investor presentation + screener**; query widely enough to fill the quality bar.
- Prefer grepping/BM25 over loading whole files; if packs are thin after one pass, run more targeted queries — do not stop early.
- Load **one** sector lens only (`sectors/<lens-id>/`).
- On `new_quarter`, refresh deltas; still re-check decision, outlook, financials, risks.

```text
Never Read() a full AR/concall into chat as one blob.
Do use pdf_to_text + query_source / outlook_candidates until packs support a decision-grade draft.
```

## Workflow

### 0. Resolve company + cache slug

Slug = lowercase underscores (e.g. `newgen`).  
State: `~/.company-research/<slug>/` → `sources/`, `facts/`, `output/`.

### 1. Freshness

```bash
python3 <skill_dir>/scripts/freshness.py <slug> --latest-seen YYYY-MM-DD
# --force for from-scratch
```

| Status | Action |
|--------|--------|
| `no_state` / `force_full` | Full ingest |
| `new_quarter` | New concall/results + screener deltas; rebuild decision/outlook/financials |
| `up_to_date` | Reuse only if prior PDF already met the quality bar; else rebuild |

### 2. Classify sector → one lens

Read `references/sector-router.md`. Load only:

- `sectors/<lens-id>/LENS.md`
- `sectors/<lens-id>/metrics.schema.json`

```bash
python3 <skill_dir>/scripts/build_facts.py <slug> --lens <lens-id> --init-empty
```

Adapt the lens primer to the company’s real model (e.g. product/SaaS vs pure T&M) — do not paste a mismatched primer blindly.

### 3. Ingest sources (minimum set)

Follow `references/source-routing.md`. **Minimum for a first-pass decision report:**

1. Screener consolidated (price, P&L, BS, ratios, shareholding, documents)
2. **Latest concall transcript** (PDF or captions) → `pdf_to_text` / save txt
3. Latest investor presentation if filed
4. Latest results press release
5. Peer screener pages for 3–5 comps (lens peer rules)
6. Annual report only as needed for footprint/segments/litigation gaps

```bash
python3 <skill_dir>/scripts/pdf_to_text.py in.pdf sources/foo.txt --expect-name "Company"
python3 <skill_dir>/scripts/outlook_candidates.py sources/concall.txt facts/candidate_quotes/q_candidate_quotes.json
python3 <skill_dir>/scripts/query_source.py sources/concall.txt guidance margin DSO implementation annuity --max-hits 30
python3 <skill_dir>/scripts/query_source.py sources/concall.txt --bm25 "outlook margin working capital" --top-k 8
```

Fill `facts/*.json` until the quality bar can be met. Schemas: `references/facts-schemas.md`.  
Also write `facts/decision.json` (recommendation, confidence, confirm[], kill[], one_paragraph_why).

### 4. Draft — spine in `references/report-format.md`

**Order matters:** Cover → **Investment decision** → rest of spine.

Sector slots from lens + packs; everything else from packs + sourced interpretation.

Write **analysis**: what the numbers mean for the investment case. Numbers without read-through fail the quality bar.

### 5. Assemble PDF

`scripts/html_helpers.py` (`flow_diagram()`, `verdict_box()`, tables, cards, timeline).  
`scripts/charts.py` for annual/quarterly history when it clarifies the story (preferred for financial history).

```bash
python3 -m weasyprint report.html ~/.company-research/<slug>/output/<Name>_report.pdf
```

### 6. Pre-delivery self-check (mandatory)

Answer yes to all or fix:

- [ ] Could a careful reader decide invest / hold / avoid from page 1–2 alone?
- [ ] Is every major section denser than a heading + two thin bullets?
- [ ] Was the latest concall mined (quotes + mix + risks)?
- [ ] Are peers real numbers, not placeholders?
- [ ] Are confirm/kill criteria specific and observable next quarter?
- [ ] Would you be embarrassed to send this PDF to someone risking real money? If yes → rewrite.

### 7. Mark freshness + deliver

```bash
python3 <skill_dir>/scripts/freshness.py <slug> --mark-processed YYYY-MM-DD --price <price>
```

Save `.md` + `.pdf` under `output/`. Spoken summary: recommendation + one reason + one watch item — not a full re-narration.

## Situation / badge mapping

Put the **action** in the cover badge text when possible (e.g. `HOLD — WAIT FOR RE-ACCELERATION`).

- structural growth → `growth`
- compounder with solid evidence → `bull`
- digestion / early / needs confirmation → `watch`
- structural decline / red-flag heavy → `bear`
- mixed → `neutral`

## Optional calculators

- `scripts/forward_pe.py` — when lens uses PE-style valuation  
- `scripts/capacity_utilization.py` — when capacity maths exist  

## Adding a sector lens

1. `sectors/<new-id>/LENS.md` + `metrics.schema.json`  
2. Row in `references/sector-router.md`  
3. Do not weaken the decision/quality bar in the spine  

## References

- `references/report-format.md` — spine + decision section + density rules  
- `references/sector-router.md`  
- `references/source-routing.md`  
- `references/facts-schemas.md`  
- `sectors/<lens-id>/` — matched lens only  
