# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nemo_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from classdefs.modmodifiersarea import ModifiersArea
from classdefs.modnmobscanwidget import NMOBScanWidget
from classdefs.modtkspectrumwidget import TKSpectrumWidget

class Ui_NemoMainWindow(object):
    def setupUi(self, NemoMainWindow):
        if not NemoMainWindow.objectName():
            NemoMainWindow.setObjectName(u"NemoMainWindow")
        NemoMainWindow.resize(1168, 838)
        self.centralwidget = QWidget(NemoMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_data_set_name = QLabel(self.centralwidget)
        self.label_data_set_name.setObjectName(u"label_data_set_name")
        font = QFont()
        font.setPointSize(12)
        self.label_data_set_name.setFont(font)

        self.verticalLayout_2.addWidget(self.label_data_set_name)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_lhs = QFrame(self.centralwidget)
        self.frame_lhs.setObjectName(u"frame_lhs")
        self.frame_lhs.setMaximumSize(QSize(250, 16777215))
        self.frame_lhs.setFrameShape(QFrame.StyledPanel)
        self.frame_lhs.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame_lhs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_lhs)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_add_modifier = QPushButton(self.frame_lhs)
        self.pushButton_add_modifier.setObjectName(u"pushButton_add_modifier")
        self.pushButton_add_modifier.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_add_modifier)

        self.pushButton_delete_modifier = QPushButton(self.frame_lhs)
        self.pushButton_delete_modifier.setObjectName(u"pushButton_delete_modifier")
        self.pushButton_delete_modifier.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_delete_modifier)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = ModifiersArea(self.frame_lhs)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.frame_lhs)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nmo_b_scan_widget = NMOBScanWidget(self.centralwidget)
        self.nmo_b_scan_widget.setObjectName(u"nmo_b_scan_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nmo_b_scan_widget.sizePolicy().hasHeightForWidth())
        self.nmo_b_scan_widget.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.nmo_b_scan_widget)

        self.tabWidget_nmo = QTabWidget(self.centralwidget)
        self.tabWidget_nmo.setObjectName(u"tabWidget_nmo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget_nmo.sizePolicy().hasHeightForWidth())
        self.tabWidget_nmo.setSizePolicy(sizePolicy2)
        self.tabWidget_nmo.setMaximumSize(QSize(16777215, 200))
        self.tab_nmo_plot = QWidget()
        self.tab_nmo_plot.setObjectName(u"tab_nmo_plot")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_nmo_plot)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_2 = QScrollArea(self.tab_nmo_plot)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 394, 178))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        font1 = QFont()
        font1.setBold(True)
        self.label_21.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_21)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_nmo_c_min = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_nmo_c_min.setObjectName(u"doubleSpinBox_nmo_c_min")
        self.doubleSpinBox_nmo_c_min.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_nmo_c_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_nmo_c_min.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_nmo_c_min.setFont(font2)
        self.doubleSpinBox_nmo_c_min.setDecimals(4)
        self.doubleSpinBox_nmo_c_min.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_nmo_c_min.setMaximum(1000.000000000000000)
        self.doubleSpinBox_nmo_c_min.setSingleStep(0.010000000000000)
        self.doubleSpinBox_nmo_c_min.setValue(-0.100000000000000)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_nmo_c_min)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_nmo_c_max = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_nmo_c_max.setObjectName(u"doubleSpinBox_nmo_c_max")
        self.doubleSpinBox_nmo_c_max.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_nmo_c_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_nmo_c_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_nmo_c_max.setFont(font2)
        self.doubleSpinBox_nmo_c_max.setDecimals(4)
        self.doubleSpinBox_nmo_c_max.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_nmo_c_max.setMaximum(1000.000000000000000)
        self.doubleSpinBox_nmo_c_max.setSingleStep(0.010000000000000)
        self.doubleSpinBox_nmo_c_max.setValue(0.100000000000000)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_nmo_c_max)


        self.verticalLayout_7.addLayout(self.formLayout_5)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_22)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.doubleSpinBox_nmo_t_min = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_nmo_t_min.setObjectName(u"doubleSpinBox_nmo_t_min")
        self.doubleSpinBox_nmo_t_min.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_nmo_t_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_nmo_t_min.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_nmo_t_min.setFont(font2)
        self.doubleSpinBox_nmo_t_min.setDecimals(4)
        self.doubleSpinBox_nmo_t_min.setMinimum(-100.000000000000000)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_nmo_t_min)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.doubleSpinBox_nmo_t_max = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.doubleSpinBox_nmo_t_max.setObjectName(u"doubleSpinBox_nmo_t_max")
        self.doubleSpinBox_nmo_t_max.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_nmo_t_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_nmo_t_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_nmo_t_max.setFont(font2)
        self.doubleSpinBox_nmo_t_max.setDecimals(4)
        self.doubleSpinBox_nmo_t_max.setMinimum(-100.000000000000000)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_nmo_t_max)


        self.verticalLayout_7.addLayout(self.formLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_5.addWidget(self.scrollArea_2)

        self.tabWidget_nmo.addTab(self.tab_nmo_plot, "")
        self.tab_nmo_data = QWidget()
        self.tab_nmo_data.setObjectName(u"tab_nmo_data")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_nmo_data)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea_5 = QScrollArea(self.tab_nmo_data)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 411, 151))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_23 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_23)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_24 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_24)

        self.doubleSpinBox_source_half_width_mm = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_source_half_width_mm.setObjectName(u"doubleSpinBox_source_half_width_mm")
        self.doubleSpinBox_source_half_width_mm.setEnabled(False)
        self.doubleSpinBox_source_half_width_mm.setDecimals(5)
        self.doubleSpinBox_source_half_width_mm.setSingleStep(0.001000000000000)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_source_half_width_mm)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_25)

        self.doubleSpinBox_rise_time_us = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox_rise_time_us.setObjectName(u"doubleSpinBox_rise_time_us")
        self.doubleSpinBox_rise_time_us.setEnabled(False)
        self.doubleSpinBox_rise_time_us.setDecimals(5)
        self.doubleSpinBox_rise_time_us.setSingleStep(0.001000000000000)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_rise_time_us)


        self.verticalLayout_5.addLayout(self.formLayout_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_7.addWidget(self.scrollArea_5)

        self.tabWidget_nmo.addTab(self.tab_nmo_data, "")
        self.tab_nmo_tools = QWidget()
        self.tab_nmo_tools.setObjectName(u"tab_nmo_tools")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_nmo_tools)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_6 = QScrollArea(self.tab_nmo_tools)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 394, 256))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox_x_max = QCheckBox(self.groupBox_2)
        self.checkBox_x_max.setObjectName(u"checkBox_x_max")
        self.checkBox_x_max.setEnabled(False)
        self.checkBox_x_max.setFont(font2)

        self.verticalLayout_11.addWidget(self.checkBox_x_max)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_box_mask = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_box_mask.setObjectName(u"groupBox_box_mask")
        self.groupBox_box_mask.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_box_mask.sizePolicy().hasHeightForWidth())
        self.groupBox_box_mask.setSizePolicy(sizePolicy4)
        self.groupBox_box_mask.setFont(font1)
        self.groupBox_box_mask.setCheckable(True)
        self.groupBox_box_mask.setChecked(False)
        self.formLayout_7 = QFormLayout(self.groupBox_box_mask)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.groupBox_box_mask)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.doubleSpinBox_box_mask_t_lower = QDoubleSpinBox(self.groupBox_box_mask)
        self.doubleSpinBox_box_mask_t_lower.setObjectName(u"doubleSpinBox_box_mask_t_lower")
        self.doubleSpinBox_box_mask_t_lower.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_box_mask_t_lower.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_box_mask_t_lower.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_box_mask_t_lower.setFont(font2)
        self.doubleSpinBox_box_mask_t_lower.setDecimals(4)
        self.doubleSpinBox_box_mask_t_lower.setMinimum(-100.000000000000000)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_box_mask_t_lower)

        self.label_15 = QLabel(self.groupBox_box_mask)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.doubleSpinBox_box_mask_t_upper = QDoubleSpinBox(self.groupBox_box_mask)
        self.doubleSpinBox_box_mask_t_upper.setObjectName(u"doubleSpinBox_box_mask_t_upper")
        self.doubleSpinBox_box_mask_t_upper.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_box_mask_t_upper.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_box_mask_t_upper.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_box_mask_t_upper.setFont(font2)
        self.doubleSpinBox_box_mask_t_upper.setDecimals(4)
        self.doubleSpinBox_box_mask_t_upper.setMinimum(-100.000000000000000)
        self.doubleSpinBox_box_mask_t_upper.setMaximum(100.000000000000000)
        self.doubleSpinBox_box_mask_t_upper.setValue(1.000000000000000)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_box_mask_t_upper)

        self.label_16 = QLabel(self.groupBox_box_mask)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.spinBox_box_mask_i_lower = QSpinBox(self.groupBox_box_mask)
        self.spinBox_box_mask_i_lower.setObjectName(u"spinBox_box_mask_i_lower")
        self.spinBox_box_mask_i_lower.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.spinBox_box_mask_i_lower.sizePolicy().hasHeightForWidth())
        self.spinBox_box_mask_i_lower.setSizePolicy(sizePolicy3)
        self.spinBox_box_mask_i_lower.setFont(font2)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.spinBox_box_mask_i_lower)

        self.label_17 = QLabel(self.groupBox_box_mask)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.spinBox_box_mask_i_upper = QSpinBox(self.groupBox_box_mask)
        self.spinBox_box_mask_i_upper.setObjectName(u"spinBox_box_mask_i_upper")
        self.spinBox_box_mask_i_upper.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.spinBox_box_mask_i_upper.sizePolicy().hasHeightForWidth())
        self.spinBox_box_mask_i_upper.setSizePolicy(sizePolicy3)
        self.spinBox_box_mask_i_upper.setFont(font2)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.spinBox_box_mask_i_upper)


        self.verticalLayout_10.addWidget(self.groupBox_box_mask)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)

        self.verticalLayout_10.addWidget(self.groupBox)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_8.addWidget(self.scrollArea_6)

        self.tabWidget_nmo.addTab(self.tab_nmo_tools, "")

        self.verticalLayout_3.addWidget(self.tabWidget_nmo)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tk_spectrum_widget = TKSpectrumWidget(self.centralwidget)
        self.tk_spectrum_widget.setObjectName(u"tk_spectrum_widget")
        sizePolicy1.setHeightForWidth(self.tk_spectrum_widget.sizePolicy().hasHeightForWidth())
        self.tk_spectrum_widget.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.tk_spectrum_widget)

        self.tabWidget_tk = QTabWidget(self.centralwidget)
        self.tabWidget_tk.setObjectName(u"tabWidget_tk")
        sizePolicy2.setHeightForWidth(self.tabWidget_tk.sizePolicy().hasHeightForWidth())
        self.tabWidget_tk.setSizePolicy(sizePolicy2)
        self.tabWidget_tk.setMaximumSize(QSize(16777215, 200))
        self.tab_tk_plot = QWidget()
        self.tab_tk_plot.setObjectName(u"tab_tk_plot")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_tk_plot)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea_4 = QScrollArea(self.tab_tk_plot)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy1.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy1)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 410, 151))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_20)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.doubleSpinBox_tk_c_min = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.doubleSpinBox_tk_c_min.setObjectName(u"doubleSpinBox_tk_c_min")
        self.doubleSpinBox_tk_c_min.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_tk_c_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_tk_c_min.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_tk_c_min.setFont(font2)
        self.doubleSpinBox_tk_c_min.setDecimals(4)
        self.doubleSpinBox_tk_c_min.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_tk_c_min.setMaximum(10000.000000000000000)
        self.doubleSpinBox_tk_c_min.setSingleStep(0.001000000000000)
        self.doubleSpinBox_tk_c_min.setValue(-3.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_tk_c_min)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.doubleSpinBox_tk_c_max = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.doubleSpinBox_tk_c_max.setObjectName(u"doubleSpinBox_tk_c_max")
        self.doubleSpinBox_tk_c_max.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_tk_c_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_tk_c_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_tk_c_max.setFont(font2)
        self.doubleSpinBox_tk_c_max.setDecimals(4)
        self.doubleSpinBox_tk_c_max.setMinimum(-10000.000000000000000)
        self.doubleSpinBox_tk_c_max.setMaximum(10000.000000000000000)
        self.doubleSpinBox_tk_c_max.setSingleStep(0.001000000000000)
        self.doubleSpinBox_tk_c_max.setValue(3.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_tk_c_max)


        self.verticalLayout_9.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_3.addWidget(self.scrollArea_4)

        self.tabWidget_tk.addTab(self.tab_tk_plot, "")
        self.tab_tk_data = QWidget()
        self.tab_tk_data.setObjectName(u"tab_tk_data")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_tk_data)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea = QScrollArea(self.tab_tk_data)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 393, 234))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_18)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox_tk_v_min = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_tk_v_min.setObjectName(u"doubleSpinBox_tk_v_min")
        self.doubleSpinBox_tk_v_min.setEnabled(False)
        self.doubleSpinBox_tk_v_min.setFont(font2)
        self.doubleSpinBox_tk_v_min.setMinimum(1.000000000000000)
        self.doubleSpinBox_tk_v_min.setMaximum(100000.000000000000000)
        self.doubleSpinBox_tk_v_min.setValue(1.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_tk_v_min)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.doubleSpinBox_tk_v_max = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_tk_v_max.setObjectName(u"doubleSpinBox_tk_v_max")
        self.doubleSpinBox_tk_v_max.setEnabled(False)
        self.doubleSpinBox_tk_v_max.setFont(font2)
        self.doubleSpinBox_tk_v_max.setMaximum(100000.000000000000000)
        self.doubleSpinBox_tk_v_max.setValue(7000.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_tk_v_max)

        self.spinBox_tk_n_vs = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_tk_n_vs.setObjectName(u"spinBox_tk_n_vs")
        self.spinBox_tk_n_vs.setEnabled(False)
        self.spinBox_tk_n_vs.setFont(font2)
        self.spinBox_tk_n_vs.setMaximum(1000)
        self.spinBox_tk_n_vs.setValue(200)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBox_tk_n_vs)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout_8.addLayout(self.formLayout_3)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_19)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox_tk_t_0_min = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_tk_t_0_min.setObjectName(u"doubleSpinBox_tk_t_0_min")
        self.doubleSpinBox_tk_t_0_min.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.doubleSpinBox_tk_t_0_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_tk_t_0_min.setSizePolicy(sizePolicy6)
        self.doubleSpinBox_tk_t_0_min.setFont(font2)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_tk_t_0_min)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.doubleSpinBox_tk_t_0_max = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_tk_t_0_max.setObjectName(u"doubleSpinBox_tk_t_0_max")
        self.doubleSpinBox_tk_t_0_max.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.doubleSpinBox_tk_t_0_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_tk_t_0_max.setSizePolicy(sizePolicy6)
        self.doubleSpinBox_tk_t_0_max.setFont(font2)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_tk_t_0_max)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.spinBox_tk_n_t0s = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_tk_n_t0s.setObjectName(u"spinBox_tk_n_t0s")
        self.spinBox_tk_n_t0s.setEnabled(False)
        self.spinBox_tk_n_t0s.setFont(font2)
        self.spinBox_tk_n_t0s.setMaximum(1000)
        self.spinBox_tk_n_t0s.setValue(200)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinBox_tk_n_t0s)


        self.verticalLayout_8.addLayout(self.formLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.tabWidget_tk.addTab(self.tab_tk_data, "")
        self.tab_tk_tools = QWidget()
        self.tab_tk_tools.setObjectName(u"tab_tk_tools")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_tk_tools)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scrollArea_3 = QScrollArea(self.tab_tk_tools)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 410, 151))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_box_select = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_box_select.setObjectName(u"pushButton_box_select")
        self.pushButton_box_select.setCheckable(True)
        self.pushButton_box_select.setChecked(False)

        self.horizontalLayout_6.addWidget(self.pushButton_box_select)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_print_tk = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_print_tk.setObjectName(u"pushButton_print_tk")
        self.pushButton_print_tk.setCheckable(False)
        self.pushButton_print_tk.setChecked(False)

        self.horizontalLayout_10.addWidget(self.pushButton_print_tk)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_9.addWidget(self.scrollArea_3)

        self.tabWidget_tk.addTab(self.tab_tk_tools, "")

        self.verticalLayout_4.addWidget(self.tabWidget_tk)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        NemoMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NemoMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1168, 22))
        NemoMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NemoMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        NemoMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NemoMainWindow)

        self.tabWidget_nmo.setCurrentIndex(0)
        self.tabWidget_tk.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NemoMainWindow)
    # setupUi

    def retranslateUi(self, NemoMainWindow):
        NemoMainWindow.setWindowTitle(QCoreApplication.translate("NemoMainWindow", u"MainWindow", None))
        self.label_data_set_name.setText(QCoreApplication.translate("NemoMainWindow", u"No dataset loaded", None))
        self.label.setText(QCoreApplication.translate("NemoMainWindow", u"Modifiers :", None))
        self.pushButton_add_modifier.setText("")
        self.pushButton_delete_modifier.setText("")
        self.label_21.setText(QCoreApplication.translate("NemoMainWindow", u"Colormap :", None))
        self.label_8.setText(QCoreApplication.translate("NemoMainWindow", u"C min :", None))
        self.doubleSpinBox_nmo_c_min.setSuffix(QCoreApplication.translate("NemoMainWindow", u"mV", None))
        self.label_9.setText(QCoreApplication.translate("NemoMainWindow", u"C max :", None))
        self.doubleSpinBox_nmo_c_max.setSuffix(QCoreApplication.translate("NemoMainWindow", u"mV", None))
        self.label_22.setText(QCoreApplication.translate("NemoMainWindow", u"Time axis plot limits :", None))
        self.label_10.setText(QCoreApplication.translate("NemoMainWindow", u"t min :", None))
        self.doubleSpinBox_nmo_t_min.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.label_13.setText(QCoreApplication.translate("NemoMainWindow", u"t max :", None))
        self.doubleSpinBox_nmo_t_max.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.tabWidget_nmo.setTabText(self.tabWidget_nmo.indexOf(self.tab_nmo_plot), QCoreApplication.translate("NemoMainWindow", u"Plot", None))
        self.label_23.setText(QCoreApplication.translate("NemoMainWindow", u"Corrections:", None))
        self.label_24.setText(QCoreApplication.translate("NemoMainWindow", u"Source half-width :", None))
        self.doubleSpinBox_source_half_width_mm.setSuffix(QCoreApplication.translate("NemoMainWindow", u"mm", None))
        self.label_25.setText(QCoreApplication.translate("NemoMainWindow", u"Rise time :", None))
        self.doubleSpinBox_rise_time_us.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.tabWidget_nmo.setTabText(self.tabWidget_nmo.indexOf(self.tab_nmo_data), QCoreApplication.translate("NemoMainWindow", u"Data", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NemoMainWindow", u"Adjustable data boundaries :", None))
        self.checkBox_x_max.setText(QCoreApplication.translate("NemoMainWindow", u"x max", None))
        self.groupBox_box_mask.setTitle(QCoreApplication.translate("NemoMainWindow", u"Box mask :", None))
        self.label_14.setText(QCoreApplication.translate("NemoMainWindow", u"t lower :", None))
        self.doubleSpinBox_box_mask_t_lower.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.label_15.setText(QCoreApplication.translate("NemoMainWindow", u"t upper :", None))
        self.doubleSpinBox_box_mask_t_upper.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.label_16.setText(QCoreApplication.translate("NemoMainWindow", u"i lower :", None))
        self.label_17.setText(QCoreApplication.translate("NemoMainWindow", u"i upper :", None))
        self.groupBox.setTitle(QCoreApplication.translate("NemoMainWindow", u"Hover functions :", None))
        self.tabWidget_nmo.setTabText(self.tabWidget_nmo.indexOf(self.tab_nmo_tools), QCoreApplication.translate("NemoMainWindow", u"Tools", None))
        self.label_20.setText(QCoreApplication.translate("NemoMainWindow", u"Colormap :", None))
        self.label_11.setText(QCoreApplication.translate("NemoMainWindow", u"C min :", None))
        self.label_12.setText(QCoreApplication.translate("NemoMainWindow", u"C max :", None))
        self.tabWidget_tk.setTabText(self.tabWidget_tk.indexOf(self.tab_tk_plot), QCoreApplication.translate("NemoMainWindow", u"Plot", None))
        self.label_18.setText(QCoreApplication.translate("NemoMainWindow", u"Wave speed vector :", None))
        self.label_5.setText(QCoreApplication.translate("NemoMainWindow", u"v min :", None))
        self.doubleSpinBox_tk_v_min.setSuffix(QCoreApplication.translate("NemoMainWindow", u"ms\u207b\u00b9", None))
        self.label_6.setText(QCoreApplication.translate("NemoMainWindow", u"v max :", None))
        self.doubleSpinBox_tk_v_max.setSuffix(QCoreApplication.translate("NemoMainWindow", u"ms\u207b\u00b9", None))
        self.label_7.setText(QCoreApplication.translate("NemoMainWindow", u"n vs :", None))
        self.label_19.setText(QCoreApplication.translate("NemoMainWindow", u"t\u2080 vector :", None))
        self.label_2.setText(QCoreApplication.translate("NemoMainWindow", u"t\u2080 min :", None))
        self.doubleSpinBox_tk_t_0_min.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.label_3.setText(QCoreApplication.translate("NemoMainWindow", u"t\u2080 max :", None))
        self.doubleSpinBox_tk_t_0_max.setSuffix(QCoreApplication.translate("NemoMainWindow", u"\u03bcs", None))
        self.label_4.setText(QCoreApplication.translate("NemoMainWindow", u"n t\u2080s :", None))
        self.tabWidget_tk.setTabText(self.tabWidget_tk.indexOf(self.tab_tk_data), QCoreApplication.translate("NemoMainWindow", u"Data", None))
        self.pushButton_box_select.setText(QCoreApplication.translate("NemoMainWindow", u"Area zoom", None))
        self.pushButton_print_tk.setText(QCoreApplication.translate("NemoMainWindow", u"Print", None))
        self.tabWidget_tk.setTabText(self.tabWidget_tk.indexOf(self.tab_tk_tools), QCoreApplication.translate("NemoMainWindow", u"Tools", None))
    # retranslateUi

