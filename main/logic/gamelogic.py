import logic.inputparsers as inputparsers
import pieces.pieces_manager as pieces_manager
import rendering.api as api


class GameLogic():

    def __init__(self, player1, player2):
        self.input_parser = inputparsers.ConsoleInputParser()
        self.board = pieces_manager.ImaginaryBoard(player1, player2)
        
    def play_turn(self) -> api.ChessUpdatePacket:
        start, destination = self.input_parser.wait_for_input()
        if start is destination is None:
            return api.ChessUpdatePacket.STOP

        packet = self.board.process_move(start, destination)
        if packet is not api.ChessUpdatePacket.INVALID:
            return packet
        print("Invalid move, please try again")
        return self.play_turn()
