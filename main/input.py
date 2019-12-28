# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:40:32 2019

@author: willi
"""
import rendering.api as api
import util.vector as vector
import pieces.pieces_position as pmanager
from typing import List

class InputParser():

    def __init__(self):
        pass

    def wait_for_input(self) -> List[vector.Vector2f]:
        raise NotImplementedError()
    
    def to_packet(self, vectors: List[vector.Vector2f], board: pmanager.ImaginaryBoard) -> api.ChessUpdatePacket:
        tile_modifications = {}
        tile_modifications[vectors[0]] = vectors[1]
        # temporarily converting vector to list. Vectors should be used everywhere
        destination_piece = board.piece_at_location(vectors[1].tolist())
        if destination_piece != None:
            tile_modifications[vectors[1]] = Vector2f(-1, -1)
        return api.ChessUpdatePacket(tile_modifications)
        
        
    
        