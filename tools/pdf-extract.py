#!/usr/bin/env python3
"""
PDF → 纯文本提取（项目内统一入口）。

raw/ 中的 .pdf 文件按 schema/gotchas.md 规范应通过本工具提取文本以辅助编译，
不修改原始 PDF（Raw 不可变原则）。提取结果写到临时文件或 stdout，不入仓。

与 pdftotext 的区别: 不依赖 poppler-utils，跨平台一致；底层为 PyMuPDF (mupdf C 库)。
不是格式转换器——Markdown / JSON 是后续 ljg 编译路径的责任。

用法:
  uv run python tools/pdf-extract.py raw/<file>.pdf
  uv run python tools/pdf-extract.py raw/<file>.pdf --out /tmp/paper.md
  uv run python tools/pdf-extract.py raw/<file>.pdf --pages 1-20
  uv run python tools/pdf-extract.py raw/<file>.pdf --strict
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pymupdf as fitz

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_PDF_ERROR = 3

DEFAULT_SEPARATOR = "\n\n---\n\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract plain text from a PDF (project-level standard entry).",
    )
    parser.add_argument("pdf", type=Path, help="Input PDF path")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--pages",
        type=str,
        default=None,
        help="1-indexed inclusive page range, e.g. '1-20' or '5'. Default: all pages.",
    )
    parser.add_argument(
        "--separator",
        type=str,
        default=DEFAULT_SEPARATOR,
        help="Text inserted between pages (default: blank-line + --- + blank-line)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 2 if extracted text is empty (catches image-only PDFs).",
    )
    return parser.parse_args(argv)


def parse_pages(spec: str, total: int) -> range:
    """Parse 'N-M' or 'N' (1-indexed inclusive) → 0-indexed range for doc[i]."""
    spec = spec.strip()
    if "-" in spec:
        start_s, end_s = spec.split("-", 1)
        start, end = int(start_s), int(end_s)
    else:
        start = end = int(spec)
    if start < 1 or end < start:
        raise ValueError(f"invalid page spec: {spec!r}")
    if end > total:
        raise ValueError(f"page range {spec!r} exceeds document length {total}")
    return range(start - 1, end)


def main(argv: list[str] | None = None) -> int:
    # Force UTF-8 stdout so Chinese / Unicode never breaks on Windows or CI.
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass

    args = parse_args(argv)

    # Pre-flight checks: extension + existence (cheaper than opening the PDF).
    if args.pdf.suffix.lower() != ".pdf":
        print(
            f"error: input must be a .pdf file, got {args.pdf.suffix!r}",
            file=sys.stderr,
        )
        return EXIT_INPUT_ERROR
    if not args.pdf.exists():
        print(f"error: file not found: {args.pdf}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    try:
        doc = fitz.open(args.pdf)
    except fitz.PasswordError:
        print(
            f"error: PDF is password-protected, decryption not supported: {args.pdf}",
            file=sys.stderr,
        )
        return EXIT_PDF_ERROR
    except RuntimeError as exc:
        print(f"error: failed to open PDF {args.pdf}: {exc}", file=sys.stderr)
        return EXIT_PDF_ERROR

    # PyMuPDF's open() succeeds on some encrypted PDFs and only raises on
    # page access. Detect early and bail out cleanly.
    if doc.is_encrypted or doc.needs_pass:
        doc.close()
        print(
            f"error: PDF is password-protected, decryption not supported: {args.pdf}",
            file=sys.stderr,
        )
        return EXIT_PDF_ERROR

    try:
        total = doc.page_count
        if args.pages is not None:
            try:
                pages = parse_pages(args.pages, total)
            except ValueError as exc:
                print(f"error: {exc}", file=sys.stderr)
                return EXIT_INPUT_ERROR
        else:
            pages = range(total)

        parts = [doc[i].get_text() for i in pages]
    finally:
        doc.close()

    text = args.separator.join(parts)

    if args.strict and not text.strip():
        print(
            f"warning: extracted text is empty (likely image-only PDF): {args.pdf}",
            file=sys.stderr,
        )
        return EXIT_INPUT_ERROR

    if args.out is None:
        sys.stdout.write(text)
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")

    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())