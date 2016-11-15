def minimal_edge(H, V0):
    """pick an edge with the minimal weight 
    from V0 to the rest of the nodes"""

    w_min = None
    e_min = None
    for e in H.E.keys():
        if e[0] in V0 and e[1] not in V0:
            w = H.E[e]["weight"]
            if w_min == None or w < w_min:
                e_min = e
                w_min = w
    return e_min

def prims(G, debug=None):
    "returns a list of edges"
    tree_nodes = set()
    tree_edges = set()

    # start with an arbitrarily picked vertex
    N = len(G.V)
    v = G.V.keys()[0]
    tree_nodes.add(v)

    for i in range(N-1):
        if debug: debug(i, tree_nodes, tree_edges)
        e = minimal_edge(G, tree_nodes)
        if not e:
            print "graph is not fully connected"
            return tree_edges
        tree_nodes.add(e[1])
        tree_edges.add(e)
    if debug: debug(i, tree_nodes, tree_edges)
    return tree_edges

#================================
# Kruskal
#================================

def find_set(partition, v):
    for i,p in enumerate(partition):
        if v in p:
            return i
    return None

def join_sets(partition, i1, i2):
    p1 = partition[i1]
    p2 = partition[i2]
    j1 = min(i1, i2)
    j2 = max(i1, i2)
    partition[j2:j2+1] = [] # remove the later one
    partition[j1:j1+1] = [p1 | p2]

def kruskal(G, debug=None):
    "returns a list of edges"
    # get the edges and short by the weights
    tree_edges = set()
    edges = [e for e in G.E.keys() if e[0] < e[1]]
    edges.sort(key=lambda e: G.E[e]["weight"])
    partition = [set([v]) for v in G.V.keys()]
    for i,e in enumerate(edges):
        if len(partition) == 1:
            break
        i1 = find_set(partition, e[0])
        i2 = find_set(partition, e[1])
        if not i1 == i2:
            join_sets(partition, i1, i2)
            tree_edges.add(e)
            if debug: debug(i, None, tree_edges)
    return tree_edges
