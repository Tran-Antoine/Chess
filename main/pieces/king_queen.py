# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_rook as bqr
from util.vector import Vector2f

class King(cp.Piece):
    """
    The king piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "king")
        # To know whether it can make the castling or not.
        self.can_castle = True

    def moves_available(self, board):
        """
        The moves executable by the king
        """
        self.moves = []
        for i in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                self.next = Vector2f(self.position.x + i, self.position.y + l)
                # verify if the next location is on the board and if it can goes there
                if self.location_on_board(self.next) and board.can_move_at_location(self.next, self.color):
                    self.moves.append(self.next)

        # To check if the king can castle with the rooks
        for piece in board.get_rooks(self.color):
            self.add_castling_move(piece, board)
        return self.moves

    def add_castling_move(self, rook, board):
        if not (self.can_castle and rook.can_castle):
            return
        self.delta_x = self.position.x - rook.position.x
        if self.delta_x < 0:
            # Small castling
            self.next_case = 1
            self.is_obstructing_castling(board, self.next_case)
            if self.distance_king_rook == 2:
                self.moves.append(Vector2f(self.position.x + 2, self.position.y))
                print("small castle")

        elif self.delta_x > 0:
            # Big castling
            self.next_case = -1
            self.is_obstructing_castling(board, self.next_case)
            if self.distance_king_rook == 3:
                self.moves.append(Vector2f(self.position.x - 2, self.position.y))
                print("Big castle")

    def is_obstructing_castling(self, board, next_case):
        """
        Verify if there are pieces between the rook and the king in order
        to castle.
        """
        self.distance_king_rook = 0
        self.next_position = Vector2f(self.position.x + next_case, self.position.y)
        while True:
            if board.piece_at_location(self.next_position) is None:
                self.distance_king_rook += 1
                self.next_position.x += next_case
            else:
                break


class Queen(bqr.DirectionalPiece):
    """
    The queen piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [Vector2f(1, 1), Vector2f(1, -1), Vector2f(-1, 1), Vector2f(-1, -1),
                              Vector2f(0, 1), Vector2f(0, -1), Vector2f(1, 0), Vector2f(-1, 0)]
        super().__init__(color, position, "queen")
