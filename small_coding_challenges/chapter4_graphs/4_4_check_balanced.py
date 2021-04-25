class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    extremes = {'max': 0, 'min': 0}
    def isBalanced(self, node, extremes, level = 0):
        
        # what am I missing ? I need to keep track of the depth of the tree
        if node is not None:
            if node.left is None and node.right is None:
                if level > self.extremes['max']:
                    self.extremes['max'] = level
                if level < self.extremes['min']:
                    self.extremes['min'] = level

            isBalanced(node.left, extremes, level+1)
            isBalanced(node.right, extremes, level+1)
        
        if self.extremes['max'] - self.extremes['min'] > 1:
            return False
        else:
            return True

if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B', TreeNode('D'), TreeNode('E')), TreeNode('C'))
    print(listOfDepths(root_node))
