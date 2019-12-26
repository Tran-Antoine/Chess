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

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board, "knight")

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        # Every move possible when there is no obstacles
        for i in [-1, -2, 1, 2]:
            for l in [-1, -2, 1, 2]:
                if np.abs(i) != np.abs(l) and [self.coords[0] + i, self.coords[1] + l] not in self.board.white_position:
                    if 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                        self.moves.append([self.coords[0] + i, self.coords[1] + l])

        print(self, self.moves)
        return self.moves


class Bishop(bqt.Moves):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        self.list = [-8, 8]
        super().__init__(color, coords, Board, "bishop", self.list)
