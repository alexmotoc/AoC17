import numpy as np

def direction_to_tuple(direction):
    """Returns the tuple coordinate offset from the start
    hexagon given a certain direction"""
    return {
        'n'  : (0, -1),
        'ne' : (1, -1),
        'se' : (1, 0),
        's'  : (0, 1),
        'sw' : (-1, 1),
        'nw' : (-1, 0)
    }[direction]

def hex_distance(a, b):
    """Returns the distance between two hexagons in a grid"""
    return (abs(a[0] - b[0])
          + abs(a[0] + a[1] - b[0] - b[1])
          + abs(a[1] - b[1])) / 2

with open('day11_input.txt') as file:
    input = file.read()

start = (0, 0)
current = (0, 0)
furthest_steps = 0

for direction in input.split(','):
    current = tuple(np.add(current, direction_to_tuple(direction)))
    furthest_steps = max(furthest_steps, hex_distance(current, start))

print(hex_distance(current, start))
print(furthest_steps)