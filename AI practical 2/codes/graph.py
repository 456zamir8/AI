from RMP import dict_gn

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph from the dictionary
G = nx.Graph()

# Add edges with weights
for state, neighbors in dict_gn.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(state, neighbor, weight=weight)

# Define the layout
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=8, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_color='red')

plt.title("State Connections and Distances")
plt.show()
