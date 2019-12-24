import rendering.api as api

class ConsoleRenderer(api.Renderer):

    def __init__(self):
        super().__init__()
        self.rows = [['' for _ in range(8)] for _ in range(8)]
        
    def initialize(self):
        # todo : change, the renderer should not do that itself, that work is for the pieces from 'get_renderables'
        print("Console renderer successfully initialized")
        self.rows[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        self.rows[1] = ['♙' for _ in range(8)] # putting white ones, black pawns (♟) are bicolored and bad sized
        self.rows[7] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        self.rows[6] = ['♙' for _ in range(8)]

    def update(self):
        super().update()
        for row in self.rows:
            print(''.join(row))
         
    def get_renderables(self):
        return [
            # board
            # pieces
        ]