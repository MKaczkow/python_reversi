'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import numpy as np
from config import HUMAN, RANDOM, MINMAX


class Player:

    def __init__(self, who_plays):
        self.who_plays = who_plays

    def play(self):
        if self.who_plays == HUMAN:
            pass
        elif self.who_plays == RANDOM:
            pass
        elif self.who_plays == MINMAX:
            pass
        else:
            pass
