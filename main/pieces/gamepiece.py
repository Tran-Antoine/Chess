import pieces.movedata as movedata
import util.vector as vector
from typing import List


class Piece():
    """
    An imaginary representation of a chess piece.
    Pieces are defined by their position, their color, their name and most
    importantly by their movements. Every piece is to implement the
    moves_available method, which computes a list of possible moves with the
    current state of the board. Some pieces perform special actions after
    being moved. For instance, the King removes the 'castling' move from
    his possible moves as soon as he gets moved once. These actions are
    handled by the 'moved' method, empty by default.
    """

    def __init__(self, color, position, name):
        """
        Constructs a piece.
        Pieces are defined with a color (Color), a position (util.vector.Vector2f)
        and a name (str).
        """
        self.position = position
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def to_simple_move_data(self, next_destination: vector.Vector2f) -> movedata.MoveData:
        """
        Usual conversion of a destination to a MoveData object.
        The current position is linked to the next_destination parameter, and
        the next_destination is linked to the destruction vector (-1; -1)
        """
        changes = {self.position: next_destination, next_destination: vector.Vector2f.DESTROY}
        return movedata.MoveData(next_destination, changes)

    def moves_available(self, board) -> List[movedata.MoveData]:
        raise NotImplementedError()

    def moved(self):
        pass

