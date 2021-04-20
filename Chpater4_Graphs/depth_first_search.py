class Graph:
    def __init__(self):
        self.nodes = []

    def addNodes(self, nodes):
        self.nodes = self.nodes + nodes

    def printNodes(self):
        for node in self.nodes:
            print(node.name)

    def isConnected(self, start_node, target_node):
        visited = set()
        visited.add(start_node)        
        for neighbour in start_node.neighbours:
            if neighbour == target_node:
                return True
            if neighbour not in visited:
                visited.add(neighbour)  
                self.isConnected(neighbour, target_node)

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def addChild(self, neighbour):
        self.neighbours.append(neighbour)

if __name__ == '__main__':
    graph = Graph()
    C = Node('C')
    D = Node('D')
    B = Node('B')
    B.addChild(C)
    B.addChild(D)
    E = Node('E')
    A = Node('A')
    A.addChild(E)
    A.addChild(B)
    graph.addNodes([A,B,C,D,E])
    graph.printNodes()
    print(graph.isConnected(A, D))



    



    
    

