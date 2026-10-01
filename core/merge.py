"""Inti proses merge, dipisah dari UI.

build_document() menggantikan ~100 baris empat cabang hampir identik di
Merge_Event versi lama. Karena tidak menyentuh widget sama sekali, fungsi ini
nantinya bisa langsung dipindah ke QThread/worker.
"""
from __future__ import annotations

import pymupdf

from .models import FinalizeConfig, OrderConfig, OrderPlan, TextWatermark
from .page_spec import resolve_ranges

# Urutan harus sama dengan item Algorithm_Encryption_ComboBox di Finalize_Window.
ENCRYPTION_METHODS = (
    pymupdf.PDF_ENCRYPT_RC4_40,
    pymupdf.PDF_ENCRYPT_RC4_128,
    pymupdf.PDF_ENCRYPT_AES_128,
    pymupdf.PDF_ENCRYPT_AES_256,
)


def plan_order(name: str, src: pymupdf.Document, config: OrderConfig) -> OrderPlan:
    """Validasi satu order. Melempar PageSpecError kalau input halamannya salah."""
    ranges = resolve_ranges(config.mode, config.page_spec, src.page_count)
    return OrderPlan(
        name=name,
        src=src,
        ranges=ranges,
        repeat=max(1, config.repeat),
        rotate=config.rotate,
        watermark=config.watermark,
    )


def add_text_watermark(doc: pymupdf.Document, pages: range, wm: TextWatermark) -> None:
    font = pymupdf.Font(wm.font)  # dibuat sekali, dipakai ulang untuk semua halaman
    for i in pages:
        page = doc[i]
        writer = pymupdf.TextWriter(page.rect)
        writer.append(
            pos=(page.rect.width / 2, page.rect.height / 2),
            text=wm.text,
            fontsize=wm.fontsize,
            font=font,
        )
        #Ada Masalah saaat Menambahkan Watermark Text
        page.write_text(
            rect=page.rect,
            writers=writer,
            rotate=wm.rotation,
            opacity=0.5,
            color=wm.color,
            overlay=True,
        )


def build_document(plans: list[OrderPlan], universal_wm: TextWatermark | None = None) -> pymupdf.Document:
    """Susun dokumen hasil. Pemanggil memiliki dokumen yang dikembalikan (pakai `with`)."""
    out = pymupdf.open()
    try:
        for plan in plans:
            rotate = -1 if plan.rotate is None else plan.rotate  # -1 = rotasi asli dipertahankan
            for _ in range(plan.repeat):
                start = out.page_count
                for a, b in plan.ranges:
                    out.insert_pdf(plan.src, from_page=a, to_page=b, rotate=rotate)
                for wm in plan.watermarks(universal_wm):
                    add_text_watermark(out, range(start, out.page_count), wm)
    except Exception:
        out.close()
        raise
    return out


def save_document(doc: pymupdf.Document, config: FinalizeConfig) -> None:
    doc.set_metadata(config.metadata or {})
    enc = config.encryption
    if enc is None:
        doc.save(config.final_path)
        return
    doc.save(
        config.final_path,
        owner_pw=enc.owner_pw,
        user_pw=enc.user_pw,
        permissions=enc.permissions,
        encryption=ENCRYPTION_METHODS[enc.algorithm_index],
    )
