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

        self.all_pieces()

    def all_pieces(self):
        self.pieces = []
        for player in self.players:
            for piece in player.pieces:
                self.pieces.append(piece)

    def can_move_at_location(self, loc, color):
        """
        Return true if the piece at the location given is of the same color
        as the argument given
        """
        for piece in self.pieces:
            if piece.position == loc and piece.color == color:
                return False
        return True

    def piece_at_location(self, loc):
        """
        Get the piece at a given location.
        """
        for piece in self.pieces:
            if piece.position == loc:
                return piece
        return None
        

    def canMove(self):
        """
        Verify if the piece can move to a case.
        """