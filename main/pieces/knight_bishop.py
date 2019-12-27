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
        if self.color.color_name == "white":
            self.allies_position = board.white_position
        else:
            self.allies_position = board.black_position
        self.moves = []
        # Every move possible when there is no obstacles
        print(self.allies_position)
        for i in [-1, -2, 1, 2]:
            for l in [-1, -2, 1, 2]:
                if np.abs(i) != np.abs(l) and [self.position[0] + i, self.position[1] + l] not in self.allies_position:
                    if 0 < self.position[0] + i <= 8 and 0 < self.position[1] + l <= 8:
                        self.moves.append([self.position[0] + i, self.position[1] + l])

        print(self, self.moves)
        return self.moves


class Bishop(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        super().__init__(color, position, "bishop")
