from math import ceil, floor, sqrt
from collections import defaultdict
import numpy as np

print('Address: ')
address = input()

# Part 1
if address == 1:
    min_steps = 0
else:
    square_size = floor(sqrt(address)) if floor(sqrt(address)) % 2 == 0 else ceil(sqrt(address))
    side_start = floor(address / floor(sqrt(address))) * floor(sqrt(address)) + 1
    side_end = ceil(address / floor(sqrt(address))) * floor(sqrt(address)) + 1

    if side_start == side_end:
        mid_point = side_end - square_size / 2
    else:
        mid_point = (side_end + side_start) / 2

    min_steps = floor(square_size / 2) + abs(address - mid_point)

print(int(min_steps))

# Part 2
def turn_left(direction):
    updated = ''

    if direction == 'N':
        updated = 'W'
    elif direction == 'S':
        updated = 'E'
    elif direction == 'E':
        updated = 'N'
    elif direction == 'W':
        updated = 'S'

    return updated

def move_forward(row, col, direction):
    if direction == 'N':
        row, col = row - 1, col
    elif direction == 'S':
        row, col = row + 1, col
    elif direction == 'E':
        row, col = row, col + 1
    elif direction == 'W':
        row, col = row, col - 1

    return row, col

memory = defaultdict(lambda: 0)
memory[(0, 0)] = 1
memory[(0, 1)] = 1
adjacent = [(x, y) for x in xrange(-1, 2) for y in xrange(-1, 2)]
row, col = 0, 1
direction = 'E'
current = 1

while current < address:
    if memory[move_forward(row, col, turn_left(direction))] == 0:
        direction = turn_left(direction)
    row, col = move_forward(row, col, direction)
    for a in adjacent:
        if a != (0, 0):
            memory[(row, col)] += memory[tuple(np.add((row, col), a))]
    current = memory[(row, col)]

print(current)
