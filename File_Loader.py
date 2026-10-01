
from __future__ import annotations

import logging
from pathlib import Path

import pymupdf
from PySide6.QtCore import QUrl, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFrame, QMessageBox

from UI_File.Compiled.File_Loader_UI import Ui_File_Loader
from core.documents import load_document
from core.models import DocInfo

log = logging.getLogger(__name__)

ICON_DIR = Path(__file__).resolve().parent / "Icon"
# Easter egg .dimas dikumpulkan di satu tempat ini saja (dulu tersebar di 3 file).
DIMAS_EXT = ".dimas"
DIMAS_IMAGE = ICON_DIR / "dimas.jpg"


def open_source(path: str) -> tuple[pymupdf.Document, DocInfo]:
    """Buka file yang dipilih user. Melempar core.documents.LoadError kalau gagal."""
    data_path = str(DIMAS_IMAGE) if Path(path).suffix.lower() == DIMAS_EXT else None
    return load_document(path, data_path=data_path)


class Object_Loader(QFrame,Ui_File_Loader):
    """Widget untuk satu file yang sudah di-load.

    Widget ini *tidak pernah gagal dibuat*: dokumen dibuka dulu (open_source) oleh
    MainWindow, baru widget-nya dibuat. Jadi tidak ada lagi flag `failed`,
    `hasattr(self, "File_data")`, atau `del self.File_data`.
    """

    # Signal(object) meneruskan objek Python apa adanya. Signal(dict) mengonversi ke
    # QVariantMap (key wajib str), dan itulah penyebab KeyError: 0.
    add_signal = Signal(object)     # Object_Loader
    delete_signal = Signal(object)  # Object_Loader
    info_signal = Signal(object)    # DocInfo
    DELETE_TITLE = "Menghapus Loader"
    DELETE_TEXT = (
        "Apakah kamu mau melanjutkan?\n"
        "Object Order yang terhubung dengan loader ini tidak akan bisa menemukan loadernya "
        "dan akan otomatis terhapus ketika diproses/diinteraksi."
    )
    def __init__(self, doc: pymupdf.Document, info: DocInfo, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.doc: pymupdf.Document | None = doc  # satu-satunya pemilik dokumen ini
        self.info = info

        self.File_Name.setText(info.location)
        self.Input_Object_Name.setMaxLength(12)

        self.Remove_Btn.clicked.connect(self.Delete_Event)
        self.AddList_Btn.clicked.connect(self.Add_list_Event)
        self.Input_Object_Name.returnPressed.connect(self.Add_list_Event)
        self.Metadata_info_btn.clicked.connect(self.Metadata_info_func)
        self.Open_File_BTN.clicked.connect(self.Open_File_Event)

    @property
    def is_open(self) -> bool:
        return self.doc is not None

    def close_document(self) -> None:
        """Idempotent: aman dipanggil berkali-kali (mirip Drop/RAII)."""
        if self.doc is not None:
            log.info("Close loader: %s", self.info.location)
            self.doc.close()
            self.doc = None

    def requested_order_name(self) -> str:
        name = self.Input_Object_Name.text().strip() or "Order"
        self.Input_Object_Name.setText(name)
        return name

    def Open_File_Event(self):
        # Lintas platform, menggantikan os.startfile (yang hanya ada di Windows).
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.info.location))

    def Metadata_info_func(self):
        lines = [self.info.location, ""]
        lines += [f"{key} : {value}" for key, value in self.info.metadata.items()]
        QMessageBox.information(self, "Metadata Info", "\n".join(lines))

    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        self.info_signal.emit(self.info)

    def Add_list_Event(self):
        self.add_signal.emit(self)

    def Delete_Event(self):
        answer = QMessageBox.warning(
            self, self.DELETE_TITLE, self.DELETE_TEXT,
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if answer == QMessageBox.StandardButton.Ok:
            # Layout milik MainWindow, jadi MainWindow yang mencabut widget ini.
            self.delete_signal.emit(self)
