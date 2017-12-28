with open('day18_input.txt') as file:
    input = file.read()

def is_number(s):
    """Returns true if the input is number, false otherwise"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_value(memory, val):
    """Returns the value from the instructions if it is an integer
    or loads the register from memory (default 0 if it hasn't been initialized yet)"""
    if val in memory:
        amount = memory[val]
    else:
        if is_number(val):
            amount = int(val)
        else:
            amount = 0

    return amount

first_recovered = -1
memory = {}
played = []
instructions = input.split('\n')
line = 0

while line < len(instructions):
    name = instructions[line].split()[0]
    val1 = instructions[line].split()[1]

    amount1 = get_value(memory, val1)

    amount2 = 0
    if len(instructions[line].split()) > 2:
        val2 = instructions[line].split()[2]
        amount2 = get_value(memory, val2)

    if name == 'snd':
        played.append(amount1)
    elif name == 'set':
        memory[val1] = amount2
    elif name == 'add':
        memory[val1] = amount1 + amount2
    elif name == 'mul':
        memory[val1] = amount1 * amount2
    elif name == 'mod':
        memory[val1] = amount1 % amount2
    elif name == 'rcv':
        if len(played) > 0:
            break
    elif name == 'jgz':
        if amount1 > 0:
            line += amount2
            continue

    line += 1

# Part 1
print(played[-1])

# Part 2
sent = 0
memory = [{'p': 0}, {'p': 1}]
queue_sent = [[], []]
waiting = [False, False]
current_program = 0
line = [0, 0]

while True:
    other_program = (current_program + 1) % 2
     
    name = instructions[line[current_program]].split()[0]
    val1 = instructions[line[current_program]].split()[1]

    amount1 = get_value(memory[current_program], val1)

    amount2 = 0
    if len(instructions[line[current_program]].split()) > 2:
        val2 = instructions[line[current_program]].split()[2]
        amount2 = get_value(memory[current_program], val2)

    if name == 'snd':
        if current_program == 1:
            sent += 1
        queue_sent[current_program].append(amount1)
    elif name == 'set':
        memory[current_program][val1] = amount2
    elif name == 'add':
        memory[current_program][val1] = amount1 + amount2
    elif name == 'mul':
        memory[current_program][val1] = amount1 * amount2
    elif name == 'mod':
        memory[current_program][val1] = amount1 % amount2
    elif name == 'rcv':
        # Check if there are any items in the other program's queue
        if len(queue_sent[other_program]):
            memory[current_program][val1] = queue_sent[other_program].pop(0)
            waiting[current_program] = False
        else:
            waiting[current_program] = True
            if len(queue_sent[current_program]):
                current_program = other_program
                waiting[current_program] = False
                line[current_program] -= 1
    elif name == 'jgz':
        if amount1 > 0:
            line[current_program] += amount2 - 1

    # If deadlock is encountered (both are waiting) break loop
    if waiting[0] and waiting[1]:
        break

    if waiting[current_program]:
        if 0 <= line[other_program] < len(instructions):
            current_program = other_program
        else:
            # Deadlock - current is waiting and the other is finished
            break
    else:
        line[current_program] += 1

print(sent)