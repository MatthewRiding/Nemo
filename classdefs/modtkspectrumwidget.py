from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame, QVBoxLayout
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import colorcet as cc
import numpy as np

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager


class TKSpectrumWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(parent=self, width=4, height=2, dpi=100)

        # Create the interactive matplotlib toolbar, passing the MplCanvas as the first parameter, then the parent (
        # self, the QWidget) as the second parameter:
        toolbar = NavigationToolbar(self.mpl_canvas, self)

        # Add the toolbar to a horizontal layout with a label to describe the plot:
        layout_title_and_tools = QHBoxLayout()
        layout_title_and_tools.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel('  T-K spectrum  ')
        self.label_title.setStyleSheet("font: 14pt Segoe UI")
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        layout_title_and_tools.addWidget(self.label_title)
        layout_title_and_tools.addWidget(v_line)
        layout_title_and_tools.addWidget(toolbar)

        # Stack the h layout and the MplCanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(layout_title_and_tools)
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
        self.mpl_canvas.ax.set_xlabel(r'Wave speed ($\mathregular{ms^{-1}}$)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('$t_{0}$ (μs)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)

        # Plot an image of zeros to update later:
        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([10, 10])
            c_map = cc.m_CET_D7
            axes_image = self.mpl_canvas.ax.imshow(data_array, cmap=c_map, interpolation='nearest', aspect='auto',
                                                   **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Plot an invisible line that will be updated to display the iso-b contour the mouse is hovering over:
        self.line_iso_b, = self.mpl_canvas.ax.plot([], [], visible=False, color='aqua', linewidth=0.5)

        # A text object to write the b-value:
        self.text_iso_b = self.mpl_canvas.ax.text([], [], '', color='aqua', fontsize=fontsize_labels, visible=False,
                                                  va='bottom', ha='right')

        # A plot with a marker to mark the selected [v,b] point:
        # self.marker_selected_vb, = self.mpl_canvas.ax.plot([], [], visible=False, marker='+',
        #                                                    markeredgecolor=[1, 1, 1, 0.8])

        # Implement matplotlib figure event handling to enable pixel selection:
        # Connect the method 'motion_hover' to the 'motion_notify_event' in the MatPlotLib event handler:
        # self.mpl_canvas.fig.canvas.mpl_connect('motion_notify_event', self.motion_hover)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.line_iso_b,
                                                          self.text_iso_b])
