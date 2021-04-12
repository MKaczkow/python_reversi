'''
Author: Maciej Kaczkowski
26.03-07.04.2021
'''


import numpy as np
import player
import board
from config import *


class Reversi:

    def __init__(self, first_player, second_player):
        self.board = board.Board()
        if first_player == RANDOM:
            self.black_player = player.RandomPlayer(color=BLACK, board_instance=self.board)
        elif first_player == ALGO:
            self.black_player = player.AlgoPlayer(color=BLACK, board_instance=self.board)
        else:
            print("Wrong black player!")

        if second_player == RANDOM:
            self.white_player = player.RandomPlayer(color=WHITE, board_instance=self.board)
        elif second_player == ALGO:
            self.black_player = player.AlgoPlayer(color=WHITE, board_instance=self.board)
        else:
            print("Wrong white player!")

        self.winner = None

    def run(self):
        running = True

        while running:
            temp_state = self.board.board_state

            self.board.playing_next = BLACK
            self.board.get_moves(colour=BLACK)
            _, best_child = self.black_player.play()
            diff_board = abs(best_child.board_state) - abs(self.board.board_state)
            chosen_move = np.where(diff_board == 1)
            self.board.attempt_move(chosen_move, BLACK)
            self.board.playing_next = WHITE
            self.board.attempt_move(self.white_player.play(self.board))

            if temp_state.all() == self.board.board_state.all():
                running = False

        if np.sum(self.board.board_state) > 0:
            self.winner = BLACK
            print(self.board.board_state)
            print("And the winner is...\nBlack!")
        elif np.sum(self.board.board_state) < 0:
            self.winner = WHITE
            print(self.board.board_state)
            print("And the winner is...\nWhite!")
        else:
            print("Draw! Nobody wins!")


def main():
    game = Reversi(ALGO, RANDOM)
    game.run()


if __name__ == '__main__':
    main()
