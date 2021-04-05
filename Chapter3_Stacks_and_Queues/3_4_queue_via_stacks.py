from stack_implementation_with_list import Stack

class MyQueue:
    def __init__(self):
        self.stack_newest = Stack() # original stack
        self.stack_oldest = Stack() # reversed copy
        self.active_stack = self.stack_newest
    
    def isEmpty(self):
        return self.active_stack.isEmpty()

    def add(self, val):
        if (self.stack_newest == self.active_stack):   
            self.stack_newest.push(val)
        else:
            pass
            # copy_stack
    
    def remove(self):
        if self.active_stack == self.stack_oldest:
            if self.active_stack.isEmpty():
                raise Exception('Stack is empty')
            else:
                self.active_stack.pop()
        else:
            pass
            # copy_stack

        while True:
            temp = self.stack_newest.peep()
            self.stack_newest.pop()

    
    def peek(self):
        if self.active_stack == self.stack_newest:
            self.copy_stack(self.stack_newest, self.stack_oldest)
        self.active_stack.peep()    

    def copy_stack(self, original_stack, new_stack):
        while True:
            new_stack.push(original_stack.peep()) 
            original_stack.pop()
            if original_stack.isEmpty():
                self.active_stack = new_stack
                break      

if __name__ == "__main__":
    test = MyQueue()
    test.add(1)
    test.add(2)
    print(test.stack_oldest.peep())
    print(test.peek())






