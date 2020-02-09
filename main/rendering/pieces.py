import rendering.api as api
import rendering.renderers as renderers # todo : why does api.py need this remote import ??
import util.vector as vector
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

    def render_tkinter_with_frame(self, renderer):
        root = renderer.thread.queue.get(timeout=1)
        renderer.thread.queue.put(root)
        white = True
        for i in range(1, 9):
            for j in range(1, 9):
                tile = tkinter.Frame(master=root, bg=('#eccca1' if white else '#c78b57'), width=80, height=80)
                tile.grid(row=i, column=j)
                white = not white
            white = not white

    def render_tkinter_with_canvas(self, renderer):
        """
        Create the graphical interface with the chessboard and the number 1-8 and A-H.
        """
        root = renderer.thread.queue.get(timeout=1)
        renderer.thread.queue.put(root)
        LETTER_LIST = ["A", "B", "C", "D", "E", "F", "G", "H"]
        renderer.canvas = tkinter.Canvas(master=root, height=renderer.CANVAS_SIZE, width=renderer.CANVAS_SIZE)
        renderer.canvas.grid(row=1, column=2, rowspan=8, columnspan=8)
        white = True
        for i in range(1, 9):
            label_y = tkinter.Label(master=root, text=9 - i, height=5, width=5, font=30)
            label_y.grid(row=i, column=1)
            label_x = tkinter.Label(master=root, text=LETTER_LIST[i - 1], height=5, width=5, font=30)
            label_x.grid(row=9, column=i + 1)
            for j in range(1, 9):
                renderer.canvas.create_rectangle(renderer.CANVAS_SIZE/8*(i - 1), renderer.CANVAS_SIZE/8*(j - 1),
                                                 renderer.CANVAS_SIZE/8*i, renderer.CANVAS_SIZE/8*j,
                                                 fill=('#eccca1' if white else '#c78b57'))
                white = not white
            white = not white
        # position where the piece should be on the canvas
        renderer.canvas.piece_position = vector.Vector2f(0, 7)


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
#        print(f"Next destination found : {next}")            
        if next == vector.Vector2f(-1, -1):
            self.destroyed = True
        self.next_position = next
        return True
        
    def render_console(self, renderer):
        """
        Updates the display by modifying the grid of pieces hold by the renderer.
        The current position of the piece is replaced by an empty tile.
        Then, the next position is replaced by the symbol of the piece
        """
        print(f"Rendering piece {type(self)} from {self.position} to {self.next_position}")
        old_x = self.position.x
        old_y = self.position.y
        if self.next_position is None: # meaning that we just want to 'refresh'
            renderer.rows[old_y][old_x] = self.console_symbol()
            return
        x = self.next_position.x
        y = self.next_position.y
        renderer.rows[old_y][old_x] = renderers.ConsoleRenderer.EMPTY_TILE
        renderer.rows[y][x] = self.console_symbol()
        self.position = self.next_position
        self.next_position = None
        
    def render_tkinter_with_frame(self, renderer):
        if self.display_image is None:
            self.load_display_image_frame(renderer)

        next = None
        if self.next_position is None:
            next = self.position
        else:
            next = self.next_position
        print(next)
        if next == vector.Vector2f(-1, -1):
            self.display_image.grid()
        real_next = self.convert_to_tkinter_coords(next)
        # there might be a better way of doing this
        self.display_image.grid(column=real_next.x + 1, row=real_next.y + 1)
        self.position = next
        self.next_position = None

    def render_tkinter_with_canvas(self, renderer):
        if self.display_image is not None:
            next = None
            if self.next_position is None:
                next = self.position
            else:
                next = self.next_position
            real_next = self.convert_to_canvas_coords(renderer, next)
            position_in_canvas_coords = self.convert_to_canvas_coords(renderer, self.position)
            renderer.canvas.move(self.display_image, -(position_in_canvas_coords.x - real_next.x),
                                 -(position_in_canvas_coords.y - real_next.y))
            self.position = next
            self.next_position = None
        else:
            self.load_display_image_canvas(renderer)


    def convert_to_canvas_coords(self, renderer, coords):
        return vector.Vector2f(renderer.CANVAS_SIZE/16 + renderer.CANVAS_SIZE/8 * coords.x,
                               (renderer.CANVAS_SIZE - renderer.CANVAS_SIZE/16) - renderer.CANVAS_SIZE/8*coords.y)

    def convert_to_tkinter_coords(self, coords):
        return vector.Vector2f(coords.x, 7 - coords.y)

    def load_display_image_canvas(self, renderer):
        """Initialize the images when the program is run"""
        root = renderer.thread.queue.get(timeout=1)
        renderer.thread.queue.put(root)
        image = Image.open("rendering/assets/" + self.color + '/' + self.file_name())
        renderer.canvas.image = ImageTk.PhotoImage(image)
        self.display_image = renderer.canvas.create_image(renderer.CANVAS_SIZE/16 + renderer.CANVAS_SIZE/8*renderer.canvas.piece_position.x,
                                                          renderer.CANVAS_SIZE/16 + renderer.CANVAS_SIZE/8*renderer.canvas.piece_position.y,
                                                          image=renderer.canvas.image)
        if renderer.canvas.piece_position.x != vector.Vector2f(7, 0).x:
            renderer.canvas.piece_position = vector.Vector2f(renderer.canvas.piece_position.x + 1, renderer.canvas.piece_position.y)
        elif renderer.canvas.piece_position == vector.Vector2f(7, 6):
            renderer.canvas.piece_position = vector.Vector2f(0, 1)
        else:
            renderer.canvas.piece_position = vector.Vector2f(0, renderer.canvas.piece_position.y - 1)
        renderer.list_images.append(renderer.canvas.image)

    def load_display_image_frame(self, renderer):
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