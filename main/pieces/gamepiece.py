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
        """
        Computes a list of moves (represented by the MoveData class),
        corresponding to the available moves of the piece at the current
        state of the game. This method must take into account the location
        of the other pieces (for instance, a rook cannot go through a piece),
        but also the general state of the game. For instance, if the king
        is in check, the overall moves of the pieces are restricted: the next
        move must protect the king.
        """
        raise NotImplementedError()

    def absolute_moves_available(self, board):
        absolute_moves = []
        moves = self.moves_available(board)
        for move in moves:
            changes = move.changes
            valid = board.is_safe_for_king(self.color, changes)
            if valid:
                absolute_moves.append(move)
        return absolute_moves

    def moved(self):
        """
        Called once the piece is moved, regardless of the destination.
        Several pieces might implement this method, such as the king,
        which bans the 'castling' from his moves once he has moved once.
        """
        pass

    @staticmethod
    def location_on_board(loc: vector.Vector2f):
        """
        Checks whether the position is on the board.
        Coordinates are considered 'on the board' if both
        their components are between 1 and 7 included.
        """
        return 0 <= loc.x <= 7 and 0 <= loc.y <= 7

