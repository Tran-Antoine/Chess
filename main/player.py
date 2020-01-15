# -*- coding: utf-8 -*-
"""
File which creates the players.
"""
from util.vector import Vector2f
import pieces.directionalpieces as dp
import pieces.king as king
import pieces.knight as knight
import pieces.pawn as pawn


class Player():
    """
    Initialize the player.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.pieces = self.load_pieces()

    def load_pieces(self):
        """
        Set the pieces on their location on the board
        """
        pieces_order = [dp.Rook, knight.Knight, dp.Bishop, dp.Queen,
                        king.King, dp.Bishop, knight.Knight, dp.Rook]
        pieces = []
        if self.color == self.color.WHITE:
            for index in range(8):
                pieces.append(pawn.Pawn(self.color, Vector2f(index, 1)))
                pieces.append(pieces_order[index](self.color, Vector2f(index, 0)))
        else:
            for index in range(8):
                pieces.append(pawn.Pawn(self.color, Vector2f(index, 6)))
                pieces.append(pieces_order[index](self.color, Vector2f(index, 7)))
        return pieces
                
    def __str__(self):
        return f"{self.name} (playing {self.color})"


class Color():
    
    def __init__(self, color_name):
        self.color_name = color_name
        
    def __str__(self):
        return self.color_name

    def __eq__(self, other):
        return self.color_name == other.color_name


# default constants
Color.WHITE = Color("white")
Color.BLACK = Color("black")

Player.DEFAULT_1 = Player(Color.WHITE, "Player 1")
Player.DEFAULT_2 = Player(Color.BLACK, "Player 2")