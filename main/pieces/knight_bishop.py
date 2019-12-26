# -*- coding: utf-8 -*-
"""
The knight and the bishop.
"""
import pieces.common_pieces as cp
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
                    self.moves.append([self.coords[0] + i, self.coords[1] + l])

        # To know whether the knight is on the edge of the board and remove
        # the positions which are outside the board.
        self.available = list(self.moves)
        for position in self.available:
            if position[0] > 8 or position[0] <= 0 or position[1] > 8 or position[1] <= 0 or position in self.board.white_position:
                self.moves.remove(position)
        print(self, self.moves)
        return self.moves


class Bishop(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board, "bishop")

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        for i in self.minus8_to_8:
            for l in self.minus8_to_8:
                if np.abs(i) == np.abs(l) and 0 < self.coords[0] + i <= 8 and 0 < self.coords[1] + l <= 8:
                    self.moves.append([self.coords[0] + i, self.coords[1] + l])
        self.is_obstructing()
        return self.moves

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
