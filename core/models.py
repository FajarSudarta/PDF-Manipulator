"""Struktur data yang dipakai bersama oleh UI dan core.

Menggantikan dict ber-key "ajaib" (Configuration_Info, Final_Conf, __Doc_Info)
dan list berindeks (Info[1], i[2], ...) di versi lama.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # hanya untuk type hint, core/models tidak butuh pymupdf saat runtime
    import pymupdf


class PageMode(IntEnum):
    """Mode pemilihan halaman. Nilainya sama dengan index combobox di UI."""

    ALL = 0
    FROM_START = 1
    SPECIFIC = 2
    INTERVAL = 3
    FROM_END = 4  # masih "Coming Soon" di UI


@dataclass(frozen=True)
class DocInfo:
    """Info dokumen yang ditampilkan di panel info. Immutable: aman dikirim lewat signal."""

    file_name: str
    location: str
    page_count: int
    file_size: str
    ext: str
    metadata: dict = field(default_factory=dict)


@dataclass(frozen=True)
class TextWatermark:
    text: str
    font: str
    fontsize: int
    rotation: int
    color: tuple[float, float, float]
    # Dulu "timpa": kalau True, watermark universal tetap ditumpuk di atas watermark order ini.
    overlay_universal: bool = False


@dataclass(frozen=True)
class OrderConfig:
    """Konfigurasi satu ObjectOrder (dulu Configuration_Info + isi panel utama)."""

    mode: PageMode = PageMode.ALL
    page_spec: str = ""
    rotate: int | None = None
    repeat: int = 1
    watermark: TextWatermark | None = None


@dataclass(frozen=True)
class Encryption:
    # repr=False supaya password tidak ikut tercetak kalau objeknya di-log/print.
    owner_pw: str = field(repr=False)
    user_pw: str = field(repr=False)
    permissions: int
    algorithm_index: int


@dataclass(frozen=True)
class FinalizeConfig:
    """Hasil dialog finalisasi (dulu self.Final_Conf)."""

    final_path: str
    metadata: dict | None  # None = kosongkan metadata
    encryption: Encryption | None
    watermark: TextWatermark | None
    open_after_save: bool


@dataclass(frozen=True)
class OrderPlan:
    """Satu order yang sudah divalidasi dan siap dieksekusi oleh core.merge.build_document."""

    name: str
    src: "pymupdf.Document"
    ranges: list[tuple[int, int]]  # 0-based inklusif; from > to berarti urutan terbalik
    repeat: int = 1
    rotate: int | None = None
    watermark: TextWatermark | None = None

    @property
    def page_total(self) -> int:
        return sum(abs(b - a) + 1 for a, b in self.ranges) * self.repeat

    def watermarks(self, universal: TextWatermark | None) -> list[TextWatermark]:
        """Watermark yang diterapkan ke halaman order ini, sesuai urutan.

        Aturan "timpa" dulu di-copy-paste 4x di Merge_Event, sekarang cukup di sini.
        """
        if self.watermark is None:
            return [universal] if universal is not None else []
        if universal is not None and self.watermark.overlay_universal:
            return [self.watermark, universal]
        return [self.watermark]
