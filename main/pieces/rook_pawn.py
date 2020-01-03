# -*- coding: utf-8 -*-
"""
The tower and the pawn.
"""
import pieces.common_pieces as cp
import pieces.move_bishop_queen_rook as bqr
from util.vector import Vector2f

class Pawn(cp.Piece):
    """
    The pawn piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "pawn")
        # To know whether it can move two cases or only one
        self.alreadyMoved = False

    def moves_available(self, board):
        """
        How the piece moves.
        """
        self.moves = []
        factor = 1 if self.color.color_name == 'white' else -1
        # When it is the first time the pawn moves, it can moves 2 cases
        if board.piece_at_location(Vector2f(self.position.x, self.position.y + factor)) is None:
            self.moves.append(Vector2f(self.position.x, self.position.y + factor))
            if not self.alreadyMoved and board.piece_at_location(Vector2f(self.position.x, self.position.y + 2*factor)) is None:
                self.moves.append(Vector2f(self.position.x, self.position.y + 2*factor))
                
        self.can_eat(board)
        return self.moves

    def move(self, former_position, next_position, board):
        """
        Move the piece to the next position. This method must be called from
        outside of the class.
        """
        super().move(former_position, next_position, board)
        self.alreadyMoved = True

    def can_eat(self, board):
        """
        Verify if there is an adverse piece that can be eaten.
        """
        self.can_go = []
        if self.color.color_name == "black":
            self.diagonal_left = Vector2f(self.position.x - 1, self.position.y - 1)
            self.diagonal_right = Vector2f(self.position.x + 1, self.position.y - 1)
        elif self.color.color_name == "white":
            self.diagonal_left = Vector2f(self.position.x - 1, self.position.y + 1)
            self.diagonal_right = Vector2f(self.position.x + 1, self.position.y + 1)
            
        self.can_go.append(board.piece_at_location(self.diagonal_left))
        self.can_go.append(board.piece_at_location(self.diagonal_right))
        for piece in self.can_go:
            if piece is not None:
                if piece.color != self.color:
                    self.moves.append(piece.position)

    def transform(self):
        """
        Transform the piece into another when it reaches the end of the board.
        """
        if self.color.color_name == "white" and self.position.y == 8:
            print("TRANSFORMATION DES RENOIS!!!")
        if self.color.color_name == "black" and self.position.y == 8:
            print("TRANSFORMATION DES COLONS!!!")

class Rook(bqr.DirectionalPiece):
    """
    The rook piece.
    """

    def __init__(self, color, position):
        self.one_case_list = [Vector2f(0, 1), Vector2f(0, -1), Vector2f(1, 0), Vector2f(-1, 0)]
        super().__init__(color, position, "rook")
        # To know whether it can make the castling
        self.can_castle = True

    def move(self, former_position, next_position, board):
        super().move(former_position, next_position, board)
        self.can_castle = False
