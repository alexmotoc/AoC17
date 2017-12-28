from collections import Counter
import networkx as nx

G = nx.DiGraph()

with open('day7_input.txt') as file:
    # Build graph
    for line in file:
        name = line.split()[0]
        weight = line.split()[1].strip('()')

        G.add_node(name, weight=int(weight))

        if '->' in line.split():
            for i in range(3, len(line.split())):
                child = line.split()[i].strip(',')
                G.add_edge(name, child)

# Part 1
ordered = list(nx.topological_sort(G))
print(ordered[0])

# Part 2
# Process leaves first
for node in reversed(ordered):
    # Calculate the total weight of each program
    children_weight = sum(G.node[child]['total_weight'] for child in G.successors(node))
    G.node[node]['total_weight'] = G.node[node]['weight'] + children_weight

    weights = Counter(G.node[child]['total_weight'] for child in G.successors(node))

    offset = 0

    if len(weights) > 1:
        for child in G.successors(node):
            if weights[G.node[child]['total_weight']] == 1:
                offset = abs(list(weights)[0] - list(weights)[1])
                print(G.node[child]['weight'] - offset)
                break

    if offset != 0:
        break

