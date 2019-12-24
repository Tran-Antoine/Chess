import rendering.api as api
import rendering.renderers as renderers

class RenderablePiece(api.Renderable):

    def __init__(self, initial_position, color):
        super().__init__()
        self.position = initial_position
        self.next_position = None
        self.color = color
    
    def console_symbol(self):
        raise NotImplementedError()
            
    def update(self, packet: api.ChessUpdatePacket):
        print(f"Looking for updating {type(self)}")
        if packet == None:
            return
        next = packet.new_destination(self.position)
        if next == None:
            return False  
        print(f"Next destination found : {next}")            
        if next == (-1, -1):
            self.destroyed = True
            return False
        self.next_position = next
        return True
        
    def render(self, renderer):
        old_x = self.position[0]
        old_y = self.position[1]
        if self.next_position == None: # meaning that we just want to 'refresh'
            print(self.console_symbol() + " goes at loc " + str(self.position))
            renderer.rows[old_y][old_x] = self.console_symbol()
            return
        x = self.next_position[0]
        y = self.next_position[1]
        renderer.rows[old_y][old_x] = ''
        renderer.rows[y][x] = self.console_symbol()
            
   
class PawnRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♙'

class KnightRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♘' if self.color == 'white' else '♞'
        
class BishopRenderable(RenderablePiece):
 
    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♗' if self.color == 'white' else '♝'
        
class RookRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♖' if self.color == 'white' else '♜'
        
class QueenRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♕' if self.color == 'white' else '♛'

class KingRenderable(RenderablePiece):

    def __init__(self, initial_position, color):
        super().__init__(initial_position, color)
        self.image = None # TODO : create an image here
     
    def console_symbol(self):
        return '♔' if self.color == 'white' else '♚' 