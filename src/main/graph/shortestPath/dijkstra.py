"""
    Dijkstra's Algorithm with adjacency list representation of the graph

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

import pprint

class Heap:
    def __init__(self):
        self.arr = []

    def heapPush(self, node, dist):
        self.arr.append(([node, dist]))
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
        if rightChild < self.arrSize() and self.arr[smallest][1] > self.arr[leftChild][1]:
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

    def isinHeap(self, node):
         for i in range(self.arrSize()):
            if node == self.arr[i][0]:
                return True 

    def updateDist(self, node, new_dist):
        for i in range(self.arrSize()):
            if node == self.arr[i][0]:
                self.arr[i][1] = new_dist
        
        for i in range((self.arrSize()//2)-1, -1, -1):
            self.heapify(i)

    def isEmpty(self):
        return True if self.arrSize() == 0 else False

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, orig):
        dist = {node: float('inf') for node in self.graph}
        #pred = {node: None for node in self.graph}
        
        dist[orig] = 0
        #pred[orig] = -9999        

        pq = Heap()
        pq.heapPush(orig, 0)

        while not pq.isEmpty():
            current_node, current_dist = pq.pop()

            if current_dist > dist[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    #pred[neighbor] = current_node
                    pq.heapPush(neighbor, new_dist)

        return dist #, pred

if __name__ == "__main__":
    grp = {
        'A':{('C', 3), ('F', 2)},
        'B':{('D', 2), ('E', 5)},
        'C':{('A', 3), ('F', 8), ('D', 7), ('H', 5)},
        'D':{('C', 7), ('H', 4), ('E', 3), ('B', 2)},
        'E':{('H', 6), ('D', 3), ('B', 5), ('F', 1)},
        'F':{('A', 2), ('C', 8), ('H', 5), ('E', 1)},
        'H':{('C', 5), ('D', 4), ('F', 5), ('E', 6)}
    }

    shortestPath = Graph(grp)

    sp = {orig: shortestPath.dijkstra(orig) for orig in grp}
    pprint.pprint(sp)