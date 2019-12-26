# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import pieces.common_pieces as cp
import pieces.obstruct_movements as om
import numpy as np


class Pawn(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board)
        # To know whether it can move two cases or only one
        self.alreadyMoved = False

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        # When it is the first time the pawn moves, it can moves 2 cases
        if not self.alreadyMoved and self.color.color_name == "black":
            self.moves.append([self.coords[0], self.coords[1] - 2])
        elif not self.alreadyMoved and self.color.color_name == "white":
            self.moves.append([self.coords[0], self.coords[1] + 2])

        if self.color.color_name == "black":
            self.moves.append([self.coords[0], self.coords[1] - 1])
        elif self.color.color_name == "white":
            self.moves.append([self.coords[0], self.coords[1] + 1])

        print(self.moves)

    def canEat(self, other):
        """
        Verify if there is an adverse piece that can be eaten.
        """
        

    def transform(self):
        """
        Transform the piece into another when it reaches the end of the board.
        """
        if self.color.color_name == "white" and self.coords[1] == 8:
            print("TRANSFORMATION DES RENOIS!!!")
        if self.color.color_name == "black" and self.coords[1] == 8:
            print("TRANSFORMATION DES COLONS!!!")

class Tower(om.Obstruct):
    """
    The tower piece.
    """

    def __init__(self, color, coords, Board):
        super().__init__(color, coords, Board, "tower")
        # To know whether it can make the castling
        self.canCastling = True

    def moves_available(self):
        """
        How the piece moves.
        """
        self.moves = []
        for i in self.minus8_to_8:
            # Horizontal moves
            if 0 < self.coords[0] + i <= 8:
                self.moves.append([self.coords[0] + i, self.coords[1]])
            # Vertical moves
            if 0 < self.coords[1] + i <= 8:
                self.moves.append([self.coords[0], self.coords[1] + i])
        self.is_obstructing()
        print(self.moves)
        return self.moves

    def is_obstructing(self):
        """
        """
        for move in self.moves:
            if move in self.board.white_position:
                # The difference Bx - Ax and By - Ay
                self.column = move[0] - self.coords[0]
                self.row = move[1] - self.coords[1]
                if self.column != 0 and self.row == 0:
                    self.divisor = np.abs(self.column)
                elif self.column == 0 and self.row != 0:
                    self.divisor = np.abs(self.row)
                else:
                    self.divisor = np.abs(self.column)
                # divide by the absolute value of the vector to get the smallest vector possible.
                self.next = [self.column/self.divisor, self.row/self.divisor]
                print("self.next == ", self.next)
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