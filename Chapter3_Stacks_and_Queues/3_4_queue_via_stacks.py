from stack_implementation_with_list import Stack

class MyQueue:
    def __init__(self):
        self.stack_newest = Stack() # original stack
        self.stack_oldest = Stack() # reversed copy
        self.active_stack = self.stack_newest
    
    def isEmpty(self):
        return self.active_stack.isEmpty()

    def add(self, val):
        if self.active_stack == self.stack_oldest:
            self.copy_stack(self.stack_oldest, self.active_stack)   
        self.active_stack.push(val)    
        
    def remove(self):
        if self.active_stack == self.stack_newest:
            self.copy_stack(self.stack_newest, self.stack_oldest)
        self.active_stack.pop()
    
    def peek(self):
        if self.active_stack == self.stack_newest:
            self.copy_stack(self.stack_newest, self.stack_oldest)
        return self.active_stack.peep()    

    def copy_stack(self, original_stack, new_stack):
        while True:
            if original_stack.isEmpty():
                self.active_stack = new_stack
                break      
            else:
                new_stack.push(original_stack.peep())
                original_stack.pop()

if __name__ == "__main__":
    test = MyQueue()
    test.add(1)
    test.add(2)
    test.add(3)
    test.remove()
    test.remove()
    test.remove()
    print(test.peek())






