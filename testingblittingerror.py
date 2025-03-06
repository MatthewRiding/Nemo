import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, layout="constrained")
        self.ax = self.fig.add_subplot(1, 1, 1)
        super(MplCanvas, self).__init__(self.fig)

        self.setParent(parent)


class BlitManager:
    def __init__(self, canvas, animated_artists=()):
        """
        Parameters
        ----------
        canvas : FigureCanvasAgg
            The canvas to work with, this only works for subclasses of the Agg
            canvas which have the `~FigureCanvasAgg.copy_from_bbox` and
            `~FigureCanvasAgg.restore_region` methods.

        animated_artists : Iterable[Artist]
            List of the artists to manage
        """
        self.canvas = canvas
        self._bg = None
        self._artists = []

        for a in animated_artists:
            self.add_artist(a)
        # grab the background on every draw
        self.cid = canvas.mpl_connect("draw_event", self.on_draw)

    def on_draw(self, event):
        """Callback to register with 'draw_event'."""
        cv = self.canvas
        if event is not None:
            if event.canvas != cv:
                raise RuntimeError
        self._bg = cv.copy_from_bbox(cv.figure.bbox)
        self._draw_animated()

    def add_artist(self, art):
        """
        Add an artist to be managed.

        Parameters
        ----------
        art : Artist

            The artist to be added.  Will be set to 'animated' (just
            to be safe).  *art* must be in the figure associated with
            the canvas this class is managing.

        """
        if art.figure != self.canvas.figure:
            raise RuntimeError
        art.set_animated(True)
        self._artists.append(art)

    def _draw_animated(self):
        """Draw all of the animated artists."""
        fig = self.canvas.figure
        for a in self._artists:
            fig.draw_artist(a)

    def update(self):
        """Update the screen with animated artists."""
        cv = self.canvas
        fig = cv.figure
        # paranoia in case we missed the draw event,
        if self._bg is None:
            self.on_draw(None)
        else:
            # restore the background
            cv.restore_region(self._bg)
            # draw all of the animated artists
            self._draw_animated()
            # update the GUI state
            cv.blit(fig.bbox)
        # let the GUI event loop process anything it has to do
        #cv.flush_events()


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add two instances of a Matplotlib canvas:
        mpl_canvas_1 = MplCanvas()
        mpl_canvas_2 = MplCanvas()

        # Label the plots:
        mpl_canvas_1.ax.set_title('Canvas 1')
        mpl_canvas_2.ax.set_title('Canvas 2')

        # On each canvas, create a line plot with fixed x data and y data initially set to all zeros:
        n_points = 3
        self.x_data = np.linspace(0, 100, n_points)
        y_data_initial = np.zeros(n_points)
        self.line1, = mpl_canvas_1.ax.plot(self.x_data, y_data_initial)
        self.line2, = mpl_canvas_2.ax.plot(self.x_data, y_data_initial)
        
        # Adjust the axes limits:
        mpl_canvas_1.ax.set_xlim(0, 100)
        mpl_canvas_1.ax.set_ylim(0, 100)
        mpl_canvas_2.ax.set_xlim(0, 100)
        mpl_canvas_2.ax.set_ylim(0, 100)

        # For each canvas, create an instance of the BlitManager class to manage blitting:
        self.blit_manager_1 = BlitManager(mpl_canvas_1, [self.line1])
        self.blit_manager_2 = BlitManager(mpl_canvas_2, [self.line2])

        # Create a horizontal layout:
        h_layout = QHBoxLayout()
        # Add the Mpl canvases:
        h_layout.addWidget(mpl_canvas_1)
        h_layout.addWidget(mpl_canvas_2)

        # Create a widget to hold the layout:
        widget = QWidget()
        widget.setLayout(h_layout)

        self.setCentralWidget(widget)

        # Connect the matplotlib 'motion_notify_event' to the canvas_mouse_hover method:
        mpl_canvas_1.fig.canvas.mpl_connect('motion_notify_event', self.mouse_moved_in_canvas)

    def mouse_moved_in_canvas(self, event):
        if event.inaxes:
            # Mouse is in data axes.
            # Get data co-ordinates of cursor:
            x_hover = event.xdata
            y_hover = event.ydata

            # Draw line passing through zero and hover point:
            # Compute y values for fixed x vector:
            gradient = y_hover / x_hover
            y_vector = gradient * self.x_data

            # Set ydata for lines:
            self.line1.set_ydata(y_vector)
            self.line2.set_ydata(y_vector)

            # Blit changes:
            self.blit_manager_1.update()
            self.blit_manager_2.update()


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MyMainWindow()
window.show()
app.exec()
