from queue_implementation_with_list import Queue

class Animal():
    def __init__(self, type, order):
        self.type = type
        self.order = order

class AnimalShelter:
    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()
        self.order = 0
    
    def enqueue(self, animal):
        # I got stuck on how to add the ordering to the queue
        if animal.type == 'dog':
            self.dogQueue.add(Animal(animal, self.order))
        elif animal.type == 'cat':
            self.catQueue.add(Animal(animal, self.order))
        self.order += 1

    def dequeueAny(self):
        if self.dogQueue.isEmpty():
            self.catQueue.remove()
        elif self.catQueue.isEmpty():
            self.dogQueue.remove()
        elif self.dogQueue.isEmpty() and self.catQueue.isEmpty():
            raise Exception('No more animals in shelter')
        else:
            getOldest.remove()
        
    def getOldest(self):
        if self.dogQueue.peek().order < self.catQueue.peek().order
            return self.dogQueue
        else:
            return self.catQueue

    def dequeueCat(self):
        if self.catQueue.isEmpty():
            raise Exception('No more cats available')
        else:
            self.catQueue.remove()

    def dequeueDog(self):
        if self.dogQueue.isEmpty():
            raise Exception('No more cats available')
        else:
            self.dogQueue.remove()
            

if __name__ == "__main__":
    print('')
