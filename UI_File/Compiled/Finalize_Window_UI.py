# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Finalize_Window_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDialog, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Finalize_Window(object):
    def setupUi(self, Finalize_Window):
        if not Finalize_Window.objectName():
            Finalize_Window.setObjectName(u"Finalize_Window")
        Finalize_Window.resize(524, 613)
        self.verticalLayout = QVBoxLayout(Finalize_Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Finalize_Window)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.Estimasi_Halaman_Input = QLabel(self.frame)
        self.Estimasi_Halaman_Input.setObjectName(u"Estimasi_Halaman_Input")

        self.horizontalLayout_4.addWidget(self.Estimasi_Halaman_Input)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.Final_Path_Input = QLineEdit(self.frame)
        self.Final_Path_Input.setObjectName(u"Final_Path_Input")
        self.Final_Path_Input.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.Final_Path_Input)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Change_Path_BTN = QPushButton(self.frame)
        self.Change_Path_BTN.setObjectName(u"Change_Path_BTN")

        self.verticalLayout_2.addWidget(self.Change_Path_BTN)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(Finalize_Window)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Configure_tabWidget = QTabWidget(self.frame_4)
        self.Configure_tabWidget.setObjectName(u"Configure_tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_13 = QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Metadata_Panel = QFrame(self.tab_3)
        self.Metadata_Panel.setObjectName(u"Metadata_Panel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Metadata_Panel.sizePolicy().hasHeightForWidth())
        self.Metadata_Panel.setSizePolicy(sizePolicy)
        self.Metadata_Panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.Metadata_Panel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Metadata_Panel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Clear_Metadata_Checkbox = QCheckBox(self.Metadata_Panel)
        self.Clear_Metadata_Checkbox.setObjectName(u"Clear_Metadata_Checkbox")
        self.Clear_Metadata_Checkbox.setFont(font)

        self.verticalLayout_4.addWidget(self.Clear_Metadata_Checkbox)

        self.Metadata_Edit_Panel = QFrame(self.Metadata_Panel)
        self.Metadata_Edit_Panel.setObjectName(u"Metadata_Edit_Panel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Metadata_Edit_Panel.sizePolicy().hasHeightForWidth())
        self.Metadata_Edit_Panel.setSizePolicy(sizePolicy1)
        self.Metadata_Edit_Panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.Metadata_Edit_Panel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Metadata_Edit_Panel)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.Metadata_Edit_Panel)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.Metadata_Edit_Panel)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.Title_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Title_Input.setObjectName(u"Title_Input")

        self.horizontalLayout_8.addWidget(self.Title_Input)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.Metadata_Edit_Panel)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.Subject_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Subject_Input.setObjectName(u"Subject_Input")

        self.horizontalLayout_14.addWidget(self.Subject_Input)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.Metadata_Edit_Panel)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.Creator_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Creator_Input.setObjectName(u"Creator_Input")

        self.horizontalLayout_12.addWidget(self.Creator_Input)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_15.addLayout(self.verticalLayout_12)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.Metadata_Edit_Panel)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.Keywords_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Keywords_Input.setObjectName(u"Keywords_Input")

        self.horizontalLayout_13.addWidget(self.Keywords_Input)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.Metadata_Edit_Panel)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.Author_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Author_Input.setObjectName(u"Author_Input")

        self.horizontalLayout_3.addWidget(self.Author_Input)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.Metadata_Edit_Panel)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.Producer_Input = QLineEdit(self.Metadata_Edit_Panel)
        self.Producer_Input.setObjectName(u"Producer_Input")

        self.horizontalLayout_11.addWidget(self.Producer_Input)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.Metadata_Edit_Panel)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.Timedate_Creation_Type = QComboBox(self.Metadata_Edit_Panel)
        self.Timedate_Creation_Type.addItem("")
        self.Timedate_Creation_Type.addItem("")
        self.Timedate_Creation_Type.addItem("")
        self.Timedate_Creation_Type.setObjectName(u"Timedate_Creation_Type")

        self.horizontalLayout_6.addWidget(self.Timedate_Creation_Type)

        self.Timedate_Creation_Input = QDateTimeEdit(self.Metadata_Edit_Panel)
        self.Timedate_Creation_Input.setObjectName(u"Timedate_Creation_Input")

        self.horizontalLayout_6.addWidget(self.Timedate_Creation_Input)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.Metadata_Edit_Panel)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.Timedate_Modification_Type = QComboBox(self.Metadata_Edit_Panel)
        self.Timedate_Modification_Type.addItem("")
        self.Timedate_Modification_Type.addItem("")
        self.Timedate_Modification_Type.addItem("")
        self.Timedate_Modification_Type.setObjectName(u"Timedate_Modification_Type")

        self.horizontalLayout_10.addWidget(self.Timedate_Modification_Type)

        self.Timedate_Modification_Input = QDateTimeEdit(self.Metadata_Edit_Panel)
        self.Timedate_Modification_Input.setObjectName(u"Timedate_Modification_Input")

        self.horizontalLayout_10.addWidget(self.Timedate_Modification_Input)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.Metadata_Edit_Panel)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.trapped_input = QLineEdit(self.Metadata_Edit_Panel)
        self.trapped_input.setObjectName(u"trapped_input")

        self.horizontalLayout_9.addWidget(self.trapped_input)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.Metadata_Edit_Panel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_13.addWidget(self.Metadata_Panel)

        self.Configure_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.tab_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Add_Watermark_Checkbox = QCheckBox(self.frame_2)
        self.Add_Watermark_Checkbox.setObjectName(u"Add_Watermark_Checkbox")

        self.verticalLayout_5.addWidget(self.Add_Watermark_Checkbox)

        self.Watermark_Tab = QTabWidget(self.frame_2)
        self.Watermark_Tab.setObjectName(u"Watermark_Tab")
        self.Watermark_Tab.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Watermark_Tab.sizePolicy().hasHeightForWidth())
        self.Watermark_Tab.setSizePolicy(sizePolicy2)
        self.Text_Watermark_Tab = QWidget()
        self.Text_Watermark_Tab.setObjectName(u"Text_Watermark_Tab")
        self.verticalLayout_16 = QVBoxLayout(self.Text_Watermark_Tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_24 = QLabel(self.Text_Watermark_Tab)
        self.label_24.setObjectName(u"label_24")
        font2 = QFont()
        font2.setFamilies([u"Impact"])
        font2.setPointSize(14)
        self.label_24.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.Text_watermark_Input = QLineEdit(self.Text_Watermark_Tab)
        self.Text_watermark_Input.setObjectName(u"Text_watermark_Input")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Text_watermark_Input)

        self.label_25 = QLabel(self.Text_Watermark_Tab)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.Font_watermark_input = QComboBox(self.Text_Watermark_Tab)
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

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Font_watermark_input)

        self.label_26 = QLabel(self.Text_Watermark_Tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.Font_size_watermark_input = QSpinBox(self.Text_Watermark_Tab)
        self.Font_size_watermark_input.setObjectName(u"Font_size_watermark_input")
        self.Font_size_watermark_input.setMinimum(25)
        self.Font_size_watermark_input.setMaximum(50)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Font_size_watermark_input)

        self.label_27 = QLabel(self.Text_Watermark_Tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.Rotation_text_watermark_input = QSpinBox(self.Text_Watermark_Tab)
        self.Rotation_text_watermark_input.setObjectName(u"Rotation_text_watermark_input")
        self.Rotation_text_watermark_input.setMaximum(360)
        self.Rotation_text_watermark_input.setSingleStep(1)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.Rotation_text_watermark_input)

        self.label_28 = QLabel(self.Text_Watermark_Tab)
        self.label_28.setObjectName(u"label_28")
        font3 = QFont()
        font3.setFamilies([u"Impact"])
        font3.setPointSize(12)
        self.label_28.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.Text_Watermark_Tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_29)

        self.Red_color_input = QSpinBox(self.Text_Watermark_Tab)
        self.Red_color_input.setObjectName(u"Red_color_input")

        self.horizontalLayout_19.addWidget(self.Red_color_input)

        self.label_30 = QLabel(self.Text_Watermark_Tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.Green_Color_Input = QSpinBox(self.Text_Watermark_Tab)
        self.Green_Color_Input.setObjectName(u"Green_Color_Input")

        self.horizontalLayout_19.addWidget(self.Green_Color_Input)

        self.label_31 = QLabel(self.Text_Watermark_Tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_31)

        self.Blue_Color_Input = QSpinBox(self.Text_Watermark_Tab)
        self.Blue_Color_Input.setObjectName(u"Blue_Color_Input")

        self.horizontalLayout_19.addWidget(self.Blue_Color_Input)


        self.formLayout_2.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_19)


        self.verticalLayout_16.addLayout(self.formLayout_2)

        self.Watermark_Tab.addTab(self.Text_Watermark_Tab, "")
        self.Image_Watermark_Tab = QWidget()
        self.Image_Watermark_Tab.setObjectName(u"Image_Watermark_Tab")
        self.verticalLayout_17 = QVBoxLayout(self.Image_Watermark_Tab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_32 = QLabel(self.Image_Watermark_Tab)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_17.addWidget(self.label_32)

        self.Watermark_Tab.addTab(self.Image_Watermark_Tab, "")

        self.verticalLayout_5.addWidget(self.Watermark_Tab)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.Configure_tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Policy_Checkbox = QCheckBox(self.tab_5)
        self.Policy_Checkbox.setObjectName(u"Policy_Checkbox")
        self.Policy_Checkbox.setFont(font)

        self.verticalLayout_3.addWidget(self.Policy_Checkbox)

        self.Policy_Frame = QFrame(self.tab_5)
        self.Policy_Frame.setObjectName(u"Policy_Frame")
        self.Policy_Frame.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Policy_Frame.sizePolicy().hasHeightForWidth())
        self.Policy_Frame.setSizePolicy(sizePolicy3)
        self.Policy_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Policy_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Policy_Frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Owner_Password_label = QLabel(self.Policy_Frame)
        self.Owner_Password_label.setObjectName(u"Owner_Password_label")
        self.Owner_Password_label.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.Owner_Password_label)

        self.Owner_Password_Input = QLineEdit(self.Policy_Frame)
        self.Owner_Password_Input.setObjectName(u"Owner_Password_Input")
        self.Owner_Password_Input.setEnabled(True)
        self.Owner_Password_Input.setDragEnabled(False)

        self.horizontalLayout_5.addWidget(self.Owner_Password_Input)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.Permission_comboBox = QComboBox(self.Policy_Frame)
        self.Permission_comboBox.addItem("")
        self.Permission_comboBox.addItem("")
        self.Permission_comboBox.setObjectName(u"Permission_comboBox")

        self.verticalLayout_8.addWidget(self.Permission_comboBox)

        self.Permission_gridlayout = QGridLayout()
        self.Permission_gridlayout.setObjectName(u"Permission_gridlayout")
        self.allow_modify_doc_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_modify_doc_checkbox.setObjectName(u"allow_modify_doc_checkbox")
        self.allow_modify_doc_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_modify_doc_checkbox, 1, 0, 1, 1)

        self.allow_read_doc_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_read_doc_checkbox.setObjectName(u"allow_read_doc_checkbox")
        self.allow_read_doc_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_read_doc_checkbox, 2, 0, 1, 1)

        self.allow_copy_doc_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_copy_doc_checkbox.setObjectName(u"allow_copy_doc_checkbox")
        self.allow_copy_doc_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_copy_doc_checkbox, 3, 0, 1, 1)

        self.allow_print_doc_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_print_doc_checkbox.setObjectName(u"allow_print_doc_checkbox")
        self.allow_print_doc_checkbox.setEnabled(True)
        self.allow_print_doc_checkbox.setCheckable(True)
        self.allow_print_doc_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_print_doc_checkbox, 0, 0, 1, 1)

        self.allow_comment_annotate_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_comment_annotate_checkbox.setObjectName(u"allow_comment_annotate_checkbox")
        self.allow_comment_annotate_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_comment_annotate_checkbox, 0, 1, 1, 1)

        self.allow_filling_form_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_filling_form_checkbox.setObjectName(u"allow_filling_form_checkbox")
        self.allow_filling_form_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_filling_form_checkbox, 1, 1, 1, 1)

        self.allow_high_quality_print_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_high_quality_print_checkbox.setObjectName(u"allow_high_quality_print_checkbox")
        self.allow_high_quality_print_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_high_quality_print_checkbox, 2, 1, 1, 1)

        self.allow_assemble_doc_checkbox = QCheckBox(self.Policy_Frame)
        self.allow_assemble_doc_checkbox.setObjectName(u"allow_assemble_doc_checkbox")
        self.allow_assemble_doc_checkbox.setChecked(False)

        self.Permission_gridlayout.addWidget(self.allow_assemble_doc_checkbox, 3, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.Permission_gridlayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.Policy_Frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.Algorithm_Encryption_ComboBox = QComboBox(self.Policy_Frame)
        self.Algorithm_Encryption_ComboBox.addItem("")
        self.Algorithm_Encryption_ComboBox.addItem("")
        self.Algorithm_Encryption_ComboBox.addItem("")
        self.Algorithm_Encryption_ComboBox.addItem("")
        self.Algorithm_Encryption_ComboBox.setObjectName(u"Algorithm_Encryption_ComboBox")
        self.Algorithm_Encryption_ComboBox.setEnabled(True)
        self.Algorithm_Encryption_ComboBox.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_7.addWidget(self.Algorithm_Encryption_ComboBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.Lock_doc_checkBox = QCheckBox(self.Policy_Frame)
        self.Lock_doc_checkBox.setObjectName(u"Lock_doc_checkBox")
        font4 = QFont()
        font4.setPointSize(11)
        self.Lock_doc_checkBox.setFont(font4)

        self.verticalLayout_8.addWidget(self.Lock_doc_checkBox)

        self.Lock_doc_frame = QFrame(self.Policy_Frame)
        self.Lock_doc_frame.setObjectName(u"Lock_doc_frame")
        self.Lock_doc_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Lock_doc_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Lock_doc_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.User_Password_Label = QLabel(self.Lock_doc_frame)
        self.User_Password_Label.setObjectName(u"User_Password_Label")
        self.User_Password_Label.setEnabled(True)

        self.horizontalLayout_16.addWidget(self.User_Password_Label)

        self.User_Password_Input = QLineEdit(self.Lock_doc_frame)
        self.User_Password_Input.setObjectName(u"User_Password_Input")
        self.User_Password_Input.setEnabled(True)

        self.horizontalLayout_16.addWidget(self.User_Password_Input)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)


        self.verticalLayout_8.addWidget(self.Lock_doc_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.Policy_Frame)

        self.Configure_tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_9.addWidget(self.Configure_tabWidget)


        self.verticalLayout.addWidget(self.frame_4)

        self.Open_Document_BTN = QCheckBox(Finalize_Window)
        self.Open_Document_BTN.setObjectName(u"Open_Document_BTN")

        self.verticalLayout.addWidget(self.Open_Document_BTN)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Execute_Merge_Button = QPushButton(Finalize_Window)
        self.Execute_Merge_Button.setObjectName(u"Execute_Merge_Button")

        self.horizontalLayout.addWidget(self.Execute_Merge_Button)

        self.Cancel_Button = QPushButton(Finalize_Window)
        self.Cancel_Button.setObjectName(u"Cancel_Button")

        self.horizontalLayout.addWidget(self.Cancel_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Finalize_Window)

        self.Configure_tabWidget.setCurrentIndex(1)
        self.Watermark_Tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Finalize_Window)
    # setupUi

    def retranslateUi(self, Finalize_Window):
        Finalize_Window.setWindowTitle(QCoreApplication.translate("Finalize_Window", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Finalize_Window", u"Summary", None))
        self.label_3.setText(QCoreApplication.translate("Finalize_Window", u"Estimasi Halaman                        :", None))
        self.Estimasi_Halaman_Input.setText(QCoreApplication.translate("Finalize_Window", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Finalize_Window", u"Final Path                                     :", None))
        self.Change_Path_BTN.setText(QCoreApplication.translate("Finalize_Window", u"Ubah Path Penyimpanan", None))
        self.Clear_Metadata_Checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Kosongkan Metadata", None))
        self.label_8.setText(QCoreApplication.translate("Finalize_Window", u"Metadata Edit", None))
        self.label_10.setText(QCoreApplication.translate("Finalize_Window", u"Title ", None))
        self.label_16.setText(QCoreApplication.translate("Finalize_Window", u"Subject", None))
        self.label_14.setText(QCoreApplication.translate("Finalize_Window", u"Creator ", None))
        self.label_15.setText(QCoreApplication.translate("Finalize_Window", u"Keywords ", None))
        self.label.setText(QCoreApplication.translate("Finalize_Window", u"Author", None))
        self.label_13.setText(QCoreApplication.translate("Finalize_Window", u"Producer", None))
        self.label_7.setText(QCoreApplication.translate("Finalize_Window", u"Creation Date", None))
        self.Timedate_Creation_Type.setItemText(0, QCoreApplication.translate("Finalize_Window", u"Waktu Saat ini", None))
        self.Timedate_Creation_Type.setItemText(1, QCoreApplication.translate("Finalize_Window", u"Palsukan", None))
        self.Timedate_Creation_Type.setItemText(2, QCoreApplication.translate("Finalize_Window", u"Kosongkan", None))

        self.label_12.setText(QCoreApplication.translate("Finalize_Window", u"Modification Date", None))
        self.Timedate_Modification_Type.setItemText(0, QCoreApplication.translate("Finalize_Window", u"Waktu Saat ini", None))
        self.Timedate_Modification_Type.setItemText(1, QCoreApplication.translate("Finalize_Window", u"Palsukan", None))
        self.Timedate_Modification_Type.setItemText(2, QCoreApplication.translate("Finalize_Window", u"Kosongkan", None))

        self.label_11.setText(QCoreApplication.translate("Finalize_Window", u"trapped ", None))
        self.Configure_tabWidget.setTabText(self.Configure_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Finalize_Window", u"Metadata", None))
        self.Add_Watermark_Checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Tambahkan Watermark", None))
        self.label_24.setText(QCoreApplication.translate("Finalize_Window", u"Text:    ", None))
        self.label_25.setText(QCoreApplication.translate("Finalize_Window", u"Font", None))
        self.Font_watermark_input.setItemText(0, QCoreApplication.translate("Finalize_Window", u"courier", None))
        self.Font_watermark_input.setItemText(1, QCoreApplication.translate("Finalize_Window", u"courier-oblique", None))
        self.Font_watermark_input.setItemText(2, QCoreApplication.translate("Finalize_Window", u"courier-bold", None))
        self.Font_watermark_input.setItemText(3, QCoreApplication.translate("Finalize_Window", u"courier-boldoblique", None))
        self.Font_watermark_input.setItemText(4, QCoreApplication.translate("Finalize_Window", u"helvetica", None))
        self.Font_watermark_input.setItemText(5, QCoreApplication.translate("Finalize_Window", u"helvetica-oblique", None))
        self.Font_watermark_input.setItemText(6, QCoreApplication.translate("Finalize_Window", u"helvetica-bold", None))
        self.Font_watermark_input.setItemText(7, QCoreApplication.translate("Finalize_Window", u"helvetica-boldoblique", None))
        self.Font_watermark_input.setItemText(8, QCoreApplication.translate("Finalize_Window", u"times-roman", None))
        self.Font_watermark_input.setItemText(9, QCoreApplication.translate("Finalize_Window", u"times-italic", None))
        self.Font_watermark_input.setItemText(10, QCoreApplication.translate("Finalize_Window", u"times-bold", None))
        self.Font_watermark_input.setItemText(11, QCoreApplication.translate("Finalize_Window", u"times-bolditalic", None))
        self.Font_watermark_input.setItemText(12, QCoreApplication.translate("Finalize_Window", u"symbol", None))
        self.Font_watermark_input.setItemText(13, QCoreApplication.translate("Finalize_Window", u"zapfdingbats", None))

        self.label_26.setText(QCoreApplication.translate("Finalize_Window", u"Font Size", None))
        self.label_27.setText(QCoreApplication.translate("Finalize_Window", u"Rotation", None))
        self.label_28.setText(QCoreApplication.translate("Finalize_Window", u"Color Text", None))
        self.label_29.setText(QCoreApplication.translate("Finalize_Window", u"Red", None))
        self.label_30.setText(QCoreApplication.translate("Finalize_Window", u"Green", None))
        self.label_31.setText(QCoreApplication.translate("Finalize_Window", u"Blue", None))
        self.Watermark_Tab.setTabText(self.Watermark_Tab.indexOf(self.Text_Watermark_Tab), QCoreApplication.translate("Finalize_Window", u"Text", None))
        self.label_32.setText(QCoreApplication.translate("Finalize_Window", u"Image: Coming Soon", None))
        self.Watermark_Tab.setTabText(self.Watermark_Tab.indexOf(self.Image_Watermark_Tab), QCoreApplication.translate("Finalize_Window", u"Image", None))
        self.Configure_tabWidget.setTabText(self.Configure_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Finalize_Window", u"Watermark", None))
        self.Policy_Checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Add Policy and Lock Document", None))
        self.Owner_Password_label.setText(QCoreApplication.translate("Finalize_Window", u"Owner Pssword", None))
        self.Permission_comboBox.setItemText(0, QCoreApplication.translate("Finalize_Window", u"Allow All", None))
        self.Permission_comboBox.setItemText(1, QCoreApplication.translate("Finalize_Window", u"Deny All", None))

        self.allow_modify_doc_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Modify Document", None))
        self.allow_read_doc_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Reading Document", None))
        self.allow_copy_doc_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Copy Content", None))
        self.allow_print_doc_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Print Document", None))
        self.allow_comment_annotate_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Comment/Annotate", None))
        self.allow_filling_form_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Filling Form", None))
        self.allow_high_quality_print_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow High Quality Printing", None))
        self.allow_assemble_doc_checkbox.setText(QCoreApplication.translate("Finalize_Window", u"Allow Merge/Split Document", None))
        self.label_4.setText(QCoreApplication.translate("Finalize_Window", u"Pilih Algoritma Enkripsi:", None))
        self.Algorithm_Encryption_ComboBox.setItemText(0, QCoreApplication.translate("Finalize_Window", u"RC4 40-bit", None))
        self.Algorithm_Encryption_ComboBox.setItemText(1, QCoreApplication.translate("Finalize_Window", u"RC4 128-bit", None))
        self.Algorithm_Encryption_ComboBox.setItemText(2, QCoreApplication.translate("Finalize_Window", u"AES 128-bit", None))
        self.Algorithm_Encryption_ComboBox.setItemText(3, QCoreApplication.translate("Finalize_Window", u"AES 256-bit (Recommended)", None))

        self.Lock_doc_checkBox.setText(QCoreApplication.translate("Finalize_Window", u"Lock Document (Need User Password)", None))
        self.User_Password_Label.setText(QCoreApplication.translate("Finalize_Window", u"User_Password: ", None))
        self.Configure_tabWidget.setTabText(self.Configure_tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Finalize_Window", u"Policy", None))
        self.Open_Document_BTN.setText(QCoreApplication.translate("Finalize_Window", u"Buka hasil merging setelah selesai", None))
        self.Execute_Merge_Button.setText(QCoreApplication.translate("Finalize_Window", u"Execute Merge", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Finalize_Window", u"Cancel", None))
    # retranslateUi

