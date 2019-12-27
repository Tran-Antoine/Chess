# -*- coding: utf-8 -*-
"""
Common links between every pieces.
"""


class Piece():
    """
    Common links between every pieces.
    """

    def __init__(self, color, coords):
        self.coords_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.coords_number = [str(x + 1) for x in range(8)]
        self.position = None
        self.color = color
        # a list [x, y]
        self.coords = coords
        # The image of the piece
        self.image = None

    def move(self):
        pass


    def moves_available(self):
        pass

