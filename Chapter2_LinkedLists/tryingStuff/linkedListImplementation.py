# source https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/

class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value
    
    def printNode(self):
        print('Node value is: ', self.value, ' Node pointer is: ', self.next)

    def traverse(self):
        node = self # start from the head node
        while node != None:
            print(node.value) # access the node value
            node = node.next # move on to the next node

headerNode = Node(None, 15)
firstNode = Node(headerNode, 33)
secondNode = Node(firstNode, 44)

secondNode.traverse()
