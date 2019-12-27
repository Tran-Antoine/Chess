import rendering.api as api
import rendering.renderers as renderers # todo : why does api.py need this remote import ??
import tkinter
import threading
from PIL import Image, ImageTk

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
        root = renderer.thread.queue.get(timeout=1)
        renderer.thread.queue.put(root)
        white = True
        for i in range(1, 9):
            for j in range(1, 9):
                tile = tkinter.Frame(master=root, bg=('#eccca1' if white else '#c78b57'), width=80, height=80)
                tile.grid(row=i, column=j)
                white = not white
            white = not white

class RenderablePiece(api.Renderable):
    """
    Implementation of the renderable class for chess pieces
    """
    def __init__(self, initial_position, color):
        super().__init__()
        self.position = initial_position
        self.next_position = None
        self.color = color
        self.display_image = None
    
    def console_symbol(self):
        """
        Defined to return the symbol of the piece.
        Note that the returned value is not necessarily constant, since its value might depend on the color
        """
        raise NotImplementedError()
    
    def file_name(self):
        """
        Defined to return the name of the file, stored in 'rendering/assets/white' or in 'rendering/assets/black'
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
        
    def render_tkinter(self, renderer):
        if self.display_image == None:
            self.load_display_image(renderer)
    
        next = None
        if self.next_position == None:
            next = self.position
        else:
            next = self.next_position
        real_next = self.convert_to_tkinter_coords(next)
        # there might be a better way of doing this
        self.display_image.grid(column=real_next[0] + 1, row=real_next[1] + 1)
        self.position = next
        self.next_position = None
    
    def convert_to_tkinter_coords(self, coords):
        return (coords[0], 7 - coords[1])
        
    def load_display_image(self, renderer):
        root = renderer.thread.queue.get(timeout=1)
        renderer.thread.queue.put(root)
        
        image = Image.open("rendering/assets/" + self.color + '/' + self.file_name())
        render = ImageTk.PhotoImage(image)
        self.display_image = tkinter.Label(master=root, image=render)
        self.display_image.image = render
            
   
class PawnRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♙'
    
    def file_name(self):
        return 'pawn.png'

class KnightRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♘' if self.color == 'white' else '♞'
        
    def file_name(self):
        return 'knight.png'
        
class BishopRenderable(RenderablePiece):
 
    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♗' if self.color == 'white' else '♝'

    def file_name(self):
        return 'bishop.png'
        
class RookRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♖' if self.color == 'white' else '♜'

    def file_name(self):
        return 'rook.png'
        
class QueenRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♕' if self.color == 'white' else '♛'

    def file_name(self):
        return 'queen.png'

class KingRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
     
    def console_symbol(self):
        return '♔' if self.color == 'white' else '♚'
        
    def file_name(self):
        return 'king.png'