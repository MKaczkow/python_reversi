'''
Author: Maciej Kaczkowski
26.03-07.04.2021
'''


import numpy as np
import board
import minimax
import copy
import random
from config import *
from minimax import *


class AlgoPlayer(object):

    def __init__(self, color,  board_instance, max_depth=MAX_DEPTH):
        self.max_depth = max_depth
        self.minimax_object = Minimax(heuristic_evaluation=0)
        self.color = color
        self.board = board_instance

    def play(self):
        return self.minimax_object.minimax(self.board, None, self.max_depth,
                                       self.color, -self.color)


class RandomPlayer (AlgoPlayer):

    def play(self, board_instance):
        board_instance.get_moves()
        index = np.random.randint(len(board_instance.possible_moves))
        chosen_move = board_instance.possible_moves[index]
        return chosen_move
