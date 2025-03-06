# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_import_nmo_periodic_amps_mat.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_dialog_nmo_mat(object):
    def setupUi(self, dialog_nmo_mat):
        if not dialog_nmo_mat.objectName():
            dialog_nmo_mat.setObjectName(u"dialog_nmo_mat")
        dialog_nmo_mat.resize(487, 254)
        self.verticalLayout = QVBoxLayout(dialog_nmo_mat)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_tfm_parameters = QLabel(dialog_nmo_mat)
        self.label_tfm_parameters.setObjectName(u"label_tfm_parameters")
        self.label_tfm_parameters.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_tfm_parameters.setFont(font)

        self.verticalLayout.addWidget(self.label_tfm_parameters)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(dialog_nmo_mat)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.line_edit_name = QLineEdit(dialog_nmo_mat)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_name)

        self.label_2 = QLabel(dialog_nmo_mat)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_file_path = QLineEdit(dialog_nmo_mat)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_file_path)

        self.push_button_browse_for_file = QPushButton(dialog_nmo_mat)
        self.push_button_browse_for_file.setObjectName(u"push_button_browse_for_file")
        self.push_button_browse_for_file.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_2.addWidget(self.push_button_browse_for_file)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.groupBox = QGroupBox(dialog_nmo_mat)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.doubleSpinBox_time_min_us = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_time_min_us.setObjectName(u"doubleSpinBox_time_min_us")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_time_min_us.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_time_min_us.setSizePolicy(sizePolicy)
        self.doubleSpinBox_time_min_us.setFont(font2)
        self.doubleSpinBox_time_min_us.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_time_min_us.setDecimals(3)
        self.doubleSpinBox_time_min_us.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_time_min_us.setMaximum(1000.000000000000000)
        self.doubleSpinBox_time_min_us.setSingleStep(0.000000000000000)
        self.doubleSpinBox_time_min_us.setValue(-0.250000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_time_min_us, 0, 1, 1, 1)

        self.doubleSpinBox_time_max_us = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_time_max_us.setObjectName(u"doubleSpinBox_time_max_us")
        self.doubleSpinBox_time_max_us.setFont(font2)
        self.doubleSpinBox_time_max_us.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_time_max_us.setDecimals(3)
        self.doubleSpinBox_time_max_us.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_time_max_us.setMaximum(1000.000000000000000)
        self.doubleSpinBox_time_max_us.setValue(4.750000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_time_max_us, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(dialog_nmo_mat)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.doubleSpinBox_pitch_mm = QDoubleSpinBox(dialog_nmo_mat)
        self.doubleSpinBox_pitch_mm.setObjectName(u"doubleSpinBox_pitch_mm")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_pitch_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_pitch_mm.setSizePolicy(sizePolicy)
        self.doubleSpinBox_pitch_mm.setDecimals(4)
        self.doubleSpinBox_pitch_mm.setSingleStep(0.010000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_pitch_mm)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(dialog_nmo_mat)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dialog_nmo_mat)
        self.buttonBox.accepted.connect(dialog_nmo_mat.accept)
        self.buttonBox.rejected.connect(dialog_nmo_mat.reject)

        QMetaObject.connectSlotsByName(dialog_nmo_mat)
    # setupUi

    def retranslateUi(self, dialog_nmo_mat):
        dialog_nmo_mat.setWindowTitle(QCoreApplication.translate("dialog_nmo_mat", u"Dialog", None))
        self.label_tfm_parameters.setText(QCoreApplication.translate("dialog_nmo_mat", u"Import NMO periodic amplitude array from .mat 2D array format :", None))
        self.label.setText(QCoreApplication.translate("dialog_nmo_mat", u"Data set name :", None))
        self.label_2.setText(QCoreApplication.translate("dialog_nmo_mat", u"File path :", None))
        self.push_button_browse_for_file.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("dialog_nmo_mat", u"Time record :", None))
        self.label_3.setText(QCoreApplication.translate("dialog_nmo_mat", u"t min :", None))
        self.doubleSpinBox_time_min_us.setSuffix(QCoreApplication.translate("dialog_nmo_mat", u"\u03bcs", None))
        self.doubleSpinBox_time_max_us.setSuffix(QCoreApplication.translate("dialog_nmo_mat", u"\u03bcs", None))
        self.label_4.setText(QCoreApplication.translate("dialog_nmo_mat", u"t max :", None))
        self.label_5.setText(QCoreApplication.translate("dialog_nmo_mat", u"Pitch :", None))
        self.doubleSpinBox_pitch_mm.setSuffix(QCoreApplication.translate("dialog_nmo_mat", u"mm", None))
    # retranslateUi

