# in addtion to stack of plates basic we implement the popAt function which
# performs the pop operation on a specific sub stack

class Stack:
    def __init__(self):
        self.items = []
        self.top = None
        self.bottom = None

    def push(self, data):
        self.items.append(data)
        self.top = data
        self.bottom = self.items.[0]
    
    def pop(self):
        if self.items == []:
            raise Exception('Stack empty')
        self.items.pop()
        self.top = self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def peep(self):
        if self.isEmpty():
            raise Exception('Stack empty')
        return self.items[len(self.items) - 1]

if __name__ == "__main__":
    print('test')