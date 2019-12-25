import rendering.api as api
import rendering.pieces as pieces

def initial_row(row, color):
    if row == 1 or row == 6:
        return [pieces.PawnRenderable((x, row), color) for x in range(8)]
    return [
        pieces.RookRenderable((0, row), color),
        pieces.KnightRenderable((1, row), color),
        pieces.BishopRenderable((2, row), color),
        pieces.QueenRenderable((3, row), color),
        pieces.KingRenderable((4, row), color),
        pieces.BishopRenderable((5, row), color),
        pieces.KnightRenderable((6, row), color),
        pieces.RookRenderable((7, row), color)
    ]
    

class ConsoleRenderer(api.Renderer):

    def __init__(self):
        super().__init__()
        self.rows = [[ConsoleRenderer.EMPTY_TILE for _ in range(8)] for _ in range(8)]
        
    def initialize(self):
        # todo : change, the renderer should not do that itself, that work is for the pieces from 'get_renderables'
        print("Console renderer successfully initialized")
        self.update(None, True)

    def update(self, packet, force_update=False):
        super().update(packet, force_update)
        self._display()
    
    def render_call(self, renderable: api.Renderable):
        renderable.render_console(self)

    def _display(self):
        for row in self.rows[::-1]:
            print(('').join([7 * ' ' if char == ' ' else char + 6*(' ') for char in row]))
            print('\n')

    def get_renderables(self):
        white_row_back = initial_row(0, 'white')
        white_row_front = initial_row(1, 'white')
        black_row_front = initial_row(6, 'black')
        black_row_back = initial_row(7, 'black')

        return white_row_back + white_row_front + black_row_front + black_row_back
        
ConsoleRenderer.EMPTY_TILE = '- '