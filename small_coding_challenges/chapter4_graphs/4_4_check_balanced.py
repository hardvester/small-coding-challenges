# source: https://www.youtube.com/watch?v=nOcFiGl5Vy4

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBalanced(node):
    if balancedHeight(node) > -1:
        return True
    return False

def balancedHeight(node):
    if node is None:
        return 0
    h1 = balancedHeight(node.left)
    h2 = balancedHeight(node.right)

    # this will allow to boild up the information that one
    # of the subtrees is not balanced
    if h1 == -1 or h2 == -1:
        return -1
    if abs(h1-h2) > 1:
        return -1
    # incrementing by one which expresses the level
    if h1 > h2:
        return h1+1
    return h2+1   

'''
def isBalanced(node, extr, level):
    # what am I missing ? I need to keep track of the depth of the tree
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data)
            if extr['max'] is None or level>extr['max']:
                extr['max'] = level
            if extr['min'] is None or level<extr['min']:
                extr['min'] = level
            height_diff = extr['max'] - extr['min']
            if height_diff > 1:
                return False
                # Question: will this return jump out of all of the recursive calls? No.
                # We should calculate the height difference at each step and exit the 
                # function if the height_diff exceeds 1.        
        isBalanced(node.left, extr, level+1)
        isBalanced(node.right, extr, level+1)
            
def isBalancedBoolean(node):
    extr = {'max': None, 'min': None}
    isBalanced(node, extr, 0)
    if extr['max'] - extr['min'] > 1:
        return False
    else:
        return True
'''

if __name__ == '__main__':
    root_node = TreeNode('A', TreeNode('B'), TreeNode('C', TreeNode('D', TreeNode('E',TreeNode('F', TreeNode('G'))))))
    print(isBalanced(root_node))
