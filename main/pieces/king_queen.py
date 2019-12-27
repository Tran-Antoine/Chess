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

    def __init__(self, color, coords):
        super().__init__(color, coords, "king")
        # To know whether it can make the castling or not.
        self.canCastling = True


    def moves_available(self, board):
        """
        How the piece moves.
        """
        self.moves = []
        for i in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                    # To know if there is already a white piece on the case
                    if not [self.coords[0] + i, self.coords[1] + l] in board.white_position:
                        self.moves.append([self.coords[0] + i, self.coords[1] + l])
        print(self, self.moves)
        return self.moves

    def castling(self, other):
        """
        Le roque in french.
        """
        if self.canCastling is True and other.canCastling is True:
            # If the difference is negative, it is the small castling
            if self.coords[0] - other.coords[0] > 0:
                # Small castling
                print("Small castling")
            # if the difference is positive, it is the big castling
            elif self.coords[0] - other.coords[0] < 0:
                # Big castling
                print("Big castling")


class Queen(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, coords):
        self.one_case_list = [[1, 1], [1, -1], [-1, 1], [-1, -1],
                              [0, 1], [0, -1], [1, 0], [-1, 0]]
        super().__init__(color, coords, "queen")
