import board
import minimax
import reversi
from config import *
import numpy as np


b = board.Board()

child2 = b.get_child_states(colour=BLACK)
print(child2)
child3 = b.get_child_states(colour=BLACK)
print(child3)
child4 = b.get_child_states(colour=BLACK)
print(child4)
