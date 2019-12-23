# -*- coding: utf-8 -*-
"""
Common links between every pieces.
"""


class Piece():
    """
    Common links between every pieces.
    """

    def __init__(self, color):
        self.position = None
        self.color = color
        # The image of the piece
        self.image = None

    def eat(self):
        """
        How the piece eats.
        """

