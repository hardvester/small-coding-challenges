from stack_implementation_with_list import Stack

class StackMin(Stack):
    def __init__(self):
        self.min = []
        Stack.__init__(self)    

if __name__ == "__main__":
    stack = StackMin()
    stack.push('xx')
    print(stack.peep())