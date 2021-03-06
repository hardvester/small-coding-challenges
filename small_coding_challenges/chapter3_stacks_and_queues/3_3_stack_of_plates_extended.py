# in addtion to stack of plates basic we implement the popAt function which
# performs the pop operation on a specific sub stack

class Stack:
    def __init__(self):
        # we will be tracking both the bottom and top of the stack
        self.items = []
        self.top = None
        self.bottom = None

    def push(self, data):
        self.items.append(data)
        self.top = data
        self.bottom = self.items[0]
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        removed_item = self.items.pop()
        if self.isEmpty():
            self.top = None
            self.bottom = None
        else:
            self.top = self.items[-1]
        return removed_item
    
    def isEmpty(self):
        return self.items == []

    def peep(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        return self.items[len(self.items) - 1]
    
    def remove_bottom(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        bottom_element = self.items[0]
        self.bottom = self.items[1]
        self.items = self.items[1:]
        return bottom_element
        
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
        if self.counter == 0 and len(self.stack_array) == 1:
            raise Exception('Stack empty')
        elif self.counter == 0:
            removed_item = self.stack_array.pop()
            del self.stack_array[-1]
            stack = self.getLastStack()
            stack.pop()
            self.counter = self.capacity - 1
        else:
            stack = self.getLastStack()
            removed_item = stack.pop()
            self.counter -= 1
        return removed_item

    def pop_at(self, index):
        return self.left_shift(index, True)
    
    def left_shift(self, index, remove_top):
        stack = self.stack_array[index] 
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.isEmpty():
            del self.stack_array[index] 
        elif len(self.stack_array) > index + 1:
            v = self.left_shift(index + 1, False) # 
            stack.push(v)
        return removed_item

    def isEmpty(self):
        return self.stack_array[0].isEmpty()

    def peep(self):
        return self.getLastStack().peep()

    def getLastStack(self):
        return self.stack_array[-1]

    def showStacks(self):
        return self.stack_array

if __name__ == "__main__":
    stack = LimitedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.pop_at(0)
    print(stack.stack_array[0].top)

    
    