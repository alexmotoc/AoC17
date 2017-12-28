import numpy as np
from math import sqrt

def matrix_to_tuple(matrix):
    """Returns a tuple representation of a numpy array"""
    return tuple(map(tuple, matrix))

def get_divisions(pattern, size):
    """Returns a list of divisions based on a given pattern"""
    division = []
    shape = pattern.shape

    for r in xrange(0, shape[0], size):
        for c in xrange(0, shape[1], size):
            division.append(current[r:r+size,c:c+size])

    return division

def update_divisions(division, rules):
    """Returns the updated divisions after the rules have been applied"""
    for i in xrange(len(division)):
        if matrix_to_tuple(division[i]) in rules:
            # Normal division matches
            division[i] = rules[matrix_to_tuple(division[i])]
        elif matrix_to_tuple(np.flipud(division[i])) in rules:
            # Division flipped vertically matches
            division[i] = rules[matrix_to_tuple(np.flipud(division[i]))]
        elif matrix_to_tuple(np.fliplr(division[i])) in rules:
            # Division flipped horizontally matches
            division[i] = rules[matrix_to_tuple(np.fliplr(division[i]))]
        else:
            # Try all rotations (3 rotations of 90 degrees)
            for r in xrange(1, 4):
                if matrix_to_tuple(np.rot90(division[i], r)) in rules:
                    # Rotation matches
                    division[i] = rules[matrix_to_tuple(np.rot90(division[i], r))]
                    break
                elif matrix_to_tuple(np.flipud(np.rot90(division[i], r))) in rules:
                    # Rotation flipped vertically matches
                    division[i] = rules[matrix_to_tuple(np.flipud(np.rot90(division[i], r)))]
                    break
                elif matrix_to_tuple(np.fliplr(np.rot90(division[i], r))) in rules:
                    # Rotation flipped horizontally matches
                    division[i] = rules[matrix_to_tuple(np.fliplr(np.rot90(division[i], r)))]
                    break

    return division

def combine_divisions(division):
    """Return the new pattern after the rules have been applied to every division"""
    size = int(sqrt(len(division)))
    matrix = []

    for r in xrange(size):
        matrix.append([])
        for c in xrange(r * size, (r + 1) * size):
            matrix[len(matrix) - 1].append(division[c])

    return np.array((np.bmat(matrix)))

pattern = '.#./..#/###'

rules = {}
with open('day21_input.txt') as file:
    for line in file:
        rule = line.strip().split(' => ')
        key = np.array([list(row) for row in rule[0].split('/')])
        value = np.array([list(row) for row in rule[1].split('/')])
        rules[matrix_to_tuple(key)] = value

current = np.array([list(row) for row in pattern.split('/')])
iterations = 18

for i in xrange(iterations):
    size = current.shape[0]

    if size % 2 == 0:
        division = get_divisions(current, 2)
    elif size % 3 == 0:
        division = get_divisions(current, 3)

    division = update_divisions(division, rules)
    current = combine_divisions(division)

on = 0
for pixel in np.nditer(current):
    if pixel == '#':
        on += 1

# Part 1
print(on)