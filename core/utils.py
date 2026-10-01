from __future__ import annotations

import os
from collections.abc import Collection


def format_size(num_bytes: float) -> str:
    """1536 -> '1.50 KB'. Dulu Specify_byte_unit, terduplikasi di dua class."""
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def unique_name(base: str, used: Collection[str]) -> str:
    """'Order' -> 'Order', lalu 'Order(2)', 'Order(3)', ...

    Menggantikan list_objek_name + list_all_objek_name. `used` dihitung dari
    widget yang masih hidup, jadi tidak perlu bookkeeping saat order dihapus.
    """
    if base not in used:
        return base
    n = 2
    while f"{base}({n})" in used:
        n += 1
    return f"{base}({n})"


def norm_path(path: str) -> str:
    """Kunci pembanding path: absolut, separator seragam, case-insensitive di Windows.

    QFileDialog selalu mengembalikan '/', sedangkan versi lama menyimpan path loader
    dengan '\\', sehingga cek "jangan overwrite loader" tidak pernah cocok.
    """
    return os.path.normcase(os.path.realpath(path))
