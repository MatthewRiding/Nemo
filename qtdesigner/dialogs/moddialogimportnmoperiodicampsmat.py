from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QIcon

from qtdesigner.dialogs.UI_dialog_import_nmo_periodic_amps import Ui_dialog_nmo_mat


class DialogImportNMOPeriodicMat(QDialog, Ui_dialog_nmo_mat):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.parent_main_window = parent
        self.name_string = None
        self.file_path = None
        self.t_min_us = None
        self.t_max_us = None
        self.pitch_mm = None

        # Display folder icon on browse button:
        self.push_button_browse_for_file.setIcon(QIcon('graphicfiles/browse_folder.png'))

        # Wire signals to slots:
        self.push_button_browse_for_file.clicked.connect(self.browse_for_file)
        self.buttonBox.accepted.connect(self.accept_button_clicked)

    def browse_for_file(self):
        # Open a QFileDialog to get the path to the .mat file:
        file_path, file_filter = QFileDialog.getOpenFileName(parent=self.parent_main_window, filter='mat files (*.mat)')

        # After closure of the file dialog, display the file path in the line edit:
        self.lineEdit_file_path.setText(file_path)

    def accept_button_clicked(self):
        # Take the description, file path and time limits entered by the user and save them to the instance as
        # instance variables:
        self.name_string = self.line_edit_name.text()
        self.file_path = self.lineEdit_file_path.text()
        self.t_min_us = self.doubleSpinBox_time_min_us.value()
        self.t_max_us = self.doubleSpinBox_time_max_us.value()
        self.pitch_mm = self.doubleSpinBox_pitch_mm.value()
