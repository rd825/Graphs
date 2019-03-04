"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, start_vertex, visited=None):
        if visited is None:
            visited = []
        visited.append(start_vertex)
        for neighbor in self.vertices[start_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        return visited

    def bfs(self, start_vertex, target):
        queue = Queue()
        visited = []
        queue.enqueue(start_vertex)
        while queue.size() > 0:  # base case
            vertex = queue.dequeue()  # leads to base case
            if vertex not in visited:
                visited.append(vertex)
                if vertex == target:
                    return visited
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)
        print(f'path to {target} vertex not found (BFS)')

    def dfs(self, start_vertex, target):
        stack = Stack()
        visited = []
        stack.push(start_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                if vertex == target:
                    return visited
                for neigbor in self.vertices[vertex]:
                    if neigbor not in visited:
                        stack.push(neigbor)
        print(f'path to {target} vertex not found (DFS)')


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
# Continuing from previous example
# graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
print('\n\nBFT:')
print(graph.bft('0'))
print('\n\nDFT:')
print(graph.dft('0'))
print('\n\nDFT Recursive:')
print(graph.dft_recursive('0'))
print(graph.bfs("0", "1"))
print(graph.dfs("3", "1"))
