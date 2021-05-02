# implement a function to check if a binary treeis a binary search tree
from queue_implementation import Queue

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# checking only if the previous value is smaller than the current value
class WrapInt:
    def __init__(self):
        self.data = None

def validate_bst(node, wrapint):
    if node == None:
        return True
    if not validate_bst(node.left, wrapint):
        return False
    if wrapint.data != None and node.data <= wrapint.data:
        return False
    wrapint.data = node.data
    if not validate_bst(node.right, wrapint):
        return False
    return True

if __name__ == '__main__':
    root_node = TreeNode(8)
    root_node.left = TreeNode(4)
    root_node.right = TreeNode(10)
    root_node.left.left = TreeNode(21)
    root_node.left.right = TreeNode(6)
    root_node.right.right = TreeNode(20)
    print(validate_bst(root_node, WrapInt()))