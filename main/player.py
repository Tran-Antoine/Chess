# -*- coding: utf-8 -*-
"""
File which creates the players.
"""
# todo : have the pieces module import work
import pieces.king_queen as kq
import pieces.knight_bishop as kb
import pieces.tower_pawn as tp
import pieces.pieces_position as pp


class Player():
    """
    Initialize the player.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.coords_letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        """A mettre dehors depuis la classe qui gère les deux joueurs"""
        self.imaginary_board = pp.ImaginaryBoard()
        self.pieces = [kq.King(self.color, [3, 4], self.imaginary_board),
                       kb.Bishop(self.color, [3, 3], self.imaginary_board),
                       kb.Knight(self.color, [3, 1], self.imaginary_board)]

    def start_test(self):
        self.answer = input("Veuillez la case sur laquelle la pièce va bouger: """)
        while self.answer != "q":
            if len(self.answer.split(" ")) == 1:
                for piece in self.pieces:
                    if piece.__str__() == self.answer:
                        print(f"Coords: {self.coords_letter[piece.coords[0] - 1]}{piece.coords[1]}")
            else:
                self.moved = False
                self.before, self.next = self.answer.upper().split(" ")
                self.former_coords = [int(self.coords_letter.index(self.before[0]) + 1), int(self.before[1])]
                self.next_coords = [int(self.coords_letter.index(self.next[0]) + 1), int(self.next[1])]
                for piece in self.pieces:
                    if piece.coords == self.former_coords and self.next_coords in piece.moves_available():
                        piece.move(self.former_coords, self.next_coords)
                        print(f"{piece} est bien allé en {self.next}")
                        self.moved = True
                        break
                if not self.moved:
                    print("Entrée invalide, réessayez.")
            self.answer = input("Veuillez la case sur laquelle la pièce va bouger: """)

    def __str__(self):
        return f"{self.name} (playing {self.color})"


class Color():
    
    def __init__(self, color_name):
        self.color_name = color_name
        
    def __str__(self):
        return self.color_name

    def __eq__(self, other):
        return self.color_name == other.color_name

        

# default constants
Color.WHITE = Color("white")
Color.BLACK = Color("black")

Player.DEFAULT_1 = Player(Color.WHITE, "Player 1")
Player.DEFAULT_1.start_test()
#Player.DEFAULT_2 = Player(Color.BLACK, "Player 2")