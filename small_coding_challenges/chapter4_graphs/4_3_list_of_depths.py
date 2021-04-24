from queue_implementation import Queue

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.level = None

class LLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def addNodeAtBeginning(self, data):
        self.head = LLNode(data, self.head)

# this algorithm is based on BFS

def isConnectedBFS(self, node):
    visited = set()
    queue = Queue()
    node.level = 0
    queue.add(node)
    while not queue.isEmpty():
        current_node = queue.remove()
        addNodeToQueueIfNotNone(current_node.left, visited, queue, current_node.level)
        addNodeToQueueIfNotNone(current_node.right, visited, queue, current_node.level)
        # how to incorporate the linked list in this problem

def addNodeToQueueIfNotNone(Node, visited, queue, current_node):
    if Node is not None:
        Node.level = current_node + 1
        queue.add(Node)
        visited.add(Node)