class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(node, extremes = {'max': 0, 'min': 0}, level = 0):
    
    # what am I missing ? I need to keep track of the depth of the tree
    if node is not None:
        if node.left is None and node.right is None:
            if level > extremes['max']:
                extremes['max'] = level
            if level < extremes['min']:
                extremes['min'] = level

        isBalanced(node.left, extremes, level+1)
        isBalanced(node.right, extremes, level+1)
    
    if extremes['max'] - extremes['min'] > 1:
        return extremes
    else:
        return extremes

if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B', TreeNode('D'), TreeNode('E')), TreeNode('C'))
    print(isBalanced(root_node))
