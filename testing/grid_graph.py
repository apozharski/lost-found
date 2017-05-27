import networkx as nx
import matplotlib.pyplot as plt
import random as rand


G = nx.grid_graph([6,6])

nx.draw_spectral(G)
print(G.edge)
for edge in G.edge:
    G.edge[edge]['weight'] = rand.randint(1,10)
print(G.edge)
plt.show()

