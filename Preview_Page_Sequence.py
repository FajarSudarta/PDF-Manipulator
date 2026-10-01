from __future__ import annotations

import pymupdf
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QDialog

from UI_File.Compiled.Preview_Page_Sequence_Window_UI import Ui_Preview_Sequence_ObjectOrder

# Render sekali di resolusi yang cukup tajam, lalu cukup di-scale saat window di-resize.
# (Dulu: zoom 0.5 dan render ulang dari PDF di setiap resizeEvent.)
RENDER_ZOOM = 1.5


class PreviewPageSequence(QDialog, Ui_Preview_Sequence_ObjectOrder):
    """Menampilkan halaman sesuai urutan yang akan di-merge.

    `pages` adalah list index halaman 0-based yang sudah di-expand
    (core.page_spec.expand_ranges), jadi semua mode (all, spesifik, interval,
    interval terbalik) cukup dinavigasi dengan satu index.
    Dulu: tiga fungsi navigasi berbeda + state dict "current"/"current interval".
    """

    def __init__(self, parent, doc: pymupdf.Document, pages: list[int]):
        super().__init__(parent)
        self.setupUi(self)
        if not pages:
            raise ValueError("pages tidak boleh kosong")
        self._doc = doc
        self._pages = pages
        self._idx = 0
        self._pixmap: QPixmap | None = None

        self.Next_Page_Button.clicked.connect(lambda: self._step(1))
        self.Previous_Page_Button.clicked.connect(lambda: self._step(-1))
        # Tunggu layout selesai supaya ukuran Page_Viewer_Embed sudah benar.
        QTimer.singleShot(0, self._render)

    def _step(self, delta: int) -> None:
        self._idx = (self._idx + delta) % len(self._pages)
        self._render()

    def _render(self) -> None:
        page_no = self._pages[self._idx]
        pix = self._doc.load_page(page_no).get_pixmap(matrix=pymupdf.Matrix(RENDER_ZOOM, RENDER_ZOOM))
        fmt = QImage.Format.Format_RGBA8888 if pix.alpha else QImage.Format.Format_RGB888
        # QImage(buffer, ...) tidak menyalin buffer; .copy() membuat QImage memiliki
        # datanya sendiri sehingga tidak bergantung pada umur objek `pix`.
        image = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt).copy()
        self._pixmap = QPixmap.fromImage(image)
        self.Halaman_Label.setText(f"Halaman: {page_no + 1}   ({self._idx + 1}/{len(self._pages)})")
        self._show_scaled()

    def _show_scaled(self) -> None:
        if self._pixmap is None:
            return
        self.Page_Viewer_Embed.setPixmap(
            self._pixmap.scaled(
                self.Page_Viewer_Embed.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._show_scaled()
