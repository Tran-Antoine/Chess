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
        self.first_move = False

    def moves_available(self, board):
        """
        How the piece moves.
        """
        moves = []
        self.add_regular_moves(board, moves)
        self.add_taking_moves(board, moves)
        return list(map(lambda vec: self.to_simple_move_data(vec), moves))
    
    def add_regular_moves(self, board, moves):
        direction = Vector2f(0, 1) if self.color.color_name == 'white' else Vector2f(0, -1)
        can_go_forward = self.add_if_empty(board, moves, self.position + direction)
        # When it is the first time the pawn moves, it can moves 2 cases
        if can_go_forward and not self.already_moved:
            self.add_if_empty(board, moves, self.position + direction.scalar_mult(2))

    def add_if_empty(self, board, moves, destination):
        if board.piece_at_location(destination) is None:
            moves.append(destination)
            return True
        return False
        
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
                    moves.append(piece.position)

    def moved(self):
        self.already_moved = True
        # todo : give the user the choice for the piece
        return self.position.y in (0, 7)
