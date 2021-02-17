# we will have to implement for this methods that are used for a stack: peep(), pop(), push(), isEmpty()
# we implement the easier approach, i.e. approach where we pre allocate a fixed ammount of memory for each stack

class multiStack:

    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * self.number_of_stacks * self.stack_size
        self.offset = [0] * self.number_of_stacks

    # note the constant time it takes to push/peep/pop a value to the stack
    def push(self, value, stack_number):
        if self.offset[stack_number-1] >= self.stack_size:
            raise OverflowError('Stackoverflow')
        self.array[self.stack_size*(stack_number-1) + self.offset[(stack_number-1)]] = value
        self.offset[(stack_number-1)] += 1
    
    def peep(self, stack_number):
        # seems we should shift to the left
        if self.isEmpty(stack_number):
            raise Exception('Stack is empty')
        return self.array[(stack_number-1) * self.stack_size + self.offset[stack_number-1]-1]

    def isEmpty(self, stack_number):
        return self.offset[stack_number-1] == True

    def pop(self, stack_number):
        # treating the case when we try to pop an empty array
        if self.isEmpty(stack_number):
            raise Exception('Stack is empty')
        self.array[(stack_number-1) * self.stack_size + self.offset[stack_number-1]-1] = None
        self.offset[(stack_number-1)] -= 1



if __name__ == "__main__":
    new_multi_stack = multiStack(3)
    new_multi_stack.push(4, 1)
    new_multi_stack.push('a', 2)
    new_multi_stack.push('b', 2)
    new_multi_stack.push('c', 2)

    new_multi_stack.pop(2)
    print(new_multi_stack.peep(2))

        
