import logic.inputparsers as inputparsers
import pieces.pieces_manager as pieces_manager
import rendering.api as api
import player


class GameLogic():

    def __init__(self, player1, player2):
        self.input_parser = inputparsers.ConsoleInputParser()
        self.board = pieces_manager.ImaginaryBoard(player1.color, player2.color)
        self.p1 = player1
        self.p2 = player2
        self.winner = None
        self.ended = False
        
    def play_turn(self) -> api.ChessUpdatePacket:
        start, destination = self.input_parser.wait_for_input()
        if start is destination is None:
            return api.ChessUpdatePacket.STOP

        packet = self.board.process_move(start, destination, self.p1.color)
        if packet is not api.ChessUpdatePacket.INVALID:
            self.ended = self.is_ended(self.p1, self.p2)
            self.p1, self.p2 = self.p2, self.p1
            return packet
        print("Invalid move, please try again")
        return self.play_turn()

    def is_ended(self, attacker: player.Player, target: player.Player):
        king, = self.board.get_by_name("king", target.color)
        is_check = self.board.is_king_attacked(king)
        can_move = len(self.board.all_absolute_destinations(target.color)) != 0

        if not can_move:
            if is_check:
                self.winner = attacker
            return True
        return False


