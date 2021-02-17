# we will have to implement for this methods that are used for a stack: peep(), pop(), push(), isEmpty()
# we implement the easier approach, i.e. approach where we pre allocate a fixed ammount of memory for each stack


class multiStack:

    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * self.number_of_stacks * self.stack_size
        self.offset = [0] * self.number_of_stacks

    # note the constant time it take to push a value to the stack
    def push(self, value, stack_number):
        if self.offset[stack_number-1] >= self.stack_size:
            raise OverflowError('Stackoverflow')
        self.array[self.stack_size*(stack_number-1) + self.offset[(stack_number-1)]] = value
        self.offset[(stack_number-1)] += 1
    
    def peep(self, stack_number):
        # seems we should shift to the left
        return self.array[(stack_number-1) * self.stack_size + self.offset[stack_number-1]-1]

    def isEmpty(self, stack_number):
        return self.offset[stack_number-1] == True

    def pop(self, stack_number):
        
    
    # this is not good as we should be able to achieve O(1) performance to push a value to the stack, leaving it here for educative purposes
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

if __name__ == "__main__":
    new_multi_stack = multiStack(3)
    new_multi_stack.push(4, 1)
    new_multi_stack.push('a', 2)
    new_multi_stack.push('c', 2)
    new_multi_stack.push('c', 2)

    print(new_multi_stack.peep(2))
        
