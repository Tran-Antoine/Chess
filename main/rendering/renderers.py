import rendering.api as api
import rendering.pieces as pieces

def initial_row(row, color):
    """
    Used to retrieve a list of renderable pieces according to their initial row.
    Row 1 or row 6 correpond to a range of 8 pawns
    Row 0 or row 7 correpond to the defense line, containing the king
    """
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
    """
    An implementation of the Renderer class for playing in the console.
    Note that since it only cares about the console, no GUI is built, therefore some input parsers
    might not work along with this specific kind of renderer.
    Since the display (printed text) can not strictly speaking be modified, it updates it by reprinting it every time
    it is updated.
    """
    def __init__(self):
        """
        Constructs a ConsoleRenderer, initializing the grid with empty tiles
        """
        super().__init__()
        self.rows = [[ConsoleRenderer.EMPTY_TILE for _ in range(8)] for _ in range(8)]
        
    def initialize(self):
        """
        Asks every piece to modify the currently empty grid. 
        To achieve that goal, it force updates the renderables
        """
        print("Console renderer successfully initialized")
        self.update(None, True)

    def update(self, packet, force_update=False):
        """
        Since the display can not really be 'updated', it needs to be printed every time it is modified.
        This implementation thus simply adds a '_display' call after updating
        """
        super().update(packet, force_update)
        self._display()
    
    def render_call(self, renderable: api.Renderable):
        """
        Calls the render method designed for console rendering
        """
        renderable.render_console(self)

    def _display(self):
        """
        Displays the grid by printing it.
        Unfortunately, a chess piece's size does not equal that of a space or regular dot. 
        The display method tries to minimize the wrong alignment that the latter issue causes.
        """
        for row in self.rows[::-1]:
            print(('').join([7 * ' ' if char == ' ' else char + 6*(' ') for char in row]))
            print('\n')

    def get_renderables(self):
        """
        Loads the 4 initial rows, each piece being an instance of the RenderablePiece class.
        The board in itself does not need to be managed by a renderable, since it is just a range
        of dots.
        """
        white_row_back = initial_row(0, 'white')
        white_row_front = initial_row(1, 'white')
        black_row_front = initial_row(6, 'black')
        black_row_back = initial_row(7, 'black')

        return white_row_back + white_row_front + black_row_front + black_row_back

# Constant for the ConsoleRenderer class
ConsoleRenderer.EMPTY_TILE = '- '