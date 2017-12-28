import numpy as np

input = np.loadtxt('day6_input.txt', dtype='i', delimiter='\t')
# Convert list to tuple to be able to use sets for previous encounter detection
input = tuple(input)

states = set()

count = 0
seen = {}

while input not in states:
    states.add(input)
    seen[input] = count
    count += 1

    most_blocks = max(input)
    most_blocks_index = input.index(max(input))

    difference = -1
    # Find out how many elements will receive an extra block
    if len(input) - most_blocks_index <= most_blocks % len(input):
        difference = most_blocks % len(input) - (len(input) - most_blocks_index)

    # Convert tuple to list for processing
    input = list(input)

    # Reset memory with most blocks
    input[most_blocks_index] = 0

    # Update memory blocks
    for i in range(len(input)):
        if (i <= difference) or \
           (i > most_blocks_index and i <= most_blocks_index + most_blocks % len(input)):
            input[i] += 1
        input[i] += most_blocks / len(input)

    input = tuple(input)

print(len(states))
print(count - seen[input])