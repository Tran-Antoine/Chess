from rendering import board, api, renderers
from logic import gamelogic
from player import Player


class ChessGame():

    def __init__(self, player1=Player.DEFAULT_1, player2=Player.DEFAULT_2):
        self.player1 = player1
        self.player2 = player2
        self.render_board = board.ChessBoard(renderers.TkinterRenderer())
        self.logic = gamelogic.GameLogic(player1, player2)

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
