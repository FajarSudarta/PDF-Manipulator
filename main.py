import logging
import sys
from PySide6 import QtWidgets
from UI_File.Compiling_Scripts import Compile_ALL


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    # TODO: jadikan langkah build terpisah (mis. script `python -m UI_File.Compiling_Scripts`)
    # alih-alih jalan di setiap startup. Belum diubah karena isi Compiling_Scripts tidak ikut di-upload.
    Compile_ALL() #<- berguna untuk compile ..ui ke .py semua sebelum di jalankan

    from Main_Window import MainWindow  # import setelah .ui dikompilasi

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow("PDF Manipulator")
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
