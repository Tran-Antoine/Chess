# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:12:01 2019

@author: willi
"""
import pieces.common_pieces as cm
from util.vector import Vector2f

class DirectionalPiece(cm.Piece):
    """
    Class which verifies if a piece is obstructing another one so it cannot go
    through that piece.
    """

    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def moves_available(self, board):
        """
        where the bishop can go.
        """
        self.moves = []
        # to divide and move 1 case at once
        self.divisor = 8
        for dir_angle in self.one_case_list:
            # The next case on which the piece will be
            self.next = Vector2f(self.position.x + dir_angle.x, self.position.y + dir_angle.y)
            self.index = 0
            while self.index != self.divisor:
                # if the piece goes out of the board or if it is on another piece
                # stop the loop
                self.piece = board.piece_at_location(self.next)
                if self.piece is not None and self.location_on_board(self.next):
                    if self.piece.color != self.color:
                        self.moves.append(self.next)
                    break
                elif self.piece is None and self.location_on_board(self.next):
                    self.moves.append(self.next)
                self.next = Vector2f(self.next.x + dir_angle.x, self.next.y + dir_angle.y)
                self.index += 1
        return self.moves