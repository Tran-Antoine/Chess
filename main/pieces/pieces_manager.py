from rendering.api import ChessUpdatePacket
from pieces.movedata import MoveData
from pieces.gamepiece import Piece
from util.vector import Vector2f
from typing import Tuple, List


class ImaginaryBoard():

    def __init__(self, player1, player2):
        self.players = player1, player2
        self.position_letter = 'ABCDEFGH'
        self.pieces = self.load_pieces()

    def load_pieces(self) -> List[Piece]:
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

    def piece_at_location(self, loc: Vector2f) -> Piece:
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

    def move_players_pieces(self, tiles_modification):
        for piece in self.pieces:
            if piece.position in tiles_modification.keys():
                piece.position = tiles_modification[piece.position]

    @staticmethod
    def find_matching_move(destination, moves) -> MoveData:
        for move in moves:
            if move.destination == destination:
                return move
        return None

    def process_move(self, former_position: Vector2f, next_position: Vector2f):
        """
        return the change on the board
        """
        target = self.piece_at_location(former_position)

        if target is None:
            return ChessUpdatePacket.INVALID

        moves_available = target.moves_available(self)
        current_move = ImaginaryBoard.find_matching_move(next_position, moves_available)

        if current_move is None:  # meaning that the requested move was 'illegal'
            return ChessUpdatePacket.INVALID

        changes = current_move.changes
        for piece in self.pieces:
            if piece.position in changes.keys():
                piece.position = changes[piece.position]

        return ChessUpdatePacket(changes)

    @staticmethod
    def location_on_board(loc):
        """
        Verify if the position is on the board, i.e > 0 and < 8
        """
        if 0 <= loc.x <= 7 and 0 <= loc.y <= 7:
            return True
        return False

    def analyse_path(self, start: Vector2f, end: Vector2f) -> Tuple[bool, Vector2f]:
        direction = (end - start).normalize()
        current_pos = start + direction

        while current_pos != end:
            if self.piece_at_location(current_pos) is not None:
                return False, direction
            current_pos += direction
        return True, direction
