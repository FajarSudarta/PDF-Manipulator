# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Preview_Page_Sequence_Window_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Preview_Sequence_ObjectOrder(object):
    def setupUi(self, Preview_Sequence_ObjectOrder):
        if not Preview_Sequence_ObjectOrder.objectName():
            Preview_Sequence_ObjectOrder.setObjectName(u"Preview_Sequence_ObjectOrder")
        Preview_Sequence_ObjectOrder.resize(566, 626)
        self.verticalLayout = QVBoxLayout(Preview_Sequence_ObjectOrder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Page_Viewer_Embed = QLabel(Preview_Sequence_ObjectOrder)
        self.Page_Viewer_Embed.setObjectName(u"Page_Viewer_Embed")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Page_Viewer_Embed.sizePolicy().hasHeightForWidth())
        self.Page_Viewer_Embed.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(24)
        self.Page_Viewer_Embed.setFont(font)
        self.Page_Viewer_Embed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Page_Viewer_Embed)

        self.Halaman_Label = QLabel(Preview_Sequence_ObjectOrder)
        self.Halaman_Label.setObjectName(u"Halaman_Label")
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(18)
        self.Halaman_Label.setFont(font1)
        self.Halaman_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Halaman_Label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Previous_Interval_Button = QPushButton(Preview_Sequence_ObjectOrder)
        self.Previous_Interval_Button.setObjectName(u"Previous_Interval_Button")

        self.horizontalLayout.addWidget(self.Previous_Interval_Button)

        self.Previous_Page_Button = QPushButton(Preview_Sequence_ObjectOrder)
        self.Previous_Page_Button.setObjectName(u"Previous_Page_Button")

        self.horizontalLayout.addWidget(self.Previous_Page_Button)

        self.Next_Page_Button = QPushButton(Preview_Sequence_ObjectOrder)
        self.Next_Page_Button.setObjectName(u"Next_Page_Button")

        self.horizontalLayout.addWidget(self.Next_Page_Button)

        self.Next_Interval_Button = QPushButton(Preview_Sequence_ObjectOrder)
        self.Next_Interval_Button.setObjectName(u"Next_Interval_Button")

        self.horizontalLayout.addWidget(self.Next_Interval_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Preview_Sequence_ObjectOrder)

        QMetaObject.connectSlotsByName(Preview_Sequence_ObjectOrder)
    # setupUi

    def retranslateUi(self, Preview_Sequence_ObjectOrder):
        Preview_Sequence_ObjectOrder.setWindowTitle(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"Dialog", None))
        self.Page_Viewer_Embed.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"Page", None))
        self.Halaman_Label.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"Halaman: ", None))
        self.Previous_Interval_Button.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"< Previous Interval", None))
        self.Previous_Page_Button.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"< Previous Page", None))
        self.Next_Page_Button.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"Next Page >", None))
        self.Next_Interval_Button.setText(QCoreApplication.translate("Preview_Sequence_ObjectOrder", u"Next Interval >", None))
    # retranslateUi

