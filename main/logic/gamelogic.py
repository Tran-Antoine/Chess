import logic.inputparsers as inputparsers
import pieces.pieces_manager as pieces_manager
import rendering.api as api

class GameLogic():

    def __init__(self, player1, player2, parser_number, renderer):
        self.input_parser = self.load(parser_number, renderer)
        self.board = pieces_manager.ImaginaryBoard(player1, player2)

    def load(self, parser_number, renderer):
        """Loads the input parser according to the id given."""
        if parser_number == 1 or parser_number == 2:
            return inputparsers.ConsoleInputParser()
        return inputparsers.TkinterInputParser(renderer)

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
