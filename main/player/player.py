# -*- coding: utf-8 -*-
"""
File which creates the players.
"""
# todo : have the pieces module import work

class Player():
    """
    Initialize the player.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.pieces = []
    
    def __str__(self):
        return f"{self.name} (playing {self.color})"

class Color():
    
    def __init__(self, color_name):
        self.color_name = color_name
        
    def __str__(self):
        return self.color_name
        

# default constants
Color.WHITE = Color("white")
Color.BLACK = Color("black")

Player.DEFAULT_1 = Player(Color.WHITE, "Player 1")
Player.DEFAULT_2 = Player(Color.BLACK, "Player 2")