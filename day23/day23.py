from collections import defaultdict
from math import sqrt

def is_number(s):
    """Returns true if the input is number, false otherwise"""
    try:
        float(s)
        return True
    except ValueError:
        return False

with open('day23_input.txt') as file:
    input = file.read()

memory = defaultdict(lambda: 0)
instructions = input.split('\n')
line = 0
multiply = 0

while line < len(instructions):
    name = instructions[line].split()[0]
    val1 = instructions[line].split()[1]

    if is_number(val1):
        amount1 = int(val1)
    else:
        amount1 = memory[val1]

    val2 = instructions[line].split()[2]

    if is_number(val2):
        amount2 = int(val2)
    else:
        amount2 = memory[val2]

    if name == 'set':
        memory[val1] = amount2
    elif name == 'sub':
        memory[val1] -= amount2
    elif name == 'mul':
        multiply += 1
        memory[val1] *= amount2
    elif name == 'jnz':
        if amount1 != 0:
            line += amount2
            continue

    line += 1

# Part 1
print(multiply)

# Part 2
# Algorithm counts the number of primes between b and c
def is_prime(number):
    """Returns true if the given number is prime, false otherwise"""
    if number == 0 or number == 1:
        return False
    for d in xrange(2, int(sqrt(number))):
        if number % d == 0:
            return False
    return True

b = 84 * 100 + 100000
c = b + 17000

h = 0
for n in xrange(b, c + 1, 17):
    if not is_prime(n):
        h += 1

print(h)
