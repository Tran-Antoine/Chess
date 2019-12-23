# -*- coding: utf-8 -*-
"""
File which creates the players.
"""
import piece_manager as pm
import pieces as p


class Player():
    """
    Initialize the player.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.pieces = []
        # To know whether the player wins or not
        self.canMove = True
