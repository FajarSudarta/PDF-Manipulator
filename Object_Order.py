from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QMimeData, Qt, Signal
from PySide6.QtGui import QColor, QDrag, QMouseEvent, QPalette, QPixmap
from PySide6.QtWidgets import QFrame, QMessageBox
from shiboken6 import isValid

from UI_File.Compiled.Object_Order_UI import Ui_Object_Order
from File_Loader import Object_Loader
from Preview_Page_Sequence import PreviewPageSequence
from Specify_Window import SpecifyWindow
from core.models import OrderConfig, PageMode
from core.page_spec import EDITABLE_MODES, MODE_HELP, PageSpecError, expand_ranges, resolve_ranges

ICON_DIR = Path(__file__).resolve().parent / "Icon"
ICON_SIZE = (80, 85)
FILE_ICONS = {
    ".pdf": "PDF64.png",
    ".jpg": "jpg-file-format_64.png",
    ".jpeg": "jpg-file-format_64.png",
    ".png": "png-file-format_64.png",
}
UNKNOWN_ICON = "unknown-file-types-64.png"
WARNING_ICON = "Warning64x64.png"


class ObjectOrder(QFrame, Ui_Object_Order):
    # Tidak ada lagi callback di konstruktor: MainWindow yang connect signal ini.
    info_signal = Signal(object)    # DocInfo
    delete_signal = Signal(object)  # ObjectOrder

    LOADER_MISSING = (
        "Objek Loader tidak ditemukan",
        "Loader dari order ini sepertinya telah dihapus, silakan import dan load ulang file.",
    )

    def __init__(self, loader: Object_Loader, name: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)

        # State instance (dulu sebagian berupa atribut class, yang dibagi semua instance).
        self.loader = loader
        self.doc_info = loader.info
        self.File_Path = self.doc_info.location
        self._error = False
        self._deleting = False
        self._rotate: int | None = None
        self._repeat = 1
        self._watermark = None
        self._pages_selectable = self.doc_info.page_count > 1

        self.Object_Name.setText(name)
        font = self.Object_Name.font()
        font.setPointSize(12)
        self.Object_Name.setFont(font)
        self._default_name_style = (self.Object_Name.font(), self.Object_Name.palette())

        self.File_Path_Line.setText(self.File_Path)
        self._set_icon(FILE_ICONS.get(self.doc_info.ext, UNKNOWN_ICON))

        # Gambar sudah dikonversi ke PDF saat load, jadi semua format didukung.
        if self._pages_selectable:
            self.Parsing_input.setMaxLength(150)
        else:
            message = "Dokumen hanya memiliki satu halaman"
            self.Parsing_input.setMaxLength(len(message))
            self.Parsing_input.setText(message)
            self.Specify_pages_comboBox.setDisabled(True)
            self.Parsing_input.setDisabled(True)
        self._sync_mode_widgets()
        self.Repetition_Label.setText("")

        self.Specify_pages_comboBox.currentIndexChanged.connect(self._on_mode_changed)
        self.Specify_pages_comboBox.wheelEvent = lambda event: event.ignore()
        self.Info_Specify_BTN.clicked.connect(self.Specify_Info_Func)
        self.Delete_Button.clicked.connect(self.Delete_Event)
        self.Specify_Btn.clicked.connect(self.specify_event)
        self.Preview_Sequence_Page_Button.clicked.connect(self.Preview_Sequence_Event)

    # ---------- config ----------

    def current_mode(self) -> PageMode:
        return PageMode(self.Specify_pages_comboBox.currentIndex())

    def config(self) -> OrderConfig:
        """Snapshot konfigurasi order ini (panel utama + opsi dari SpecifyWindow)."""
        return OrderConfig(
            mode=self.current_mode(),
            page_spec=self.Parsing_input.text().strip(),
            rotate=self._rotate,
            repeat=self._repeat,
            watermark=self._watermark,
        )

    def apply_config(self, cfg: OrderConfig) -> None:
        # setCurrentIndex memicu _on_mode_changed (mengosongkan input), jadi teks di-set sesudahnya.
        self.Specify_pages_comboBox.setCurrentIndex(int(cfg.mode))
        self.Parsing_input.setText(cfg.page_spec)
        self._sync_mode_widgets()
        self._rotate = cfg.rotate
        self._repeat = cfg.repeat
        self._watermark = cfg.watermark
        self.Repetition_Label.setText(f"X {cfg.repeat}" if cfg.repeat > 1 else "")

    def _sync_mode_widgets(self) -> None:
        mode = self.current_mode()
        self.Parsing_input.setReadOnly(mode not in EDITABLE_MODES)
        if mode == PageMode.FROM_END:
            self.Parsing_input.setText("Coming Soon")

    def _on_mode_changed(self) -> None:
        self.Parsing_input.setText("")
        self._sync_mode_widgets()

    def Specify_Info_Func(self):
        title, text = MODE_HELP[self.current_mode()]
        QMessageBox.information(self, f"Specify Info: {title}", text)

    # ---------- loader ----------

    def loader_alive(self) -> bool:
        return isValid(self.loader) and self.loader.is_open

    def _ensure_loader(self) -> bool:
        """Kalau loader sudah dihapus: beri tahu user, minta MainWindow menghapus order ini."""
        if self._deleting:
            return False  # sudah minta dihapus; jangan munculkan pesan dua kali (press lalu release)
        if self.loader_alive():
            return True
        QMessageBox.critical(self, *self.LOADER_MISSING)
        self.Delete_Event()
        return False

    def mark_loader_missing(self) -> None:
        self._set_icon(WARNING_ICON)

    def _set_icon(self, filename: str) -> None:
        pix = QPixmap(str(ICON_DIR / filename)).scaled(
            *ICON_SIZE,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.label.setPixmap(pix)

    # ---------- dialog ----------

    def Preview_Sequence_Event(self):
        if not self._ensure_loader():
            return
        cfg = self.config()
        try:
            ranges = resolve_ranges(cfg.mode, cfg.page_spec, self.doc_info.page_count)
        except PageSpecError as e:
            # Dulu gagal diam-diam (cuma print ke console).
            QMessageBox.warning(self, "Tidak bisa preview", str(e))
            return
        preview = PreviewPageSequence(self, doc=self.loader.doc, pages=expand_ranges(ranges))
        preview.exec()
        preview.deleteLater()

    def specify_event(self):
        if not self._ensure_loader():
            return
        dialog = SpecifyWindow(
            parent=self,
            config=self.config(),
            object_name=self.Object_Name.text(),
            file_path=self.File_Path,
            page_count=self.doc_info.page_count,
            pages_selectable=self._pages_selectable,
        )
        if dialog.exec():
            self.apply_config(dialog.result_config())
        dialog.deleteLater()

    # ---------- tampilan ----------

    def Self_Highlighting(self):
        self.setStyleSheet("QFrame { background: #42f5f2; }")
        font = self.Object_Name.font()
        font.setPointSize(12)
        font.setBold(True)
        self.Object_Name.setFont(font)
        palette = self.Object_Name.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor("yellow"))
        palette.setColor(QPalette.ColorRole.Text, QColor("black"))
        self.Object_Name.setPalette(palette)

    def Self_DeHighlighting(self):
        self.setStyleSheet("")
        self.Object_Name.setFont(self._default_name_style[0])
        self.Object_Name.setPalette(self._default_name_style[1])

    def On_Error(self):
        self._error = True
        self.setStyleSheet("QFrame { background: #fc4503; }")

    # ---------- drag & drop / mouse ----------

    def dropEvent(self, event):
        super().dropEvent(event)
        source = event.source()
        if isinstance(source, ObjectOrder):  # drag dari luar aplikasi punya source None
            source.Self_DeHighlighting()
        event.acceptProposedAction()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        source = event.source()
        if isinstance(source, ObjectOrder) and source is not self:
            layout = self.parentWidget().layout()
            layout.insertWidget(layout.indexOf(self), source)
        super().dragEnterEvent(event)
        event.acceptProposedAction()

    def mousePressEvent(self, event: QMouseEvent):
        if not self._ensure_loader():
            return
        super().mousePressEvent(event)
        if self._error:
            self._error = False
            self.Self_DeHighlighting()
            return
        if event.button() == Qt.MouseButton.LeftButton:
            self.Self_Highlighting()
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec(Qt.DropAction.MoveAction)

    def mouseDoubleClickEvent(self, event):
        if not self._ensure_loader():
            return
        super().mouseDoubleClickEvent(event)
        if event.button() == Qt.MouseButton.RightButton:
            self.info_signal.emit(self.doc_info)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if not self._ensure_loader():
            return
        super().mouseReleaseEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.Self_DeHighlighting()

    def Delete_Event(self):
        if self._deleting:
            return
        self._deleting = True
        # Layout milik MainWindow, jadi MainWindow yang mencabut widget ini.
        self.delete_signal.emit(self)
