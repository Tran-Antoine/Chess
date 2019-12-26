# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:12:01 2019

@author: willi
"""
import pieces.common_pieces as cm
import numpy as np

class Obstruct(cm.Piece):
    """
    Class which verifies if a piece is obstructing another one so it cannot go
    through that piece.
    """

    def __init__(self, color, coords, Board, name):
        super().__init__(color, coords, Board, name)

    def is_obstructing(self):
        """Verify whether a move is possible or not."""
        for move in self.moves:
            if move in self.board.white_position:
                # The difference Bx - Ax and By - Ay
                self.column = move[0] - self.coords[0]
                self.row = move[1] - self.coords[1]
                # divide by the absolute value of the vector to get the smallest vector possible.
                self.next = [self.column/np.abs(self.column), self.row/np.abs(self.row)]
                # Add one move, so when it goes in the loop it verifies if
                # this move is possible.
                self.next_coords = [self.coords[0] + self.next[0], self.coords[1] + self.next[1]]
                # When a piece is obstructing, change the bool to remove
                #the moves which are after the obstructing piece
                self.remove_move = False
                while True:
                    # If the the next case is in a position of a piece,
                    # remove every move that is after.
                    if self.next_coords in self.board.white_position or self.remove_move is True:
                        print("liste self.moves: ", self.moves)
                        # If there is no next move, goes out of the loop
                        try:
                            self.moves.remove(self.next_coords)
                        except ValueError:
                            break
                        # to remove every move after
                        self.remove_move = True
                    
                    self.next_coords = [self.next_coords[0] + self.next[0], self.next_coords[1] + self.next[1]]
        print(self, self.moves)
