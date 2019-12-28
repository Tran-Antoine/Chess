# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_tower as bqt
import numpy as np


class Knight(cp.Piece):
    """
    The tower piece.
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
                self.next_position = [self.position[0] + i, self.position[1] + l]
                if np.abs(i) != np.abs(l) and board.can_move_at_location(self.next_position, self.color):
                    if 0 < self.next_position[0] <= 8 and 0 < self.next_position[1] <= 8:
                        self.moves.append(self.next_position)

        print(self, self.moves)
        return self.moves


class Bishop(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        super().__init__(color, position, "bishop")
