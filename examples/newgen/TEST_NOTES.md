# Newgen pipeline test (2026-07-17)

Exercise of the redesigned `company-thesis-report` skill against
https://www.screener.in/company/NEWGEN/consolidated/

## Pipeline exercised
1. Freshness → `force_full` then `--mark-processed 2026-07-16`
2. Sector router → `it-services` (screener: IT - Software)
3. `build_facts.py --init-empty` + populated packs under `~/.company-research/newgen/facts/`
4. Source on disk: Q1 FY27 official press release text + screener structured numbers
5. `outlook_candidates.py` + `query_source.py` on the PR text
6. HTML via `html_helpers` (incl. `flow_diagram`) → WeasyPrint PDF

## Gaps intentionally left (honest)
- Full Q1 FY27 investor-presentation PDF / concall transcript not binary-ingested (IR page is link table; audio-only call noted on screener)
- Screener peers table JS-empty in fetch
- Attrition / utilization not disclosed in PR — stated as lens gap
- CRISIL rationale PDF listed but not extracted

## Verdict (short)
Steady product/software compounder with annuity/SaaS strength; tempered by FY26 growth slowdown and 164 debtor days. Confidence: moderate / watchlist.
