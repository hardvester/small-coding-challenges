class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)

def arrayToBinary(array, start, end):

    # I still don't undrstand this part
    if start > end:
        return ''
    mid = (start + end) // 2
    root = Node(array[mid])
    # this respects well the definition of a binary search tree => left < node
    root.left = arrayToBinary(array, start, mid - 1)
    # this respects well the definition of a binary search tree => left > node
    root.right = arrayToBinary(array, mid + 1, end)
    # what happens ? In each recursive call 
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(initiateArrayToBinary(testArray))