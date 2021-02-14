class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.items == []:
            raise Exception('Stack empty')
        self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def peep(self):
        return self.items[len(self.items) - 1]


if __name__ == "__main__":
    stack = Stack()
    stack.push('xx')
    print(stack.isEmpty())
    print(stack.peep())
    stack.pop()
    stack.pop()


