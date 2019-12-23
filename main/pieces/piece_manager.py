# -*- coding: utf-8 -*-
"""
File which binds the files between them.
"""
import knight_bishop as kb
import king_queen as kq
import tower_pawn as tp


class pieceManager():
    """
    """

    def __init__(self):
        self.isCheck = False

    def canMove(self):
        """
        Verify if the piece can move to a case.
        """