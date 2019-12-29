# -*- coding: utf-8 -*-
"""
get the position of every pieces.
"""
from rendering.api import ChessUpdatePacket


class ImaginaryBoard():
    """
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = self.player1, self.player2
        self.position_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]

        self.pieces = self.load_pieces()

    def load_pieces(self):
        self.pieces_loaded = []
        for player in self.players:
            for piece in player.pieces:
                self.pieces_loaded.append(piece)
        return self.pieces_loaded

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

    def get_rooks(self, color):
        self.rooks = []
        for piece in self.pieces:
            if piece.name == "rook" and piece.color == color:
                self.rooks.append(piece)
        return self.rooks

    def make_castle(self, distance_rook_king, rook_moved, next_pos, piece):
        """
        Move the king and the rook, so they make a castle.
        """
        piece.position = next_pos
        self.rooks = self.get_rooks(piece.color)
        for rook in self.rooks:
            if rook.position[0] + distance_rook_king == piece.position[0]:
                rook.position = [rook.position[0] + rook_moved, rook.position[1]]
                rook.can_castle = False

    def to_packet(self, former_position, next_position):
        """
        return the change on the board
        """
        self.tiles_modification = {}
        self.tiles_modification[former_position] = next_position
        for piece in self.pieces:
            if piece.position == next_position:
                self.tiles_modification[piece.position] = [-1, -1]
        return ChessUpdatePacket(self.tiles_modification)