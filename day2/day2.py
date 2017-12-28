import numpy as np

input = np.loadtxt('day2_input.txt', dtype='i', delimiter='\t')

checksum = 0
total = 0
for i in range(len(input)):
    # Part 1 checksum
    checksum += max(input[i]) - min(input[i])

    # Part 2 evenly divisible results total
    for j in range(len(input[i]) - 1):
        for k in range(j + 1, len(input[i])):
            max_number = max(input[i, j], input[i, k])
            min_number = min(input[i, j], input[i, k])

            if max_number % min_number == 0:
                total += max_number / min_number

print(checksum)
print(total)
