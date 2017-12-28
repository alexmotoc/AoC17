from collections import defaultdict

def set_rules(memory, index, state):
    """Returns the write, offset for the new index and next state"""
    write, position, next_state = 1, 1, state

    if memory[index] == 0:
        if state == 'A':
            write, position, next_state = 1, 1, 'B'
        elif state == 'B':
            write, position, next_state = 1, -1, 'C'
        elif state == 'C':
            write, position, next_state = 1, -1, 'D'
        elif state == 'D':
            write, position, next_state = 1, -1, 'E'
        elif state == 'E':
            write, position, next_state = 1, -1, 'A'
        elif state == 'F':
            write, position, next_state = 1, -1, 'E'
    else:
        if state == 'A':
            write, position, next_state = 0, -1, 'E'
        elif state == 'B':
            write, position, next_state = 0, 1, 'A'
        elif state == 'C':
            write, position, next_state = 0, 1, 'C'
        elif state == 'D':
            write, position, next_state = 0, -1, 'F'
        elif state == 'E':
            write, position, next_state = 1, -1, 'C'
        elif state == 'F':
            write, position, next_state = 1, 1, 'A'

    return write, position, next_state

memory = defaultdict(lambda: 0)
steps = 12208951
index = 0
state = 'A'

for i in xrange(steps):
    write, position, state = set_rules(memory, index, state)
    memory[index] = write
    index += position

checksum = 0

for key in memory:
    if memory[key] == 1:
        checksum += 1

# Part 1
print(checksum)