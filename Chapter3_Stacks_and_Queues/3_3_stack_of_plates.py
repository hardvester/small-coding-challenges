from stack_implementation_with_list import Stack

class LimitedStack:
    def __init__(self, capacity=10):    
        self.capacity = capacity
        self.counter = 0
        self.stack_array = []

    def push(self, data):
        if self.counter > self.capacity:
            # I would need to create a new empty stack




