import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])
print(nx.info(g))
nx.draw(g)
plt.show()

nx.write_edgelist(g,'edgelist.txt')
