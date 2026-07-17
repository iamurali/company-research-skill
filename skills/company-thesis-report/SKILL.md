---
name: company-thesis-report
description: "Generates a research-grade investment advisory PDF for a listed company using a fixed sector-agnostic section spine, a token-efficient facts-pack pipeline (never load full concalls/ARs into context), and one matched sector lens from sectors/ for Sector Context, Sector Deep-Dive, metrics, and valuation. Use when the user asks to research a company, build a thesis, deep-dive a stock, or evaluate buy/hold/sell — even for a bare ticker."
---

# Company thesis report (research-grade, token-efficient)

## Why this exists

A decision-useful report needs sourced facts, an honest bear case, and the **right sector lens** — without burning a context window on full transcripts and annual reports. This skill:

1. Extracts sources to disk and drafts only from small **facts packs**
2. Uses a **fixed section spine** (predictable format)
3. Loads **one** sector lens under `sectors/<lens-id>/` for sector-specific analysis
4. Renders a visual PDF (WeasyPrint) with a **styled value-chain diagram** — never ASCII/code

Discipline: a claim without a source and a date is marketing, not evidence.

## Token rules (non-negotiable)

- **Never** `Read()` a full concall, deck, or annual report into context.
- Extract with `scripts/pdf_to_text.py`, then `scripts/query_source.py` / `scripts/outlook_candidates.py`.
- Draft each section from `~/.company-research/<slug>/facts/*.json` only.
- Load **one** sector lens per run — never the whole `sectors/` tree.
- Prefer screener.in structured pages over re-parsing AR tables.
- On `new_quarter`, refresh deltas only; carry forward stable packs (sector primer, value chain, footprint, peers) unless evidence changed.

## Workflow

### 0. Resolve company + cache slug

Slug = lowercase company name with underscores (e.g. `td_power_systems`).
Working state: `~/.company-research/<slug>/` (`sources/`, `facts/`, `output/`).

### 1. Freshness

From screener Documents/Concalls, resolve the **full date** of the latest results/concall (`YYYY-MM-DD`).

```bash
python3 <skill_dir>/scripts/freshness.py <slug> --latest-seen YYYY-MM-DD
# or --force for from-scratch
```

| Status | Action |
|--------|--------|
| `no_state` / `force_full` | Full ingest + all packs |
| `new_quarter` | New concall/results + last 1–2 screener columns; delta packs |
| `up_to_date` | Reuse report; optional price-only valuation refresh |

### 2. Classify sector → load one lens

Read `references/sector-router.md`. Set `sector_lens_id` in `facts/meta.json`.
Then open **only**:

- `sectors/<lens-id>/LENS.md`
- `sectors/<lens-id>/metrics.schema.json`

```bash
python3 <skill_dir>/scripts/build_facts.py <slug> --lens <lens-id> --init-empty
```

### 3. Ingest sources to disk

Follow `references/source-routing.md`. Typical set:

- screener consolidated page (numbers, shareholding, documents links)
- latest concall transcript PDF (or YouTube captions if REC-only)
- latest investor presentation
- latest annual report when needed for footprint/segments/litigation

```bash
python3 <skill_dir>/scripts/pdf_to_text.py in.pdf sources/foo.txt --expect-name "Company"
python3 <skill_dir>/scripts/outlook_candidates.py sources/concall.txt facts/candidate_quotes/q_candidate_quotes.json
python3 <skill_dir>/scripts/query_source.py sources/foo.txt KEYWORD [KEYWORD...]
# or: python3 <skill_dir>/scripts/query_source.py sources/foo.txt --bm25 "order book guidance"
```

Merge hits into packs via `build_facts.py --hits hits.json` and by editing the small JSON packs. Schemas: `references/facts-schemas.md`.

### 4. Draft `report.md` from packs

Section contract: `references/report-format.md` (fixed spine).

**Sector-filled slots (from lens + packs):**

- Sector Context ← `LENS.md` primer + `facts/sector.json`
- Sector Deep-Dive ← lens deep-dive template + `facts/sector_overlay.json`
- Financial metric cards / valuation method / peer columns ← lens overlay

**Universal slots** ← corresponding facts packs.

Gaps: one honest line, no invented filler. No industry-named permanent headings.

### 5. Assemble PDF

Use `scripts/html_helpers.py` (including **`flow_diagram()`** for value chains — never ASCII) and `assets/report_style.css`. Charts in `scripts/charts.py` are opt-in.

```bash
python3 -m weasyprint report.html ~/.company-research/<slug>/output/<Name>_report.pdf
```

Verify WeasyPrint import first; `pip install weasyprint matplotlib --break-system-packages` if needed.

### 6. Mark freshness + deliver

```bash
python3 <skill_dir>/scripts/freshness.py <slug> --mark-processed YYYY-MM-DD --price <price>
```

Save both `.md` and `.pdf` under `output/`. Spoken summary: 1–2 sentences on situation + verdict — do not re-narrate the whole report.

## Situation badge mapping

- structural growth → `growth`
- compounder / evidenced turnaround → `bull`
- cyclical / early / thin evidence → `watch`
- structural decline / red-flag heavy → `bear`
- mixed → `neutral`

## Optional calculators

- `scripts/forward_pe.py` — only if the **loaded lens** uses PE-style valuation
- `scripts/capacity_utilization.py` — when capacity maths are disclosed

## Adding a sector lens

1. Add `sectors/<new-id>/LENS.md` + `metrics.schema.json`
2. Add a row to `references/sector-router.md`
3. Do **not** change the report spine

## References (read when needed, not all at once)

- `references/report-format.md` — spine + visual rules
- `references/sector-router.md` — classification
- `references/source-routing.md` — cheapest source per need
- `references/facts-schemas.md` — pack shapes
- `sectors/<lens-id>/` — only the matched lens
