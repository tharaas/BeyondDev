# Write a program to find the shortest path between two nodes in a graph.


class graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def bfs(self, start, end, path=None):
        if path is None:
            path = [start]
        else:
            path = path + [start]

        if start == end:
            return path

        short = None
        for node in self.graph[start]:
            if node not in path:
                new = self.bfs(node, end, path)
                if new:
                    if not short or len(new) < len(short):
                        short = new
        return short

    def printGraph(self):
        for node, neighbors in self.graph.items():
            print(node, ":", neighbors)


graph0 = graph()
graph0.addEdge("10", "12")
graph0.addEdge("12", "2")
graph0.addEdge("12", "11")
graph0.addEdge("2", "11")
graph0.addEdge("11", "5")
graph0.addEdge("5", "10")
graph0.printGraph()
print("\nThe shortest path from 10 to 11", graph0.bfs("10", "11"))
