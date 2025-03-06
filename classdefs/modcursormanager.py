from matplotlib.backend_tools import Cursors


class CursorManager:
    def __init__(self, mpl_canvas):
        self.mpl_canvas = mpl_canvas
        self.list_of_artists = []

        # Connect motion_notify_callback to matplotlib event:
        self.mpl_canvas.fig.canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)

    def add_artist(self, artist):
        self.list_of_artists.append(artist)

    def remove_artist(self, artist):
        try:
            self.list_of_artists.remove(artist)
        except:
            print(f'Artist {artist} not under management.')

    def motion_notify_callback(self, *args):
        _any = False

        for artist in self.list_of_artists:
            if artist.mouse_above_handle:
                # Transform into the associated cursor:
                self.mpl_canvas.fig.canvas.set_cursor(artist.resize_cursor)
                # Set the variable _any to true:
                _any = True

        if not _any:
            # Revert cursor to pointer:
            self.mpl_canvas.fig.canvas.set_cursor(Cursors.POINTER)