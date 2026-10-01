# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 641)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.List_Objek = QScrollArea(self.centralwidget)
        self.List_Objek.setObjectName(u"List_Objek")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.List_Objek.sizePolicy().hasHeightForWidth())
        self.List_Objek.setSizePolicy(sizePolicy2)
        self.List_Objek.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.List_Objek.setWidgetResizable(True)
        self.List_Objek_Konten = QWidget()
        self.List_Objek_Konten.setObjectName(u"List_Objek_Konten")
        self.List_Objek_Konten.setGeometry(QRect(0, 0, 378, 513))
        self.List_ObjectOrder = QVBoxLayout(self.List_Objek_Konten)
        self.List_ObjectOrder.setObjectName(u"List_ObjectOrder")
        self.Label_Penanda_Kosong = QLabel(self.List_Objek_Konten)
        self.Label_Penanda_Kosong.setObjectName(u"Label_Penanda_Kosong")
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(18)
        self.Label_Penanda_Kosong.setFont(font1)
        self.Label_Penanda_Kosong.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.List_ObjectOrder.addWidget(self.Label_Penanda_Kosong)

        self.List_Objek.setWidget(self.List_Objek_Konten)

        self.verticalLayout_2.addWidget(self.List_Objek)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Safe_mode_button = QCheckBox(self.frame_3)
        self.Safe_mode_button.setObjectName(u"Safe_mode_button")
        self.Safe_mode_button.setEnabled(True)
        font2 = QFont()
        font2.setUnderline(False)
        self.Safe_mode_button.setFont(font2)
        self.Safe_mode_button.setChecked(True)

        self.verticalLayout_3.addWidget(self.Safe_mode_button)

        self.Load_File_Button = QPushButton(self.frame_3)
        self.Load_File_Button.setObjectName(u"Load_File_Button")
        sizePolicy3.setHeightForWidth(self.Load_File_Button.sizePolicy().hasHeightForWidth())
        self.Load_File_Button.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Impact"])
        font3.setPointSize(14)
        self.Load_File_Button.setFont(font3)

        self.verticalLayout_3.addWidget(self.Load_File_Button)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 358, 195))
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy6)
        self.Loader_list = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.Loader_list.setObjectName(u"Loader_list")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.scrollArea_3 = QScrollArea(self.frame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 346, 253))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.Info_NameFile = QLineEdit(self.frame_7)
        self.Info_NameFile.setObjectName(u"Info_NameFile")
        self.Info_NameFile.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.Info_NameFile)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy7.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy7)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.Info_File_Location = QLineEdit(self.frame_13)
        self.Info_File_Location.setObjectName(u"Info_File_Location")
        self.Info_File_Location.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.Info_File_Location)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy7.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy7)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.Info_Page = QLineEdit(self.frame_16)
        self.Info_Page.setObjectName(u"Info_Page")
        self.Info_Page.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.Info_Page)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy7.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy7)
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.Info_File_Size = QLineEdit(self.frame_21)
        self.Info_File_Size.setObjectName(u"Info_File_Size")
        self.Info_File_Size.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.Info_File_Size)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy7.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy7)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.Info_Format = QLineEdit(self.frame_15)
        self.Info_Format.setObjectName(u"Info_Format")
        self.Info_Format.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.Info_Format)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Merge_BTN = QPushButton(self.frame)
        self.Merge_BTN.setObjectName(u"Merge_BTN")

        self.horizontalLayout_4.addWidget(self.Merge_BTN)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"List Object Order", None))
        self.Label_Penanda_Kosong.setText(QCoreApplication.translate("MainWindow", u"Tidak ada ObjekOrder", None))
        self.Safe_mode_button.setText(QCoreApplication.translate("MainWindow", u"Safe Mode", None))
        self.Load_File_Button.setText(QCoreApplication.translate("MainWindow", u"Import Dokumen", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"File Loader", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Document Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nama File:        ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lokasi File:        ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Halaman: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Besar File:         ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Jenis Format File: ", None))
        self.Merge_BTN.setText(QCoreApplication.translate("MainWindow", u"Execute Process", None))
    # retranslateUi

