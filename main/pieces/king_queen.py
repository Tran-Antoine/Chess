# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import common_pieces as cp
import numpy as np

class King(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()
        # To know whether it can make the castling or not.
        self.alreadyMoved = False

    def move(self):
        """
        How the piece moves.
        """

    def castling(self):
        """
        Le roque in french.
        """


class Queen(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords):
        super().__init__(color, coords)

        # A list from -8 to 8, useful for the moves later.
        self.minus8_to_8 = []
        for i in range(16):
            if i >= 8:
                self.minus8_to_8.append(i - 7)
            else:
                self.minus8_to_8.append(-8 + i)

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []

        for i in self.minus8_to_8:
            for l in self.minus8_to_8:
                # Diagonal moves
                if np.abs(i) == np.abs(l) and 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                    self.moves.append([self.coords[0] + i, self.coords[1] + l])
            # Horizontal moves
            if 0 < self.coords[0] + i <= 8:
                self.moves.append([self.coords[0] + i, self.coords[1]])
            # Vertical moves
            if 0 < self.coords[1] + i <= 8:
                self.moves.append([self.coords[0], self.coords[1] + i])
        return self.moves
















