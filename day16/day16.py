import string

def spin(programs, size):
    """Returns the updated list of programs after performing a spin"""
    return programs[-size:] + programs[:-size]

def exchange(programs, p1, p2):
    """Returns the updated list of programs after performing an exchange"""
    programs[p1], programs[p2] = programs[p2], programs[p1]
    return programs

def partner(programs, p1, p2):
    """Returns the updated list of programs after performing a partner move"""
    a = programs.index(p1)
    b = programs.index(p2)
    return exchange(programs, a, b)

def dance_move(programs, move):
    """Executes a given dance move on the list of programs"""
    if move[0] == 's':
        programs = spin(programs, int(move[1:]))
    elif move[0] == 'x':
        p1 = int(move[1:].split('/')[0])
        p2 = int(move[1:].split('/')[1])
        programs = exchange(programs, p1, p2)
    elif move[0] == 'p':
        p1 = move[1]
        p2 = move[3]
        programs = partner(programs, p1, p2)

    return programs

def dance(programs, dance_moves, times):
    """Returns the update programs as a string after executing
    the dance a specified number of times"""
    seen = []
    for i in xrange(times):
        if ''.join(programs) in seen:
            return ''.join(seen[times % i])

        seen.append(''.join(programs))
        for move in dance_moves:
            programs = dance_move(programs, move)

    return ''.join(programs)

with open('day16_input.txt') as file:
    input = file.read()

dance_moves = input.split(',')
programs = list(string.ascii_lowercase[:16])

# Part 1
print(dance(programs, dance_moves, 1))

# Part 2
print(dance(programs, dance_moves, 1000000000))