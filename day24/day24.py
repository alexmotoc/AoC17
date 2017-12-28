max_length = 0
max_strength = 0
max_strength_longest = 0

def get_strongest_bridge(components, port, length, strength):
    """Returns the weight of the strongest bridge"""
    global max_length
    global max_strength
    global max_strength_longest

    max_strength = max(max_strength, strength)
    max_length = max(max_length, length)

    if max_length == length:
        max_strength_longest = max(max_strength_longest, strength)

    for c in components:
        if not c[2] and (c[0] == port or c[1] == port):
            c[2] = True
            if c[0] == port:
                other_port = c[1]
            else:
                other_port = c[0]
            get_strongest_bridge(components, other_port, length + 1, strength + c[0] + c[1])
            c[2] = False

components = []

with open('day24_input.txt') as file:
    for line in file:
        component = line.split('/')
        first_port = min(int(component[0]), int(component[1]))
        second_port = max(int(component[0]), int(component[1]))
        components.append([first_port, second_port, False])

get_strongest_bridge(components, 0, 0, 0)

# Part 1
print(max_strength)

# Part 2
print(max_strength_longest)