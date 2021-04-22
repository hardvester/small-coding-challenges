class Queue:
    def __init__(self):
        self.items = []

    def add(self, data):
        self.items.append(data)
    
    def remove(self):
        if self.items == []:
            raise Exception('Queue empty')
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue empty')
        return self.items[0]

