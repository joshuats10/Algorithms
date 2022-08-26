"""
    Prim's minimum spanning tree algorithm implementation
    by using indexed priority queue data structure.
    Note the input is [(orig_edge, dest_edge, weight), ... ]

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

from collections import defaultdict
from dependency.indexedPQ import indexedPQ

class Graph:
    def __init__(self, graph):
        self.graph = defaultdict(list)

        for idx, data in enumerate(graph):
            self.graph[data[0]].append((data[1],data[2]))
            self.graph[data[1]].append((data[0],data[2]))

        self.N = len(self.graph)

    def relaxEdgesNode(self, nodeIdx):
        self.visited[nodeIdx] = True
        for neighbor, weight in self.graph[nodeIdx]:
            if self.visited[neighbor]:
                continue
            
            if not self.ipq.contains(neighbor):
                self.ipq.insert(neighbor, (weight, (nodeIdx, neighbor)))
            else:
                self.ipq.decreaseKey(neighbor, (weight, (nodeIdx, neighbor)))

    def eagerPrims(self, start=0):
        self.visited = {node: False for node in self.graph}

        edgeCount, mstCost = 0, 0
        mstEdges = [None] * (self.N-1)

        self.ipq = indexedPQ(self.N)
        self.relaxEdgesNode(start)

        while not self.ipq.isEmpty() and edgeCount != self.N-1:

            destNodeIdx, edge = self.ipq.poll()
    
            mstEdges[edgeCount] = edge[1]
            edgeCount += 1
            mstCost += edge[0]
            self.relaxEdgesNode(destNodeIdx)

        if edgeCount != self.N-1:
            return None, None

        return mstCost, mstEdges

if __name__ == "__main__":
    grp = [(0,1,9), (0,2,0), (0,3,5), (0,5,7),\
           (1,3,-2), (1,4,3), (1,6,4), (2,5,6),\
           (3,5,2), (3,6,3), (4,6,6), (5,6,1)]

    mst = Graph(grp)

    mstCost, mstEdges = mst.eagerPrims()
    
    print(f'The minimum spanning tree cost: {mstCost}')
    print(f'and the edges are: {mstEdges}')