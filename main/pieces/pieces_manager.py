# -*- coding: utf-8 -*-
"""
get the position of every pieces.
"""
from rendering.api import ChessUpdatePacket
from util.vector import Vector2f


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

    def make_castle(self, delta_x, next_pos, piece):
        """
        Move the king and the rook, so they make a castle.
        """
        self.tiles_modification[Vector2f(piece.position[0], piece.position[1])] = Vector2f(next_pos[0], next_pos[1])

        if delta_x == 1:
            pass
        elif delta_x > 2:
            piece.can_castle = False
            for rook in self.get_rooks:
                if piece.position[0] - rook.position[0] == 4:
                    self.tiles_modification[Vector2f(rook.position[0], rook.position[1])] = Vector2f(rook.position[0] + 3, rook.position[1])
                    rook.can_castle = False
        elif delta_x < 2:
            piece.can_castle = False
            for rook in self.get_rooks:
                if piece.position[0] - rook.position[0] == 3:
                    self.tiles_modification[Vector2f(rook.position[0], rook.position[1])] = Vector2f(rook.position[0] - 2, rook.position[1])
                    rook.can_castle = False

    def is_valid(self, former_position, next_position):
        """
        Verify if the piece can move to the given location.
        """
        for piece in self.pieces:
            if piece.position == former_position and next_position in piece.moves_available(self):
                return True
        return False

    def to_packet(self, former_position, next_position):
        """
        return the change on the board
        """
        self.tiles_modification = {}
        if self.is_valid(former_position, next_position):
            self.initial_vector = Vector2f(former_position[0], former_position[1])
            self.tiles_modification[self.initial_vector] = Vector2f(next_position[0], next_position[1])
            for piece in self.pieces:
                if piece.position == next_position and piece.name == "king":
                    self.delta_x = piece.position[0] - next_position[0]
                    self.make_castle(self.delta_x, next_position, piece)
                elif piece.position == next_position:
                    self.tiles_modification[Vector2f(piece.position[0], piece.position[1])] = Vector2f(-1, -1)
        return ChessUpdatePacket(self.tiles_modification)