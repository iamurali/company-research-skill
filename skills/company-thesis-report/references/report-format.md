# Report format — decision-grade, sector-agnostic spine

Every company report uses this section order. Sector relevance comes only from the
loaded sector lens (`sectors/<lens-id>/`). **Never** put an industry name in a
permanent body heading. Never render value chain as ASCII/code — use
`html_helpers.flow_diagram()`.

## Density rule (applies to every section)

A section fails if it is only a heading plus thin labels. Each section must help the
investment decision: **what happened, why it matters, what to watch**. Prefer short
analytical paragraphs + tight bullets over empty cards.

Gaps: one honest sourced line (“not disclosed in concall/PR/screener reviewed”) —
never invent filler.

---

## Cover (`cover()` + `badge()`)

Company name, ticker(s)/exchange(s), **action-oriented** badge text when possible
(e.g. `HOLD — WAIT FOR RE-ACCELERATION`), report date, price/mcap meta line.

Badge kinds: `growth` | `bull` | `watch` | `bear` | `neutral`.

---

## 0. Investment decision *(required — immediately after cover)*

This is the most important page. Use `verdict_box()` plus two short lists.

Must include:

1. **Action:** BUY / HOLD / AVOID / selective accumulate (pick one primary action)
2. **One dense paragraph:** why, at this price, with the key evidence and the key doubt
3. **Confirm thesis** (3–5 observable bullets that would upgrade conviction / move toward BUY)
4. **Kill thesis** (3–5 observable bullets that would force AVOID / exit)
5. **Confidence:** high / medium / low on the action itself

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

- Multi-year `data_table()` (sales, YoY, margins, PAT)
- **Read-through paragraph** (is this growth, margin, or air-pocket?)
- CAGR cards
- BS/cash anomaly bullets (debtor days, leverage, FCF)
- Prefer `revenue_profit_chart` / `quarterly_trend_chart` when history clarifies the story

---

## 12. Segment / geography / mix deep-dive

Whenever the concall or filings give mix: table **plus** interpretation of what carried
growth and what is the swing factor for the next two quarters. This section is often
where BUY vs HOLD is decided.

---

## 13. Commercial backlog / demand indicators

Order book / logos / named TCV / AUM / subscribers as disclosed. Distinguish stock vs flow.

---

## 14–16. Footprint / capacity analogue / TAM

Include when material; otherwise one-line gap. Do not pad.

---

## 17. Valuation

Required:

- Lens method + current multiple(s)
- What is priced in at today’s price
- Bull / base / bear bands (label as judgmental if not street targets)
- Optional street note — paraphrase, tag as broker opinion, never as your primary finding

---

## 18. Industry Tailwinds / Headwinds

Sourced, specific to this company’s demand drivers.

---

## 19. Peer Comparison

**≥3 real peers** with screener (or equivalent) numbers. Subject as own row. Empty
“n/a this run” peer rows are a quality failure — fetch peer pages.

Add 2–4 sentences: does the subject deserve its premium/discount?

---

## 20. MOATs

Only evidenced moats. Separate real vs marketing (AI narrative, awards, etc.).

---

## 21. Technical Snapshot

As-of price, 52w, simple published stats. No invented indicators.

---

## 22. Promoter / Governance

Shareholding trend; guidance reliability; ratings/litigation/raises; **leadership
transitions** when material.

---

## 23. Investment Thesis Summary

3–5 **falsifiable** claims: evidence now + how the claim would be falsified next quarters.

---

## 24. Key Risks

Mandatory `flag_list(..., kind='bear')`. Specific to this print (WC, growth air-pocket,
geo delays, transition, competition) — not generic macro filler only.

---

## 25. Final verdict

`verdict_box()` restating action, confidence, and the single next thing to watch.
Must agree with section 0.

---

## 26. Sources

Numbered, linked, what each supports. Must include screener + latest concall (or explicit
failure to obtain transcript).

---

## Paragraph discipline

- Prefer analysis paragraphs ≤ ~10 lines; then bullets.
- Never mention internal script paths in the report text.

## Assembly sketch

```python
body = ''
body += cover(...)
body += section('0. Investment decision')
body += verdict_box('Recommendation: ...')
# confirm / kill lists
body += section('1. Company Summary')
# ... through section 26 ...
html = render(body, '<skill_dir>/assets/report_style.css')
```
