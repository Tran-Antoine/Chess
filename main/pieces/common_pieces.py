# -*- coding: utf-8 -*-
"""
Common links between every pieces.
"""


class Piece():
    """
    Common links between every piece.
    """

    def __init__(self, color, position, name):
        # To know the position of each pieces
        self.position_letter = 'ABCDEFGH'
        self.position_number = [str(x + 1) for x in range(8)]
        self.position = position
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def moves_available(self, board):
        raise NotImplementedError()

    def location_on_board(self, loc):
        """
        Verify if the position is on the board, i.e > 0 and < 8
        """
        if 0 <= loc.x <= 7 and 0 <= loc.y <= 7:
            return True
        return False
