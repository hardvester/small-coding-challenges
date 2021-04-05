from stack_implementation_with_list import Stack

# imput will be a stack, the output will be the same stack but sorted

def sortStack(main_stack):
    helper_stack = Stack()
    helper_stack.push(main_stack.pop())
    
    if helper_stack.peep() > main_stack.peep():
        
        temp = main_stack.pop()
        count = 0
        while not helper_stack.isEmpty() and helper_stack.peep() > temp:
            count += 1
            main_stack.push(helper_stack.pop())
        helper_stack.push(temp)
        for _ in range(count):
            helper_stack.push(main_stack.pop())
        return helper_stack
    else:
        helper_stack.push(main_stack.pop())


    return main_stack
    # main stack : 1, 2
    # helper stack: 3

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    sorted_stack = sortStack(stack)
    print(sorted_stack.peep())
