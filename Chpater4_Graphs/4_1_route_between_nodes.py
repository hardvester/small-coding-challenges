from Chapter3_Stacks_and_Queues.queue_implementation_with_list import Queue

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
            current_node = queue.pop()
            for neighbour in current_node.neighbors:
                if neighbour == target_node:
                    return True
                queue.add(neighbour)
            visited.add(neighbour)
        return False

    '''
    def breadthfirstsearch(g, start, end):
    if start == end:
        return True
    q = Queue.Queue(len(g.getNodes()))
    start.visited = True
    q.put(start)
    while not q.empty():
        r = q.get()
        if r != None:
            adjacent = r.getAdjacent()
            for i in range(len(adjacent)):
                if adjacent[i].visited == False:
                    if adjacent[i] == end:
                        return True
                    else:
                        q.put(adjacent[i])
                    adjacent[i].visited = True
    return False    
    '''

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
    # print(graph.isConnectedDFS(A,C))
    


    



    
    

