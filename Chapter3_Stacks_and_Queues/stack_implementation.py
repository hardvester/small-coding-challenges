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

    def remove(self):
        self.top = self.top.next
    
    def showTop(self):
        print(self.top.data)
    
    def add(self, data):
        self.top.next = self.top
        self.top.data = data

    def isEmpty(self):
        if self.top.data is None:
            print('isEmpty')

if __name__ == "__main__":
    