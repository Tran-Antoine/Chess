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
        self.players = player1, player2
        self.position_letter = 'ABCDEFGH'
        self.pieces = self.load_pieces()

    def load_pieces(self):
        pieces_loaded = []
        for player in self.players:
            for piece in player.pieces:
                pieces_loaded.append(piece)
        return pieces_loaded

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
        rooks = []
        for piece in self.pieces:
            if piece.name == "rook" and piece.color == color:
                rooks.append(piece)
        return rooks

    def castle(self, delta_x, king, tiles_modification):
        """
        Move the king and the rook, so they make a castle.
        """
        if delta_x == 2:
            king.can_castle = False
            for rook in self.get_rooks(king.color):
                if king.position.x - rook.position.x == 4:
                    tiles_modification[rook.position] = Vector2f(rook.position.x + 3, rook.position.y)
                    rook.can_castle = False
        elif delta_x == -2:
            king.can_castle = False
            for rook in self.get_rooks(king.color):
                if king.position.x - rook.position.x == -3:
                    tiles_modification[rook.position] = Vector2f(rook.position.x - 2, rook.position.y)
                    rook.can_castle = False

    def is_valid(self, former_position, next_position):
        """
        Verify if the piece can move to the given location.
        """
        for piece in self.pieces:
            if piece.position == former_position and next_position in piece.moves_available(self):
                return True
        return False

    def move_players_pieces(self, tiles_modification):
        """
        """
        for piece in self.pieces:
            if piece.position in tiles_modification.keys():
                piece.position = tiles_modification[piece.position]

    def process_move(self, former_position, next_position):
        """
        return the change on the board
        """
        tiles_modification = {}
        if self.is_valid(former_position, next_position):
            initial_vector = Vector2f(former_position.x, former_position.y)
            tiles_modification[initial_vector] = next_position
            for piece in self.pieces:
                if piece.position == former_position and piece.name == "king":
                    delta_x = piece.position.x - next_position.x
                    self.castle(delta_x, piece, tiles_modification)
                elif piece.position == next_position:
                    tiles_modification[piece.position] = Vector2f(-1, -1)
            self.move_players_pieces(tiles_modification)
        return ChessUpdatePacket(tiles_modification)

    def location_on_board(self, loc):
        """
        Verify if the position is on the board, i.e > 0 and < 8
        """
        if 0 <= loc.x <= 7 and 0 <= loc.y <= 7:
            return True
        return False
