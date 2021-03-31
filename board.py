'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import numpy as np
from config import WHITE, BLACK


class Board:

    def __init__(self, board_size):
        self.board = np.zeros(board_size, board_size)
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.possible_moves = np.array(1)
        self.playing_next = BLACK

    def get_moves(self) -> 'get list of possible moves':
        if self.playing_next == BLACK:
            player_stones = np.argwhere(self.board == BLACK)
        else:
            player_stones = np.argwhere(self.board == WHITE)

        while not player_stones.size == 0:
            current_stone = player_stones[-1]
            # TODO: check all 8 directions, finish get_moves
            np.append(self.possible_moves, )
            np.delete(player_stones, -1)

    def heuristic_evaluate(self):
        game_state = self.board
        fields_values = np.ones_like(game_state, dtype=int)
        fields_values[0] += 1
        fields_values[-1] += 1
        fields_values[:, 0] += 1
        fields_values[:, -1] += 1
        fields_values[0][0] += 1
        fields_values[0][-1] += 1
        fields_values[-1][0] += 1
        fields_values[-1][-1] += 1

        result = np.multiply(game_state, fields_values)
        result = np.sum(result)
        return result
