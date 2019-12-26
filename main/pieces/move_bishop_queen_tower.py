# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:12:01 2019

@author: willi
"""
import pieces.common_pieces as cm


class Moves(cm.Piece):
    """
    Class which verifies if a piece is obstructing another one so it cannot go
    through that piece.
    """

    def __init__(self, color, coords, Board, name, list_number):
        self.list = list_number
        super().__init__(color, coords, Board, name)

    def moves_available(self):
        """
        where the bishop can go.
        """
        self.moves = []
        # to divide and move 1 case at once
        self.divisor = 8
        for i in self.list:
            for l in self.list:
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
                    self.moves.append(self.next)
                    self.next = [self.next[0] + self.one_case[0], self.next[1] + self.one_case[1]]
                    self.index += 1
        return self.moves