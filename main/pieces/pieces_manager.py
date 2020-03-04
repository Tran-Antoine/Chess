from rendering.api import ChessUpdatePacket
from pieces.movedata import MoveData
from pieces.gamepiece import Piece
from pieces import pawn, knight, king
from pieces import directionalpieces as dp
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

    PIECES_TYPE = [dp.Rook, knight.Knight, dp.Bishop, dp.Queen,
                   king.King, dp.Bishop, knight.Knight, dp.Rook]
    
    ID_MAP = {id:piece for id, piece in zip(("R", "Kn", "B", "Q", "Ki", "P"), PIECES_TYPE + [pawn.Pawn])}

    def __init__(self, *colors):
        self.colors = colors
        self.pieces = self._load_pieces()
        self.pending_todelete_pawn = None
        self.pending_color = None

    def _load_pieces(self) -> List[Piece]:
        """
        Loads the pieces. The board makes no distinction between
        the pieces, black and white ones are both put in a single list.
        """
        pieces = []
        for color, front_row_index, back_row_index in zip(self.colors, (1, 6), (0, 7)):
            for x_index in range(8):
                pieces.append(pawn.Pawn(color, Vector2f(x_index, front_row_index)))
                pieces.append(ImaginaryBoard.PIECES_TYPE[x_index](color, Vector2f(x_index, back_row_index)))
        return pieces

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

    def get_by_name(self, name, color=None):
        pieces = []
        for piece in self.pieces:
            if piece.name == name and (color is None or piece.color == color):
                pieces.append(piece)
        return pieces

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

    def process_move(self, former_position: Vector2f, next_position: Vector2f, color):
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

        if target is None or target.color != color:
            return ChessUpdatePacket.INVALID, False

        moves_available = target.absolute_moves_available(self)
        current_move = ImaginaryBoard.find_matching_move(next_position, moves_available)

        if current_move is None:  # meaning that the requested move was 'illegal'
            return ChessUpdatePacket.INVALID, False

        changes = current_move.changes
        
        _, requires_extra_piece = self._move_pieces(changes, real_move=True)
        print(requires_extra_piece)
        return ChessUpdatePacket(changes), requires_extra_piece

    def is_safe_for_king(self, king_color, board_movements):
        canceller = self._move_pieces(board_movements, real_move=False)
        target_king, = self.get_by_name("king", king_color)
        king_attacked = self.is_king_attacked(target_king)
        self._cancel_move(canceller)
        return not king_attacked

    def is_king_attacked(self, target_king):
        # all_destinations instead of all_absolute_destinations.
        # for instance, the king cannot go to a "danger tile",
        # EVEN if the attacking piece is "stuck" because it protects its king
        # Besides, all_absolute_destination would cause a recursion error.
        danger_tiles = self.all_destinations(target_king.color, color_inverted=True)
        return target_king.position in danger_tiles

    def all_destinations(self, color, color_inverted=False):
        return self._all_destinations(color, color_inverted, lambda piece: piece.moves_available(self))

    def all_absolute_destinations(self, color, color_inverted=False):
        return self._all_destinations(color, color_inverted, lambda piece: piece.absolute_moves_available(self))

    def _all_destinations(self, color, color_inverted, moves_func):
        color_test = (lambda c: c == color) if not color_inverted else (lambda c: c != color)
        destinations = []
        for piece in self.pieces:
            if not color_test(piece.color):
                continue
            destinations += list(map(lambda m: m.destination, moves_func(piece)))
        return destinations

    def _move_pieces(self, changes, real_move=True):
        """
        Moves the pieces handled by the board according to the changes.
        This method is handled by the board itself, and should thus not
        be called from outside this class.
        Returns a dictionary that can be used to cancel the changes, in case
        of a simulated movement
        """
        extra_piece_required = False
        reverse = {}
        for piece in self.pieces:
            if piece.position not in changes.keys():
                continue
            
            reverse[piece] = piece.position
            piece.position = changes[piece.position]
            
            if real_move:
                result = piece.moved()
                if (result is not None) and result:
                    extra_piece_required = result
                    self.pending_todelete_pawn = piece
                
        if real_move:
            return reverse, extra_piece_required
        return reverse
    
    def add_extra_piece(self, id):
        assert self.pending_todelete_pawn is not None
        
        new_piece = ID_MAP[id](self.pending_todelete_pawn.color, self.pending_todelete_pawn.position)
        pawn = self.pending_todelete_pawn
        changes = {pawn.position, Vector2f.DESTROY}
        
        pawn.position = Vector2f.DESTROY
        self.pieces.append(new_piece)
        self.pending_todelete_pawn = None
        
        return ChessPacket(changes, new_piece=new_piece)  # todo, convert the game piece to a renderable piece

    def _cancel_move(self, canceller):
        for piece in self.pieces:
            if piece in canceller.keys():
                piece.position = canceller[piece]

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
