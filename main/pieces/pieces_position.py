# -*- coding: utf-8 -*-
"""
get the position of every pieces.
"""


class ImaginaryBoard():
    """
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = self.player1, self.player2
        self.position_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]

        self.white_position = []
        self.black_position = []
        self.all_pieces()

    def all_pieces(self):
        self.pieces = []
        for player in self.players:
            for piece in player.pieces:
                if player.color.color_name == "white":
                    self.white_position.append(piece.position)
                else:
                    self.black_position.append(piece.position)
                self.pieces.append(piece)

    def canMove(self):
        """
        Verify if the piece can move to a case.
        """