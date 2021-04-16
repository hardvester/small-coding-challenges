# given a directed graph, design an algorith to find out whwther there is a route between two nodes

# storing a graph in a dictionary
class Graph:
    def __init__(self):
        self.nodes = {}

class Node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children




if __name__ == "__main__":
    tree = Node('root', [Node('1st_child'), Node('2nd_child')])
    print(tree.children[0].name)
