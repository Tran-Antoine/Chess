import rendering.api as api

class RenderablePiece(api.Renderable):

    def __init__(self, initial_position):
        super().__init__()
        self.position = initial_position
        
    def update(packet: ChessPacket):
        next = packet.new_destination(self.position)
        if next == None:
            return False
        if next == (-1, -1):
            self.destroyed = True
            return False
        self.position = next
        return True
        
    def render(renderer: ConsoleRenderer):
        pass # TODO : render the image of the piece
            
   
class PawnRenderable(RenderablePiece):

    def __init__(self, initial_position):
        super().__init__()
        self.image = None # TODO : create an image here
        
        
    
        