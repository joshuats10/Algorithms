"""
    Dijkstra's Algorithm with adjacency matrix representation of the graph
    Input = [(from, to, weight), ...] 
    *Note that the input is only in one direction, while actually is a 2-way network. 

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

import pprint
from itertools import chain

class Heap:
    def __init__(self):
        self.arr = []

    def heapPush(self, node, dist):
        self.arr.append((node, dist))
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
        self.links = []
        for edges in graph:
            self.links.append((edges[0], edges[1]))
            self.links.append((edges[1], edges[0]))
        self.nodes = sorted(list(set(chain.from_iterable(self.links))))
        self.N = len(self.nodes)
        self.L = len(self.links)

        self.graph = [[None for i in range(self.N)] for j in range(self.N)]
        for i, j ,weight in graph:
            self.graph[i][j] = weight
            self.graph[j][i] = weight

    def dijkstra(self, orig, returnPred=False):
        dist = [float('inf') for i in range(self.N)]
        pred = [None for i in range(self.N)]
        
        dist[orig] = 0
        pred[orig] = -9999        

        pq = Heap()
        pq.heapPush(orig, 0)

        while not pq.isEmpty():
            current_node, current_dist = pq.pop()

            if current_dist > dist[current_node]:
                continue

            for neighbor, weight in enumerate(self.graph[current_node]):
                if weight is not None:
                    new_dist = current_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        pred[neighbor] = current_node
                        pq.heapPush(neighbor, new_dist)
                else:
                    continue
                    
        if returnPred:
            return dist, pred
        else:
            return dist

if __name__ == "__main__":
    grp = [(0, 2, 3), (0, 5, 2), (1, 3, 2), (1, 4, 5), (2, 3, 7), (2, 5, 8), (2, 6, 5),\
           (3, 4, 3), (3, 6, 4), (4, 5, 1), (4, 6, 6), (5, 6, 5)]

    shortestPath = Graph(grp)

    sp = [shortestPath.dijkstra(orig) for orig in shortestPath.nodes]
    pprint.pprint(sp)