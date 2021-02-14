# stack uses LIFO (last in first out)
# imagine a stack as a stack of plates
# implementing with a singly linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, top):
        self.top = top

    def pop(self):
        if self.top is None:
            raise Exception('Can\'t pop a node on a empty Stack')
        self.top = self.top.next
    
    def peep(self):
        return self.top.data
    
    def push(self, data):
        self.top.next = self.top
        self.top.data = data

    def isEmpty(self):
        return self.top.data is None
    
if __name__ == "__main__":
    stack = Stack(Node('x'))
    stack.push('3')
    stack.peep()
    stack.isEmpty()

