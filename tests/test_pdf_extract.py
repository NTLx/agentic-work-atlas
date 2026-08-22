"""Tests for tools/pdf-extract.py.

PDFs are generated on the fly via pymupdf to avoid committing binary fixtures.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]


def load_pdf_extract():
    spec = importlib.util.spec_from_file_location(
        "pdf_extract", ROOT / "tools" / "pdf-extract.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_pdf(tmp_path: Path, pages: list[str]) -> Path:
    """Generate a minimal PDF with the given page bodies."""
    path = tmp_path / "fixture.pdf"
    doc = fitz.open()
    for body in pages:
        page = doc.new_page()
        page.insert_text((72, 72), body)
    doc.save(path)
    doc.close()
    return path


def run_cli(*args: str) -> subprocess.CompletedProcess:
    """Invoke the script via uv run for end-to-end CLI coverage."""
    return subprocess.run(
        ["uv", "run", "python", "tools/pdf-extract.py", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


# ---- in-process (function-level) tests ----


def test_parse_pages_single():
    pe = load_pdf_extract()
    assert pe.parse_pages("5", total=10) == range(4, 5)


def test_parse_pages_range():
    pe = load_pdf_extract()
    assert pe.parse_pages("1-3", total=10) == range(0, 3)


def test_parse_pages_invalid_specs(tmp_path):
    pe = load_pdf_extract()
    for bad in ["0-1", "5-3", "0", "abc-5", "-1"]:
        try:
            pe.parse_pages(bad, total=10)
        except ValueError:
            continue
        else:
            raise AssertionError(f"expected ValueError for {bad!r}")


def test_parse_pages_exceeds_total():
    pe = load_pdf_extract()
    try:
        pe.parse_pages("99-100", total=10)
    except ValueError as exc:
        assert "exceeds" in str(exc)
    else:
        raise AssertionError("expected ValueError")


# ---- CLI end-to-end tests ----


def test_cli_happy_path_default_stdout(tmp_path):
    pdf = make_pdf(tmp_path, ["Page One body.", "Page Two body.", "Page Three body."])
    result = run_cli(str(pdf))
    assert result.returncode == 0, result.stderr
    body = result.stdout
    assert "Page One body." in body
    assert "Page Two body." in body
    assert "Page Three body." in body
    # Default separator is the gotchas.md convention.
    assert "\n\n---\n\n" in body
    # 3 pages → 2 separators.
    assert body.count("\n\n---\n\n") == 2


def test_cli_pages_range(tmp_path):
    pdf = make_pdf(tmp_path, [f"Page {i}" for i in range(1, 6)])
    result = run_cli(str(pdf), "--pages", "2-4")
    assert result.returncode == 0, result.stderr
    body = result.stdout
    assert "Page 2" in body
    assert "Page 3" in body
    assert "Page 4" in body
    assert "Page 1" not in body
    assert "Page 5" not in body


def test_cli_out_file_with_unicode_path(tmp_path):
    """--out to a non-ASCII path round-trips; fixture text is ASCII because
    PyMuPDF's default helv font has no CJK glyphs (real CJK PDFs still work,
    but fixture generation needs an explicit CJK font)."""
    pdf = make_pdf(tmp_path, ["ASCII body content."])
    out = tmp_path / "输出" / "result.md"
    result = run_cli(str(pdf), "--out", str(out))
    assert result.returncode == 0, result.stderr
    assert out.exists()
    assert "ASCII body content." in out.read_text(encoding="utf-8")


def test_cli_nonexistent_file(tmp_path):
    result = run_cli(str(tmp_path / "nope.pdf"))
    assert result.returncode == 2
    assert "file not found" in result.stderr


def test_cli_non_pdf_extension(tmp_path):
    fake = tmp_path / "note.txt"
    fake.write_text("not a pdf", encoding="utf-8")
    result = run_cli(str(fake))
    assert result.returncode == 2
    assert ".pdf" in result.stderr


def test_cli_pages_out_of_range(tmp_path):
    pdf = make_pdf(tmp_path, ["only one"])
    result = run_cli(str(pdf), "--pages", "99-100")
    assert result.returncode == 2
    assert "exceeds" in result.stderr


def test_cli_encrypted_pdf(tmp_path):
    """Generate a real encrypted PDF and confirm exit code 3."""
    path = tmp_path / "encrypted.pdf"
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "secret body")
    doc.save(path, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw="owner", user_pw="user")
    doc.close()

    result = run_cli(str(path))
    assert result.returncode == 3
    assert "password" in result.stderr.lower() or "decrypt" in result.stderr.lower()


def test_cli_strict_on_text_pdf_passes(tmp_path):
    pdf = make_pdf(tmp_path, ["actual text content"])
    result = run_cli(str(pdf), "--strict")
    assert result.returncode == 0