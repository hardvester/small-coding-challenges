class Queue:
    def __init__(self):
        self.items = []

    def add(self, data):
        self.items.append(data)
    
    def remove(self):
        if self.items == []:
            raise Exception('Queue empty')
        self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue empty')
        return self.items[0]

if __name__ == "__main__":
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.remove()
    print(queue.peek())

