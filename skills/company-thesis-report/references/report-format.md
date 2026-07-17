# Report format — fixed sector-agnostic spine

Every company report uses this section order. Sector relevance comes only from the
loaded sector lens (`sectors/<lens-id>/`), which fills **Sector Context**,
**Sector Deep-Dive**, metric card overlays, valuation method, and peer rules.
**Never** put an industry name in a permanent body heading. Never render value
chain as ASCII/code blocks — always use `html_helpers.flow_diagram()`.

Gaps are data-driven: write one honest line (“not disclosed” / “not material for
this lens”), never invent filler and never “skip industry heading X.”

## Cover (`cover()` + `badge()`)

Company name, ticker(s)/exchange(s), situation badge, report date.

Badge kinds: `growth` | `bull` | `watch` | `bear` | `neutral`.

## 1. Company Summary

3–5 short sentences: what the company does, sector/industry label, listing age or
history hint, exchanges, market cap. Follow with a `card_grid()` of 3–4 headline
stats (market cap, price, 52-week range, sector). Source from screener About +
structured widgets — never invent a description.

## 2. Sector Context *(from loaded lens)*

Filled entirely by the sector lens primer + any sparse market facts in the
`sector` facts pack. Cover:

- What this sector does and how it operates
- How the sector is typically valued
- Sector-level value chain (visual `flow_diagram()` if the lens provides stages)
- Competitive intensity / market structure

Do not re-derive a sector primer from scratch every run when the lens already has one.

## 3. Company Value Chain Positioning

Firm-specific placement inside its industry. Short bullets or a short lead-in,
then **always** a visual `flow_diagram()` with stages such as Upstream → Company
→ Downstream → End market. Capture backward integration on the Company stage when
disclosed. **No ASCII/code diagrams.**

## 4. Situation Classification

Bullets, not a wall of prose. Opening bullet = classification; following bullets =
evidence. Classifications: distress recovery / turnaround · steady compounder ·
cyclical · structural growth · structural decline / red-flag heavy · or an honest mix.

## 5–7. Near / Medium / Long Term outlook

Three sections in this order:

1. `Near Term (Next 1 to 2 Quarters)`
2. `Medium Term (6 to 12 Months)`
3. `Long Term (1+ Years)`

2–4 bullets each. Format:
`**<Headline, 3-6 words>** \`[STATUS]\`: <claim with numbers>. "<verbatim quote>"`

Status pointers: `[Pending]` | `[On Track]` | `[Delivered]` | `[Delayed]` | `[Missed]`.
Quotes must be verbatim from a sourced document. If no quote supports a claim, drop it.
Draft from `facts/outlook.json` — never by reading a full transcript into context.

## 8. Marquee & Niche Customers

2–5 bullets naming disclosed customers only. Include concentration % if disclosed.
State when customer-own guidance was checked and not found.

## 9. Capex / Milestones / Certifications

Chronological table or `timeline()`: Date/Quarter | Milestone | Status | Amount | Source.
Roll up other dated commitments from elsewhere in the report with a one-line cross-ref.

## 10. Sector Deep-Dive *(from loaded lens)*

**Title and body come from the loaded lens** (`LENS.md` deep-dive template +
`facts/sector_overlay.json`). This is where sector-specific analysis lives
(asset quality for a bank lens, pipeline/service mix for a healthcare-manufacturing
lens, programme exposure for a defence lens, etc.). The format spec itself never
names those industries.

## 11. Financial Performance Summary

Table of recent years/quarters: Revenue, YoY %, margins, PBT/PAT as disclosed.
Optional CAGR `card_grid()`. Add lens-required metric cards from the overlay.
Include a one- or two-line balance-sheet anomaly check (or explicitly “none found”).
Prefer `data_table()` over charts by default; charts are opt-in.

## 12. Segment-wise Performance

Only if segment disclosure exists. Always a table (one table per disclosed basis).
Include exports vs domestic when disclosed informally.

## 13. Commercial backlog / demand indicators

Include when material for this lens or clearly disclosed (order book, AUM,
subscribers, bookings, etc.). Table with as-of date. If not material/disclosed,
one-line note.

## 14. Operating footprint

Plants, branches, stores, network nodes — whatever the business actually discloses.
Bullets, one fact per location/node. Raw-material domestic/import split when disclosed.

## 15. Capacity / utilization (or sector analogue)

Native physical unit first (or the analogue the lens defines: credit growth, CASA,
occupancy, PLF, etc.). Flag shared multi-purpose pools when relevant.

## 16. Market opportunity / TAM

Only if a real disclosed figure exists (not a vague growth rate). State source and as-of.

## 17. Valuation

Method **from the lens** (P/B + RoA for banks, EV/EBITDA, forward PE, etc. — not
always PE). Show inputs, as-of price, and any historical median multiple if available.
Use `scripts/forward_pe.py` only when the lens calls for that method.

## 18. Industry Tailwinds / Headwinds

Short bullets, sourced. Prefer sector lens framing + recent primary evidence.

## 19. Peer Comparison

3–5 peers per lens peer rules. Reporting company as its own row. Columns = lens metrics.

## 20. MOATs

Bullets only. Entry barriers, switching costs, network, cost, regulatory — only if
sources support them. Never invent a moat.

## 21. Technical Snapshot

Table or bullets (price, ranges, simple published technicals if available). Never prose.
Always include as-of date. Skip invented indicators.

## 22. Promoter / Governance Track Record

Shareholding trend table; guidance reliability from outlook history; credit ratings;
litigation; material fund raises. Plain language — no internal script names in the report.

## 23. Investment Thesis Summary

Bullets, one claim per bullet, each evidenced. Or an honest “research does not yet
support a real thesis.”

## 24. Key Risks

Mandatory. `flag_list(..., kind='bear')`. Carry through rating downgrades, litigation,
concentration, high utilization, sector-specific risks from the lens.

## 25. Verdict

`verdict_box()` — situation, strongest evidence, biggest open question, honest confidence.

## 26. Sources

`sources_list()` — numbered, hyperlinked, short note each. Traceability from
`facts/quotes.json` / source manifest.

## Paragraph / bullet discipline

- No paragraph longer than ~10 lines at body width — convert to bullets.
- Claims need a source and a date (or as-of). Marketing adjectives alone are not evidence.
- Never mention internal tooling paths or script names in the report text.

## Assembly sketch

```python
import sys
sys.path.insert(0, '<skill_dir>/scripts')
from html_helpers import *

body = ''
body += cover(...)
body += section('1. Company Summary')
# ... concatenate builders per this spine ...
# Company + sector value chains:
body += flow_diagram([('Upstream', '...'), ('THE COMPANY', '...'), ...])
html = render(body, '<skill_dir>/assets/report_style.css')
```

Then: `python3 -m weasyprint report.html report.pdf`
