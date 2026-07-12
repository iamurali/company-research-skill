---
name: company-thesis-report
description: "Generates a rigorous, decision-useful investment research report on any publicly listed company as a visual, infographic-style PDF - metric cards, charts for financial/ownership trends, a timeline for dated milestones, and data tables for detail, built for fast scanning without losing any underlying data. Covers business overview, financial history, ownership/capital structure, the situation driving interest in the stock, the bull thesis with evidence, dated management promises, a mandatory red-flags/bear-case section, a verdict, and sourced citations. Use whenever the user asks to research a company for an investment decision, build a thesis, do a deep dive on a stock, evaluate a buy/hold/sell, or wants a writeup on a company - even if they just name a ticker and say 'what's the story with X', without asking for a 'report' or using investment jargon. Works for any situation - turnaround, compounder, cyclical, growth story, or decline."
---

# Company thesis report

## Why this exists

A good investment decision needs a document you can actually rely on later - one where every number traces back to a primary source, where the bear case gets the same rigor as the bull case, and where "I couldn't find solid evidence for X" is written down honestly instead of papered over with vague optimism. This skill produces that document for any company, in any situation - as a visual, fast-to-scan PDF rather than a wall of prose.

The single most important discipline here: **a claim without a source and a date is not evidence, it's marketing**. Treat every fact this way whether it makes the thesis look better or worse. The second discipline: **visual and complete are not in tension** - a chart or metric card should make a number easier to absorb, never a replacement for showing the real figures. If something doesn't chart well, put it in a text paragraph or a dense table instead of forcing a bad visual or dropping the data.

## Step 1: Research (before touching the output format)

Do the research first. Do not open the format/build references below or start building the document until you have gathered real facts - reading the format before you have content anchors you on document mechanics instead of substance.

Gather, in roughly this order of trust:

1. **Primary sources** - exchange filings (BSE/NSE Regulation 30 disclosures, annual reports, investor presentations filed with the exchange), NCLT/court orders if relevant, credit rating agency actions (CRISIL/ICRA/CARE/India Ratings press releases), and the company's own investor call transcripts or press releases as filed.
2. **Structured financial data** - screener.in (P&L, balance sheet, cash flow, ratios, shareholding pattern history), or an equivalent financial data source. Pull the full history, not just the latest quarter - the charts in Step 3 need real time series.
3. **Discovery-only sources** - news aggregators, PR-syndicated releases, sites like Trendlyne or Moneycontrol. Fine for finding leads (a contract win, a rating action, a management interview) but never cite a number from them without tracing it back to the primary filing or press release it originated from. Aggregators garble numbers surprisingly often - verify before including.

If the user has given you Kite (Zerodha) access in this session, use it for live price/volume history rather than guessing at technicals from search snippets.

### Sourcing rules - non-negotiable

- Every material fact (financial figures, investor names, amounts, dates, contract values, guidance) must trace to a source you can cite with a URL.
- No vague qualifiers as evidence - "strong pipeline," "well-positioned," "attractive valuation" are not facts unless attached to a number, a date, and a source.
- Flag unverified management claims explicitly: "management states X - not yet corroborated by an independent filing."
- **If, after real research, you cannot find enough verifiable material to support a genuine thesis, say so plainly rather than padding it out.** A report that honestly concludes "there isn't a well-evidenced thesis here yet" is more useful than one that manufactures a story. This applies per-section too - if the red-flags section only has one weak flag, write one weak flag, don't invent three to look thorough.

## Step 2: Identify the company's situation

Before writing the thesis, figure out - from the evidence, not from assumption - which broad situation the company is actually in right now. This determines the framing and the badge color used on the cover (see Step 3). Common situations:

- **Distress recovery / turnaround** - was in real financial trouble (debt default, NCLT resolution, negative net worth, trade-to-trade classification) and has since had a documented reset.
- **Steady compounder** - consistent revenue/profit growth, stable or improving margins and returns on capital, no major structural change - the thesis here is about durability and reasonable valuation, not a catalyst.
- **Cyclical** - earnings and stock price move with a commodity price, interest rate, or capacity-utilization cycle; the thesis is about where in the cycle the company sits now.
- **Structural growth** - riding a multi-year secular trend (market share gains, new product category, geographic expansion) with evidence of execution, not just narrative.
- **Structural decline / red-flag heavy** - genuine deterioration with no credible turnaround evidence yet. It is completely fine, and expected sometimes, for the report to conclude this and recommend against building a thesis at all.

State which situation applies (or a mix) early in the report, with the evidence for that classification. Don't force a "turnaround" or "growth story" framing onto a company that's actually just declining, and don't force red flags onto a genuinely boring, healthy compounder just to fill a section.

## Step 3: Build the report as a PDF

Once research is solid, read `references/report-format.md` for the exact section structure and how each section maps to a chart, a card grid, a table, or plain text. Then use the two bundled Python modules:

- `scripts/charts.py` - matplotlib chart generators (revenue/profit history, quarterly trend, shareholding pattern, before/after comparison, capital-raise donut, line comparisons) that each save a PNG in the report's visual style.
- `scripts/html_helpers.py` - functions that build the HTML for covers, badges, metric-card grids, chart embeds, data tables, bullet flag-lists, timelines, a verdict box, and a sourced citation list, all styled by `assets/report_style.css`.

Assemble the page as HTML (concatenate the section builders per `references/report-format.md`), then render to PDF with WeasyPrint:

```bash
python3 -m weasyprint report.html report.pdf
```

(WeasyPrint may need installing first: `pip install weasyprint --break-system-packages`.)

**Decide per section whether a chart, a table, or plain text is the right call** - don't force every section into a chart. Long time series with a clear trend (revenue history, shareholding mix, margin trend) chart well. A one-off list of named investors with exact amounts, or a detailed annexure of every allottee, is genuinely better as a dense table - charting it would lose precision the reader needs. Narrative sections (the thesis argument, red flags, the situation writeup) stay as text - don't invent a chart just to have one on the page.

Verify the rendered output before delivering it: convert (already done above) and render a few pages to JPEG (`pdftoppm -jpeg -r 120 report.pdf page`) to visually check charts aren't clipped, tables aren't overflowing the page width, and page breaks land sensibly - the same verification step used for any PDF deliverable.

## Step 4: Deliver

Save the final `.pdf` to the outputs folder, present it to the user, and give a short spoken summary - one or two sentences on what situation the company is in and the headline verdict. Don't re-narrate the whole report in the chat response; the document is the deliverable.
