# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import pieces.gamepiece as gamepiece
import pieces.pieces_manager as pieces_manager
from util.vector import Vector2f


class Knight(gamepiece.Piece):
    """
    The knight piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "knight")

    def moves_available(self, board):
        """
        How the piece moves.
        """
        moves = []
        # Every move possible
        for i in [-1, -2, 1, 2]:
            for j in [-1, -2, 1, 2]:
                next_position = Vector2f(self.position.x + i, self.position.y + j)
                if abs(i) != abs(j) and board.can_move_at_location(next_position, self.color):
                    if gamepiece.Piece.location_on_board(next_position):
                        moves.append(self.to_simple_move_data(next_position))

        return moves

