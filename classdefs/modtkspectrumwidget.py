from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Signal
import colorcet as cc
import numpy as np
from matplotlib.transforms import blended_transform_factory

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager


class TKSpectrumBase(QWidget):
    # Define custom signals:
    pixel_clicked = Signal(tuple)

    def __init__(self, parent):
        super().__init__(parent)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(parent=self, width=4, height=2, dpi=100)

        # Set style elements:
        my_grey = '0.3'
        self.fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel(r'Wave speed $c$ ($\mathregular{ms^{-1}}$)', fontsize=self.fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('$t_{0}$ (μs)', fontsize=self.fontsize_labels)
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

        # A plot with a marker to mark the selected [v, t_0] point:
        self.marker_selected, = self.mpl_canvas.ax.plot([], [], visible=False, marker='x',
                                                        markeredgecolor=[0, 1, 0, 0.8])

        # Store the v_vector_mpers as an instance variable for use in computing the iso-b line:
        self.v_vector_mpers = None

        # Implement matplotlib figure event handling to enable pixel selection:
        # Connect to the 'button_press_event':
        self.mpl_canvas.fig.canvas.mpl_connect('button_press_event', self.button_press_response)

        self.blit_manager = None

    def button_press_response(self, event):
        # Implement different responses depending on whether the left or right mouse button was clicked:
        if event.button == 1:
            # Matplotlib MouseButton Enum, 1 = LEFT mouse button:
            # Move the selected pixel marker to the location that has been clicked:
            self.marker_selected.set_data([event.xdata], [event.ydata])
            # If invisible, make visible:
            if not self.marker_selected.get_visible():
                self.marker_selected.set_visible(True)

            # Get the selected values of wave speed (c) and normal incidence time (t_0):
            tuple_c_t_0 = (event.xdata, event.ydata)

        else:
            # Either the right or middle mouse buttons were clicked.
            # Make the marker invisible:
            self.marker_selected.set_visible(False)
            # Transmit None as the tuple in the 'pixel_clicked' signal:
            tuple_c_t_0 = None

        # Emit the 'pixel_clicked' event to prompt the B-scan and iso-t widgets to display the associated delay law
        # (if left mouse button) or else make the selected hyperbola disappear:
        self.pixel_clicked.emit(tuple_c_t_0)

        # Blit changes:
        self.blit_manager.blit_all_animated_artists()


class TKSpectrumWidget(TKSpectrumBase):
    """
    Class for use in the mainWindow of Nemo.
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Add a label for the title:
        self.label_title = QLabel('  T-K plot  ')
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

        # Plot an invisible line that will be updated to display the iso-b contour the mouse is hovering over:
        self.line_iso_b, = self.mpl_canvas.ax.plot([], [], visible=False, color='aqua', linewidth=0.5)

        # Use blended transforms for the text annotations, to specify one co-ordinate in normalised axes units,
        # and the other in data units:
        trans_x_data_y_norm = blended_transform_factory(self.mpl_canvas.ax.transData,
                                                        self.mpl_canvas.ax.transAxes)
        trans_x_norm_y_data = blended_transform_factory(self.mpl_canvas.ax.transAxes,
                                                        self.mpl_canvas.ax.transData)

        # A text object to write the b-value:
        self.text_iso_b = self.mpl_canvas.ax.text(1, [], '', color='aqua', fontsize=self.fontsize_labels,
                                                  visible=False, va='bottom', ha='right',
                                                  transform=trans_x_norm_y_data)
        # A text object to write the v-value hovered over:
        self.text_v_hover = self.mpl_canvas.ax.text([], 1, '', color='w', fontsize=self.fontsize_labels,
                                                    visible=False, va='top', ha='right',
                                                    transform=trans_x_data_y_norm)
        # A text object to write the t_0-value hovered over:
        self.text_t_0_hover = self.mpl_canvas.ax.text(0, [], '', color='w', fontsize=self.fontsize_labels,
                                                      visible=False, va='bottom', ha='left',
                                                      transform=trans_x_norm_y_data)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.line_iso_b,
                                                          self.text_iso_b,
                                                          self.text_v_hover,
                                                          self.text_t_0_hover,
                                                          self.marker_selected])

    def new_v_vector_mpers(self, v_vector_mpers):
        self.v_vector_mpers = v_vector_mpers
        # Use v_vector as x-values for the iso-b line plot:
        self.line_iso_b.set_xdata(v_vector_mpers)
        # Use v_max as the x-location for the b_hover text annotation:
        # self.text_iso_b.set_x(v_vector_mpers[-1])
        # Use v_min as the x_location for the t_0 hover text annotation:
        # self.text_t_0_hover.set_x(v_vector_mpers[0])

    def set_hover_annotations_visible(self, visible):
        self.line_iso_b.set_visible(visible)
        self.text_iso_b.set_visible(visible)
        self.text_v_hover.set_visible(visible)
        self.text_t_0_hover.set_visible(visible)

    def update_hover_annotations(self, v_hover_mpers, t_0_hover_us):
        # Update iso-b line on TK spectrum:
        # Compute b:
        b_hover_mm = 10 ** 3 * 0.5 * t_0_hover_us * 10 ** -6 * v_hover_mpers
        # Compute t_0 values for this b value:
        t_0s_iso_b_line_us = 10 ** 6 * 2 * b_hover_mm * 10 ** -3 / self.v_vector_mpers
        # Set ydata for iso-b line:
        self.line_iso_b.set_ydata(t_0s_iso_b_line_us)

        # Update b text:
        self.text_iso_b.set_text(r'$b=$' + f'{b_hover_mm:.2f}mm')
        self.text_iso_b.set_y(t_0s_iso_b_line_us[-1])

        # Update v text:
        self.text_v_hover.set_text(r'$c=$' + f'{v_hover_mpers:.1f}ms' + r'$^{-1}$')
        self.text_v_hover.set_x(v_hover_mpers)

        # Update t_0 text:
        self.text_t_0_hover.set_text(r'$t_0=$' + f'{t_0_hover_us:.4f}μs')
        self.text_t_0_hover.set_y(t_0_hover_us)


class TKSpectrumZoom(TKSpectrumBase):
    """
    Class for use in the TK Zoom floating widget that can be instantiated from Nemo.
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Set MplWidget into a layout and assign to self:
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mpl_canvas)
        self.setLayout(layout)
