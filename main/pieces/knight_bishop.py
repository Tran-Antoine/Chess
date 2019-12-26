# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import pieces.common_pieces as cp
import pieces.obstruct_movements as om
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


class Bishop(om.Obstruct):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):

        super().__init__(color, coords, Board, "bishop")

    def moves_available(self):
        """
        where the bishop can go.
        """
        self.moves = []
        # to divide and move 1 case at once
        self.divisor = 8
        for i in [-8, 8]:
            for l in [-8, 8]:
                # Move only 1 case in diagonal
                self.one_case = [i/self.divisor, l/self.divisor]
                # The next case on which the piece will be
                self.next = [self.coords[0] + self.one_case[0], self.coords[1] + self.one_case[1]]
                self.index = 0
                while self.index != self.divisor:
                    # if the piece goes out of the board or if it is on another piece
                    # stop the loop
                    if (self.next in self.board.white_position or self.next[0] > 8
                        or self.next[0] <= 0 or self.next[1] > 8 or self.next[1] <= 0):
                        break
                    # if the loop isn't stopped, move on
                    self.moves.append(self.next)
                    # move to the next case
                    self.next = [self.next[0] + self.one_case[0], self.next[1] + self.one_case[1]]
                    self.index += 1
        return self.moves
