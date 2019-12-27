# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_tower as bqt


class Pawn(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "pawn")
        # To know whether it can move two cases or only one
        self.alreadyMoved = False

    def moves_available(self, board):
        """
        How the piece moves.
        """
        self.moves = []
        # When it is the first time the pawn moves, it can moves 2 cases
        if not self.alreadyMoved and self.color.color_name == "black":
            self.moves.append([self.position[0], self.position[1] - 2])
        elif not self.alreadyMoved and self.color.color_name == "white":
            self.moves.append([self.position[0], self.position[1] + 2])

        if self.color.color_name == "black":
            self.moves.append([self.position[0], self.position[1] - 1])
        elif self.color.color_name == "white":
            self.moves.append([self.position[0], self.position[1] + 1])
        return self.moves

    def move(self, former_position, next_position, board):
        """
        Move the piece to the next position. This method must be called from
        outside of the class.
        """
        super().move(former_position, next_position, board)
        self.alreadyMoved = True

    def canEat(self, other):
        """
        Verify if there is an adverse piece that can be eaten.
        """
        

    def transform(self):
        """
        Transform the piece into another when it reaches the end of the board.
        """
        if self.color.color_name == "white" and self.position[1] == 8:
            print("TRANSFORMATION DES RENOIS!!!")
        if self.color.color_name == "black" and self.position[1] == 8:
            print("TRANSFORMATION DES COLONS!!!")

class Rook(bqt.DirectionalPiece):
    """
    The tower piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        super().__init__(color, position, "rook")
        # To know whether it can make the castling
        self.can_castle = True
