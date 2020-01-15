class Piece():
    """
    Common links between every piece.
    """

    def __init__(self, color, position, name):
        self.position_number = [str(x + 1) for x in range(8)]
        self.position = position
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def moves_available(self, board):
        raise NotImplementedError()

