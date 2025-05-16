from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
import numpy as np

from qtdesigner.tkzoomwidget.UI_tkzoomwidget import Ui_tk_zoom_widget
from functions.modextracttkcontributions import extract_tk_contributions
from qtdesigner.dialogs.PrettyPrint.moddialogprettyprint import DialogPrettyPrintZoom


class TKZoomWidget(QWidget, Ui_tk_zoom_widget):
    """A floating widget that displays a selected area of the main Taner-Koehler spectrum at high resolution."""

    # Define a signal to emit when this window is closed:
    tk_zoom_closed = Signal()
    # Define a signal to
    tk_zoom_hyperbola_found = Signal(tuple)

    def __init__(self, b_scan_amps, x_vector_mm, t_vector_us):
        super().__init__()
        self.setupUi(self)

        # Instance variables:
        self.b_scan_amps = b_scan_amps
        self.x_vector_mm = x_vector_mm
        self.t_vector_us = t_vector_us
        self.tk_spectrum_values_mv = None
        self.v_vector_mpers = None
        self.t_0_vector_us = None
        self.found_v_t_0_b_tuple = None
        self.i_min_x = None
        self.i_max_x = None

        # Set window title:
        self.setWindowTitle('T-K Zoom widget')
        # Set attributes:
        self.setAttribute(Qt.WA_DeleteOnClose)
        # Set window flags:
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Set default value for n_pixels per axis:
        self.spinBox_n_pixels_per_axis.setValue(300)

        # Add options to auto find combobox:
        list_of_auto_find_types = ['Min', 'Max']
        self.comboBox_find.addItems(list_of_auto_find_types)

        # Make an invisible plot to mark the 'autofind' result on the spectrum:
        self.plot_found_point, = self.tk_spectrum_widget.mpl_canvas.ax.plot(0, 0, marker='x', mec='w', ls='none',
                                                                           markersize=7, visible=False)

        # Wire signals to slots:
        self.groupBox_auto_find.toggled.connect(self.auto_find_toggled)
        self.comboBox_find.currentTextChanged.connect(self.auto_find_and_draw)
        self.pushButton_centre.clicked.connect(self.centre_clicked)
        self.pushButton_print.clicked.connect(self.print_clicked)

    def compute_new_spectrum_from_limits(self, v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us,
                                         boundary_i_min, boundary_i_max):
        # Compute new v & t_0 vectors:
        # Get n pixels per axis:
        n_pixels_per_axis = self.spinBox_n_pixels_per_axis.value()
        self.v_vector_mpers = np.linspace(v_min_mpers, v_max_mpers, n_pixels_per_axis)
        self.t_0_vector_us = np.linspace(t_0_min_us, t_0_max_us, n_pixels_per_axis)
        # Compute a new spectrum:
        spectrum_contributions_3d, query_times_3d = extract_tk_contributions(self.b_scan_amps,
                                                                             self.t_vector_us,
                                                                             self.x_vector_mm,
                                                                             self.v_vector_mpers,
                                                                             self.t_0_vector_us)
        # Sum over the specified x range:
        self.tk_spectrum_values_mv = np.sum(spectrum_contributions_3d[boundary_i_min:boundary_i_max], axis=0)

    def update_spectrum_plot_data(self, v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us):
        # Display the new spectrum:
        self.tk_spectrum_widget.axes_image.set_data(self.tk_spectrum_values_mv)
        self.tk_spectrum_widget.axes_image.set_extent((v_min_mpers, v_max_mpers, t_0_max_us, t_0_min_us))
        # Calculate colorbar limits:
        max_val = np.max(self.tk_spectrum_values_mv)
        min_val = np.min(self.tk_spectrum_values_mv)
        max_abs = np.max(np.abs([max_val, min_val]))
        self.tk_spectrum_widget.axes_image.set_clim(vmin=-max_abs, vmax=max_abs)

    def new_limits_from_rectangle(self, v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us,
                                  boundary_i_min, boundary_i_max):
        # Pin variables to self for access in other functions:
        self.i_min_x = boundary_i_min
        self.i_max_x = boundary_i_max

        # Compute new spectrum from limits:
        self.compute_new_spectrum_from_limits(v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us,
                                              boundary_i_min, boundary_i_max)

        # Display the new spectrum:
        self.update_spectrum_plot_data(v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us)

        # If auto find is checked, perform auto-find:
        if self.groupBox_auto_find.isChecked():
            self.perform_auto_find()

        # Draw:
        self.tk_spectrum_widget.mpl_canvas.draw()

    def closeEvent(self, event):
        self.tk_zoom_closed.emit()
        super().closeEvent(event)

    def perform_auto_find(self):
        # Execute find based on selected type:
        find_type = self.comboBox_find.currentText()
        if find_type == 'Max':
            # Find the indices of the maximum value in the spectrum array:
            flat_index = np.argmax(self.tk_spectrum_values_mv)
        elif find_type == 'Min':
            # Find the indices of the minimum value in the spectrum array:
            flat_index = np.argmin(self.tk_spectrum_values_mv)
        else:
            raise ValueError

        # Index into axis vectors to find v and t_0 corresponding to the found point:
        i_t_0, i_v = np.unravel_index(flat_index, np.shape(self.tk_spectrum_values_mv))
        t_0_found_us = self.t_0_vector_us[i_t_0]
        v_found_mpers = self.v_vector_mpers[i_v]
        # Calculate b:
        b_mm = (0.5 * t_0_found_us * 10**-6 * v_found_mpers) * 1000
        self.found_v_t_0_b_tuple = (v_found_mpers, t_0_found_us, b_mm)
        # Display found values in read-only spinboxes:
        self.doubleSpinBox_c.setValue(v_found_mpers)
        self.doubleSpinBox_t_0.setValue(t_0_found_us)
        self.doubleSpinBox_b.setValue(b_mm)

        # Mark the found point on the spectrum plot:
        self.plot_found_point.set_data([v_found_mpers], [t_0_found_us])
        self.plot_found_point.set_visible(True)

        # Emit the 'hyperbola_found' signal, transmitting the v and t_0 values found:
        self.tk_zoom_hyperbola_found.emit((v_found_mpers, t_0_found_us))

    def auto_find_and_draw(self):
        self.perform_auto_find()
        self.tk_spectrum_widget.mpl_canvas.draw()

    def auto_find_toggled(self, checked):
        if checked:
            self.auto_find_and_draw()
        else:
            self.plot_found_point.set_visible(False)
            self.tk_spectrum_widget.mpl_canvas.draw()
            self.doubleSpinBox_c.setValue(0)
            self.doubleSpinBox_t_0.setValue(0)
            self.doubleSpinBox_b.setValue(0)

    def centre_clicked(self):
        # Compute new limits around the found point:
        half_width_v_mpers = 500
        v_min_mpers = self.found_v_t_0_b_tuple[0] - half_width_v_mpers
        v_max_mpers = self.found_v_t_0_b_tuple[0] + half_width_v_mpers
        half_width_t_0_us = 0.11
        t_0_min_us = self.found_v_t_0_b_tuple[1] - half_width_t_0_us
        t_0_max_us = self.found_v_t_0_b_tuple[1] + half_width_t_0_us

        # Compute new spectrum:
        self.compute_new_spectrum_from_limits(v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us,
                                              self.i_min_x, self.i_max_x)

        # Send new spectrum data to plot:
        self.update_spectrum_plot_data(v_min_mpers, v_max_mpers, t_0_min_us, t_0_max_us)

        # Re-draw spectrum plot:
        self.tk_spectrum_widget.mpl_canvas.draw()

    def print_clicked(self):
        # Launch an instance of the PrettyPrint dialog:
        if self.groupBox_auto_find.isChecked():
            v_t_0_b_found_tuple = self.found_v_t_0_b_tuple
        else:
            v_t_0_b_found_tuple = None

        dialog_pretty_print = DialogPrettyPrintZoom(v_t_0_b_found_tuple,
                                                    parent=self,
                                                    fig=self.tk_spectrum_widget.mpl_canvas.fig,
                                                    x_label_string=r'Wave speed $c$ ($\mathregular{ms^{-1}}$)',
                                                    y_label_string='$t_{0}$ (μs)',
                                                    colorbar_string='Sum (mV)',
                                                    title_string=None,
                                                    fig_height=200)
        dialog_pretty_print.exec()
