from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        visited = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node = item[1]

            if current_node == goal_node:
                print(current_node, end=" ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                print(current_node, end=" ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                    queue.put((neighbour[0], neighbour[1]))


g = Graph(False)
g.graph = defaultdict(list)
g.add_edge('A', 'B', 22)
g.add_edge('A', 'F', 18)
g.add_edge('A', 'C', 25)

g.add_edge('B', 'A', 20)
g.add_edge('B', 'E', 24)
g.add_edge('B', 'C', 25)

g.add_edge('C', 'A', 20)
g.add_edge('C', 'B', 22)
g.add_edge('C', 'E', 24)
g.add_edge('C', 'D', 19)
g.add_edge('C', 'G', 0)

g.add_edge('D', 'E', 24)
g.add_edge('D', 'C', 23)
g.add_edge('D', 'F', 18)
g.add_edge('D', 'G', 0)

g.add_edge('E', 'B', 22)
g.add_edge('E', 'C', 23)
g.add_edge('E', 'D', 19)
g.add_edge('E', 'F', 18)
g.add_edge('E', 'H', 17)

g.add_edge('F', 'H', 17)
g.add_edge('F', 'A', 20)
g.add_edge('F', 'E', 24)
g.add_edge('F', 'D', 19)
g.add_edge('F', 'G', 0)

g.add_edge('G', 'C', 23)
g.add_edge('G', 'D', 19)
g.add_edge('G', 'F', 18)
g.add_edge('G', 'H', 17)

g.add_edge('H', 'E', 24)
g.add_edge('H', 'F', 18)
g.add_edge('H', 'G', 0)

g.graph

print("The Path needed t be followed is: ")
g.ucs('A', 'G')