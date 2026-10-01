from __future__ import annotations


import pymupdf
from PySide6.QtCore import QDateTime, Qt
from PySide6.QtWidgets import QCheckBox, QDateTimeEdit, QDialog, QFileDialog, QMessageBox

from UI_File.Compiled.Finalize_Window_UI import Ui_Finalize_Window
from core.models import Encryption, FinalizeConfig, TextWatermark

TEXT_WATERMARK_TAB = 0
PERMISSION_ALL, PERMISSION_NONE = 0, 1
DATETIME_NOW, DATETIME_CUSTOM = 0, 1


class FinalizeWindow(QDialog, Ui_Finalize_Window):  # class Qt di depan, seperti dialog lain
    """Dialog modal finalisasi. Pakai: `if dlg.exec(): cfg = dlg.config()`.

    Dulu hasilnya dikirim lewat Signal(dict) ke MainWindow.Final_Conf, lalu
    MainWindow mencetaknya ke console, termasuk owner/user password.
    """

    def __init__(self, parent=None, resultpage: int = 0, final_path: str = ""):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Finalisasi Merging Dokumen")
        self.setFixedWidth(self.size().width())
        self._permission = 0
        self._config: FinalizeConfig | None = None

        self.Estimasi_Halaman_Input.setText(str(resultpage))
        self.Final_Path_Input.setText(final_path)

        self.Execute_Merge_Button.clicked.connect(self.Execute_Func)
        self.Cancel_Button.clicked.connect(self.reject)
        self.Add_Watermark_Checkbox.checkStateChanged.connect(
            lambda state: self.Watermark_Tab.setEnabled(state == Qt.CheckState.Checked)
        )
        self.Timedate_Creation_Type.currentIndexChanged.connect(
            lambda mode: self._apply_datetime_mode(self.Timedate_Creation_Input, mode)
        )
        self.Timedate_Modification_Type.currentIndexChanged.connect(
            lambda mode: self._apply_datetime_mode(self.Timedate_Modification_Input, mode)
        )
        self.Change_Path_BTN.clicked.connect(self.Change_Path_Func)
        self.Permission_comboBox.currentIndexChanged.connect(self.Permission_comboBox_Func)
        self.Clear_Metadata_Checkbox.checkStateChanged.connect(
            lambda state: self.Metadata_Edit_Panel.setDisabled(state == Qt.CheckState.Checked)
        )
        self.Policy_Checkbox.checkStateChanged.connect(self.Policy_Panel_Func)
        self.Lock_doc_checkBox.checkStateChanged.connect(
            lambda state: self.Lock_doc_frame.setEnabled(state == Qt.CheckState.Checked)
        )

        permission_boxes = {
            self.allow_print_doc_checkbox: pymupdf.PDF_PERM_PRINT,
            self.allow_modify_doc_checkbox: pymupdf.PDF_PERM_MODIFY,
            self.allow_copy_doc_checkbox: pymupdf.PDF_PERM_COPY,
            self.allow_comment_annotate_checkbox: pymupdf.PDF_PERM_ANNOTATE,
            self.allow_filling_form_checkbox: pymupdf.PDF_PERM_FORM,
            self.allow_read_doc_checkbox: pymupdf.PDF_PERM_ACCESSIBILITY,
            self.allow_assemble_doc_checkbox: pymupdf.PDF_PERM_ASSEMBLE,
            self.allow_high_quality_print_checkbox: pymupdf.PDF_PERM_PRINT_HQ,
        }
        for box, flag in permission_boxes.items():
            # flag=flag: tangkap nilai sekarang (late binding closure di Python).
            box.checkStateChanged.connect(lambda state, flag=flag: self.Permission_func(state, flag))

        self._apply_datetime_mode(self.Timedate_Creation_Input, DATETIME_NOW)
        self._apply_datetime_mode(self.Timedate_Modification_Input, DATETIME_NOW)
        self.Permission_comboBox.setCurrentIndex(PERMISSION_NONE)
        self.Configure_tabWidget.setCurrentIndex(0)
        self.Policy_Frame.setEnabled(False)
        self.Watermark_Tab.setEnabled(False)

    def config(self) -> FinalizeConfig | None:
        return self._config

    # ---------- membaca form ----------

    def _read_metadata(self) -> dict | None:
        if self.Clear_Metadata_Checkbox.isChecked():
            return None
        return {
            "title": self.Title_Input.text().strip(),
            "author": self.Author_Input.text().strip(),
            "subject": self.Subject_Input.text().strip(),
            "keywords": self.Keywords_Input.text().strip(),
            "creator": self.Creator_Input.text().strip(),
            "producer": self.Producer_Input.text().strip(),
            "creationDate": "D:" + self.Timedate_Creation_Input.dateTime().toString("yyyyMMddHHmmss"),
            "modDate": "D:" + self.Timedate_Modification_Input.dateTime().toString("yyyyMMddHHmmss"),
            "trapped": self.trapped_input.text().strip(),
        }

    def _read_encryption(self) -> Encryption | None:
        """Melempar ValueError berisi pesan untuk user kalau form belum lengkap."""
        if not self.Policy_Checkbox.isChecked():
            return None
        owner_pw = self.Owner_Password_Input.text().strip()
        if not owner_pw:
            raise ValueError("Please input owner pass")
        user_pw = ""
        if self.Lock_doc_checkBox.isChecked():
            user_pw = self.User_Password_Input.text().strip()
            if not user_pw:
                raise ValueError("Please input user pass")
        return Encryption(
            owner_pw=owner_pw,
            user_pw=user_pw,
            permissions=self._permission,
            algorithm_index=self.Algorithm_Encryption_ComboBox.currentIndex(),
        )

    def _read_watermark(self) -> TextWatermark | None:
        if not self.Add_Watermark_Checkbox.isChecked():
            return None
        if self.Watermark_Tab.currentIndex() != TEXT_WATERMARK_TAB:
            # Dulu: return diam-diam, tombol Execute terasa "mati".
            raise ValueError("Watermark gambar belum didukung.")
        text = self.Text_watermark_Input.text().strip()
        if not text:
            raise ValueError("No watermark text")
        return TextWatermark(
            text=text,
            font=self.Font_watermark_input.currentText(),
            fontsize=self.Font_size_watermark_input.value(),
            rotation=self.Rotation_text_watermark_input.value(),
            color=(self.Red_color_input.value(), self.Green_Color_Input.value(), self.Blue_Color_Input.value()),
        )

    def Execute_Func(self):
        try:
            config = FinalizeConfig(
                final_path=self.Final_Path_Input.text(),
                metadata=self._read_metadata(),
                encryption=self._read_encryption(),
                watermark=self._read_watermark(),
                open_after_save=self.Open_Document_BTN.isChecked(),
            )
        except ValueError as e:
            QMessageBox.information(self, "Input belum lengkap", str(e))
            return
        self._config = config
        self.accept()

    # ---------- handler UI ----------

    def Change_Path_Func(self):
        path, _ = QFileDialog.getSaveFileName(self, "Ubah direktori Hasil Dokumen", "", "PDF (*.pdf)")
        if not path:
            return
        self.Final_Path_Input.setText(path)
        QMessageBox.information(self, "Direktori Akhir diubah", "Direktori Akhir berhasil diubah")

    def Policy_Panel_Func(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.Policy_Frame.setEnabled(True)
            self.Lock_doc_frame.setEnabled(False)
        else:
            self.Policy_Frame.setEnabled(False)
            self.Lock_doc_checkBox.setChecked(False)

    def Permission_comboBox_Func(self, index: int):
        if index not in (PERMISSION_ALL, PERMISSION_NONE):
            return
        state = Qt.CheckState.Checked if index == PERMISSION_ALL else Qt.CheckState.Unchecked
        for i in range(self.Permission_gridlayout.count()):
            box = self.Permission_gridlayout.itemAt(i).widget()
            if isinstance(box, QCheckBox):
                box.setCheckState(state)
        if index == PERMISSION_NONE:
            self._permission = 0

    def Permission_func(self, state: Qt.CheckState, flag: int):
        if state == Qt.CheckState.Checked:
            self._permission |= flag
        else:
            self._permission &= ~flag

    @staticmethod
    def _apply_datetime_mode(widget: QDateTimeEdit, mode: int) -> None:
        """Dulu dua fungsi identik: Timedate_Creation_Func dan Timedate_Modification_Func."""
        if mode == DATETIME_NOW:
            widget.setDateTime(QDateTime.currentDateTime())
        widget.setReadOnly(mode != DATETIME_CUSTOM)
        widget.setDisabled(mode not in (DATETIME_NOW, DATETIME_CUSTOM))
