from rendering import board, api, renderers
from logic import gamelogic
from player import Player
from pieces.pieces_manager import ImaginaryBoard
import util.vector as vector

class ChessGame():

    def __init__(self, player1=Player.DEFAULT_1, player2=Player.DEFAULT_2):
        self.player1 = player1
        self.player2 = player2
        self.board = board.ChessBoard(renderers.ConsoleRenderer())
        self.logic = gamelogic.GameLogic(player1, player2)
        self.imaginary_board = ImaginaryBoard(player1, player2)
 
    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        self.start_test()
        # self.board.show()
        # while True: 
            # packet = self.logic.play_turn()
            # # Usage of 'is' instead of '=='. We want to check if the instance is the same, not if the two packets are equivalent
            # if packet is api.ChessUpdatePacket.STOP:
                # break
            # self.board.update(packet)


    def start_test(self):
        """
        The following code is for testing only.
        """
        # sorry for the french usage. I was against it :( I told him to stop but he won't 
        self.answer = input("Veuillez la case sur laquelle la pièce va bouger: """)
        while self.answer != "q":
            if len(self.answer.split(" ")) == 1:
                for piece in self.imaginary_board.pieces:
                    self.position = [int(self.imaginary_board.position_letter.index(self.answer[0].upper()) + 1), int(self.answer[1])]

                    if self.position == piece.position:
                        print(piece)
                        print(f"position: {self.imaginary_board.position_letter[piece.position[0] - 1]}{piece.position[1]}")
                        print(f"mouvements possibles: {piece.moves_available(self.imaginary_board)}")
            else:
                self.moved = False
                self.before, self.next = self.answer.upper().split(" ") 
                self.former_position = [int(self.imaginary_board.position_letter.index(self.before[0]) + 1), int(self.before[1])]
                self.next_position = [int(self.imaginary_board.position_letter.index(self.next[0]) + 1), int(self.next[1])]
                for piece in self.imaginary_board.pieces:
                    if piece.position == self.former_position and self.next_position in piece.moves_available(self.imaginary_board):
                        piece.move(self.former_position, self.next_position, self.imaginary_board)
                        print(f"{piece} est bien allé en {self.next}")
                        self.moved = True
                        break
                if not self.moved:
                    print("Entrée invalide, réessayez.")
            self.answer = input("Veuillez la case sur laquelle la pièce va bouger: """)
