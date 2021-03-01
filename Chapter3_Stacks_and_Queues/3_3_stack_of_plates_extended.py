# in addtion to stack of plates basic we implement the popAt function which
# performs the pop operation on a specific sub stack

from stack_implementation_with_list import Stack
from limited_stack_implementation import LimitedStack

class LimitedStackWithIndexPop(LimitedStack):
    


if __name__ == "__main__":
    limited_stack = LimitedStack()
    limited_stack.push(1)
    limited_stack.push(2)
    limited_stack.pop()
    print(limited_stack.showStacks())
    print(limited_stack.counter)
    print(limited_stack.isEmpty())
    print(limited_stack.peep())



