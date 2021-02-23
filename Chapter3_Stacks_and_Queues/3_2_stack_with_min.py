class StackMin:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, data):
        if not len(self.min):
            self.min.append(data)
        elif data <= self.min[-1]: 
            self.min.append(data) 
        self.items.append(data)
    
    def pop(self):
        if self.items == []:
            raise Exception('Stack empty')
        if self.peep() == self.min[-1]:
            self.min.pop()
        self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def peep(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.items[len(self.items) - 1]

    def get_min(self):
        if self.isEmpty:
            raise Exception('Stack is empty')
        return self.min[-1]

# trying to implement a stack where I am going to inherit the original stack implementation and extend the way how the stack is treated


if __name__ == "__main__":
    stack = StackMin()
    stack.push(5)
    stack.push(6)
    stack.push(4)
    stack.push(4)
    stack.push(5)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    

    print(stack.get_min())


