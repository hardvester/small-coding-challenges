from graph_and_nodes import Graph, Node

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
    print(graph.isConnectedBFS(B, E))
