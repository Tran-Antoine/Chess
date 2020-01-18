import pieces.gamepiece as gamepiece
import pieces.directionalpieces as dirpieces
import pieces.movedata as movedata
from util.vector import Vector2f
from typing import List


class King(gamepiece.Piece):
    """
    The king piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "king")
        # To know whether it can castle or not.
        self.can_castle = True

    def moves_available(self, board):
        """
        The moves executable by the king
        """
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                next_position = Vector2f(self.position.x + i, self.position.y + j)
                # verify if the next location is on the board and if it can goes there
                if gamepiece.Piece.location_on_board(next_position) and board.can_move_at_location(next_position, self.color):
                    moves.append(self.to_simple_move_data(next_position))

        # To check if the king can castle with the rooks
        for rook in board.get_by_name("rook", self.color):
            self.add_castling_move(rook, board, moves)
        return moves

    def add_castling_move(self, rook: dirpieces.Rook, board, moves: List[movedata.MoveData]):
        if not (self.can_castle and rook.can_castle):
            return
        is_clean, direction = board.analyse_path(self.position, rook.position)
        if is_clean:
            king_destination = self.position + direction.scalar_mult(2)
            changes = {
                self.position: king_destination,
                rook.position: self.position + direction
            }
            moves.append(movedata.MoveData(king_destination, changes))

    def moved(self):
        self.can_castle = False
