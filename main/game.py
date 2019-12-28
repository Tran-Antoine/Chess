from logic import gamelogic
from rendering import board, api, renderers
from player import Player
from pieces.pieces_position import ImaginaryBoard

class ChessGame():

    def __init__(self):
        self.logic = gamelogic.GameLogic()
        self.board = board.ChessBoard(renderers.ConsoleRenderer())
        self.player1 = Player.DEFAULT_1
        self.player2 = Player.DEFAULT_2

        self.imaginary_board = ImaginaryBoard(self.player1, self.player2)

    def set_players(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        
    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        #self.start_test()
        self.board.show()
        self._test_input() # uncomment this to test the rendering system


    def start_test(self):
        """
        The following code is for testing only.
        """
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
                        print("ICI")
                        piece.move(self.former_position, self.next_position, self.imaginary_board)
                        print(f"{piece} est bien allé en {self.next}")
                        self.moved = True
                        break
                if not self.moved:
                    print("Entrée invalide, réessayez.")
            self.answer = input("Veuillez la case sur laquelle la pièce va bouger: """)

    def _test_input(self):
        """
        The following code is for testing only.
        This input parser has nothing to do here, and is totally incomplete
        """
        move = input("Enter your next move, 'stop' to interrupt the program\n")
        
        while move != 'stop':
            try:
                target, destination = move.upper().split()
                conversion = lambda letter: 'ABCDEFGH'.index(letter)
                initial_position = (conversion(target[0]), int(target[1])-1)
                final_position = (conversion(destination[0]), int(destination[1])-1)
                # print(f"Input successfully translated : Player wants to move {initial_position} to {final_position}")
                packet = api.ChessUpdatePacket({initial_position: final_position})
                self.board.update(packet)
            except ValueError:
                print("Invalid input, try again")
            finally:
                move = input("Enter your next move, 'stop' to interrupt the program\n")