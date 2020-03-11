import rendering.renderers as renderers
import rendering.api as api

class ChessBoard():
    
    """
    A simple overlay to the rendering system, which may contain more features in the future
    The ChessBoard object holds a renderer whose implementation that can be changed
    Beware that some input parsers only work for specific Renderers.
    """
    def __init__(self, renderer):
        """
        Constructs a chessboard from the given renderer
        """
        self.renderer = renderer

    def show(self):
        """
        A simple overlay to the initialize() method defined in the
        handled renderer.
        """
        self.renderer.initialize()

    def update(self, packet: api.ChessUpdatePacket, force_update=False):
        """
        A simple overlay to the update() method defined in the 
        handled renderer.
        """
        self.renderer.update(packet, force_update)