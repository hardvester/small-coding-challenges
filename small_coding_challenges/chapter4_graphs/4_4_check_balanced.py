class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(node, extr, level):
    # what am I missing ? I need to keep track of the depth of the tree
    if node is not None:
        if node.left is None and node.right is None:
            if extr['max'] is None or level>extr['max']:
                extr['max'] = level
            if extr['min'] is None or level<extr['min']:
                extr['min'] = level          
        isBalanced(node.left, extr, level+1)
        isBalanced(node.right, extr, level+1)
            
def isBalancedBoolean(node):
    extr = {'max': None, 'min': None}
    isBalanced(node, extr, 0)
    if extr['max'] - extr['min'] > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B'), TreeNode('C', TreeNode('D')))
    print(isBalancedBoolean(root_node))
