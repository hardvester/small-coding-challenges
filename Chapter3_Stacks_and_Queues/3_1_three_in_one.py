# we will have to implement for this methods that are used for a stack: peep(), pop(), push(), isEmpty()
# we implement the easier approach, i.e. approach where we pre allocate a fixed ammount of memory for each stack


class multiStack:

    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * self.number_of_stacks * self.stack_size

    def push(self, value, stack_number):
        
        
    def index(self, stack_number):
        # stack = 1
        offset = (stack_number * self.stack_size) - 1
        index = 0
        while True:
            if index > self.stack_size-1:
                raise EnvironmentError('Stack number ' + stack_number + ' is full')
            elif self.array[index + offset] is None:
                return index
            index += 1
        

    

if __name__ == "__main__":
    new_multi_stack = multiStack(5)
    print(new_multi_stack.array)
        
