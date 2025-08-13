# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tkzoomwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

from classdefs.modtkspectrumwidget import TKSpectrumZoom

class Ui_tk_zoom_widget(object):
    def setupUi(self, tk_zoom_widget):
        if not tk_zoom_widget.objectName():
            tk_zoom_widget.setObjectName(u"tk_zoom_widget")
        tk_zoom_widget.resize(519, 737)
        self.verticalLayout_4 = QVBoxLayout(tk_zoom_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tk_spectrum_widget = TKSpectrumZoom(tk_zoom_widget)
        self.tk_spectrum_widget.setObjectName(u"tk_spectrum_widget")

        self.verticalLayout_4.addWidget(self.tk_spectrum_widget)

        self.tabWidget = QTabWidget(tk_zoom_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 475, 233))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.spinBox_n_pixels_per_axis = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_n_pixels_per_axis.setObjectName(u"spinBox_n_pixels_per_axis")
        self.spinBox_n_pixels_per_axis.setMinimum(1)
        self.spinBox_n_pixels_per_axis.setMaximum(1000)

        self.horizontalLayout_7.addWidget(self.spinBox_n_pixels_per_axis)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_8.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 458, 238))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_auto_find = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_auto_find.setObjectName(u"groupBox_auto_find")
        font = QFont()
        font.setBold(True)
        self.groupBox_auto_find.setFont(font)
        self.groupBox_auto_find.setCheckable(True)
        self.groupBox_auto_find.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_auto_find)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_auto_find)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox_find = QComboBox(self.groupBox_auto_find)
        self.comboBox_find.setObjectName(u"comboBox_find")
        self.comboBox_find.setMinimumSize(QSize(100, 0))
        self.comboBox_find.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_find)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_auto_find)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.doubleSpinBox_c = QDoubleSpinBox(self.groupBox_auto_find)
        self.doubleSpinBox_c.setObjectName(u"doubleSpinBox_c")
        self.doubleSpinBox_c.setFont(font1)
        self.doubleSpinBox_c.setReadOnly(True)
        self.doubleSpinBox_c.setMaximum(100000.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_c)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_auto_find)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.doubleSpinBox_t_0 = QDoubleSpinBox(self.groupBox_auto_find)
        self.doubleSpinBox_t_0.setObjectName(u"doubleSpinBox_t_0")
        self.doubleSpinBox_t_0.setFont(font1)
        self.doubleSpinBox_t_0.setReadOnly(True)
        self.doubleSpinBox_t_0.setDecimals(4)
        self.doubleSpinBox_t_0.setMaximum(10000.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_t_0)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_auto_find)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.doubleSpinBox_b = QDoubleSpinBox(self.groupBox_auto_find)
        self.doubleSpinBox_b.setObjectName(u"doubleSpinBox_b")
        self.doubleSpinBox_b.setFont(font1)
        self.doubleSpinBox_b.setReadOnly(True)
        self.doubleSpinBox_b.setDecimals(4)
        self.doubleSpinBox_b.setMaximum(10000.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_b)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.pushButton_centre = QPushButton(self.groupBox_auto_find)
        self.pushButton_centre.setObjectName(u"pushButton_centre")
        self.pushButton_centre.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_centre)


        self.verticalLayout.addWidget(self.groupBox_auto_find)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_print = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_print.setObjectName(u"pushButton_print")

        self.horizontalLayout_2.addWidget(self.pushButton_print)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(tk_zoom_widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(tk_zoom_widget)
    # setupUi

    def retranslateUi(self, tk_zoom_widget):
        tk_zoom_widget.setWindowTitle(QCoreApplication.translate("tk_zoom_widget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("tk_zoom_widget", u"n pixels per axis :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("tk_zoom_widget", u"Data", None))
        self.groupBox_auto_find.setTitle(QCoreApplication.translate("tk_zoom_widget", u"Auto find", None))
        self.label.setText(QCoreApplication.translate("tk_zoom_widget", u"Find :", None))
        self.label_2.setText(QCoreApplication.translate("tk_zoom_widget", u"<html><head/><body><p>Wave speed <span style=\" font-style:italic;\">c </span>:</p></body></html>", None))
        self.doubleSpinBox_c.setSuffix(QCoreApplication.translate("tk_zoom_widget", u" m/s", None))
        self.label_3.setText(QCoreApplication.translate("tk_zoom_widget", u"<html><head/><body><p>Normal incidence time <span style=\" font-style:italic;\">t</span><span style=\" vertical-align:sub;\">0</span> :</p></body></html>", None))
        self.doubleSpinBox_t_0.setSuffix(QCoreApplication.translate("tk_zoom_widget", u" \u03bcs", None))
        self.label_4.setText(QCoreApplication.translate("tk_zoom_widget", u"<html><head/><body><p>Thickness<span style=\" font-style:italic;\"> b</span> (1/2 <span style=\" font-style:italic;\">t</span><span style=\" vertical-align:sub;\">0</span><span style=\" font-style:italic;\">c</span>) :</p></body></html>", None))
        self.doubleSpinBox_b.setSuffix(QCoreApplication.translate("tk_zoom_widget", u" mm", None))
        self.pushButton_centre.setText(QCoreApplication.translate("tk_zoom_widget", u"Centre", None))
        self.pushButton_print.setText(QCoreApplication.translate("tk_zoom_widget", u"Print", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("tk_zoom_widget", u"Tools", None))
    # retranslateUi

