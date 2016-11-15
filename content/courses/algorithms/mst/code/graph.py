import random
import math
from matplotlib import pyplot
import networkx as nx
import mst

class Graph:
    def __init__(self):
        self.adj = dict()
        self.V = dict()
        self.E = dict()

    def add_node(self, id, data):
        self.V[id] = data
        return self

    def add_directed_edge(self, s, t, data=None):
        if s not in self.adj:
            self.adj[s] = []
        self.adj[s].append(t)
        self.E[(s, t)] = data
        return self

    def add_edge(self, v1, v2, data=None):
        self.add_directed_edge(v1, v2, data)
        self.add_directed_edge(v2, v1, data)

    def edges_from(self, v1):
        result = []
        if v1 in self.adj:
            for v2 in self.adj[v1]:
                result.append((v1, v2))
        return result

    def to_nx(self):
        g = nx.Graph()
        g.add_nodes_from(self.V.keys())
        g.add_edges_from (self.E.keys())
        return g

    def from_nx(self, g):
        for v in g.nodes():
            self.add_node(v, dict())
        for e in g.edges():
            self.add_edge(e[0], e[1], dict())
        return self

    def save(self, filename, pos, highlight_edges=None):
        g = self.to_nx()
        pyplot.figure()
        nx.draw_networkx_nodes(g, pos, node_size=10)
        nx.draw_networkx_edges(g, pos, edge_color="gray", width=0.5)
        if highlight_edges:
            nx.draw_networkx_edges(g, pos, 
                    edgelist=highlight_edges,
                    edge_color="red",
                    width=2.0)

        pyplot.savefig(filename)
        pyplot.close()
        return self

def random_graph(N):
    def distance(p0, p1):
        x = p0[0] - p1[0]
        y = p0[1] - p1[1]
        return math.sqrt(x*x + y*y)

    random.seed(100)
    g = nx.random_geometric_graph(N, 0.125)
    pos = nx.get_node_attributes(g, 'pos')
    H = Graph().from_nx(g)
    for e in H.E.keys():
        H.E[e] = {"weight": distance(pos[e[0]], pos[e[1]])}
    return (H, pos)

(H, pos) = random_graph(200)

def plot(i, V, E):
    print i
    H.save("mst_%03d.png" % i, pos, highlight_edges=E)

def test_prims():
    E = mst.prims(H, debug=plot)

def test_kruskal():
    E = mst.kruskal(H, debug=plot)
    print E

import sys
if sys.argv[1:]:
    if sys.argv[1].startswith("k"):
        test_kruskal()
    else:
        test_prims()
