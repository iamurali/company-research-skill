# Report format — decision-grade, sector-agnostic spine

Every company report uses this section order. Sector relevance comes only from the
loaded sector lens (`sectors/<lens-id>/`). **Never** put an industry name in a
permanent body heading. Never render value chain as ASCII/code — use
`html_helpers.flow_diagram()`.

## Density rule (applies to every section)

A section fails if it is only a heading plus thin labels. Each section must help the
investment decision: **what happened, why it matters, what to watch**. Prefer short
analytical paragraphs + tight bullets over empty cards.

**Depth floor:** see [depth-checklist.md](depth-checklist.md). A mid-cap report that
cannot support invest / not is a failure — thicken before shipping.

Gaps: one honest sourced line (“not disclosed in concall/PR/screener reviewed”) —
never invent filler.

---

## Cover (`cover()` + `badge()`)

Company name, ticker(s)/exchange(s), **action-oriented** badge text when possible
(e.g. `HOLD — WAIT FOR RE-ACCELERATION`), report date, price/mcap meta line.

Badge kinds: `growth` | `bull` | `watch` | `bear` | `neutral`.

---

## 0. Investment decision *(required — immediately after cover)*

This is the most important page. Use `verdict_box()` plus structured lists.

Must include:

1. **Action:** BUY / HOLD / AVOID / selective accumulate (pick one primary action)
2. **Conviction:** High / Medium / Low
3. **Horizon:** e.g. 2–3 quarters / 12 months
4. **Entry / invalidation:** price zone or condition (judgment labeled as such)
5. **Key debate:** one sentence — the single bull vs bear disagreement
6. **One dense paragraph:** why, at this price, with key evidence and key doubt
7. **Confirm thesis** (3–5 observable, dated bullets)
8. **Kill thesis** (3–5 observable, dated bullets)
9. **Alternative thesis:** what the other side believes and why you reject / partially accept
10. **Position framing:** core / satellite / wait / trim (not personalized advice)

Do not bury the call in section 25 only. Section 25 restates; section 0 decides.

---

## 1. Company Summary

What the reader owns in plain language: products/platform, how it monetizes, main
verticals/geos, scale (mcap, sales, headcount if known). Then `card_grid()` of
headline stats (mcap, price, 52w, P/E or lens multiple, ROE/ROCE as relevant).

---

## 2. Sector Context *(from loaded lens — adapted to this company)*

Not a generic paste. Cover:

- How the sector makes money
- How it should be valued (and what multiple you pay for)
- Competitive intensity
- Sector value chain via `flow_diagram()`

Call out when the company is a hybrid (e.g. product/SaaS inside an IT-Software tag).

---

## 3. Company Value Chain Positioning

Firm-specific stages + `flow_diagram()`. Backward integration / own-IP note when
disclosed.

---

## 4. Situation Classification

Opening bullet = classification; following bullets = dated evidence. Be honest if the
company is a compounder **in digestion** rather than forcing “bull growth.”

---

## 5–7. Near / Medium / Long Term outlook

Order fixed. 2–4 bullets each. Format:

`**<Headline>** \`[STATUS]\`: <claim with numbers>. "<verbatim quote>" (Source)`

Status: `[Pending]` | `[On Track]` | `[Delivered]` | `[Delayed]` | `[Missed]`.

Quotes from **concall/transcript/deck** preferred over PR alone. Drop unsupported claims.
Prefer evidence spanning **multiple quarters**, not a single print.

---

## 8. Marquee & Niche Customers

Named disclosed customers only + size/context. Concentration if disclosed. Note
customer-guidance checks.

---

## 9. Capex / Milestones / Certifications

`timeline()` or table with status. Include leadership changes and dated commercial wins
when material to the thesis.

---

## 10. Sector Deep-Dive *(from lens)*

Title from lens; body must interpret mix/metrics for the decision (not a metric dump).
Include lens must-have metrics or explicit gaps (e.g. attrition not disclosed).

---

## 11. Financial Performance Summary

Required:

- Multi-year annual `data_table()` (sales, YoY, margins, PAT) **with a regime-shift paragraph**
- **Last 8 quarters** table or chart with YoY **and** QoQ read-through
- **Earnings bridge:** what drove the latest beat/miss (volume / mix / price / geo / one-offs)
- CAGR cards
- Prefer `revenue_profit_chart` / `quarterly_trend_chart`

---

## 11b. Working capital & earnings quality *(required)*

Dedicated subsection or H2 — not a one-liner buried in BS anomalies:

- Debtor days / DSO trend (multi-year + latest)
- Inventory / creditor days when relevant
- Cash conversion cycle direction
- **CFO vs PAT** for last 3 years — is profit turning into cash?
- Any concall commentary on collections / advances / billing delays

If WC looks fine, say so with numbers — do not skip the section.

---

## 12. Segment / geography / mix deep-dive

Whenever the concall or filings give mix: table **plus** interpretation of what carried
growth and what is the swing factor for the next two quarters. This section is often
where BUY vs HOLD is decided.

---

## 12b. KPI scorecard *(required)*

Table of **≥6** operating KPIs (lens-defined) across ≥4 periods where disclosed.
Each row: metric, trend, peer/context note if available, implication for the thesis.
Examples (IT/product): annuity %, SaaS growth, logos, DSO, utilisation, attrition.
Do not invent undisclosed KPIs — gap them explicitly.

---

## 13. Commercial backlog / demand indicators

Order book / logos / named TCV / AUM / subscribers as disclosed. Distinguish stock vs flow.
Comment on whether **count vs size** of wins is changing.

---

## 14–16. Footprint / capacity analogue / TAM

Include when material; otherwise one-line gap. Do not pad.

---

## 17. Valuation

Required:

- Lens method + current multiple(s)
- **What is priced in** at today’s price (implied growth / back-of-envelope OK if labeled)
- Bull / base / bear bands with **explicit growth & margin assumptions** and probabilities
- Optional street note — paraphrase, tag as broker opinion, never as your primary finding

---

## 18. Industry Tailwinds / Headwinds

Sourced, specific to this company’s demand drivers.

---

## 19. Peer Comparison

**≥3 real peers** with screener (or equivalent) numbers — valuation **and** operating
metrics. Subject as own row. Empty “n/a this run” peer rows are a quality failure.

Add 2–4 sentences: does the subject deserve its premium/discount?

---

## 20. MOATs

Only evidenced moats. Separate real vs marketing (AI narrative, awards, etc.).

---

## 21. Technical Snapshot

As-of price, 52w, simple published stats. No invented indicators.

---

## 22. Promoter / Governance / Management scorecard

Shareholding trend; ratings/litigation/raises; **leadership transitions**.

**Management scorecard** (required block):

- Guidance delivery over last 2–4 quarters (said vs delivered)
- Capital allocation grade (dividends, buybacks, M&A, cash vs reinvestment)
- Key-person / succession risk
- Governance flags with evidence

---

## 23. Investment Thesis Summary

3–5 **falsifiable** claims: evidence now + how the claim would be falsified next quarters.

---

## 24. Key Risks

Mandatory `flag_list(..., kind='bear')`. Specific to this print (WC, growth air-pocket,
geo delays, transition, competition) — not generic macro filler only.
Include the **thesis-breaking** risks, not only mild ones.

---

## 25. Final verdict

`verdict_box()` restating action, confidence, horizon, and the single next thing to watch.
Must agree with section 0. Restate confirm/kill in one line each if space allows.

---

## 26. Sources

Numbered, linked, what each supports. Must include screener + **latest concall** (or
explicit failure to obtain transcript) + peer sources used.

---

## Charts (required)

≥3 Plotly figures before assembly: price/context, financial trend, valuation and/or
WC/KPI. Export under `output/`.

---

## Paragraph discipline

- Prefer analysis paragraphs ≤ ~10 lines; then bullets.
- Never mention internal script paths in the report text.
- Target feel: institutional memo depth (~2,500–5,000+ words of analysis + tables),
  not a 1–2 page brief, unless the user asked for a short memo.

## Assembly sketch

```python
body = ''
body += cover(...)
body += section('0. Investment decision')
body += verdict_box('Recommendation: ...')
# confirm / kill / alternative thesis
body += section('1. Company Summary')
# ... through section 26 ...
html = render(body, '<skill_dir>/assets/report_style.css')
```
