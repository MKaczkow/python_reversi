'''
Author: Maciej Kaczkowski
26.03-07.04.2021
'''


import numpy as np
import player
import board
import copy
from config import *


class Reversi:

    def __init__(self, first_player, second_player):
        self.board_instance = board.Board()

        if first_player == RANDOM:
            self.black_player = player.RandomPlayer(color=BLACK, board_instance=self.board_instance)
        elif first_player == ALGO:
            self.black_player = player.AlgoPlayer(color=BLACK, board_instance=self.board_instance)
        else:
            print("Wrong black player!")

        if second_player == RANDOM:
            self.white_player = player.RandomPlayer(color=WHITE, board_instance=self.board_instance)
        elif second_player == ALGO:
            self.black_player = player.AlgoPlayer(color=WHITE, board_instance=self.board_instance)
        else:
            print("Wrong white player!")

        self.winner = None
        self.white_wins = 0
        self.black_wins = 0
        self.draws = 0

    def run(self):
        running = True

        while running:
            passes = 0
            self.board_instance.playing_next = BLACK
            self.board_instance.get_moves(colour=BLACK)

            if len(self.board_instance.possible_moves) == 0:
                passes += 1
            else:
                _, best_child = self.black_player.play()
                diff_board = abs(best_child.board_state) - abs(self.board_instance.board_state)
                chosen_move = np.where(diff_board == 1)
                self.board_instance.attempt_move(chosen_move, BLACK)

            self.board_instance.playing_next = WHITE
            self.board_instance.get_moves(colour=WHITE)

            if len(self.board_instance.possible_moves) == 0:
                passes += 1
            else:
                self.board_instance.attempt_move(self.white_player.play(self.board_instance))

            if passes >= 2:
                running = False

        if np.sum(self.board_instance.board_state) > 0:
            self.winner = BLACK
            self.black_wins += 1
            print("And the winner is...\nBlack!")
        elif np.sum(self.board_instance.board_state) < 0:
            self.winner = WHITE
            self.white_wins += 1
            print("And the winner is...\nWhite!")
        else:
            self.winner = None
            self.draws += 1
            print("Draw! Nobody wins!")

    def reset(self):
        self.winner = None
        self.board_instance.reset_board()


def main():
    game = Reversi(ALGO, RANDOM)
    for i in range(100):
        game.run()
        game.reset()
        print("Game nr " + str(i) + " finished")

    print("Black: " + str(game.black_wins))
    print("White: " + str(game.white_wins))
    print("Draws: " + str(game.draws))


if __name__ == '__main__':
    main()
