'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


# configuration file with constans, etc.

# using "reversi convention" - black has first move,
# hence BLACK is Max player, while WHITE is Min player
WHITE = -1
BLACK = 1

# player's codenames
HUMAN = 'human'
RANDOM = 'random'
MINMAX = 'minmax'

# cordinates for better readability
NORTHEAST = (-1, 1)
NORTH = (-1, 0)
NORTHWEST = (-1, -1)
WEST = (0, -1)
SOUTHWEST = (1, -1)
SOUTH = (1, 0)
SOUTHEAST = (1, 1)
EAST = (0, 1)
