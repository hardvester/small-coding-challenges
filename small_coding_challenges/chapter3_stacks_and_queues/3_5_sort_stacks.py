from stack_implementation_with_list import Stack

# imput will be a stack, the output will be the same stack but sorted

def sortStack(main_stack):
    helper_stack = Stack()
    helper_stack.push(main_stack.pop())
    while not main_stack.isEmpty():
        if helper_stack.peep() > main_stack.peep():
            temp = main_stack.pop()
            count = 0
            while not helper_stack.isEmpty() and helper_stack.peep() > temp:
                count += 1
                main_stack.push(helper_stack.pop())
            helper_stack.push(temp)
            for _ in range(count):
                helper_stack.push(main_stack.pop())
        else:
            helper_stack.push(main_stack.pop())
    
    while not helper_stack.isEmpty():
        main_stack.push(helper_stack.pop())
    return main_stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(14)
    stack.push(34)
    stack.push(0)
    stack.push(12)
    sorted_stack = sortStack(stack)
    sorted_stack.pop()
    sorted_stack.pop()

    print(sorted_stack.peep())
