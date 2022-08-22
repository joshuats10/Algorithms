class ShortestPathDFS:
    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links

    def printPath(self, path):
        result = ''
        for i in range(len(path)):
            result = result + str(path[i])
            if i != len(path) - 1:
                result = result + '->'
        return result

    def DFS(self, start, end, path, shortest, toPrint = False):
        path = path + [start]
        if toPrint:
            print('Current DFS path: ', self.printPath(path))
        if start == end:
            return path
        for node in self.links[start]:
            if node not in path:
                if shortest == None or len(path) < len(shortest):
                    newPath = self.DFS(node, end, path, shortest, toPrint)
                    if newPath != None:
                        shortest = newPath
        return shortest

    def shortestPath_DFS(self, start, end, toPrint = False):
        return self.DFS(start, end, [], None, toPrint)

if __name__ == "__main__":
    nodes = ['A','B','C','D','E','F']
    links = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['D', 'E'],
        'D': ['B', 'E', 'F'],
        'E': ['A'],
        'F': []
    }

    graph = ShortestPathDFS(nodes, links)
    sp_DFS = graph.shortestPath_DFS('A', 'F', toPrint=True)

    print(f'Shortest path found: {graph.printPath(sp_DFS)}')