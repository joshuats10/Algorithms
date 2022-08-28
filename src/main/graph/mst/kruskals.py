"""
    Implementation of Kruskal's minimum spanning tree algorithm
    with Union Find (disjoint set) data structures.

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

from itertools import chain

class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]

    def find(self, i):
        
        root = i
        while(root != self.id[root]):
            root = self.id[root]

        while (i != root):
            next = self.id[i]
            self.id[i] = root
            i = next

        return root

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, i):
        return self.sz[self.find(i)]

    def union(self, x, y):

        if self.connected(x, y):
            return

        root1 = self.find(x)
        root2 = self.find(y)

        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
            self.sz[root1] = 0
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
            self.sz[root2] = 0

class Graph:
    def __init__(self, graph):
        self.graph = graph
        
        self.links = []
        for edge in self.graph:
            self.links.append((edge[0], edge[1]))
        self.nodes = sorted(list(set(chain.from_iterable(self.links))))
        self.N = len(self.nodes)
        self.L = len(self.links)

    def kruskalMST(self):

        edgeCount, mstCost = 0, 0
        mstEdges = [None] * (self.N-1)

        uf = UnionFind(self.L)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        for edge in self.graph:

            if uf.connected(edge[0], edge[1]):
                continue

            uf.union(edge[0], edge[1])
            mstCost += edge[2]
            mstEdges[edgeCount] = (edge[0], edge[1])
            edgeCount += 1

            if uf.size(0) == self.N:
                break

        return mstCost, mstEdges

if __name__ == "__main__":

    grp = [(0,1,10), (0,2,1), (0,3,4), (1,2,3), (2,3,2), (1,4,0), (2,5,8), (3,5,2),\
           (3,6,7), (4,5,1), (4,7,8), (5,6,6), (5,7,9), (6,7,12)]

    mst = Graph(grp)

    mstCost, mstEdges = mst.kruskalMST()
    
    print(f'The minimum spanning tree cost: {mstCost}')
    print(f'and the edges are: {mstEdges}')