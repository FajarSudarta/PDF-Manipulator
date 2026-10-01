# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Specify_Window_UI.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDialog, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_specify_window(object):
    def setupUi(self, specify_window):
        if not specify_window.objectName():
            specify_window.setObjectName(u"specify_window")
        specify_window.resize(572, 497)
        specify_window.setMinimumSize(QSize(572, 279))
        self.verticalLayout_2 = QVBoxLayout(specify_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(specify_window)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 552, 437))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Object_Name_Label = QLabel(self.frame_2)
        self.Object_Name_Label.setObjectName(u"Object_Name_Label")
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(22)
        self.Object_Name_Label.setFont(font)

        self.horizontalLayout_7.addWidget(self.Object_Name_Label)

        self.File_path_location = QLineEdit(self.frame_2)
        self.File_path_location.setObjectName(u"File_path_location")
        font1 = QFont()
        font1.setPointSize(12)
        self.File_path_location.setFont(font1)

        self.horizontalLayout_7.addWidget(self.File_path_location)


        self.verticalLayout.addWidget(self.frame_2)

        self.Specifiy_Window_Tab = QTabWidget(self.scrollAreaWidgetContents)
        self.Specifiy_Window_Tab.setObjectName(u"Specifiy_Window_Tab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Specify_page = QComboBox(self.frame)
        self.Specify_page.addItem("")
        self.Specify_page.addItem("")
        self.Specify_page.addItem("")
        self.Specify_page.addItem("")
        self.Specify_page.setObjectName(u"Specify_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Specify_page.sizePolicy().hasHeightForWidth())
        self.Specify_page.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Impact"])
        font2.setPointSize(12)
        self.Specify_page.setFont(font2)

        self.horizontalLayout_6.addWidget(self.Specify_page)

        self.Specify_page_input = QLineEdit(self.frame)
        self.Specify_page_input.setObjectName(u"Specify_page_input")
        self.Specify_page_input.setFont(font2)

        self.horizontalLayout_6.addWidget(self.Specify_page_input)


        self.verticalLayout_11.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.Specifiy_Window_Tab.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalFrame = QFrame(self.tab_3)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Putar_Halaman_CheckBox = QCheckBox(self.horizontalFrame)
        self.Putar_Halaman_CheckBox.setObjectName(u"Putar_Halaman_CheckBox")
        font3 = QFont()
        font3.setFamilies([u"Impact"])
        font3.setPointSize(14)
        self.Putar_Halaman_CheckBox.setFont(font3)
        self.Putar_Halaman_CheckBox.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.Putar_Halaman_CheckBox)

        self.Rotate_Page_Input = QSpinBox(self.horizontalFrame)
        self.Rotate_Page_Input.setObjectName(u"Rotate_Page_Input")
        self.Rotate_Page_Input.setEnabled(True)
        self.Rotate_Page_Input.setFont(font2)
        self.Rotate_Page_Input.setMinimum(90)
        self.Rotate_Page_Input.setMaximum(270)
        self.Rotate_Page_Input.setSingleStep(90)
        self.Rotate_Page_Input.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Rotate_Page_Input.setValue(90)

        self.horizontalLayout.addWidget(self.Rotate_Page_Input)


        self.verticalLayout_9.addWidget(self.horizontalFrame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.Specifiy_Window_Tab.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_10 = QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.tab_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Impact"])
        font4.setPointSize(16)
        self.label.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label)

        self.Repetition_Count_Input = QSpinBox(self.frame_3)
        self.Repetition_Count_Input.setObjectName(u"Repetition_Count_Input")
        self.Repetition_Count_Input.setFont(font2)
        self.Repetition_Count_Input.setMinimum(1)
        self.Repetition_Count_Input.setMaximum(5)

        self.horizontalLayout_8.addWidget(self.Repetition_Count_Input)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.Specifiy_Window_Tab.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Add_Watermark_Checkbox = QCheckBox(self.frame_4)
        self.Add_Watermark_Checkbox.setObjectName(u"Add_Watermark_Checkbox")
        self.Add_Watermark_Checkbox.setFont(font2)

        self.verticalLayout_7.addWidget(self.Add_Watermark_Checkbox)

        self.Watermark_Tab = QTabWidget(self.frame_4)
        self.Watermark_Tab.setObjectName(u"Watermark_Tab")
        self.Watermark_Tab.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Watermark_Tab.sizePolicy().hasHeightForWidth())
        self.Watermark_Tab.setSizePolicy(sizePolicy)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_18 = QVBoxLayout(self.tab_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_33 = QLabel(self.tab_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.Text_watermark_Input = QLineEdit(self.tab_8)
        self.Text_watermark_Input.setObjectName(u"Text_watermark_Input")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Text_watermark_Input)

        self.label_34 = QLabel(self.tab_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.Font_watermark_input = QComboBox(self.tab_8)
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.addItem("")
        self.Font_watermark_input.setObjectName(u"Font_watermark_input")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Font_watermark_input)

        self.label_35 = QLabel(self.tab_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.Font_size_watermark_input = QSpinBox(self.tab_8)
        self.Font_size_watermark_input.setObjectName(u"Font_size_watermark_input")
        self.Font_size_watermark_input.setMinimum(25)
        self.Font_size_watermark_input.setMaximum(50)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Font_size_watermark_input)

        self.label_36 = QLabel(self.tab_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.Rotation_text_watermark_input = QSpinBox(self.tab_8)
        self.Rotation_text_watermark_input.setObjectName(u"Rotation_text_watermark_input")
        self.Rotation_text_watermark_input.setMaximum(360)
        self.Rotation_text_watermark_input.setSingleStep(1)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.Rotation_text_watermark_input)

        self.label_37 = QLabel(self.tab_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_37)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_38 = QLabel(self.tab_8)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_38)

        self.Red_color_input = QSpinBox(self.tab_8)
        self.Red_color_input.setObjectName(u"Red_color_input")
        self.Red_color_input.setMaximum(255)

        self.horizontalLayout_20.addWidget(self.Red_color_input)

        self.label_39 = QLabel(self.tab_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_39)

        self.Green_Color_Input = QSpinBox(self.tab_8)
        self.Green_Color_Input.setObjectName(u"Green_Color_Input")
        self.Green_Color_Input.setMaximum(255)

        self.horizontalLayout_20.addWidget(self.Green_Color_Input)

        self.label_40 = QLabel(self.tab_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_40)

        self.Blue_Color_Input = QSpinBox(self.tab_8)
        self.Blue_Color_Input.setObjectName(u"Blue_Color_Input")
        self.Blue_Color_Input.setMaximum(255)

        self.horizontalLayout_20.addWidget(self.Blue_Color_Input)


        self.formLayout_3.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_20)


        self.verticalLayout_18.addLayout(self.formLayout_3)

        self.Watermark_Tab.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_19 = QVBoxLayout(self.tab_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_41 = QLabel(self.tab_9)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_19.addWidget(self.label_41)

        self.Watermark_Tab.addTab(self.tab_9, "")

        self.verticalLayout_7.addWidget(self.Watermark_Tab)

        self.Timpa_watermark_checkbox = QCheckBox(self.frame_4)
        self.Timpa_watermark_checkbox.setObjectName(u"Timpa_watermark_checkbox")

        self.verticalLayout_7.addWidget(self.Timpa_watermark_checkbox)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.Specifiy_Window_Tab.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.Specifiy_Window_Tab)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Ok_Button = QPushButton(specify_window)
        self.Ok_Button.setObjectName(u"Ok_Button")
        self.Ok_Button.setFont(font3)

        self.horizontalLayout_5.addWidget(self.Ok_Button)

        self.Cancel_Button = QPushButton(specify_window)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setFont(font3)

        self.horizontalLayout_5.addWidget(self.Cancel_Button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(specify_window)

        self.Specifiy_Window_Tab.setCurrentIndex(3)
        self.Watermark_Tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(specify_window)
    # setupUi

    def retranslateUi(self, specify_window):
        specify_window.setWindowTitle(QCoreApplication.translate("specify_window", u"Dialog", None))
        self.Object_Name_Label.setText(QCoreApplication.translate("specify_window", u"TextLabel", None))
        self.Specify_page.setItemText(0, QCoreApplication.translate("specify_window", u"All Pages", None))
        self.Specify_page.setItemText(1, QCoreApplication.translate("specify_window", u"Jumlah Halaman", None))
        self.Specify_page.setItemText(2, QCoreApplication.translate("specify_window", u"Specific Pages", None))
        self.Specify_page.setItemText(3, QCoreApplication.translate("specify_window", u"Interval Pages", None))

        self.Specifiy_Window_Tab.setTabText(self.Specifiy_Window_Tab.indexOf(self.tab), QCoreApplication.translate("specify_window", u"Specify Sequence Page", None))
        self.Putar_Halaman_CheckBox.setText(QCoreApplication.translate("specify_window", u"Putar Halaman", None))
        self.Rotate_Page_Input.setSuffix(QCoreApplication.translate("specify_window", u" derajat", None))
        self.Rotate_Page_Input.setPrefix("")
        self.Specifiy_Window_Tab.setTabText(self.Specifiy_Window_Tab.indexOf(self.tab_3), QCoreApplication.translate("specify_window", u"Rotate Page", None))
        self.label.setText(QCoreApplication.translate("specify_window", u"Repetisi", None))
        self.Specifiy_Window_Tab.setTabText(self.Specifiy_Window_Tab.indexOf(self.tab_4), QCoreApplication.translate("specify_window", u"Repetisi", None))
        self.Add_Watermark_Checkbox.setText(QCoreApplication.translate("specify_window", u"Tambahkan Watermark", None))
        self.label_33.setText(QCoreApplication.translate("specify_window", u"Text:    ", None))
        self.label_34.setText(QCoreApplication.translate("specify_window", u"Font", None))
        self.Font_watermark_input.setItemText(0, QCoreApplication.translate("specify_window", u"courier", None))
        self.Font_watermark_input.setItemText(1, QCoreApplication.translate("specify_window", u"courier-oblique", None))
        self.Font_watermark_input.setItemText(2, QCoreApplication.translate("specify_window", u"courier-bold", None))
        self.Font_watermark_input.setItemText(3, QCoreApplication.translate("specify_window", u"courier-boldoblique", None))
        self.Font_watermark_input.setItemText(4, QCoreApplication.translate("specify_window", u"helvetica", None))
        self.Font_watermark_input.setItemText(5, QCoreApplication.translate("specify_window", u"helvetica-oblique", None))
        self.Font_watermark_input.setItemText(6, QCoreApplication.translate("specify_window", u"helvetica-bold", None))
        self.Font_watermark_input.setItemText(7, QCoreApplication.translate("specify_window", u"helvetica-boldoblique", None))
        self.Font_watermark_input.setItemText(8, QCoreApplication.translate("specify_window", u"times-roman", None))
        self.Font_watermark_input.setItemText(9, QCoreApplication.translate("specify_window", u"times-italic", None))
        self.Font_watermark_input.setItemText(10, QCoreApplication.translate("specify_window", u"times-bold", None))
        self.Font_watermark_input.setItemText(11, QCoreApplication.translate("specify_window", u"times-bolditalic", None))
        self.Font_watermark_input.setItemText(12, QCoreApplication.translate("specify_window", u"symbol", None))
        self.Font_watermark_input.setItemText(13, QCoreApplication.translate("specify_window", u"zapfdingbats", None))

        self.label_35.setText(QCoreApplication.translate("specify_window", u"Font Size", None))
        self.label_36.setText(QCoreApplication.translate("specify_window", u"Rotation", None))
        self.label_37.setText(QCoreApplication.translate("specify_window", u"Color Text", None))
        self.label_38.setText(QCoreApplication.translate("specify_window", u"Red", None))
        self.label_39.setText(QCoreApplication.translate("specify_window", u"Green", None))
        self.label_40.setText(QCoreApplication.translate("specify_window", u"Blue", None))
        self.Watermark_Tab.setTabText(self.Watermark_Tab.indexOf(self.tab_8), QCoreApplication.translate("specify_window", u"Text", None))
        self.label_41.setText(QCoreApplication.translate("specify_window", u"Image: Coming Soon", None))
        self.Watermark_Tab.setTabText(self.Watermark_Tab.indexOf(self.tab_9), QCoreApplication.translate("specify_window", u"Image", None))
        self.Timpa_watermark_checkbox.setText(QCoreApplication.translate("specify_window", u"Timpa dengan universal watermark", None))
        self.Specifiy_Window_Tab.setTabText(self.Specifiy_Window_Tab.indexOf(self.tab_2), QCoreApplication.translate("specify_window", u"Watermark", None))
        self.Ok_Button.setText(QCoreApplication.translate("specify_window", u"Ok", None))
        self.Cancel_Button.setText(QCoreApplication.translate("specify_window", u"Cancel", None))
    # retranslateUi

