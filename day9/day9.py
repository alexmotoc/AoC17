with open('day9_input.txt') as file:
    input = file.read()

stack = []
total = 0
cancelled = 0
garbage = False
ignored = False

for i in range(len(input)):
    if len(stack) == 0:
        group = 0

    if not ignored:
        # Check if garbage segment is starting
        if not garbage and input[i] == '<':
            garbage = True
            cancelled -= 1

        if garbage:
            # Check for ignored characters
            if input[i] == '!':
                ignored = True
            elif input[i] == '>':
                garbage = False
            else:
                cancelled += 1
        else:
            # Detect valid groups
            if input[i] == '{':
                stack.append('{')
                group += 1
            elif len(stack) > 0 and input[i] == '}':
                stack.pop()
                total += group
                group -= 1
    else:
        ignored = False

# Part 1
print(total)

# Part 2
print(cancelled)

