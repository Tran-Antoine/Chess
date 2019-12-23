# -*- coding: utf-8 -*-
"""
Main file to launch the game.
"""
import tkinter as tk


class View(tk.Frame):
    """
    The graphical interface of the game.
    """

    def __init__(self, master):
        super().__init__(master)


class Control(tk.Tk):
    """
    """

    def __init__(self):
        super().__init__()


    def choosePiece(self, event):
        """
        Choose the piece on which the mouse is.
        """

    def movePiece(self, event):
        """
        Move the piece onto the next case.
        """

if __name__ == "__main__":
    Control().mainloop()