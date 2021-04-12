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

    def dequeue(self):
        

    def getOldest(self):
        
        





if __name__ == "__main__":
    pass
