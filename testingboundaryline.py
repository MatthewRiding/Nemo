from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QApplication
import sys
import numpy as np

from classdefs.modboundaryline import BoundaryLine
from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager
from classdefs.modcursormanager import CursorManager


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add a Matplotlib canvas:
        self.mpl_canvas = MplCanvas()

        # Create an instance of the BlitManager class to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [])

        # Manage mouse cursor:
        self.cursor_manager = CursorManager(self.mpl_canvas)

        # Create a horizontal layout:
        h_layout = QHBoxLayout()
        # Add the Mpl canvas:
        h_layout.addWidget(self.mpl_canvas)

        # Create a widget to hold the layout:
        widget = QWidget()
        widget.setLayout(h_layout)

        self.setCentralWidget(widget)

        # Plot a line on the canvas:
        # x = [1, 2, 3, 4, 5]
        # y = [2, 6, 1, 7, 3]
        # self.mpl_canvas.ax.plot(x, y, color=[1, 0, 1])
        # # Invert y axis:
        # self.mpl_canvas.ax.invert_yaxis()

        # Plot an image on the canvas:
        data = np.eye(10, 10, 4)
        self.mpl_canvas.ax.imshow(data)

        # Create a BoundaryLine on the MplCanvas:
        self.mpl_canvas.ax.autoscale(enable=False)
        self.bl_2 = BoundaryLine(self.mpl_canvas, 'y', 'min', self.blit_manager, self.cursor_manager)
        #self.bl_1 = BoundaryLine(self.mpl_canvas, 'y', 'max', self.blit_manager)

        # Respond to signals:
        #self.bl_1.boundary_moved.connect(self.bl_1_moved)
        self.bl_2.boundary_moved.connect(self.bl_2_moved)

    def bl_1_moved(self, value):
        print(f'Boundary 1 moved to {value}')

    def bl_2_moved(self, value):
        print(f'Boundary 2 moved to {value}')

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MyMainWindow()
window.show()
app.exec()