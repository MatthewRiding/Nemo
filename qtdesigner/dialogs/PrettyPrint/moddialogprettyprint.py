from PySide6.QtWidgets import QDialog, QFileDialog, QHBoxLayout
from PySide6.QtGui import QIcon
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from qtdesigner.dialogs.PrettyPrint.UI_dialog_pretty_print import Ui_dialog_pretty_print
from classdefs.modqtmatplotlib import MplCanvasCopycat



class DialogPrettyPrint(QDialog, Ui_dialog_pretty_print):
    def __init__(self, parent=None, fig=None,
                 x_label_string=None,
                 y_label_string=None,
                 colorbar_string=None,
                 title_string=None,
                 fig_width=300,
                 fig_height=300):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.parent = parent

        # Display folder icon on browse button:
        self.pushButton_browse.setIcon(QIcon('graphicfiles/browse_folder.png'))

        # Present the figure provided on a new MplCanvasCopycat instance:
        self.mpl_canvas = MplCanvasCopycat(self.widget_size_controller, fig_to_copy=fig)
        self.mpl_canvas.axis_image = self.mpl_canvas.ax.get_images()[0]

        # Insert the new MplCanvas into a horizontal layout:
        hl = QHBoxLayout()
        hl.addWidget(self.mpl_canvas)
        self.widget_size_controller.setLayout(hl)

        # Get current widget size & display in SpinBoxes:
        width_default = fig_width
        height_default = fig_height
        self.spinBox_width.setValue(width_default)
        self.spinBox_height.setValue(height_default)
        self.new_size_requested()

        # Set pretty parameters:
        line_art_color = 'k'
        self.mpl_canvas.ax.spines[:].set_edgecolor(line_art_color)
        self.mpl_canvas.ax.xaxis.label.set_color(line_art_color)
        self.mpl_canvas.ax.yaxis.label.set_color(line_art_color)

        self.mpl_canvas.fig.patch.set_facecolor((1, 1, 1))
        self.mpl_canvas.fig.patch.set_alpha(1)

        # Change the font used for the figure:
        small_size = 8
        medium_size = 10
        bigger_size = 12
        self.mpl_canvas.ax.set_xlabel(x_label_string, fontsize=medium_size)
        self.mpl_canvas.ax.set_ylabel(y_label_string, fontsize=medium_size)

        self.mpl_canvas.ax.tick_params(color=line_art_color, labelcolor=line_art_color, labelsize=small_size)

        # Add a title to the TFM image plot using the TFM image name:
        _title_string = title_string if title_string else ''
        self.mpl_canvas.ax.set_title(_title_string, fontsize=bigger_size)

        if self.mpl_canvas.axis_image:
            # Add colorbar:
            #divider = make_axes_locatable(self.mpl_canvas.ax)
            #cax1 = divider.append_axes("right", size="5%", pad=0.2)
            self.cbar = self.mpl_canvas.fig.colorbar(self.mpl_canvas.axis_image, ax=self.mpl_canvas.ax)
            self.cbar.ax.tick_params(labelsize=small_size)
            self.cbar.set_label(colorbar_string, size=small_size)

        # Transmit provided strings to lineEdits:
        self.lineEdit_title.setText(_title_string)
        self.lineEdit_y_label.setText(y_label_string)

        # Wire signals to slots:
        self.pushButton_browse.clicked.connect(self.save_as_button_clicked)
        self.spinBox_width.editingFinished.connect(self.new_size_requested)
        self.spinBox_height.editingFinished.connect(self.new_size_requested)
        self.lineEdit_title.textEdited.connect(self.title_changed)
        self.lineEdit_y_label.textEdited.connect(self.y_label_changed)

    def title_changed(self):
        self.mpl_canvas.ax.set_title(self.lineEdit_title.text())
        self.mpl_canvas.draw()

    def y_label_changed(self):
        self.mpl_canvas.ax.set_ylabel(self.lineEdit_y_label.text())
        self.mpl_canvas.draw()

    def new_size_requested(self):
        # Resize the widget_size_controller using the new width:
        width = self.spinBox_width.value()
        height = self.spinBox_height.value()
        self.widget_size_controller.setFixedSize(width, height)

    def save_as_button_clicked(self):
        # Open a QFileDialog to get the path to the save location:
        file_path, file_filter = QFileDialog.getSaveFileName(parent=self.parent)

        # Print the figure, saving to the path specified in the lineEdit_save_path:
        self.mpl_canvas.fig.savefig(file_path, dpi=300, format='png')


class DialogPrettyPrintZoom(DialogPrettyPrint):
    def __init__(self, v_t_0_b_found_tuple=None, **kwargs):
        super().__init__(**kwargs)

        # This class will add a little text box onto the plot, showing the v, t_0 & b values (if given):
        if v_t_0_b_found_tuple:
            v_found_mpers, t_0_found_us, b_mm = v_t_0_b_found_tuple
            # Add text box:
            # String:
            text_string = (r'$c=$' + f'{v_found_mpers:.0f}' + r'$\mathregular{ms^{-1}}$' + '\n' +
                           r'$t_{0}=$' +  f'{t_0_found_us:.3f}' + 'μs' + '\n' +
                           r'$b=$' + f'{b_mm:.4f}' + 'mm')
            # Box patch properties:
            props = dict(boxstyle='round', facecolor='w', alpha=0.5, edgecolor='w')
            self.mpl_canvas.ax.annotate(text_string, xy=(0.5, 0.05), fontsize=8,
                                        xycoords='axes fraction', va='bottom', ha='center', bbox=props)
