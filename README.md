# company-research-skill

A [Claude Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that turns Claude into an equity-research analyst: point it at a listed company and it produces a **decision-grade** sourced PDF — clear **BUY / HOLD / AVOID**, confirm/kill criteria, dense analysis (not headings-only), a fixed spine, facts-pack ingest, and **one matched sector lens**.

**Quality beats token savings** when they conflict. Facts packs avoid dumping whole ARs into context; they are not an excuse to ship a thin report.

## What it produces

A single PDF (plus markdown source) that opens with an **investment decision**, then:

- Confirm / kill criteria, key debate, alternative thesis, position framing
- Company Summary + Sector Context + visual value chain
- Situation Classification + multi-quarter outlook (verbatim from concall/deck)
- Customers, milestones, Sector Deep-Dive (lens-defined)
- Financials with **8-quarter bridge**, **working-capital / CFO vs PAT**, KPI scorecard
- Mix deep-dive, demand indicators, capital allocation
- Valuation with **what is priced in** + bull/base/bear scenarios
- Real peer comps (ops + multiples), moats, technicals
- Management scorecard, falsifiable thesis, mandatory risks, final verdict, sources

Discipline: **a claim without a source and a date is not evidence.** A headings-only or thin PDF is a failed run — see `references/depth-checklist.md`.

## Ingest design (efficient, not thin)

Raw concalls / decks / annual reports are extracted to disk under `~/.company-research/<slug>/sources/`. The agent drafts from JSON **facts packs** in `facts/` — but packs must be rich enough for a **decision-grade** PDF (concall mined, peers filled, confirm/kill written). Built with:

| Script | Role |
|--------|------|
| `scripts/freshness.py` | `no_state` / `up_to_date` / `new_quarter` / `force_full` |
| `scripts/pdf_to_text.py` | Full-doc PDF → txt |
| `scripts/query_source.py` | Grep / BM25 snippets only |
| `scripts/outlook_candidates.py` | Forward-looking quote candidates |
| `scripts/build_facts.py` | Init/merge packs + apply sector lens schema |
| `scripts/forward_pe.py` / `capacity_utilization.py` | Deterministic maths when needed |

## Sector lenses (~26)

The report spine never names an industry. After classifying the company (`references/sector-router.md`), the skill loads **one** folder:

```
skills/company-thesis-report/sectors/<lens-id>/
  LENS.md                 # primer, metrics, valuation, deep-dive template
  metrics.schema.json     # overlay shape + query keys
```

Examples of lens ids: `banks`, `nbfc-hfc`, `aerospace-defence`, `capital-goods-epc`, `it-services`, `specialty-chemicals`, `fmcg-staples`, `generic`, …

To add a sector: create a new folder + router row — **no spine changes**.

## Repository layout

```
company-research-skill/
└── skills/
    └── company-thesis-report/
        ├── SKILL.md
        ├── references/
        │   ├── report-format.md
        │   ├── depth-checklist.md
        │   ├── sector-router.md
        │   ├── source-routing.md
        │   └── facts-schemas.md
        ├── sectors/                 # one lens per coverage bucket
        ├── scripts/
        │   ├── html_helpers.py      # includes flow_diagram()
        │   ├── charts.py
        │   ├── pdf_to_text.py
        │   ├── query_source.py
        │   ├── outlook_candidates.py
        │   ├── build_facts.py
        │   ├── freshness.py
        │   ├── forward_pe.py
        │   └── capacity_utilization.py
        └── assets/
            └── report_style.css
```

## Requirements

- Claude with Agent Skills + code execution / file access
- Python 3 with:

  ```bash
  pip install matplotlib weasyprint pypdf rank_bm25 --break-system-packages
  ```

## Installation

### Claude Code / Agent SDK

```bash
git clone git@github.com:iamurali/company-research-skill.git
mkdir -p ~/.claude/skills
cp -r company-research-skill/skills/company-thesis-report ~/.claude/skills/
```

Project-scoped:

```bash
mkdir -p .claude/skills
cp -r company-research-skill/skills/company-thesis-report .claude/skills/
```

### Claude / Cowork desktop

```bash
cd company-research-skill/skills
zip -r company-thesis-report.skill company-thesis-report
```

Upload under Settings → Capabilities → Skills.

## Usage

- "What's the story with `<TICKER>`?"
- "Build me an investment thesis on `<Company>`."
- "Research `<Company>` — is it a buy?"

Claude will:

1. Check freshness for `~/.company-research/<slug>/`
2. Classify sector → load one lens
3. Ingest sources to disk; build facts packs (no full-doc context dumps)
4. Draft the fixed spine; render visual PDF with `flow_diagram()` value chains
5. Deliver PDF + short spoken summary

### First run vs refresh

| Request | Behavior |
|---------|----------|
| New company | Full ingest + all packs |
| Same quarter again | `up_to_date` — reuse; optional price refresh |
| New results/concall | `new_quarter` — delta packs only |
| "from scratch" / "rebuild" | `force_full` |

## Customizing

- **Section spine** — `references/report-format.md` (keep sector-agnostic)
- **Sector routing / new lens** — `references/sector-router.md` + `sectors/<id>/`
- **Visual style** — `assets/report_style.css`
- **HTML components** — `scripts/html_helpers.py` (`flow_diagram`, timeline, cards, tables)

## License

MIT — see [LICENSE](LICENSE).
