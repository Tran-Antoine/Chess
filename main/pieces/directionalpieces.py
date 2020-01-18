# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:12:01 2019

@author: willi
"""
import pieces.gamepiece as gamepiece
import pieces.movedata as movedata
from util.vector import Vector2f
from typing import List


class DirectionalPiece(gamepiece.Piece):
    """
    Pieces that follow constant directional vectors to move, that have no
    distance limitations and that can't go through other pieces on their way.
    Directional pieces don't implement 'moves_available', instead they define
    a load_directions() method that returns the different directional vectors
    corresponding to the piece.
    """

    def __init__(self, color, position, name):
        super().__init__(color, position, name)
        self.directions = self.load_directions()

    def load_directions(self) -> List[Vector2f]:
        raise NotImplementedError()

    def moves_available(self, board) -> List[movedata.MoveData]:
        moves = []
        # to divide and move 1 case at once
        divisor = 8
        for dir_angle in self.directions:
            # The next case on which the piece will be
            next_destination = Vector2f(self.position.x + dir_angle.x, self.position.y + dir_angle.y)
            index = 0
            while index != divisor:
                # if the piece goes out of the board or if it is on another piece
                # stop the loop
                piece = board.piece_at_location(next_destination)
                if piece is not None and gamepiece.Piece.location_on_board(next_destination):
                    if piece.color != self.color:
                        moves.append(self.to_simple_move_data(next_destination))
                    break
                elif piece is None and gamepiece.Piece.location_on_board(next_destination):
                    moves.append(self.to_simple_move_data(next_destination))
                next_destination = Vector2f(next_destination.x + dir_angle.x, next_destination.y + dir_angle.y)
                index += 1
        return moves


class Queen(DirectionalPiece):
    """
    The queen piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "queen")

    def load_directions(self):
        return [Vector2f(1, 1), Vector2f(1, -1), Vector2f(-1, 1), Vector2f(-1, -1),
                Vector2f(0, 1), Vector2f(0, -1), Vector2f(1, 0), Vector2f(-1, 0)]


class Bishop(DirectionalPiece):
    """
    The bishop piece.
    """
    def __init__(self, color, position):
        super().__init__(color, position, "bishop")

    def load_directions(self):
        return [Vector2f(1, 1), Vector2f(-1, 1), Vector2f(-1, -1), Vector2f(1, -1)]


class Rook(DirectionalPiece):
    """
    The rook piece.
    """

    def __init__(self, color, position):
        super().__init__(color, position, "rook")
        # To know whether it can make the castling
        self.can_castle = True

    def load_directions(self):
        return [Vector2f(0, 1), Vector2f(0, -1), Vector2f(1, 0), Vector2f(-1, 0)]

    def moved(self):
        self.can_castle = False
