from typing import List
import rendering.renderers as renderers


class ChessUpdatePacket():
    """
    A data class storing the modification of the chess board caused by
    the latest move played
    """
    # tile_modifications links a position with a new position.
    # If new position is -1, -1, piece is destroyed
    def __init__(self, tile_modifications, new_piece=None):
        """
        Constructs a packet from a dictionnary linking initial positions to destinations.
        """
        self.tile_modifications = tile_modifications
        self.new_piece = new_piece
        
    def new_destination(self, initial):
        """
        Retrieves the destination of a location.
        If the given location can not be found in the "initial positions", returns None
        """
        if initial in self.tile_modifications.keys():
            return self.tile_modifications[initial]
        return None  # explicit yet not obligatory return statement to clarify

    def __str__(self):
        return self.tile_modifications.__str__()


ChessUpdatePacket.STOP = ChessUpdatePacket({})
ChessUpdatePacket.INVALID = ChessUpdatePacket({})


class Renderable():

    """
    An Object that can be displayed on the screen.
    Renderables are managed by a Renderer. Renderers construct or update a displayable result each frame,
    by asking every renderable that they hold to update themselves, providing modifications to the current result.
    Eventually, once modified by every renderable, the result is displayed once per frame on the screen.
    However, renderables are not always enclined to bring modification to the constructed display. Therefore, rendering
    updates are performed only if the update() method returns True, meaning that the object wants to modify the display.
    The renders method take care of that action, and must be defined for each Renderer implementation available.

    Renderables can be destroyed, by setting the 'destroyed' field to True. Once a renderable is destroyed,
    the renderer managing it must simply chuck it and stop using it.
    """
    def __init__(self):
        """
        Constructs a renderable
        """
        self.destroyed = False
        
    def render_console(self, renderer):
        """
        Implementation of the render method for the ConsoleRenderer
        """
        raise NotImplementedError()
        
    def render_tkinter_with_frame(self, renderer):
        """
        Implementation of the render method for the FrameTkinterRenderer
        """
        raise NotImplementedError()

    def render_tkinter_with_canvas(self, renderer):
        """
        Implementation of the render method for the CanvasTkinterRenderer
        """
        raise NotImplementedError()

    def update(self, packet: ChessUpdatePacket):
        """
        Checks whether the renderable wants to modify the display or not.
        The update method may also modify the renderable object itself, but should usually not change
        the packet it is provided.
        If this method returns true, one of the render methods of the object will be chosen
        by the renderer, and then be called to update the display
        """
        raise NotImplementedError()


class Renderer():

    """
    A manager holding renderables, that is in itself NOT able to render a result.
    Renderers are initialized through the "initialize" method, and should be updated every time
    a potential display modification is to occur. When that happens, the renderer will ask every renderable
    it contains whether they 'want' to modify the display or not. If they do, they will modify themselves the
    result managed by the Renderer
    """
    def __init__(self):
        """
        Constructs a renderer.
        The renderables are loaded and stored at the moment the object is created
        """
        self.renderables = self.get_renderables()
        self.destroyed = False

    def initialize(self):
        """
        Initializes the renderer. 
        This is method should only be called once, when the rendered must be prepared to be updated.
        Uninitialized renderers that are updated might cause unexpected results.
        """
        raise NotImplementedError()

    def get_renderables(self) -> List[Renderable]:
        """
        Used to load / retrieve the renderables that the Renderer needs to be able to construct his display
        """
        raise NotImplementedError()

    def render_call(self, renderable: Renderable):
        """
        Calls one of the render methods of the renderable. For instance, the ConsoleRenderer will call the render_console()
        method, where as the TkinterRenderer will call the render_tkinter_with_frame() method.
        Unfortunately, python does not allow several methods to have the same name and parameter length, since object types
        are not explicitely mentionned.
        """
        raise NotImplementedError()

    def update(self, packet: ChessUpdatePacket, force_update=False):
        """
        Updates the renderer.
        By default, the object will simply go through every renderable it manages, checks whether they 
        want to update the display, asks them to do so if they want to, and eventually removes all the
        destroyed renderables of the list
        """
        for renderable in self.renderables:
            needs_update = renderable.update(packet)
            if force_update or needs_update:
                self.render_call(renderable)
        self.renderables = list(filter(lambda r: not r.destroyed, self.renderables))
