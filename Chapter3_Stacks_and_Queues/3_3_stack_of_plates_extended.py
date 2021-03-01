# in addtion to stack of plates basic we implement the popAt function which
# performs the pop operation on a specific sub stack

from limited_stack_implementation import LimitedStack

class LimitedStackWithIndexPop(LimitedStack):
    def __init__(self):
        super().__init__()

    def popAt(self):
        return

if __name__ == "__main__":
    limited_stack_with_pop = LimitedStackWithIndexPop()
    limited_stack_with_pop.test()




