import networkx as nx

G = nx.Graph()

with open('day12_input.txt') as file:
    # Build graph
    for line in file:
        name = line.split()[0]
        G.add_node(name)

        if '<->' in line.split():
            for i in range(2, len(line.split())):
                adjacent = line.split()[i].strip(',')
                G.add_edge(name, adjacent)

# Part 1 - get the number of nodes in the connected component containing 0
print(len(nx.node_connected_component(G, '0')))

# Part 2 - get the number of connected components
print(nx.number_connected_components(G))