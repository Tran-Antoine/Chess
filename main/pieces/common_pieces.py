# -*- coding: utf-8 -*-
"""
Common links between every pieces.
"""


class Piece():
    """
    Common links between every pieces.
    """

    def __init__(self, color, coords, Board):
        # To know the position of each pieces
        self.board = Board
        self.coords_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.coords_number = [str(x + 1) for x in range(8)]
        self.position = None
        self.name = None
        self.color = color
        # a list [x, y]
        self.coords = coords
        # The image of the piece
        self.image = None
        # For the movements of some piece
        self.minus8_to_8 = []
        for i in range(16):
            if i >= 8:
                self.minus8_to_8.append(i - 7)
            else:
                self.minus8_to_8.append(-8 + i)

        if self.color.color_name == "black":
            self.board.black_position.append(self.coords)
        else:
            self.board.white_position.append(self.coords)

    def __str__(self):
        return self.name
    def move(self, former_coord, next_coord):
        """Move the piece to the next position."""
        self.coords = next_coord
        for index, position in enumerate(self.board.white_position):
            print(former_coord, position)
            if former_coord == position:
                self.board.white_position[index] = next_coord
                print("Bonjour")
                break
        print(self.board.white_position)

    def moves_available(self):
        raise NotImplementedError()

