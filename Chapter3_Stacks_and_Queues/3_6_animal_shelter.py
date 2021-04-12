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
        if animal == 'dog':
            self.dogQueue.add(Animal(animal, self.order))
        elif animal == 'cat':
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
            if self.catQueue.peek().order < self.dogQueue.peek().order:
                self.catQueue.remove()
            else:
                self.dogQueue.remove()

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
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('cat')
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('dog') 
    animal_shelter.dequeueAny()
    print(animal_shelter.catQueue.peek())

