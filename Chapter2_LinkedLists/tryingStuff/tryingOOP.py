class car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        classOwner = 'Eduard'

    def printCarProperties(self):
        print('Car value is: ', self.price)

myCar = car('audi', 10000)

myCar.printCarProperties()
print(car.classOwner)
