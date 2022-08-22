class ShortestPathBFS:
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

    def BFS(self, start, end):
        initPath = [start]
        pathQueue = [initPath]
        while len(pathQueue) != 0:
            tmpPath = pathQueue.pop(0)
            print('Current BFS path:', self.printPath(tmpPath))
            lastNode = tmpPath[-1]
            if lastNode == end:
                return tmpPath
            for nextNode in self.links[lastNode]:
                if nextNode not in tmpPath:
                    newPath = tmpPath + [nextNode]
                    pathQueue.append(newPath)

        return None 

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

    graph = ShortestPathBFS(nodes, links)
    sp_BFS = graph.BFS('A', 'F')

    print(f'Shortest path found: {graph.printPath(sp_BFS)}')