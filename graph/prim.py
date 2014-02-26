import random
from collections import defaultdict
from heapq import *

class Node(object):
    def __init__(self, val):
        self.val = val
        self.cost = float('inf')
        self.prev = None

    def __repr__(self):
        return "(%s -> %s|%s)" \
            % (self.val, getattr(self.prev, 'val', ''),
                    self.cost) 

def prim2(nodes, edges):
    conn = defaultdict(list)
    for v, u, cost in edges:
        conn[v].append((cost, v, u))
        conn[u].append((cost, u, v))

    mst = []
    used = set(nodes[0])
    usable_edges = conn[nodes[0]][:]
    heapify(usable_edges)

    while usable_edges:
        cost, v, u = heappop(usable_edges)
        if u not in used:
            used.add(u)
            mst.append((v, u, cost))

            for e in conn[u]:
                if e[2] not in used:
                    heappush(usable_edges, e)
    return mst


def prim(G):

    # set up vertices
    V = [Node(x) for x in xrange(1, len(G[1]) + 1)]

    # pick any initial node u0
    #start = V[random.randint(0, len(V) - 1)]
    start = V[0]
    start.cost = 0

    print "Start:", start

    # heap/priority queue, with cost-value keys
    H = []
    for v in V:
        H.append(v)
    # we'll cheat by sorting it.
    H = sorted(H, key=lambda v: v.cost, reverse=True)

    while H:
        v = H.pop()
        for z, weight in enumerate(G[int(v.val) - 1], 1):
            if weight > 0:
                z = V[z - 1]
                print "%d -> %d, weight: %d" % (v.val, z.val, weight)
                if z.cost > weight and v.prev != z:
                    z.cost = weight
                    z.prev = v
                    H = sorted(H, key=lambda v: v.cost, reverse=True)
        print "Sorted again", H

    print V, reduce(lambda x, y: x + y, [v.cost or 0 for v in V])

if __name__ == "__main__":
    G = [[0, 5, 6, 4, 0, 0],
         [5, 0, 1, 2, 0, 0],
         [6, 1, 0, 2, 5, 3],
         [4, 2, 2, 0, 0, 4],
         [0, 0, 5, 0, 0, 4],
         [0, 0, 3, 4, 4, 0]]

    edges = []
    for i, v in enumerate(G, 1):
        for j, e in enumerate(v, 1):
            if e != 0 and i < j:
                edges.append((str(i), str(j), e))

    nodes = list('123456')
    
    print prim2(nodes, edges)


