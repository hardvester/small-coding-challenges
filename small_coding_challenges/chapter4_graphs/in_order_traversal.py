class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inOrderTraversal(node):
    if node is None:
        return
    print(node.data)
    inOrderTraversal(node.left)
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    inOrderTraversal(node.right)
    print(node.data)

def preOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data)
    inOrderTraversal(node.right)


if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B'), TreeNode('C', TreeNode('D'), TreeNode('E')))
    postOrderTraversal(root_node)
    