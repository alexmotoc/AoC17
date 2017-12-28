from collections import deque

def update_memory(memory, step, insertions):
    """Returns the updated memory after performing a specified
    number of insertions"""
    for i in xrange(1, insertions + 1):
        memory.append(i)
        memory.rotate(-step)

    return memory

def get_value_after_zero(step, insertions):
    """Returns the value following 0 after a number of insertions
    has been performed"""
    zero_position = 0
    insert_position = 0
    value = 1

    for i in xrange(1, insertions + 1):
        insert_position = (insert_position + step + 1) % i

        if insert_position == 0:
            insert_position = i
        if insert_position <= zero_position:
            zero_position += 1
        elif insert_position == zero_position + 1:
            value = i

    return value

step = 304

# Part 1
memory = deque([0])
memory = update_memory(memory, step, 2017)
memory = list(memory)
print(memory[memory.index(2017) + 1])

# Part 2
print(get_value_after_zero(step, 50000000))