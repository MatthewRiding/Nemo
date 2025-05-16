from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
import colorcet as cc
import numpy as np


from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager
from classdefs.modcursormanager import CursorManager


class NMOBScanWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(parent=self, width=4, height=2, dpi=100)

        # Create the interactive matplotlib toolbar, passing the MplCanvas as the first parameter, then the parent (
        # # self, the QWidget) as the second parameter:
        # toolbar = NavigationToolbar(self.mpl_canvas, self)

        # Add a label for the title:
        self.label_title = QLabel('  NMO B-scan  ')
        self.label_title.setStyleSheet("font: 14pt Segoe UI")
        self.label_title.setSizePolicy(QSizePolicy.Policy.Expanding,
                                       QSizePolicy.Policy.Maximum)

        # Stack the title label and the MplCanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label_title)
        layout.addWidget(self.mpl_canvas)
        self.setLayout(layout)

        # Set style elements:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Off-set (mm)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Time (μs)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.autoscale(enable=False, axis='both', tight=True)

        # Plot an image of zeros to update later:
        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([10, 10])
            c_map = cc.m_CET_D7
            axes_image = self.mpl_canvas.ax.imshow(data_array, cmap=c_map, interpolation='nearest', aspect='auto',
                                                   **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Plot an invisible line that will be updated to display the hyperbola selected in the T-K spectrum plot:
        self.hyperbola_hover, = self.mpl_canvas.ax.plot([], [], visible=False, color=[1, 1, 1, 1], linewidth=0.6,
                                                        dashes=(5, 4))
        # self.hyperbola_click, = self.mpl_canvas.ax.plot([], [], visible=False, color=[1, 1, 1, 1], linewidth=0.6)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.hyperbola_hover])

        # Create a CursorManager instance to manage cursor transformations:
        self.cursor_manager = CursorManager(self.mpl_canvas)

    def new_amplitude_array(self, amplitudes_2d_array):
        # Set amplitudes as new data for imshow image:
        self.axes_image.set_data(amplitudes_2d_array)
