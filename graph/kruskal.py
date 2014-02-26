#!/usr/bin/env python

class Node(object):
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.rank = None

    def __repr__(self):
        return "v: %s" % str(self.val)

def makeset(x):
    x.parent = x
    x.rank = 0

def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry: return
    
    if rx.rank > ry.rank:
        ry.parent = rx
    else:
        rx.parent = ry
        if rx.rank == ry.rank:
            ry.rank = ry.rank + 1

def find(x):
    while x != x.parent:
        x = x.parent
    return x

def kruskal(G):
    V = [Node(x) for x in xrange(1, len(G[1]) + 1)]

    for v in V:
        makeset(v)

    E = []
    for i, v in enumerate(G, 1):
        for j, e in enumerate(v, 1):
            if e != 0 and i < j:
                E.append((i, j, e))

    E = sorted(E, key=lambda e: e[2])

    X = []
    for u, v, w in E:
        if find(V[u-1]) != find(V[v-1]):
            X.append((u, v, w))
            union(V[u-1], V[v-1])

    print X


if __name__ == "__main__":

    G = [[0, 5, 6, 4, 0, 0],
         [5, 0, 1, 2, 0, 0],
         [6, 1, 0, 2, 5, 3],
         [4, 2, 2, 0, 0, 4],
         [0, 0, 5, 0, 0, 4],
         [0, 0, 3, 4, 4, 0]]

    kruskal(G)


