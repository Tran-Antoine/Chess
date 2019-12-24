# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import common_pieces as cp
import numpy as np


class Knight(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords):
        super().__init__(color, coords)
        self.moves_available()
        print(f"The knight's coordinates: {self.coords}")

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        # Every move possible when there is no obstacles
        for i in [-1, -2, 1, 2]:
            for l in [-1, -2, 1, 2]:
                if np.abs(i) != np.abs(l):
                    self.moves.append([self.coords[0] + i, self.coords[1] + l])

        # To know whether the knight is on the edge of the board and remove
        # the positions which are outside the board.
        self.available = list(self.moves)
        for position in self.available:
            if position[0] > 8 or position[1] > 8:
                self.moves.remove(position)
        print(self.moves)


class Bishop(cp.Piece):
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

        self.move_available()

    def move_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        for i in self.minus8_to_8:
            for l in self.minus8_to_8:
                if np.abs(i) == np.abs(l) and 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                    self.moves.append([self.coords[0] + i, self.coords[1] + l])
        print(self.moves)


























