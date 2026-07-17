#!/usr/bin/env python3
"""Extract full PDF text to a UTF-8 .txt file (disk only — do not load into model context).

Usage:
  python3 pdf_to_text.py input.pdf output.txt [--expect-name "Company"] [--pages START-END]

--pages is for scouting only (e.g. first 5 pages). Default extracts the whole document.
--expect-name scouts the first 2 pages and aborts if the name is missing (wrong-PDF guard).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _extract_pypdf(path: Path, start: int | None, end: int | None) -> tuple[str, int]:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    n = len(reader.pages)
    s = 0 if start is None else max(0, start - 1)
    e = n if end is None else min(n, end)
    parts = []
    for i in range(s, e):
        try:
            text = reader.pages[i].extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            text = f"\n[extract error page {i+1}: {exc}]\n"
        parts.append(f"\n\n----- PAGE {i+1} -----\n{text}")
    return "".join(parts), n


def _extract_pdfminer(path: Path, start: int | None, end: int | None) -> tuple[str, int]:
    from pdfminer.high_level import extract_text

    # pdfminer page numbers are 0-based in page_numbers=
    kwargs = {}
    if start is not None or end is not None:
        # Without page count, extract all then slice markers — prefer pypdf for ranges.
        text = extract_text(str(path))
        return text, text.count("\f") + 1 if text else 0
    text = extract_text(str(path))
    return text, text.count("\f") + 1 if text else 0


def extract(path: Path, start: int | None = None, end: int | None = None) -> tuple[str, int]:
    try:
        return _extract_pypdf(path, start, end)
    except ImportError:
        pass
    try:
        return _extract_pdfminer(path, start, end)
    except ImportError as exc:
        raise SystemExit(
            "Need pypdf or pdfminer.six: pip install pypdf --break-system-packages"
        ) from exc


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_pdf", type=Path)
    ap.add_argument("output_txt", type=Path)
    ap.add_argument("--expect-name", default=None, help="Abort if name missing on first pages")
    ap.add_argument("--pages", default=None, help="Optional START-END (1-based, inclusive)")
    args = ap.parse_args()

    if not args.input_pdf.exists():
        raise SystemExit(f"missing pdf: {args.input_pdf}")

    start = end = None
    if args.pages:
        m = re.fullmatch(r"(\d+)-(\d+)", args.pages.strip())
        if not m:
            raise SystemExit("--pages must look like 1-5")
        start, end = int(m.group(1)), int(m.group(2))

    if args.expect_name:
        scout, _ = extract(args.input_pdf, 1, 2)
        if args.expect_name.lower() not in scout.lower():
            raise SystemExit(
                f"--expect-name '{args.expect_name}' not found in first 2 pages; "
                "refusing full extract (possible wrong-company PDF)"
            )

    text, n_pages = extract(args.input_pdf, start, end)
    args.output_txt.parent.mkdir(parents=True, exist_ok=True)
    args.output_txt.write_text(text, encoding="utf-8")
    print(f"wrote {args.output_txt} ({len(text)} chars, pdf_pages={n_pages})")


if __name__ == "__main__":
    main()
