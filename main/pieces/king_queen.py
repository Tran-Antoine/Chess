# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_tower as bqt
import numpy as np

class King(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "king")
        # To know whether it can make the castling or not.


    def moves_available(self, board):
        """
        How the piece moves.
        """
        self.moves = []
        for i in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if 0 < self.position[0] + i <= 8 and 0 < self.position[1] + l <= 8:
                    # To know if there is already a white piece on the case
                    if not [self.position[0] + i, self.position[1] + l] in board.white_position:
                        self.moves.append([self.position[0] + i, self.position[1] + l])
        print(self, self.moves)
        return self.moves

    def castling(self, other):
        """
        Le roque in french.
        """
        if self.can_castle is True and other.can_castle is True:
            # If the difference is negative, it is the small castling
            if self.position[0] - other.position[0] > 0:
                # Small castling
                print("Small castling")
            # if the difference is positive, it is the big castling
            elif self.position[0] - other.position[0] < 0:
                # Big castling
                print("Big castling")


class Queen(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [[1, 1], [1, -1], [-1, 1], [-1, -1],
                              [0, 1], [0, -1], [1, 0], [-1, 0]]
        super().__init__(color, position, "queen")
