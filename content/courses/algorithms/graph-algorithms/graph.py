import networkx as nx
import random
import matplotlib.pyplot as plt

def drawgraph(g, filename):
    f = plt.figure()
    nx.draw(g)
    f.savefig(filename)

def make_graph(N, g):
    nodes = range(N)
    for i in nodes:
        g.add_node(i)
    for i in range(2*N):
        (a, b) = random.sample(nodes, 2)
        g.add_edge(a, b)
    return g

g = make_graph(10, nx.Graph())
drawgraph(g, "undirected.png")

g = make_graph(10, nx.DiGraph())
drawgraph(g, "directed.png")

g = nx.DiGraph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 1)
f = plt.figure()
layout = nx.spring_layout(g)
nx.draw_networkx(g, layout, 
        node_size=2000, 
        font_size=24,
        labels={0: "0:pi=3.14", 1:1, 2:2})
f.savefig("simple.png")
