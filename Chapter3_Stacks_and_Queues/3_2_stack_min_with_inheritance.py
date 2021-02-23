from stack_implementation_with_list import Stack

class StackMin(Stack):
    def __init__(self):
        self.min = []
        Stack.__init__(self)    

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

    def get_min(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.min[-1]

if __name__ == "__main__":
    stack = StackMin()
    stack.push(5)
    stack.push(6)
    stack.push(4)
    stack.push(4)
    stack.push(5)
    print(stack.get_min())
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()