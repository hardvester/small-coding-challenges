from stack_implementation_with_list import Stack

class LimitedStack:
    def __init__(self, capacity=10):    
        self.capacity = capacity
        self.counter = 0
        self.stack_array = []

    def LimitedStackPush(self, data):
        if len(self.stack_array) == 0 or self.counter == self.capacity:
            new_stack = Stack()
            new_stack.push(data)
            self.stack_array.append(new_stack)
        else:
            stack = self.stack_array[-1]
            stack.push(data)

    def LimitedStackPop(self):
        




