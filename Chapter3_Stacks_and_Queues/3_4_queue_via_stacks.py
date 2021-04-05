from stack_implementation_with_list import Stack

class MyQueue:
    def __init__(self):
        self.stack_newest = Stack() # original stack
        self.stack_oldest = Stack() # reversed copy
    
    def isEmpty(self):
        return self.stack_newest.isEmpty()

    def add(self, val):
        self.stack_newest.push(val)
    
    def remove(self):
        while True:
            temp = self.stack_newest.peep()
            self.stack_newest.pop()
            if self.stack_newest.isEmpty():
                while True:
                    # basically here we need to copy back the values
                    if self.stack_oldest.isEmpty():
                        break
                    else:
                        self.stack_newest.push(self.stack_oldest.peep())
                        self.stack_oldest.pop()
                break
            else:
                self.stack_oldest.push(temp)
    
    def peek(self):
        while True:
            temp = self.stack_newest.peep()
            # i would need to copy all of the values to stack_oldest just to check the
            # last value and then copy back everything
            return    

if __name__ == "__main__":
    test = MyQueue()
    test.add(1)
    test.add(2)

    test.remove()
    test.remove()

    print(test.isEmpty())






