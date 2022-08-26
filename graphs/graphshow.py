#import networkx as nx
#import matplotlib.pyplot as plt

#g=nx.read_weighted_edgelist('kruskal_input.txt',create_using=nx.Graph(),nodetype=int)

#print(nx.info(g))
#nx.draw(g)
#plt.show()
#nx.write_edgelist(g,'edgelist2.txt')
import networkx as nx
import sys
import random
import os

# Generate
nvertex = random.randint(100, 200)
G = nx.erdos_renyi_graph(nvertex, 0.5, seed=123, directed=False)
for (u, v, w) in G.edges(data=True):
    w['weight'] = random.randint(0, 10000)

# Print
file_path = 'prim_input.txt'
sys.stdout = open(file_path, "w")

print(nx.number_of_nodes(G), end=" ")
print(nx.number_of_edges(G))
for line in nx.generate_edgelist(G, data=["weight"]):
    print(line)
