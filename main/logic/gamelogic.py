import logic.inputparsers as inputparsers
import pieces.pieces_manager as pieces_manager
import rendering.api as api
import player
from typing import Tuple

class GameLogic():

    def __init__(self, player1, player2, parser_number, renderer):
        self.input_parser = self.load(parser_number, renderer)
        self.board = pieces_manager.ImaginaryBoard(player1, player2)
        self.p1 = player1
        self.p2 = player2
        self.winner = None
        self.ended = False

    def load(self, parser_number, renderer):
        """Loads the input parser according to the id given."""
        if parser_number == 1 or parser_number == 2:
            return inputparsers.ConsoleInputParser()
        return inputparsers.TkinterInputParser(renderer)
     
    def play_turn(self) -> Tuple[api.ChessUpdatePacket, bool]:
      
        start, destination = self.input_parser.wait_for_input()
        if start is destination is None:
            return api.ChessUpdatePacket.STOP, False

        packet, extra_piece_required = self.board.process_move(start, destination, self.p1.color)
        if packet is not api.ChessUpdatePacket.INVALID:
            self.ended = self.is_ended(self.p1, self.p2)
            self.p1, self.p2 = self.p2, self.p1
            return packet, extra_piece_required
        
        print("Invalid move, please try again")
        return self.play_turn()
        
    def add_extra_piece(self):
        input_result = self.input_parser.wait_for_extra_piece()
        return self.board.add_extra_piece(input_result)

    def is_ended(self, attacker: player.Player, target: player.Player):
        king, = self.board.get_by_name("king", target.color)
        is_check = self.board.is_king_attacked(king)
        can_move = len(self.board.all_absolute_destinations(target.color)) != 0

        if not can_move:
            if is_check:
                self.winner = attacker
            return True
        return False
