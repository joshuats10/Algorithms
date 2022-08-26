"""
    Prim's minimum spanning tree algorithm implementation
    Note the input is [(orig_edge, dest_edge, weight), ... ]

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

from collections import defaultdict

class Heap:
    def __init__(self):
        self.arr = []

    def heapPush(self, initNode, destNode, dist):
        self.arr.append(((initNode, destNode), dist))
        if self.arrSize() > 1:
            for i in range((self.arrSize()//2)-1, -1, -1):
                self.heapify(i)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def arrSize(self):
        return len(self.arr)

    def heapify(self, i):

        leftChild = 2 * i + 1
        rightChild = 2 * i + 2

        smallest = i

        if leftChild < self.arrSize() and self.arr[smallest][1] > self.arr[leftChild][1]:
            smallest = leftChild
        if rightChild < self.arrSize() and self.arr[smallest][1] > self.arr[rightChild][1]:
            smallest = rightChild

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def pop(self):
        self.swap(0, -1)
        ret = self.arr.pop(-1)
        for i in range((self.arrSize()//2)-1, -1, -1):
            self.heapify(i)
        return ret

    def isEmpty(self):
        return True if self.arrSize() == 0 else False

class Graph:
    def __init__(self, graph):
        self.graph = defaultdict(list)
        for idx, data in enumerate(graph):
            self.graph[data[0]].append((data[1],data[2]))
            self.graph[data[1]].append((data[0],data[2]))
        
        self.N = len(self.graph)

    def addEdges(self, nodeIdx):
        self.visited[nodeIdx] = True
        for neighbor, weight in self.graph[nodeIdx]:
            if not self.visited[neighbor]:
                self.pq.heapPush(nodeIdx, neighbor, weight)

    def lazyPrims(self, start=0):
        self.visited = {node: False for node in self.graph}

        edgeCount, mstCost = 0, 0
        mstEdges = [None] * (self.N-1)

        self.pq = Heap()
        self.addEdges(start)

        while not self.pq.isEmpty() and edgeCount != self.N-1:
            current_edge, dist = self.pq.pop()
    
            if self.visited[current_edge[1]]:
                continue
            
            mstEdges[edgeCount] = current_edge
            edgeCount += 1
            mstCost += dist
            self.addEdges(current_edge[1])

        if edgeCount != self.N-1:
            return None, None

        return mstCost, mstEdges

if __name__ == "__main__":
    grp = [(0,1,10), (0,2,1), (0,3,4), (1,2,3), (2,3,2), (1,4,0), (2,5,8), (3,5,2),\
           (3,6,7), (4,5,1), (4,7,8), (5,6,6), (5,7,9), (6,7,12)]
    
    mst = Graph(grp)

    mstCost, mstEdges = mst.lazyPrims()
    
    print(f'The minimum spanning tree cost: {mstCost}')
    print(f'and the edges are: {mstEdges}')