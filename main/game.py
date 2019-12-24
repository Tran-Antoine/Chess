from logic import gamelogic
from rendering import board
from player import Player

class ChessGame():

    def __init__(self):
        self.logic = gamelogic.GameLogic()
        self.board = board.ChessBoard()
        self.player1 = Player.DEFAULT_1
        self.player2 = Player.DEFAULT_2
        
    def set_players(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        
    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        self.board.show()