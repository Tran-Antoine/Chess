# -*- coding: utf-8 -*-
"""
File which creates the players.
"""
# todo : have the pieces module import work
import pieces.king_queen as kq
import pieces.knight_bishop as kb
import pieces.rook_pawn as rp


class Player():
    """
    Initialize the player.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.set_piece()        

    def set_piece(self):
        """
        Set the pieces on their location on the board
        """
        self.pieces_order = [rp.Rook, kb.Knight, kb.Bishop, kq.Queen,
                             kq.King, kb.Bishop, kb.Knight, rp.Rook]
        self.pieces = []
        if self.color == self.color.WHITE:
            for index in range(8):
                self.pieces.append(rp.Pawn(self.color, [index + 1, 2]))
                self.pieces.append(self.pieces_order[index](self.color, [index + 1, 1]))
        else:
            for index in range(8):
                self.pieces.append(rp.Pawn(self.color, [index + 1, 7]))
                self.pieces.append(self.pieces_order[index](self.color, [index + 1, 8]))

                
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