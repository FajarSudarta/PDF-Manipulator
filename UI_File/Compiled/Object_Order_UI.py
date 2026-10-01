# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Object_Order_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Object_Order(object):
    def setupUi(self, Object_Order):
        if not Object_Order.objectName():
            Object_Order.setObjectName(u"Object_Order")
        Object_Order.resize(460, 155)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Object_Order.sizePolicy().hasHeightForWidth())
        Object_Order.setSizePolicy(sizePolicy)
        Object_Order.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(Object_Order)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Object_Order)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.frame = QFrame(Object_Order)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Object_Name = QLineEdit(self.frame)
        self.Object_Name.setObjectName(u"Object_Name")
        self.Object_Name.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.Object_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.File_Path_Line = QLineEdit(self.frame)
        self.File_Path_Line.setObjectName(u"File_Path_Line")
        self.File_Path_Line.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.File_Path_Line)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.HLayout_specifyfilepages = QHBoxLayout()
        self.HLayout_specifyfilepages.setObjectName(u"HLayout_specifyfilepages")
        self.Specify_pages_comboBox = QComboBox(self.frame)
        self.Specify_pages_comboBox.addItem("")
        self.Specify_pages_comboBox.addItem("")
        self.Specify_pages_comboBox.addItem("")
        self.Specify_pages_comboBox.addItem("")
        self.Specify_pages_comboBox.setObjectName(u"Specify_pages_comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Specify_pages_comboBox.sizePolicy().hasHeightForWidth())
        self.Specify_pages_comboBox.setSizePolicy(sizePolicy3)

        self.HLayout_specifyfilepages.addWidget(self.Specify_pages_comboBox)

        self.Parsing_input = QLineEdit(self.frame)
        self.Parsing_input.setObjectName(u"Parsing_input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Parsing_input.sizePolicy().hasHeightForWidth())
        self.Parsing_input.setSizePolicy(sizePolicy4)
        self.Parsing_input.setReadOnly(True)

        self.HLayout_specifyfilepages.addWidget(self.Parsing_input)

        self.Info_Specify_BTN = QPushButton(self.frame)
        self.Info_Specify_BTN.setObjectName(u"Info_Specify_BTN")

        self.HLayout_specifyfilepages.addWidget(self.Info_Specify_BTN)


        self.verticalLayout.addLayout(self.HLayout_specifyfilepages)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Specify_Btn = QPushButton(self.frame)
        self.Specify_Btn.setObjectName(u"Specify_Btn")

        self.horizontalLayout_6.addWidget(self.Specify_Btn)

        self.Preview_Sequence_Page_Button = QPushButton(self.frame)
        self.Preview_Sequence_Page_Button.setObjectName(u"Preview_Sequence_Page_Button")

        self.horizontalLayout_6.addWidget(self.Preview_Sequence_Page_Button)

        self.Delete_Button = QPushButton(self.frame)
        self.Delete_Button.setObjectName(u"Delete_Button")

        self.horizontalLayout_6.addWidget(self.Delete_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addWidget(self.frame)

        self.Repetition_Label = QLabel(Object_Order)
        self.Repetition_Label.setObjectName(u"Repetition_Label")
        self.Repetition_Label.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Repetition_Label.sizePolicy().hasHeightForWidth())
        self.Repetition_Label.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setPointSize(20)
        self.Repetition_Label.setFont(font)

        self.horizontalLayout.addWidget(self.Repetition_Label)


        self.retranslateUi(Object_Order)

        QMetaObject.connectSlotsByName(Object_Order)
    # setupUi

    def retranslateUi(self, Object_Order):
        Object_Order.setWindowTitle(QCoreApplication.translate("Object_Order", u"Frame", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Object_Order", u"Path:   ", None))
        self.Specify_pages_comboBox.setItemText(0, QCoreApplication.translate("Object_Order", u"All Pages", None))
        self.Specify_pages_comboBox.setItemText(1, QCoreApplication.translate("Object_Order", u"Jumlah Halaman", None))
        self.Specify_pages_comboBox.setItemText(2, QCoreApplication.translate("Object_Order", u"Specific Pages", None))
        self.Specify_pages_comboBox.setItemText(3, QCoreApplication.translate("Object_Order", u"Interval Pages", None))

        self.Info_Specify_BTN.setText(QCoreApplication.translate("Object_Order", u"Info", None))
        self.Specify_Btn.setText(QCoreApplication.translate("Object_Order", u"Specify More..", None))
        self.Preview_Sequence_Page_Button.setText(QCoreApplication.translate("Object_Order", u"Preview", None))
        self.Delete_Button.setText(QCoreApplication.translate("Object_Order", u"Delete", None))
        self.Repetition_Label.setText(QCoreApplication.translate("Object_Order", u"X 1", None))
    # retranslateUi

