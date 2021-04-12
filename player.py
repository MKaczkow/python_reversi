'''
Author: Maciej Kaczkowski
26.03-07.04.2021
'''


import numpy as np
import board
from config import *


class Player:

    def __init__(self, who_plays):
        self.who_plays = who_plays

    def play(self, board_instance: board.Board):

        if self.who_plays == RANDOM:
            passes = self.random_play(board_instance)
        elif self.who_plays == ALGO:
            passes = self.algo_play(board_instance)
        else:
            print('Wrong player name!')

        return passes

    def random_play(self, board_instance):
        board_instance.get_moves()
        if len(board_instance.possible_moves) == 0:
            # which means 0 possible moves, so turn is passed
            return 1

        index = np.random.randint(len(board_instance.possible_moves))
        chosen_move = board_instance.possible_moves[index]
        board_instance.attempt_move(chosen_move)
        return 0

    def algo_play(self, board_instance, depth):
        board_instance.get_moves()
        if len(board_instance.possible_moves) == 0:
            # which means 0 possible moves, so turn is passed
            return 1


        return 0
