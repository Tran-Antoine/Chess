import rendering.renderers as renderers
import rendering.api as api

class ChessBoard():

    def __init__(self):
        self.renderer = renderers.ConsoleRenderer()
              
    def show(self):
        self.renderer.initialize()
        
    def update(self, packet: api.ChessUpdatePacket):
        self.renderer.update(packet)