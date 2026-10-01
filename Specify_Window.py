from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox

from UI_File.Compiled.Specify_Window_UI import Ui_specify_window
from core.models import OrderConfig, PageMode, TextWatermark
from core.page_spec import EDITABLE_MODES, PageSpecError, resolve_ranges

TEXT_WATERMARK_TAB = 0


class SpecifyWindow(QDialog, Ui_specify_window):
    """Dialog modal untuk mengatur satu ObjectOrder.

    Pola pemakaian (tanpa signal):
        dialog = SpecifyWindow(...)
        if dialog.exec():
            cfg = dialog.result_config()
    Dulu hasilnya dikirim lewat Signal(dict), dan closeEvent meng-emit {} lagi
    setelah OK, sehingga slot-nya terpanggil dua kali.
    """

    def __init__(self, parent=None, *, config: OrderConfig, object_name: str = "",
                 file_path: str = "", page_count: int = 0, pages_selectable: bool = True):
        super().__init__(parent)
        self.setupUi(self)
        self.page_count = page_count
        self._result: OrderConfig | None = None

        self.setWindowTitle(object_name)
        self.setMinimumSize(572, 279)
        self.Object_Name_Label.setText(object_name)
        self.File_path_location.setText(file_path)
        self.Specifiy_Window_Tab.setCurrentIndex(0)

        # Halaman
        self.Specify_page.setCurrentIndex(int(config.mode))
        self.Specify_page_input.setText(config.page_spec)
        self._sync_mode_widgets()
        if not pages_selectable:  # dulu parameter ini tidak pernah dikirim oleh ObjectOrder
            self.Specify_page.setDisabled(True)
            self.Specify_page_input.setDisabled(True)
        self.Specify_page.currentIndexChanged.connect(self._on_mode_changed)
        self.Specify_page.wheelEvent = lambda event: event.ignore()

        # Rotasi
        rotate_enabled = config.rotate is not None
        self.Putar_Halaman_CheckBox.setChecked(rotate_enabled)
        self.Rotate_Page_Input.setEnabled(rotate_enabled)
        if rotate_enabled:
            self.Rotate_Page_Input.setValue(config.rotate)  # dulu setValue(0): rotasi ter-reset
        self.Putar_Halaman_CheckBox.checkStateChanged.connect(
            lambda state: self.Rotate_Page_Input.setEnabled(state == Qt.CheckState.Checked)
        )
        self.Rotate_Page_Input.wheelEvent = lambda event: event.ignore()

        # Repetisi
        self.Repetition_Count_Input.setEnabled(True)
        self.Repetition_Count_Input.setValue(config.repeat)
        self.Repetition_Count_Input.wheelEvent = lambda event: event.ignore()

        # Watermark
        self.Add_Watermark_Checkbox.checkStateChanged.connect(self._set_watermark_enabled)
        wm = config.watermark
        self.Add_Watermark_Checkbox.setChecked(wm is not None)
        self._set_watermark_enabled(Qt.CheckState.Checked if wm else Qt.CheckState.Unchecked)
        if wm is not None:
            self.Text_watermark_Input.setText(wm.text)
            self.Font_watermark_input.setCurrentText(wm.font)
            self.Font_size_watermark_input.setValue(wm.fontsize)
            self.Rotation_text_watermark_input.setValue(wm.rotation)
            self.Red_color_input.setValue(wm.color[0])
            self.Green_Color_Input.setValue(wm.color[1])
            self.Blue_Color_Input.setValue(wm.color[2])
            self.Timpa_watermark_checkbox.setChecked(wm.overlay_universal)

        self.Ok_Button.clicked.connect(self._on_ok)
        self.Cancel_Button.clicked.connect(self.reject)

    def result_config(self) -> OrderConfig | None:
        return self._result

    def _current_mode(self) -> PageMode:
        return PageMode(self.Specify_page.currentIndex())

    def _sync_mode_widgets(self) -> None:
        mode = self._current_mode()
        self.Specify_page_input.setReadOnly(mode not in EDITABLE_MODES)
        if mode == PageMode.FROM_END:
            self.Specify_page_input.setText("Coming Soon")

    def _on_mode_changed(self) -> None:
        self.Specify_page_input.setText("")
        self._sync_mode_widgets()

    def _set_watermark_enabled(self, state: Qt.CheckState) -> None:
        enabled = state == Qt.CheckState.Checked
        self.Watermark_Tab.setEnabled(enabled)
        self.Timpa_watermark_checkbox.setEnabled(enabled)

    def _read_watermark(self) -> TextWatermark | None:
        """Melempar ValueError berisi pesan untuk user kalau input watermark belum lengkap."""
        if not self.Add_Watermark_Checkbox.isChecked():
            return None
        if self.Watermark_Tab.currentIndex() != TEXT_WATERMARK_TAB:
            raise ValueError("Watermark gambar belum didukung.")
        text = self.Text_watermark_Input.text().strip()
        if not text:
            raise ValueError("Silakan isi teks yang dijadikan watermark.")
        return TextWatermark(
            text=text,
            font=self.Font_watermark_input.currentText(),
            fontsize=self.Font_size_watermark_input.value(),
            rotation=self.Rotation_text_watermark_input.value(),
            color=(self.Red_color_input.value(), self.Green_Color_Input.value(), self.Blue_Color_Input.value()),
            overlay_universal=self.Timpa_watermark_checkbox.isChecked(),
        )

    def _on_ok(self) -> None:
        mode = self._current_mode()
        page_spec = self.Specify_page_input.text().strip()
        if self.Specify_page.isEnabled():
            try:
                resolve_ranges(mode, page_spec, self.page_count)  # aturan yang sama dengan Merge
            except PageSpecError as e:
                QMessageBox.warning(self, "Input halaman tidak valid", str(e))
                return
        try:
            watermark = self._read_watermark()
        except ValueError as e:
            QMessageBox.information(self, "Watermark", str(e))
            return

        self._result = OrderConfig(
            mode=mode,
            page_spec=page_spec,
            rotate=self.Rotate_Page_Input.value() if self.Putar_Halaman_CheckBox.isChecked() else None,
            repeat=self.Repetition_Count_Input.value(),
            watermark=watermark,
        )
        self.accept()
