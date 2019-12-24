from typing import List
import rendering.renderers as renderers

class ChessUpdatePacket():
    
    # tile_modifications links a position with a new position.
    # If new position is -1, -1, piece is destroyed
    def __init__(self, tile_modifications, pieces_lost1=None, pieces_lost2=None):
        self.tile_modifications = tile_modifications
        self.pieces_lost1 = pieces_lost1
        self.pieces_lost2 = pieces_lost2
        
    def new_destination(self, initial):
        if initial in self.tile_modifications.keys():
            return self.tile_modifications[initial]
        return None
  
class Renderable():

    def __init__(self):
        self.destroyed = False
        
    def render(self, renderer):
        raise NotImplementedError()
    
    def update(self, packet: ChessUpdatePacket):
        raise NotImplementedError()
      
class Renderer():

    def __init__(self):
        self.renderables = self.get_renderables()
        self.destroyed = False
        
    def initialize(self):
        raise NotImplementedError()
        
    def get_renderables(self) -> List[Renderable]:
        raise NotImplementedError()
        
    def update(self, packet: ChessUpdatePacket, force_update=False):
        for renderable in self.renderables:
            needs_update = renderable.update(packet)
            if not renderable.destroyed and (force_update or needs_update):
                renderable.render(self)
        self.renderables = filter(lambda r: not r.destroyed, self.renderables)
