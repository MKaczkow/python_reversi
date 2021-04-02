'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import numpy as np
from config import *


class Board:

    def __init__(self, board_size=8):
        self.board_state = np.zeros((board_size, board_size), dtype=int)
        self.board_state[3][4] = BLACK
        self.board_state[4][3] = BLACK
        self.board_state[3][3] = WHITE
        self.board_state[4][4] = WHITE
        self.possible_moves = np.array([])
        self.playing_next = BLACK
        self.board_size = board_size

    def get_moves(self) -> 'get list of possible moves':
        if self.playing_next == BLACK:
            player_stones = np.argwhere(self.board_state == BLACK)
        else:
            player_stones = np.argwhere(self.board_state == WHITE)

        while not player_stones.size == 0:
            current_stone = player_stones[-1]
            valid_directions = self.check_directions(current_stone[0], current_stone[1])
            valid_moves = self.check_direction(current_stone[0], current_stone[1], valid_directions)
            np.append(self.possible_moves, valid_moves)
            np.delete(player_stones, -1)

    def look_around(self, x, y) -> "check for opponent's stones in 8 directions":
        '''
        :param x: first coordinate of checked point
        :param y: second coordinate of checked point
        :return: list of tuples representing directions
        '''
        colour = self.board_state[x][y]
        if colour == EMPTY:
            return []
        directions = [NORTHWEST, NORTH, NORTHEAST,
                      WEST, EAST,
                      SOUTHWEST, SOUTH, SOUTHEAST]

        valid_directions = [(x_add, y_add) for (x_add, y_add) in directions
                            if self.board_state[x + x_add][y + y_add] == - colour]

        # TODO: ??dict or enum directions instead of list comprehensions (for readability of return)??
        return valid_directions

    def check_direction(self, x, y, directions) -> "check how much opponent's stones are in each direction":
        colour = self.board_state[x][y]
        valid_moves = np.empty((1, 2), dtype=int)

        for (x_add, y_add) in directions:
            x_temp, y_temp = x, y
            while self.board_state[x_temp + x_add][y_temp + y_add] == -colour:
                x_temp += x_add
                y_temp += y_add

            if self.board_state[x_temp + x_add][y_temp + y_add] == EMPTY:
                valid_moves = np.append(valid_moves, [[x_temp + x_add, y_temp + y_add]], axis=0)

        valid_moves = np.delete(valid_moves, 0, 0)
        return valid_moves

    def heuristic_evaluate(self):
        game_state = self.board_state
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
