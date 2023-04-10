"""
    A* Algorithm with adjacency matrix representation of the graph
    Input = [(from, to, weight), ...] & [(vertex, position_x, position_y), ...]
    *Note that while the input is only in one direction, while actually is a 2-way network. 

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

import heapq
from itertools import chain

class Graph:
    def __init__(self, graph, pos):
        self.links = []
        for edges in graph:
            self.links.append((edges[0], edges[1]))
            self.links.append((edges[1], edges[0]))
        self.nodes = sorted(list(set(chain.from_iterable(self.links))))
        self.N = len(self.nodes)
        self.L = len(self.links)
        self.pos = {i: (x, y) for i, x, y in pos}

        self.cost_matrix = [[None for i in range(self.N)] for j in range(self.N)]
        self.dist_matrix = [[None for i in range(self.N)] for j in range(self.N)]
        for i, j, weight in graph:
            self.cost_matrix[i][j] = weight
            self.cost_matrix[j][i] = weight

        for i in range(self.N):
            for j in range(self.N):
                self.dist_matrix[i][j] = self.calculate_euclidian_dist(i, j)
                self.dist_matrix[j][i] = self.calculate_euclidian_dist(j, i)

    def calculate_euclidian_dist(self, i, j):
        return ((self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2)**0.5
    
    def construct_path(self, pred, dest):
        path = [dest]
        current_node = pred[dest]
        while current_node != -1:
            path.append(current_node)
            current_node = pred[current_node]
        path.reverse()
        return path

    def a_star(self, orig, dest):
        h = [self.dist_matrix[i][dest] for i in range(self.N)]
        min_cost, min_score, pred = [float('inf')]*self.N, [float('inf')]*self.N, [None]*self.N
        min_cost[orig], min_score[orig], pred[orig] = 0, h[orig], -1

        pq = []
        heapq.heappush(pq, (min_score[orig], orig))

        while pq:
            current_score, current_node = heapq.heappop(pq)

            if current_node == dest:
                return self.construct_path(pred, dest), min_cost[dest]

            for neighbor, cost in enumerate(self.cost_matrix[current_node]):
                if cost is not None:
                    new_cost = min_cost[current_node] + cost
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        min_score[neighbor] = new_cost + h[neighbor]
                        pred[neighbor] = current_node
                        heapq.heappush(pq, (new_cost + h[neighbor], neighbor))

        return None, None

if __name__ == "__main__":
    grp = [(0, 2, 3), (0, 5, 2), (1, 3, 2), (1, 4, 5), (2, 3, 7), (2, 5, 8), (2, 6, 5),\
           (3, 4, 3), (3, 6, 4), (4, 5, 1), (4, 6, 6), (5, 6, 5)]
    
    pos = [
        (0,   0,  0),
        (1,   0, 90),
        (2,  20, 30),
        (3,  20, 60),
        (4, -20, 60),
        (5, -20, 30),
        (6,   0, 45),
    ]

    shortestPath = Graph(grp, pos)
    path, min_cost = shortestPath.a_star(0, 1)
    print(path, min_cost)