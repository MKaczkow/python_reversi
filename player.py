'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


from config import *


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
