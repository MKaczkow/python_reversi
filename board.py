'''
Author: Maciej Kaczkowski
26.03-07.04.2021
'''


import numpy as np
import copy
from config import *


class Board:

    def __init__(self, board_size=8):
        self.board_state = np.zeros((board_size, board_size), dtype=int)
        self.board_state[3, 4] = BLACK
        self.board_state[4, 3] = BLACK
        self.board_state[3, 3] = WHITE
        self.board_state[4, 4] = WHITE
        self.possible_moves = np.empty([1, 2], dtype=int)
        self.playing_next = BLACK
        self.board_size = board_size

    def get_moves(self, colour=None, need_return=False) -> 'get list of possible moves':
        if colour is None:
            colour = self.playing_next

        places = []

        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == colour:
                    places = places + self.look_around(i, j)

        places = list(set(places))
        self.possible_moves = places
        if need_return:
            return places

    def look_around(self, x, y) -> "check for opponent's stones in 8 directions":
        '''
        :param x: first coordinate of checked point
        :param y: second coordinate of checked point
        :return: list of lists representing directions
        '''
        result = []
        colour = self.board_state[x][y]
        if colour == EMPTY:
            return result

        directions = [NORTHWEST, NORTH, NORTHEAST,
                      WEST, EAST,
                      SOUTHWEST, SOUTH, SOUTHEAST]

        for (x_add, y_add) in directions:
            point = self.check_direction(x, y, x_add, y_add)
            if point:
                result.append(point)

        return result

    def check_direction(self, x, y, x_add, y_add) -> "check how much opponent's stones are in given direction":
        '''
        :return: point, where it's possible to place stone
        '''
        x_temp = x + x_add
        y_temp = y + y_add
        colour = self.board_state[x, y]

        while 0 <= x_temp <= 7 and 0 <= y_temp <= 7 and self.board_state[x_temp, y_temp] == -colour:
            x_temp += x_add
            y_temp += y_add
            if 0 <= x_temp <= 7 and 0 <= y_temp <= 7 and self.board_state[x_temp, y_temp] == EMPTY:
                return x_temp, y_temp

    def attempt_move(self, move, colour=None):

        if colour is None:
            colour = self.playing_next

        if move in self.possible_moves:
            self.board_state[move[0], move[1]] = colour
            for i in range(1, 9):
                self.flip(i, move[0], move[1])

    # TODO: enum or dict as directions
    def flip(self, direction, x, y):
        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        elif direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        elif direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        elif direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        elif direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        elif direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        elif direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        elif direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1

        stones_to_flip = []
        i = x + row_inc
        j = y + col_inc

        if i in range(8) and j in range(8) and self.board_state[i, j] == -self.playing_next:
            stones_to_flip = stones_to_flip + [(i, j)]
            i = i + row_inc
            j = j + col_inc
            while i in range(8) and j in range(8) and self.board_state[i, j] == -self.playing_next:
                # search for more pieces to flip
                stones_to_flip = stones_to_flip + [(i, j)]
                i = i + row_inc
                j = j + col_inc
            if i in range(8) and j in range(8) and self.board_state[i, j] == self.playing_next:
                # found a piece of the right color to flip the pieces between
                for pos in stones_to_flip:
                    # flips
                    self.board_state[pos[0], pos[1]] = self.playing_next

    def heuristic_evaluate(self):
        game_state = self.board_state
        fields_values = np.ones_like(game_state, dtype=int)
        fields_values[0] += 1
        fields_values[-1] += 1
        fields_values[:, 0] += 1
        fields_values[:, -1] += 1
        fields_values[0][0] += 5
        fields_values[0][-1] += 5
        fields_values[-1][0] += 5
        fields_values[-1][-1] += 5

        result = np.multiply(game_state, fields_values)
        result = np.sum(result)
        return result

    def get_child_states(self, colour):
        valid_moves = self.get_moves(colour=colour, need_return=True)
        for move in valid_moves:
            new_board = copy.deepcopy(self)
            new_board.attempt_move(move)
            yield new_board
