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
        self.position_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.position_number = [str(x + 1) for x in range(8)]
        self.position = position
        self.name = name
        self.color = color

        # The image of the piece
        self.image = None

#        print(f"The {self}'s coordinates: {self.position_letter[self.position[0] - 1]}{self.position[1]}")

    def __str__(self):
        return self.name

    def move(self, former_position, next_position, board):
        """
        Move the piece to the next position. This method must be called from
        outside of the class.
        """
        for index, piece in enumerate(board.pieces):
            if former_position == piece.position:
                piece.position = next_position
                break

    def moves_available(self, board):
        raise NotImplementedError()

    def location_on_board(self, loc):
        """
        Verify if the position is on the board, i.e > 0 and < 8
        """
        if 0 < loc[0] <= 8 and 0 < loc[1] <= 8:
            return True
        return False
