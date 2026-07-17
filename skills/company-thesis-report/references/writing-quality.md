# Writing quality — research memo, not tips

The deliverable is a **sell-side-style research report**: dense tables, sourced
numbers, and analytical read-throughs. It is **not** a checklist of trading tips,
positioning advice, or bullet aphorisms.

Reference intent (structure/density): Research-Advisory `report-generator` and its
Sterlite-style examples — **functionality only**, not their code or ASCII diagrams.

## Hard bans (instant fail)

- Tip-speak: “accumulate on dips”, “trim above”, “satellite/wait”, “avoid chasing”,
  “position sizing”, “entry zone for traders” as the main voice of the report.
- Sections that are only short bullets with no table and no interpreting paragraph.
- Empty or near-empty H2s.
- Dumping confirm/kill as the majority of page-2 content without a research argument.
- Average body paragraph under ~35 words (excluding table cells and status bullets).

## What “sophisticated” means here

1. **Tables carry the numbers** — multi-year annual, ≥8 quarters, segments/geo,
   peers, valuation inputs, WC/AQ. Prefer `data_table()` over prose lists of figures.
2. **Every major table is followed by analysis** — 1–3 paragraphs that answer:
   what changed, why, what it implies for the thesis (Sterlite pattern:
   “FY24–FY25 mark a downturn… Q4 alone delivered… indicating recovery accelerated”).
3. **Outlook bullets are evidence packets**, not tips — each has a headline, status
   pointer, concrete numbers, and a verbatim sourced quote when available.
4. **Decision is a research conclusion**, not a broker pitch:
   - Lead with 1 dense analytical paragraph (the argument).
   - Then falsifiers (confirm/kill) framed as **what would prove the thesis right/wrong**,
     not as trade instructions.
   - Optional judgmental bands belong in Valuation with math — not as “buy below X” tips
     in the lede unless labeled as scenario outputs.
5. **Length signal:** a serious mid-cap report should land roughly **4,000–10,000+**
   words of substance (tables + analysis), not a 2-page tip sheet.

## Section voice

| Section | Voice |
|---------|--------|
| 0 Decision | Analytical conclusion + falsifiers (research), not trade tips |
| 1 Summary | 3–5 factual sentences + cards |
| 2–3 Sector / value chain | Short primer + visual flow; no filler |
| 4 Situation | Classification + evidenced bullets |
| 5–7 Outlook | 2–4 **evidence** bullets each with `[STATUS]` + quote |
| 8–9 Customers / milestones | Named facts / timeline table |
| 10 Deep-dive | Lens metrics as tables + interpretation |
| 11–11b Financials / WC | Dense tables **then** regime/bridge paragraphs |
| 12–12b Mix / KPI | Tables + what swings the next 2 prints |
| 17 Valuation | Input table + implied growth paragraph + scenario math |
| 19 Peers | Table + 1 paragraph on premium/discount deserved |
| 23–25 Thesis / risks / verdict | Evidenced claims; risks specific to this print |

## Paragraph vs bullet

- Use bullets for: outlook status items, situation evidence, moats, risks, thesis pillars.
- Use paragraphs for: financial read-through, segment interpretation, valuation “what is
  priced in”, peer relative view, decision argument.
- Cap any single paragraph at ~10 lines; if longer, split into multiple short paragraphs
  or evidenced bullets — **do not delete substance**.

## Self-check before PDF

```bash
python scripts/validate_depth.py --slug <slug> --html output/report.html
```

Prose gates (fail = do not ship):

- Body word count (approx) ≥ 3500
- `li` / `p` ratio ≤ 2.5
- Average `<p>` word count ≥ 35
- At least one analytical paragraph immediately after the annual financials table
  (heuristic: a `<p>` following the first large `data_table` in section 11)

If the draft feels like a tip list when you skim page 2–4, rewrite — do not ship.
