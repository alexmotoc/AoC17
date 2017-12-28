with open('day13_input.txt') as file:
    lines = [line.split(': ') for line in file]

# Build layer -> depth dictionary
layers = {int(layer): int(depth) for layer, depth in lines}

def get_scanner(time, height):
    """Returns the position of the scanner in a layer with a given depth after
    a specified number of picoseconds has passed"""
    # Use triangle wave to determine the position
    offset = time % ((height - 1) * 2)

    if offset > height - 1:
        position = 2 * (height - 1) - offset
    else:
        position = offset

    return position

# Part 1
severity = sum(l * layers[l] for l in layers if get_scanner(l, layers[l]) == 0)
print(severity)

# Part 2 - brute force approach
def get_shortest_delay(layers):
    """Returns the shortest delay that allows the packet to run
    through the firewall without being detected"""
    shortest_delay = 0
    while True:
        severity = sum(1 for l in layers if get_scanner(shortest_delay + l, layers[l]) == 0)
        if severity == 0:
            break
        shortest_delay += 1
    return shortest_delay

print(get_shortest_delay(layers))