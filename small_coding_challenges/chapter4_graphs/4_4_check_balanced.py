class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(node, extremes, arr, level):
    # what am I missing ? I need to keep track of the depth of the tree
    if node is not None:
        if node.left is None and node.right is None:
            arr.append(level)        
        isBalanced(node.left, extremes, arr, level+1)
        isBalanced(node.right, extremes, arr, level+1)
            
def returnFunction(node):
    extremes = {'max': 0, 'min': 0}
    arr = []
    isBalanced(node, extremes, arr, 0)
    return arr
    return extremes
    if extremes['max'] - extremes['min'] > 1:
        return True
    else:
        return False

if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B'), TreeNode('C', TreeNode('D')))
    print(returnFunction(root_node))
