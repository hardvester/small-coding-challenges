class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.items == []:
            raise Exception('Stack empty')
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def peep(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        return self.items[len(self.items) - 1]


if __name__ == "__main__":
    
    stack = Stack()
    stack.push('xx')
    stack.peep()
    # print(stack.isEmpty())
    # print(stack.peep())
    # stack.pop()
    # stack.pop()


