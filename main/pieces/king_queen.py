# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import pieces.common_pieces as cp
import numpy as np

class King(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board, "king")
        # To know whether it can make the castling or not.
        self.canCastling = True


    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        for i in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                    # To know if there is already a white piece on the case
                    if not [self.coords[0] + i, self.coords[1] + l] in self.board.white_position:
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


class Queen(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board, "queen")

    def moves_available(self):
        """
        How the piece moves without obstacles.
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
        self.is_obstructing()
        return self.moves

    def is_obstructing(self):
        """
        Verify if there is a piece that obstructs the passage of another piece.
        """
        for move in self.moves:
            self.column = move[0] - self.coords[0]
            self.row = move[1] - self.coords[1]
            print(self.column, self.row)














