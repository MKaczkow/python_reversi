'''
Author: Maciej Kaczkowski
26.03-13.04.2021
'''

import numpy as np
import board


class Minimax(object):

    def __init__(self, heuristic_evaluation=0):
        self.heuristic_evaluation = heuristic_evaluation

    def minimax(self, board_instance: board.Board, parent_board, depth, player, opponent,
                alfa=-np.Infinity, beta=np.Infinity):

        best_child = board_instance
        if depth == 0:
            return self.heuristic_evaluate(board_instance), best_child

        for child in board_instance.get_child_states(colour=player):
            score, new_child = self.minimax(child, board_instance, depth - 1,
                                            opponent, player, -beta, -alfa)
            score = -score

            if score > alfa:
                alfa = score
                best_child = child

            if beta <= alfa:
                break

        return self.heuristic_evaluate(best_child), best_child

    def heuristic_evaluate(self, board_instance):
        fields_values = np.ones_like(board_instance.board_state, dtype=int)
        fields_values[0] += 1
        fields_values[-1] += 1
        fields_values[:, 0] += 1
        fields_values[:, -1] += 1
        fields_values[0][0] += 5
        fields_values[0][-1] += 5
        fields_values[-1][0] += 5
        fields_values[-1][-1] += 5

        result = np.multiply(board_instance.board_state, fields_values)
        result = np.sum(result)
        return result
