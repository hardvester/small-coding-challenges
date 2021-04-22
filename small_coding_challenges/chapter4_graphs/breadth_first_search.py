# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

# extending the function two find the path between 2 nodes

def dfs(visited, graph, node_a, target_node):
    if node_a not in visited:
        if node_a == target_node:
            print('path exists')
        visited.add(node_a)
        for neighbour in graph[node_a]:
            dfs(visited, graph, neighbour, target_node)

# Driver Code
#dfs(visited, graph, 'C', 'F')

# implement the DFS and graph using the adjaceny list

class Graph:
    def __init__(self):
      self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)


class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    

graph = Graph([Node('A', ['B', 'C']), Node('B', ['C', 'D'])])

# let's implement the DFS on this data structure

def DFS(graph, node):
    visited = set()
    if node not in visited:
        visited.add(node)
        for neighbour in node.children:
            DFS(neighbour)

























    

    


