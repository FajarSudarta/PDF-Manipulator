from __future__ import annotations

import os
from pathlib import Path

import pymupdf

from .models import DocInfo
from .utils import format_size


class LoadError(Exception):
    """File tidak bisa dimuat. str(error) aman ditampilkan ke user."""


def load_document(path: str, data_path: str | None = None) -> tuple[pymupdf.Document, DocInfo]:
    """Buka file sebagai dokumen PDF dan kembalikan (dokumen, info).

    Gambar (PNG/JPG/...) langsung dikonversi ke PDF 1 halaman di sini, sehingga
    sisa program tidak perlu cabang khusus gambar: rotasi, repetisi, watermark,
    dan preview otomatis berlaku sama untuk semua format.

    `data_path` dipakai kalau isi yang dibuka berbeda dengan file yang ditampilkan
    (misalnya format .dimas). Pemanggil memiliki dokumen yang dikembalikan dan
    wajib menutupnya.
    """
    data_path = data_path or path
    try:
        doc = pymupdf.open(data_path)
    except Exception as e:
        raise LoadError(f"Tidak bisa membuka file:\n{e}") from e

    try:
        metadata = dict(doc.metadata or {})
        if not doc.is_pdf:
            pdf = pymupdf.open("pdf", doc.convert_to_pdf())
            doc.close()
            doc = pdf
        if doc.page_count <= 0:
            raise LoadError("Dokumen tidak memiliki halaman.")
    except LoadError:
        doc.close()
        raise
    except Exception as e:
        doc.close()
        raise LoadError(f"File terbuka tapi gagal diproses:\n{e}") from e

    p = Path(path)
    info = DocInfo(
        file_name=p.name,
        location=os.path.normpath(path),
        page_count=doc.page_count,
        file_size=format_size(p.stat().st_size),
        ext=p.suffix.lower(),
        metadata=metadata,
    )
    return doc, info
