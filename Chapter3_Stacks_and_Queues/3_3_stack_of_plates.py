class Stack:
    def __init__(self, capacity=10):    
        self.stack = []
        self.capacity = capacity
        self.counter = 0
        self.stack_number = 0

    def push(self, data):
        if self.counter > self.capacity:
            # I would need to create a new empty stack
        else:
            self.stack.append(data)

