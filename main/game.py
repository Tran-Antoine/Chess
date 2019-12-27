from logic import gamelogic
from rendering import board, api, renderers
from player import Player

class ChessGame():

    def __init__(self):
        self.logic = gamelogic.GameLogic()
        self.board = board.ChessBoard(renderers.TkinterRenderer())
        self.player1 = Player.DEFAULT_1
        self.player2 = Player.DEFAULT_2
        
    def set_players(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        
    def start(self):
        print(f"Starting a new game, opposing {self.player1} with {self.player2}")
        self.board.show()
        # self._test_input() # uncomment this to test the rendering system
    
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