with open('day19_input.txt') as file:
    diagram = file.read().split('\n')[:-1]

letters = []

def update_position(dir, x, y):
    """Returns the updated coordinates depending on the direction of the path"""
    if dir == 'DOWN':
        return x, y + 1
    elif dir == 'UP':
        return x, y - 1
    elif dir == 'LEFT':
        return x - 1, y
    elif dir == 'RIGHT':
        return x + 1, y

def update_direction(dir, diagram, x, y):
    """Returns the updated direction in case a + symbol is encountered"""
    updated_dir = dir

    if direction == 'DOWN' or direction == 'UP':
        if diagram[y][x + 1] == '-':
            updated_dir = 'RIGHT'
        elif diagram[y][x - 1] == '-':
            updated_dir = 'LEFT'
    elif direction == 'LEFT' or direction == 'RIGHT':
        if diagram[y - 1][x] == '|':
            updated_dir = 'UP'
        elif diagram[y + 1][x] == '|':
            updated_dir = 'DOWN'

    return updated_dir

# Consider top left as origin of the system (0, 0)
x = diagram[0].index('|')
y = 0
steps = 0
symbol = diagram[y][x]
direction = 'DOWN'

while symbol != ' ':
    steps += 1
    x, y = update_position(direction, x, y)
    symbol = diagram[y][x]

    # Check if direction needs to be changed
    if symbol == '+':
        direction = update_direction(direction, diagram, x, y)

    if symbol.isalpha():
        letters.append(symbol)

# Part 1
print(''.join(letters))

# Part 2
print(steps)