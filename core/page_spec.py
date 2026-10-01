"""Satu-satunya tempat yang mengubah (mode, teks input) menjadi daftar halaman.

Dulu logika ini ada di tiga tempat (SpecifyWindow.Evaluate_Parsing_Page,
PreviewPageSequence.__Evaluate_Parsing, Merge_Event) dengan aturan yang mulai berbeda.
Semua fungsi di sini murni (tanpa Qt, tanpa pymupdf), jadi gampang di-test.
"""
from __future__ import annotations

import re

from .models import PageMode


class PageSpecError(ValueError):
    """Input halaman tidak valid. str(error) aman ditampilkan langsung ke user."""


EDITABLE_MODES = frozenset({PageMode.FROM_START, PageMode.SPECIFIC, PageMode.INTERVAL})

MODE_HELP: dict[PageMode, tuple[str, str]] = {
    PageMode.ALL: ("All Pages", "Semua halaman pada dokumen akan dimasukkan ke urutan ini."),
    PageMode.FROM_START: ("Jumlah Halaman", "Jumlah halaman yang dimuat mulai dari halaman 1.\nContoh: 5"),
    PageMode.SPECIFIC: ("Spesifik Pages", "Halaman spesifik yang mau dimuat, dipisah koma.\nContoh: 1,3,5"),
    PageMode.INTERVAL: (
        "Interval Pages",
        "Rentang halaman yang mau dimuat, bisa multi interval.\n"
        "Format: (Awal1,Akhir1),(Awal2,Akhir2),dst\n"
        "Awal boleh lebih besar dari Akhir untuk urutan terbalik, contoh: (7,3)",
    ),
    PageMode.FROM_END: ("Coming Soon", "Mode ini belum didukung."),
}

# [0-9] dan bukan \d: \d juga cocok dengan digit Unicode non-ASCII.
_COUNT_RE = re.compile(r"[0-9]+")
_SPECIFIC_RE = re.compile(r"[0-9]+(?:,[0-9]+)*")
_ONE_INTERVAL_RE = re.compile(r"\(([0-9]+),([0-9]+)\)")
_INTERVALS_RE = re.compile(r"\([0-9]+,[0-9]+\)(?:,?\([0-9]+,[0-9]+\))*")


def _clean(text: str) -> str:
    return "".join(text.split())


def _check_page(page: int, page_count: int) -> None:
    if not 1 <= page <= page_count:
        raise PageSpecError(f"Halaman {page} tidak ada; dokumen hanya punya {page_count} halaman.")


def parse_count(text: str, page_count: int) -> int:
    s = _clean(text)
    if not _COUNT_RE.fullmatch(s):
        raise PageSpecError("Jumlah halaman harus berupa angka bulat positif.")
    n = int(s)
    if not 1 <= n <= page_count:
        raise PageSpecError(f"Jumlah halaman harus antara 1 dan {page_count}.")
    return n


def parse_specific_pages(text: str, page_count: int) -> list[int]:
    """'1, 3,5' -> [1, 3, 5] (1-based, urutan dan duplikat dipertahankan)."""
    s = _clean(text)
    if not _SPECIFIC_RE.fullmatch(s):
        raise PageSpecError("Format halaman spesifik: angka dipisah koma, contoh: 1,3,5")
    pages = [int(x) for x in s.split(",")]
    for p in pages:
        _check_page(p, page_count)
    return pages


def parse_intervals(text: str, page_count: int) -> list[tuple[int, int]]:
    """'(1,3),(7,5)' -> [(1, 3), (7, 5)] (1-based, arah dipertahankan)."""
    s = _clean(text)
    if not _INTERVALS_RE.fullmatch(s):
        raise PageSpecError("Format interval: (awal,akhir), contoh: (1,3),(7,5)")
    result = [(int(a), int(b)) for a, b in _ONE_INTERVAL_RE.findall(s)]
    for a, b in result:
        _check_page(a, page_count)
        _check_page(b, page_count)
    return result


def resolve_ranges(mode: PageMode | int, text: str, page_count: int) -> list[tuple[int, int]]:
    """Ubah input user menjadi range halaman 0-based inklusif.

    Range (a, b) dengan a > b berarti halaman disalin terbalik, sesuai perilaku
    pymupdf.Document.insert_pdf(from_page=a, to_page=b).
    """
    if page_count <= 0:
        raise PageSpecError("Dokumen tidak memiliki halaman.")
    try:
        mode = PageMode(mode)
    except ValueError:
        raise PageSpecError("Mode halaman tidak dikenal.") from None

    if mode == PageMode.ALL:
        return [(0, page_count - 1)]
    if mode not in EDITABLE_MODES:
        raise PageSpecError("Mode ini belum didukung.")
    if not _clean(text):
        raise PageSpecError("Tidak ada input halaman.")

    if mode == PageMode.FROM_START:
        n = parse_count(text, page_count)
        return [(0, n - 1)]
    if mode == PageMode.SPECIFIC:
        return [(p - 1, p - 1) for p in parse_specific_pages(text, page_count)]
    return [(a - 1, b - 1) for a, b in parse_intervals(text, page_count)]


def expand_ranges(ranges: list[tuple[int, int]]) -> list[int]:
    """[(0, 2), (5, 4)] -> [0, 1, 2, 5, 4]. Dipakai preview untuk navigasi."""
    pages: list[int] = []
    for a, b in ranges:
        step = 1 if b >= a else -1
        pages.extend(range(a, b + step, step))
    return pages
