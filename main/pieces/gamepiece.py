import pieces.movedata as movedata
import util.vector as vector
from typing import List


class Piece():
    """
    Common links between every piece.
    """

    def __init__(self, color, position, name):
        self.position = position
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def to_simple_move_data(self, next_destination: vector.Vector2f) -> movedata.MoveData:
        changes = {self.position: next_destination, next_destination: vector.Vector2f(-1, -1)}
        return movedata.MoveData(next_destination, changes)

    def moves_available(self, board) -> List[movedata.MoveData]:
        raise NotImplementedError()

