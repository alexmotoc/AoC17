import sys
sys.path.append('../day10')

import day10
import networkx as nx
import numpy as np

def to_binary(input):
    """Returns the binary representation of a knot-hash"""
    binary = ''
    for i in range(len(input)):
        binary += format(int(input[i], 16), '04b')
    return binary

input = 'ffayrhll'

# Part 1
used = 0
memory = []

for i in range(128):
    row = input + '-'+ str(i)
    sequence = day10.to_ascii(row) + [17, 31, 73, 47, 23]
    sparse_hash = day10.run_hash(list(range(256)), sequence, 64)
    dense_hash = day10.to_dense_hash(sparse_hash)
    knot_hash = day10.hex_form(dense_hash)
    binary = to_binary(knot_hash)

    # Store the memory into a matrix for part 2 processing
    memory.append([int(b) for b in binary])
    for bit in binary:
        if bit == '1':
            used += 1

print(used)

# Part 2

# Create a graph based on the memory grid and remove the nodes that are free
G = nx.grid_2d_graph(128, 128)
for row in range(len(memory)):
    for col in range(len(memory[i])):
        if memory[row][col] == 0:
            G.remove_node((row, col))

# The regions are just the number of connected components
print(nx.number_connected_components(G))