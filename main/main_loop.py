# -*- coding: utf-8 -*-
"""
Main file to launch the game.
"""
from game import ChessGame

chosen_interface = int(input("Choose between ConsoleRenderer (1), " +
                             "FrameTkinterRenderer (2) or CanvasTkinterRenderer (3) >>>"))
chess_game = ChessGame(chosen_interface)
chess_game.start()
