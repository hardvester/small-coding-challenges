from queue_implementation import Queue

class LLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def addNode(self, data):
        self.head = LLNode(data, self.head)

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.level = None

def listOfDepths(node):
    visited = set()
    ll_dict = {}
    queue = Queue()
    node.level = 0
    
    queue.add(node)
    while not queue.isEmpty():
        current_node = queue.remove()
        if current_node.level in ll_dict:
            ll_dict[current_node.level].addNode(current_node.data)
        else:
            ll_dict[current_node.level] = LinkedList(LLNode(current_node.data))

        addNodeToQueueIfNotNone(current_node.left, visited, queue, current_node.level)
        addNodeToQueueIfNotNone(current_node.right, visited, queue, current_node.level)
    return ll_dict

def addNodeToQueueIfNotNone(Node, visited, queue, current_node):
    if Node is not None:
        Node.level = current_node + 1
        queue.add(Node)
        visited.add(Node)


if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B', TreeNode('D'), TreeNode('E')), TreeNode('C'))
    print(listOfDepths(root_node))
    