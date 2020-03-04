from rendering import board, api, renderers
from logic import gamelogic
from player import Player


class ChessGame():

    VIEW = [renderers.ConsoleRenderer, renderers.FrameTkinterRenderer, renderers.CanvasTkinterRenderer]

    def __init__(self, chosen_interface, player1=Player.DEFAULT_1, player2=Player.DEFAULT_2):
        # To choose which view the user wants.
        self.player1 = player1
        self.player2 = player2
        # Save the renderer, so we can use it in the inputparser for the canvas
        self.renderer = self.VIEW[chosen_interface - 1]()
        self.render_board = board.ChessBoard(self.renderer)
        # Initialize the canvas/frame/console renderer
        self.render_board.show()
        self.logic = gamelogic.GameLogic(player1, player2, chosen_interface, self.renderer)

    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        self.render_board.show()
        while not self.logic.ended:
            packet, extra_piece_required = self.logic.play_turn()
            # Usage of 'is' instead of '=='. We want to check if the instance is the same, not if the two packets are equivalent
            if packet is api.ChessUpdatePacket.STOP:
                break
            self.render_board.update(packet)
            
            if extra_piece_required:
                additional_packet = self.logic.add_extra_piece()
                print("Successfully got extra piece")
                self.render_board.update(additional_packet)

        winner = self.logic.winner
        if winner is None:
            print("Game ended in a draw")
        else:
            print(f"{winner.name} won!")
