# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'File_Loader_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_File_Loader(object):
    def setupUi(self, File_Loader):
        if not File_Loader.objectName():
            File_Loader.setObjectName(u"File_Loader")
        File_Loader.resize(383, 134)
        self.horizontalLayout_3 = QHBoxLayout(File_Loader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(File_Loader)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.File_Name = QLineEdit(File_Loader)
        self.File_Name.setObjectName(u"File_Name")
        self.File_Name.setReadOnly(True)

        self.horizontalLayout.addWidget(self.File_Name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(File_Loader)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Input_Object_Name = QLineEdit(File_Loader)
        self.Input_Object_Name.setObjectName(u"Input_Object_Name")

        self.horizontalLayout_2.addWidget(self.Input_Object_Name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AddList_Btn = QPushButton(File_Loader)
        self.AddList_Btn.setObjectName(u"AddList_Btn")

        self.verticalLayout.addWidget(self.AddList_Btn)

        self.Metadata_info_btn = QPushButton(File_Loader)
        self.Metadata_info_btn.setObjectName(u"Metadata_info_btn")

        self.verticalLayout.addWidget(self.Metadata_info_btn)

        self.Open_File_BTN = QPushButton(File_Loader)
        self.Open_File_BTN.setObjectName(u"Open_File_BTN")

        self.verticalLayout.addWidget(self.Open_File_BTN)

        self.Remove_Btn = QPushButton(File_Loader)
        self.Remove_Btn.setObjectName(u"Remove_Btn")

        self.verticalLayout.addWidget(self.Remove_Btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(File_Loader)

        QMetaObject.connectSlotsByName(File_Loader)
    # setupUi

    def retranslateUi(self, File_Loader):
        File_Loader.setWindowTitle(QCoreApplication.translate("File_Loader", u"Frame", None))
        self.label.setText(QCoreApplication.translate("File_Loader", u"File Name:     ", None))
        self.label_2.setText(QCoreApplication.translate("File_Loader", u"Object Name:", None))
        self.AddList_Btn.setText(QCoreApplication.translate("File_Loader", u"Add to list", None))
        self.Metadata_info_btn.setText(QCoreApplication.translate("File_Loader", u"Info", None))
        self.Open_File_BTN.setText(QCoreApplication.translate("File_Loader", u"Open Doc", None))
        self.Remove_Btn.setText(QCoreApplication.translate("File_Loader", u"Remove", None))
    # retranslateUi

