from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal, Qt
import numpy as np
import colorcet as cc

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager
from classdefs.modmytoolbar import MyToolBar


class PCVViewer(QWidget):
    """
    A widget for viewing pixel contribution vectors (PCVs) for pixels selected by the user in the TK spectrum widget.
    A PCV is the 1D array of displacement values that are obtained by sampling each A-scan along the NMO hyperbola
    defined by the selected value of (v, t_0).  The displacement values in the PCV are summed to produce the hyperbola
    'score' displayed at the corresponding pixel in the Taner-Koehler spectrum. This viewer enables the set of sampled
    displacements contributing to the score at a chosen pixel to be visualised, to highlight trends, anomalous values,
    and ultimately help explain the contrast observed between different pixels in the TK spectrum.
    """

    # Create a closed signal as class attribute:
    pcv_viewer_closed = Signal()

    def __init__(self, n_a_scans=2, v_min=None, v_max=None, pcv_nm=None):
        super().__init__()

        # Set window title:
        self.setWindowTitle('PCV viewer')

        # Set attributes:
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Set window flags:
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Create an MplCanvas instance:
        self.mpl_canvas = MplCanvas()

        # Create a matplotlib toolbar to enable zooming:
        self.toolbar = MyToolBar(self.mpl_canvas, self)

        # Create a button to auto-scale the y-axis:
        self.button_autoscale_y = QPushButton('Autoscale y axis')

        # Stack the widgets into a vertical layout:
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.mpl_canvas)
        self.layout.addWidget(self.button_autoscale_y)
        self.setLayout(self.layout)

        # Customise the default 2D axis instance:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('A-scan index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Displacement (nm)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.axhline(0, color=my_grey, lw=1)

        if pcv_nm is None:
            # We have no PCV to plot.
            # Create a vector of n_elements zeros and make it invisible:
            pcv_nm = np.zeros(n_a_scans)
            visible = False
        else:
            visible = True

        # Create the PCV scatter plot which will be updated in the future:
        self.a_scan_indices = range(n_a_scans)
        self.scatter_pcv = self.mpl_canvas.ax.scatter(self.a_scan_indices, pcv_nm, c=pcv_nm, visible=visible,
                                                      marker='o', s=20, cmap=cc.m_CET_D7, vmin=v_min, vmax=v_max,
                                                      edgecolors='none')

        # Set axis limits:
        self.mpl_canvas.ax.set_xlim(0, n_a_scans - 1)

        # Set widget size:
        self.resize(600, 600)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.scatter_pcv])

        # Wire signals to slot:
        self.button_autoscale_y.pressed.connect(self.auto_scale_y)

    def update_pcv_values(self, pcv_nm):
        # Transmit the new pixel contributions vector as the y-data for the 2d line plot:
        # The existing scatter plot takes data in the form of 'offsets', an array of shape (n_points, 2) where the
        # x-values form the first column and y-values form the second column.
        offsets = np.transpose(np.vstack((self.a_scan_indices, pcv_nm)))
        self.scatter_pcv.set_offsets(offsets)
        # Set the colors of the sampling points:
        self.scatter_pcv.set_array(pcv_nm)
        # If not already visible, make the scatter plot visible:
        if not self.scatter_pcv.get_visible():
            self.scatter_pcv.set_visible(True)
        # Blit changes:
        self.blit_manager.blit_all_animated_artists()

    def update_color_limits(self, v_min_nm, v_max_nm):
        self.scatter_pcv.set_clim(v_min_nm, v_max_nm)
        # Blit changes:
        self.blit_manager.blit_all_animated_artists()

    def update_n_a_scans(self, n_a_scans):
        # This only affects the instance variable a_scan_indices:
        self.a_scan_indices = range(n_a_scans)

    def closeEvent(self, event):
        self.pcv_viewer_closed.emit()
        super().closeEvent(event)

    def auto_scale_y(self):
        # Get max of absolute value of PCV displacements:
        offsets = self.scatter_pcv.get_offsets()
        max_abs_nm = np.max(np.abs(offsets[:, 1]))
        # Set max abs as positive and negative y-axis limits:
        self.mpl_canvas.ax.set_ylim(-max_abs_nm, max_abs_nm)
        # Re-draw canvas:
        self.mpl_canvas.draw()

