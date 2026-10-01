from __future__ import annotations
import logging
import os
from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtGui import QCloseEvent, QDesktopServices
from PySide6.QtWidgets import QFileDialog, QMessageBox
from UI_File.Compiled.Main_Window_UI import Ui_MainWindow
from File_Loader import Object_Loader, open_source
from Finalize_Window import FinalizeWindow
from Object_Order import ObjectOrder
from core.documents import LoadError
from core.merge import build_document, plan_order, save_document
from core.models import DocInfo
from core.page_spec import PageSpecError
from core.utils import norm_path, unique_name


import traceback

log = logging.getLogger(__name__)
IMPORT_FILTER = (
    "Supported Format (*.pdf *.jpg *.jpeg *.png *.dimas);;PDF (*.pdf);;"
    "JPEG (*.jpg *.jpeg);;PNG (*.png);;File Dimas (*.dimas)"
)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    LIMIT_MB : int = 100
    LIMIT_PAGE : int = 1000
    LIMIT_OBJECTORDER : int = 50

    def __init__(self,title:str):
        super().__init__()

        self.setupUi(self)
        self.safe_mode = True
        self.setMinimumSize(895,640)
        self.setWindowTitle(title)
        self.safe_mode = True
        # norm_path(path) -> loader. Menggantikan list_path; kuncinya sudah dinormalisasi
        # sehingga cek duplikat dan cek "jangan overwrite loader" benar-benar cocok.

        self.loaders: dict[str, Object_Loader] = {}

        self.Load_File_Button.setText("Import Document")
        self.Load_File_Button.clicked.connect(self.Load_Event)
        self.Merge_BTN.clicked.connect(self.Merge_Event)
        self.Safe_mode_button.clicked.connect(self._on_safe_mode_clicked)

        self.Label_ObjectOrder_Kosong = self.List_ObjectOrder.itemAt(0).widget()
        self.List_ObjectOrder.addStretch()
        self.Loader_list.addStretch()

    # ---------- helper ----------
    def _orders(self) -> list[ObjectOrder]:
        layout = self.List_ObjectOrder
        items = (layout.itemAt(i).widget() for i in range(layout.count()))
        return [w for w in items if isinstance(w,ObjectOrder)]

    def _is_loader_path(self,path: str) -> bool:
        return norm_path(path) in self.loaders

    def _update_empty_state(self) -> None:
        self.Label_ObjectOrder_Kosong.setVisible(not self._orders())

    @staticmethod
    def _insert_before_stretch(layout: QtWidgets.QBoxLayout, widget: QtWidgets.QWidget) -> None:
       layout.insertWidget(layout.count() - 1, widget)

    # ---------- safe mode ----------
    def _on_safe_mode_clicked(self,checked:bool):
        #print(state)
        if checked:
            self.safe_mode = True
            return
        self.Safe_mode_button.setChecked(True)  # batalkan dulu sampai user konfirmasi
        answer = QMessageBox.warning(
            self,
            "Matikan safe mode",
            "Apakah kamu yakin untuk matikan safe mode?\n"
            "Jika dimatikan, user bisa melewati batas default sistem. "
            "Ini berpotensi membuat sistem overload jika berlebihan.",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if answer == QMessageBox.StandardButton.Ok:
            self.Safe_mode_button.setChecked(False)
            self.safe_mode = False
        log.info("Safe mode: %s", self.safe_mode)

    # ---------- info panel ----------
    def Show_File_Info_Event(self,info:DocInfo):
        self.Info_NameFile.setText(info.file_name)
        self.Info_File_Location.setText(info.location)
        self.Info_Page.setText(f"{info.page_count} Halaman")
        self.Info_File_Size.setText(info.file_size)
        self.Info_Format.setText(info.ext)


    def Clear_document_info_pages(self):
         for label in (self.Info_NameFile, self.Info_File_Location, self.Info_Page,
                       self.Info_File_Size, self.Info_Format):
             label.setText("")

    # ---------- loader ----------

    def Load_Event(self):
         paths, _ = QFileDialog.getOpenFileNames(self, "Pilih File", "", IMPORT_FILTER)
         for path in paths:
             if self._is_loader_path(path):
                 QMessageBox.information(self, "File sudah di-load", f"File {os.path.normpath(path)} sudah di-import")
                 continue

             size_mb = os.path.getsize(path) / (1024 * 1024)
             if size_mb >= self.LIMIT_MB and self.safe_mode:
                 QMessageBox.warning(
                     self, "File terlalu besar",
                     f"Tidak bisa me-load file berukuran {size_mb:.2f} MB.\nMaksimum adalah {self.LIMIT_MB} MB",
                 )
                 continue

             try:
                 doc, info = open_source(path)
             except LoadError as e:
                 # Satu file gagal tidak menghentikan file lain di multi-select.
                 log.warning("Gagal load %s: %s", path, e)
                 QMessageBox.critical(self, "Tidak bisa membuka file", f"{os.path.normpath(path)}\n\n{e}")
                 continue

             loader = Object_Loader(doc, info)
             loader.add_signal.connect(self.Add_ObjectOrder_Event)
             loader.delete_signal.connect(self.Delete_Loader_Event)
             loader.info_signal.connect(self.Show_File_Info_Event)
             self.loaders[norm_path(path)] = loader
             self._insert_before_stretch(self.Loader_list, loader)
             log.info("Loaded %s (%d halaman)", info.location, info.page_count)

    def Delete_Loader_Event(self, loader: Object_Loader):
         self.loaders = {k: v for k, v in self.loaders.items() if v is not loader}
         self.Loader_list.removeWidget(loader)
         loader.hide()  # removeWidget tidak menyembunyikan widget; deleteLater baru jalan di iterasi event berikutnya
         if self.Info_File_Location.text() == loader.info.location:
             self.Clear_document_info_pages()
         for order in self._orders():
             if order.loader is loader:
                 order.mark_loader_missing()
         loader.close_document()
         loader.deleteLater()

    # ---------- object order ----------
    def Add_ObjectOrder_Event(self, loader: Object_Loader):
        orders = self._orders()
        if len(orders) >= self.LIMIT_OBJECTORDER and self.safe_mode:
            QMessageBox.warning(self, "Melebihi batas", "Object Order melebihi batas")
            return
        used = {o.Object_Name.text() for o in orders}
        name = unique_name(loader.requested_order_name(), used)

        order = ObjectOrder(loader, name)
        order.info_signal.connect(self.Show_File_Info_Event)
        order.delete_signal.connect(self.Delete_ObjectOrder_Event)
        self._insert_before_stretch(self.List_ObjectOrder, order)
        self._update_empty_state()

    def Delete_ObjectOrder_Event(self, order: ObjectOrder):
         self.List_ObjectOrder.removeWidget(order)
         order.hide()
         order.deleteLater()
         self._update_empty_state()

    def Merge_Event(self):
        orders = self._orders()
        if not orders and not self.loaders:
            QMessageBox.information(self, "r u serious?", "Tidak ada loader dan File objek")
            return
        if not orders or not self.loaders:
            QMessageBox.information(
                self, "Tidak ada loader atau ObjectOrder",
                "Merging pdf tidak bisa dilanjutkan.\nTidak ada file yang di-load, yang benar saja!",
            )
            return

        path, _ = QFileDialog.getSaveFileName(self, "Pilih File", "", "PDF (*.pdf)")
        if not path:
            return
        if self._is_loader_path(path):
            self._warn_overwrite_loader()
            return

        # 1) Validasi semua order dulu, sebelum ada dokumen yang dibuat.
        plans = []
        for order in orders:
            name = order.Object_Name.text()
            if not order.loader_alive():
                QMessageBox.critical(self, "Tidak ada Loader",
                                     f"Block Order {name} tidak memiliki Loader\nSepertinya telah dihapus")
                order.On_Error()
                return
            try:
                plans.append(plan_order(name, order.loader.doc, order.config()))
            except PageSpecError as e:
                QMessageBox.critical(self, "Input halaman tidak valid", f"Order {name}:\n{e}")
                order.On_Error()
                return

        total_pages = sum(p.page_total for p in plans)
        if total_pages > self.LIMIT_PAGE and self.safe_mode:
            QMessageBox.warning(self, "Warning", f"Estimasi {total_pages} halaman melebihi batas {self.LIMIT_PAGE}")
            return

        # 2) Dialog finalisasi: modal, hasilnya dibaca langsung (tanpa signal + self.Final_Conf).
        dialog = FinalizeWindow(self, resultpage=total_pages, final_path=path)
        accepted = dialog.exec()
        config = dialog.config()
        dialog.deleteLater()
        if not accepted or config is None:
            return
        if self._is_loader_path(config.final_path):
            self._warn_overwrite_loader()
            return

        # 3) Bangun dan simpan. `with` menutup dokumen hasil apa pun yang terjadi.
        try:
            with build_document(plans, config.watermark) as out:
                save_document(out, config)
        except Exception as e:
            log.exception("Gagal membuat/menyimpan %s", config.final_path)
            QMessageBox.critical(
                self, "Gagal menyimpan dokumen",
                f"Dokumen gagal dibuat atau disimpan.\n"
                f"Pastikan file tujuan tidak sedang dibuka aplikasi lain.\n\nDetail: {e}",
            )
            return

        log.info("Tersimpan: %s (%d halaman)", config.final_path, total_pages)
        if config.open_after_save:
            QDesktopServices.openUrl(QUrl.fromLocalFile(config.final_path))


    def _warn_overwrite_loader(self):
         QMessageBox.warning(self, "Warning",
                             "Path akhir dokumen adalah salah satu file loader!\nTidak boleh overwrite loader")

    def Show_Info_File_Already_Loaded(self,path):
        QMessageBox.information(self,"File sudah di loaded",f"File {path} sudah di import",QMessageBox.StandardButton.Ok)


     # ---------- lifecycle ----------
    def closeEvent(self, event: QCloseEvent):
         for loader in self.loaders.values():
             loader.close_document()
         self.loaders.clear()
         super().closeEvent(event)
