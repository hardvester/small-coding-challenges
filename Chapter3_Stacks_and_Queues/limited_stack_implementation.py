class LimitedStack:
    def __init__(self, capacity=2):    
        self.capacity = capacity
        self.counter = 0
        self.stack_array = []

    def push(self, data):
        if len(self.stack_array) == 0 or self.counter == self.capacity:
            new_stack = Stack()
            new_stack.push(data)
            self.stack_array.append(new_stack)
            self.counter = 1
        else:
            stack = self.getLastStack()
            stack.push(data)
            self.counter += 1
    def pop(self):
        # improving by destructing the last stack?
        if self.counter == 0 and len(self.stack_array) == 1:
            raise Exception('Stack empty')
        elif self.counter == 0:
            self.stack_array.pop()
            stack = self.getLastStack()
            stack.pop()
            self.counter = self.capacity - 1
        else:
            stack = self.getLastStack()
            stack.pop()
            self.counter -= 1
    
    def isEmpty(self):
        return self.stack_array[0].isEmpty()

    def peep(self):
        return self.getLastStack().peep()

    def getLastStack(self):
        return self.stack_array[-1]

    def showStacks(self):
        return self.stack_array