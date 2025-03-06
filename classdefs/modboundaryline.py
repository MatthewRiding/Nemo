from matplotlib.backend_tools import Cursors
from matplotlib.patches import Rectangle
from PySide6.QtCore import Signal, QObject

class BoundaryLine(QObject):
    # Define a custom signal to be emitted when the boundary is moved:
    boundary_moved = Signal(float)

    def __init__(self, mpl_canvas, axis, min_or_max, blit_manager, cursor_manager):
        super().__init__()

        # Initialise instance variables:
        self.mpl_canvas = mpl_canvas
        self.blit_manager = blit_manager
        self.cursor_manager = cursor_manager
        self.stuck_to_mouse = False
        self.rect = None
        self.mouse_above_handle = False

        # Create an axvline or axhline instance to visually appear as the boundary line:
        # Also create a plot that will contain one point in the middle of the line to use as a 'handle' for dragging the
        # line.
        color_boundary = [0.4, 0.4, 0.4]
        dict_line_params = {'color': color_boundary,
                            'linestyle': '-',
                            'linewidth': 2}
        dict_marker_params = {'markerfacecolor': color_boundary,
                              'markeredgecolor': 'none',
                              'markersize': 7,
                              'picker': True,
                              'pickradius': 5}
        dict_rect_params = {'facecolor': color_boundary,
                            'alpha': 0.5}

        # Get axis limits:
        y_bottom, y_top = mpl_canvas.ax.get_ylim()
        x_left, x_right = mpl_canvas.ax.get_xlim()
        x_range = x_right - x_left
        y_range = y_bottom - y_top

        # Set rectangle anchor coords to None initially:
        x_anchor = None
        y_anchor = None

        # Set parameters depending on whether axis is 'x' or 'y':
        if axis == 'x':
            # Line:
            self.line = mpl_canvas.ax.axvline(x=0, **dict_line_params)
            # Handle point:
            y_handle = y_top + (y_range / 2)
            self.handle_point, = mpl_canvas.ax.plot([0], [y_handle], **dict_marker_params)
            # Rectangle:
            y_anchor = y_top
            self.set_boundary_line_position = self.set_position_x
            # x min: use caretright (centered at base)
            marker_min = 9
            # x max: use caretleft (centered at base)
            marker_max = 8
            # Specify appropriate resize cursor:
            self.resize_cursor = Cursors.RESIZE_HORIZONTAL
        elif axis == 'y':
            # Line:
            self.line = mpl_canvas.ax.axhline(y=0, **dict_line_params)
            # Handle point:
            x_handle = x_left + (x_range / 2)
            self.handle_point, = mpl_canvas.ax.plot([x_handle], [0], **dict_marker_params)
            # Rectangle:
            x_anchor = x_left
            self.set_boundary_line_position = self.set_position_y
            # y min: use caretdown (centered at base)
            marker_min = 11
            # y max: use caretup (centered at base)
            marker_max = 10
            # Specify appropriate resize cursor:
            self.resize_cursor = Cursors.RESIZE_VERTICAL
        else:
            raise ValueError('Parameter \'axis\' must be either \'x\' or \'y\'')

        # Write one function to create a rectangle and add it to the canvas:
        def create_rectangle():
            self.rect = Rectangle((x_anchor, y_anchor), x_range, y_range, **dict_rect_params)
            self.mpl_canvas.ax.add_patch(self.rect)

        # Set the starting position of the line  & handle point marker shape depending on whether it is a minimum or
        # maximum boundary:
        if min_or_max == 'min':
            # Set rect anchor coords:
            x_anchor = (x_anchor if x_anchor else x_left)
            y_anchor = (y_anchor if y_anchor else y_top)
            create_rectangle()
            # Set handle point marker:
            self.handle_point.set_marker(marker_min)
            # Position the line at the minimum value of the axis:
            self.set_boundary_line_position(x=x_left, y=y_top)
        elif min_or_max == 'max':
            # Set rect anchor coords:
            x_anchor = (x_anchor if x_anchor else x_right)
            y_anchor = (y_anchor if y_anchor else y_bottom)
            create_rectangle()
            # Set handle point marker:
            self.handle_point.set_marker(marker_max)
            # Position the line at the maximum value of the axis:
            self.set_boundary_line_position(x=x_right, y=y_bottom)

        # Add artists to blit_manager:
        self.blit_manager.add_artist(self.line)
        self.blit_manager.add_artist(self.handle_point)
        self.blit_manager.add_artist(self.rect)

        # Add handle artist to cursor_manager:
        self.cursor_manager.add_artist(self)

        # Connect callbacks to matplotlib events for the specified canvas:
        self.cid_motion = mpl_canvas.fig.canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)
        self.cid_pick = mpl_canvas.fig.canvas.mpl_connect('pick_event', self.pick_event_callback)
        self.cid_release = mpl_canvas.fig.canvas.mpl_connect('button_release_event', self.mouse_release_callback)

    def set_position_x(self, x, y):
        self.line.set_xdata([x])
        self.handle_point.set_xdata([x])
        rect_width = x - self.rect.get_x()
        self.rect.set_width(rect_width)
        # Emit boundary_moved signal:
        self.boundary_moved.emit(x)

    def set_position_y(self, x, y):
        self.line.set_ydata([y])
        self.handle_point.set_ydata([y])
        rect_height = y - self.rect.get_y()
        self.rect.set_height(rect_height)
        # Emit boundary_moved signal:
        self.boundary_moved.emit(y)

    def motion_notify_callback(self, event):
        if event.inaxes == self.mpl_canvas.ax:
            # Should the boundary line be following the mouse right now?
            if self.stuck_to_mouse:
                # Move the boundary line to the location of this event:
                self.set_boundary_line_position(event.xdata, event.ydata)
                # Blit changes:
                self.blit_manager.blit_all_animated_artists()
            else:
                # The boundary line is not currently stuck to the mouse.
                # Is the cursor within the pick radius of the handle point artist?
                self.mouse_above_handle, details = self.handle_point.contains(event)

    def pick_event_callback(self, event):
        # Only do something if this handle is the picked artist:
        if event.artist == self.handle_point:
            # The handle point for this BoundaryLine has been clicked.
            # Set stuck_to_mouse to True so that if the mouse moves whilst down, the BoundaryLine will be moved:
            self.stuck_to_mouse = True

    def mouse_release_callback(self, event):
        # Set stuck_to_mouse to false:
        self.stuck_to_mouse = False

    def disconnect_callbacks(self):
        """Disconnect all callbacks connected to matplotlib events."""
        self.mpl_canvas.fig.canvas.mpl_disconnect(self.cid_motion)
        self.mpl_canvas.fig.canvas.mpl_disconnect(self.cid_pick)
        self.mpl_canvas.fig.canvas.mpl_disconnect(self.cid_release)

    def safe_disconnect(self):
        # Remove this instance from all event subscriptions and managers:
        # Remove from BlitManager:
        self.blit_manager.remove_artist(self.line)
        self.blit_manager.remove_artist(self.handle_point)
        self.blit_manager.remove_artist(self.rect)
        # Remove from CursorManager:
        self.cursor_manager.remove_artist(self)
        # Disconnect from matplotlib events:
        self.disconnect_callbacks()
        # Remove artists from canvases:
        self.line.remove()
        self.handle_point.remove()
        self.rect.remove()
