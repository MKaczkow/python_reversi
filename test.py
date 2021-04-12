import board
import minimax
import reversi
from config import *
import numpy as np


a = np.zeros((2, 2))
b = np.zeros((2, 2))
a[0, 1] += 1

print(a)
print(b)

c = abs(b - a)
c = list(c)
print(c)

d = np.where(c == 1)

print(list(d))