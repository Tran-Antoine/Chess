# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import pieces.gamepiece as gamepiece
from util.vector import Vector2f


class Pawn(gamepiece.Piece):
    """
    The pawn piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "pawn")
        # To know whether it can move two cases or only one
        self.already_moved = False
        # To know whether it can be taken by the en passant
        self.first_move = False

    def moves_available(self, board):
        """
        How the piece moves.
        """
        moves = []
        factor = 1 if self.color.color_name == 'white' else -1
        # When it is the first time the pawn moves, it can moves 2 cases
        if board.piece_at_location(Vector2f(self.position.x, self.position.y + factor)) is None:
            moves.append(self.to_simple_move_data(Vector2f(self.position.x, self.position.y + factor)))
            if not self.already_moved and board.piece_at_location(Vector2f(self.position.x, self.position.y + 2 * factor)) is None:
                moves.append(self.to_simple_move_data(Vector2f(self.position.x, self.position.y + 2*factor)))
                
        self.add_taking_moves(board, moves)
        return moves

    def add_taking_moves(self, board, moves):
        """
        Verify if there is an adverse piece that can be taken.
        """
        can_go = []

        factor = -1 if self.color.color_name == "black" else 1
        diagonal_left = Vector2f(self.position.x - 1, self.position.y + factor)
        diagonal_right = Vector2f(self.position.x + 1, self.position.y + factor)
            
        can_go.append(board.piece_at_location(diagonal_left))
        can_go.append(board.piece_at_location(diagonal_right))
        for piece in can_go:
            if piece is not None:
                if piece.color != self.color:
                    moves.append(self.to_simple_move_data(piece.position))

    def moved(self):
        self.already_moved = True
