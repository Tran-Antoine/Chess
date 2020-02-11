import logic.inputparsers as inputparsers
import pieces.pieces_manager as pieces_manager
import rendering.api as api

class GameLogic():

    CONTROL_INPUT = [inputparsers.ConsoleInputParser, inputparsers.ConsoleInputParser, inputparsers.TkinterInputParser]

    def __init__(self, player1, player2, parser_number, renderer):
        try:
            self.input_parser = self.CONTROL_INPUT[parser_number - 1]()
        except TypeError:
            self.input_parser = inputparsers.TkinterInputParser(renderer)

        self.board = pieces_manager.ImaginaryBoard(player1, player2)
        
    def play_turn(self) -> api.ChessUpdatePacket:
        start, destination = self.input_parser.wait_for_input()
        print(start, destination)
        if start is destination is None:
            return api.ChessUpdatePacket.STOP
            
        piece = self.board.piece_at_location(start) 

        if (piece is not None) and destination in piece.moves_available(self.board):
            return self.board.process_move(start, destination)
        
        print("Invalid move, please try again")
        return self.play_turn()
