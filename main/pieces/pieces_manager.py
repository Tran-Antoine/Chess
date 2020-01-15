from rendering.api import ChessUpdatePacket
from pieces.movedata import MoveData
from pieces.gamepiece import Piece
from util.vector import Vector2f
from typing import Tuple, List, Optional


class ImaginaryBoard():
    """
    An imaginary representation of a chess board.
    ImaginaryBoard handles a list of pieces, and is often given to the latter
    to determine which moves are available. It also contains a few util
    methods, to retrieve pieces from their locations, to analyse the path
    between two pieces, and so on.
    More importantly, the imaginary board handles the overall movements
    happening on the board. Once the parser has given the requested move
    to it, it asks the targeted piece whether the move is 'legal' chesswise
    or not. If it is, based from the modifications list provided by the
    piece, the board will move every piece involved to their destination.
    """
    def __init__(self, player1, player2):
        self.players = player1, player2
        self.pieces = self._load_pieces()

    def _load_pieces(self) -> List[Piece]:
        """
        Loads the pieces from the players. Each player handles their own
        pieces set. However, the board makes no distinction between
        the pieces, black and white ones are both put in a single list.
        """
        pieces_loaded = []
        for player in self.players:
            for piece in player.pieces:
                pieces_loaded.append(piece)
        return pieces_loaded

    def can_move_at_location(self, loc: Vector2f, color):
        """
        Return true if the piece at the location given is of the same color
        as the argument given
        """
        for piece in self.pieces:
            if piece.position == loc and piece.color == color:
                return False
        return True

    def piece_at_location(self, loc: Vector2f) -> Optional[Piece]:
        """
        Retrieves the piece from the board located at the given coordinates.
        If the targeted tile is empty, returns None
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

    @staticmethod
    def find_matching_move(destination: Vector2f, moves: List[MoveData]) -> Optional[MoveData]:
        """
        Static util method returning one element from the list, whose
        destination matches the given one. If no element is suitable,
        returns None.
        """
        for move in moves:
            if move.destination == destination:
                return move
        return None

    def process_move(self, former_position: Vector2f, next_position: Vector2f):
        """
        Analyses the requested move from the player, and
        depending on the result of the analysis, processes the required
        actions on the targeted pieces. Basically, the analysis checks
        whether the move from the player is legal, according to the chess
        rules. Beforehand, it will check if the player actually targets
        a piece, and stops if they don't.
        Once the move is checked and if accepted, the board will move
        the required pieces to their destination. Eventually, the changes
        will be returned, since they're required by the renderer.
        """
        target = self.piece_at_location(former_position)

        if target is None:
            return ChessUpdatePacket.INVALID

        moves_available = target.moves_available(self)
        current_move = ImaginaryBoard.find_matching_move(next_position, moves_available)

        if current_move is None:  # meaning that the requested move was 'illegal'
            return ChessUpdatePacket.INVALID

        changes = current_move.changes
        self._move_pieces(changes)
        return ChessUpdatePacket(changes)

    def _move_pieces(self, changes):
        """
        Moves the pieces handled by the board according to the changes.
        This method is handled by the board itself, and should thus not
        be called from outside this class
        """
        for piece in self.pieces:
            if piece.position in changes.keys():
                piece.moved()
                piece.position = changes[piece.position]

    @staticmethod
    def location_on_board(loc: Vector2f):
        """
        Checks whether the position is on the board.
        Coordinates are considered 'on the board' if both
        their components are between 1 and 7 included.
        """
        return 0 <= loc.x <= 7 and 0 <= loc.y <= 7

    def analyse_path(self, start: Vector2f, end: Vector2f) -> Tuple[bool, Vector2f]:
        """
        Analyses what happens from the 'start' vector to the 'end' vector.
        The analysis returns two pieces of information. First, whether the path
        from 'start' to 'end' is clean, meaning that there is no chess piece
        on the way. Second, the directional vector used to reach 'end' from
        'start'. The directional vector's components are either -1, 0, or 1.
        """
        direction = (end - start).normalize()
        current_pos = start + direction

        while current_pos != end:
            if self.piece_at_location(current_pos) is not None:
                return False, direction
            current_pos += direction
        return True, direction
