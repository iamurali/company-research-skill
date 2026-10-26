---
name: "company-research-canvas"
description: "Build a themed, interactive HTML research canvas for an Indian listed company (industry, verticals, promoters, policy, triggers, J-curve, KPI timeline, risks), published as an artifact. Use when asked for a company canvas or deep-dive page."
---

# Company Research Canvas

Produces one self-contained HTML page, visually themed to the company's own world, covering a fixed nine-section spine. Published with the Artifact tool. Use this instead of the PDF report skills when the user asks for a "canvas", "HTML", "page", or "similar report" to earlier canvases (e.g. Kanohar Electricals, Axiscades).

Input: a company name or NSE/BSE ticker. Optional: uploaded annual reports, concall transcripts, rating reports, Discord PDFs.

## 1. Research protocol (do this before writing any HTML)

Work through sources in this priority order. Official documents win over everything else.

1. **User-supplied files** (annual report, transcripts, Discord notes/PDFs). Read them fully first.
2. **Exchange filings** on nsearchives.nseindia.com / bseindia.com: latest investor presentation, press release, results, Reg 30 order wins, acquisitions, shareholding changes, credit-rating intimations. Search `"<company> investor presentation Q<n> FY<yy>"` and fetch the PDF directly.
3. **Annual report** (latest year). If the company listed recently, use the **RHP/DRHP** restated financials instead and say so.
4. **Concall transcript** (or a credible summary if the transcript is not reachable). Capture management guidance and Q&A answers verbatim where possible; these are the "real-time promoter responses".
5. **Credit rating rationales** (CRISIL, CARE, ICRA, India Ratings). Fetch the latest and the rating history; note upgrades, watches, sensitivities, working-capital days, liquidity.
6. **Community / independent research**: search `"<company> valuepickr"`, `"<company> substack"`. Use only if found; never imply you used a source you could not find.
7. **Credible web**: broker IPO/result notes (Arihant, SMC, ICICI Direct, DSIJ), Business Standard, shareholding (Trendlyne), share price (Business Standard / NSE), sector policy (budget, CEA, ministry releases).

Always fetch: current share price + date, market cap, 52-week range, latest quarter results, latest order book, shareholding trend with pledge %, any promoter buying/selling in the last 12 months.

### Data discipline
- Every number traces to a source. Label any arithmetic you did on company data as **(derived)**.
- When sources conflict (e.g. revenue vs total income, two deal values), pick the official one and note the conflict in a small source line.
- Prefer the company's own segment names and terms of art.
- Use the current date in searches; anything that could have changed since training must be looked up.
- If a key document cannot be fetched (CDN blocks, paywall), say which one in the footer coverage note and what replaced it.

## 2. The nine-section spine (fixed order)

Hero (always first): company name, ticker chips (NSE/BSE, HQ, listing/CMP date), a 6-tile spec strip (revenue + growth, margin, profit/ROE, order book or visibility, capacity or key operating metric, credit rating), and a 3–4 sentence thesis in plain language that names the single most important fact.

1. **Industry & positioning across the value chain** — what the product does in one plain sentence; market size table (CY/FY, CAGR, which segments the company plays); why entry barriers exist; a 5-step value-chain strip with the company's links highlighted; listed peer table with overlap/edge/gap.
2. **Business verticals deep dive** — revenue mix bars (by product, by voltage/class/geography as relevant); then one product card per vertical: schematic inline SVG illustration (labelled as schematic, not a photo), status pills, 3 key-value facts, plain-language description of what it is, and a "Final application" box naming end users/programmes. Include order-book split and plant/utilisation if manufacturing. Include what is being sold/exited if relevant.
3. **Promoter skin in the game & history** — who the promoters are (generations, education, roles, relationships); holding trend bars incl. pledge; OFS/selling or buying with amounts and dates; remuneration quirks; governance flags; a vertical company timeline with key milestones highlighted.
4. **Government initiatives / policies / tailwinds** — 6 policy cards, each with a figure, what it means for this company, and a relevance pill (Direct / Indirect / Timing risk).
5. **Key growth triggers table** — columns: Trigger, What it unlocks, Status & evidence, Timeline, State pill. Colour code: green Done/On track, amber In progress, red Not started/At risk, grey Dormant/Long-dated. Include management guidance as triggers.
6. **J-curve** — answer the question directly. Show either an actual chart (margin/utilisation history) if the J already happened, or a schematic curve (clearly labelled illustrative) if it is ahead. List evidence for the dip and for the upswing, end with a one-paragraph verdict.
7. **KPIs on a quarterly horizontal timeline** — horizontally scrollable row, ~9 columns from the last reported quarter to 2–3 years out. Each column: dot (green = reported, accent = current/next, neutral = future), dates, and 3–5 chips typed as Actual (green edge), Target/guidance (accent edge), Event (neutral edge: lock-in expiry, results, deal closings, capex go-live).
8. **Key risks & mitigating actions** — columns: Risk, Evidence (numbers), Mitigation (what the company is doing), Closure / check date, Severity pill (High/Medium/Low). Always cover cash conversion/working capital, concentration, execution, promoter behaviour, valuation, and any company-specific issue.
9. **Financial track record** — 3–4 years + last two quarters + guidance column; margins, PAT, cash flow, working-capital days, order book. Note the basis.

Footer: coverage note (which source types were found / not found / unreachable), numbered source links, "derived" definition, "personal research canvas, not investment advice".

## 3. Design rules

Load the `artifact-design` skill before writing. Then:

- **Theme the page to the company's physical world.** Pick one metaphor from the subject: e.g. a transformer rating plate + copper accent for a transformer maker; an avionics mission display with a radar sweep + signal-amber accent for defence electronics; a pharma batch record, a cement kiln gauge, a shipping manifest, etc. The section labels follow the metaphor ("BAY 01", "CH-01"). Never reuse the previous canvas's palette or fonts for a new company.
- One accent colour, one structural colour, deliberately tinted neutrals; full light + dark token sets per the artifact contract. Semantic good/warn/bad/idle colours are separate from the accent.
- Three Google Fonts roles: a characterful condensed/technical display face, a readable body face, a mono for numbers and labels. `tabular-nums` wherever numbers align.
- Components to reuse: spec strip, value-chain strip, data tables in `overflow-x:auto` wrappers, status pills, horizontal bar rows, stacked bar with legend, product cards (SVG art left, body right, stacking on phone), vertical history timeline, horizontal KPI timeline, callout box.
- Product illustrations: simple inline SVG built from tokens (no external images; the CSP blocks them). Say in the section lede that they are schematic.
- Phone width must work: grids collapse, only tables and the KPI timeline scroll sideways.
- Copy: plain language a non-engineer understands ("a transformer works like a pressure valve for electricity"), short sentences, no hype.

### Reference examples

Two finished canvases live in `examples/`: `kanohar-electricals.html` (transformer rating-plate theme, copper accent) and `axiscades-technologies.html` (avionics mission-display theme, signal-amber accent). Read one before writing a new canvas to match the depth and component set, then pick a new theme for the new company.

## 4. Build & publish

1. Write the page to the scratchpad as `<company-slug>.html` with `<title>` = "<Company> Canvas" (or the company's short name + Canvas).
2. Re-check a few numbers against sources and fix contradictions before publishing.
3. Publish with the Artifact tool: one generic `icon` word (chart, radar, factory…) and a one-sentence `description`.
4. For updates, republish the same file path.

## 5. Final reply

- One sentence on what the canvas is.
- 3–4 bullets with the most decision-relevant findings (thesis, biggest trigger, biggest risk, J-curve verdict).
- Coverage gaps: which requested source types (annual report, transcript, rating, ValuePickr, Discord, Substack) were or were not found/readable.
- A "Sources:" list of markdown links.
- Do not paste the artifact URL.