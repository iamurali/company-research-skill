#!/usr/bin/env python3
"""Assemble report HTML → PDF (blessed path).

Usage:
  python3 assemble_pdf.py \\
    --html ~/.company-research/<slug>/output/report.html \\
    --out  ~/.company-research/<slug>/output/<Name>_report.pdf

  # or wrap a body fragment with the skill stylesheet:
  python3 assemble_pdf.py \\
    --body-html /tmp/body.html \\
    --out report.pdf

Runs smoke_check_html before WeasyPrint. Exit 1 on broken markers unless
--allow-broken (debug only).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from html_helpers import render, smoke_check_html  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", type=Path, help="Full HTML document path")
    ap.add_argument("--body-html", type=Path, help="Body fragment; wrapped with CSS")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--title", default="", help="Unused; reserved for metadata")
    ap.add_argument(
        "--allow-broken",
        action="store_true",
        help="Do not fail on smoke_check markers (debug only)",
    )
    ap.add_argument("--skip-pdf", action="store_true", help="Write HTML only")
    args = ap.parse_args()

    css = SKILL_ROOT / "assets" / "report_style.css"
    if args.html and args.body_html:
        raise SystemExit("pass only one of --html or --body-html")
    if not args.html and not args.body_html:
        raise SystemExit("need --html or --body-html")

    if args.html:
        html = args.html.read_text(encoding="utf-8")
    else:
        body = args.body_html.read_text(encoding="utf-8")
        html = render(body, str(css))

    problems = smoke_check_html(html)
    if problems:
        msg = "smoke_check_html failures: " + "; ".join(problems)
        if args.allow_broken:
            print("WARNING:", msg, file=sys.stderr)
        else:
            raise SystemExit(msg)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    html_out = args.out.with_suffix(".html")
    if args.out.suffix.lower() == ".pdf":
        html_out.write_text(html, encoding="utf-8")
    else:
        args.out.write_text(html, encoding="utf-8")
        html_out = args.out

    if args.skip_pdf or args.out.suffix.lower() != ".pdf":
        print(json_dumps({"html": str(html_out), "smoke": "pass"}))
        return

    try:
        from weasyprint import HTML
    except ImportError as e:
        raise SystemExit(
            "weasyprint not installed. pip install weasyprint"
        ) from e

    HTML(filename=str(html_out), base_url=str(html_out.parent)).write_pdf(args.out)
    print(json_dumps({
        "html": str(html_out),
        "pdf": str(args.out),
        "bytes": args.out.stat().st_size,
        "smoke": "pass",
    }))


def json_dumps(obj: dict) -> str:
    import json
    return json.dumps(obj, indent=2)


if __name__ == "__main__":
    main()
