"""
Reusable HTML snippet builders for company-thesis-report.
Pairs with assets/report_style.css and scripts/charts.py.

Blessed assembly path: scripts/assemble_pdf.py (HTML → WeasyPrint PDF).
"""

from __future__ import annotations

import html as _html
from typing import Any


def esc(s: Any) -> str:
    return _html.escape("" if s is None else str(s))


def cover(title, ticker_line, situation_line, meta_line):
    return f'''
<div class="cover">
  <h1>{esc(title)}</h1>
  <div class="ticker">{esc(ticker_line)}</div>
  <div class="situation-line">{situation_line}</div>
  <div class="meta">{esc(meta_line)}</div>
</div>'''


def badge(text, kind='neutral'):
    # kind: bull | bear | watch | neutral | growth
    return f'<span class="badge badge-{kind}">{esc(text)}</span>'


def section(title):
    return f'<h2 class="section">{esc(title)}</h2>'


def subsection(title):
    return f'<h3 class="subsection">{esc(title)}</h3>'


def para(text, note=False):
    cls = ' class="note"' if note else ''
    return f'<p{cls}>{text}</p>'


def card_grid(cards):
    """cards: list of (label, value, tone) where tone is '' | 'good' | 'bad'"""
    items = ''.join(
        f'<div class="card"><div class="label">{esc(label)}</div>'
        f'<div class="value {tone}">{esc(value)}</div></div>'
        for label, value, tone in cards
    )
    return f'<div class="card-grid">{items}</div>'


def chart_block(img_path, caption=''):
    cap = f'<div class="chart-caption">{esc(caption)}</div>' if caption else ''
    return f'<div class="chart-wrap"><img src="{esc(img_path)}"/>{cap}</div>'


def chart_row(blocks):
    """blocks: list of chart_block() html strings, laid out side by side"""
    return f'<div class="chart-row">{"".join(blocks)}</div>'


def _cell_text(c: Any) -> str:
    """Reject dumping raw dicts/lists into table cells (causes PDF garbage)."""
    if isinstance(c, (dict, list, tuple, set)):
        raise TypeError(
            "table cells must be scalars/strings, not "
            f"{type(c).__name__}. Use kpi_table() or flatten values first."
        )
    return esc(c)


def data_table(headers, rows, total_row_index=None):
    """
    headers: list[str]; rows: list[list[str|number]]
    total_row_index: optional index of a row to bold as a total/summary row
    """
    thead = ''.join(f'<th>{esc(h)}</th>' for h in headers)
    trs = []
    for i, r in enumerate(rows):
        cls = ' class="total"' if total_row_index is not None and i == total_row_index else ''
        tds = ''.join(f'<td>{_cell_text(c)}</td>' for c in r)
        trs.append(f'<tr{cls}>{tds}</tr>')
    return f'<table class="data"><thead><tr>{thead}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


def kpi_table(scorecard: dict) -> str:
    """Render facts/kpi_scorecard.json as a proper period grid.

    Expected shape:
      {
        "period_columns": ["Jun25", "Sep25", "Dec25", "Mar26", "Jun26"],
        "rows": [
          {
            "metric": "Annuity (Cr)",
            "periods": {"Jun25": 220, "Jun26": 254},
            "trend": "up",
            "implication": "...",
            "gap_reason": ""   # if periods sparse
          }
        ],
        "gap": ""
      }

    Falls back to scorecard["columns"] + row["values"] if legacy shape, but
    still flattens dict values into period columns — never str(dict).
    """
    if not scorecard:
        raise ValueError("kpi_table: empty scorecard")

    rows_in = scorecard.get("rows") or []
    if not rows_in:
        gap = scorecard.get("gap") or "KPI scorecard empty"
        return para(esc(gap), note=True)

    period_cols = list(scorecard.get("period_columns") or [])
    if not period_cols:
        # Infer ordered union of period keys from rows
        seen = []
        for r in rows_in:
            periods = r.get("periods") or r.get("values") or {}
            if isinstance(periods, dict):
                for k in periods:
                    if k not in seen:
                        seen.append(k)
        period_cols = seen

    headers = ["KPI"] + period_cols + ["Trend", "Implication"]
    table_rows = []
    for r in rows_in:
        metric = r.get("metric") or ""
        periods = r.get("periods") if r.get("periods") is not None else r.get("values")
        if periods is None:
            periods = {}
        if not isinstance(periods, dict):
            raise TypeError(
                f"kpi_table: row '{metric}' periods/values must be a dict of "
                f"period→value, got {type(periods).__name__}"
            )
        cells = [metric]
        for p in period_cols:
            v = periods.get(p, "—")
            if isinstance(v, (dict, list, tuple, set)):
                raise TypeError(f"kpi_table: nested structure in {metric}/{p}")
            cells.append("—" if v is None or v == "" else v)
        cells.append(r.get("trend") or "")
        impl = r.get("implication") or ""
        gap_reason = r.get("gap_reason") or ""
        if gap_reason and not impl:
            impl = gap_reason
        elif gap_reason:
            impl = f"{impl} ({gap_reason})"
        cells.append(impl)
        table_rows.append(cells)

    html = data_table(headers, table_rows)
    gap = scorecard.get("gap")
    if gap:
        html += para(esc(gap), note=True)
    return html


def flag_list(items, kind='bear'):
    """items: list of strings (can include inline HTML like <b>). kind: 'bear' or 'bull'"""
    lis = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul class="flags {kind}">{lis}</ul>'


def bullet_list(items):
    """Plain bullet list for Sector Context / situation evidence."""
    lis = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul class="bullets">{lis}</ul>'


# Map outlook / milestone labels → CSS status kind
STATUS_KIND = {
    'delivered': 'done',
    'achieved': 'done',
    'done': 'done',
    'on track': 'on-track',
    'on-track': 'on-track',
    'pending': 'pending',
    'delayed': 'delayed',
    'missed': 'missed',
}


def _normalize_timeline_item(item: Any) -> tuple[str, str, str, str]:
    """Accept tuple/list or dict; return (date, title, status_text, status_kind)."""
    if isinstance(item, dict):
        date_str = item.get("date") or item.get("date_str") or ""
        title = item.get("title") or item.get("milestone") or item.get("headline") or ""
        status_text = (
            item.get("status_text")
            or item.get("detail")
            or item.get("amount")
            or item.get("status")
            or ""
        )
        status_kind = item.get("status_kind") or item.get("status") or ""
        return str(date_str), str(title), str(status_text), str(status_kind)

    if isinstance(item, (list, tuple)):
        if len(item) < 2:
            raise ValueError(f"timeline item too short: {item!r}")
        date_str = item[0]
        title = item[1]
        status_text = item[2] if len(item) > 2 else ""
        status_kind = item[3] if len(item) > 3 else status_text
        return str(date_str), str(title), str(status_text), str(status_kind)

    raise TypeError(
        f"timeline items must be dict or tuple, got {type(item).__name__}"
    )


def timeline(items):
    """items: list of tuples (date, title, status_text, status_kind) OR dicts
    with keys date/title/status|status_text/status_kind/detail.

    status_kind: done | on-track | pending | delayed | missed | ''
    (also accepts delivered/achieved/on track via STATUS_KIND)

    Raises ValueError if items is empty — omit the section instead of shipping
    an empty shell.
    """
    if not items:
        raise ValueError(
            "timeline: empty items — omit section 9 or pass a one-line gap via para()"
        )

    parts = []
    for raw in items:
        date_str, title, status_text, status_kind = _normalize_timeline_item(raw)
        if not str(title).strip():
            raise ValueError(f"timeline: item missing title: {raw!r}")
        kind = STATUS_KIND.get(str(status_kind).lower().strip(), status_kind or '')
        # If status_kind was a long detail string, don't use it as CSS class
        if kind and len(str(kind)) > 24:
            kind = STATUS_KIND.get(str(status_text).lower().strip(), '')
            display_status = status_text
        else:
            display_status = status_text
        parts.append(f'''
<div class="timeline-item">
  <div class="timeline-date">{esc(date_str)}</div>
  <div class="timeline-body">
    <div class="title">{esc(title)}</div>
    <div class="status {esc(kind)}">{esc(display_status)}</div>
  </div>
</div>''')
    return f'<div class="timeline">{"".join(parts)}</div>'


def flow_diagram(stages, caption=''):
    """Visual value-chain / sector-flow diagram — NEVER use ASCII/code blocks.

    stages: list of (label, detail) or dicts with keys label/detail
    Renders a vertical stack of styled boxes with arrow connectors.
    """
    boxes = []
    for i, stage in enumerate(stages):
        if isinstance(stage, dict):
            label, detail = stage.get('label', ''), stage.get('detail', '')
        else:
            label, detail = stage[0], stage[1] if len(stage) > 1 else ''
        boxes.append(
            f'<div class="flow-stage">'
            f'<div class="flow-label">{esc(label)}</div>'
            f'<div class="flow-detail">{esc(detail)}</div>'
            f'</div>'
        )
        if i < len(stages) - 1:
            boxes.append('<div class="flow-arrow" aria-hidden="true">↓</div>')
    cap = f'<div class="flow-caption">{esc(caption)}</div>' if caption else ''
    return f'<div class="flow-diagram">{"".join(boxes)}{cap}</div>'


def verdict_box(text):
    return f'<div class="verdict-box">{text}</div>'


def sources_list(sources):
    """sources: list of (title, url, note) — note is a short description, may be empty"""
    parts = []
    for i, (title, url, note) in enumerate(sources, 1):
        note_html = f' — {esc(note)}' if note else ''
        parts.append(
            f'<div class="source-item"><span class="title">{i}. {esc(title)}</span>{note_html}<br>'
            f'<a href="{esc(url)}">{esc(url)}</a></div>'
        )
    return ''.join(parts)


def page_break():
    return '<div class="page-break"></div>'


def render(body_html, css_path):
    """Wrap assembled body HTML in a full document with the stylesheet inlined."""
    css = open(css_path).read()
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body_html}</body></html>'


def smoke_check_html(html: str) -> list[str]:
    """Return list of production-failure markers found in assembled HTML."""
    failures = []
    markers = [
        ("date title\nstatus", "empty timeline shell"),
        ("date title status", "empty timeline shell"),
        # classic bug: for date,title,status,kind in [dict] unpacks dict KEYS
        ('timeline-date">date</div>', "timeline unpacked dict keys as content"),
        ('class="title">title</div>', "timeline unpacked dict keys as content"),
        ("{&#x27;", "escaped Python dict in cells"),
        ("{&#39;", "escaped Python dict in cells"),
        ("{'", "raw Python dict string in HTML"),
    ]
    for needle, label in markers:
        if needle in html:
            failures.append(label)
    # de-dupe preserving order
    seen = set()
    out = []
    for f in failures:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out
