"""
Starting point of the program.
It creates a ChessGame object, then starts the game from it.
"""
from game import ChessGame


def main():
    chosen_interface = int(input("Choose between ConsoleRenderer (1), " +
                                 "FrameTkinterRenderer (2) or CanvasTkinterRenderer (3) >>>"))
    chess_game = ChessGame(chosen_interface)
    chess_game.start()


if __name__ == '__main__':
    main()
