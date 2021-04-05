from stack_implementation_with_list import Stack

# imput will be a stack, the output will be the same stack but sorted

def sortStack(main_stack):
    helper_stack = Stack()
    helper_stack.push(main_stack.pop())
    
    if helper_stack.peep() > main_stack.peep():
        # remove the top of the main stack
        temp = main_stack.pop()
        while not helper_stack.isEmpty() and helper_stack.peep() > temp:
            # transfered the value from the helper stack to the main stack
            main_stack.push(helper_stack.pop())
            
            if not helper_stack.isEmpty() and helper_stack.peep() > temp:
                continue
            # I will need to count how many items did I push to the main stack
            else:
                helper_stack.push(temp)
        

    
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

    print(sortStack(stack).peep())
