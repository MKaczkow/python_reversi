'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import numpy as np
import player
import board
from config import *


class Reversi:

    def __init__(self, first_player, second_player):
        self.board = board.Board()
        self.black_player = player.Player(first_player)
        self.white_player = player.Player(second_player)
        self.winner = None

    def run(self):
        running = True

        while running:
            passes = 0
            passes += self.black_player.play(self, board_instance=self.board)
            passes += self.white_player.play(self, board_instance=self.board)

            if passes == 2:
                running = False

        print("And the winner is")
        if np.sum(self.board.board_state) > 0:
            self.winner = BLACK
            print("...\n...\n...\nBlack!")
        elif np.sum(self.board.board_state) < 0:
            self.winner = WHITE
            print("...\n...\n...\nWhite!")


def main():
    game = Reversi(RANDOM, RANDOM)
    game.run()


if __name__ == '__main__':
    main()
