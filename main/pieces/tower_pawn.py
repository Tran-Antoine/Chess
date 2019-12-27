# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_tower as bqt
import numpy as np


class Pawn(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, coords):
        super().__init__(color, coords)
        # To know whether it can move two cases or only one
        self.alreadyMoved = False

    def moves_available(self, board):
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

class Rook(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, coords):
        self.one_case_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        super().__init__(color, coords, "rook")
        # To know whether it can make the castling
        self.canCastling = True
