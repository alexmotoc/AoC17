import operator

def get_operator(op):
    return {
        '<'  : operator.lt,
        '<=' : operator.le,
        '==' : operator.eq,
        '!=' : operator.ne,
        '>=' : operator.ge,
        '>'  : operator.gt,
    }[op]

def evaluate_condition(val1, op, val2):
    return get_operator(op)(val1, val2)

def evaluate_instruction(val1, instr, val2):
    if instr == 'inc':
        return val1 + val2
    elif instr == 'dec':
        return val1 - val2

memory = {}
highest_value = 0

with open('day8_input.txt') as file:
    for line in file:
        register = line.split()[0]
        instruction = line.split()[1]
        amount = line.split()[2]
        val1 = line.split()[4]
        oper = line.split()[5]
        val2 = line.split()[6]

        register_value = 0
        if register in memory:
            register_value = memory[register]

        # Default registers to 0 if they haven't been used yet
        if val1 not in memory:
            val1 = 0
        else:
            val1 = memory[val1]

        if evaluate_condition(val1, oper, int(val2)):
            memory[register] = evaluate_instruction(register_value, instruction, int(amount))
            highest_value = max(highest_value, memory[register])

# Part 1
print(max(memory.iteritems(), key=operator.itemgetter(1)))

# Part 2
print(highest_value)