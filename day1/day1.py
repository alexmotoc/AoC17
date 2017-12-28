with open('day1_input.txt') as file:
    input = file.read()

# Part 1
sum = 0
for i in range(len(input) - 1):
    if input[i] == input[i + 1]:
        sum += int(input[i])

if input[len(input) - 1] == input[0]:
    sum += int(input[0])

print(sum)

# Part 2
sum = 0
forward = len(input) / 2
for i in range(forward):
    if input[i] == input[i + forward]:
        sum += int(input[i])

for i in range(forward, len(input)):
    if input[i] == input[(i + forward) % len(input)]:
        sum += int(input[i])

print(sum)
