# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_rook as bqr
import numpy as np
from util.vector import Vector2f

class Knight(cp.Piece):
    """
    The knight piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "knight")

    def moves_available(self, board):
        """
        How the piece moves.
        """
        self.moves = []
        # Every move possible
        for i in [-1, -2, 1, 2]:
            for l in [-1, -2, 1, 2]:
                self.next_position = Vector2f(self.position.x + i, self.position.y + l)
                if np.abs(i) != np.abs(l) and board.can_move_at_location(self.next_position, self.color):
                    if self.location_on_board(self.next_position):
                        self.moves.append(self.next_position)

        print(self, self.moves)
        return self.moves


class Bishop(bqr.DirectionalPiece):
    """
    The bishop piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [Vector2f(1, 1), Vector2f(-1, 1), Vector2f(-1, -1), Vector2f(1, -1)]
        super().__init__(color, position, "bishop")
