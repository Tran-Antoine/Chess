import rendering.api as api
import rendering.renderers as renderers # todo : why does api.py need this remote import ??
import tkinter

class RenderableBoard(api.Renderable):

    def __init__(self):
        super().__init__()
        
    def update(self, packet: api.ChessUpdatePacket):
        # Board only need to be updated once, by the initial force update of the renderer
        return False
    
    def render_console(self, renderer):
        for i, row in enumerate(renderer.rows):
            for j, tile in enumerate(row):
                if tile == None:
                    renderer.rows[i][j] = renderers.ConsoleRenderer.EMPTY_TILE
    
    def render_tkinter(self, renderer):
        display = renderer.thread.display
        white = True
        for i in range(1, 9):
            for j in range(1, 9):
                tile = tkinter.Frame(master=display, bg=('white' if white else 'black'))
                display.grid(row=i, column=j)

class RenderablePiece(api.Renderable):
    """
    Implementation of the renderable class for chess pieces
    """
    def __init__(self, initial_position, color):
        super().__init__()
        self.position = initial_position
        self.next_position = None
        self.color = color
    
    def console_symbol(self):
        """
        Defined to return the symbol of the piece.
        Note that the returned value is not necessarily constant, since its value might depend on the color
        """
        raise NotImplementedError()
            
    def update(self, packet: api.ChessUpdatePacket):
        # print(f"Looking for updating {type(self)}")
        if packet == None:
            return False
        next = packet.new_destination(self.position)
        if next == None:
            return False  
        # print(f"Next destination found : {next}")            
        if next == (-1, -1):
            self.destroyed = True
            return False
        self.next_position = next
        return True
        
    def render_console(self, renderer):
        """
        Updates the display by modifying the grid of pieces hold by the renderer.
        The current position of the piece is replaced by an empty tile.
        Then, the next position is replaced by the symbol of the piece
        """
        # print(f"Rendering piece {type(self)} from {self.position} to {self.next_position}")
        old_x = self.position[0]
        old_y = self.position[1]
        if self.next_position == None: # meaning that we just want to 'refresh'
            # print(self.console_symbol() + " goes at loc " + str(self.position))
            renderer.rows[old_y][old_x] = self.console_symbol()
            return
        x = self.next_position[0]
        y = self.next_position[1]
        renderer.rows[old_y][old_x] = renderers.ConsoleRenderer.EMPTY_TILE
        renderer.rows[y][x] = self.console_symbol()
        self.position = self.next_position
        self.next_position = None
            
   
class PawnRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♙'

class KnightRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♘' if self.color == 'white' else '♞'
        
class BishopRenderable(RenderablePiece):
 
    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♗' if self.color == 'white' else '♝'
        
class RookRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♖' if self.color == 'white' else '♜'
        
class QueenRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♕' if self.color == 'white' else '♛'

class KingRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♔' if self.color == 'white' else '♚' 