# Report format, section-by-section

Adapt section titles and content to the company's actual situation (identified in Step 2 of SKILL.md) - the section *purposes* below are fixed, but don't force template language or a template chart onto content that doesn't fit. A steady compounder doesn't need a "debt resolution" chart; a distressed company might not have much of a growth roadmap to timeline. Omit or merge sections that genuinely don't apply rather than writing filler.

For each section below: **which visual, and why**. If the described chart type doesn't fit the actual data you found, use your judgment - the goal is always "easiest to scan without losing precision," not "must contain a chart."

## Cover (`cover()`)

Company name, ticker(s) and exchange(s), a `badge()` for the situation classification (bull/growth for compounder or growth story, watch for cyclical or early-stage turnaround, bear for distress/decline), report date. One line only per field - this page exists to be read in five seconds.

## 1. How this came onto the radar (if applicable)

Plain text. If the company surfaced from a specific screen or trigger (a shareholding shift, a news event, a user request), state the mechanism and the raw numbers that triggered it, as a small `data_table()` if there are several metrics. Skip this section entirely if the user just asked for research on a company with no prior screening step.

## 2. Business overview

Plain text, 2-3 short paragraphs: what the company actually does, segment mix if relevant, brief history. A `card_grid()` of 3-4 headline stats (market cap, price, 52-week range, sector) works well right under this section as an at-a-glance anchor before the reader gets into the weeds.

## 3. Financial history

The backbone of the report, and the section where charts do the most work:

- **Annual revenue and profit** - `revenue_profit_chart()`, the two-panel bar chart. Use the full history available (10 years if screener.in has it), plus TTM. This one chart usually tells the whole growth/decline story faster than any paragraph.
- **Quarterly trend** - `quarterly_trend_chart()` if there's a recent inflection worth showing quarter by quarter (a turnaround's margin recovery, a cyclical's swing). Skip if the quarterly data is unremarkable and the annual chart already tells the story.
- **Balance sheet snapshot** - a `data_table()` for the raw numbers (equity, reserves, borrowings, total assets) across recent periods. If there's a structural break to show (a recapitalization, a deleveraging), also use `before_after_chart()` for the headline metrics (net worth, total debt) - the visual contrast lands harder than a table row.
- **Key ratios** - `card_grid()` for the 3-4 ratios that matter most to *this* situation (debtor days and interest coverage for distress; ROCE/ROE trend for a compounder; utilization or realizations for a cyclical), plus a `data_table()` if there are more than 4 or a multi-year trend worth preserving.
- **Compounded growth rates** (10yr/5yr/3yr/TTM revenue and profit CAGR) - a small `card_grid()`. These single numbers are often the fastest way to see the shape of the story and deserve to be visually prominent, not buried in a paragraph.

## 4. Ownership and capital structure

- **Shareholding pattern trend** - `shareholding_chart()`, the stacked bar of Promoter/FII/DII/Public % over several quarters. This is almost always worth charting - the shape of the stack over time (a promoter block growing, FII entering) is much faster to read visually than a table of percentages.
- **Capital raise / ownership change detail** - if there's a specific recent event (preferential allotment, QIP, block deal, promoter stake change), give the full named-investor detail as a `data_table()` (don't summarize away individual names/amounts - that's exactly the kind of precision a chart would lose), and optionally a `donut_chart()` if there are enough distinct investors that a proportional breakdown adds insight beyond the table. If specific named investors participated, list them individually - named, verifiable backers are a real signal; anonymous ones are not.
- Promoter pledge status, if any, as a `card_grid()` metric.

## 5. The situation / catalyst

Plain text. State plainly which situation (Step 2 of SKILL.md) applies and why, with the evidence. This is where a debt-resolution mechanism, a new product cycle, a management change, a cyclical inflection, or a structural decline gets explained on its own terms. No forced chart here - this section is the argument, not the data.

## 6. The thesis

Plain text, structured as a sequence of evidenced claims (works well as short paragraphs or a `flag_list(..., kind='bull')` if the claims are cleanly separable bullets), each with a source. This should read as "here is the specific, falsifiable argument for why this could work," not general enthusiasm.

## 7. What's promised / roadmap

`timeline()` for any dated, verifiable commitments or milestones from management (a delivery date, a capacity expansion timeline, a debt-repayment deadline). Mark each item's status honestly (`done`, `pending`, or blank for aspirational-but-undated). If management has given no concrete guidance at all, say so in a plain-text paragraph instead of forcing an empty timeline - that absence is itself useful information.

## 8. Red flags / bear case

`flag_list(..., kind='bear')` - mandatory, even for a report that's otherwise bullish. What's unproven, what could go wrong, what a skeptic would point to. If the company is genuinely troubled, this section (not Section 6) should dominate the report, and the verdict should say so plainly.

## 9. Verdict

`verdict_box()` - one or two sentences: what situation this is, the single strongest piece of evidence for the thesis, and the single biggest open question or risk. State confidence honestly - "well-evidenced but early," "speculative," "not enough here for a real thesis" are all legitimate verdicts.

## 10. Sources

`sources_list()` - every URL cited, numbered, hyperlinked, each with a short note on what it supports.

## Assembly

```python
import sys
sys.path.insert(0, '<skill_dir>/scripts')
from charts import revenue_profit_chart, quarterly_trend_chart, shareholding_chart, before_after_chart, donut_chart, line_compare_chart
from html_helpers import *

body = ''
body += cover('Company Name', 'NSE: TICKER | BSE: 000000', badge('STEADY COMPOUNDER', 'bull'), 'Report date: 11 July 2026')
body += section('2. Business overview')
body += para('...')
body += card_grid([('Market cap', 'Rs X Cr', ''), ('P/E', 'Nx', ''), ...])
body += section('3. Financial history')
revenue_profit_chart('rp.png', years, revenue, profit)
body += chart_block('rp.png', 'Annual revenue and net profit. Source: screener.in')
# ... etc through section 10 ...

html = render(body, '<skill_dir>/assets/report_style.css')
open('report.html', 'w').write(html)
```

Then: `python3 -m weasyprint report.html report.pdf`

Save chart PNGs to a working directory alongside the HTML (relative paths), and delete them (along with the intermediate HTML) after the PDF is built and verified - only the final PDF should remain in the outputs folder.

## Two easy mistakes to avoid

- WeasyPrint needs `pip install weasyprint --break-system-packages` if it's not already present in the environment - check before assuming it's missing.
- `data_table()`'s `total_row_index` bolds one row (typically a "Total" summary row) - pass the row's index within `rows`, not counting the header.
