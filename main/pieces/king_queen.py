# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import common_pieces as cp


class King(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()
        # To know whether it can make the castling or not.
        self.alreadyMoved = False

    def move(self):
        """
        How the piece moves.
        """

    def castling(self):
        """
        Le roque in french.
        """


class Queen(cp.Piece):
    """
    The tower piece.
    """

    def __init__(self):
        super().__init__()

    def move(self):
        """
        How the piece moves.
        """