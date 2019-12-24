# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import common_pieces as cp


class Pawn(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()
        # To know whether it can move two cases or only one
        self.alreadyMoved = False

    def move(self):
        """
        How the piece moves.
        """

    def transform(self):
        """
        Transform the piece into another when it reaches the end of the board.
        """


class Tower(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()
        # To know whether it can make the castling
        self.alreadyMoved = False

    def move(self):
        """
        How the piece moves.
        """
