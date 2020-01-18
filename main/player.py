"""
Module designed to store data in player objects
"""
from util.color import Color


class Player():

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.elo = (...)
        self.current_game_score = (...)
                
    def __str__(self):
        return f"{self.name} (playing {self.color})"


Player.DEFAULT_1 = Player(Color.WHITE, "Player 1")
Player.DEFAULT_2 = Player(Color.BLACK, "Player 2")