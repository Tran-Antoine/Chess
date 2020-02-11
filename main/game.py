from rendering import board, api, renderers
from logic import gamelogic
from player import Player
from pieces.pieces_manager import ImaginaryBoard
import util.vector as vector


class ChessGame():

    VIEW = [renderers.ConsoleRenderer, renderers.FrameTkinterRenderer, renderers.CanvasTkinterRenderer]

    def __init__(self, player1=Player.DEFAULT_1, player2=Player.DEFAULT_2):
        # To choose which view the user wants.
        chosen_interface = int(input("Choose between ConsoleRenderer (1), FrameTkinterRenderer (2) or CanvasTkinterRenderer (3)"))
        self.player1 = player1
        self.player2 = player2
        # Save the renderer, so we can use it in the inputparser for the canvas
        self.renderer = self.VIEW[chosen_interface - 1]()
        self.render_board = board.ChessBoard(self.renderer)
        self.logic = gamelogic.GameLogic(player1, player2, chosen_interface, self.renderer)
        self.imaginary_board = ImaginaryBoard(player1, player2)

    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        self.render_board.show()
        while True:
            packet = self.logic.play_turn()
            # Usage of 'is' instead of '=='. We want to check
            # if the instance is the same, not if the two packets are equivalent
            if packet is api.ChessUpdatePacket.STOP:
                break
            self.render_board.update(packet)
