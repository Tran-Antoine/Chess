# -*- coding: utf-8 -*-
"""
The king and the queen.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_rook as bqr
import numpy as np

class King(cp.Piece):
    """
    The king piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "king")
        # To know whether it can make the castling or not.
        self.can_castle = True

    def moves_available(self, board):
        """
        The moves executable by the king
        """
        self.moves = []
        for i in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                self.next = [self.position[0] + i, self.position[1] + l]
                # verify if the next location is on the board and if it can goes there
                if self.location_on_board(self.next) and board.can_move_at_location(self.next, self.color):
                    self.moves.append(self.next)

        # To check if the king can castle with the rooks
        for piece in board.get_rooks(self.color):
            self.castling(piece, board)
        return self.moves

    def move(self, former_position, next_position, board):
        for index, piece in enumerate(board.pieces):
            # To know if the king is doing a castle
            self.delta_x = piece.position[0] - next_position[0]
            # small castle
            if former_position == piece.position and self.delta_x == -2:
                board.make_castle(-1, -2, next_position, piece)
            # big castle
            elif former_position == piece.position and self.delta_x == 2:
                board.make_castle(2, 3, next_position, piece)
            # normal move
            elif former_position == piece.position:
                piece.position = next_position
        self.can_castle = False

    def castling(self, other, board):
        """
        Le roque in french.
        """
        self.delta_x = self.position[0] - other.position[0]
        if self.can_castle and other.can_castle and self.delta_x < 0:
            # Small castling
            self.next_case = 1
            self.is_obstructing_castling(board, self.next_case)
            if self.distance_king_rook == 2:
                self.moves.append([self.position[0] + 2, self.position[1]])
                print("small castle")

        elif self.can_castle and other.can_castle and self.delta_x > 0:
            # Big castling
            self.next_case = -1
            self.is_obstructing_castling(board, self.next_case)
            if self.distance_king_rook == 3:
                self.moves.append([self.position[0] - 2, self.position[1]])
                print("Big castle")

    def is_obstructing_castling(self, board, next_case):
        """
        Verify if there are pieces between the rook and the king in order
        to castle.
        """
        self.distance_king_rook = 0
        self.next_position = [self.position[0] + next_case, self.position[1]]
        while True:
            if board.piece_at_location(self.next_position) is None:
                self.distance_king_rook += 1
                self.next_position[0] += next_case
            else:
                break


class Queen(bqr.DirectionalPiece):
    """
    The queen piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [[1, 1], [1, -1], [-1, 1], [-1, -1],
                              [0, 1], [0, -1], [1, 0], [-1, 0]]
        super().__init__(color, position, "queen")
