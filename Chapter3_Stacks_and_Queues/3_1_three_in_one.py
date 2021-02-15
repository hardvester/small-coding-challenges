# we will have to implement for this methods that are used for a stack: peep(), pop(), push(), isEmpty()
# we implement the easier approach, i.e. approach where we pre allocate a fixed ammount of memory for each stack


class multiStack:

    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * self.number_of_stacks * self.stack_size

    def push(self, value, stack_number):
        self.array[self.index(stack_number)] = value

    def index(self, stack_number):
        offset = (stack_number - 1) * self.stack_size
        index = 0
        while True:
            if index > self.stack_size-1:
                # HOW TO TREAT THE ERROR
                raise IndexError('Stack number ' + stack_number + ' is full')
            elif self.array[index + offset] is None:
                return index + offset
            index += 1
    
    def peep(self, stack_number):
        

if __name__ == "__main__":
    new_multi_stack = multiStack(3)
    new_multi_stack.push(4, 1)
    new_multi_stack.push('a', 2)
    new_multi_stack.push('c', 2)
    new_multi_stack.push('c', 2)
    new_multi_stack.push('c', 2)

    print(new_multi_stack.array)
        
