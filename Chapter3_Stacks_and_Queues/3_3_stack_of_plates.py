from stack_implementation_with_list import Stack

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
            print('push 1')
        else:
            stack = self.getLastStack()
            stack.push(data)
            self.counter += 1
            print('push 2')
    def pop(self):
        if self.counter == 0 and len(self.stack_array) == 1:
            raise Exception('Stack empty')
        elif self.counter == 0:
            # this is the built in pop method used for the array
            self.stack_array.pop()
            stack = self.getLastStack()
            stack.pop()
            self.counter = self.capacity - 1
        elif self.counter > 0:
            print('pop')
            stack = self.getLastStack()
            stack.pop()
            self.counter -= 1

    def getLastStack(self):
        return self.stack_array[-1]

    def showStacks(self):
        return self.stack_array
        

if __name__ == "__main__":
    limited_stack = LimitedStack()
    limited_stack.push(1)
    limited_stack.push(2)
    limited_stack.pop()
    print(limited_stack.showStacks())
    print(limited_stack.counter)



