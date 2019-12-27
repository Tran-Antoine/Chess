# -*- coding: utf-8 -*-
"""
Common links between every pieces.
"""


class Piece():
    """
    Common links between every pieces.
    """

    def __init__(self, color, coords, name):
        # To know the position of each pieces
        self.coords_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.coords_number = [str(x + 1) for x in range(8)]
        self.position = None
        self.name = name
        self.color = color
        # a list [x, y]
        self.coords = coords
        # The image of the piece
        self.image = None

        print(f"The {self}'s coordinates: {self.coords_letter[self.coords[0] - 1]}{self.coords[1]}")


    def __str__(self):
        return self.name

    def move(self, former_coord, next_coord, board):
        """
        Move the piece to the next position. This method must be called from
        outside of the class.
        """
        self.coords = next_coord
        for index, position in enumerate(board.white_position):
            print(former_coord, position)
            if former_coord == position:
                board.white_position[index] = next_coord
                print("Bonjour")
                break
        print(board.white_position)

    def moves_available(self, board):
        raise NotImplementedError()

