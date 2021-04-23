from queue_implementation import Queue

class Graph:
    def __init__(self):
        self.nodes = []

    def addNodes(self, nodes):
        self.nodes = self.nodes + nodes

    def printNodes(self):
        for node in self.nodes:
            print(node.name)

    visited = set()
    def isConnectedDFS(self, start_node, target_node):
        if start_node == target_node:
            return True
            print("true")
        self.visited.add(start_node)
        for neighbour in start_node.neighbours:
            if neighbour not in self.visited:
                self.visited.add(neighbour)
                self.isConnected(neighbour, target_node)

    def isConnectedBFS(self, start_node, target_node):
        visited = set()
        if start_node == target_node:
            return True
        queue = Queue()
        queue.add(start_node)
        while not queue.isEmpty():
            current_node = queue.remove()
            for neighbour in current_node.neighbours:
                if neighbour == target_node:
                    return True
                queue.add(neighbour)
            visited.add(neighbour)
        return False

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def addChild(self, neighbour):
        self.neighbours.append(neighbour)