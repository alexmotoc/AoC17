import numpy as np

input = np.loadtxt('day5_input.txt', dtype='i', delimiter='\n')

current_index = 0
steps = 0

while current_index >= 0 and current_index < len(input):
    previous_index = current_index
    current_index += input[current_index]
    if input[previous_index] >= 3:
        input[previous_index] -= 1
    else:
        input[previous_index] += 1
    steps += 1

print(steps)
