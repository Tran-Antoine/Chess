"""
Starting point of the program.
It creates a ChessGame object, then starts the game from it.
"""
from game import ChessGame


def main():
    chess_game = ChessGame()
    chess_game.start()


if __name__ == '__main__':
    main()
