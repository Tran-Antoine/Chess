# -*- coding: utf-8 -*-
"""
Manage the interactions between the two players.
"""
class PlayerManager():
    """
    Manage the interactions between the two players.
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def gameState(self):
        """
        Verify if one player is check/checkmate or if both cannot move.
        """