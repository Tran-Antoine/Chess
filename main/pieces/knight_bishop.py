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
        print(self.coords,"BONJOUR")

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
        print(self.moves)


class Bishop(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()

    def move(self):
        """
        How the piece moves.
        """
