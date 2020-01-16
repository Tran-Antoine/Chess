# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:40:32 2019

@author: willi
"""
import rendering.api as api
import util.vector as vector
import pieces.pieces_manager as pmanager
from typing import List

class InputParser():

    def __init__(self):
        pass

    def wait_for_input(self) -> List[vector.Vector2f]:
        raise NotImplementedError()
