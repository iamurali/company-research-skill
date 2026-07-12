"""
Reusable HTML snippet builders for company-thesis-report.
Pairs with assets/report_style.css (link/inline it in the page <head>) and
scripts/charts.py (embed the PNGs these charts produce via chart_block()).

These return HTML strings — assemble a per-company report by concatenating
them inside a page template, then render with WeasyPrint:

    import sys; sys.path.insert(0, '<skill_dir>/scripts')
    from html_helpers import *
    html = f'''<!DOCTYPE html><html><head><meta charset="utf-8">
    <style>{open('<skill_dir>/assets/report_style.css').read()}</style>
    </head><body>{cover(...)}{section("2. Business overview", ...)}...</body></html>'''
    open('report.html','w').write(html)
    # then: python3 -m weasyprint report.html report.pdf
"""

import html as _html


def esc(s):
    return _html.escape(str(s))


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


def data_table(headers, rows, total_row_index=None):
    """
    headers: list[str]; rows: list[list[str]]
    total_row_index: optional index of a row to bold as a total/summary row
    """
    thead = ''.join(f'<th>{esc(h)}</th>' for h in headers)
    trs = []
    for i, r in enumerate(rows):
        cls = ' class="total"' if total_row_index is not None and i == total_row_index else ''
        tds = ''.join(f'<td>{esc(c)}</td>' for c in r)
        trs.append(f'<tr{cls}>{tds}</tr>')
    return f'<table class="data"><thead><tr>{thead}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


def flag_list(items, kind='bear'):
    """items: list of strings (can include inline HTML like <b>). kind: 'bear' or 'bull'"""
    lis = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul class="flags {kind}">{lis}</ul>'


def timeline(items):
    """items: list of (date_str, title, status_text, status_kind) where status_kind is 'done'|'pending'|''"""
    parts = []
    for date_str, title, status_text, status_kind in items:
        parts.append(f'''
<div class="timeline-item">
  <div class="timeline-date">{esc(date_str)}</div>
  <div class="timeline-body">
    <div class="title">{esc(title)}</div>
    <div class="status {status_kind}">{esc(status_text)}</div>
  </div>
</div>''')
    return f'<div class="timeline">{"".join(parts)}</div>'


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
