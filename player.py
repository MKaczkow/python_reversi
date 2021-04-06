'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import numpy as np
import board
from config import *


class Player:

    def __init__(self, who_plays):
        self.who_plays = who_plays

    def play(self, board_instance: board.Board):

        if self.who_plays == HUMAN:
            pass
        elif self.who_plays == RANDOM:
            passes = self.random_play(self, board_instance)
        elif self.who_plays == ALGO:
            passes = self.algo_play(self, board_instance)
        else:
            print('Wrong player name!')

        return passes

    def random_play(self, board_instance):
        valid_moves = board_instance.get_moves()
        if len(valid_moves) == 0:
            # which means 0 possible moves, so turn is passed
            return 1

        board_instance.attempt_move(np.choice(valid_moves))
        return 0

    def algo_play(self, board_instance):
        # TODO: algo play using min-max with alpha-beta
        return 1
