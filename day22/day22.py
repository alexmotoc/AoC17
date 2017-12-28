from collections import defaultdict

def turn_left(face):
    """Return the new facing position after turning left"""
    updated = face

    if face == 'N':
        updated = 'W'
    elif face == 'S':
        updated = 'E'
    elif face == 'E':
        updated = 'N'
    elif face == 'W':
        updated = 'S'

    return updated

def turn_right(face):
    """Return the new facing position after turning right"""
    updated = face

    for i in xrange(3):
        updated = turn_left(updated)

    return updated

def reverse(face):
    """Return the new facing position after reversing direction"""
    updated = face

    for i in xrange(2):
        updated = turn_left(updated)

    return updated

def move(face, row, col):
    """Returns the updated coordinates after moving forward
    in the direction the virus is facing"""
    if face == 'N':
        row, col = row - 1, col
    elif face == 'S':
        row, col = row + 1, col
    elif face == 'E':
        row, col = row, col + 1
    elif face == 'W':
        row, col = row, col - 1

    return row, col

with open('day22_input.txt') as file:
    input = file.read()

input = input.split('\n')

# Part 1
grid = defaultdict(lambda: '.')
for r in xrange(len(input)):
    for c in xrange(len(input[r])):
        grid[(r, c)] = input[r][c]

# Start in the center of the grid
row = len(input) // 2
col = len(input[0]) // 2
# Face up (NORTH)
face = 'N'

activity_bursts = 10000
infections = 0

for i in xrange(activity_bursts):
    # Turn in place
    if grid[(row, col)] == '#':
        face = turn_right(face)
        grid[(row, col)] = '.'
    else:
        face = turn_left(face)
        grid[(row, col)] = '#'
        infections += 1
    row, col = move(face, row, col)

print(infections)

# Part 2
grid = defaultdict(lambda: '.')
for r in xrange(len(input)):
    for c in xrange(len(input[r])):
        grid[(r, c)] = input[r][c]

# Start in the center of the grid
row = len(input) // 2
col = len(input[0]) // 2
# Face up (NORTH)
face = 'N'

activity_bursts = 10000000
infections = 0

for i in xrange(activity_bursts):
    if grid[(row, col)] == '#':
        face = turn_right(face)
        grid[(row, col)] = 'F'
    elif grid[(row, col)] == '.':
        face = turn_left(face)
        grid[(row, col)] = 'W'
    elif grid[(row, col)] == 'F':
        face = reverse(face)
        grid[(row, col)] = '.'
    else:
        grid[(row, col)] = '#'
        infections += 1

    row, col = move(face, row, col)

print(infections)